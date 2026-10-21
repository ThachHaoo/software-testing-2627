#!/usr/bin/env python3
"""
Sinh bảng dữ kiện cho report chính HW02 từ <feature>/testcases.json, bugs/BUG-xx.md, ai-outputs và git.

Script KHÔNG dùng AI và không viết lời giải thích: chỉ thay nội dung giữa các marker
  <!-- REPORT:<feature>:<khối>:START --> ... <!-- REPORT:<feature>:<khối>:END -->
trong file report. Marker nào không có trong report thì bỏ qua.

Khối: scope, req, assum, vars, parts, min, bva, exec, bugs.

Cách dùng (từ gốc repo):
  python tools/report_tables.py HW02 A_FR01 --report HW02/23120255_HW02_Report.md
  python tools/report_tables.py HW02 A_FR01 --print exec      # in một khối ra màn hình
"""
import argparse
import glob
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

POINTS = ["LB-1", "LB", "LB+1", "NOM", "UB-1", "UB", "UB+1", "MIN_UI", "MAX_UI"]
MAX_IDS = 4      # số mã TC tối đa hiện trong ô "TC phủ"
SAMPLE = 3       # số case mẫu mỗi suite ở bảng minimum set


def show(v):
    """Giá trị nhập: cùng quy ước với render_md.py của skill (rỗng → `''`, khoảng trắng đầu/cuối → ␣)."""
    if not isinstance(v, str):
        return v
    if v == "":
        return "`''` (rỗng)"
    if v != v.strip():
        return "`" + v.replace(" ", "␣").replace("	", "⇥") + "`"
    return v


def cell(s):
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def short(tc):
    return tc.split("-")[-1]


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(cell(x) for x in r) + " |" for r in rows]
    return "\n".join(out)


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else ""


def aid(a):
    m = re.match(r"(A\d+)", a)
    return m.group(1) if m else a[:4]


def all_cases(d):
    return [c for s in d["suites"] for c in s["cases"]]


def counts(cases):
    st = Counter(c.get("status") or "Not Run" for c in cases)
    return {"design": len(cases), "pass": st["Pass"], "fail": st["Fail"], "blocked": st["Blocked"],
            "run": st["Pass"] + st["Fail"],
            "notrun": len(cases) - st["Pass"] - st["Fail"] - st["Blocked"]}


# ---------- khối ----------

def b_scope(ctx):
    return "> " + ctx["d"]["meta"]["scope"] + f"\n\n*Nguồn: `{ctx['rel']}` → `meta.scope` (nguyên văn).*"


def b_req(ctx):
    rows = [(r["id"], r["text"]) for r in ctx["d"]["requirements"]]
    return table(["Mã", "Nội dung"], rows) + f"\n\n*Nguồn: `{ctx['rel']}` → `requirements` ({len(rows)} mục).*"


def assumption_history(ctx):
    """Mã giả định → nguồn gốc: xuất hiện lần đầu ở bản AI đóng băng (ai-outputs) hay ở một commit
    (so theo giờ), rồi các commit làm nội dung khác bản đầu."""
    import datetime as dt
    feat, final = ctx["feat"], {aid(a): a for a in ctx["d"]["meta"]["assumptions"]}
    frz = []
    for f in sorted(glob.glob(str(ctx["hw"] / "appendix" / "ai-outputs" / f"{feat}_step*.json"))):
        m = re.search(r"_step(\d+)_(\d{8})-(\d{4})(\d{2})?", f)
        try:
            when = dt.datetime.strptime(m.group(2) + m.group(3) + (m.group(4) or "00"), "%Y%m%d%H%M%S")
            frz.append((when, int(m.group(1)), {aid(a): a for a in json.load(open(f, encoding="utf-8"))["meta"].get("assumptions", [])}))
        except Exception:
            pass
    path = f"{ctx['hw'].name}/{feat}/testcases.json"
    hist = {}
    for line in git("log", "--reverse", "--format=%h|%cI", "--", path).split():
        h, ts = line.split("|")
        try:
            o = json.loads(git("show", f"{h}:{path}"))
        except json.JSONDecodeError:
            continue
        when = dt.datetime.fromisoformat(ts).replace(tzinfo=None)
        for k, v in ((aid(a), a) for a in o["meta"].get("assumptions", [])):
            lst = hist.setdefault(k, [])
            if not lst or lst[-1][2] != v:
                lst.append((when, h, v))
    res = {}
    for k, text in final.items():
        f0 = next(((w, st, a[k]) for w, st, a in frz if k in a), None)
        c0 = hist.get(k, [None])[0]
        if f0 and (c0 is None or f0[0] <= c0[0]):
            origin, base = f"AI nháp bước {f0[1]}", f0[2]
        elif c0:
            origin, base = f"Không có trong bản AI đóng băng trước đó; thêm ở `{c0[1]}`", c0[2]
        else:
            res[k] = "?"
            continue
        changed = [h for w, h, v in hist.get(k, []) if v != base]
        res[k] = origin + ("; giữ nguyên" if base == text else "; đổi ở " + ", ".join(f"`{c}`" for c in changed)
                           + " (commit cuối = bản hiện tại)")
    return res


