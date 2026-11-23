#!/usr/bin/env python3
"""Chèn nội dung một file (bảng sinh từ jtl_stats.py, RUN.md…) vào file Markdown đích, GIỮA hai marker:
    <!-- BEGIN:<key> -->
    ...  (bị thay toàn bộ)
    <!-- END:<key> -->
Chỉ thay phần giữa marker; phần SV viết ngoài marker không bị đụng. Thiếu marker → lỗi (không tự thêm).

Usage: python render_md.py <target.md> <key> <source-file> [--section "## Timeline theo phút"]
  --section : chỉ lấy một mục của source (từ dòng tiêu đề đó tới tiêu đề cùng cấp kế tiếp)
"""
import argparse
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def section(text, head):
    lines = text.splitlines()
    try:
        i = next(k for k, l in enumerate(lines) if l.strip() == head.strip())
    except StopIteration:
        raise SystemExit(f"không thấy mục '{head}'")
    level = len(head) - len(head.lstrip("#"))
    j = next((k for k in range(i + 1, len(lines)) if re.match(rf"^#{{1,{level}}}\s", lines[k])), len(lines))
    return "\n".join(lines[i + 1:j]).strip("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", type=Path)
    ap.add_argument("key")
    ap.add_argument("source", type=Path)
    ap.add_argument("--section")
    a = ap.parse_args()
    body = a.source.read_text(encoding="utf-8")
    if a.section:
        body = section(body, a.section)
    t = a.target.read_text(encoding="utf-8")
    b, e = f"<!-- BEGIN:{a.key} -->", f"<!-- END:{a.key} -->"
    if t.count(b) != 1 or t.count(e) != 1 or t.index(b) > t.index(e):
        raise SystemExit(f"{a.target}: cần đúng một cặp marker {b} … {e}")
    i, j = t.index(b) + len(b), t.index(e)
    a.target.write_text(t[:i] + "\n" + body.strip("\n") + "\n" + t[j:], encoding="utf-8", newline="\n")
    print(f"Đã chèn {a.source} vào {a.target} [{a.key}]")


if __name__ == "__main__":
    main()
