"""Nén ảnh chạy tay của D_FR20 trước khi merge (xuất .png).

1. Ảnh gốc ở --raw (mặc định HW02/D_FR20/manual_raw; .png/.jpg/.jpeg, không bao giờ bị sửa) →
   bản nén .png ở --out (mặc định HW02/D_FR20/evidence) theo tên chuẩn:
     <mã TC>[-_]manual[-_<n>]          → <mã TC>_manual_<n>.png   (ảnh điện thoại; thiếu n → 1)
     <mã TC>[-_]admin[-_manual][-_<n>] → <mã TC>_admin_<n>.png    (ảnh admin chụp theo case)
     D_admin_truoc|sau[_<n>]           → D_admin_truoc|sau_<n>.png (ảnh admin cả lượt)
   Tên không nhận ra → in ra, bỏ qua. Nhiều ảnh gốc cùng tên chuẩn (vd .png và .jpg) → giữ 1 bản
   (ảnh có nhiều điểm ảnh hơn), in ra để kiểm.
2. Ảnh `*_manual_*.png`, `*_admin_*.png`, `D_admin_*.png` đã có sẵn trong --out mà không vừa tạo ở bước 1:
   nén tại chỗ, chỉ ghi đè khi file mới nhỏ hơn.

Nén = thu nhỏ chiều rộng về --max-width, giảm còn 256 màu (ảnh chụp giao diện vẫn đọc rõ chữ), PNG optimize.
In kích thước trước/sau và bảng đổi tên.

Cần Pillow: py -3.12 -m pip install Pillow

Usage: py -3.12 tools/compress_manual.py [--raw DIR] [--out DIR] [--max-width 720] [--dry-run]
"""
import argparse
import io
import re
from pathlib import Path

from PIL import Image

PATTERNS = ("*_manual_*.png", "*_admin_*.png", "D_admin_*.png")
RAW_EXT = (".png", ".jpg", ".jpeg")
RULES = (
    (re.compile(r"(?i)^D_admin_(truoc|sau)(?:[-_](\d+))?$"), lambda m: f"D_admin_{m[1].lower()}_{m[2] or 1}"),
    (re.compile(r"^(TC-[A-Z0-9]+-\d+)[-_]admin(?:[-_]manual)?(?:[-_](\d+))?$"), lambda m: f"{m[1]}_admin_{m[2] or 1}"),
    (re.compile(r"^(TC-[A-Z0-9]+-\d+)[-_]manual(?:[-_](\d+))?$"), lambda m: f"{m[1]}_manual_{m[2] or 1}"),
)


def std_name(stem):
    for rx, fmt in RULES:
        m = rx.match(stem)
        if m:
            return fmt(m) + ".png"
    return None


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
    ap.add_argument("--raw", type=Path, default=Path("HW02/D_FR20/manual_raw"))
    ap.add_argument("--out", type=Path, default=Path("HW02/D_FR20/evidence"))
    ap.add_argument("--max-width", type=int, default=720)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    before = after = 0
    made = set()
    if a.raw.is_dir():
        groups = {}
        for f in sorted(a.raw.iterdir()):
            if f.suffix.lower() not in RAW_EXT:
                continue
            name = std_name(f.stem)
            if not name:
                print(f"[KHÔNG NHẬN RA] {f.name} — đổi tên tay rồi chạy lại")
                continue
            groups.setdefault(name, []).append(f)
        print("| Tên gốc | Tên mới |\n|---|---|")
        for name, files in sorted(groups.items()):
            src = max(files, key=lambda p: Image.open(p).size[0] * Image.open(p).size[1])
            for f in files:
                print(f"| `{f.name}` | `{name}`" + (" (trùng, bỏ)" if f != src else "") + " |")
            data = compress(src, a.max_width)
            dst = a.out / name
            if not a.dry_run:
                a.out.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(data)
            made.add(dst.resolve())
            before, after = before + src.stat().st_size, after + len(data)
    if a.out.is_dir():
        for f in sorted({f for pat in PATTERNS for f in a.out.glob(pat)}):
            if f.resolve() in made:
                continue
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