def b_assum(ctx):
    hist = assumption_history(ctx)
    rows = [(*(x.strip() for x in a.split(":", 1)), hist.get(aid(a), "")) if ":" in a else (aid(a), a, hist.get(aid(a), ""))
            for a in ctx["d"]["meta"]["assumptions"]]
    return table(["Mã", "Nội dung (nguyên văn, gồm ghi chú chốt)", "Nguồn gốc (ai-outputs + git)"], rows) + \
        f"\n\n*Nguồn: `{ctx['rel']}` → `meta.assumptions` (bản HEAD); cột cuối so với `appendix/ai-outputs/{ctx['feat']}_step*.json` và `git log -- {ctx['feat']}/testcases.json`.*"


def b_vars(ctx):
    io = {"input": "Vào", "output": "Ra"}
    rows = [(v["id"], v["name"], io.get(v["io"], v["io"]), v["type"], v["constraint"], v.get("note", ""))
            for v in ctx["d"]["domain"]["variables"]]
    n = Counter(v["io"] for v in ctx["d"]["domain"]["variables"])
    return table(["Mã", "Biến", "Vào/Ra", "Kiểu", "Ràng buộc (đặc tả)", "Ghi chú"], rows) + \
        f"\n\n*{n['input']} biến vào, {n['output']} biến ra. Cột \"Nguồn\" (tên trường, dòng code) bỏ cho gọn — xem `{ctx['feat']}/testcases.md` mục Bước 1.*"


def b_parts(ctx):
    var = {v["id"]: v["name"] for v in ctx["d"]["domain"]["variables"]}
    cov = {}
    for c in all_cases(ctx["d"]):
        for ec in c.get("covers", []):
            cov.setdefault(ec, []).append(c["id"])
    rows = []
    for p in ctx["d"]["domain"]["partitions"]:
        ids = cov.get(p["id"], [])
        tc = ", ".join(short(x) for x in ids[:MAX_IDS]) + (f" … (+{len(ids) - MAX_IDS})" if len(ids) > MAX_IDS else "")
        rows.append((p["id"], f"{p['variable']} {var.get(p['variable'], '')}", p["class"], "Có" if p["valid"] else "Không", len(ids), tc or "—"))
    parts = ctx["d"]["domain"]["partitions"]
    nv = sum(1 for p in parts if p["valid"])
    miss = [p["id"] for p in parts if p["id"] not in cov]
    return table(["EC", "Biến", "Lớp tương đương", "Hợp lệ", "Số TC phủ", "TC phủ (số cuối mã TC-xx)"], rows) + \
        f"\n\n*{len(parts)} lớp: {nv} hợp lệ, {len(parts) - nv} không hợp lệ. Lớp chưa có TC phủ: {', '.join(miss) or 'không có'}. " \
        f"Cột \"Hướng dẫn\", \"Ghi chú\" và danh sách TC phủ đầy đủ: `{ctx['feat']}/testcases.md` mục Bước 2, Bước 3a.*"


