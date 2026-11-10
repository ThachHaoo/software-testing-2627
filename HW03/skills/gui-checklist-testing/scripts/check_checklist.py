#!/usr/bin/env python3
"""Kiểm checklist.json (schema: references/schema-checklist.md).

Usage: python check_checklist.py <checklist.json> [--min 41]
Lỗi (ERROR) → mã thoát 1; cảnh báo (WARN) chỉ in ra.
"""
import argparse, json, re, sys, unicodedata
from collections import Counter
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

IAS = ["IA-01", "IA-02", "IA-03", "IA-04"]
SOURCES = ["SRS", "Control", "Heuristic"]
REQUIRED = ["id", "ia", "man_hinh", "muc_kiem_tra", "can_cu", "loai_nguon", "expected", "uu_tien", "nen_tang", "nguon"]
CODE = re.compile(r"\b(GA|NA)\d+\b")


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def check(doc, min_items):
    err, warn = [], []
    meta, items, assum = doc.get("meta", {}), doc.get("items", []), doc.get("assumptions", {})
    plats = list(meta.get("platforms", {}))
    results = set(meta.get("result_values", ["Passed", "Failed", "N/A", "Blocked"]))
    if not plats:
        err.append("meta.platforms rỗng")

    ids = [i.get("id") for i in items]
    for k, n in Counter(ids).items():
        if n > 1:
            err.append(f"{k}: id trùng ({n} lần)")
    seen = {}
    for it in items:
        iid = it.get("id", "?")
        for f in REQUIRED:
            if it.get(f) in (None, "", []):
                err.append(f"{iid}: thiếu {f}")
        if iid != "?" and not re.fullmatch(r"(CL|SV)-\d{2,3}", iid):
            err.append(f"{iid}: id phải dạng CL-xx (AI/Both) hoặc SV-xx (SV)")
        if iid.startswith("SV-") and it.get("nguon") != "SV":
            err.append(f"{iid}: id SV-xx nhưng nguon khác 'SV'")
        for f, v in it.items():
            if isinstance(v, str) and v == "(SV chưa ghi)":
                err.append(f"{iid}: {f} = (SV chưa ghi)")
            if isinstance(v, dict):
                for k2, v2 in v.items():
                    if v2 == "(SV chưa ghi)":
                        err.append(f"{iid}: {f}.{k2} = (SV chưa ghi)")
        if it.get("ia") not in IAS:
            err.append(f"{iid}: ia '{it.get('ia')}' ngoài {IAS}")
        if it.get("loai_nguon") not in SOURCES:
            err.append(f"{iid}: loai_nguon '{it.get('loai_nguon')}' ngoài {SOURCES}")
        if it.get("uu_tien") not in ("Mandatory", "Optional"):
            err.append(f"{iid}: uu_tien phải Mandatory/Optional")
        if it.get("nguon") not in ("AI", "SV", "Both"):
            err.append(f"{iid}: nguon phải AI/SV/Both")
        if it.get("nguon") == "SV" and not it.get("ly_do_ai_bo_sot"):
            warn.append(f"{iid}: item SV chưa có ly_do_ai_bo_sot")
        if "che_do" in it and it["che_do"] not in ("auto", "mixed", "manual"):
            err.append(f"{iid}: che_do '{it['che_do']}' ngoài auto/mixed/manual")
        if it.get("che_do") == "mixed" and not it.get("che_do_ghi_chu"):
            warn.append(f"{iid}: mixed nhưng chưa ghi phần nào chạy tay (che_do_ghi_chu)")
        nt = it.get("nen_tang", [])
        for p in nt:
            if p not in plats:
                err.append(f"{iid}: nền tảng {p} không có trong meta.platforms")
        na = it.get("na", {})
        for p in plats:
            if p not in nt and not na.get(p):
                err.append(f"{iid}: {p} không áp dụng nhưng thiếu giả định trong 'na'")
        for p in na:
            if p in nt:
                err.append(f"{iid}: {p} vừa trong nen_tang vừa N/A")
        text = " ".join(str(x) for x in (it.get("gia_dinh", ""), *na.values()))
        for m in CODE.finditer(text):
            if m.group(0) not in assum:
                err.append(f"{iid}: mã giả định {m.group(0)} không có trong assumptions")
        exp = it.get("expected", "")
        if exp and "fail nếu" not in exp.lower():
            warn.append(f"{iid}: expected chưa có ngưỡng 'Fail nếu …'")
        key = (norm(it.get("man_hinh", "")), norm(it.get("muc_kiem_tra", "")))
        if key in seen:
            err.append(f"{iid}: trùng màn hình + mục kiểm tra với {seen[key]}")
        seen[key] = iid
        for p, r in it.get("ket_qua", {}).items():
            if r not in results:
                err.append(f"{iid}: ket_qua[{p}] = '{r}' ngoài {sorted(results)}")
            if r == "N/A" and p in nt:
                err.append(f"{iid}: ket_qua[{p}] = N/A nhưng {p} trong nen_tang (đưa vào 'na' kèm giả định)")
            if r in ("Failed", "Blocked") and not it.get("notes_nt", {}).get(p):
                err.append(f"{iid}: {r} trên {p} nhưng thiếu notes_nt[{p}]")
            if r == "Failed" and not it.get("evidence", {}).get(p):
                err.append(f"{iid}: Failed trên {p} nhưng thiếu evidence[{p}]")

    by_ia = Counter(i.get("ia") for i in items)
    for ia in IAS:
        if not by_ia.get(ia):
            err.append(f"không có item nào cho {ia}")
    by_src = Counter(i.get("loai_nguon") for i in items)
    for s in SOURCES:
        if not by_src.get(s):
            warn.append(f"không có item nguồn {s}")
    if len(items) < min_items:
        err.append(f"chỉ có {len(items)} item (< {min_items})")
    used = set()
    for it in items:
        used |= {m.group(0) for m in CODE.finditer(" ".join(str(x) for x in (it.get("gia_dinh", ""), *it.get("na", {}).values())))}
    for k in assum:
        if CODE.fullmatch(k) and k not in used:
            warn.append(f"giả định {k} không được item nào tham chiếu")
    return err, warn, by_ia, by_src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--min", type=int, default=41, help="số item tối thiểu (đề HW03: > 40)")
    a = ap.parse_args()
    doc = json.loads(Path(a.json).read_text(encoding="utf-8"))
    err, warn, by_ia, by_src = check(doc, a.min)
    items = doc.get("items", [])
    print(f"{a.json}: {len(items)} item · " + ", ".join(f"{k} {by_ia[k]}" for k in IAS) +
          " · " + ", ".join(f"{k} {by_src.get(k, 0)}" for k in SOURCES) +
          " · nguồn " + ", ".join(f"{k} {v}" for k, v in sorted(Counter(i.get('nguon') for i in items).items())))
    for e in err:
        print("ERROR", e)
    for w in warn:
        print("WARN ", w)
    print(f"{len(err)} lỗi, {len(warn)} cảnh báo")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
