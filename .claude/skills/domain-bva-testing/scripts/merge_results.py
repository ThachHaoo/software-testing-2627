#!/usr/bin/env python3
"""Gộp kết quả Playwright (reporter JSON) vào testcases.json.

Usage: python merge_results.py testcases.json results.json [--dry-run]
- Test được nhận diện qua mã TC ở đầu tiêu đề (vd "TC-FR01-03 Kiểm tra …").
- Actual lấy từ annotation type "actual"; bằng chứng lấy từ attachment có path.
- Ảnh/attachment có path được chép vào <thư mục feature>/evidence/ (Playwright xoá test-results mỗi lần chạy).
- Không đụng tới expected_result.
"""
import argparse
import json
import re
import shutil
from pathlib import Path
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows: in tiếng Việt khi output bị chuyển hướng
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

STATUS = {"passed": "Pass", "failed": "Fail", "timedOut": "Fail", "skipped": "Not run", "interrupted": "Blocked"}
ID_RE = re.compile(r"^(TC-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2,4})\b")


def walk(suite):
    for s in suite.get("suites", []) or []:
        yield from walk(s)
    for spec in suite.get("specs", []) or []:
        yield spec


def collect(results):
    found = {}
    for top in results.get("suites", []):
        for spec in walk(top):
            m = ID_RE.match(spec.get("title", ""))
            if not m:
                continue
            for t in spec.get("tests", []):
                runs = t.get("results", [])
                if not runs:
                    continue
                last = runs[-1]
                ann = [a.get("description", "") for a in (t.get("annotations", []) + last.get("annotations", [])) if a.get("type") == "actual"]
                err = (last.get("error") or {}).get("message", "")
                files = [a["path"] for a in last.get("attachments", []) if a.get("path")]
                found[m.group(1)] = {
                    "status": STATUS.get(last.get("status"), last.get("status")),
                    "actual": ann[-1] if ann else "",
                    "error": re.sub(r"\x1b\[[0-9;]*m", "", err).strip().splitlines()[0] if err else "",
                    "evidence": files,
                    "project": t.get("projectName", ""),
                }
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("testcases", type=Path)
    ap.add_argument("results", type=Path)
    ap.add_argument("--evidence-dir", type=Path, help="mặc định <thư mục testcases>/evidence")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    data = json.loads(a.testcases.read_text(encoding="utf-8"))
    res = collect(json.loads(a.results.read_text(encoding="utf-8")))
    base = a.testcases.parent
    evdir = a.evidence_dir or base / "evidence"
    hit = 0
    for s in data.get("suites", []):
        for c in s.get("cases", []):
            r = res.get(c.get("id"))
            if not r:
                continue
            hit += 1
            c["status"] = r["status"]
            c["actual_result"] = r["actual"] or (f"(không ghi actual) {r['error']}" if r["error"] else "")
            ev = []
            for i, p in enumerate(r["evidence"], 1):
                src = Path(p)
                if not src.exists():
                    continue
                dst = evdir / f"{c['id']}{'' if i == 1 else '_' + str(i)}{src.suffix}"
                if not a.dry_run:
                    evdir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                try:
                    ev.append(str(dst.resolve().relative_to(base.resolve())).replace("\\", "/"))
                except ValueError:
                    ev.append(str(dst))
            if ev:
                c["evidence"] = ", ".join(ev)
            print(f"{c['id']}: {r['status']}  {c['actual_result'][:80]}")
    missing = set(res) - {c.get("id") for s in data.get("suites", []) for c in s.get("cases", [])}
    for m in sorted(missing):
        print(f"[WARN] {m} có trong kết quả nhưng không có trong {a.testcases.name}")
    print(f"Đã gộp {hit} test case.")
    if not a.dry_run:
        a.testcases.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
