#!/usr/bin/env python3
"""Bước 6 – gộp kết quả các lượt chạy (mỗi trình duyệt một report) của một feature.

Đọc results.json (Playwright JSON reporter, nằm cạnh index.html trong HW04/reports/<project>_<ts>/),
lấy test có tiêu đề bắt đầu bằng tc_id trong data/<X_FRnn>.json, rồi ghi:
  <feature-dir>/results.md     bảng tc_id × trình duyệt (Pass / Fail / Blocked / Not run) + tổng
  <feature-dir>/bug_groups.md  TC Fail gom theo thông điệp lỗi đầu tiên — CHỈ dữ kiện, SV viết bug

Quy tắc verdict:
  passed → Pass · failed có lỗi assertion (expect) → Fail
  failed/timedOut mà lỗi chỉ là TimeoutError (không assertion nào fail) → Blocked (lỗi harness)
  skipped kèm annotation type 'blocked' → Blocked · skipped khác → Not run

Usage: python merge_reports.py HW04/data/A_FR01.json HW04/A_FR01 \
           HW04/reports/chrome_<ts> HW04/reports/edge_<ts> HW04/reports/firefox_<ts>
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ANSI = re.compile(r"\x1b\[[0-9;]*m")


def walk(suite, out):
    for s in suite.get("suites", []):
        walk(s, out)
    for sp in suite.get("specs", []):
        for t in sp.get("tests", []):
            out.append((sp["title"], t))


def verdict(test) -> tuple[str, str]:
    r = (test.get("results") or [{}])[-1]
    st = r.get("status", "skipped")
    errs = [ANSI.sub("", e.get("message", "")) for e in r.get("errors", [])]
    first = next((e.strip().splitlines()[0] for e in errs if e.strip()), "")
    if st == "passed":
        return "Pass", ""
    if st == "skipped":
        ann = [a for a in test.get("annotations", []) + r.get("annotations", []) if a.get("type") == "blocked"]
        return ("Blocked", ann[0].get("description", "")) if ann else ("Not run", "")
    has_assert = any("expect(" in e or "Expected" in e for e in errs)
    only_timeout = errs and all("TimeoutError" in e or "Timeout" in e.splitlines()[0] for e in errs if e.strip())
    if st == "timedOut" or (only_timeout and not has_assert):
        return "Blocked", first or "timeout"
    return "Fail", first


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data", type=Path)
    ap.add_argument("feature_dir", type=Path)
    ap.add_argument("reports", nargs="+", type=Path)
    a = ap.parse_args()
    data = json.loads(a.data.read_text(encoding="utf-8"))
    ids = [t["tc_id"] for t in data["testcases"]]
    table = defaultdict(dict)       # tc_id -> project -> (verdict, msg)
    runs = []
    for rep in a.reports:
        rj = json.loads((rep / "results.json").read_text(encoding="utf-8"))
        project = rep.name.rsplit("_", 1)[0]
        meta = rj.get("config", {}).get("metadata", {})
        runs.append((project, rep.as_posix(), meta.get("Run by", "")))
        tests = []
        for s in rj.get("suites", []):
            walk(s, tests)
        for title, t in tests:
            tc = next((i for i in ids if title.startswith(i + " ")), None)
            if tc:
                table[tc][project] = verdict(t)
    projects = [p for p, _, _ in runs]

    L = [f"# {data['feature']} – kết quả chạy đa trình duyệt", "",
         "| trình duyệt | report | Run by |", "|---|---|---|"]
    L += [f"| {p} | `{r}` | {rb} |" for p, r, rb in runs]
    L += ["", "| tc_id | HW02 | " + " | ".join(projects) + " |", "|---|---|" + "---|" * len(projects)]
    tot = defaultdict(lambda: defaultdict(int))
    for i in ids:
        row = []
        for p in projects:
            v = table[i].get(p, ("Not run", ""))[0]
            tot[p][v] += 1
            row.append(v)
        hw = next(t["hw02"]["status"] for t in data["testcases"] if t["tc_id"] == i)
        L.append(f"| {i} | {hw} | " + " | ".join(row) + " |")
    L += ["", "| tổng | " + " | ".join(projects) + " |", "|---|" + "---|" * len(projects)]
    for v in ("Pass", "Fail", "Blocked", "Not run"):
        L.append(f"| {v} | " + " | ".join(str(tot[p][v]) for p in projects) + " |")
    (a.feature_dir / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")

    groups = defaultdict(list)
    for i in ids:
        for p in projects:
            v, msg = table[i].get(p, ("Not run", ""))
            if v == "Fail":
                groups[re.sub(r"\d{10,}", "{ts}", msg)].append(f"{i} [{p}]")
    G = [f"# {data['feature']} – nhóm TC Fail (dữ kiện, SV viết bug)", "",
         "Chỉ gom theo thông điệp lỗi đầu tiên của Playwright. Không đặt tên bug, không severity/priority, không kết luận nguyên nhân.",
         "Trước khi viết bug: chạy lại, restart backend, so UI với API (cô lập nguyên nhân).", ""]
    for n, (msg, items) in enumerate(sorted(groups.items(), key=lambda x: -len(x[1])), 1):
        G += [f"## G{n} ({len(items)} lượt)", "", f"- Lỗi đầu tiên: `{msg}`", f"- TC [trình duyệt]: {', '.join(items)}", ""]
    if not groups:
        G.append("Không có TC Fail.")
    (a.feature_dir / "bug_groups.md").write_text("\n".join(G) + "\n", encoding="utf-8", newline="\n")
    print(f"Đã ghi {a.feature_dir / 'results.md'} và bug_groups.md ({sum(len(v) for v in groups.values())} lượt Fail)")


if __name__ == "__main__":
    main()
