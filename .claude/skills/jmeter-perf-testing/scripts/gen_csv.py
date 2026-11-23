#!/usr/bin/env python3
"""Sinh file CSV dữ liệu từ khối data[].generator của perf_plan.json.

Kiểu generator:
  users  : {"type":"users","count":N,"start":1,"email":"perf{i}@eshop.test","password":"...","name":"Perf User {i}"}
           -> cột theo data[].columns (email/password/name; cột khác lấy từ "extra": {"col": "mẫu {i}"})
  values : {"type":"values","values":[...]}  (1 cột) hoặc [[...],[...]] (nhiều cột)
  range  : {"type":"range","start":1,"stop":5}  (1 cột, stop tính cả)
  manual : không sinh; file do SV viết, chỉ kiểm tồn tại + header

Ghi UTF-8 không BOM, có dòng header = columns, LF. Không ghi đè file có sẵn trừ khi --force.
Usage: python gen_csv.py <hw-dir>/perf_plan.json [--hw-dir HW05] [--force] [--only <data-id>]
"""
import argparse
import csv
import json
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def rows_for(d):
    g = d.get("generator") or {"type": "manual"}
    cols = d["columns"]
    t = g["type"]
    if t == "users":
        start, n = int(g.get("start", 1)), int(g["count"])
        pats = {"email": g.get("email", "perf{i}@example.test"), "password": g.get("password", ""),
                "name": g.get("name", "Perf User {i}"), **g.get("extra", {})}
        for i in range(start, start + n):
            yield [str(pats.get(c, "")).format(i=i) for c in cols]
    elif t == "values":
        for v in g["values"]:
            yield v if isinstance(v, list) else [v]
    elif t == "range":
        for i in range(int(g["start"]), int(g["stop"]) + 1):
            yield [i]
    else:
        raise ValueError(f"generator.type '{t}' không hỗ trợ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", type=Path)
    ap.add_argument("--hw-dir", type=Path, help="gốc của data[].file (mặc định: thư mục chứa plan)")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()
    plan = json.loads(a.plan.read_text(encoding="utf-8"))
    base = a.hw_dir or a.plan.parent
    err = 0
    for d in plan.get("data", []):
        if a.only and d["id"] != a.only:
            continue
        f = base / d["file"]
        gtype = (d.get("generator") or {}).get("type", "manual")
        if gtype == "manual":
            if not f.exists():
                print(f"LỖI {d['id']}: generator manual nhưng chưa có {f}")
                err += 1
                continue
            head = f.read_text(encoding="utf-8").splitlines()[0].split(",")
            if head != d["columns"]:
                print(f"LỖI {d['id']}: header {head} ≠ columns {d['columns']}")
                err += 1
            else:
                print(f"OK  {d['id']}: {f} (manual)")
            continue
        if f.exists() and not a.force:
            print(f"BỎ QUA {d['id']}: {f} đã có (dùng --force để sinh lại)")
            continue
        f.parent.mkdir(parents=True, exist_ok=True)
        rows = list(rows_for(d))
        with open(f, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(d["columns"])
            w.writerows(rows)
        print(f"ĐÃ SINH {d['id']}: {f} ({len(rows)} dòng)")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
