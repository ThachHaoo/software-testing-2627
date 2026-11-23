#!/usr/bin/env python3
"""Sinh test plan JMeter (.jmx, JMeter 5.6.x, chỉ phần tử lõi – không cần plugin) từ perf_plan.json.

Mỗi scenario một file: <out>/<MSSV>_<Type>_<YYYYMMDD>.jmx (Type = Smoke|Load|Stress|Soak|Spike).
YYYYMMDD = NGÀY CHẠY CHÍNH THỨC, truyền bằng --date (bắt buộc; không tự lấy ngày hôm nay).

Cấu trúc sinh ra:
  TestPlan
  ├─ HTTP Request Defaults (protocol/host/port từ meta.base) + Header Manager (Content-Type: application/json)
  ├─ setUp Thread Group / mục setup[]: 1 thread, loops = số dòng CSV, CSV Data Set riêng (vd đăng ký user)
  ├─ Thread Group chính / mục scenarios.<s>.groups[] (stage = thread group có delay + duration)
  │    CSV Data Set (data scope "main") → workflow[]: request once_per_vu nằm trong Once Only Controller,
  │    think_before_ms = timer con của sampler (chạy TRƯỚC sampler đó), extractor JSON, assertion theo assertions[id]
  ├─ Thread Group lockout (nếu lockout_flow.enabled và scenarios.<s>.lockout = true), CSV user riêng
  └─ Listener theo listeners.<s> – KHÔNG ghi file; bằng chứng: mở .jmx bằng GUI, listener → Browse… jtl chính thức → chụp

Usage: python gen_jmx.py HW05/perf_plan.json --date 20261125 [--scenario load ...] [--out HW05/testplans] [--hw-dir HW05]
"""
import argparse
import json
import os
import sys
import zlib
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

TYPES = {"smoke": "Smoke", "load": "Load", "stress": "Stress", "soak": "Soak", "spike": "Spike"}
LISTENERS = {  # type -> (guiclass, tên hiển thị)
    "summary": ("SummaryReport", "Summary Report"),
    "aggregate": ("StatVisualizer", "Aggregate Report"),
    "view_results_tree": ("ViewResultsFullVisualizer", "View Results Tree"),
    "response_time_graph": ("RespTimeGraphVisualizer", "Response Time Graph"),
    "table": ("TableVisualizer", "View Results in Table"),
}
SAVE_FIELDS = [("time", 1), ("latency", 1), ("timestamp", 1), ("success", 1), ("label", 1), ("code", 1),
               ("message", 1), ("threadName", 1), ("dataType", 1), ("encoding", 0), ("assertions", 1),
               ("subresults", 1), ("responseData", 0), ("samplerData", 0), ("xml", 0), ("fieldNames", 1),
               ("responseHeaders", 0), ("requestHeaders", 0), ("responseDataOnError", 0),
               ("saveAssertionResultsFailureMessage", 1), ("assertionsResultsToSave", None), ("bytes", 1),
               ("sentBytes", 1), ("url", 1), ("threadCounts", 1), ("idleTime", 1), ("connectTime", 1)]


def s(name, v):
    return f'<stringProp name="{name}">{escape(str(v))}</stringProp>'


def b(name, v):
    return f'<boolProp name="{name}">{"true" if v else "false"}</boolProp>'


def el(tag, gui, test, name, props, children="", enabled=True):
    """Phần tử + hashTree con."""
    return (f'<{tag} guiclass="{gui}" testclass="{test}" testname={quoteattr(name)} enabled="{str(enabled).lower()}">'
            f'{"".join(props)}</{tag}><hashTree>{children}</hashTree>')


def args_empty():
    return ('<elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" '
            'testclass="Arguments" testname="User Defined Variables"><collectionProp name="Arguments.arguments"/></elementProp>')


def header_manager(name, headers):
    items = "".join(f'<elementProp name="" elementType="Header">{s("Header.name", k)}{s("Header.value", v)}</elementProp>'
                    for k, v in headers.items())
    return el("HeaderManager", "HeaderPanel", "HeaderManager", name,
              [f'<collectionProp name="HeaderManager.headers">{items}</collectionProp>'])


