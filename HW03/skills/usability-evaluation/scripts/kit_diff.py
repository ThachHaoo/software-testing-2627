#!/usr/bin/env python3
"""Bước 2 (sau pilot): bảng thay đổi giữa kit đóng băng và kit đã sửa, cột "Lý do (SV)" để SV tự ghi.

Usage: python kit_diff.py <bản-đóng-băng.md> <participant_kit.md> -o pilot_changes.md [--title "Participant kit"]
Không ghi đè file đã có lý do SV: nếu -o đã tồn tại và có lý do khác "(SV chưa ghi)" → dừng, dùng --force để tạo lại.
"""
import argparse, difflib, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

TODO = "(SV chưa ghi)"


def cell(lines):
    s = " ⏎ ".join(l.strip() for l in lines if l.strip())
    return (s or "—").replace("|", "\\|")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("old", type=Path)
    ap.add_argument("new", type=Path)
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--title", default="Participant kit")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    if a.out.exists() and not a.force:
        body = a.out.read_text(encoding="utf-8")
        if "| C" in body and body.count(TODO) < body.count("\n| C"):
            sys.exit(f"{a.out} đã có lý do SV ghi — không ghi đè (dùng --force nếu chắc chắn)")
    old = a.old.read_text(encoding="utf-8").splitlines()
    new = a.new.read_text(encoding="utf-8").splitlines()
    rows = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        kind = {"replace": "Sửa", "delete": "Xoá", "insert": "Thêm"}[tag]
        rows.append((kind, f"{i1 + 1}–{i2}" if i2 > i1 else "—", f"{j1 + 1}–{j2}" if j2 > j1 else "—", cell(old[i1:i2]), cell(new[j1:j2])))
    out = [f"# Thay đổi sau pilot – {a.title}", "",
           f"So `{a.old.as_posix()}` (bản AI đóng băng) với `{a.new.as_posix()}` (sau pilot). Sinh bằng `kit_diff.py`; "
           f"**cột Lý do do SV ghi** (thấy gì ở pilot → vì sao sửa). AI không điền lý do.", "",
           "| # | Loại | Dòng cũ | Dòng mới | Trước | Sau | Lý do (SV) |", "|---|---|---|---|---|---|---|"]
    out += [f"| C{k} | {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {TODO} |" for k, r in enumerate(rows, 1)]
    if not rows:
        out.append("| – | Không đổi | | | | | |")
    a.out.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Đã ghi {a.out}: {len(rows)} thay đổi")


if __name__ == "__main__":
    main()
