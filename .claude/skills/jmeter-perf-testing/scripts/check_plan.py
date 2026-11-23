#!/usr/bin/env python3
"""Kiểm perf_plan.json + các .jmx đã sinh. In LỖI/CẢNH BÁO, thoát 1 nếu có LỖI.

Kiểm:
  plan  – đủ khoá bắt buộc; id request duy nhất; request nào cũng có "source" dạng file:dòng (đọc từ code SUT thật);
          request nào cũng có ≥ 1 assertion trong assertions[id]; data[].file tồn tại;
          listener 3 plan chính (load/stress/spike) KHÔNG trùng loại; meta.lockout_required → lockout_flow bật,
          CSV lockout khác file và KHÔNG chung user (cột đầu) với CSV chính / không nằm trong CSV chính.
  jmx   – tên file + TestPlan.testname khớp ^<MSSV>_(Smoke|Load|Stress|Soak|Spike)_YYYYMMDD$;
          HTTP sampler nào cũng có assertion con; CSV Data Set trỏ file tồn tại (đường dẫn tương đối theo thư mục .jmx);
          listener trong jmx khớp listeners.<scenario>; 3 plan chính listener (guiclass) không trùng nhau;
          có thread group lockout khi lockout_required (trừ smoke/soak nếu scenario tắt lockout).
Usage: python check_plan.py HW05/perf_plan.json [--jmx-dir HW05/testplans] [--hw-dir HW05]
"""
import argparse
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

TYPES = {"smoke": "Smoke", "load": "Load", "stress": "Stress", "soak": "Soak", "spike": "Spike"}
MAIN = ("load", "stress", "spike")
GUI = {"summary": "SummaryReport", "aggregate": "StatVisualizer", "view_results_tree": "ViewResultsFullVisualizer",
       "response_time_graph": "RespTimeGraphVisualizer", "table": "TableVisualizer"}
ASSERT_TAGS = {"ResponseAssertion", "JSONPathAssertion", "DurationAssertion", "SizeAssertion", "JSR223Assertion"}
SRC = re.compile(r"^[\w./\\-]+\.\w+:\d+(-\d+)?(,\s*[\w./\\-]+\.\w+:\d+(-\d+)?)*$")

errors, warns = [], []


def err(m):
    errors.append(m)


def warn(m):
    warns.append(m)


def first_col(path):
    with open(path, encoding="utf-8", newline="") as fh:
        r = csv.reader(fh)
        next(r, None)
        return {row[0] for row in r if row}


def all_requests(plan):
    out = [("workflow", r) for r in plan.get("workflow", [])]
    for st in plan.get("setup", []):
        out += [("setup", r) for r in st.get("requests", [])]
    out += [("lockout", r) for r in (plan.get("lockout_flow") or {}).get("requests", [])]
    return out


def check_plan(plan, hw):
    for k in ("meta", "workflow", "data", "assertions", "scenarios", "listeners", "thresholds", "review_log", "assumptions"):
        if k not in plan:
            err(f"plan thiếu khoá '{k}'")
    meta = plan.get("meta", {})
    for k in ("mssv", "base"):
        if k not in meta:
            err(f"meta thiếu '{k}'")
    ids = set()
    for where, r in all_requests(plan):
        rid = r.get("id")
        if rid in ids:
            err(f"request id trùng: {rid}")
        ids.add(rid)
        for k in ("id", "label", "method", "path"):
            if k not in r:
                err(f"{where}/{rid}: thiếu '{k}'")
        if not SRC.match(str(r.get("source", ""))):
            err(f"{where}/{rid}: 'source' phải dạng file:dòng (vd server.js:141-157), đang là {r.get('source')!r}")
        if not plan.get("assertions", {}).get(rid):
            err(f"{where}/{rid}: không có assertion (assertions['{rid}'] rỗng)")
    for k in plan.get("assertions", {}):
        if k not in ids:
            warn(f"assertions['{k}'] không ứng với request nào")
    data = {d["id"]: d for d in plan.get("data", [])}
    for d in data.values():
        if not (hw / d["file"]).exists():
            err(f"data/{d['id']}: chưa có file {hw / d['file']} (chạy gen_csv.py)")
    lst = plan.get("listeners", {})
    seen = {}
    for sc in MAIN:
        if sc not in plan.get("scenarios", {}):
            warn(f"chưa có scenario {sc}")
            continue
        types = [x["type"] for x in lst.get(sc, [])]
        if not types:
            err(f"listeners.{sc} rỗng – mỗi plan chính cần ≥ 1 report view")
        for t in types:
            if t not in GUI:
                err(f"listeners.{sc}: loại '{t}' không hỗ trợ")
            if t in seen and seen[t] != sc:
                err(f"listener '{t}' dùng ở cả {seen[t]} và {sc} – 3 plan chính phải khác loại")
            seen.setdefault(t, sc)
    lf = plan.get("lockout_flow") or {}
    if meta.get("lockout_required"):
        if not lf.get("enabled"):
            err("meta.lockout_required = true nhưng lockout_flow chưa bật")
        else:
            ld = data.get(lf.get("data"))
            mains = [d for d in data.values() if d.get("scope", "main") == "main"]
            if not ld:
                err(f"lockout_flow.data '{lf.get('data')}' không có trong data[]")
            elif ld.get("scope") != "lockout":
                err(f"data/{ld['id']}: scope phải là 'lockout'")
            elif (hw / ld["file"]).exists():
                lus = first_col(hw / ld["file"])
                for m in mains:
                    if m["file"] == ld["file"]:
                        err("CSV lockout trùng file với CSV chính")
                    elif (hw / m["file"]).exists() and lus & first_col(hw / m["file"]):
                        err(f"CSV lockout và {m['id']} chung user: {sorted(lus & first_col(hw / m['file']))[:5]}")
    elif not lf.get("enabled"):
        warn("không có luồng lockout (meta.lockout_required = false) – chỉ hợp lệ khi workflow không có login")


