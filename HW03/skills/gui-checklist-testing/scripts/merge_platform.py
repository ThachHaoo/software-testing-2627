#!/usr/bin/env python3
"""Gộp kết quả một lượt chạy checklist trên một nền tảng vào checklist.json.

Usage: python merge_platform.py <checklist.json> <lượt.csv|lượt.json> --platform P1 [--dry-run] [--force]

- CSV: header id,status,notes,evidence (evidence cách nhau bởi ';'). JSON: xem references/schema-checklist.md.
- Lượt chạy tay: ghi ket_qua[Px], notes_nt[Px], evidence[Px], run[Px]. Lượt tự động (JSON kind="auto"): ghi auto_status[Px],
  auto_notes[Px], auto_evidence[Px], auto_run[Px] (luôn thay bằng lượt mới), không đụng ket_qua. Item có ket_qua[Px] khác giá trị mới → giữ nguyên
  và báo, trừ khi --force. --dry-run chỉ in thay đổi.
- Item áp dụng Px mà lượt chạy không có → báo "chưa chạy". id lạ → báo, bỏ qua.
"""
import argparse, csv, json, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def load_run(path, platform):
    p = Path(path)
    if p.suffix.lower() == ".json":
        d = json.loads(p.read_text(encoding="utf-8"))
        if d.get("platform") and d["platform"] != platform:
            sys.exit(f"File lượt là của {d['platform']}, không phải {platform}")
        return d.get("kind", "manual"), {k: {"status": v.get("status", ""), "notes": v.get("notes", ""), "evidence": v.get("evidence", [])}
                for k, v in d.get("results", {}).items()}
    out = {}
    with open(p, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            iid = (row.get("id") or "").strip()
            if not iid:
                continue
            ev = [x.strip() for x in (row.get("evidence") or "").split(";") if x.strip()]
            out[iid] = {"status": (row.get("status") or "").strip(), "notes": (row.get("notes") or "").strip(), "evidence": ev}
    return "manual", out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("run")
    ap.add_argument("--platform", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    jp = Path(a.json)
    doc = json.loads(jp.read_text(encoding="utf-8"))
    P = a.platform
    if P not in doc["meta"].get("platforms", {}):
        sys.exit(f"{P} không có trong meta.platforms")
    allowed = set(doc["meta"].get("result_values", ["Passed", "Failed", "N/A", "Blocked"]))
    kind, run = load_run(a.run, P)
    auto = kind == "auto"
    # lượt tự động (Playwright) → auto_status / auto_notes / auto_evidence / auto_run; luôn thay bằng lượt mới nhất,
    # không đụng ket_qua (verdict chính thức = lượt chạy tay trên trình duyệt thật)
    F = {"st": "auto_status", "no": "auto_notes", "ev": "auto_evidence", "run": "auto_run"} if auto else \
        {"st": "ket_qua", "no": "notes_nt", "ev": "evidence", "run": "run"}
    if auto:
        allowed = allowed | {"Skipped"}
    items = {i["id"]: i for i in doc["items"]}
    changed, kept, problems = 0, 0, []
    for iid, r in run.items():
        it = items.get(iid)
        if not it:
            problems.append(f"{iid}: không có trong checklist — bỏ qua")
            continue
        st = r["status"]
        if st not in allowed:
            problems.append(f"{iid}: status '{st}' ngoài {sorted(allowed)} — bỏ qua")
            continue
        if P not in it.get("nen_tang", []) and st != "N/A":
            problems.append(f"{iid}: {P} là N/A theo thiết kế nhưng lượt ghi '{st}' — bỏ qua")
            continue
        if P in it.get("nen_tang", []) and st == "N/A":
            problems.append(f"{iid}: lượt ghi N/A nhưng {P} áp dụng theo thiết kế — bỏ qua; "
                            f"muốn N/A thì sửa item (bỏ {P} khỏi nen_tang, thêm 'na' + giả định NAx)")
            continue
        old = it.get(F["st"], {}).get(P)
        if old and old != st and not a.force and not auto:
            problems.append(f"{iid}: đã có {old}, lượt ghi {st} — giữ {old} (dùng --force để ghi đè)")
            kept += 1
            continue
        if old != st or it.get(F["no"], {}).get(P, "") != r["notes"] or it.get(F["ev"], {}).get(P, []) != r["evidence"]:
            changed += 1
            print(f"{iid}: {old or '—'} → {st}" + (f" · {r['notes'][:60]}" if r["notes"] else ""))
        if not a.dry_run:
            it.setdefault(F["st"], {})[P] = st
            if r["notes"] or auto:
                it.setdefault(F["no"], {})[P] = r["notes"]
            if r["evidence"] or auto:
                it.setdefault(F["ev"], {})[P] = r["evidence"]
            it.setdefault(F["run"], {})[P] = Path(a.run).as_posix()
    missing = [i["id"] for i in doc["items"] if P in i.get("nen_tang", []) and i["id"] not in run
               and (not auto or (i.get("che_do") in ("auto", "mixed") and P in i.get("auto_nen_tang", [P])))]
    for p in problems:
        print("WARN ", p)
    if missing:
        print(f"WARN  chưa chạy trên {P}: {', '.join(missing)}")
    if not a.dry_run:
        jp.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{'(dry-run) ' if a.dry_run else ''}{P} [{kind}]: {changed} item đổi, {kept} giữ nguyên, {len(missing)} chưa chạy")


if __name__ == "__main__":
    main()
