#!/usr/bin/env python3
"""Kiểm file dữ liệu data/<X_FRnn>.json trước khi sinh/chạy spec.

- đủ trường; tc_id không trùng; ≥ --min TC (đề HW04: ≥ 12)
- sha1(expected) khớp expected_sha1
- expected trùng NGUYÊN VĂN với testcases.json HW02 tại commit nguồn (phát hiện sửa expected cho test xanh)
- có đủ Positive / Negative / Boundary (cảnh báo nếu thiếu)

Usage: python check_data.py HW04/data/A_FR01.json [--min 12]
Thoát mã 1 nếu có lỗi.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

REQ = ["tc_id", "title", "type", "technique", "inputs", "expected", "expected_sha1"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data", type=Path)
    ap.add_argument("--min", type=int, default=12)
    a = ap.parse_args()
    d = json.loads(a.data.read_text(encoding="utf-8"))
    err, warn = [], []
    tcs = d.get("testcases", [])
    if len(tcs) < a.min:
        err.append(f"chỉ có {len(tcs)} TC (< {a.min})")
    seen = set()
    for t in tcs:
        for k in REQ:
            if k not in t or t[k] in (None, ""):
                err.append(f"{t.get('tc_id','?')}: thiếu {k}")
        if t.get("tc_id") in seen:
            err.append(f"{t['tc_id']}: trùng tc_id")
        seen.add(t.get("tc_id"))
        if hashlib.sha1(t.get("expected", "").encode("utf-8")).hexdigest() != t.get("expected_sha1"):
            err.append(f"{t.get('tc_id')}: sha1(expected) không khớp expected_sha1")

    src = d.get("source", {})
    try:
        raw = subprocess.run(["git", "show", f"{src['commit']}:{src['file']}"], capture_output=True, text=True,
                             encoding="utf-8", check=True).stdout
        orig = {c["id"]: c.get("expected_result") for s in json.loads(raw)["suites"] for c in s.get("cases", [])}
        for t in tcs:
            if t.get("tc_id") not in orig:
                err.append(f"{t.get('tc_id')}: không có trong nguồn {src['file']}@{src['commit']}")
            elif orig[t["tc_id"]] != t.get("expected"):
                err.append(f"{t['tc_id']}: expected khác nguyên văn nguồn HW02")
    except Exception as e:  # noqa: BLE001
        err.append(f"không đọc được nguồn {src}: {e}")

    kinds = {t.get("type", "").split(" ")[0] for t in tcs}
    for k in ("Positive", "Negative", "Boundary"):
        if k not in kinds:
            warn.append(f"không có TC loại {k}")

    for w in warn:
        print("CẢNH BÁO:", w)
    for e in err:
        print("LỖI:", e)
    print(f"{a.data}: {len(tcs)} TC, {len(err)} lỗi, {len(warn)} cảnh báo")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
