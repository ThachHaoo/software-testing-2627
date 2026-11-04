#!/usr/bin/env python3
"""Đóng băng bản nháp AI: chép checklist.json (và .md cùng tên nếu có) sang thư mục ai-outputs,
tên có tiền tố + bước + thời gian. Không bao giờ ghi đè file đã có. Ghi một dòng vào INDEX.md.

Usage: python freeze.py <dir>/checklist.json --step 1 --out HW03/appendix/ai-outputs [--prefix T1_checklist] [--note "#5"]
Tiền tố mặc định: <tên thư mục>_<tên file>, vd checklist_checklist → nên truyền --prefix.
"""
import argparse
import datetime as dt
import hashlib
import shutil
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json_path", type=Path)
    ap.add_argument("--step", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--prefix", default="")
    ap.add_argument("--note", default="", help="vd mã prompt #n")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    prefix = a.prefix or f"{a.json_path.parent.name}_{a.json_path.stem}"
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    written = []
    for src in [a.json_path, a.json_path.with_suffix(".md")]:
        if not src.exists():
            continue
        dst = a.out / f"{prefix}_step{a.step}_{stamp}{src.suffix}"
        if dst.exists():
            raise SystemExit(f"{dst} đã tồn tại — không ghi đè bản đóng băng")
        shutil.copy2(src, dst)
        written.append(dst)
    with open(a.out / "INDEX.md", "a", encoding="utf-8") as f:
        for d in written:
            h = hashlib.sha256(d.read_bytes()).hexdigest()[:12]
            f.write(f"- {dt.datetime.now():%H:%M %d/%m/%Y} · `{d.name}` · bước {a.step} · {a.note} · sha256 {h}\n")
    for d in written:
        print(f"Đã đóng băng {d}")


if __name__ == "__main__":
    main()