def http_defaults(base):
    return el("ConfigTestElement", "HttpDefaultsGui", "ConfigTestElement", "HTTP Request Defaults", [
        '<elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" '
        'testclass="Arguments" testname="User Defined Variables"><collectionProp name="Arguments.arguments"/></elementProp>',
        s("HTTPSampler.domain", base["host"]), s("HTTPSampler.port", base["port"]),
        s("HTTPSampler.protocol", base.get("protocol", "http")), s("HTTPSampler.contentEncoding", "UTF-8"),
        s("HTTPSampler.connect_timeout", base.get("connect_timeout_ms", 5000)),
        s("HTTPSampler.response_timeout", base.get("response_timeout_ms", 30000)),
    ])


def csv_dataset(d, jmx_dir, hw_dir):
    rel = os.path.relpath((hw_dir / d["file"]).resolve(), jmx_dir.resolve()).replace("\\", "/")
    share = {"all": "shareMode.all", "group": "shareMode.group", "thread": "shareMode.thread"}[d.get("share", "all")]
    return el("CSVDataSet", "TestBeanGUI", "CSVDataSet", f"CSV {d['id']} ({Path(d['file']).name})", [
        s("filename", rel), s("fileEncoding", "UTF-8"), s("variableNames", ",".join(d["columns"])),
        b("ignoreFirstLine", True), s("delimiter", ","), b("quotedData", True),
        b("recycle", d.get("recycle", True)), b("stopThread", d.get("stop_thread", False)), s("shareMode", share),
    ])


def timer(t):
    if not t:
        return ""
    kind = t.get("type", "constant")
    if kind == "constant":
        return el("ConstantTimer", "ConstantTimerGui", "ConstantTimer", f"Think {t['ms']} ms", [s("ConstantTimer.delay", t["ms"])])
    if kind == "uniform":
        return el("UniformRandomTimer", "UniformRandomTimerGui", "UniformRandomTimer",
                  f"Think {t['min']}–{t['max']} ms", [s("ConstantTimer.delay", t["min"]), s("RandomTimer.range", t["max"] - t["min"])])
    if kind == "gaussian":
        return el("GaussianRandomTimer", "GaussianRandomTimerGui", "GaussianRandomTimer",
                  f"Think {t['ms']}±{t['dev']} ms", [s("ConstantTimer.delay", t["ms"]), s("RandomTimer.range", t["dev"])])
    raise ValueError(f"timer type '{kind}'")


def assertion(a, i):
    t = a["type"]
    if t in ("code", "contains", "equals_body", "not_contains"):
        field = "Assertion.response_code" if t == "code" else "Assertion.response_data"
        val = a.get("equals") if t == "code" else a.get("text")
        ttype = {"code": 8, "equals_body": 8, "contains": 16, "not_contains": 16 | 4}[t]
        name = a.get("name") or {"code": f"Code = {val}", "contains": f"Body chứa '{val}'",
                                 "not_contains": f"Body không chứa '{val}'", "equals_body": "Body = …"}[t]
        return el("ResponseAssertion", "AssertionGui", "ResponseAssertion", name, [
            f'<collectionProp name="Asserion.test_strings">{s(str(zlib.crc32(f"{val}#{i}".encode())), val)}</collectionProp>',
            s("Assertion.custom_message", a.get("message", "")), s("Assertion.test_field", field),
            b("Assertion.assume_success", False), f'<intProp name="Assertion.test_type">{ttype}</intProp>',
        ])
    if t == "json":
        has_val = "value" in a
        return el("JSONPathAssertion", "JSONPathAssertionGui", "JSONPathAssertion",
                  a.get("name") or (f"JSON {a['path']} = {a['value']}" if has_val else f"JSON {a['path']} tồn tại"), [
                      s("JSON_PATH", a["path"]), s("EXPECTED_VALUE", a.get("value", "")),
                      b("JSONVALIDATION", has_val), b("EXPECT_NULL", False), b("INVERT", a.get("invert", False)),
                      b("ISREGEX", a.get("regex", False))])
    if t == "duration":
        return el("DurationAssertion", "DurationAssertionGui", "DurationAssertion", a.get("name") or f"≤ {a['ms']} ms",
                  [s("DurationAssertion.duration", a["ms"])])
    raise ValueError(f"assertion type '{t}'")


