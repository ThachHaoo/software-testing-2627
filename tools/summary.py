#!/usr/bin/env python3
"""Tổng hợp số liệu test cho README (test summary bắt buộc của HW02).

Đọc <HW>/*/testcases.json và <HW>/bugs/BUG-*.md, in bảng Markdown.
--write README.md : thay đoạn giữa <!-- SUMMARY:START --> và <!-- SUMMARY:END -->.

Usage: python tools/summary.py HW02 [--write HW02/README.md]
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows: in tiếng Việt khi output bị chuyển hướng
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

START, END = "<!-- SUMMARY:START -->", "<!-- SUMMARY:END -->"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hw", type=Path)
    ap.add_argument("--write", type=Path)
    a = ap.parse_args()

    bug_files = sorted((a.hw / "bugs").glob("BUG-*.md"))
    bug_text = {b.stem: b.read_text(encoding="utf-8") for b in bug_files}
    # mã TC trong mục "## TC liên quan" của từng BUG-xx.md → đếm bug theo feature khi testcases.json chưa ghi bug_id
    bug_tcs = {k: set(re.findall(r"TC-[A-Z0-9]+-\d+", (re.search(r"(?ms)^## TC liên quan\s*$(.*?)(?=^## )", v) or [None, ""])[1]))
               for k, v in bug_text.items()}

    rows, tot = [], Counter()
    for tc in sorted(a.hw.glob("*/testcases.json")):
        d = json.loads(tc.read_text(encoding="utf-8"))
        cases = [c for s in d.get("suites", []) for c in s.get("cases", [])]
        st = Counter(c.get("status") or "Not run" for c in cases)
        og = Counter(c.get("origin") or "?" for c in cases)
        bugs = {b for c in cases for b in re.split(r"[,\s]+", c.get("bug_id") or "") if b}
        ids = {c.get("id") for c in cases}
        bugs |= {k for k, tcs in bug_tcs.items() if tcs & ids}
        r = Counter(designed=len(cases), executed=st["Pass"] + st["Fail"], passed=st["Pass"], failed=st["Fail"],
                    blocked=st["Blocked"], notrun=st["Not run"] + st["Skipped"], ai=og["AI"], both=og["Both"], sv=og["Human"], bugs=len(bugs))
        tot.update(r)
        rows.append((tc.parent.name, d.get("meta", {}).get("feature", ""), r))

    sev = Counter()
    for b in bug_files:
        m = re.search(r"(?im)^(?:- )?\*\*Severity:?\*\*:?\s*(\w+)", bug_text[b.stem])
        sev[m.group(1) if m else "?"] += 1

    h = "| Feature | Chức năng | Thiết kế | Đã chạy | Pass | Fail | Blocked | Chưa chạy | TC từ AI | TC AI + SV sửa | TC SV thêm | Bug |\n|---|---|---|---|---|---|---|---|---|---|---|---|"
    lines = [h] + [f"| {f} | {name} | {r['designed']} | {r['executed']} | {r['passed']} | {r['failed']} | {r['blocked']} | {r['notrun']} | {r['ai']} | {r['both']} | {r['sv']} | {r['bugs']} |" for f, name, r in rows]
    lines.append(f"| **Tổng** | **{len(rows)} feature** | **{tot['designed']}** | **{tot['executed']}** | **{tot['passed']}** | **{tot['failed']}** | **{tot['blocked']}** | **{tot['notrun']}** | **{tot['ai']}** | **{tot['both']}** | **{tot['sv']}** | **{len(bug_files) or tot['bugs']}** |")
    if bug_files:
        lines.append("")
        lines.append("Bug theo severity: " + ", ".join(f"{k} {v}" for k, v in sev.items()) + f" (tổng {len(bug_files)} file trong `bugs/`).")
    block = "\n".join(lines)
    print(block)

    if a.write:
        txt = a.write.read_text(encoding="utf-8") if a.write.exists() else f"{START}\n{END}\n"
        if START not in txt:
            txt += f"\n{START}\n{END}\n"
        txt = re.sub(re.escape(START) + r".*?" + re.escape(END), f"{START}\n{block}\n{END}", txt, flags=re.S)
        a.write.write_text(txt, encoding="utf-8")
        print(f"\nĐã cập nhật {a.write}")


if __name__ == "__main__":
    main()
