#!/usr/bin/env python3
"""
Sinh 3 biểu mẫu AI-02, AI-03, AI-05 (.md) cho HW02 từ report chính và prompt log. Không dùng AI.

- Bảng và đoạn văn lấy nguyên văn từ report (§10, §12, tuyên bố §9) và từ prompt log (dòng Tổng, tiêu đề lượt, prompt).
- Ô SV phải tự điền/ký/tick để `[...]` hoặc `[ ]` kèm "(em tự xác nhận)".
- Chạy lại sau lần trích prompt log cuối và sau khi report chốt: số liệu tự cập nhật.

Cách dùng (từ gốc repo):  python tools/build_forms.py HW02
"""
import importlib.util
import re
import sys
import tomllib
from pathlib import Path

REPORT = "23120255_HW02_Report.md"
LOG = "appendix/A_prompt_log.md"
KEY_PROMPTS = [(17, "A_FR01 bước 0–1 (gọi skill, giới hạn test basis)"),
               (35, "A_FR01 bước 5 (hỏi AI vì sao bỏ sót, sau khi em tự thêm case)"),
               (31, "A_FR01 bước 4 (BVA)")]
MAXP = 1500
HEAD = ["**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**",
        "**CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**",
        "**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**", ""]
SIGN = ["## Chữ ký", "", "| Mục | Giá trị |", "|---|---|",
        "| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |", "| MSSV: | 23120255 |", "| Lớp / Khoá: | Software Testing - 23_3 |",
        "| Môn học: | CSC13003 – Kiểm chứng Phần mềm |",
        "| Giảng viên: | Thầy Lâm Quang Vũ, Thầy Trần Duy Hoàng, Cô Trần Thị Bích Hạnh, Thầy Trương Phước Lộc, Thầy Hồ Tuấn Thanh |",
        "| Ngày: | [...] |", "| Chữ ký: | [...] |", ""]
REFS = ["## Tham khảo", "",
        "- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.",
        "- ISTQB Foundation Level Syllabus (latest version).",
        "- Hardman, P. (2025). A Post-AI Learning Taxonomy.",
        "- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.",
        "- Anthropic (2025). Building reliable AI test agents — engineering blog.", ""]


def section(t, start, end):
    i = t.index(start)
    j = t.index(end, i + len(start))
    return t[i:j]


def clean(block, drop_heading=True):
    """Bỏ dòng marker HTML, dòng 📝 và (tuỳ chọn) dòng tiêu đề đầu; giữ nguyên phần còn lại."""
    lines = block.splitlines()
    if drop_heading and lines and lines[0].startswith("#"):
        lines = lines[1:]
    out = [l for l in lines if not l.startswith("<!--") and not l.startswith("> 📝")]
    return "\n".join(out).strip("\n")


def demote(block, by=1):
    return re.sub(r"(?m)^(#{2,5}) ", lambda m: "#" * (len(m.group(1)) + by) + " ", block)


def load_turns(hw):
    spec = importlib.util.spec_from_file_location("at", "tools/audit_tables.py")
    at = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(at)
    return at.turns_of(hw)


def totals(log):
    line = next(l for l in log.splitlines() if l.startswith("**Tổng:**"))
    total = int(re.search(r"\*\*Tổng:\*\* (\d+) lượt", line).group(1))
    models = [(m.group(1).strip(), int(m.group(2)), m.group(3)) for m in re.finditer(r";\s*(.+?) (\d+) lượt \((#[^)]*)\)", line)]
    mixed = re.search(r"(\d+) lượt có output từ hơn một model", line)
    return total, models, int(mixed.group(1)) if mixed else 0


def prompt_of(log, n):
    m = re.search(rf"(?ms)^## #{n} \|([^\n]*)\n.*?\*\*Prompt:\*\*\n(`{{3,}})\n(.*?)\n\2\n", log)
    return (m.group(1).strip(), m.group(3)) if m else ("", "")


