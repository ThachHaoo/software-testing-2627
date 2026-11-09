#!/usr/bin/env python3
"""Bước 6: gom các sự kiện SV đã đánh dấu "bug": true trong phiếu phiên → một file dữ kiện cho SV viết bug.
Chép nguyên văn những gì SV ghi (không diễn giải, không viết mô tả bug). Pilot vẫn liệt kê, có ghi (pilot).

Usage: python bug_facts.py <sessions-dir> -o <bugs>/_groups_usability.md
"""
import argparse, json, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", type=Path)
    ap.add_argument("-o", "--out", type=Path, required=True)
    a = ap.parse_args()
    rows = []
    for f in sorted(a.dir.glob("S*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for e in d.get("su_kien") or []:
            if e.get("bug") is True:
                rows.append((d.get("phien", f.stem) + (" (pilot)" if d.get("pilot") else ""), e.get("t") or "", e.get("man_hinh") or "",
                             e.get("loai") or "", (e.get("mo_ta") or "").replace("|", "\\|"), d.get("video") or ""))
    out = ["# Dữ kiện bug từ phiên usability (gom tự động)", "",
           "Sinh bằng `bug_facts.py` từ sự kiện SV đánh dấu `\"bug\": true`. Cột Mô tả = nguyên văn SV ghi trong phiếu. "
           "**SV gom nhóm, kiểm trùng issue (ghi \"đã biết – #xx\"), viết bug report**; AI chỉ chạy bước tái hiện SV viết.", "",
           "| Phiên | Mốc | Màn hình | Loại | Mô tả (SV ghi) | Video | Nhóm (SV) | Trùng issue? |", "|---|---|---|---|---|---|---|---|"]
    out += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | | |" for r in rows]
    if not rows:
        out.append("| – | | | | Chưa có sự kiện nào được đánh dấu bug | | | |")
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Đã ghi {a.out}: {len(rows)} sự kiện")


if __name__ == "__main__":
    main()
