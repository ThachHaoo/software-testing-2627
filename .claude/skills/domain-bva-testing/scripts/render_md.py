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


def render(data, h):
    H = "#" * h
    meta, dom = data.get("meta", {}), data.get("domain", {})
    variables = dom.get("variables", [])
    vname = {v["id"]: v.get("name", v["id"]) for v in variables}
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
    out += [table(["EC", "Biến", "Lớp tương đương", "Hợp lệ", "Hướng dẫn", "Ghi chú"],
                  [[p["id"], vname.get(p.get("variable"), p.get("variable")), p.get("class"), "✔" if p.get("valid") else "✘", p.get("guideline"), p.get("note")] for p in parts]), ""]

    covered = defaultdict(list)
    for s, c in cases:
        for e in as_list(c.get("covers")):
            covered[e].append(c["id"])
    out += [f"{H} Bước 3a — Test Cases Providing Coverage of Partitions"]
    out += [table(["EC", "Lớp", "Test case phủ"], [[p["id"], p.get("class"), ", ".join(covered.get(p["id"], [])) or "⚠ chưa phủ"] for p in parts]), ""]

    def suite_table(s, bva=False):
        cols = s.get("columns", [])
        hdr = ["#TC", "Tiêu đề", "EC phủ"] + (["Điểm biên"] if bva else []) + cols + ["Expected", "Lý do chọn input", "Nguồn"]
        rows = []
        for c in s.get("cases", []):
            ins = c.get("inputs", {})
            rows.append([c["id"], c.get("title"), ", ".join(as_list(c.get("covers")))] + ([c.get("bva_point")] if bva else [])
                        + [ins.get(k, "") for k in cols] + [c.get("expected_result"), c.get("rationale"), ORIGIN.get(c.get("origin"), c.get("origin"))])
        body = []
        if s.get("preconditions"):
            body.append("**Tiền điều kiện:** " + "; ".join(s["preconditions"]))
        if s.get("procedure"):
            body.append("**Quy trình chung:**\n" + "\n".join(f"{i}. {p['action']} → {p.get('expected', '')}" for i, p in enumerate(s["procedure"], 1)))
        if s.get("cleanup"):
            body.append("**Dọn dẹp:** " + "; ".join(s["cleanup"]))
        return "\n\n".join(body + [table(hdr, rows)])

    titles = {"TS-DOM": "Bước 3b — Minimum Set of Test Cases (Domain)", "TS-BVA": "Bước 4 — Boundary Value Test Cases", "TS-SV": "Bước 5 — Test case sinh viên bổ sung"}
    for s in suites:
        out += [f"{H} {titles.get(s['id'], s['id'] + ' — ' + s.get('name', ''))}", suite_table(s, bva=s["id"] == "TS-BVA" or any(c.get("bva_point") for c in s.get("cases", []))), ""]

    out += [f"{H} Truy vết yêu cầu ↔ test case"]
    req_cov = defaultdict(list)
    for s, c in cases:
        for r in as_list(c.get("requirements")):
            req_cov[r].append(c["id"])
    out += [table(["Yêu cầu", "Test case", "Số TC"], [[r["id"], ", ".join(req_cov.get(r["id"], [])) or "⚠", len(req_cov.get(r["id"], []))] for r in data.get("requirements", [])]), ""]

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
