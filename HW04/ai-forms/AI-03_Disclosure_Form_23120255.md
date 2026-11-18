**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**
**CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**
**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# Biểu mẫu Khai báo Sử dụng AI

*Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.*

## 1. Thông tin Môn học & Sinh viên

| Mục | Giá trị |
|---|---|
| Môn học: | CSC13003 – Kiểm chứng Phần mềm |
| Mã bài tập: | HW04-AI |
| Tên bài tập: | Automation Testing on EShop |
| Cấp độ AI (1–5): | Cấp 4 |
| Ngày: | [...] |
| Họ tên sinh viên: | Lê Tấn Hiệp |
| MSSV: | 23120255 |

## 2. Câu hỏi Khai báo

### 1. Công cụ AI đã dùng:

- **Claude Opus 5.5** (Claude Code) – 49 lượt
- **Claude (không rõ model)** – 37 lượt trong log:
  - 36 lượt phiên thảo luận claude.ai: bản xuất dữ liệu claude.ai (`conversations.json`) không ghi model; em xác nhận dùng **Claude Opus 5.5** (ghi ở `appendix/prompt_log_notes.toml`, trường `ghi_chu_model`, áp cho các lượt `nguon_luot = "claude.ai"`). Log giữ nguyên nhãn "không rõ model".
  - #52 (19:45 17/11/2026, Claude Code): lượt `<task-notification>` do Claude Code tự sinh khi một tiến trình nền kết thúc (không phải em gõ); transcript không ghi model cho lượt này (AI chép từ log).
- Tổng 86 lượt theo dòng "Tổng" của `appendix/A_prompt_log.md` (bản trích 08:53 18/11/2026). Danh sách mã `#n` từng model ở dòng đó.
- Phiên claude.ai lấy từ bản xuất dữ liệu có lượt cuối lúc 21:40 17/11/2026; **các lượt claude.ai sau 21:40 17/11/2026 chưa có trong bản xuất** (chưa xuất lại) nên chưa có trong prompt log.
- Kênh: Claude Code (chạy lệnh, sửa file, commit trong repo) và claude.ai (phiên thảo luận "Homework Testing Software": lập kế hoạch, soạn lệnh, đối chiếu code khi em review).
- Cách tạo prompt log: hook Stop của Claude Code (`tools/hooks/on_stop.py`) chép transcript vào `.transcripts/` (không nộp) và chạy `tools/extract_prompt_log.py`: chép nguyên văn prompt + output, lọc khối hệ thống, giờ Asia/Saigon, ghi model từng lượt; phiên claude.ai đọc từ bản xuất dữ liệu (`claude-ai_session_HW04_p1.json`). Mốc/bỏ lượt theo `tools/hw.toml`; Section / Mục đích / Xử lý do em ghi trong `prompt_log_notes.toml`. Không sửa tay log.

### 2. Giai đoạn nào của bài tập có dùng AI:

`<SV điền>` (tick: brainstorm / outline / viết nháp / phản hồi / sửa chữa / code / phân tích dữ liệu / thiết kế đồ hoạ / khác)

### 3. Prompt / nhiệm vụ chính cho AI:

`<SV điền>` (chọn 2–3 lượt tiêu biểu theo mã `#n` trong `appendix/A_prompt_log.md`)

### 4. Phần cụ thể AI đóng góp:

Theo danh mục artifact của AI-02 (mục 3.3): H1 Harness HW04: `HW04/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp); H2 Bộ chạy Playwright: config 3 trình duyệt + "Run by" + JSON reporter, global-setup, package/tsconfig; S1 Agent Skill `playwright-ddt-automation` v1 (SKILL.md, 4 script, 3 asset); S2 Skill v2 – bài học review A/B/C (template fixture/spec, checklist review bước 5); S3 Skill v2.1 – freeze ngoài testDir, chế độ demo (`demo.py`), chạy thử E2E; S4 Bản chép skill nộp `HW04/skills/` + `VideoLinks.md`; A1 A_FR01 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng; A2 A_FR01 bước 2: fixture + page object – bản đóng băng; A3 A_FR01 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng; A4 A_FR01 `RUN.md` – dữ kiện lượt thử/chính thức; A6 A_FR01 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng; A7 A_FR01 `not_automated.md` – TC/phần expected không tự động; B1 B_FR07 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng; B2 B_FR07 bước 2: fixture + page object – bản đóng băng; B3 B_FR07 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng; B4 B_FR07 `RUN.md` – dữ kiện lượt thử/chính thức; B6 B_FR07 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng; B7 B_FR07 `not_automated.md` – TC/phần expected không tự động; C1 C_FR15 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng; C2 C_FR15 bước 2: fixture + page object – bản đóng băng; C3 C_FR15 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng; C4 C_FR15 `RUN.md` – dữ kiện lượt thử/chính thức; C6 C_FR15 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng; C7 C_FR15 `not_automated.md` – TC/phần expected không tự động; K1 Dữ kiện nhóm Fail A+B, C (`_groups_AB.md`, `_groups_C.md`); K2 Khung 18 bug (Cách 2, chỉ dữ kiện) + `bugs/README.md`; K3 Kiểm tái hiện 18 bug bằng Playwright (`repro_check.md`); K4 Tạo 18 GitHub Issue `gh issue create --body-file` (file SV viết) + ảnh trang Issues; R1 README test summary (`tools/hw04_summary.py`); R2 Dàn ý report + khối REPORT (`tools/hw04_report.py`); R3 Khung AI-02 + khối Mandatory Disclosure §10 (`tools/forms_hw04.py`); P1 Bộ đọc bản xuất dữ liệu claude.ai cho prompt log; D1 Chạy thử skill E2E ở chế độ demo (nhánh `skill-dryrun`, đã xoá, không commit).

**Phần AI KHÔNG đóng góp (em tự làm):** `<SV điền>`

**Danh mục AI không được làm (CLAUDE.md mục 3, HW04/CLAUDE.md mục 6):** không viết/nháp mô tả bug và nội dung issue; không gợi ý edge case/selector/assertion khi em đang review spec (bước 5); không viết AI Critique, phần "vì sao AI sai/bỏ sót", verdict Audit; không sinh/sửa HTML report ("Run by", timestamp); không viết lời thuyết minh video.

### 5. Cách em rà soát / chỉnh sửa / xác minh đầu ra AI:

`<SV viết>`

### 6. Trích dẫn tool AI sử dụng:

[1] Anthropic. (2026). *Claude Opus 5.5* [Large language model]. https://claude.ai

[2] Anthropic. (2026). *Claude Code* [Software]. https://claude.com/claude-code

## 3. Cam đoan Trung thực

*Bằng việc ký tên dưới đây, em cam đoan thông tin khai báo ở trên là chính xác và đầy đủ.* [...]

## Chữ ký

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |
| MSSV: | 23120255 |
| Lớp / Khoá: | Software Testing - 23_3 |
| Môn học: | CSC13003 – Kiểm chứng Phần mềm |
| Giảng viên: | Thầy Lâm Quang Vũ, Thầy Trần Duy Hoàng, Cô Trần Thị Bích Hạnh, Thầy Trương Phước Lộc, Thầy Hồ Tuấn Thanh |
| Ngày: | [...] |
| Chữ ký: | [...] |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Hardman, P. (2025). A Post-AI Learning Taxonomy.
- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.