def extractor(x):
    if x.get("type", "json") != "json":
        raise ValueError("chỉ hỗ trợ extractor json")
    return el("JSONPostProcessor", "JSONPostProcessorGui", "JSONPostProcessor", f"Lấy {x['var']} ← {x['path']}", [
        s("JSONPostProcessor.referenceNames", x["var"]), s("JSONPostProcessor.jsonPathExprs", x["path"]),
        s("JSONPostProcessor.match_numbers", x.get("match", "1")), s("JSONPostProcessor.defaultValues", x.get("default", "NOT_FOUND")),
    ])


def sampler(r, asserts, auth_header):
    body = r.get("body")
    if isinstance(body, (dict, list)):
        body = json.dumps(body, ensure_ascii=False)
    props = []
    if body is not None:
        props += [b("HTTPSampler.postBodyRaw", True),
                  '<elementProp name="HTTPsampler.Arguments" elementType="Arguments"><collectionProp name="Arguments.arguments">'
                  f'<elementProp name="" elementType="HTTPArgument">{b("HTTPArgument.always_encode", False)}'
                  f'{s("Argument.value", body)}{s("Argument.metadata", "=")}</elementProp></collectionProp></elementProp>']
    else:
        props += ['<elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" '
                  'testclass="Arguments" testname="User Defined Variables"><collectionProp name="Arguments.arguments"/></elementProp>']
    props += [s("HTTPSampler.domain", ""), s("HTTPSampler.port", ""), s("HTTPSampler.protocol", ""),
              s("HTTPSampler.path", r["path"]), s("HTTPSampler.method", r["method"].upper()),
              b("HTTPSampler.follow_redirects", False), b("HTTPSampler.auto_redirects", False),
              b("HTTPSampler.use_keepalive", True), b("HTTPSampler.DO_MULTIPART_POST", False),
              s("TestPlan.comments", f"nguồn: {r.get('source', '?')}")]
    kids = timer(r.get("think_before_ms"))
    if r.get("auth"):
        kids += header_manager("Authorization", {"Authorization": auth_header})
    kids += "".join(extractor(x) for x in r.get("extract", []))
    kids += "".join(assertion(a, i) for i, a in enumerate(asserts))
    return el("HTTPSamplerProxy", "HttpTestSampleGui", "HTTPSamplerProxy", r["label"], props, kids)


def requests_tree(reqs, plan):
    auth = plan["meta"].get("auth_header", "Bearer ${token}")
    out, once = "", ""
    for r in reqs:
        x = sampler(r, plan.get("assertions", {}).get(r["id"], []), auth)
        if r.get("once_per_vu"):
            once += x
        else:
            if once:
                out += el("OnceOnlyController", "OnceOnlyControllerGui", "OnceOnlyController", "Một lần mỗi VU", [], once)
                once = ""
            out += x
    if once:
        out += el("OnceOnlyController", "OnceOnlyControllerGui", "OnceOnlyController", "Một lần mỗi VU", [], once)
    return out


def thread_group(name, g, children, setup=False):
    loops = g.get("loops", -1)
    dur = g.get("duration_s")
    scheduler = dur is not None
    lc = (f'<elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" '
          f'testclass="LoopController" testname="Loop Controller">{b("LoopController.continue_forever", False)}'
          f'{s("LoopController.loops", loops)}</elementProp>')
    props = [s("ThreadGroup.on_sample_error", g.get("on_error", "continue")), lc,
             s("ThreadGroup.num_threads", g["threads"]), s("ThreadGroup.ramp_time", g.get("ramp_s", 1)),
             b("ThreadGroup.scheduler", scheduler), s("ThreadGroup.duration", dur if scheduler else ""),
             s("ThreadGroup.delay", g.get("delay_s", 0) if scheduler else ""), b("ThreadGroup.same_user_on_next_iteration", True)]
    if setup:
        return el("SetupThreadGroup", "SetupThreadGroupGui", "SetupThreadGroup", name, props, children)
    return el("ThreadGroup", "ThreadGroupGui", "ThreadGroup", name, props, children)