def check_jmx(plan, jdir):
    meta = plan["meta"]
    pat = re.compile(rf"^{re.escape(str(meta['mssv']))}_(Smoke|Load|Stress|Soak|Spike)_(\d{{8}})$")
    rev = {v: k for k, v in TYPES.items()}
    files = sorted(jdir.glob("*.jmx"))
    if not files:
        err(f"không có .jmx trong {jdir}")
    main_gui, dates = {}, set()
    for f in files:
        m = pat.match(f.stem)
        if not m:
            err(f"{f.name}: tên không đúng mẫu {meta['mssv']}_<Type>_YYYYMMDD")
            continue
        scen = rev[m.group(1)]
        dates.add(m.group(2))
        try:
            root = ET.parse(f).getroot()
        except ET.ParseError as e:
            err(f"{f.name}: XML lỗi {e}")
            continue
        tp = root.find("./hashTree/TestPlan")
        if tp is None or tp.get("testname") != f.stem:
            err(f"{f.name}: TestPlan.testname ≠ tên file")
        # sampler + hashTree ngay sau nó
        for parent in root.iter("hashTree"):
            kids = list(parent)
            for i, k in enumerate(kids):
                if k.tag == "HTTPSamplerProxy" and k.get("enabled", "true") == "true":
                    sub = kids[i + 1] if i + 1 < len(kids) and kids[i + 1].tag == "hashTree" else None
                    if sub is None or not any(c.tag in ASSERT_TAGS for c in sub):
                        err(f"{f.name}: sampler '{k.get('testname')}' không có assertion")
                if k.tag == "CSVDataSet":
                    fn = next((p.text for p in k if p.get("name") == "filename"), "")
                    if not fn or "${" in fn:
                        warn(f"{f.name}: CSV '{fn}' dùng biến – không kiểm được")
                    elif not (f.parent / fn).exists():
                        err(f"{f.name}: CSV '{fn}' không tồn tại (tính từ {f.parent})")
        guis = sorted({rc.get("guiclass") for rc in root.iter("ResultCollector") if rc.get("enabled", "true") == "true"})
        want = sorted({GUI[x["type"]] for x in plan.get("listeners", {}).get(scen, [])})
        if guis != want:
            err(f"{f.name}: listener {guis} ≠ listeners.{scen} {want}")
        if scen in MAIN:
            main_gui[scen] = set(guis)
        tgs = [t.get("testname", "") for t in root.iter("ThreadGroup")]
        lf_on = (plan.get("lockout_flow") or {}).get("enabled") and plan["scenarios"].get(scen, {}).get("lockout", True)
        if meta.get("lockout_required") and lf_on and not any(n.startswith("Lockout") for n in tgs):
            err(f"{f.name}: thiếu thread group lockout")
        print(f"đã kiểm {f.name}: {len(tgs)} thread group, listener {guis or '—'}")
    sc = list(main_gui)
    for i in range(len(sc)):
        for j in range(i + 1, len(sc)):
            both = main_gui[sc[i]] & main_gui[sc[j]]
            if both:
                err(f"{sc[i]} và {sc[j]} dùng chung listener {sorted(both)}")
    if len(dates) > 1:
        warn(f"các .jmx mang nhiều ngày khác nhau: {sorted(dates)} – YYYYMMDD phải là ngày chạy chính thức của từng plan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", type=Path)
    ap.add_argument("--jmx-dir", type=Path)
    ap.add_argument("--hw-dir", type=Path)
    a = ap.parse_args()
    plan = json.loads(a.plan.read_text(encoding="utf-8"))
    hw = a.hw_dir or a.plan.parent
    check_plan(plan, hw)
    if not errors or a.jmx_dir:
        check_jmx(plan, a.jmx_dir or hw / plan["meta"].get("plan_dir", "testplans"))
    for w in warns:
        print(f"CẢNH BÁO: {w}")
    for e in errors:
        print(f"LỖI: {e}")
    print(f"Tổng: {len(errors)} lỗi, {len(warns)} cảnh báo")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
