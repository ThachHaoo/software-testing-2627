"""Nén + đổi tên ảnh chạy tay HW03 (T1 bước 4). Dùng lại compress() của tools/compress_manual.py.

Ảnh gốc ở HW03/checklist/evidence_raw/<Px_dir>/ (gitignore, không bị sửa) → bản nén .png ở
HW03/checklist/evidence/<Px_dir>/ tên chuẩn P<n>_<ID>_<k>.png (ID = CL-xx / SV-xx / M<k>).
Ảnh trong --exclude (còn lỗi: thiếu overlay, nhãn sai, gắn nhầm item) → bỏ qua, ở lại evidence_raw.

Usage: python tools/compress_hw03.py [--max-width 1280] [--exclude P3_M1_1,...] [--dry-run]
"""
import argparse, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from compress_manual import compress

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1] / "HW03" / "checklist"
DIRS = ["P1_chrome", "P2_firefox", "P3_android"]
RX = re.compile(r"^(P[123])_((?:CL|SV)-?\d{2}|M\d)[-_](\d+)$", re.I)


def std(stem):
    m = RX.match(stem)
    if not m:
        return None
    iid = m[2].upper()
    if iid[:2] in ("CL", "SV") and "-" not in iid:
        iid = iid[:2] + "-" + iid[2:]
    return f"{m[1].upper()}_{iid}_{int(m[3])}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-width", type=int, default=1280)
    ap.add_argument("--exclude", default="")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    excl = {x.strip() for x in a.exclude.split(",") if x.strip()}
    before = after = 0
    print("| Gốc (evidence_raw) | Bản nén (evidence) |\n|---|---|")
    for d in DIRS:
        raw, out = ROOT / "evidence_raw" / d, ROOT / "evidence" / d
        for f in sorted(raw.glob("*")):
            if f.suffix.lower() not in (".png", ".jpg", ".jpeg"):
                continue
            name = std(f.stem)
            if not name:
                print(f"| `{f.name}` | KHÔNG NHẬN RA – bỏ qua |")
                continue
            if f.stem in excl or name in excl:
                print(f"| `{f.name}` | **giữ ở evidence_raw (còn lỗi)** |")
                continue
            data = compress(f, a.max_width)
            if not a.dry_run:
                out.mkdir(parents=True, exist_ok=True)
                (out / f"{name}.png").write_bytes(data)
            before, after = before + f.stat().st_size, after + len(data)
            print(f"| `{d}/{f.name}` | `{d}/{name}.png` |")
    print(f"\nTổng: {before / 1048576:.2f} MB → {after / 1048576:.2f} MB" + (" (dry-run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
