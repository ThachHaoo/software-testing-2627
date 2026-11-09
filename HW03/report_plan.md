# HW03 – GUI & Usability · Kế hoạch nộp bài (report_plan)

Lê Tấn Hiệp – 23120255 · Deadline **10:00 11/11/2026** · Cấp độ AI: **Cấp 4** · Bloom-AI: **G9.3 + G9.4** (theo đề §3, §8)

## a. Biểu mẫu AI

| Form | Bắt buộc | File | Ai làm |
|---|---|---|---|
| AI-02 Audit Report | Có | `ai-forms/AI-02_Audit_Report_23120255.md` + `.pdf` | AI điền dữ kiện, tỉ lệ; SV viết verdict + lý do, ký |
| AI-03 Disclosure | Có | `ai-forms/AI-03_Disclosure_23120255.md` + `.pdf` | AI điền công cụ, số lượt, dải #; SV xác nhận, ký |
| AI-04 Reflective | Không | — | HW thường, đề không yêu cầu |
| AI-05 Privacy | Có (làm cuối) | `ai-forms/AI-05_Privacy_Checklist_23120255.md` + `.pdf` | AI tick mục có bằng chứng; SV tick cam kết, ký. Bài có dữ liệu người tham gia → ghi rõ đã che gì |
| AI-06 | Đã nộp tuần 1 | — | — |

Câu tuyên bố nguyên văn: *"I use AI tools for the following tasks,"*. Mẫu định dạng form: `HW02/ai-forms/*.md` (không chép số liệu).

## b. Rubric (đề §15)

| # | Mục | Max | Tự chấm |
|---|---|---|---|
| 1 | Task 1 – GUI Checklist (thiết kế + chạy + bug) | 30 | `<SV>` |
| 2 | Task 2 – Usability (kịch bản + 7 phiên + phân tích) | 40 | `<SV>` |
| 3 | Task 3 – Cross-platform (≥ 3 nền tảng) | 20 | `<SV>` |
| 4 | Agent Skills (+ video YouTube) | 10 | `<SV>` |
| | Tổng = 3 số trong tên zip | 100 | `<SV>` |

## c. Danh sách nộp (đề §14) – trạng thái

| # | Mục | Đường dẫn dự kiến | Trạng thái | Nộp? |
|---|---|---|---|---|
| 1 | Report chính (.md + PDF): checklist report + usability report | `23120255_HW03_Report.md/.pdf` | THIẾU | Có |
| 2 | Bug report + ảnh trang GitHub Issues | `bugs/BUG-58…md`, `bugs/issues_page_HW03.png` | THIẾU | Có |
| 3 | AI Critique (200–300 từ) + Audit (.md + PDF) | report §Critique; `ai-forms/AI-02…` | THIẾU | Có |
| 4 | Commit log (text) | `commit_log.txt` | THIẾU | Có |
| 5 | Excel checklist (> 40 item) + test summary | `excel/23120255_HW03_Checklist.xlsx` | THIẾU | Có |
| 6 | Bằng chứng usability: kịch bản, ghi chú quan sát, SUS, findings xếp hạng, video (nếu có), bảng 7 người | `usability/…` | THIẾU | Có |
| 7 | Ảnh cross-platform (có overlay) | `checklist/evidence/P1_chrome`, `P2_firefox`, `P3_android` | THIẾU | Có |
| 8 | README.md: tự đánh giá + test summary (số màn/flow, item thiết kế/chạy/Pass/Fail, số bug, số người, link video) | `README.md` | THIẾU | Có |
| 9 | Skill + video demo (YouTube) | `skills/…`, `skills/VideoLinks.md` | THIẾU | Có |
| 10 | Prompt log | `appendix/A_prompt_log.md` | THIẾU (đổi `tools/hw.toml` sang HW03) | Có |
| — | Kế hoạch nộp bài (file này) | `report_plan.md` | — | Không (`HW03/.gitattributes`: export-ignore) |

Moodle: ≤ 20 file, mỗi file ≤ 20 MB. Zip: `23120255_HW03_AI_GUIUsability_<ggg>.zip`, đóng gói bằng `git archive` (như HW02 R2).

