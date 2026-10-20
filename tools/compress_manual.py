"""Nén ảnh chạy tay của D_FR20 trước khi merge (giữ tên .png).

Chỉ đụng ảnh `*_manual_*.png` và `D_admin_*.png` trong các thư mục truyền vào
(mặc định HW02/D_FR20/manual_raw và HW02/D_FR20/evidence). Thu nhỏ chiều rộng về
--max-width, giảm còn 256 màu (ảnh chụp màn hình giao diện vẫn đọc rõ chữ), lưu PNG
optimize. Chỉ ghi đè khi file mới nhỏ hơn. In kích thước trước/sau.

Cần Pillow: pip install Pillow

Usage: python tools/compress_manual.py [thư mục ...] [--max-width 720] [--dry-run]
"""
import argparse
import io
from pathlib import Path

from PIL import Image

PATTERNS = ("*_manual_*.png", "D_admin_*.png")
DEFAULT_DIRS = ("HW02/D_FR20/manual_raw", "HW02/D_FR20/evidence")


def compress(path, max_width):
    img = Image.open(path)
    img.load()
    if img.width > max_width:
        img = img.resize((max_width, round(img.height * max_width / img.width)), Image.LANCZOS)
    img = img.convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="*", default=DEFAULT_DIRS)
    ap.add_argument("--max-width", type=int, default=720)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    before = after = 0
    for d in map(Path, a.dirs):
        if not d.is_dir():
            continue
        files = sorted({f for pat in PATTERNS for f in d.glob(pat)})
        for f in files:
            old = f.stat().st_size
            data = compress(f, a.max_width)
            new = len(data) if len(data) < old else old
            if new < old and not a.dry_run:
                f.write_bytes(data)
            before, after = before + old, after + new
            print(f"{f}: {old / 1024:.0f} KB → {new / 1024:.0f} KB" + (" (giữ nguyên)" if new == old else ""))
    print(f"Tổng: {before / 1024 / 1024:.2f} MB → {after / 1024 / 1024:.2f} MB" + (" (dry-run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
