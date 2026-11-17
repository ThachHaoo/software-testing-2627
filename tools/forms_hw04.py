"""Sinh khung AI-02 (Audit) cho HW04 và khối Mandatory Disclosure (report §10). Không dùng AI.

    python tools/forms_hw04.py

- Artifact AI tạo: danh mục ART dưới đây + git (commit tạo = commit đầu tiên thêm file chính, hoặc commit chỉ định;
  cột (5) = commit sửa sau đó, chỉ liệt kê).
- Cột #n: "–" (chưa có prompt_log_turns.txt cho HW04; điền sau lần trích prompt log cuối).
- Verdict / Lý do / kết luận / chữ ký: `<SV viết>` — AI không điền; ô SV đã điền được giữ khi chạy lại.
- "Khai cho Audit": chép nguyên văn report_plan.md mục f.
- Số lượt theo model: dòng "**Tổng:**" của HW04/appendix/A_prompt_log.md lúc chạy.
- Mẫu định dạng: tools/forms_hw03.py / HW03/ai-forms (không chép số liệu HW03).
"""
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO = Path(__file__).resolve().parents[1]
HW = REPO / "HW04"
AI02 = HW / "ai-forms" / "AI-02_Audit_Report_23120255.md"
SV = "`<SV viết>`"
TBD = "–"
SK = ".claude/skills/playwright-ddt-automation"
HEAD = ["**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**",
        "**CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**", "**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**", ""]
SIGN = ["## Chữ ký", "", "| Mục | Giá trị |", "|---|---|", "| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |", "| MSSV: | 23120255 |",
        "| Lớp / Khoá: | Software Testing - 23_3 |", "| Môn học: | CSC13003 – Kiểm chứng Phần mềm |",
        "| Giảng viên: | Thầy Lâm Quang Vũ, Thầy Trần Duy Hoàng, Cô Trần Thị Bích Hạnh, Thầy Trương Phước Lộc, Thầy Hồ Tuấn Thanh |",
        "| Ngày: | [...] |", "| Chữ ký: | [...] |", ""]
REFS = ["## Tham khảo", "", "- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.",
        "- ISTQB Foundation Level Syllabus (latest version).", "- Hardman, P. (2025). A Post-AI Learning Taxonomy.",
        "- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.", ""]

FEAT = {"A_FR01": "A", "B_FR07": "B", "C_FR15": "C"}
STEP2 = {"A_FR01": ["a_fr01.ts", "ddt.ts", "register.page.ts", "login.page.ts"], "B_FR07": ["b_fr07.ts", "shop.pages.ts"],
         "C_FR15": ["c_fr15.ts", "admin.pages.ts"]}
STEP3 = {"A_FR01": ["A_FR01.spec.ts", "assertions.md"], "B_FR07": ["B_FR07.spec.ts", "b_fr07.oracle.ts", "assertions.md"],
         "C_FR15": ["C_FR15.spec.ts", "c_fr15.oracle.ts", "assertions.md"]}

# (mã, artifact, [đường dẫn], ghi chú output, [commit chỉ định])
ART = [
    ("H1", "Harness HW04: `HW04/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp)", ["HW04/CLAUDE.md", "HW04/report_plan.md"], "đề tóm tắt, quyết định, khai Audit"),
    ("H2", "Bộ chạy Playwright: config 3 trình duyệt + \"Run by\" + JSON reporter, global-setup, package/tsconfig", ["HW04/tests/playwright.config.ts", "HW04/tests/global-setup.ts", "HW04/tests/package.json", "HW04/tests/tsconfig.json"], "project chrome/edge/firefox, workers 1, retries 0"),
    ("S1", "Agent Skill `playwright-ddt-automation` v1 (SKILL.md, 4 script, 3 asset)", [f"{SK}/SKILL.md", f"{SK}/scripts/select_tc.py", f"{SK}/scripts/merge_reports.py"], "quy trình 6 bước có điểm dừng", "b0e2f7c"),
    ("S2", "Skill v2 – bài học review A/B/C (template fixture/spec, checklist review bước 5)", [f"{SK}/assets/spec.template.ts", f"{SK}/assets/ddt-fixture.template.ts", f"{SK}/SKILL.md"], "bỏ serial, step/until/esc/assumption", "5bb31d1"),
    ("S3", "Skill v2.1 – freeze ngoài testDir, chế độ demo (`demo.py`), chạy thử E2E", [f"{SK}/scripts/demo.py", f"{SK}/scripts/freeze.py"], "4 TC × 3 trình duyệt khớp HW02", "99080b2"),
    ("S4", "Bản chép skill nộp `HW04/skills/` + `VideoLinks.md`", ["HW04/skills/playwright-ddt-automation/SKILL.md", "HW04/skills/VideoLinks.md"], "bản v2.1 @99080b2; link 2 video"),
]
for f, x in FEAT.items():
    base = f"HW04/appendix/ai-outputs/{f}"
    ART += [
        (f"{x}1", f"{f} bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng", [f"{base}/step1/selection.json", f"{base}/step1/{f}.json", f"{base}/step1/selection.md"], "selection + data"),
        (f"{x}2", f"{f} bước 2: fixture + page object – bản đóng băng", [f"{base}/step2/{n}" for n in STEP2[f]], "selector theo mã UI thật"),
        (f"{x}3", f"{f} bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng", [f"{base}/step3/{n}" for n in STEP3[f]], "45 test (15 TC × 3)"),
        (f"{x}4", f"{f} `RUN.md` – dữ kiện lượt thử/chính thức", [f"HW04/{f}/RUN.md"], "bảng lượt chạy, ghi chú lỗi hạ tầng"),
        (f"{x}6", f"{f} bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng", [f"{base}/step6/results.md", f"{base}/step6/bug_groups.md"], "Pass/Fail/Blocked theo trình duyệt, nhóm Fail (dữ kiện)"),
        (f"{x}7", f"{f} `not_automated.md` – TC/phần expected không tự động", [f"HW04/{f}/not_automated.md"], "từ selection.json + annotation report"),
    ]