## d. Mâu thuẫn / dễ sót trong đề

| Mã | Nội dung | Cách xử lý |
|---|---|---|
| M1 | Overlay ảnh: §6 "username dạng email SV" ↔ §11 "MSSV + họ tên" | Overlay đủ email SV + MSSV + họ tên |
| M2 | "Perform Task 1 across ≥ 3 platforms" | **SV chốt: chạy TOÀN BỘ checklist trên mỗi nền tảng** |
| M3 | Đề chỉ có Passed/Failed | **SV chốt: thêm N/A, ghi giả định** (căn cứ slide: checklist chấm Yes/No/N/A) |
| M4 | Không trùng màn chính/flow với thành viên nhóm | Chia C1/C2/C3, U1–U4 (tin nhắn nhóm 04/11) |
| M5 | Bảng đầu "G9.1→G9.6" ↔ §3/§8 "G9.3 + G9.4"; Skill thuộc G9.5 | Ghi G9.3 + G9.4 |
| M6 | Excel bắt buộc ↔ Homework Policies (bảng tổng hợp phải có trong .md) | Excel + chép bảng sang report |
| M7 | Video phiên usability chứa giọng/màn hình người tham gia; 20 MB/file | Xin đồng ý; không đăng công khai; link Drive giới hạn quyền (`[...]` SV chốt) |
| M8 | Commit cho mỗi bước, kể cả **mỗi phiên usability** | ≥ 9 commit Task 2 (plan, pilot, 7 phiên, phân tích) |
| M9 | Flow U1 đi qua chỗ có bug HW02 đã biết (BUG-15…29 giỏ hàng) | Findings ghi "đã biết – BUG-xx", không tạo issue trùng |
| M10 | Đề nói "spec không gán FR cho UI" ↔ SRS `README.md` §8 có **FR-21…FR-24** khớp IA-01…IA-04 | Report nêu ánh xạ IA ↔ FR một lần; dùng FR-21…24 (+ FR-02/03/04/11 phần UI) làm căn cứ Expected |
| M11 | Đề nhắc BrowserStack/LambdaTest "strongly preferred" | Không dùng: trial 30 phút Live, 1 phút/thiết bị (BrowserStack), phiên 2 phút (LambdaTest/TestMu AI) → không đủ chạy toàn bộ checklist (M2). Đề cho phép thiết bị thật |

## e. Quyết định đã chốt

| Mã | Quyết định |
|---|---|
| S1 | Checklist **C2 – Tài khoản (web :5173)**: Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ + Lịch sử đơn/huỷ đơn, navbar khi đã đăng nhập. **Không lấy Đăng ký** (đã kiểm ở HW02 A/D) |
| U | Usability **U1**: đăng nhập (tài khoản cho sẵn) → tìm SP → thêm giỏ → thanh toán có mã giảm giá → xem đơn trong Hồ sơ. Moderated, trực tiếp trên PC của SV. Restart backend trước mỗi phiên |
| M2 | Toàn bộ checklist × 3 nền tảng |
| M3 | Có N/A + giả định |
| P1 | Chrome trên Windows (localhost:5173) |
| P2 | Firefox trên Windows (cài mới) |
| P3 | Chrome Android trên POCO F5 qua `adb reverse tcp:5173` + `tcp:3000` — **đã kiểm chứng 04/11 17:35** (adb 37.0.1 ở `D:\Tools\platform-tools`, web chạy `--host 127.0.0.1`) |
| BS | Không dùng BrowserStack/LambdaTest (M11) |
| R | Người tham gia: 1 pilot + 7 chính, đã tuyển 04/11 (ngoài lớp; một phần IT, một phần non-IT) |
| E1 | Excel **mới** `excel/23120255_HW03_Checklist.xlsx`, 3 sheet như HW01 (Test Cases / Checklist / Test Summary Report) |
| O1 | Overlay: `23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn`. PC = cửa sổ Sticky Notes + chụp toàn màn hình (thấy tên trình duyệt + URL); điện thoại = thêm chữ bằng trình sửa ảnh của máy ngay sau khi chụp |
| T | Thang: **SUS** (10 câu tiếng Việt) + **SEQ** (1 câu sau nhiệm vụ); bộ câu hỏi tối giản vì có người non-IT |
| K1 | Mã giảm giá trong nhiệm vụ U1 = **VIP100** (a). Lý do: usability đo thiết kế, không để bug tính tiền đã biết (SAVE10) làm nhiễu SUS |
| X1 | (a) Cài `openpyxl` cho Python các script dùng (`C:\msys64\ucrt64\bin\python.exe` 3.14; Python này không có pip → `pacman -S mingw-w64-ucrt-x86_64-python-openpyxl`) → `build_excel.py` chạy được |
| X2 | (a) `HW03/CLAUDE.md` không nộp: `export-ignore` trong `HW03/.gitattributes` |
| E2 | (b) Playwright tự chạy các item kiểm được qua DOM/bàn phím trên P1 (Chrome channel) + P2 (Firefox của Playwright) → `auto_status`; SV chạy tay phần còn lại + toàn bộ P3. **Verdict chính thức = lượt trên trình duyệt thật** |
| H1 | Ngưỡng màu cho auto: CL-04 xanh dương = hue 190–250°, CL-05 đỏ = hue 340–20°, độ bão hoà ≥ 0,3 (SV: "nhìn thấy đúng xanh dương/đỏ là được"); expected không đổi |

