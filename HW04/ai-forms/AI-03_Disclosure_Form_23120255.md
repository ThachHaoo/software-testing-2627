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
| Ngày: | 18/11/2026 |
| Họ tên sinh viên: | Lê Tấn Hiệp |
| MSSV: | 23120255 |

## 2. Câu hỏi Khai báo

### 1. Công cụ AI đã dùng:

- **Claude Opus 5.5** (Claude Code) – 50 lượt
- **Claude (không rõ model)** – 37 lượt trong log:
  - 36 lượt phiên thảo luận claude.ai: bản xuất dữ liệu claude.ai (`conversations.json`) không ghi model; em xác nhận dùng **Claude Opus 5.5** (ghi ở `appendix/prompt_log_notes.toml`, trường `ghi_chu_model`, áp cho các lượt `nguon_luot = "claude.ai"`). Log giữ nguyên nhãn "không rõ model".
  - #52 (19:45 17/11/2026, Claude Code): lượt `<task-notification>` do Claude Code tự sinh khi một tiến trình nền kết thúc (không phải em gõ); transcript không ghi model cho lượt này (AI chép từ log).
- Tổng 87 lượt theo dòng "Tổng" của `appendix/A_prompt_log.md` (bản trích 09:40 18/11/2026; #87 là lượt chốt nộp, output chép tới lúc commit). Danh sách mã `#n` từng model ở dòng đó.
- Phiên claude.ai lấy từ bản xuất dữ liệu có lượt cuối lúc 21:40 17/11/2026; **các lượt claude.ai sau 21:40 17/11/2026 chưa có trong bản xuất** (chưa xuất lại) nên chưa có trong prompt log.
- Kênh: Claude Code (chạy lệnh, sửa file, commit trong repo) và claude.ai (phiên thảo luận "Homework Testing Software": lập kế hoạch, soạn lệnh, đối chiếu code khi em review).
- Cách tạo prompt log: hook Stop của Claude Code (`tools/hooks/on_stop.py`) chép transcript vào `.transcripts/` (không nộp) và chạy `tools/extract_prompt_log.py`: chép nguyên văn prompt + output, lọc khối hệ thống, giờ Asia/Saigon, ghi model từng lượt; phiên claude.ai đọc từ bản xuất dữ liệu (`claude-ai_session_HW04_p1.json`). Mốc/bỏ lượt theo `tools/hw.toml`; Section / Mục đích / Xử lý do em ghi trong `prompt_log_notes.toml`. Không sửa tay log.

### 2. Giai đoạn nào của bài tập có dùng AI:

- [x] **Brainstorm** (lên phương án quy trình 6 bước DDT, xử lý các điểm quyết định kỹ thuật như trình duyệt thay thế W1=a, giới hạn dung lượng Z1=d, health-check backend C2)
- [x] **Outline** (dựng dàn ý báo cáo chính, kế hoạch nộp bài `report_plan.md` và khung biểu mẫu AI-02, AI-03)
- [x] **Viết nháp** (tạo khung dữ kiện thô cho 18 bug report để SV tự viết nội dung phân tích, nháp phần Mandatory Disclosure §10)
- [x] **Phản hồi** (đối chiếu mã nguồn spec với các nhận xét tự soi của SV trong `review_sv.md` ở bước 5)
- [x] **Sửa chữa** (cập nhật mã nguồn kịch bản theo từng điểm SV chốt sửa ở các commit `5/6x`, nâng cấp Agent Skill từ v1 lên v2.1)
- [x] **Code** (sinh cấu hình Playwright, Page Object, fixture, 3 file spec data-driven, parser oracle và các script Python hỗ trợ trích xuất/gộp báo cáo)
- [x] **Phân tích dữ liệu** (gộp kết quả JSON từ 3 trình duyệt thành `results.md`, gom nhóm lỗi theo chữ ký thất bại trong `bug_groups.md` và thống kê bảng tổng hợp)
- [ ] **Thiết kế đồ hoạ**
- [x] **Khác:** Tự động hóa thao tác CLI (chạy lệnh `gh issue create` đăng tải 18 issue từ file SV viết và chụp ảnh trang GitHub Issues).

### 3. Prompt / nhiệm vụ chính cho AI:

- **Lượt #5 (23:02 16/11/2026 – Claude Opus 5.5, Claude Code):** Dựng quy trình 6 bước data-driven (`playwright-ddt-automation` v1) gồm `SKILL.md`, 4 script kiểm tra/đóng băng/gộp báo cáo và 3 template; cấu hình chạy 3 trình duyệt Chrome/Edge/Firefox kèm reporter `Run by: 23120255` và chọn 15 TC bước 1 cho `A_FR01`.
- **Lượt #14 (00:55 17/11/2026 – Claude Opus 5.5, Claude Code):** Ghi nhận kết quả tự soi `A_FR01.spec.ts` vào `review_sv.md` trước khi sửa mã, sau đó thực hiện 3 commit tách biệt để sửa lỗi đồng bộ API (`users.list()` chờ phản hồi `POST /api/register`), sửa nhóm regex oracle `^(…|…)` kèm escape ký tự đặc biệt và chặn chạy khi `workers > 1`.
- **Lượt #79 (01:13 18/11/2026 – Claude Opus 5.5, Claude Code):** Tự chạy thử nghiệm đầu-cuối (E2E) ở chế độ demo trên nhánh tạm `skill-dryrun` để rà soát và nâng cấp Agent Skill lên v2.1 (khắc phục lỗi nạp nhầm file đóng băng trong `testDir`, lỗi chờ cứng `POST` gây Blocked giả ở form HTML5 và xung đột `testMatch` giữa config chính thức với spec demo).

### 4. Phần cụ thể AI đóng góp:

Theo danh mục artifact của AI-02 (mục 3.3): H1 Harness HW04: `HW04/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp); H2 Bộ chạy Playwright: config 3 trình duyệt + "Run by" + JSON reporter, global-setup, package/tsconfig; S1 Agent Skill `playwright-ddt-automation` v1 (SKILL.md, 4 script, 3 asset); S2 Skill v2 – bài học review A/B/C (template fixture/spec, checklist review bước 5); S3 Skill v2.1 – freeze ngoài testDir, chế độ demo (`demo.py`), chạy thử E2E; S4 Bản chép skill nộp `HW04/skills/` + `VideoLinks.md`; A1 A_FR01 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng; A2 A_FR01 bước 2: fixture + page object – bản đóng băng; A3 A_FR01 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng; A4 A_FR01 `RUN.md` – dữ kiện lượt thử/chính thức; A6 A_FR01 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng; A7 A_FR01 `not_automated.md` – TC/phần expected không tự động; B1 B_FR07 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng; B2 B_FR07 bước 2: fixture + page object – bản đóng băng; B3 B_FR07 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng; B4 B_FR07 `RUN.md` – dữ kiện lượt thử/chính thức; B6 B_FR07 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng; B7 B_FR07 `not_automated.md` – TC/phần expected không tự động; C1 C_FR15 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng; C2 C_FR15 bước 2: fixture + page object – bản đóng băng; C3 C_FR15 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng; C4 C_FR15 `RUN.md` – dữ kiện lượt thử/chính thức; C6 C_FR15 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng; C7 C_FR15 `not_automated.md` – TC/phần expected không tự động; K1 Dữ kiện nhóm Fail A+B, C (`_groups_AB.md`, `_groups_C.md`); K2 Khung 18 bug (Cách 2, chỉ dữ kiện) + `bugs/README.md`; K3 Kiểm tái hiện 18 bug bằng Playwright (`repro_check.md`); K4 Tạo 18 GitHub Issue `gh issue create --body-file` (file SV viết) + ảnh trang Issues; R1 README test summary (`tools/hw04_summary.py`); R2 Dàn ý report + khối REPORT (`tools/hw04_report.py`); R3 Khung AI-02 + khối Mandatory Disclosure §10 (`tools/forms_hw04.py`); P1 Bộ đọc bản xuất dữ liệu claude.ai cho prompt log; D1 Chạy thử skill E2E ở chế độ demo (nhánh `skill-dryrun`, đã xoá, không commit).

**Phần AI KHÔNG đóng góp (em tự làm):**
- **Chốt phạm vi, quyết định kỹ thuật và duyệt đầu vào:** chốt bộ trình duyệt thay thế Chrome/Edge/Firefox (`W1=a`), tắt trace để tối ưu dung lượng report (`Z1=d`), xử lý rủi ro sập backend ở `C_FR15` (`C2=a`), duyệt danh sách 45 TC (15 TC/feature), phân loại các TC Error Guessing (`TC-202`, `TC-211`, `TC-200`, `TC-201`, `TC-205`) và chốt các giả định kiểm thử (`empty_cart_keyword`, `H3`, `C21`, `C24`).
- **Thực thi toàn bộ 9 lượt kiểm thử chính thức và các lượt chạy thử/demo:** tự khởi chạy bộ test trên 3 trình duyệt Chrome, Edge, Firefox để sinh HTML report chính thức có kèm `"Run by: 23120255"` và ISO timestamp; tự chạy kiểm thử cô lập `--repeat-each=3` cho `TC-FR07-60` trên Firefox để xác minh lỗi hạ tầng `0xC0000409`.
- **Tự rà soát mã nguồn kịch bản (Review Bước 5):** tự đọc và ghi nhận trực tiếp các điểm yếu của cả 3 file spec (`review_sv.md`) trước khi đối chiếu và yêu cầu AI sửa mã nguồn.
- **Phân loại và tự viết toàn bộ 18 Bug Report (`BUG-86` đến `BUG-103`):** tự chốt tiêu chí gom nhóm lỗi (`G → BUG` theo Cách 2: hành vi/triệu chứng độc lập), tự viết toàn bộ tiêu đề, mức độ nghiêm trọng (Severity/Priority), tiền điều kiện, các bước tái hiện, Expected, Actual và nhận định kỹ thuật cho cả 18 bug (đồng thời tự chỉnh sửa lại 12 bug sau bước kiểm tái hiện).
- **Quay và thuyết minh 2 video nộp bài:** tự thực hiện và thuyết minh tiếng Việt trực tiếp cho video Task 2 (`https://youtu.be/TNy_QPFwyB4`, kèm lệnh terminal `whoami`/`hostname` và phân tích lỗi `mode: 'serial'`) cùng video demo quy trình 6 bước của Agent Skill (`https://youtu.be/yGC0R2qd92U`).
- **Đánh giá phản biện, kiểm toán và tự chấm điểm:** tự viết phần phân tích nguyên nhân AI sai/bỏ sót, phần AI Critique (200–300 từ), tự chấm và giải trình verdict (`VALID` / `INCOMPLETE` / `INVALID`) cho toàn bộ artifact trong `AI-02`, tự rà soát bảo mật/riêng tư trong `AI-05` và tự chấm điểm trong `README.md`.

**Danh mục AI không được làm (CLAUDE.md mục 3, HW04/CLAUDE.md mục 6):** không viết/nháp mô tả bug và nội dung issue; không gợi ý edge case/selector/assertion khi em đang review spec (bước 5); không viết AI Critique, phần "vì sao AI sai/bỏ sót", verdict Audit; không sinh/sửa HTML report ("Run by", timestamp); không viết lời thuyết minh video.

### 5. Cách em rà soát / chỉnh sửa / xác minh đầu ra AI:

- **Đóng băng đầu ra nháp và kiểm soát tính toàn vẹn dữ liệu (SHA-1):** Mọi đầu ra do AI tạo ở các bước 1, 2, 3 và 6 đều được xuất nguyên trạng vào `HW04/appendix/ai-outputs/<X_FRnn>/step<k>/` trước khi em chỉnh sửa. Dữ liệu kiểm thử (`HW04/data/*.json`) chép nguyên văn cột `Expected` từ HW02 kèm mã băm SHA-1 để script `check_data.py` và fixture tự động đối chiếu, ngăn chặn AI tự ý sửa đổi oracle để làm test xanh giả.
- **Rà soát mã nguồn kịch bản và chia nhỏ commit theo từng lỗi (Bước 5):** Sau khi AI sinh spec và kiểm tra tĩnh (`tsc --noEmit`, `playwright test --list`), em tự chạy test trên 3 trình duyệt, đọc trực tiếp mã nguồn và ghi nhận nhận xét vào `review_sv.md` trước khi đối chiếu. Các điểm yếu phát hiện được (như `mode: 'serial'` khiến 1 Fail chặn 14 TC ở `A_FR01`, `users.list()` gọi trước khi chờ phản hồi `POST`, gõ cứng từ khóa `/trống/i` và selector `.first()` lỏng lẻo ở `B_FR07`, hay ghi trùng sự kiện `invalid` khi gọi `checkValidity()` ở `C_FR15`) đều được yêu cầu AI sửa tách bạch thành từng commit `5/6x` riêng biệt.
- **Xác minh thực thi đa trình duyệt và cô lập lỗi hạ tầng:** Em tự chạy toàn bộ 9 lượt chính thức trên Chrome, Edge, Firefox và kiểm tra thủ công từng file `index.html` để xác nhận có đủ dòng `"Run by: 23120255"` kèm ISO timestamp. Khi gặp sai lệch kết quả trên Firefox (`TC-FR07-60` Fail ở lượt thử 2 do worker crash `0xC0000409` hoặc Firefox bị Windows Code Integrity chặn `spawn UNKNOWN`), em chạy kiểm thử lặp cô lập (`--repeat-each=3`) và đối chiếu log hệ thống để phân định rõ lỗi hạ tầng với bug của SUT.
- **Kiểm tra tái hiện bug thực tế và rà soát thông tin cá nhân trên repo public:** Toàn bộ 18 bug report do em viết đều được chạy kiểm tái hiện thực tế trên trình duyệt (`repro_check.md`) trước khi đẩy lên GitHub Issues; qua đó phát hiện và sửa 12 bug có bước thao tác chưa chuẩn xác (như gõ URL `/cart` làm mất state React thay vì bấm link điều hướng, hoặc lệch số `id` tự tăng của CSDL). Toàn bộ 156 ảnh bằng chứng (`evidence/`) và ảnh chụp trang Issues đều được em trực tiếp rà soát thủ công để đảm bảo không lọt thông tin cá nhân trước khi push lên repository công khai.
- **Kiểm thử đầu-cuối (E2E) và nâng cấp Agent Skill:** Khi chạy demo thực tế trên nhánh tạm `demo-video`, em phát hiện bản skill v1/v2 còn sót lỗi khi chạy độc lập (còn `mode: 'serial'` trong template, file đóng băng trong `testDir` bị Playwright nạp nhầm, chờ cứng request `POST` gây Blocked giả ở form HTML5). Em yêu cầu chạy thử nghiệm E2E trên nhánh `skill-dryrun` và nâng cấp skill lên bản v2.1 (`99080b2`) trước khi đóng gói nộp bài.

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
| Ngày: | 18/11/2026 |
| Chữ ký: | ![Chữ ký](signature.png)  |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Hardman, P. (2025). A Post-AI Learning Taxonomy.
- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.
