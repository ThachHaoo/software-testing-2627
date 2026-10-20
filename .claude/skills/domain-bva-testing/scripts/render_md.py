#!/usr/bin/env python3
"""Sinh bảng Markdown theo slide Domain Testing từ testcases.json.

Usage: python render_md.py testcases.json [-o testcases.md] [--level 3]
Các bảng: Biến vào/ra · Complete Set of Partitions · Coverage of Partitions ·
Minimum Set (TS-DOM) · Boundary Value TC (TS-BVA) · Bổ sung (TS-SV, suite khác) ·
Truy vết · Giả định · Tổng kết chạy.
"""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows: in tiếng Việt khi output bị chuyển hướng
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def as_list(v):
    if not v:
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v]
    return [x.strip() for x in str(v).replace(";", ",").split(",") if x.strip()]


def cell(v):
    if v is None:
        return ""
    if isinstance(v, list):
        v = "<br>".join(str(x) for x in v)
    return str(v).replace("|", "\\|").replace("\n", "<br>")


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(cell(x) for x in r) + " |" for r in rows]
    return "\n".join(out)


ORIGIN = {"AI": "AI", "Human": "SV", "Both": "AI + SV sửa"}


def show(v):
    """Giá trị nhập: hiện rõ chuỗi rỗng và khoảng trắng đầu/cuối (␣) để bảng .md không đánh lừa người đọc."""
    if not isinstance(v, str):
        return v
    if v == "":
        return "`''` (rỗng)"
    if v != v.strip():
        return "`" + v.replace(" ", "␣").replace("\t", "⇥") + "`"
    return v