def b_min(ctx):
    out = []
    for s in ctx["d"]["suites"]:
        if not s["id"].startswith("TS-DOM"):
            continue
        cols = s.get("columns", [])
        rows = [(c["id"], c["title"], ", ".join(c.get("covers", [])), *[show(c["inputs"].get(k, "")) for k in cols],
                 c["expected_result"], c.get("origin", "")) for c in s["cases"][:SAMPLE]]
        out.append(f"**{s['id']} — {s['name']}** ({len(s['cases'])} case; trích {min(SAMPLE, len(s['cases']))} case đầu)\n")
        out.append(table(["#TC", "Tiêu đề", "EC phủ", *cols, "Expected", "Nguồn"], rows) + "\n")
    out.append(f"*Đủ các case và cột \"Lý do chọn input\": `{ctx['feat']}/testcases.md` mục Bước 3b.*")
    return "\n".join(out)


def b_bva(ctx):
    var = {p["id"]: p for p in ctx["d"]["domain"]["partitions"]}
    out = []
    for s in ctx["d"]["suites"]:
        if not s["id"].startswith("TS-BVA"):
            continue
        # gom case liên tiếp thành từng chiều: chiều mới bắt đầu ở điểm LB-1
        dims, cur = [], None
        for c in s["cases"]:
            if c.get("bva_point") == "LB-1" or cur is None:
                cur = []
                dims.append(cur)
            cur.append(c)
        rows = []
        for dim in dims:
            lb = next((c for c in dim if c.get("bva_point") == "LB"), dim[0])
            ec = next((e for e in lb.get("covers", []) if e in var and var[e]["valid"]), "")
            keys = [k for k in dim[0]["inputs"] if len({c["inputs"].get(k) for c in dim}) > 1 and "{ts}" not in str(dim[0]["inputs"].get(k))][:1]
            label = f"{var[ec]['variable']} – {ec} {var[ec]['class']}" if ec else "?"
            by = {c["bva_point"]: c for c in dim}
            row = [label]
            for pt in POINTS:
                c = by.get(pt)
                row.append(f"{short(c['id'])}: `{', '.join(str(c['inputs'].get(k)) for k in keys) or '∅'}`" if c else "—")
            rows.append(row)
        out.append(f"**{s['id']} — {s['name']}** ({len(s['cases'])} case)\n")
        out.append(table(["Chiều (biến – lớp hợp lệ ở LB)", *[p.replace("-", "−") for p in POINTS]], rows) + "\n")
        if s.get("notes"):
            out.append(f"Ghi chú suite (nguyên văn): {s['notes']}\n")
    out.append("*Ô = số cuối mã TC: giá trị biến đang xét (`∅` = rỗng; ở tầng UI ô Xác nhận mật khẩu nhập cùng giá trị Mật khẩu theo cột dữ liệu); \"—\" = không có case ở điểm này. "
               f"Expected từng case: `{ctx['feat']}/testcases.md` mục Bước 4.*")
    return "\n".join(out)


def b_exec(ctx):
    rows, allc = [], []
    for s in ctx["d"]["suites"]:
        k = counts(s["cases"])
        allc += s["cases"]
        og = Counter(c.get("origin") or "?" for c in s["cases"])
        rows.append((s["id"], k["design"], k["run"], k["pass"], k["fail"], k["blocked"], k["notrun"],
                     ", ".join(f"{a} {b}" for a, b in sorted(og.items()))))
    k = counts(allc)
    og = Counter(c.get("origin") or "?" for c in allc)
    rows.append(("**Tổng**", k["design"], k["run"], k["pass"], k["fail"], k["blocked"], k["notrun"],
                 ", ".join(f"{a} {b}" for a, b in sorted(og.items()))))
    diff = [c for c in allc if c.get("auto_status") and c.get("auto_status") != c.get("status")]
    d2 = Counter((c["auto_status"], c["status"]) for c in diff)
    txt = table(["Suite", "Thiết kế", "Đã chạy (Pass+Fail)", "Pass", "Fail", "Blocked", "Chưa chạy", "Nguồn TC"], rows)
    txt += f"\n\nVerdict cuối khác kết quả tự động gốc (`auto_status`): {len(diff)} case — " + \
        "; ".join(f"{a}→{b}: {n}" for (a, b), n in sorted(d2.items())) + \
        " (" + ", ".join(short(c["id"]) for c in diff) + ")."
    txt += f"\n\n*Nguồn: `{ctx['rel']}` (`status`, `auto_status`, `origin`); tổng khớp dòng {ctx['feat']} của `python tools/summary.py {ctx['hw'].name}`.*"
    return txt


