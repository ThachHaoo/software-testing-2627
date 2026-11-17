#!/usr/bin/env python3
"""Bước 1 – chọn TC từ testcases.json của HW02 và xuất file dữ liệu cho spec data-driven.

Hai chế độ:
  --candidates   liệt kê TC ứng viên (tầng UI, suite matrix có inputs) kèm loại/kỹ thuật/kết quả HW02
  (mặc định)     đọc file chọn <feature-dir>/selection.json → ghi data/<X_FRnn>.json + <feature-dir>/selection.md

expected được CHÉP NGUYÊN VĂN từ bản HW02 tại commit nguồn (git show <commit>:<path>), kèm sha1.

Usage:
  python select_tc.py HW02/A_FR01/testcases.json --candidates
  python select_tc.py HW02/A_FR01/testcases.json --selection HW04/A_FR01/selection.json \
      --data HW04/data/A_FR01.json --md HW04/A_FR01/selection.md
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


def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", check=True).stdout


def source_commit(path: Path) -> str:
    """Commit gần nhất đã sửa file nguồn; file phải sạch (không sửa dở) để chép nguyên văn."""
    rel = path.as_posix()
    if git("status", "--porcelain", "--", rel).strip():
        raise SystemExit(f"{rel} đang có thay đổi chưa commit — commit trước rồi mới chọn TC")
    return git("log", "-1", "--format=%h", "--", rel).strip()


def load_at(commit: str, path: Path) -> dict:
    return json.loads(git("show", f"{commit}:{path.as_posix()}"))


def ui_cases(doc: dict):
    """TC tầng UI trong suite matrix (có inputs). Bỏ suite API và suite checklist/steps (không có dữ liệu vào)."""
    for s in doc.get("suites", []):
        if s.get("format") != "matrix":
            continue
        for c in s.get("cases", []):
            layer = c.get("layer") or (c.get("inputs") or {}).get("Tầng")
            if layer == "UI" and c.get("inputs"):
                yield s, c


def kind(c: dict, override: dict, note: str) -> str:
    """Loại +/-/biên: lấy type của HW02; thiếu thì lấy từ selection.json kèm ghi chú nguồn (mặc định "suy ra")."""
    t = c.get("type")
    if t in ("Positive", "Negative", "Boundary"):
        return t
    if c["id"] in override:
        return f"{override[c['id']]} ({note})"
    return "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("testcases", type=Path)
    ap.add_argument("--candidates", action="store_true")
    ap.add_argument("--selection", type=Path)
    ap.add_argument("--data", type=Path)
    ap.add_argument("--md", type=Path)
    a = ap.parse_args()

    commit = source_commit(a.testcases)
    doc = load_at(commit, a.testcases)
    cands = list(ui_cases(doc))

    if a.candidates:
        print(f"Nguồn: {a.testcases.as_posix()} @ {commit} — {len(cands)} TC UI có inputs")
        print("| tc_id | suite | loại | kỹ thuật | điểm BVA | HW02 auto | HW02 status | bug |")
        print("|---|---|---|---|---|---|---|---|")
        for s, c in cands:
            print(f"| {c['id']} | {s['id']} | {c.get('type') or '?'} | {c.get('technique','')} | {c.get('bva_point') or ''} "
                  f"| {c.get('auto_status','')} | {c.get('status','')} | {c.get('bug_id','')} |")
        return

    if not (a.selection and a.data and a.md):
        raise SystemExit("cần --selection, --data, --md (hoặc --candidates)")
    sel = json.loads(a.selection.read_text(encoding="utf-8"))
    by_id = {c["id"]: (s, c) for s, c in cands}
    missing = [i for i in sel["ids"] if i not in by_id]
    if missing:
        raise SystemExit(f"Không phải TC UI có inputs trong nguồn: {missing}")
    override = sel.get("type_override", {})
    reasons = sel.get("reasons", {})

    tcs = []
    for i in sel["ids"]:
        s, c = by_id[i]
        exp = c["expected_result"]
        tcs.append({
            "tc_id": c["id"],
            "title": c["title"],
            "suite": s["id"],
            "type": kind(c, override, sel.get("type_override_note", "suy ra")),
            "technique": c.get("technique", ""),
            "bva_point": c.get("bva_point") or "",
            "inputs": c["inputs"],
            "expected": exp,
            "expected_sha1": sha1(exp),
            "notes": c.get("notes", ""),
            "hw02": {"status": c.get("status", ""), "auto_status": c.get("auto_status", ""),
                     # testcases.json không ghi bug_id → lấy từ bug_map (trích HW02/bugs/BUG-xx.md mục TC liên quan)
                     "bug_id": c.get("bug_id") or sel.get("bug_map", {}).get(c["id"], "")},
        })
    data = {
        "feature": sel["feature"],
        "source": {"file": a.testcases.as_posix(), "commit": commit},
        "preconditions": {s["id"]: s.get("preconditions", []) for s, _ in (by_id[i] for i in sel["ids"])},
        "testcases": tcs,
    }
    if sel.get("assumptions"):        # dữ liệu phụ ngoài expected (giả định SV chốt), không đổi sha1 expected
        data["assumptions"] = sel["assumptions"]
    a.data.parent.mkdir(parents=True, exist_ok=True)
    a.data.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    # selection.md
    from collections import Counter
    cnt_type = Counter(t["type"].split(" ")[0] for t in tcs)
    cnt_hw02 = Counter(t["hw02"]["status"] for t in tcs)
    L = [f"# {sel['feature']} – chọn TC tự động hoá (bước 1)", "",
         f"Nguồn: `{a.testcases.as_posix()}` @ `{commit}` · {len(cands)} TC UI có inputs → chọn **{len(tcs)}**.",
         f"Dữ liệu: `{a.data.as_posix()}` (expected chép nguyên văn + sha1).", "",
         "Loại: " + ", ".join(f"{k} {v}" for k, v in sorted(cnt_type.items()))
         + " · HW02 status: " + ", ".join(f"{k} {v}" for k, v in sorted(cnt_hw02.items())), "",
         "| # | tc_id | loại | kỹ thuật | BVA | HW02 auto / status | bug | lý do chọn |",
         "|---|---|---|---|---|---|---|---|"]
    for n, t in enumerate(tcs, 1):
        h = t["hw02"]
        L.append(f"| {n} | {t['tc_id']} | {t['type']} | {t['technique']} | {t['bva_point']} | {h['auto_status']} / {h['status']} "
                 f"| {h['bug_id']} | {reasons.get(t['tc_id'], '')} |")
    if sel.get("excluded"):
        L += ["", "## Không chọn", "", "| TC / nhóm | lý do |", "|---|---|"]
        L += [f"| {k} | {v} |" for k, v in sel["excluded"].items()]
    for title, lines in sel.get("sections", {}).items():
        L += ["", f"## {title}", ""] + [f"- {x}" for x in lines]
    if sel.get("decisions"):
        L += ["", "## Quyết định của SV", ""] + [f"- {x}" for x in sel["decisions"]]
    if sel.get("criteria"):
        L += ["", "## Tiêu chí", ""] + [f"- {x}" for x in sel["criteria"]]
    a.md.parent.mkdir(parents=True, exist_ok=True)
    a.md.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"Đã ghi {a.data} ({len(tcs)} TC) và {a.md}")


if __name__ == "__main__":
    main()
