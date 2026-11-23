#!/usr/bin/env python3
"""Đóng băng output AI của một bước (1 workflow, 2 scenarios, 7 phân tích, 8 đề xuất tối ưu) TRƯỚC khi SV sửa:
chép file vào <out>/step<k><tag>/ (giữ tên), ghi dòng vào <out>/INDEX.md kèm sha256. Không bao giờ ghi đè.
.jmx đóng băng đổi đuôi thành .jmx.txt để không bị mở/chạy nhầm như test plan chính thức.

Usage: python freeze.py --step 1 --out HW05/appendix/ai-outputs HW05/perf_plan.json [--tag b] [--note "#12"]
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

RENAME = {".jmx", ".ps1", ".py"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--step", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--tag", default="")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    dst = a.out / f"step{a.step}{a.tag}"
    if dst.exists():
        raise SystemExit(f"{dst} đã tồn tại – không ghi đè bản đóng băng (dùng --tag)")
    for f in a.files:
        if not f.is_file():
            raise SystemExit(f"không thấy {f}")
    dst.mkdir(parents=True)
    lines = []
    for f in a.files:
        d = dst / (f.name + ".txt" if f.suffix in RENAME else f.name)
        shutil.copy2(f, d)
        h = hashlib.sha256(d.read_bytes()).hexdigest()[:12]
        lines.append(f"- {dt.datetime.now():%H:%M %d/%m/%Y} · bước {a.step}{a.tag} · `{f.as_posix()}` → "
                     f"`{d.relative_to(a.out).as_posix()}` · sha256 {h} · {a.note}")
        print(f"Đã đóng băng {d}")
    with open(a.out / "INDEX.md", "a", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