**Còn chờ SV chốt:** (không còn)

## f. Khai cho Audit (ghi dần)

- 04/11 phiên thảo luận: đọc đề + slide, lập bảng form, đề xuất chia C1/C2/C3 + U1–U4 cho nhóm, tin nhắn mời người tham gia (AI nháp), hướng dẫn bật Gỡ lỗi USB, lệnh kiểm chứng P3.
- 04/11 Claude Code: tải platform-tools (SV đồng ý), chạy backend/web, `adb reverse`, liệt kê issue nhóm (158).
- AI phát hiện khi kiểm luồng U1: SAVE10 tính sai (server.js:400), ngưỡng dùng > thay vì >= (server.js:379) – chưa quyết lập bug.
- AI phát hiện khi đọc code: login_attempts +2 (server.js:54), khoá 180 s (server.js:57) ≠ FR-02 – chờ CL-52 chạy tay. Kiểm trùng: đã có #1, #2, #3 (`checklist/issue_dup_FR02.md`).
- 05/11 Claude Code: cài Firefox của Playwright (131.0), thêm project P3 (Playwright `_android`) vào harness; sửa lỗi reporter.ts ghi 0 item (`TestResult.annotations` chưa có ở 1.48) – phát hiện khi smoke CL-03.
- Lỗi phiên thảo luận: `[...]`.

## g. Danh sách cho Mandatory Disclosure (ghi dần)

- AI tạo bản đầu: `[...]` (checklist nháp, gói usability nháp, script/harness…).
- SV xem xét và sửa: `[...]`.
- Item SV bổ sung (🔒, kèm lý do AI bỏ sót): `[...]`.
- SV tự làm hoàn toàn: tuyển + danh sách 7 người, điều phối phiên, ghi chú quan sát, câu trả lời SUS, ảnh cross-platform có overlay, bug report, Critique, verdict Audit, điểm tự chấm, giọng video.
- Prompt log: trích tự động bằng `tools/extract_prompt_log.py` (hook `on_stop.py`); Section/Mục đích/Xử lý do em ghi.

## h. Lịch (deadline 10:00 thứ Tư 11/11/2026)

| Khi | Việc |
|---|---|
| T2 09/11 tối | Chạy tay checklist (P1, P2, P3) theo RUN.md |
| T3 10/11 ngày | T1 bước 4/6 (gộp kết quả P1–P3) + form AI-02/03/05 |
| T3 10/11 tối | Pilot + 7 phiên usability (S1–S7) |
| Đêm T3 → sáng T4 11/11 | Phân tích usability + report + zip; nộp trước 10:00 |
