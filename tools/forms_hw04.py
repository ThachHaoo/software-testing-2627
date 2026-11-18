"""Sinh khung AI-02 (Audit) cho HW04 và khối Mandatory Disclosure (report §10). Không dùng AI.

    python tools/forms_hw04.py

- Artifact AI tạo: danh mục ART dưới đây + git (commit tạo = commit đầu tiên thêm file chính, hoặc commit chỉ định;
  cột (5) = commit sửa sau đó, chỉ liệt kê).
- Cột #n: "–" (chưa có prompt_log_turns.txt cho HW04; điền sau lần trích prompt log cuối).
- AI-02 mục 3.1 chép bảng §9 của report (verdict/lý do em viết ở đó; hw04_report.py giữ khi sinh lại); 3.2 tỉ lệ verdict.
- AI-03: model theo dòng Tổng; lượt claude.ai = Claude Opus 5.5 (SV xác nhận). AI-05: mục cam kết để [ ] "(em tự xác nhận)".
- Kết luận / cam đoan / chữ ký: `<SV viết>` / [...] — AI không điền.
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
AI03 = HW / "ai-forms" / "AI-03_Disclosure_Form_23120255.md"
AI05 = HW / "ai-forms" / "AI-05_Privacy_Checklist_23120255.md"
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


def plan_section(letter: str) -> list[str]:
    t = (HW / "report_plan.md").read_text(encoding="utf-8")
    m = re.search(rf"^## {letter}\. [^\n]*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    return m.group(1).strip("\n").splitlines() if m else ["_(không thấy mục trong report_plan.md)_"]


def audit_table(report: str) -> list[str]:
    """Bảng §9 của report (giữa marker REPORT:audit) – verdict/lý do em viết ở đó."""
    b, e = "<!-- REPORT:audit:BEGIN -->", "<!-- REPORT:audit:END -->"
    return report[report.index(b) + len(b):report.index(e)].strip("\n").splitlines()


def verdict_count(report: str) -> dict:
    c = {"VALID": 0, "INVALID": 0, "INCOMPLETE": 0, "SV làm": 0, "chưa có": 0}
    for line in audit_table(report)[2:]:
        cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
        v = cells[-2].strip() if len(cells) >= 7 else ""
        if v in ("VALID", "INVALID", "INCOMPLETE"):
            c[v] += 1
        elif v.startswith("—"):
            c["SV làm"] += 1
        else:
            c["chưa có"] += 1
    return c


def ratio_lines(c: dict) -> list[str]:
    n = c["VALID"] + c["INVALID"] + c["INCOMPLETE"]
    pct = lambda k: f"{c[k]} ({c[k] * 100 / n:.0f}%)" if n else str(c[k])
    return ["| Verdict | Số artifact (commit AI) |", "|---|---|",
            f"| VALID | {pct('VALID')} |", f"| INVALID | {pct('INVALID')} |", f"| INCOMPLETE | {pct('INCOMPLETE')} |",
            f"| Tổng có verdict | {n} |", "",
            f"Không tính: {c['SV làm']} commit SV làm (\"— (SV làm…)\")" + (f"; {c['chưa có']} commit AI chưa có verdict (`<SV viết>`)." if c["chưa có"] else ".")]


def ai02(tot, report):
    n, parts, when = tot
    tools = "; ".join(f"{p[0]} {p[1]} lượt" for p in parts)
    c = verdict_count(report)
    L = HEAD + ["# AI Audit Report — Mẫu 5 mục cho mỗi Artifact", "", "*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW#01–HW#06, Seminar).*", "",
                "## 1. Thông tin Sinh viên", "", "| Mục | Giá trị |", "|---|---|", "| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |", "| MSSV: | 23120255 |",
                "| Lớp / Khoá: | Software Testing - 23_3 |", "| Mã bài tập: | HW04-AI – Automation Testing on EShop |", "| Ngày làm bài: | 16/11/2026 – 18/11/2026 |",
                f"| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — {tools} (tổng {n} lượt theo dòng Tổng của `appendix/A_prompt_log.md`, bản trích {when}); lượt claude.ai: Claude Opus 5.5 (em xác nhận, log ghi \"không rõ model\") – AI-03 mục 1 |",
                "| Có sử dụng AI: | [x] Có [ ] Không |", "", "**Tuyên bố sử dụng AI (đề):** xem report chính §10 Mandatory Disclosure.", "",
                "## 2. Hướng dẫn", "",
                "- Mỗi commit HW04 là một artifact (lấy từ `git log`): mục (1) công cụ + thời gian + commit, (2) output = message + file trong commit, (5) commit sửa sau đó = các hàng kế tiếp cùng chủ đề; mục (3) Verdict và (4) Lý do do em viết.",
                "- Prompt và output nguyên văn: `appendix/A_prompt_log.md`; output dạng file đóng băng: `appendix/ai-outputs/` (`INDEX.md`).",
                "- Commit do em làm (viết/sửa/chốt/hoàn thiện) ghi \"— (SV làm…)\" và không tính vào tỉ lệ verdict.", "",
                "## 3. Bảng Audit — 1 hàng / artifact", "",
                "### 3.1 Theo commit (chép từ report §9)", ""] + audit_table(report) + [
                "", "### 3.2 Tỉ lệ verdict", ""] + ratio_lines(c) + [
                "", "### 3.3 Danh mục artifact theo file (tham chiếu – verdict theo commit tạo ở 3.1)", "",
                "| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |", "|---|---|---|---|---|"]
    R = rows()
    L += ["| " + " | ".join(r) + " |" for r in R]
    L += ["", f"*{len(R)} artifact. Sinh bằng `tools/forms_hw04.py` từ danh mục trong script + `git log`.*", "",
          "### 3.4 Khai cho Audit (chép nguyên văn `report_plan.md` mục f)", ""] + plan_section("f")
    L += ["", "## 4. Kết luận chung", "", SV, "", "## 5. AI Critique", "", "Xem report chính `23120255_HW04_Report.md` §8.", ""] + SIGN + REFS
    return "\n".join(L)


def claude_ai_export_end() -> str:
    f = REPO / ".transcripts" / "claude-ai_session_HW04_p1.json"
    if not f.exists():
        return ""
    import json
    d = json.loads(f.read_text(encoding="utf-8"))
    m = d.get("chat_messages") or d.get("messages") or []
    if not m:
        return ""
    t = dt.datetime.fromisoformat(m[-1]["created_at"].replace("Z", "+00:00")).astimezone(dt.timezone(dt.timedelta(hours=7)))
    return t.strftime("%H:%M %d/%m/%Y")


def ai03(tot):
    n, parts, when = tot
    end = claude_ai_export_end()
    L = HEAD + ["# Biểu mẫu Khai báo Sử dụng AI", "", "*Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.*", "",
                "## 1. Thông tin Môn học & Sinh viên", "", "| Mục | Giá trị |", "|---|---|", "| Môn học: | CSC13003 – Kiểm chứng Phần mềm |",
                "| Mã bài tập: | HW04-AI |", "| Tên bài tập: | Automation Testing on EShop |", "| Cấp độ AI (1–5): | Cấp 4 |", "| Ngày: | [...] |",
                "| Họ tên sinh viên: | Lê Tấn Hiệp |", "| MSSV: | 23120255 |", "", "## 2. Câu hỏi Khai báo", "", "### 1. Công cụ AI đã dùng:", ""]
    unk = next((p for p in parts if "không rõ" in p[0]), None)
    for name, k in parts:
        if "không rõ" in name:
            continue
        L.append(f"- **{name}** (Claude Code) – {k} lượt")
    if unk:
        L.append(f"- **Claude (không rõ model)** – {unk[1]} lượt trong log:")
        L.append("  - 36 lượt phiên thảo luận claude.ai: bản xuất dữ liệu claude.ai (`conversations.json`) không ghi model; em xác nhận dùng **Claude Opus 5.5** (ghi ở `appendix/prompt_log_notes.toml`, trường `ghi_chu_model`, áp cho các lượt `nguon_luot = \"claude.ai\"`). Log giữ nguyên nhãn \"không rõ model\".")
        L.append("  - #52 (19:45 17/11/2026, Claude Code): lượt `<task-notification>` do Claude Code tự sinh khi một tiến trình nền kết thúc (không phải em gõ); transcript không ghi model cho lượt này (AI chép từ log).")
    L += [f"- Tổng {n} lượt theo dòng \"Tổng\" của `appendix/A_prompt_log.md` (bản trích {when}). Danh sách mã `#n` từng model ở dòng đó."]
    if end:
        L.append(f"- Phiên claude.ai lấy từ bản xuất dữ liệu có lượt cuối lúc {end}; **các lượt claude.ai sau {end} chưa có trong bản xuất** (chưa xuất lại) nên chưa có trong prompt log.")
    L += ["- Kênh: Claude Code (chạy lệnh, sửa file, commit trong repo) và claude.ai (phiên thảo luận \"Homework Testing Software\": lập kế hoạch, soạn lệnh, đối chiếu code khi em review).",
          "- Cách tạo prompt log: hook Stop của Claude Code (`tools/hooks/on_stop.py`) chép transcript vào `.transcripts/` (không nộp) và chạy `tools/extract_prompt_log.py`: chép nguyên văn prompt + output, lọc khối hệ thống, giờ Asia/Saigon, ghi model từng lượt; phiên claude.ai đọc từ bản xuất dữ liệu (`claude-ai_session_HW04_p1.json`). Mốc/bỏ lượt theo `tools/hw.toml`; Section / Mục đích / Xử lý do em ghi trong `prompt_log_notes.toml`. Không sửa tay log.", "",
          "### 2. Giai đoạn nào của bài tập có dùng AI:", "", "`<SV điền>` (tick: brainstorm / outline / viết nháp / phản hồi / sửa chữa / code / phân tích dữ liệu / thiết kế đồ hoạ / khác)", "",
          "### 3. Prompt / nhiệm vụ chính cho AI:", "", "`<SV điền>` (chọn 2–3 lượt tiêu biểu theo mã `#n` trong `appendix/A_prompt_log.md`)", "",
          "### 4. Phần cụ thể AI đóng góp:", "", "Theo danh mục artifact của AI-02 (mục 3.3): " + "; ".join(f"{a[0]} {a[1]}" for a in ART) + ".", "",
          "**Phần AI KHÔNG đóng góp (em tự làm):** `<SV điền>`", "",
          "**Danh mục AI không được làm (CLAUDE.md mục 3, HW04/CLAUDE.md mục 6):** không viết/nháp mô tả bug và nội dung issue; không gợi ý edge case/selector/assertion khi em đang review spec (bước 5); "
          "không viết AI Critique, phần \"vì sao AI sai/bỏ sót\", verdict Audit; không sinh/sửa HTML report (\"Run by\", timestamp); không viết lời thuyết minh video.", "",
          "### 5. Cách em rà soát / chỉnh sửa / xác minh đầu ra AI:", "", SV, "",
          "### 6. Trích dẫn tool AI sử dụng:", "",
          "[1] Anthropic. (2026). *Claude Opus 5.5* [Large language model]. https://claude.ai", "",
          "[2] Anthropic. (2026). *Claude Code* [Software]. https://claude.com/claude-code", "",
          "## 3. Cam đoan Trung thực", "", "*Bằng việc ký tên dưới đây, em cam đoan thông tin khai báo ở trên là chính xác và đầy đủ.* [...]", ""] + SIGN + REFS
    return "\n".join(L)


def ai05(tot):
    n, parts, when = tot
    tools = "; ".join(f"{p[0]} {p[1]} lượt" for p in parts)
    Y = "*(em tự xác nhận)*"
    L = HEAD + ["# Bảng Kiểm Quyền Riêng tư & Sử dụng AI Có Trách nhiệm", "",
                "**Bài tập:** HW04-AI – Automation Testing on EShop",
                f"**Công cụ AI:** {tools} (tổng {n} lượt theo dòng Tổng của `appendix/A_prompt_log.md`, khớp AI-03 mục 1; lượt claude.ai: Claude Opus 5.5 theo em xác nhận)", "",
                "*Chỉ tick mục có bằng chứng trong repo (ghi ở cuối dòng). Mục cam kết cá nhân để trống \"(em tự xác nhận)\".*", "",
                "## 1. Trước khi dùng AI", "",
                "- [x] Đã xác nhận Cấp độ AI cho bài tập này. — *report dòng đầu: Cấp 4; AI-03 mục 1*",
                f"- [ ] Dùng tài khoản Claude tự chọn. {Y}",
                f"- [ ] Đã đọc Thoả thuận AI của môn học. {Y}",
                "- [x] Hiểu rõ artifact nào KHÔNG được sinh bằng AI. — *AI-03 mục 4 \"Danh mục AI không được làm\"; `CLAUDE.md` §3, `HW04/CLAUDE.md` §6*", "",
                "## 2. Trong khi dùng AI", "",
                f"- [ ] Không nhập dữ liệu cá nhân của bạn, khách hàng, bệnh nhân. {Y}",
                "  - **Minh bạch:** log Code Integrity em xuất (`env/firefox_blocked_20261117.txt`) có đường dẫn chứa tên người dùng Windows; tài khoản thử nghiệm dùng tài khoản seed của SUT (`admin@eshop.com`, `test@eshop.com`) và email sinh theo `{ts}`.",
                f"- [ ] Không paste nguyên si tài liệu có bản quyền lên AI. {Y}",
                f"- [ ] Không paste code công ty / code open-source giới hạn license. {Y}",
                f"- [x] Đã ghi mọi prompt + phản hồi AI vào prompt log có timestamp. — *`appendix/A_prompt_log.md` ({n} lượt, trích tự động, giờ Asia/Saigon; lượt claude.ai sau lần xuất dữ liệu cuối chưa có – AI-03 mục 1)*", "",
                "## 3. Trước khi nộp bài", "",
                "- [x] Mọi artifact AI sinh đã được gắn tag trong AI Audit Report. — *AI-02 mục 3.1 (theo commit), 3.3 (theo file), report §9*",
                f"- [ ] Mọi trích dẫn AI đã được xác minh (nguồn thực sự tồn tại). {Y}",
                "- [x] Mọi code AI sinh đã được thực thi và test. — *9 lượt chính thức (3 feature × 3 trình duyệt) `reports/`; `tsc --noEmit` + `--list`; tái hiện bug `bugs/repro_check.md`*",
                "- [x] AI Critique 200–300 chữ đã có trong báo cáo. — *report §8*",
                "- [x] Đoạn Mandatory Disclosure ở cuối báo cáo. — *report §10*",
                "- [x] Đính kèm AI Use Disclosure Form. — *`ai-forms/AI-03_Disclosure_Form_23120255.md`*",
                f"- [ ] Sẵn sàng cho vấn đáp ngẫu nhiên 5–7 phút tuần kế nộp bài. {Y}", "",
                "## 4. Cam đoan Cuối cùng", "", "*Em xác nhận đã rà soát danh sách trên; các mục chưa tick do em tự xác nhận trước khi ký.*", ""] + SIGN + REFS
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
    for f in (AI02, AI03, AI05):
        if f.exists() and "signature.png" in f.read_text(encoding="utf-8"):
            raise SystemExit(f"{f.name} đã có chữ ký – không ghi đè; sửa tay.")
    AI02.parent.mkdir(exist_ok=True)
    tot = totals()
    rp = HW / "23120255_HW04_Report.md"
    t = rp.read_text(encoding="utf-8")
    AI02.write_text(ai02(tot, t), encoding="utf-8", newline="\n")
    AI03.write_text(ai03(tot), encoding="utf-8", newline="\n")
    AI05.write_text(ai05(tot), encoding="utf-8", newline="\n")
    b, e = "<!-- REPORT:disclosure:BEGIN -->", "<!-- REPORT:disclosure:END -->"
    ok = b in t and e in t
    if ok:
        t = t[:t.index(b) + len(b)] + "\n" + disclosure() + "\n" + t[t.index(e):]
        rp.write_text(t, encoding="utf-8", newline="\n")
    print(f"AI-02/03/05 đã ghi; tổng {tot[0]} lượt ({tot[2]}); verdict {verdict_count(t)}; §10: {'đã ghi' if ok else 'CHƯA CÓ MARKER'}")


if __name__ == "__main__":
    main()
