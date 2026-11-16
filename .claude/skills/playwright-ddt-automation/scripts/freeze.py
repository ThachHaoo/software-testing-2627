#!/usr/bin/env python3
"""Đóng băng output AI của một bước TRƯỚC khi SV sửa: chép các file vào
<out>/<X_FRnn>/step<k>/ (giữ tên file). Không bao giờ ghi đè — thư mục bước đã có thì dừng
(lần đóng băng thứ hai của cùng bước dùng --tag, vd step3b).

Usage: python freeze.py --feature A_FR01 --step 1 --out HW04/appendix/ai-outputs \
           HW04/data/A_FR01.json HW04/A_FR01/selection.md [--note "#3"] [--tag b]
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
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--feature", required=True)
    ap.add_argument("--step", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--tag", default="")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    dst_dir = a.out / a.feature / f"step{a.step}{a.tag}"
    if dst_dir.exists():
        raise SystemExit(f"{dst_dir} đã tồn tại — không ghi đè bản đóng băng (dùng --tag)")
    for f in a.files:
        if not f.is_file():
            raise SystemExit(f"không thấy {f}")
    dst_dir.mkdir(parents=True)
    lines = []
    for f in a.files:
        d = dst_dir / f.name
        shutil.copy2(f, d)
        h = hashlib.sha256(d.read_bytes()).hexdigest()[:12]
        lines.append(f"- {dt.datetime.now():%H:%M %d/%m/%Y} · {a.feature} bước {a.step}{a.tag} · `{f.as_posix()}` → "
                     f"`{d.relative_to(a.out).as_posix()}` · sha256 {h} · {a.note}")
        print(f"Đã đóng băng {d}")
    with open(a.out / "INDEX.md", "a", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