def listener(lst, plan_name):
    gui, title = LISTENERS[lst["type"]]
    cfg = "".join(f"<{k}>{v}</{k}>" if v is None else f"<{k}>{'true' if v else 'false'}</{k}>" for k, v in SAVE_FIELDS)
    cfg = cfg.replace("<assertionsResultsToSave>None</assertionsResultsToSave>", "<assertionsResultsToSave>0</assertionsResultsToSave>")
    # Không ghi filename: jtl chính thức (-l) là nguồn duy nhất; listener chỉ để mở GUI → Browse jtl → chụp (tránh CSV trùng jtl)
    errs = lst.get("errors_only", False)
    name = title + (" (chỉ lỗi)" if errs else "")
    return el("ResultCollector", gui, "ResultCollector", name, [
        b("ResultCollector.error_logging", errs),
        f'<objProp><name>saveConfig</name><value class="SampleSaveConfiguration">{cfg}</value></objProp>',
        s("filename", "")])


def build(plan, scen, date, jmx_dir, hw_dir):
    meta = plan["meta"]
    sc = plan["scenarios"][scen]
    name = f"{meta['mssv']}_{TYPES[scen]}_{date}"
    data = {d["id"]: d for d in plan.get("data", [])}
    body = http_defaults(meta["base"]) + header_manager("Header JSON", {"Content-Type": "application/json"})
    for i, st in enumerate(plan.get("setup", []), 1):
        d = data[st["data"]]
        rows = sum(1 for _ in open(hw_dir / d["file"], encoding="utf-8")) - 1
        kids = csv_dataset({**d, "recycle": False, "stop_thread": True}, jmx_dir, hw_dir) + requests_tree(st["requests"], plan)
        body += thread_group(f"setUp {i} – {st.get('name', st['data'])} ({rows} dòng)", {"threads": 1, "loops": rows}, kids, setup=True)
    main_csv = "".join(csv_dataset(d, jmx_dir, hw_dir) for d in plan.get("data", []) if d.get("scope", "main") == "main")
    for i, g in enumerate(sc["groups"], 1):
        label = g.get("name") or f"Nhóm {i}"
        body += thread_group(f"{TYPES[scen]} – {label} ({g['threads']} VU)", g, main_csv + requests_tree(plan["workflow"], plan))
    lf = plan.get("lockout_flow") or {}
    if lf.get("enabled") and sc.get("lockout", True):
        d = data[lf["data"]]
        g = {"threads": lf.get("threads", 1), "ramp_s": lf.get("ramp_s", 1), "loops": lf.get("loops", 1),
             "delay_s": lf.get("delay_s", 0), "duration_s": lf.get("duration_s")}
        if g["duration_s"] is None:
            g.pop("duration_s")
        body += thread_group("Lockout – user riêng, cố ý sai", g, csv_dataset(d, jmx_dir, hw_dir) + requests_tree(lf["requests"], plan))
    body += "".join(listener(x, name) for x in plan.get("listeners", {}).get(scen, []))
    tp = el("TestPlan", "TestPlanGui", "TestPlan", name, [
        s("TestPlan.comments", f"Sinh bởi gen_jmx.py từ perf_plan.json – scenario {scen}"),
        b("TestPlan.functional_mode", False), b("TestPlan.tearDown_on_shutdown", True),
        b("TestPlan.serialize_threadgroups", False), args_empty()], body)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<jmeterTestPlan version="1.2" properties="5.0" jmeter="5.6.3">'
           f'<hashTree>{tp}</hashTree></jmeterTestPlan>\n')
    return name, xml


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", type=Path)
    ap.add_argument("--date", required=True, help="YYYYMMDD = ngày chạy chính thức")
    ap.add_argument("--scenario", action="append", choices=list(TYPES), help="mặc định: mọi scenario có trong plan")
    ap.add_argument("--out", type=Path, help="thư mục .jmx (mặc định <hw-dir>/<meta.plan_dir|testplans>)")
    ap.add_argument("--hw-dir", type=Path)
    a = ap.parse_args()
    if not (len(a.date) == 8 and a.date.isdigit()):
        raise SystemExit("--date phải dạng YYYYMMDD")
    plan = json.loads(a.plan.read_text(encoding="utf-8"))
    hw = a.hw_dir or a.plan.parent
    out = a.out or hw / plan["meta"].get("plan_dir", "testplans")
    out.mkdir(parents=True, exist_ok=True)
    for scen in a.scenario or [k for k in TYPES if k in plan["scenarios"]]:
        name, xml = build(plan, scen, a.date, out, hw)
        (out / f"{name}.jmx").write_text(xml, encoding="utf-8")
        print(f"ĐÃ SINH {out / (name + '.jmx')}")


if __name__ == "__main__":
    main()
