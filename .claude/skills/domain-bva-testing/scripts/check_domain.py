#!/usr/bin/env python3
"""Kiểm tra phần domain testing / BVA của testcases.json (xem references/schema-domain.md).

Usage: python check_domain.py testcases.json
Exit 1 nếu có ERROR.
"""
import json
import sys
from collections import Counter, defaultdict
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows: in tiếng Việt khi output bị chuyển hướng
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

BVA_POINTS = {"LB-1", "LB", "LB+1", "NOM", "UB-1", "UB", "UB+1", "MIN_UI", "MAX_UI"}
APPROACHES = {"black-box", "gray-box", "white-box"}


def as_list(v):
    if not v:
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip() for x in str(v).replace(";", ",").split(",") if x.strip()]


def all_cases(data):
    for s in data.get("suites", []):
        for c in s.get("cases", []):
            yield s, c


def check(data):
    msgs = []
    add = lambda lvl, where, text: msgs.append((lvl, where, text))
    dom = data.get("domain", {})
    variables = {v["id"]: v for v in dom.get("variables", [])}
    parts = {}
    for p in dom.get("partitions", []):
        if p["id"] in parts:
            add("ERROR", p["id"], "trùng mã lớp tương đương")
        parts[p["id"]] = p
        if p.get("variable") not in variables:
            add("ERROR", p["id"], f"trỏ tới biến không tồn tại '{p.get('variable')}'")

    if not variables:
        add("WARN", "domain", "chưa có domain.variables (bước 1)")
    if variables and not parts:
        add("WARN", "domain", "chưa có domain.partitions (bước 2)")

    for vid, v in variables.items():
        vp = [p for p in parts.values() if p.get("variable") == vid]
        if v.get("io") == "output" and not vp:
            add("WARN", vid, f"biến đầu ra '{v.get('name')}' chưa được phân lớp")
        if v.get("io") == "input" and vp and not any(not p.get("valid") for p in vp):
            add("WARN", vid, f"biến đầu vào '{v.get('name')}' không có lớp không hợp lệ nào")

    covered = defaultdict(list)
    ids = Counter()
    uses_target = any(c.get("ec_target") for _, c in all_cases(data))  # chỉ cảnh báo thiếu ec_target khi file đã dùng trường này
    # biến khai "không có cận trên": no_upper_bound = mã giả định có trong meta.assumptions
    acodes = {str(a).split(" ", 1)[0] for a in data.get("meta", {}).get("assumptions", [])}
    no_ub = {vid for vid, v in variables.items() if v.get("no_upper_bound") in acodes}
    no_ub_codes = {variables[vid]["no_upper_bound"] for vid in no_ub}
    for vid, v in variables.items():
        if v.get("no_upper_bound") and vid not in no_ub:
            add("ERROR", vid, f"no_upper_bound trỏ tới giả định không tồn tại '{v['no_upper_bound']}'")
    for s, c in all_cases(data):
        cid = c.get("id", "?")
        ids[cid] += 1
        cov = as_list(c.get("covers"))
        invalid = []
        for e in cov:
            if e not in parts:
                if e.startswith("EC"):
                    add("ERROR", cid, f"covers trỏ tới lớp không tồn tại '{e}'")
                continue
            covered[e].append(cid)
            if not parts[e].get("valid", True) and variables.get(parts[e].get("variable"), {}).get("io") != "output":
                invalid.append(e)
        if len(invalid) > 1:
            add("ERROR", cid, f"phủ {len(invalid)} lớp không hợp lệ cùng lúc {invalid} — mỗi case không hợp lệ chỉ nên phủ một lớp")
        tgt = as_list(c.get("ec_target"))
        if tgt:
            outside = [e for e in tgt if e not in cov]
            if outside:
                add("ERROR", cid, f"ec_target có EC không nằm trong covers {outside}")
            if invalid and len([e for e in tgt if e in invalid]) != 1:
                add("ERROR", cid, "case không hợp lệ phải có đúng 1 EC không hợp lệ trong ec_target")
        elif uses_target and s.get("id", "").startswith(("TS-DOM", "TS-BVA")):
            add("WARN", cid, "TC domain thiếu ec_target")
        tech = c.get("technique")
        if not tech:
            add("WARN", cid, "thiếu technique (EP/BVA/EG/ST)")
        if tech == "BVA":
            bp = c.get("bva_point", "")
            if not bp:
                add("WARN", cid, "case BVA thiếu bva_point")
            elif bp == "LARGE":
                rvars = {parts[e]["variable"] for e in cov if e in parts and parts[e].get("guideline") == "range"}
                if not rvars or not all(v in no_ub for v in rvars) or not (set(as_list(c.get("assumptions"))) & no_ub_codes):
                    add("ERROR", cid, "bva_point 'LARGE' chỉ dùng khi biến có giả định 'không có cận trên' được khai "
                                      "(domain.variables[].no_upper_bound = mã giả định, và mã đó nằm trong assumptions của case)")
            elif bp not in BVA_POINTS:
                add("WARN", cid, f"bva_point '{bp}' không thuộc {sorted(BVA_POINTS)}")
        if c.get("approach") and c["approach"] not in APPROACHES:
            add("WARN", cid, f"approach '{c['approach']}' không thuộc {sorted(APPROACHES)}")
        for f in ("rationale", "origin"):
            if not c.get(f):
                add("WARN", cid, f"thiếu {f}")
        if c.get("status") in ("Pass", "Fail") and not c.get("actual_result"):
            add("WARN", cid, f"status={c['status']} nhưng chưa có actual_result")
    for cid, n in ids.items():
        if n > 1:
            add("ERROR", cid, "trùng mã test case")

    for e, p in parts.items():
        if not covered.get(e):
            add("WARN", e, f"lớp '{p.get('class')}' chưa được test case nào phủ")

    # range partitions: check boundary points per variable
    bva = defaultdict(set)
    for s, c in all_cases(data):
        if c.get("technique") == "BVA":
            for e in as_list(c.get("covers")):
                if e in parts:
                    bva[parts[e]["variable"]].add(c.get("bva_point"))
    for vid in {p["variable"] for p in parts.values() if p.get("guideline") == "range" and p.get("valid")}:
        missing = ({"LB-1", "LB", "LB+1"} if vid in no_ub else {"LB-1", "LB", "LB+1", "UB-1", "UB", "UB+1"}) - bva[vid]
        if bva[vid] and missing:
            add("WARN", vid, f"BVA cho biến '{variables.get(vid, {}).get('name')}' còn thiếu điểm {sorted(missing)} (bỏ qua nếu miền chỉ có một phía biên)")
        if not bva[vid]:
            add("WARN", vid, f"biến có lớp khoảng giá trị '{variables.get(vid, {}).get('name')}' chưa có case BVA")
    return msgs, parts, covered


def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    msgs, parts, covered = check(data)
    order = {"ERROR": 0, "WARN": 1}
    for lvl, where, text in sorted(msgs, key=lambda m: (order[m[0]], str(m[1]))):
        print(f"[{lvl}] {where}: {text}")
    cases = [c for _, c in all_cases(data)]
    v = sum(1 for p in parts.values() if p.get("valid"))
    print(f"\nEC: {len(parts)} ({v} hợp lệ, {len(parts) - v} không hợp lệ), đã phủ {sum(1 for e in parts if covered.get(e))}/{len(parts)}")
    print("Case theo suite: " + ", ".join(f"{s['id']}={len(s.get('cases', []))}" for s in data.get("suites", [])))
    print("Theo origin: " + ", ".join(f"{k}={n}" for k, n in Counter(c.get("origin", "?") for c in cases).items()))
    print("Theo status: " + ", ".join(f"{k}={n}" for k, n in Counter(c.get("status", "Not run") for c in cases).items()))
    errs = sum(1 for m in msgs if m[0] == "ERROR")
    print(f"{errs} errors · {len(msgs) - errs} warnings")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