ART += [
    ("K1", "Dữ kiện nhóm Fail A+B, C (`_groups_AB.md`, `_groups_C.md`)", ["HW04/bugs/_groups_AB.md", "HW04/bugs/_groups_C.md"], "triệu chứng, vị trí mã SUT, issue HW02"),
    ("K2", "Khung 18 bug (Cách 2, chỉ dữ kiện) + `bugs/README.md`", ["HW04/bugs/README.md", "HW04/bugs/BUG-86.md"], "nội dung bug do SV viết", "2667147"),
    ("K3", "Kiểm tái hiện 18 bug bằng Playwright (`repro_check.md`)", ["HW04/bugs/repro_check.md"], "lần 1 lệch, lần 2 không lệch"),
    ("K4", "Tạo 18 GitHub Issue `gh issue create --body-file` (file SV viết) + ảnh trang Issues", ["HW04/bugs/issues_page_1.png"], "#298–#315 trên tkob-team/eshop-sut"),
    ("R1", "README test summary (`tools/hw04_summary.py`)", ["tools/hw04_summary.py", "HW04/README.md"], "khối SUMMARY"),
    ("R2", "Dàn ý report + khối REPORT (`tools/hw04_report.py`)", ["tools/hw04_report.py", "HW04/23120255_HW04_Report.md"], "bảng chọn TC/kết quả/review/bug/audit"),
    ("R3", "Khung AI-02 + khối Mandatory Disclosure §10 (`tools/forms_hw04.py`)", ["tools/forms_hw04.py", "HW04/ai-forms/AI-02_Audit_Report_23120255.md"], "file này"),
    ("P1", "Bộ đọc bản xuất dữ liệu claude.ai cho prompt log", ["tools/extract_prompt_log.py"], "36 lượt claude.ai vào log", "86d4d78"),
    ("D1", "Chạy thử skill E2E ở chế độ demo (nhánh `skill-dryrun`, đã xoá, không commit)", [f"{SK}/scripts/demo.py"], "lỗi phát hiện → S3", "99080b2"),
]


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a], capture_output=True, text=True, encoding="utf-8").stdout.strip()


def created(paths):
    out = git("log", "--diff-filter=A", "--format=%h|%ad|%s", "--date=format:%d/%m/%Y %H:%M", "--", paths[0]).splitlines()
    if not out:
        return None
    h, d, s = out[-1].split("|", 2)
    return h, d, s


def fixed(h):
    h2, d, s = git("log", "-1", "--format=%h|%ad|%s", "--date=format:%d/%m/%Y %H:%M", h).split("|", 2)
    return h2, d, s


def later(paths, first):
    return list(reversed(git("log", "--format=%h %s", f"{first}..HEAD", "--", *paths).splitlines()))


def totals():
    f = HW / "appendix" / "A_prompt_log.md"
    m = re.search(r"^\*\*Tổng:\*\* (.+)$", f.read_text(encoding="utf-8"), re.M)
    line = m.group(1) if m else ""
    n = re.match(r"(\d+) lượt", line)
    parts = re.findall(r"(Claude [^;]+?) (\d+) lượt", line)
    when = dt.datetime.fromtimestamp(f.stat().st_mtime).strftime("%H:%M %d/%m/%Y")
    return (int(n.group(1)) if n else 0), parts, when


