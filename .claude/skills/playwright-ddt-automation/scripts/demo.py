#!/usr/bin/env python3
"""Chế độ demo (v2.1): dựng một bộ chạy Playwright riêng trong <dir> cho một feature với số TC thu nhỏ,
không chạm data/spec/report/ai-outputs chính thức. Dùng để quay video Agent Skill hoặc chạy thử skill E2E.

Bố cục sinh ra (mặc định <dir> = HW04/tests/_demo — phải nằm DƯỚI HW04/tests để Node tìm thấy node_modules):
  <dir>/playwright.config.ts   testDir ./tests, testIgnore ai-outputs/reports, report → <dir>/reports/<project>_<ts>/
  <dir>/tests/fixtures/ddt.ts  từ assets/ddt-fixture.template.ts (đọc data ở <dir>/data qua DDT_DATA_DIR)
  <dir>/tests/<X_FRnn>.demo.ts khung từ assets/spec.template.ts (bước 3 AI viết tiếp); đuôi .demo.ts để config
                               chính thức (testMatch *.spec.ts) không nạp spec demo
  <dir>/data/                  bước 1: select_tc.py --data <dir>/data/<X_FRnn>.json
  <dir>/<X_FRnn>/              selection.json/.md, results.md, bug_groups.md
  <dir>/ai-outputs/            freeze.py --out <dir>/ai-outputs --testdir <dir>/tests (ngoài testDir, đuôi .txt)
  <dir>/reports/               HTML report + results.json của từng lượt

Đường dẫn: spec ở <dir>/tests/ → import fixture './fixtures/ddt'; page object chính thức HW04/tests/pages/ →
'<rel>/pages/…' (script in ra <rel>). globalSetup dùng HW04/tests/global-setup.ts.

Usage (chạy từ gốc repo):
  python .claude/skills/playwright-ddt-automation/scripts/demo.py --feature A_FR01 [--dir HW04/tests/_demo] [--min 4]
Dọn: xoá thư mục <dir> (không có liên kết/junction, xoá thường được).
"""
import argparse
import os
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

SKILL = Path(__file__).resolve().parent.parent
TESTS = Path("HW04/tests")

CONFIG = """import {{ defineConfig, devices }} from '@playwright/test';
import path from 'node:path';

// CHẾ ĐỘ DEMO (skill playwright-ddt-automation v2.1) — sinh bởi demo.py, không phải bộ chạy chính thức.
const STUDENT_ID = '{mssv}';
function isoLocal(d: Date): string {{
  const off = -d.getTimezoneOffset();
  const pad = (n: number) => String(Math.abs(n)).padStart(2, '0');
  const local = new Date(d.getTime() + off * 60_000).toISOString().slice(0, 19);
  return `${{local}}${{off >= 0 ? '+' : '-'}}${{pad(Math.trunc(off / 60))}}:${{pad(off % 60)}}`;
}}
process.env.HW04_RUN_ISO ??= isoLocal(new Date());
process.env.DDT_DATA_DIR ??= path.join(__dirname, 'data');      // fixture đọc data demo, không đọc HW04/data
const RUN_ISO = process.env.HW04_RUN_ISO;
const RUN_TAG = RUN_ISO.slice(0, 19).replace(/[-:]/g, '');
const projects = process.argv
  .flatMap((a, i, all) => (a.startsWith('--project=') ? [a.slice(10)] : a === '--project' ? [all[i + 1]] : []))
  .filter(Boolean);
const PROJECT_TAG = projects.length ? projects.join('+') : 'all';
const RUN_BY = `Run by: ${{STUDENT_ID}} · ${{RUN_ISO}}`;
const REPORT_DIR = path.join(__dirname, 'reports', `${{PROJECT_TAG}}_${{RUN_TAG}}`);

export default defineConfig({{
  testDir: './tests',
  testMatch: /.*\\.demo\\.ts$/,   // KHÔNG dùng *.spec.ts: config chính thức (testDir HW04/tests, testMatch *.spec.ts) sẽ nạp spec demo
  testIgnore: ['**/ai-outputs/**', '**/reports/**'],   // bản đóng băng không bao giờ bị nạp
  globalSetup: '{global_setup}',
  fullyParallel: false,
  workers: 1,
  retries: 0,
  outputDir: './test-results',
  metadata: {{ 'Run by': `${{STUDENT_ID}} · ${{RUN_ISO}}`, 'Chế độ': 'demo (không chính thức)' }},
  reporter: [
    ['list'],
    ['html', {{ title: `DEMO {feature} – ${{PROJECT_TAG}} – ${{RUN_BY}}`, outputFolder: REPORT_DIR, open: 'never' }}],
    ['json', {{ outputFile: path.join(REPORT_DIR, 'results.json') }}],
  ],
  use: {{ screenshot: 'only-on-failure', trace: 'off', video: 'off', locale: 'vi-VN', timezoneId: 'Asia/Ho_Chi_Minh' }},
  projects: [
    {{ name: 'chrome', use: {{ ...devices['Desktop Chrome'], channel: 'chrome' }} }},
    {{ name: 'edge', use: {{ ...devices['Desktop Edge'], channel: 'msedge' }} }},
    {{ name: 'firefox', use: {{ ...devices['Desktop Firefox'] }} }},
  ],
}});
"""


