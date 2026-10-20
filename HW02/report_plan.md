# HW02 – Kế hoạch nộp bài

> Lập ngày 21/10/2026 từ `context/HW02_assignment.md` (đề), skill `cs423-ai-first-homework` (AI-01, Homework Policies) và kiểm kê thật thư mục `HW02/` (ls/glob/du) tại commit `015505b`.
> File làm việc, xoá hoặc giữ ngoài zip khi nộp (SV quyết).

## a) Biểu mẫu AI cho HW02

| Mã | Biểu mẫu | Bắt buộc? | Nộp khi nào | AI làm | SV làm | Khác bảng mặc định của skill |
|---|---|---|---|---|---|---|
| AI-01 | Thoả thuận sử dụng AI | Không nộp | — | Tra điều khoản | Đọc | — |
| AI-02 | AI Audit Report | **Có** (đề §9, §14: "AI Critique and AI Audit Report (Markdown + PDF)") | Trong zip, `ai-forms/` + phụ lục report | Chuyển form → .md; điền mục (1)(2) từ prompt log / `ai-outputs/`; đếm artifact; tính tỉ lệ VALID/INVALID/INCOMPLETE | **Verdict cuối** 🔒, lý do, phần sửa; kết luận; ký | Đề §9 yêu cầu thêm: câu tuyên bố nguyên văn *"I use AI tools for the following tasks,"* và với **mỗi interaction**: tên tool, ngày giờ, prompt, output (đáp ứng bằng prompt log trích tự động + bảng artifact) |
| AI-03 | Disclosure Form | **Có** (AI-01: mọi bài có dùng AI; đề không nêu tên form, chỉ "Use the content of the given AI Templates if needed") | Trong zip, `ai-forms/` | Điền tool (Claude Sonnet 4.6, Claude Opus 5.5, các lượt "không rõ model"), số lượt, dải mã #, giai đoạn, cách tạo prompt log | Xác nhận đúng sự thật, chọn 2–3 prompt quan trọng, ký | Không |
| AI-05 | Privacy & Responsible-AI Checklist | **Có** (AI-01, làm cuối) | Trong zip, `ai-forms/`, sau AI-02/03 | Tick mục có bằng chứng, gợi ý ghi chú minh bạch | Tự tick mục cam kết cá nhân 🔒, ký | Không |
| AI-06 | Student Acknowledgement | Một lần tuần 1 | Tuần 1 | — | **SV xác nhận đã nộp tuần 1?** (repo không có file AI-06; `HW01/ai-forms/` cũng không có) | — |

AI-04 không đưa vào: đề HW02 không yêu cầu (HW thường, Cấp 4).

File cần có trong `HW02/ai-forms/` (hiện **rỗng**):
- `AI-02_Audit_Report_23120255.md` + `.pdf` (ký)
- `AI-03_Disclosure_Form_23120255.md` + `.pdf` (ký)
- `AI-05_Privacy_Checklist_23120255.md` + `.pdf` (ký)
- `signature.png` (HW01 có trong `HW01/ai-forms/`; SV tự đặt)

## b) Bảng điểm, cấp độ AI, ánh xạ G9.x

Cấp độ AI: **Cấp 4** (AI hỗ trợ sản xuất; SV thiết kế, audit, tích hợp). Bloom-AI đề yêu cầu: **G9.2 + G9.3** (đề §3, §8).

| No. | Tiêu chí (đề §15) | Điểm |
|---|---|---|
| 1 | Feature A – FR-01 (Domain + Boundary) | 25 |
| 2 | Feature B – FR-07 (Domain + Boundary) | 25 |
| 3 | Feature C – FR-15 (Domain + Boundary) | 25 |
| 4 | Feature D – FR-20 Mobile (Domain + Boundary) | 15 |
| 5 | Agent Skills | 10 |
|  | **Tổng** | **100** |

| Requirement (đề) | Nội dung | G9.x | Ghi chú |
|---|---|---|---|
| §6.1 Domain Testing | AI sinh nháp từng bước (biến → lớp → minimum set), SV review, chạy, tinh chỉnh | G9.2 (+ G9.3 khi audit) | Bước 1–3, 6 |
| §6.2 BVA | AI sinh nháp BVA 9 điểm, SV review, chạy | G9.2 (+ G9.3) | Bước 4, 6 |
| §6.3 AI gap analysis | SV tự bổ sung case/bug AI bỏ sót, giải thích **vì sao** (prompt / giới hạn công cụ / độ phức tạp) | **G9.3** | Bước 5 🔒 |
| §6.4 Bug reporting | Bug trong report .md **và** GitHub Issues nhóm, có ảnh | (AI-01 §11: 100% SV viết) | Bước 7 🔒 |
| §7 Agent Skill + video | Skill `domain-bva-testing` + video YouTube end-to-end trên 1 feature | G9.5 (vượt mức đề) | 10 điểm |
| §9 AI Audit Report | Log tool/giờ/prompt/output; verdict từng artifact | G9.3 | AI-02 |
| §10 AI Critique | 200–300 từ: AI sai/bias/thiếu ở đâu, vì sao, nguyên tắc học được | G9.3 | 🔒 |
| §9 gợi ý "skill or rule that extracts…" | Script trích prompt log tự động | G9.5 | `tools/extract_prompt_log.py` |
| §5 chọn feature không trùng nhóm, Issues chung của nhóm | | G9.4 (gián tiếp) | Không chấm riêng |

