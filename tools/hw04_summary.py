"""Sinh bảng test summary HW04 cho README từ dữ liệu đã commit (không gõ tay số liệu).

Nguồn:
- Số TC automated: HW04/data/<feature>.json (testcases).
- Lượt chính thức: các dòng có chữ "Chính thức" trong HW04/<feature>/RUN.md, lấy đường dẫn HW04/reports/<dir>/.
- Verdict từng test: results.json của report chính thức, phân loại bằng verdict() của merge_reports.py (cùng quy tắc bước 6).
- Commit có sửa .spec.ts: git log -- 'HW04/tests/*.spec.ts'.
Ghi đè phần giữa <!-- SUMMARY:BEGIN --> và <!-- SUMMARY:END --> trong HW04/README.md.

Chạy: python tools/hw04_summary.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".claude/skills/playwright-ddt-automation/scripts"))
from merge_reports import verdict, walk  # noqa: E402

FEATURES = [("A_FR01", "A – FR-01 Đăng ký"), ("B_FR07", "B – FR-07 Giỏ hàng"), ("C_FR15", "C – FR-15 Quản lý sản phẩm (admin)")]
BROWSERS = ["chrome", "edge", "firefox"]
BEGIN, END = "<!-- SUMMARY:BEGIN -->", "<!-- SUMMARY:END -->"


def official_reports(feature: str) -> dict:
    out = {}
    for line in (ROOT / f"HW04/{feature}/RUN.md").read_text(encoding="utf-8").splitlines():
        if "Chính thức" not in line:
            continue
        m = re.search(r"HW04/reports/((chrome|edge|firefox)_\d{8}T\d{6})/", line)
        if m:
            if m.group(2) in out:
                raise SystemExit(f"{feature}: RUN.md có hơn 1 lượt chính thức cho {m.group(2)}")
            out[m.group(2)] = m.group(1)
    missing = [b for b in BROWSERS if b not in out]
    if missing:
        raise SystemExit(f"{feature}: RUN.md thiếu lượt chính thức cho {missing}")
    return out


def count(report_dir: str) -> dict:
    rj = json.loads((ROOT / "HW04/reports" / report_dir / "results.json").read_text(encoding="utf-8"))
    tests = []
    for s in rj.get("suites", []):
        walk(s, tests)
    c = {"Pass": 0, "Fail": 0, "Blocked": 0, "Not run": 0}
    for _, t in tests:
        c[verdict(t)[0]] += 1
    c["runby"] = rj.get("config", {}).get("metadata", {}).get("Run by", "")
    return c


def main():
    rows, tot = [], {"auto": 0, "exec": 0, "Pass": 0, "Fail": 0, "Blocked": 0, "runs": 0}
    for feat, label in FEATURES:
        n = len(json.loads((ROOT / f"HW04/data/{feat}.json").read_text(encoding="utf-8"))["testcases"])
        tot["auto"] += n
        for b, d in official_reports(feat).items():
            c = count(d)
            executed = c["Pass"] + c["Fail"] + c["Blocked"]
            rows.append(f"| {label} | {b} | {n} | {executed} | {c['Pass']} | {c['Fail']} | {c['Blocked']} | `HW04/reports/{d}/` · {c['runby']} |")
            tot["exec"] += executed
            for k in ("Pass", "Fail", "Blocked"):
                tot[k] += c[k]
            tot["runs"] += 1
    spec_commits = subprocess.run(["git", "log", "--oneline", "--", "HW04/tests/*.spec.ts"], cwd=ROOT,
                                  capture_output=True, text=True, encoding="utf-8", check=True).stdout.strip().splitlines()
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()

    md = [BEGIN, f"_Sinh bởi `python tools/hw04_summary.py` (HEAD lúc sinh: `{head}`) — không sửa tay._", "",
          "| Chỉ số | Giá trị |", "|---|---|",
          f"| Số feature | {len(FEATURES)} |",
          f"| Số TC automated (data-driven) | {tot['auto']} |",
          f"| Số lượt chạy chính thức (feature × trình duyệt) | {tot['runs']} |",
          f"| Số lượt test thực thi (TC × trình duyệt) | {tot['exec']} |",
          f"| Pass / Fail / Blocked | {tot['Pass']} / {tot['Fail']} / {tot['Blocked']} |",
          f"| Số commit có sửa `HW04/tests/*.spec.ts` | {len(spec_commits)} |",
          "| Số bug (GitHub Issues) | [...] |",
          "| Video demo | [...] |",
          "| Video Agent Skill | [...] |", "",
          "| Feature | Trình duyệt | TC automated | Executed | Pass | Fail | Blocked | Report · Run by |",
          "|---|---|---|---|---|---|---|---|", *rows, END]
    readme = ROOT / "HW04/README.md"
    text = readme.read_text(encoding="utf-8") if readme.exists() else ""
    if BEGIN in text and END in text:
        text = text[:text.index(BEGIN)] + "\n".join(md) + text[text.index(END) + len(END):]
    else:
        text = text.rstrip() + ("\n\n" if text else "") + "\n".join(md) + "\n"
    readme.write_text(text, encoding="utf-8", newline="\n")
    print(f"Đã ghi {readme.relative_to(ROOT)}: {tot['runs']} lượt chính thức, {len(spec_commits)} commit .spec.ts")


if __name__ == "__main__":
    main()
