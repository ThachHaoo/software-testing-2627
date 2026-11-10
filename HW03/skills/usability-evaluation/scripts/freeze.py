#!/usr/bin/env python3
"""Đóng băng bản nháp AI (plan, participant kit, phiếu giấy…): chép từng file sang thư mục ai-outputs,
tên = <prefix>_<tên gốc>_step<k>_<thời gian><đuôi>. Không bao giờ ghi đè. Ghi một dòng / file vào INDEX.md.

Usage: python freeze.py <file> [<file>...] --step 1 --out HW03/appendix/ai-outputs --prefix T2 [--note "#5"]
"""
import argparse, datetime as dt, hashlib, shutil, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--step", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--prefix", default="usability")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    lines = []
    for src in a.files:
        if not src.is_file():
            sys.exit(f"{src} không tồn tại")
        dst = a.out / f"{a.prefix}_{src.stem}_step{a.step}_{stamp}{src.suffix}"
        if dst.exists():
            sys.exit(f"{dst} đã tồn tại — không ghi đè bản đóng băng")
        shutil.copy2(src, dst)
        h = hashlib.sha256(dst.read_bytes()).hexdigest()[:12]
        lines.append(f"- {dt.datetime.now():%H:%M %d/%m/%Y} · `{dst.name}` · bước {a.step} · {a.note} · sha256 {h}\n")
        print(f"Đã đóng băng {dst}")
    with open(a.out / "INDEX.md", "a", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