def parse_bug(p):
    t = p.read_text(encoding="utf-8")
    f = lambda k: (re.search(rf"\*\*{k}:\*\*\s*(.+)", t) or [None, ""])[1].strip()
    tc = re.search(r"## TC liên quan\s*\n(.*?)(?:\n## |\Z)", t, re.S)
    fail = next((l[2:].strip() for l in (tc.group(1).splitlines() if tc else []) if l.startswith("- Fail")), "")
    link = re.search(r"## Link GitHub Issue\s*\n+\s*(\S+)", t)
    return f("ID"), fail, f("Tiêu đề"), f("Severity"), f("Priority"), link.group(1) if link else ""


def b_bugs(ctx):
    ids = sorted({b for c in all_cases(ctx["d"]) for b in re.findall(r"BUG-\d+", c.get("bug_id") or "")},
                 key=lambda x: int(x[4:]))
    rows = []
    for b in ids:
        p = ctx["hw"] / "bugs" / f"{b}.md"
        if not p.exists():
            rows.append((b, "(không có file)", "", "", "", ""))
            continue
        bid, fail, title, sev, pri, link = parse_bug(p)
        num = re.search(r"/issues/(\d+)", link)
        rows.append((f"[{bid}](bugs/{b}.md)", fail, title, sev, pri, f"[#{num.group(1)}]({link})" if num else link))
    return table(["Bug ID", "TC liên quan (dòng \"Fail\")", "Tiêu đề", "Severity", "Priority", "GitHub Issue"], rows) + \
        f"\n\n*(AI chép) nguyên văn các trường `ID`, `Tiêu đề`, `Severity`, `Priority`, dòng \"Fail\" của mục \"TC liên quan\" và \"Link GitHub Issue\" từ `bugs/BUG-xx.md`; danh sách bug = các mã `BUG-xx` trong `bug_id` của `{ctx['rel']}` ({len(rows)} bug).*"


BLOCKS = {"scope": b_scope, "req": b_req, "assum": b_assum, "vars": b_vars, "parts": b_parts,
          "min": b_min, "bva": b_bva, "exec": b_exec, "bugs": b_bugs}


def main():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser()
    ap.add_argument("hw")
    ap.add_argument("feature")
    ap.add_argument("--report")
    ap.add_argument("--print", dest="show", choices=list(BLOCKS))
    a = ap.parse_args()
    hw = Path(a.hw)
    ctx = {"hw": hw, "feat": a.feature, "rel": f"{a.feature}/testcases.json",
           "d": json.load(open(hw / a.feature / "testcases.json", encoding="utf-8"))}
    if a.show:
        print(BLOCKS[a.show](ctx))
        return
    if not a.report:
        sys.exit("Cần --report hoặc --print")
    p = Path(a.report)
    txt, n = p.read_text(encoding="utf-8"), 0
    for name, fn in BLOCKS.items():
        pat = re.compile(rf"(<!-- REPORT:{a.feature}:{name}:START -->\n)(?:.*?\n)?(<!-- REPORT:{a.feature}:{name}:END -->)", re.S)
        if pat.search(txt):
            body = fn(ctx)
            txt = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), txt)
            n += 1
    p.write_text(txt, encoding="utf-8")
    print(f"Đã cập nhật {n} khối của {a.feature} trong {p}")


if __name__ == "__main__":
    main()
