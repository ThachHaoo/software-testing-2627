#!/usr/bin/env python3
"""Tạo khung phiếu phiên trống (mọi giá trị null) từ assets/session_template.json. SV nhập dữ liệu; AI không điền.

Usage: python new_session.py <sessions-dir> S01 [--pilot] [--platform P1]
Không ghi đè phiếu đã có.
"""
import argparse, json, re, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

TEMPLATE = Path(__file__).resolve().parents[1] / "assets" / "session_template.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", type=Path)
    ap.add_argument("session")
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--platform")
    a = ap.parse_args()
    if not re.fullmatch(r"S\d{2}", a.session):
        sys.exit("mã phiên dạng S00 (pilot), S01…")
    out = a.dir / f"{a.session}.json"
    if out.exists():
        sys.exit(f"{out} đã có — không ghi đè")
    d = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    d["phien"], d["pilot"] = a.session, a.pilot or a.session == "S00"
    if a.platform:
        d["nen_tang"] = a.platform
    a.dir.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã tạo khung trống {out}")


if __name__ == "__main__":
    main()