def render(data, h):
    H = "#" * h
    meta, dom = data.get("meta", {}), data.get("domain", {})
    variables = dom.get("variables", [])
    vname = {v["id"]: v.get("name", v["id"]) for v in variables}
    input_names = {v.get("name") for v in variables if v.get("io") == "input"}  # show() chỉ áp cho cột là biến đầu vào
    parts = dom.get("partitions", [])
    pmap = {p["id"]: p for p in parts}
    suites = data.get("suites", [])
    cases = [(s, c) for s in suites for c in s.get("cases", [])]
    out = []

    if meta.get("scope"):
        out += [f"{H} Phạm vi", meta["scope"], ""]
    if data.get("requirements"):
        out += [f"{H} Yêu cầu (test basis)", table(["Mã", "Nội dung"], [[r["id"], r["text"]] for r in data["requirements"]]), ""]

    out += [f"{H} Bước 1 — Biến vào/ra"]
    has_note = any(v.get("note") for v in variables)
    out += [table(["Mã", "Biến", "Vào/Ra", "Nguồn", "Kiểu", "Ràng buộc (đặc tả)"] + (["Ghi chú"] if has_note else []),
                  [[v["id"], v.get("name"), "Vào" if v.get("io") == "input" else "Ra", v.get("source"), v.get("type"), v.get("constraint")]
                   + ([v.get("note", "")] if has_note else []) for v in variables]), ""]

    out += [f"{H} Bước 2 — Complete Set of Partitions"]
    has_req = any(p.get("requirements") for p in parts)
    out += [table(["EC", "Biến", "Lớp tương đương", "Hợp lệ", "Hướng dẫn"] + (["Yêu cầu"] if has_req else []) + ["Ghi chú"],
                  [[p["id"], vname.get(p.get("variable"), p.get("variable")), p.get("class"), "✔" if p.get("valid") else "✘", p.get("guideline")]
                   + ([", ".join(as_list(p.get("requirements")))] if has_req else []) + [p.get("note")] for p in parts]), ""]

    covered = defaultdict(list)
    for s, c in cases:
        for e in as_list(c.get("covers")):
            covered[e].append(c["id"])
    out += [f"{H} Bước 3a — Test Cases Providing Coverage of Partitions"]
    out += [table(["EC", "Lớp", "Test case phủ"], [[p["id"], p.get("class"), ", ".join(covered.get(p["id"], [])) or "⚠ chưa phủ"] for p in parts]), ""]

    def suite_table(s, bva=False):
        cols = s.get("columns", [])
        tgt = any(c.get("ec_target") for c in s.get("cases", []))
        appr = any(c.get("approach") for c in s.get("cases", []))
        hdr = ["#TC", "Tiêu đề", "EC phủ"] + (["EC mục tiêu"] if tgt else []) + (["Điểm biên"] if bva else []) + cols + ["Expected", "Lý do chọn input"] + (["Cách tiếp cận"] if appr else []) + ["Nguồn"]
        rows = []
        for c in s.get("cases", []):
            ins = c.get("inputs", {})
            rows.append([c["id"], c.get("title"), ", ".join(as_list(c.get("covers")))]
                        + ([", ".join(as_list(c.get("ec_target")))] if tgt else []) + ([c.get("bva_point")] if bva else [])
                        + [show(ins.get(k, "")) if k in input_names else ins.get(k, "") for k in cols] +[c.get("expected_result"), c.get("rationale")] + ([c.get("approach") or "black-box"] if appr else []) + [ORIGIN.get(c.get("origin"), c.get("origin"))])
        body = []
        if s.get("preconditions"):
            body.append("**Tiền điều kiện:** " + "; ".join(s["preconditions"]))
        if s.get("procedure"):
            body.append("**Quy trình chung:**\n" + "\n".join(f"{i}. {p['action']} → {p.get('expected', '')}" for i, p in enumerate(s["procedure"], 1)))
        if s.get("cleanup"):
            body.append("**Dọn dẹp:** " + "; ".join(s["cleanup"]))
        return "\n\n".join(body + [table(hdr, rows)])

    def title_of(s):
        sid, name = s["id"], s.get("name", "")
        for prefix, label in (("TS-DOM", "Bước 3b — Minimum Set of Test Cases (Domain)"), ("TS-BVA", "Bước 4 — Boundary Value Test Cases"),
                              ("TS-SV", "Bước 5 — Test case sinh viên bổ sung")):
            if sid.startswith(prefix):
                return f"{label} · {sid}" + (f" — {name}" if name else "")
        return f"{sid} — {name}"

    def steps_detail(s):
        blocks = []
        for c in s.get("cases", []):
            if not c.get("steps"):
                continue
            b = [f"**{c['id']}** — {c.get('title', '')}", ""]
            if c.get("preconditions"):
                b.append("- Tiền điều kiện: " + "; ".join(as_list(c["preconditions"])))
            if c.get("test_data"):
                b.append("- Dữ liệu: " + cell(c["test_data"]))
            b += [f"- Bước {i}: {st.get('action', '')} → {st.get('expected', '')}" for i, st in enumerate(c["steps"], 1)]
            if c.get("cleanup"):
                b.append("- Dọn dẹp: " + "; ".join(as_list(c["cleanup"])))
            blocks.append("\n".join(b))
        return "\n\n".join(blocks)

    for s in suites:
        body = [f"{H} {title_of(s)}"]
        if s.get("notes"):
            body.append("**Ghi chú suite:** " + cell(s["notes"]))
        body.append(suite_table(s, bva=s["id"].startswith("TS-BVA") or any(c.get("bva_point") for c in s.get("cases", []))))
        det = steps_detail(s)
        if det:
            body += ["", "**Các bước chi tiết:**", "", det]
        out += body + [""]

    out += [f"{H} Truy vết yêu cầu ↔ test case"]
    ec_req = any(p.get("requirements") for p in parts)
    if ec_req:
        out += ["Sinh tự động: yêu cầu của một TC = hợp các yêu cầu của các EC mục tiêu (ec_target; TC không có ec_target thì dùng EC phủ) theo cột Yêu cầu ở bảng Bước 2, cộng với trường requirements và assumptions của TC (dùng cho case GUI không gắn EC). Mã giả định (B…) hiện thành dòng riêng.", ""]
    req_cov = defaultdict(list)
    for s, c in cases:
        src = as_list(c.get("ec_target")) or as_list(c.get("covers"))
        reqs = [r for e in src for r in as_list(pmap.get(e, {}).get("requirements"))] if ec_req else []
        for r in dict.fromkeys(reqs + as_list(c.get("requirements")) + as_list(c.get("assumptions"))):
            req_cov[r].append(c["id"])
    known = [r["id"] for r in data.get("requirements", [])]
    acodes = {str(a).split(" ", 1)[0] for a in meta.get("assumptions", [])}
    extra = [r for r in req_cov if r not in known]
    label = lambda r: f"{r} (giả định)" if r in acodes else f"{r} (?)"
    out += [table(["Yêu cầu", "Test case", "Số TC"], [[r, ", ".join(req_cov.get(r, [])) or "⚠", len(req_cov.get(r, []))] for r in known]
                  + [[label(r), ", ".join(req_cov[r]), len(req_cov[r])] for r in extra]), ""]

    if meta.get("assumptions"):
        out += [f"{H} Giả định khi đặc tả chưa nói rõ"] + [f"- {a}" for a in meta["assumptions"]] + [""]

    ran = [c for _, c in cases if c.get("status") not in (None, "", "Not run")]
    if ran:
        out += [f"{H} Kết quả thực thi"]
        out += [table(["#TC", "Expected", "Actual", "Verdict", "Bằng chứng", "Bug"],
                      [[c["id"], c.get("expected_result"), c.get("actual_result"), c.get("status"), c.get("evidence"), c.get("bug_id")] for _, c in cases]), ""]
    st = Counter(c.get("status") or "Not run" for _, c in cases)
    og = Counter(ORIGIN.get(c.get("origin"), c.get("origin") or "?") for _, c in cases)
    if cases:
        out += [f"**Tổng:** {len(cases)} TC · " + " · ".join(f"{k}: {v}" for k, v in st.items()) + " · Nguồn: " + ", ".join(f"{k} {v}" for k, v in og.items())]
    else:
        out += ["**Tổng:** chưa có test case (bước 3–4)."]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json_path")
    ap.add_argument("-o", "--out")
    ap.add_argument("--level", type=int, default=3, help="cấp heading (mặc định ###)")
    a = ap.parse_args()
    md = render(json.load(open(a.json_path, encoding="utf-8")), a.level)
    if a.out:
        Path(a.out).write_text(md, encoding="utf-8")
        print(f"Đã ghi {a.out}")
    else:
        print(md)


if __name__ == "__main__":
    main()
