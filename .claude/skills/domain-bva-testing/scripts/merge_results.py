#!/usr/bin/env python3
"""Gộp kết quả Playwright (reporter JSON) vào testcases.json.

Usage: python merge_results.py testcases.json results.json [--dry-run]
- Test được nhận diện qua mã TC ở đầu tiêu đề (vd "TC-FR01-03 Kiểm tra …").
- Actual lấy từ annotation type "actual"; bằng chứng lấy từ attachment có path.
- Annotation type "verdict" (Pass/Fail/Blocked/Not run/Skipped) thay cho status của Playwright, vd Blocked theo A17/A20.
- Ảnh/attachment có path được chép vào <thư mục feature>/evidence/ (Playwright xoá test-results mỗi lần chạy):
  bỏ trace .zip, bỏ file trùng nội dung (sha256, giữ file đầu), tên theo tên attachment (TC-xx_ui.png, _api.png, _req.json, _res.json; ảnh Playwright tự chụp → _failed.png).
- Ghi thêm "auto_status" (kết quả tự động gốc) cạnh "status"; testcases.json giữ nguyên định dạng phần trước "suites".
- Không đụng tới expected_result.
"""
import argparse
import hashlib
import json
import re
import shutil
import unicodedata
from pathlib import Path
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows: in tiếng Việt khi output bị chuyển hướng
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

STATUS = {"passed": "Pass", "failed": "Fail", "timedOut": "Fail", "skipped": "Not run", "interrupted": "Blocked"}
VERDICTS = {"Pass", "Fail", "Blocked", "Not run", "Skipped"}
SKIP_EXT = (".zip",)          # trace Playwright: nặng, có token/payload → để lại test-results/, không chép vào evidence
# Hậu tố tên file evidence theo TÊN attachment (Playwright đổi tên file thành <tên>-<sha1>.<đuôi>).
# Tên dạng "<mã TC>_x" → bỏ mã TC; ảnh Playwright tự chụp (test-failed-N.png / test-finished-N.png) → _failed.
NAME_SUFFIX = {"screenshot": "_ui", "_request": "_req", "_response": "_res", "render từ response thật": "_api",
               "sau đăng nhập": "_login", "trang Quản lý Người dùng": "_admin"}


def slug(s):
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    return re.sub(r"[^A-Za-z0-9]+", "-", "".join(ch for ch in s if not unicodedata.combining(ch))).strip("-").lower()


def evidence_name(cid, att_name, src, used):
    ext = src.suffix.lower()
    if re.fullmatch(r"test-(failed|finished)-\d+\.png", src.name):
        suf = "_failed"
    else:
        key = att_name[len(cid):] if att_name.startswith(cid + "_") else att_name
        suf = NAME_SUFFIX.get(key) or "_" + slug(key)
    name, n = f"{cid}{suf}{ext}", 2
    while name in used:
        name, n = f"{cid}{suf}-{n}{ext}", n + 1
    used.add(name)
    return name


def dump_like_source(original, data):
    """Giữ nguyên phần trước khoá "suites" (định dạng do người/script khác viết), chỉ ghi lại khối suites
    với indent 2 — cùng cách các script khác trong skill ghi file, để diff chỉ còn status/actual/evidence."""
    i = original.find('"suites": [')
    if i != -1:
        body = json.dumps(data["suites"], ensure_ascii=False, indent=2)
        body = "\n".join(("  " + line if k else line) for k, line in enumerate(body.split("\n")))
        text = original[:i] + '"suites": ' + body + "\n}\n"
        try:
            if json.loads(text) == data:
                return text
        except json.JSONDecodeError:
            pass
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"
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
                anns = t.get("annotations", []) + last.get("annotations", [])
                ann = [a.get("description", "") for a in anns if a.get("type") == "actual"]
                # annotation "verdict" (vd Blocked theo A17/A20) thắng STATUS map; lý do nằm trong annotation "actual"
                verdict = [a.get("description", "").strip() for a in anns if a.get("type") == "verdict"]
                if verdict and verdict[-1] not in VERDICTS:
                    print(f"[WARN] {m.group(1)}: verdict '{verdict[-1]}' không thuộc {sorted(VERDICTS)} — dùng status của Playwright")
                    verdict = []
                err = (last.get("error") or {}).get("message", "")
                files = [(a.get("name", ""), a["path"]) for a in last.get("attachments", [])
                         if a.get("path") and not a["path"].lower().endswith(SKIP_EXT)]
                found[m.group(1)] = {
                    "status": verdict[-1] if verdict else STATUS.get(last.get("status"), last.get("status")),
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
    original = a.testcases.read_text(encoding="utf-8")
    data = json.loads(original)
    res = collect(json.loads(a.results.read_text(encoding="utf-8")))
    base = a.testcases.parent
    evdir = a.evidence_dir or base / "evidence"
    hit = dup = 0
    for s in data.get("suites", []):
        for k, c in enumerate(s.get("cases", [])):
            r = res.get(c.get("id"))
            if not r:
                continue
            hit += 1
            # auto_status = kết quả tự động gốc (Playwright, hoặc annotation verdict của script); status có thể được SV chỉnh sau
            c = {**{kk: vv for kk, vv in c.items() if kk != "auto_status"}}
            items = list(c.items())
            pos = next((j for j, (kk, _) in enumerate(items) if kk == "status"), len(items) - 1)
            items = [(kk, vv) for kk, vv in items if kk != "status"]
            items[pos:pos] = [("status", r["status"]), ("auto_status", r["status"])]
            c = dict(items)
            s["cases"][k] = c
            c["actual_result"] = r["actual"] or (f"(không ghi actual) {r['error']}" if r["error"] else "")
            ev, used, seen = [], set(), set()
            for att_name, p in r["evidence"]:
                src = Path(p)
                if not src.exists():
                    continue
                h = hashlib.sha256(src.read_bytes()).hexdigest()
                if h in seen:          # trùng nội dung với attachment trước của cùng case → giữ file đầu
                    dup += 1
                    continue
                seen.add(h)
                dst = evdir / evidence_name(c["id"], att_name, src, used)
                if not a.dry_run:
                    evdir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                try:
                    ev.append(str(dst.resolve().relative_to(base.resolve())).replace("\\", "/"))
                except ValueError:
                    ev.append(str(dst))
            c["evidence"] = ", ".join(ev)
            print(f"{c['id']}: {r['status']}  {c['actual_result'][:80]}")
    if dup:
        print(f"Bỏ {dup} attachment trùng nội dung.")
    missing = set(res) - {c.get("id") for s in data.get("suites", []) for c in s.get("cases", [])}
    for m in sorted(missing):
        print(f"[WARN] {m} có trong kết quả nhưng không có trong {a.testcases.name}")
    print(f"Đã gộp {hit} test case.")
    if not a.dry_run:
        a.testcases.write_text(dump_like_source(original, data), encoding="utf-8")


if __name__ == "__main__":
    main()