def main():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    hw = Path(sys.argv[1] if len(sys.argv) > 1 else "HW02")
    rep = (hw / REPORT).read_text(encoding="utf-8")
    log = (hw / LOG).read_text(encoding="utf-8")
    turns = load_turns(hw)
    total, models, mixed = totals(log)
    extra = tomllib.loads(Path(hw / "appendix" / "prompt_log_extra.toml").read_text(encoding="utf-8")).get("entry", [])
    d0, d1 = turns[0][1], turns[-1][1]
    model_line = "; ".join(f"{m} {c} lượt" for m, c, _ in models)
    unknown = next((ids for m, c, ids in models if "không rõ" in m), "")
    decl = clean(section(rep, "**Tuyên bố sử dụng AI", "## Mục lục"), drop_heading=False)
    sec12 = clean(section(rep, "## 12. Mandatory Disclosure", "## 13."))
    s101 = clean(section(rep, "### 10.1", "### 10.2"))
    s102 = clean(section(rep, "### 10.2", "### 10.3"))
    s103 = clean(section(rep, "### 10.3", "### 10.4"))
    s104 = clean(section(rep, "### 10.4", "### 10.5"))
    s106 = clean(section(rep, "### 10.6", "## 11."))
    tools_cell = f"Claude (Anthropic) qua Claude Code và claude.ai — {model_line} (tổng {total} lượt; {mixed} lượt có output từ hơn một model được đếm ở cả hai)"
    period = f"{d0:%d/%m/%Y} – {d1:%d/%m/%Y}"

    # ---------- AI-02 ----------
    a2 = HEAD + ["# AI Audit Report — Mẫu 5 mục cho mỗi Artifact", "",
                 "*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW#01–HW#06, Seminar).*", "",
                 "## 1. Thông tin Sinh viên", "", "| Mục | Giá trị |", "|---|---|",
                 "| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |", "| MSSV: | 23120255 |", "| Lớp / Khoá: | Software Testing - 23_3 |",
                 "| Mã bài tập: | HW02-AI – Domain Testing on EShop |", f"| Ngày làm bài: | {period} |",
                 f"| Công cụ AI đã dùng: | {tools_cell} |", "| Có sử dụng AI: | [x] Có [ ] Không |", "",
                 decl, "",
                 "## 2. Hướng dẫn", "",
                 "- Mỗi artifact do AI tạo là 1 hàng. Mục (1) Prompt + công cụ + thời gian + mã `#n`, (2) Output, (5) Bản SV sửa ở bảng 3.1; mục (3) Verdict và (4) Lý do ở bảng 3.2 (em viết).",
                 "- Prompt và output nguyên văn đầy đủ: `appendix/A_prompt_log.md` theo mã `#n`; output dạng file: `appendix/ai-outputs/`.",
                 "- Bảng chép nguyên văn từ report chính §10 (sinh bằng `tools/audit_tables.py`, `tools/build_forms.py`).", "",
                 "## 3. Bảng Audit — 1 hàng / artifact", "",
                 "### 3.1 Mục (1), (2), (5)", "", s101, "",
                 "### 3.2 Mục (3), (4)", "", s102, "",
                 "### 3.3 Đánh giá từng TC do AI sinh", "", s103, "",
                 "## 4. Tổng kết Độ chính xác AI", "", s104, "",
                 s106.replace("\n- ", "\n- ", 1) if s106 else "", "",
                 "## 5. Kết luận — Khi nào nên / không nên dùng AI?", "",
                 "Xem report chính `23120255_HW02_Report.md` mục 10.5.", "",
                 "## 6. AI Critique", "", "Xem report chính `23120255_HW02_Report.md` mục 11 (R4: Critique chỉ nằm trong report).", "",
                 "## 7. Mandatory Disclosure (dán nguyên văn report §12)", "", sec12, ""] + SIGN + REFS
    (hw / "ai-forms" / "AI-02_Audit_Report_23120255.md").write_text("\n".join(a2), encoding="utf-8")

    # ---------- AI-03 ----------
    secs = []
    for n, tm, mdl, sec in turns:
        key = sec or "[chưa có section]"
        if not secs or secs[-1][0] != key:
            secs.append([key, n, n, tm, tm])
        else:
            secs[-1][2], secs[-1][4] = n, tm
    stage_rows = ["| Section (theo `prompt_log_notes.toml`) | Lượt | Thời gian |", "|---|---|---|"] + \
                 [f"| {s} | #{a}–#{b} | {t0:%H:%M %d/%m} – {t1:%H:%M %d/%m} |" for s, a, b, t0, t1 in secs]
    kp = []
    for i, (n, why) in enumerate(KEY_PROMPTS, 1):
        hdr, p = prompt_of(log, n)
        body = p if len(p) <= MAXP else p[:MAXP] + f"\n… (cắt ở {MAXP} ký tự; nguyên văn đầy đủ ở #{n})"
        kp += [f"{i}. **#{n} – {hdr}** — {why}:", "", "   ```", *["   " + l for l in body.splitlines()], "   ```", ""]
    ai_did = next((l for l in sec12.splitlines() if l.startswith("| Phần AI tạo bản đầu")), "")
    ai_not = next((l for l in sec12.splitlines() if l.startswith("| Danh mục cấm")), "")
    sv_all = next((l for l in sec12.splitlines() if l.startswith("| Phần em tự viết hoàn toàn")), "")
    sv_rev = next((l for l in sec12.splitlines() if l.startswith("| Phần em xem xét và sửa")), "")
    plog = next((l for l in sec12.splitlines() if l.startswith("| Cách tạo prompt log")), "")
    cell = lambda row: row.split("|")[2].strip() if row else "[...]"
    a3 = HEAD + ["# Biểu mẫu Khai báo Sử dụng AI", "", "*Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.*", "",
                 "## 1. Thông tin Môn học & Sinh viên", "", "| Mục | Giá trị |", "|---|---|",
                 "| Môn học: | CSC13003 – Kiểm chứng Phần mềm |", "| Mã bài tập: | HW02-AI |", "| Tên bài tập: | Domain Testing on EShop |",
                 "| Cấp độ AI (1–5): | Cấp 4 |", "| Ngày: | [...] |", "| Họ tên sinh viên: | Lê Tấn Hiệp |", "| MSSV: | 23120255 |", "",
                 "## 2. Câu hỏi Khai báo", "",
                 "### 1. Công cụ AI đã dùng:", ""] + \
         [f"- **{m}** – {c} lượt" + (f" ({ids})" if "không rõ" in m else "") for m, c, ids in models] + \
         [f"- Tổng {total} lượt theo dòng \"Tổng\" của `appendix/A_prompt_log.md`; {mixed} lượt có output từ hơn một model nên được đếm ở cả hai. Danh sách mã `#n` từng model ở dòng đó.",
          f"- Trong đó {len(extra)} lượt chép tay vào `appendix/prompt_log_extra.toml` ({extra[0]['time'].replace('T', ' ')} – {extra[-1]['time'].replace('T', ' ')}; công cụ ghi: {', '.join(sorted({e['tool'] for e in extra}))}), vì không có trong transcript tự động." if extra else "",
          f"- Các lượt ghi \"Claude (không rõ model)\" ({unknown}): transcript không ghi model; giữ nguyên theo P3, lý do từng lượt em ghi trong `appendix/prompt_log_notes.toml`.",
          "- Kênh: Claude Code (chạy lệnh, sửa file, commit trong repo) và claude.ai (phiên thảo luận, lập lệnh, review). Không dùng GitHub Copilot, Cursor, Gemini, ChatGPT.", "",
          "### 2. Giai đoạn nào của bài tập có dùng AI:", "",
          "[x] brainstorm [x] outline [x] viết nháp [x] phản hồi [x] sửa chữa [x] code [x] phân tích dữ liệu [ ] thiết kế đồ hoạ [x] khác (thiết kế test case theo từng bước, chạy lệnh, gom dữ kiện bug)", "",
          "Theo section em ghi trong prompt log:", "", *stage_rows, "",
          "### 3. Prompt / nhiệm vụ chính cho AI:", "",
          "*Nguyên văn đầy đủ ở `appendix/A_prompt_log.md` theo mã `#n`.*", "", *kp,
          "### 4. Phần cụ thể AI đóng góp:", "", cell(ai_did), "",
          "**Phần AI KHÔNG đóng góp (em tự làm):** " + cell(sv_all), "",
          "**Danh mục AI không được làm:** " + cell(ai_not), "",
          "### 5. Cách em rà soát / chỉnh sửa / xác minh đầu ra AI:", "",
          "- " + cell(sv_rev),
          "- Bản nháp AI mỗi bước được đóng băng ở `appendix/ai-outputs/` trước khi em sửa; chạy `check_domain.py` (độ phủ EC), linter `lint_testcases.py`, `render_md.py`.",
          "- Expected đối chiếu SRS; chỗ SRS im lặng ghi giả định và em chốt trước khi dùng.",
          "- Chạy thật toàn bộ test trên máy em (Playwright cho A, B, C; chạy tay trên Android cho D); bug kiểm tái hiện, so UI với API trước khi kết luận.",
          "- Đối chiếu dữ kiện bằng script: `appendix/gap_check.md` (gap analysis ↔ JSON), `appendix/audit_check.md` (Lý do Audit ↔ git), `tools/summary.py` (số liệu report ↔ JSON).",
          "- Cách tạo prompt log: " + cell(plog), "",
          "### 6. Trích dẫn tool AI sử dụng:", "",
          *[x for i, (m, _, _) in enumerate([y for y in models if "không rõ" not in y[0]], 1)
            for x in (f"[{i}] Anthropic. (2026). *{m}* [Large language model]. https://claude.ai", "")],
          f"[{len([y for y in models if 'không rõ' not in y[0]]) + 1}] Anthropic. (2026). *Claude Code* [Software]. https://claude.com/claude-code", "",
          "## 3. Cam đoan Trung thực", "",
          "*Bằng việc ký tên dưới đây, em cam đoan thông tin khai báo ở trên là chính xác và đầy đủ. Em hiểu rằng việc không khai báo hoặc khai báo sai lệch về việc dùng AI sẽ bị coi là vi phạm liêm chính học thuật và có thể dẫn đến điểm 0 cho bài tập cùng việc bị chuyển lên hội đồng kỷ luật.*", ""] + SIGN + REFS
    (hw / "ai-forms" / "AI-03_Disclosure_Form_23120255.md").write_text("\n".join(x for x in a3 if x is not None), encoding="utf-8")

    # ---------- AI-05 ----------
    crit = section(rep, "## 11. AI Critique", "## 12.")
    crit_words = len(re.findall(r"\w+", "\n".join(l for l in crit.splitlines()[1:] if not l.startswith(">"))))
    forms_ok = all((hw / "ai-forms" / f).exists() for f in ("AI-02_Audit_Report_23120255.md", "AI-03_Disclosure_Form_23120255.md"))
    ev = lambda ok, text, note: f"- [{'x' if ok else ' '}] {text} — *{note}*"
    me = lambda text, note="": f"- [ ] {text} (em tự xác nhận)" + (f" — *{note}*" if note else "")
    a5 = HEAD + ["# Bảng Kiểm Quyền Riêng tư & Sử dụng AI Có Trách nhiệm", "",
                 "**Bài tập:** HW02-AI – Domain Testing on EShop",
                 f"**Công cụ AI:** {model_line} (tổng {total} lượt, khớp AI-03 mục 1) – chi tiết ở AI-03 và `appendix/A_prompt_log.md`", "",
                 "*Chỉ tick mục có bằng chứng trong repo (ghi ở cuối dòng). Mục cam kết cá nhân để trống cho em tự xác nhận.*", "",
                 "## 1. Trước khi dùng AI", "",
                 ev(True, "Đã xác nhận Cấp độ AI cho bài tập này.", "report chính, bảng đầu: Cấp 4"),
                 me("Dùng tài khoản Claude tự chọn (không phải tài khoản cá nhân)."),
                 me("Đã đọc Thoả thuận AI của môn học."),
                 ev(True, "Hiểu rõ artifact nào KHÔNG được sinh bằng AI.", "danh mục cấm ở report §12 và `CLAUDE.md` §3"), "",
                 "## 2. Trong khi dùng AI", "",
                 me("Không nhập dữ liệu cá nhân của bạn, khách hàng, bệnh nhân.", "ghi chú minh bạch: họ tên, MSSV, email của em có trong `CLAUDE.md` và prompt"),
                 me("Không paste nguyên si tài liệu có bản quyền lên AI.", "ghi chú minh bạch: AI đọc slide bài giảng trong `context/private/` (không commit) và SRS/mã nguồn SUT của môn"),
                 me("Không paste code công ty / code open-source giới hạn license.", "ghi chú minh bạch: AI đọc mã nguồn SUT `ttbhanh/eshop-sut` do môn cung cấp"),
                 ev(True, "Đã ghi mọi prompt + phản hồi AI vào prompt log có timestamp.", f"`appendix/A_prompt_log.md` ({total} lượt, trích tự động)"), "",
                 "## 3. Trước khi nộp bài", "",
                 ev("### 10.1" in rep, "Mọi artifact AI sinh đã được gắn tag trong AI Audit Report.", "report §10.1–10.3, AI-02"),
                 me("Mọi trích dẫn AI đã được xác minh (nguồn thực sự tồn tại)."),
                 me("Mọi code AI sinh đã được thực thi và test.", "bằng chứng một phần: kết quả lượt chính thức ở `tests/results/`, `D_FR20/results/`"),
                 ev(200 <= crit_words <= 300, "AI Critique 200–300 chữ đã có trong báo cáo.", f"report §11, đếm script ≈ {crit_words} từ"),
                 ev("## 12. Mandatory Disclosure" in rep, "Đoạn Mandatory Disclosure ở cuối báo cáo.", "report §12"),
                 ev(forms_ok, "Đính kèm AI Use Disclosure Form.", "`ai-forms/AI-03_Disclosure_Form_23120255.md`"),
                 me("Sẵn sàng cho vấn đáp ngẫu nhiên 5–7 phút tuần kế nộp bài."), "",
                 "## 4. Cam đoan Cuối cùng", "",
                 "*Em xác nhận đã rà soát danh sách trên; các mục chưa tick do em tự xác nhận trước khi ký.*", ""] + SIGN + REFS
    (hw / "ai-forms" / "AI-05_Privacy_Checklist_23120255.md").write_text("\n".join(a5), encoding="utf-8")
    print(f"Đã sinh 3 form vào {hw / 'ai-forms'} ({total} lượt; Critique ≈ {crit_words} từ)")


if __name__ == "__main__":
    main()