def rows():
    out = []
    for code, name, paths, note, *fix in ART:
        c = fixed(fix[0]) if fix else created(paths)
        if not c:
            out.append((code, name, "chưa commit", note + " · " + ", ".join(f"`{p}`" for p in paths[:3]), "–"))
            continue
        h, d, s = c
        lt = later(paths, h)
        mod = ("; ".join(f"`{x.split(' ', 1)[0]}` {x.split(' ', 1)[1]}" for x in lt[:4]) + (f"; … (+{len(lt) - 4})" if len(lt) > 4 else "")) if lt else "không có"
        out.append((code, name, f"Claude Code · {d} · `{h}` ({s}) · {TBD}",
                    f"{note} · " + ", ".join(f"`{p}`" for p in paths[:3]) + (" …" if len(paths) > 3 else ""), mod.replace("|", "\\|")))
    return out


def kept():
    if not AI02.exists():
        return {}
    t = AI02.read_text(encoding="utf-8")
    out = {}
    sec = t.split("### 3.2", 1)[-1].split("## 4.", 1)
    for line in sec[0].splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 4 and re.fullmatch(r"[A-Z]\d+", c[0]) and (c[2] != SV or c[3] != SV):
            out[c[0]] = (c[2], c[3])
    if len(sec) > 1:
        kl = sec[1].split("## 5.", 1)[0].split("\n", 1)[-1].strip()
        if kl and kl != SV:
            out["_kl"] = kl
    return out