def posix_rel(target: Path, start: Path) -> str:
    r = os.path.relpath(target.resolve(), start.resolve()).replace("\\", "/")
    return r if r.startswith(".") else "./" + r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature", required=True)
    ap.add_argument("--dir", type=Path, default=TESTS / "_demo")
    ap.add_argument("--min", type=int, default=4)
    ap.add_argument("--mssv", default="23120255")
    a = ap.parse_args()
    d = a.dir
    if TESTS.resolve() not in d.resolve().parents:
        raise SystemExit(f"{d} phải nằm dưới {TESTS} (Node tìm @playwright/test ở {TESTS}/node_modules)")
    if d.exists() and any(d.iterdir()):
        raise SystemExit(f"{d} đã có nội dung — xoá thư mục demo cũ trước")
    for sub in ("tests/fixtures", "data", a.feature, "ai-outputs", "reports"):
        (d / sub).mkdir(parents=True, exist_ok=True)

    (d / "playwright.config.ts").write_text(
        CONFIG.format(mssv=a.mssv, feature=a.feature, global_setup=posix_rel(TESTS / "global-setup.ts", d)),
        encoding="utf-8", newline="\n")
    (d / "tests/fixtures/ddt.ts").write_text(
        (SKILL / "assets/ddt-fixture.template.ts").read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    spec = (SKILL / "assets/spec.template.ts").read_text(encoding="utf-8").replace("const FEATURE = 'X_FRnn';",
                                                                                f"const FEATURE = '{a.feature}';")
    (d / f"tests/{a.feature}.demo.ts").write_text(spec, encoding="utf-8", newline="\n")

    S = SKILL.relative_to(Path.cwd().resolve()).as_posix() + "/scripts" if SKILL.is_relative_to(Path.cwd().resolve()) else str(SKILL / "scripts")
    D, F = d.as_posix(), a.feature
    cfg = posix_rel(d / "playwright.config.ts", TESTS)
    print(f"Đã dựng chế độ demo {F} trong {D}")
    print(f"  page object chính thức từ spec demo: import … from '{posix_rel(TESTS / 'pages', d / 'tests')}/<file>'")
    print("Lệnh từng bước (chạy từ gốc repo; bước 4 chạy trong HW04/tests):")
    print(f"  1  python {S}/select_tc.py HW02/{F}/testcases.json --candidates")
    print(f"     python {S}/select_tc.py HW02/{F}/testcases.json --selection {D}/{F}/selection.json --data {D}/data/{F}.json --md {D}/{F}/selection.md")
    print(f"     python {S}/check_data.py {D}/data/{F}.json --min {a.min}")
    print(f"     python {S}/freeze.py --feature {F} --step 1 --out {D}/ai-outputs --testdir {D}/tests {D}/{F}/selection.json {D}/data/{F}.json {D}/{F}/selection.md")
    print(f"  2-3 sửa {D}/tests/fixtures/ddt.ts + {D}/tests/{F}.demo.ts; freeze.py --step 2|3 --out {D}/ai-outputs --testdir {D}/tests <file>")
    print(f"  4  cd {TESTS.as_posix()}; npx tsc --noEmit; npx playwright test --config {cfg} --list --reporter=list")
    print(f"     npx playwright test --config {cfg} --project=chrome   (… edge, firefox)")
    print(f"  6  python {S}/merge_reports.py {D}/data/{F}.json {D}/{F} {D}/reports/chrome_<ts> {D}/reports/edge_<ts> {D}/reports/firefox_<ts>")
    print(f"Dọn: xoá {D} (config chính thức không nạp *.demo.ts; vẫn nên xoá demo trước khi chạy lượt chính thức).")


if __name__ == "__main__":
    main()