## c) Danh sách file/mục phải nộp

Nguồn: đề §6, §7, §9, §10, §12, §14, §17 + Homework Policies (skill §1). Trạng thái kiểm bằng ls/glob/du ngày 21/10/2026.

| # | Mục | Căn cứ | Đường dẫn | Trạng thái |
|---|---|---|---|---|
| 1 | Report chính .md (Domain + BVA) | đề §14 | `HW02/report.md` (tên tạm, khung) | **CẦN CẬP NHẬT** – khung tạo ở commit này; README đang ghi `23120255_HW02_Report.md` |
| 2 | Report chính PDF | đề §14 | — | **THIẾU** |
| 3 | Bảng TC từng feature (nguồn cho report) | đề §6.1–6.2 | `HW02/{A_FR01,B_FR07,C_FR15,D_FR20}/testcases.md` + `.json` | ĐÃ CÓ |
| 4 | Giải thích từng bước Domain + BVA | đề §6.1–6.2 | trong report | **THIẾU** |
| 5 | AI gap analysis từng feature 🔒 | đề §6.3 | dữ kiện: `*/sv_cases.md`, `*/ai_gap_answer.md`, `B_FR07/sv_questions.md`, `C_FR15/sv_questions.md` | **THIẾU** phần viết trong report (dữ kiện ĐÃ CÓ) |
| 6 | Bug report .md | đề §6.4, §14 | `HW02/bugs/BUG-01.md` … `BUG-57.md` (57 file) | ĐÃ CÓ – **CẦN CẬP NHẬT**: 8 file còn chữ "(chưa kiểm chứng)" (BUG-04, 08, 13, 36, 41, 43, 47, 52) → SV xác nhận giữ/bỏ |
| 7 | Bug trong report .md (bảng) | đề §6.4 | trong report | **THIẾU** (khung cột trống) |
| 8 | Ảnh trang GitHub Issues | đề §14 | `HW02/bugs/issues_page_{A_FR01,B_FR07,C_FR15,D_FR20}.png` | ĐÃ CÓ |
| 9 | Ảnh lỗi đính kèm từng issue | đề §6.4 | trên GitHub; bản che `HW02/bugs/_issue_redacted/`; evidence `*/evidence/` | ĐÃ CÓ |
| 10 | AI Critique 200–300 từ 🔒 | đề §10, §14 (.md + PDF) | — | **THIẾU** |
| 11 | AI Audit Report .md + PDF (AI-02) | đề §9, §14 | `HW02/ai-forms/` (rỗng) | **THIẾU** |
| 12 | Mandatory Disclosure | AI-01 | report + AI-02 (nguyên văn giống nhau) | **THIẾU** |
| 13 | AI-03 Disclosure .md + PDF ký | AI-01 | `HW02/ai-forms/` | **THIẾU** |
| 14 | AI-05 Privacy Checklist .md + PDF ký | AI-01 | `HW02/ai-forms/` | **THIẾU** |
| 15 | Prompt log | đề §9; AI-01 | `HW02/appendix/A_prompt_log.md` (363 lượt `## #`) | **CẦN CẬP NHẬT**: `prompt_log_notes.toml` mới có 1 entry (`2026-10-12 21:20`, Mục đích/Xử lý `[...]`); 2 lượt "Claude (không rõ model)" (#118, #272); trích lại lần cuối trước nộp |
| 16 | Output AI gốc | AI-02 mục (2) | `HW02/appendix/ai-outputs/` (56 file) | ĐÃ CÓ |
| 17 | Git commit log (text) | đề §12, §14 | `HW02/appendix/commit_log.txt` | **THIẾU** (`tools/export_commit_log.ps1` có sẵn). Commit theo bước: A, B, C, D đều có đủ 1/7…7/7 |
| 18 | Tự đánh giá | đề §14, §15 | `HW02/README.md` bảng "Tự đánh giá" | **CẦN CẬP NHẬT** (ô `[...]`) |
| 19 | Test summary (số feature, TC thiết kế/chạy/pass/fail/chưa chạy, số bug) | đề §14 | `HW02/README.md` khối `SUMMARY` (sinh bởi `tools/summary.py`) | ĐÃ CÓ – **CẦN CẬP NHẬT** lần cuối |
| 20 | Video demo skill (YouTube link) | đề §7, §14 | `HW02/README.md` mục Video (`[...]`); `HW02/skills/VideoLinks.md` | **THIẾU** |
| 21 | Agent Skill | đề §7 | nguồn `.claude/skills/domain-bva-testing/`; đích `HW02/skills/domain-bva-testing/` | **THIẾU** (chép khi nộp) |
| 22 | README.md | đề §14 | `HW02/README.md` | ĐÃ CÓ – **CẦN CẬP NHẬT** (dòng "Công cụ AI: [...]", tên file report) |
| 23 | Tài liệu hỗ trợ | đề §14 | `HW02/env/environment.md`, `HW02/env/mobile_api_url.patch`, `HW02/tests/` (Playwright), `*/RUN.md`, `D_FR20/compare_web_mobile.md` | ĐÃ CÓ |
| 24 | Bản PDF cho mỗi .md | Homework Policies | — | **THIẾU** – phạm vi cần chốt (xem d.6) |
| 25 | Tên zip | đề §14 | `23120255_HW02_AI_DomainTesting_<ggg>.zip` | chưa tạo; `ggg` = tổng tự đánh giá |
| 26 | ≤ 20 file Moodle, mỗi file ≤ 20 MB | Homework Policies | — | **RỦI RO**: zip thử `HW02/` (bỏ `tests/node_modules`, `D_FR20/manual_raw`) = **35,6 MB** > 20 MB; không có file lẻ > 20 MB |

## d) Chỗ mâu thuẫn / dễ sót trong đề

1. Bảng thông tin chung ghi Bloom-AI "G9.1 → G9.6, tuỳ bài"; §3 và §8 chốt **G9.2 + G9.3** → theo §3/§8.
2. Bảng thông tin chung ghi "Submission: Moodle (report)"; §14 yêu cầu zip đủ nội dung → theo §14.
3. §9 chỉ yêu cầu tool/giờ/prompt/output mỗi interaction + câu tuyên bố *"I use AI tools for the following tasks,"*; không nêu AI-03/AI-05 → vẫn nộp theo AI-01; câu tuyên bố phải có nguyên văn (đặt ở đầu Audit và report).
4. §10 Critique và §14 "AI Critique and AI Audit Report (Markdown + PDF)": không rõ Critique là file riêng hay mục trong report/Audit → đặt trong report **và** trong AI-02, hoặc file riêng (SV chốt).
5. §14 "Bug report, with screenshots of the bugs on the GitHub Issues page": đọc được hai nghĩa (ảnh trang Issues / ảnh lỗi trong từng issue) → đã có cả hai.
6. Homework Policies: "bản PDF cho **mỗi** file .md"; đề §14 chỉ đòi PDF cho report chính và Critique + Audit → cần chốt có xuất PDF cho `BUG-xx.md`, `testcases.md`, prompt log (1,6 MB) hay không.
7. §7 Agent Skill "encouraged" nhưng rubric cho **10 điểm**; đề nói "demonstration videos" (số nhiều), video phải có trong README (§14) → thiếu video = mất điểm, có thể bị coi là thiếu tài liệu bắt buộc (§17: thiếu = 0).
8. Đề không quy định tên report chính → khung tạm `HW02/report.md`; README + CLAUDE.md §6 dùng `23120255_HW02_Report.md` → phải thống nhất một tên.
9. §6.4 "bug trong Markdown report": bảng bug trong report do SV viết (AI-01 §11) — AI chỉ dựng cột.
10. §11 Anti-AI-cheat "None": không cần ảnh thẻ SV / hostname watermark; video vẫn do SV tự quay, tự thuyết minh.
11. §13 vấn đáp ngẫu nhiên 30% (AI-01 ghi 10–30%) → chuẩn bị giải thích từng bước, lý do chọn input.
12. §17 "Copying … including prompts" → không chia sẻ skill/prompt với nhóm (skill nằm trong bài nộp cá nhân).
13. Pool D trong đề không liệt kê FR; chọn FR-20 (đăng ký mobile) theo SRS – nên ghi căn cứ trong report.
14. Dung lượng 35,6 MB (mục c.26) → cần nén ảnh hoặc split-and-zip; Moodle ≤ 20 file (đếm cả các phần split).

## e) File form gốc

- Không có file `.docx` AI-02/03/05 trong repo (`find -iname "*.docx"` rỗng).
- Bản .md đã chuyển của HW01 (có thể dùng làm mẫu): `HW01/ai-forms/AI-02_Audit_Report_23120255.md`, `HW01/ai-forms/AI-03_Disclosure_Form_23120255.md`, `HW01/ai-forms/AI-05_Privacy_Checklist_23120255.md` (kèm PDF, `signature.png`). Bản AI gốc: `HW01/appendix/ai-outputs/AI-0{2,3,5}_*.md`.
- Chưa chuyển đổi.