def plan_section(letter: str) -> list[str]:
    t = (HW / "report_plan.md").read_text(encoding="utf-8")
    m = re.search(rf"^## {letter}\. [^\n]*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    return m.group(1).strip("\n").splitlines() if m else ["_(không thấy mục trong report_plan.md)_"]


def ai02(tot):
    n, parts, when = tot
    tools = "; ".join(f"{p[0]} {p[1]} lượt" for p in parts)
    L = HEAD + ["# AI Audit Report — Mẫu 5 mục cho mỗi Artifact", "", "*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW#01–HW#06, Seminar).*", "",
                "## 1. Thông tin Sinh viên", "", "| Mục | Giá trị |", "|---|---|", "| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |", "| MSSV: | 23120255 |",
                "| Lớp / Khoá: | Software Testing - 23_3 |", "| Mã bài tập: | HW04-AI – Automation Testing on EShop |", "| Ngày làm bài: | 16/11/2026 – 18/11/2026 |",
                f"| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — {tools} (tổng {n} lượt theo dòng Tổng của `appendix/A_prompt_log.md`, bản trích {when}) |",
                "| Có sử dụng AI: | [x] Có [ ] Không |", "", "**Tuyên bố sử dụng AI (đề):** xem report chính §10 Mandatory Disclosure.", "",
                "## 2. Hướng dẫn", "", "- Mỗi artifact do AI tạo là 1 hàng. Mục (1) Prompt + công cụ + thời gian + mã `#n`, (2) Output, (5) Bản SV sửa ở bảng 3.1; mục (3) Verdict và (4) Lý do ở bảng 3.2 (em viết).",
                "- Prompt và output nguyên văn: `appendix/A_prompt_log.md` theo mã `#n`; output dạng file đóng băng: `appendix/ai-outputs/` (`INDEX.md`).",
                "- Bảng theo từng commit HW04: report §9.",
                f"- Cột #n để \"{TBD}\" tới lần trích prompt log cuối.", "",
                "## 3. Bảng Audit — 1 hàng / artifact", "", "### 3.1 Mục (1), (2), (5)", "",
                "| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |", "|---|---|---|---|---|"]
    R = rows()
    L += ["| " + " | ".join(r) + " |" for r in R]
    L += ["", f"*{len(R)} artifact. Sinh bằng `tools/forms_hw04.py` từ danh mục trong script + `git log` (commit tạo = commit đầu tiên thêm file chính – đường dẫn đầu ở cột (2) – hoặc commit chỉ định cho skill v1/v2/v2.1, khung bug, bộ đọc claude.ai). Cột (5) chỉ liệt kê commit, không diễn giải.*", "",
          "### 3.2 Mục (3), (4) – em điền", "", "*Verdict: VALID / INVALID / INCOMPLETE. Lý do: 1–2 câu, dẫn ISTQB/slide. #n để mở `appendix/A_prompt_log.md`.*", "",
          "| Mã | #n | (3) Verdict | (4) Lý do |", "|---|---|---|---|"]
    keep = kept()
    for code, *_ in R:
        v, ly = keep.get(code, (SV, SV))
        L.append(f"| {code} | {TBD} | {v} | {ly} |")
    L += ["", "### 3.3 Khai cho Audit (chép nguyên văn `report_plan.md` mục f)", ""] + plan_section("f")
    L += ["", "## 4. Kết luận chung", "", keep.get("_kl", SV), "", "## 5. AI Critique", "", "Xem report chính `23120255_HW04_Report.md` §8.", ""] + SIGN + REFS
    return "\n".join(L)


def disclosure():
    L = ["📝 AI nháp – SV xác nhận", "", "*\"I use AI tools for the following tasks,\"*", ""]
    items = [
        "Dựng harness bài làm: `HW04/CLAUDE.md`, kế hoạch nộp, bộ chạy Playwright (3 trình duyệt Chrome/Edge/Firefox, \"Run by\" + ISO timestamp, global-setup), `tools/hw04_summary.py`, `tools/hw04_report.py`, `tools/forms_hw04.py`.",
        "Agent Skill `playwright-ddt-automation` v1 → v2 (bài học review A/B/C) → v2.1 (freeze ngoài testDir, chế độ demo, chạy thử E2E); bản nộp ở `skills/`.",
        "Chọn 15 TC/feature từ HW02 và tạo file data JSON (expected chép nguyên văn + sha1) cho A, B, C; em duyệt danh sách và giả định (`assumptions`).",
        "Viết page object, fixture, 3 spec data-driven, 2 parser oracle và bảng assertion; bản nháp đóng băng ở `appendix/ai-outputs/` trước khi em review.",
        "Ghi dữ kiện lượt chạy (`RUN.md`), gộp 3 report/feature (`results.md`, `bug_groups.md`, `evidence/`), sửa script theo từng điểm em review (commit `5/6x`), liệt kê TC không tự động (`not_automated.md`).",
        "Gom dữ kiện nhóm Fail (`bugs/_groups_AB.md`, `bugs/_groups_C.md`), dựng khung 18 bug chỉ chứa dữ kiện, tái hiện bước em viết bằng Playwright (`bugs/repro_check.md`), tạo 18 GitHub Issue (#298–#315) bằng `gh issue create --body-file` với file em viết, chụp ảnh trang Issues.",
        "Sinh bảng README/report (khối `SUMMARY`, `REPORT`), dàn ý report, khung AI-02.",
        "Thêm bộ đọc bản xuất dữ liệu claude.ai vào `tools/extract_prompt_log.py` để prompt log có cả phiên thảo luận.",
        "Phiên thảo luận claude.ai: lập kế hoạch, đối chiếu code khi em review (`review_sv.md`), soạn khối lệnh cho Claude Code.",
    ]
    L += [f"{k}. {t}" for k, t in enumerate(items, 1)]
    L += ["", "Em xem xét và sửa: `<SV viết>`", "", "Em tự làm hoàn toàn: `<SV viết>`", "",
          "Prompt log: trích tự động bằng `tools/extract_prompt_log.py` (hook `tools/hooks/on_stop.py`); Section / Mục đích / Xử lý do em ghi. Danh mục artifact AI: `ai-forms/AI-02_Audit_Report_23120255.md`.",
          "", "*Sinh bằng `tools/forms_hw04.py` từ `report_plan.md` mục f, g.*"]
    return "\n".join(L)


def main():
    if AI02.exists() and "signature.png" in AI02.read_text(encoding="utf-8"):
        raise SystemExit("AI-02 đã có phần SV (chữ ký) – không ghi đè; sửa tay.")
    AI02.parent.mkdir(exist_ok=True)
    tot = totals()
    AI02.write_text(ai02(tot), encoding="utf-8", newline="\n")
    rp = HW / "23120255_HW04_Report.md"
    t = rp.read_text(encoding="utf-8")
    b, e = "<!-- REPORT:disclosure:BEGIN -->", "<!-- REPORT:disclosure:END -->"
    ok = b in t and e in t
    if ok:
        t = t[:t.index(b) + len(b)] + "\n" + disclosure() + "\n" + t[t.index(e):]
        rp.write_text(t, encoding="utf-8", newline="\n")
    print(f"AI-02 đã ghi ({len(ART)} artifact); tổng {tot[0]} lượt ({tot[2]}); §10: {'đã ghi' if ok else 'CHƯA CÓ MARKER'}")


if __name__ == "__main__":
    main()
