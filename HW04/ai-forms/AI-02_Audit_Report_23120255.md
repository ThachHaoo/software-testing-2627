**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**
**CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**
**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# AI Audit Report — Mẫu 5 mục cho mỗi Artifact

*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW#01–HW#06, Seminar).*

## 1. Thông tin Sinh viên

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |
| MSSV: | 23120255 |
| Lớp / Khoá: | Software Testing - 23_3 |
| Mã bài tập: | HW04-AI – Automation Testing on EShop |
| Ngày làm bài: | 16/11/2026 – 18/11/2026 |
| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — Claude (không rõ model) 37 lượt; Claude Opus 5.5 49 lượt (tổng 86 lượt theo dòng Tổng của `appendix/A_prompt_log.md`, bản trích 08:53 18/11/2026); lượt claude.ai: Claude Opus 5.5 (em xác nhận, log ghi "không rõ model") – AI-03 mục 1 |
| Có sử dụng AI: | [x] Có [ ] Không |

**Tuyên bố sử dụng AI (đề):** xem report chính §10 Mandatory Disclosure.

## 2. Hướng dẫn

- Mỗi commit HW04 là một artifact (lấy từ `git log`): mục (1) công cụ + thời gian + commit, (2) output = message + file trong commit, (5) commit sửa sau đó = các hàng kế tiếp cùng chủ đề; mục (3) Verdict và (4) Lý do do em viết.
- Prompt và output nguyên văn: `appendix/A_prompt_log.md`; output dạng file đóng băng: `appendix/ai-outputs/` (`INDEX.md`).
- Commit do em làm (viết/sửa/chốt/hoàn thiện) ghi "— (SV làm…)" và không tính vào tỉ lệ verdict.

## 3. Bảng Audit — 1 hàng / artifact

### 3.1 Theo commit (chép từ report §9)

| # | Thời điểm | Commit | Artifact (message) | Sửa `.spec.ts` | Verdict | Lý do |
|---|---|---|---|---|---|---|
| 1 | 2026-11-16 22:34 | `4d14bd7` | HW04: bước 0 – môi trường |  | INCOMPLETE | Thiếu cấu hình thay thế WebKit (W1=a) và tắt trace (Z1=d) để tối ưu dung lượng báo cáo nên phải điều chỉnh ở các bước sau. |
| 2 | 2026-11-16 23:03 | `838752b` | HW04: đổi sang Chrome/Edge/Firefox (W1=a) |  | VALID | Cấu hình đúng 3 trình duyệt thay thế đáp ứng yêu cầu kiểm thử tương thích đa trình duyệt (Portability/Compatibility theo ISTQB). |
| 3 | 2026-11-16 23:07 | `b0e2f7c` | HW04: skill playwright-ddt-automation v1 |  | INCOMPLETE | Khung quy trình 6 bước Data-Driven hợp lý nhưng template còn giữ `mode: 'serial'` và thiếu checklist review, phải nâng cấp lên v2/v2.1. |
| 4 | 2026-11-16 23:08 | `b54c170` | HW04[A-FR01] 1/6: chọn 15 TC UI + data JSON (expected nguyên văn + sha1) |  | INCOMPLETE | Tách dữ liệu và băm `expected_sha1` đúng chuẩn DDT, nhưng danh sách còn giữ các case Blocked trùng nguyên nhân nên cần SV chốt lại ở 1/6b. |
| 5 | 2026-11-16 23:08 | `f797653` | HW04: cập nhật prompt log |  | VALID | Lưu vết lịch sử tương tác AI phục vụ tính truy vết (Traceability) trong quy trình kiểm thử có hỗ trợ của AI. |
| 6 | 2026-11-17 00:08 | `0990ac0` | HW04[A-FR01] 1/6b – SV chốt |  | — (SV làm, không thuộc phạm vi audit AI) | SV rà soát loại bỏ các case Blocked trùng lỗi gốc và bổ sung điểm đại diện EP/BVA đảm bảo độ bao phủ kiểm thử hộp đen (ISTQB). |
| 7 | 2026-11-17 00:10 | `161074b` | HW04[A-FR01] 2/6: fixture + page object (Register, Login), tsconfig |  | VALID | Áp dụng mẫu thiết kế Page Object Model tách biệt locator khỏi kịch bản kiểm thử, tăng tính bảo trì theo kiến trúc tự động hóa (ISTQB TAE). |
| 8 | 2026-11-17 00:23 | `9a5e558` | HW04[A-FR01] 3/6: sinh spec data-driven + bảng assertion | Có | INCOMPLETE | Kịch bản mắc lỗi `mode: 'serial'` làm 1 Fail chặn 14 TC, thiếu escape regex và gọi `users.list()` trước khi chờ `POST` hoàn tất. |
| 9 | 2026-11-17 00:30 | `6fc76b5` | HW04[A-FR01] 5/6a – sửa: bỏ mode serial (1 Fail chặn 14 TC) | Có | VALID | Khắc phục lỗi phụ thuộc giữa các test case, đảm bảo nguyên tắc tính độc lập thực thi của kiểm thử tự động (ISTQB). |
| 10 | 2026-11-17 00:56 | `3e7dda8` | HW04[A-FR01] review của SV |  | VALID | Ghi nhận trung thực kết quả kiểm tra tĩnh (Static Review) của SV đối với mã nguồn kịch bản do AI sinh. |
| 11 | 2026-11-17 00:57 | `5a378f1` | HW04[A-FR01] 5/6b – sửa: chờ phản hồi POST trước oracle API, annotation nhánh phản hồi, timeout → Blocked | Có | VALID | Đồng bộ hóa luồng bất đồng bộ trước khi đối chiếu oracle API, loại bỏ nguy cơ Pass giả (False Positive) do race condition. |
| 12 | 2026-11-17 00:57 | `740934b` | HW04[A-FR01] 5/6c – sửa: oracleOf nhóm ^(…\|…), escape trước new RegExp, annotation oracle thông báo yếu | Có | VALID | Chuẩn hóa biểu thức chính quy phân tích oracle và gắn annotation cảnh báo khi đặc tả không nêu rõ nội dung thông báo. |
| 13 | 2026-11-17 00:58 | `3d19917` | HW04[A-FR01] 5/6d – sửa: beforeAll dừng khi workers > 1 (resetDb không an toàn song song) | Có | VALID | Bổ sung cơ chế bảo vệ môi trường dữ liệu dùng chung khi chạy song song, ngăn ngừa xung đột khởi động lại CSDL. |
| 14 | 2026-11-17 00:58 | `79d4bb6` | HW04: reports/** -text (giữ nguyên byte HTML report) |  | VALID | Cấu hình `.gitattributes` bảo toàn tính toàn vẹn dữ liệu nhị phân/văn bản của báo cáo kiểm thử HTML. |
| 15 | 2026-11-17 00:58 | `b321098` | HW04[A-FR01]: RUN.md lượt thử 2 + 4 report |  | VALID | Ghi nhận đầy đủ nhật ký thực thi thử nghiệm làm bằng chứng kiểm chứng trước khi chạy lượt chính thức. |
| 16 | 2026-11-17 01:12 | `74dd2c6` | HW04[A-FR01]: lượt chính thức (3 report) + RUN.md |  | VALID | Hoàn tất thực thi chính thức trên 3 trình duyệt với metadata định danh và kết quả nhất quán 7 Pass / 8 Fail. |
| 17 | 2026-11-17 01:14 | `9905eca` | HW04[A-FR01] 6/6: gộp 3 report → results.md, bug_groups.md (3 nhóm), 24 ảnh lỗi |  | VALID | Tổng hợp dữ kiện đa trình duyệt và gom nhóm lỗi theo chữ ký thất bại phục vụ phân tích nguyên nhân gốc (Root Cause Analysis). |
| 18 | 2026-11-17 01:17 | `597bda7` | HW04: tắt trace để report < 20 MB (Z1=d) |  | VALID | Tối ưu dung lượng gói bằng chứng kiểm thử bằng ảnh chụp và error-context thay vì tệp trace dung lượng lớn. |
| 19 | 2026-11-17 01:18 | `656962c` | HW04[B-FR07] 1/6: chọn 15 TC UI + data JSON (oracle giỏ = trạng thái UI) |  | INCOMPLETE | Xác định đúng oracle giỏ hàng qua trạng thái UI React, nhưng còn 1 TC nhạy thời gian cần SV chốt thay thế ở 1/6b. |
| 20 | 2026-11-17 01:31 | `b7cbc6b` | HW04[A-FR01] 6/6b – lượt chính thức (trace off) |  | VALID | Cập nhật bộ báo cáo chính thức gọn nhẹ sau khi áp dụng cấu hình tối ưu dung lượng Z1=d. |
| 21 | 2026-11-17 01:31 | `77111f7` | HW04[B-FR07] 1/6b – SV chốt |  | — (SV làm, không thuộc phạm vi audit AI) | Loại bỏ test case nhạy thời gian dễ gây kết quả chập chờn (Flaky Test) theo nguyên tắc ổn định của tự động hóa. |
| 22 | 2026-11-17 01:33 | `8b77124` | HW04[B-FR07] 2/6: fixture + page object (trang chủ, chi tiết, giỏ qua navbar; oracle giỏ từ UI) |  | INCOMPLETE | Xây dựng Page Object bám sát điều hướng SPA của giỏ hàng nhưng selector kiểm tra hình minh họa giỏ trống còn chung chung. |
| 23 | 2026-11-17 01:43 | `7e75536` | HW04[B-FR07] 3/6: spec data-driven + parser oracle + bảng assertion (45 test) | Có | INCOMPLETE | Kịch bản cài đặt đúng logic oracle nhưng còn gõ cứng từ khóa `/trống/i` trong spec và thiếu ảnh chụp ngay sau thao tác. |
| 24 | 2026-11-17 01:52 | `6d9f402` | HW04[B-FR07] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md |  | VALID | Thực thi lượt thử đầu tiên trên 3 trình duyệt, cung cấp dữ liệu thực tế cho bước rà soát kịch bản. |
| 25 | 2026-11-17 13:39 | `2c8372f` | HW04[B-FR07] 5/6: SV soi spec (nguyên văn) + đối chiếu code |  | VALID | Đối chiếu nhận xét của SV với mã nguồn thực tế, phân tách rõ ràng giữa lỗi script và đặc thù của SUT. |
| 26 | 2026-11-17 13:40 | `14ac598` | HW04[B-FR07] 5/6a – sửa: từ khoá giỏ trống chuyển vào data (assumptions, giả định SV chốt), expected giữ nguyên (R1=a) | Có | VALID | Tách giả định từ khóa ra khỏi mã nguồn vào tệp dữ liệu JSON, tuân thủ chặt chẽ kiến trúc Data-Driven Testing. |
| 27 | 2026-11-17 13:40 | `4f3c278` | HW04[B-FR07] 5/6b – sửa: ảnh/icon minh hoạ phải nằm trong khối chứa dòng chữ giỏ trống, bỏ .first() (R2) | Có | VALID | Thu hẹp phạm vi locator kiểm tra biểu tượng giỏ trống vào đúng khối thông báo, giảm thiểu bắt nhầm phần tử giao diện. |
| 28 | 2026-11-17 13:41 | `c8a2ce9` | HW04[B-FR07] 5/6c – sửa: ảnh <TC>_after-action ngay sau bấm Thêm/Xoá (testInfo.attach, P1=a) | Có | VALID | Bổ sung bằng chứng trực quan ngay sau thao tác chính giúp tăng tính minh bạch khi chứng minh lỗi giao diện. |
| 29 | 2026-11-17 13:42 | `9f26855` | HW04[A-FR01] 5/6e – ảnh sau submit | Có | VALID | Đồng bộ chuẩn chụp ảnh bằng chứng ngay sau thao tác submit cho feature A, đảm bảo tính nhất quán toàn bộ test suite. |
| 30 | 2026-11-17 13:42 | `841c7e2` | HW04[B-FR07] 5/6: ghi phần không tự động (TC-08 dialog đang mở) |  | VALID | Liệt kê minh bạch giới hạn kỹ thuật của dialog native khóa luồng DOM theo nguyên tắc phân định phạm vi tự động hóa (ISTQB). |
| 31 | 2026-11-17 14:05 | `ea55c9c` | HW04[A-FR01] 6/6c – lượt chính thức |  | VALID | Chạy lại lượt chính thức cho feature A sau khi bổ sung ảnh chụp sau submit, giữ nguyên kết quả 7 Pass / 8 Fail. |
| 32 | 2026-11-17 14:06 | `ef419f2` | HW04[B-FR07] 5/6: lượt thử 2 (3 trình duyệt) + RUN.md (TC-60 firefox: worker crash) |  | VALID | Ghi nhận trung thực sự cố sập worker `0xC0000409` trên Firefox để tiến hành chạy lại xác minh nguyên nhân hạ tầng. |
| 33 | 2026-11-17 14:11 | `d676bf9` | HW04[B-FR07] 5/6: RUN.md – TC-60 firefox lỗi hạ tầng (3/3 Pass khi chạy riêng), xoá 3 report rỗng |  | VALID | Phân tách chính xác lỗi hạ tầng trình duyệt khỏi lỗi phần mềm sau khi chạy kiểm chứng độc lập đạt 3/3 Pass. |
| 34 | 2026-11-17 14:14 | `25f6e6e` | HW04[C-FR15] 1/6: chọn 15 TC UI (Thêm/Sửa/Xóa) + data JSON + rủi ro sập backend (chưa quyết) |  | VALID | Phủ đủ thao tác CRUD và nhận diện sớm rủi ro sập backend do `BUG-48` để SV chốt phương án xử lý C2. |
| 35 | 2026-11-17 14:18 | `072e47f` | HW04[B-FR07] 6/6 – lượt chính thức |  | VALID | Hoàn tất chạy chính thức và tổng hợp kết quả feature B đồng nhất 6 Pass / 9 Fail trên cả 3 trình duyệt. |
| 36 | 2026-11-17 14:19 | `f4086c0` | HW04[C-FR15] 1/6b – SV chốt |  | — (SV làm, không thuộc phạm vi audit AI) | SV chốt phương án health-check backend sau mỗi case để cô lập sự cố sập server mà không làm lệch quy trình kiểm thử. |
| 37 | 2026-11-17 14:20 | `16d791d` | HW04[C-FR15] 2/6: fixture + page object admin (login, form theo placeholder, bảng, dialog, API trước/sau, health-check backend) |  | VALID | Cài đặt đầy đủ Page Object cho trang quản trị kèm cơ chế health-check backend tự động phục hồi môi trường kiểm thử. |
| 38 | 2026-11-17 14:28 | `370c9cd` | HW04[C-FR15] 3/6: spec data-driven + parser oracle + bảng assertion (45 test); giả định ngoài expected vào data | Có | INCOMPLETE | Kịch bản bao quát đủ CRUD và oracle API/UI nhưng mắc lỗi ghi nhận trùng sự kiện `invalid` do gọi sớm `checkValidity()`. |
| 39 | 2026-11-17 14:47 | `0631be5` | HW04[C-FR15] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md |  | VALID | Hoàn tất lượt chạy thử trên 3 trình duyệt, làm cơ sở đối chiếu cho bước review kịch bản feature C. |
| 40 | 2026-11-17 14:47 | `feec5e2` | HW04[C-FR15] SV duyệt giả định |  | VALID | Xác nhận chính thức các giả định kiểm thử ngoài đặc tả giúp oracle hoạt động minh bạch và có cơ sở đối chiếu. |
| 41 | 2026-11-17 14:48 | `961d61d` | HW04: dữ kiện nhóm Fail A + B để SV quyết G → BUG |  | VALID | Gom nhóm dữ kiện thất bại theo chữ ký lỗi hỗ trợ SV phân tích nguyên nhân gốc trước khi lập báo cáo bug. |
| 42 | 2026-11-17 15:10 | `9b1a139` | HW04[C-FR15] 5/6: review_sv.md (SV soi bản 1 + bản 2 sau đối chiếu) |  | VALID | Ghi nhận đầy đủ hai vòng rà soát kịch bản của SV và đối chiếu mã nguồn cho feature C. |
| 43 | 2026-11-17 15:10 | `2e9e454` | HW04[C-FR15] 5/6a – sửa: ô không hợp lệ chỉ ghi sự kiện của lần bấm Lưu (bỏ ghi trùng do checkValidity) | Có | VALID | Loại bỏ việc gọi `checkValidity()` trước khi submit, đảm bảo ghi nhận chính xác sự kiện validation của trình duyệt. |
| 44 | 2026-11-17 15:17 | `2c54f76` | HW04[C-FR15] 6/6 – lượt chính thức |  | VALID | Hoàn tất thực thi chính thức trên 3 trình duyệt cho feature C với kết quả nhất quán 6 Pass / 9 Fail. |
| 45 | 2026-11-17 15:18 | `f497ee8` | HW04: dữ kiện nhóm Fail C + README nháp (test summary sinh bằng tools/hw04_summary.py) |  | VALID | Tổng hợp dữ kiện lỗi feature C và sinh bảng thống kê kết quả tự động từ dữ liệu báo cáo thật. |
| 46 | 2026-11-17 15:34 | `2667147` | HW04: khung 18 bug (Cách 2) |  | INCOMPLETE | Khung bug chép nhầm quy ước C3 vào mục Yêu cầu của BUG-101 và BUG-103 (đã sửa ở `d6cd474`). |
| 47 | 2026-11-17 20:20 | `2775914` | HW04: SV viết 18 bug |  | — (SV làm, không thuộc phạm vi audit AI) | SV hoàn thiện mô tả, bước tái hiện, đánh giá mức độ nghiêm trọng (Severity/Priority) và nguyên nhân gốc cho 18 báo cáo lỗi (ISTQB Defect Management). |
| 48 | 2026-11-17 20:38 | `8f47846` | HW04: SV sửa bug theo kiểm dữ kiện |  | — (SV làm, không thuộc phạm vi audit AI) | Hiệu chỉnh nội dung báo cáo lỗi khớp chặt chẽ với bằng chứng thực thi thu được từ các lượt chạy chính thức. |
| 49 | 2026-11-17 20:53 | `1881c16` | HW04: SV sửa bug theo kiểm dữ kiện |  | — (SV làm, không thuộc phạm vi audit AI) | Tiếp tục rà soát tính nhất quán giữa dữ liệu thực tế và mô tả trong các báo cáo lỗi trước khi công bố. |
| 50 | 2026-11-17 20:55 | `d6cd474` | HW04: sửa Yêu cầu do AI chép nhầm C3 (BUG-101, 103) |  | VALID | Khắc phục sai sót sao chép nhầm quy ước C3 của script vào mục yêu cầu bị vi phạm của báo cáo lỗi. |
| 51 | 2026-11-17 20:59 | `9e9f88f` | HW04: kiểm tái hiện 18 bug (dữ kiện, chờ SV sửa) |  | VALID | Xác minh lại khả năng tái hiện độc lập của toàn bộ 18 lỗi trên SUT bằng kịch bản Playwright trước khi mở issue. |
| 52 | 2026-11-17 21:17 | `b264556` | HW04: SV sửa bug theo Claude Code tái hiện |  | — (SV làm, không thuộc phạm vi audit AI) | Tinh chỉnh lại các bước tái hiện trong báo cáo lỗi dựa trên kết quả kiểm chứng thực tế trên giao diện. |
| 53 | 2026-11-17 21:22 | `78873e0` | HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug |  | VALID | Đăng tải đầy đủ 18 báo cáo lỗi lên hệ thống quản lý lỗi GitHub kèm liên kết truy vết và bằng chứng trực quan. |
| 54 | 2026-11-17 21:36 | `ac813b0` | HW04: report_plan + dàn ý report (khối REPORT sinh bằng tools/hw04_report.py) + prompt log 28 lượt |  | INCOMPLETE | Dựng cấu trúc báo cáo tự động hóa các bảng dữ kiện nhưng mới trích xuất được 28 lượt log từ Claude Code (thiếu phiên `claude.ai`). |
| 55 | 2026-11-17 22:12 | `86d4d78` | tools: đọc hội thoại claude.ai từ bản xuất dữ liệu (claude-ai_*.json); HW04 prompt log 65 lượt |  | VALID | Bổ sung trình trích xuất hội thoại từ `claude.ai`, đảm bảo tính đầy đủ và minh bạch cho nhật ký sử dụng AI. |
| 56 | 2026-11-17 22:20 | `60bec96` | HW04: report_plan ghi S1/T1–T4, khai bộ đọc claude.ai; notes ghi chú model lượt claude.ai (nguon_luot) |  | VALID | Ghi chú rõ nguồn phiên làm việc và thông tin model cho từng lượt tương tác trong nhật ký kiểm toán AI. |
| 57 | 2026-11-18 00:20 | `eb40646` | HW04[A-FR01]: ghi 3 lượt không chính thức 17/11 tối (Firefox bị Code Integrity chặn) + log môi trường |  | VALID | Lưu vết đầy đủ sự cố môi trường Windows Code Integrity chặn Firefox kèm log hệ thống để giải trình tính hợp lệ của lượt chính thức. |
| 58 | 2026-11-18 00:22 | `2d3660b` | HW04: link video Task 2 (README, report §7, skills/VideoLinks.md); RUN.md A ghi 3 lượt quay video |  | VALID | Cập nhật liên kết video minh chứng thực thi kịch bản kiểm thử tự động trên máy cá nhân. |
| 59 | 2026-11-18 00:54 | `5bb31d1` | HW04: skill playwright-ddt-automation v2 (bài học review A/B/C) |  | INCOMPLETE | Cập nhật các bài học từ review A/B/C vào template skill nhưng chưa kiểm thử chạy độc lập đầu-cuối (E2E). |
| 60 | 2026-11-18 01:26 | `99080b2` | HW04: skill v2.1 – freeze ngoài testDir, chế độ demo, chạy thử E2E sạch |  | VALID | Khắc phục triệt để các lỗi phát sinh khi chạy thử E2E độc lập, hoàn thiện quy trình đóng gói và demo skill. |
| 61 | 2026-11-18 02:03 | `6ef3a84` | HW04: prompt log trích lại (on_stop) |  | VALID | Cập nhật bản trích xuất nhật ký tương tác AI đầy đủ nhất phục vụ công tác đối chiếu và kiểm toán. |
| 62 | 2026-11-18 02:07 | `e3ae77f` | HW04: link video Agent Skill, chép skill v2.1 vào HW04/skills, report điền dữ kiện, AI-02 khung, Mandatory Disclosure nháp |  | VALID | Đóng gói bản nộp hoàn chỉnh của Agent Skill, biểu mẫu AI-02 và liên kết video demo quy trình 6 bước. |
| 63 | 2026-11-18 02:08 | `6ceb790` | HW04: AI-02 mã artifact duy nhất, README repo + bảng tự chấm, users.list vào Khai Audit, placeholders_left.md |  | VALID | Chuẩn hóa mã định danh duy nhất cho từng artifact và hoàn thiện tài liệu tổng quan repository nộp bài. |
| 64 | 2026-11-18 02:08 | `a99d6ee` | HW04: report §9 bảng audit cập nhật tới 6ceb790 |  | `<SV viết>` | `<SV viết>` |
| 65 | 2026-11-18 02:21 | `00697ab` | HW04: SV viết AI Critique và lí do AI sai/bỏ sót |  | — (SV làm, không thuộc phạm vi audit AI) | — |
| 66 | 2026-11-18 02:33 | `39e1536` | HW04: Sửa lại phần AI Critique và 3.6 và 4.6 |  | — (SV làm, không thuộc phạm vi audit AI) | — |
| 67 | 2026-11-18 08:47 | `fad3ddf` | HW04: SV hoàn thiện Audit và tự chấm điểm |  | — (SV làm, không thuộc phạm vi audit AI) | — |
| 68 | 2026-11-18 08:51 | `5298b98` | HW04: SV sửa Audit |  | — (SV làm, không thuộc phạm vi audit AI) | — |

### 3.2 Tỉ lệ verdict

| Verdict | Số artifact (commit AI) |
|---|---|
| VALID | 45 (80%) |
| INVALID | 0 (0%) |
| INCOMPLETE | 11 (20%) |
| Tổng có verdict | 56 |

Không tính: 11 commit SV làm ("— (SV làm…)"); 1 commit AI chưa có verdict (`<SV viết>`).

### 3.3 Danh mục artifact theo file (tham chiếu – verdict theo commit tạo ở 3.1)

| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |
|---|---|---|---|---|
| H1 | Harness HW04: `HW04/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp) | Claude Code · 16/11/2026 22:34 · `4d14bd7` (HW04: bước 0 – môi trường) · – | đề tóm tắt, quyết định, khai Audit · `HW04/CLAUDE.md`, `HW04/report_plan.md` | `838752b` HW04: đổi sang Chrome/Edge/Firefox (W1=a); `ac813b0` HW04: report_plan + dàn ý report (khối REPORT sinh bằng tools/hw04_report.py) + prompt log 28 lượt; `60bec96` HW04: report_plan ghi S1/T1–T4, khai bộ đọc claude.ai; notes ghi chú model lượt claude.ai (nguon_luot); `eb40646` HW04[A-FR01]: ghi 3 lượt không chính thức 17/11 tối (Firefox bị Code Integrity chặn) + log môi trường; … (+2) |
| H2 | Bộ chạy Playwright: config 3 trình duyệt + "Run by" + JSON reporter, global-setup, package/tsconfig | Claude Code · 16/11/2026 22:34 · `4d14bd7` (HW04: bước 0 – môi trường) · – | project chrome/edge/firefox, workers 1, retries 0 · `HW04/tests/playwright.config.ts`, `HW04/tests/global-setup.ts`, `HW04/tests/package.json` … | `838752b` HW04: đổi sang Chrome/Edge/Firefox (W1=a); `b0e2f7c` HW04: skill playwright-ddt-automation v1; `161074b` HW04[A-FR01] 2/6: fixture + page object (Register, Login), tsconfig; `597bda7` HW04: tắt trace để report < 20 MB (Z1=d) |
| S1 | Agent Skill `playwright-ddt-automation` v1 (SKILL.md, 4 script, 3 asset) | Claude Code · 16/11/2026 23:07 · `b0e2f7c` (HW04: skill playwright-ddt-automation v1) · – | quy trình 6 bước có điểm dừng · `.claude/skills/playwright-ddt-automation/SKILL.md`, `.claude/skills/playwright-ddt-automation/scripts/select_tc.py`, `.claude/skills/playwright-ddt-automation/scripts/merge_reports.py` | `0990ac0` HW04[A-FR01] 1/6b – SV chốt; `9905eca` HW04[A-FR01] 6/6: gộp 3 report → results.md, bug_groups.md (3 nhóm), 24 ảnh lỗi; `656962c` HW04[B-FR07] 1/6: chọn 15 TC UI + data JSON (oracle giỏ = trạng thái UI); `14ac598` HW04[B-FR07] 5/6a – sửa: từ khoá giỏ trống chuyển vào data (assumptions, giả định SV chốt), expected giữ nguyên (R1=a); … (+3) |
| S2 | Skill v2 – bài học review A/B/C (template fixture/spec, checklist review bước 5) | Claude Code · 18/11/2026 00:54 · `5bb31d1` (HW04: skill playwright-ddt-automation v2 (bài học review A/B/C)) · – | bỏ serial, step/until/esc/assumption · `.claude/skills/playwright-ddt-automation/assets/spec.template.ts`, `.claude/skills/playwright-ddt-automation/assets/ddt-fixture.template.ts`, `.claude/skills/playwright-ddt-automation/SKILL.md` | `99080b2` HW04: skill v2.1 – freeze ngoài testDir, chế độ demo, chạy thử E2E sạch |
| S3 | Skill v2.1 – freeze ngoài testDir, chế độ demo (`demo.py`), chạy thử E2E | Claude Code · 18/11/2026 01:26 · `99080b2` (HW04: skill v2.1 – freeze ngoài testDir, chế độ demo, chạy thử E2E sạch) · – | 4 TC × 3 trình duyệt khớp HW02 · `.claude/skills/playwright-ddt-automation/scripts/demo.py`, `.claude/skills/playwright-ddt-automation/scripts/freeze.py` | không có |
| S4 | Bản chép skill nộp `HW04/skills/` + `VideoLinks.md` | Claude Code · 18/11/2026 02:07 · `e3ae77f` (HW04: link video Agent Skill, chép skill v2.1 vào HW04/skills, report điền dữ kiện, AI-02 khung, Mandatory Disclosure nháp) · – | bản v2.1 @99080b2; link 2 video · `HW04/skills/playwright-ddt-automation/SKILL.md`, `HW04/skills/VideoLinks.md` | không có |
| A1 | A_FR01 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng | Claude Code · 16/11/2026 23:08 · `b54c170` (HW04[A-FR01] 1/6: chọn 15 TC UI + data JSON (expected nguyên văn + sha1)) · – | selection + data · `HW04/appendix/ai-outputs/A_FR01/step1/selection.json`, `HW04/appendix/ai-outputs/A_FR01/step1/A_FR01.json`, `HW04/appendix/ai-outputs/A_FR01/step1/selection.md` | không có |
| A2 | A_FR01 bước 2: fixture + page object – bản đóng băng | Claude Code · 17/11/2026 00:10 · `161074b` (HW04[A-FR01] 2/6: fixture + page object (Register, Login), tsconfig) · – | selector theo mã UI thật · `HW04/appendix/ai-outputs/A_FR01/step2/a_fr01.ts`, `HW04/appendix/ai-outputs/A_FR01/step2/ddt.ts`, `HW04/appendix/ai-outputs/A_FR01/step2/register.page.ts` … | không có |
| A3 | A_FR01 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng | Claude Code · 17/11/2026 00:23 · `9a5e558` (HW04[A-FR01] 3/6: sinh spec data-driven + bảng assertion) · – | 45 test (15 TC × 3) · `HW04/appendix/ai-outputs/A_FR01/step3/A_FR01.spec.ts`, `HW04/appendix/ai-outputs/A_FR01/step3/assertions.md` | không có |
| A4 | A_FR01 `RUN.md` – dữ kiện lượt thử/chính thức | Claude Code · 17/11/2026 00:30 · `6fc76b5` (HW04[A-FR01] 5/6a – sửa: bỏ mode serial (1 Fail chặn 14 TC)) · – | bảng lượt chạy, ghi chú lỗi hạ tầng · `HW04/A_FR01/RUN.md` | `b321098` HW04[A-FR01]: RUN.md lượt thử 2 + 4 report; `74dd2c6` HW04[A-FR01]: lượt chính thức (3 report) + RUN.md; `9905eca` HW04[A-FR01] 6/6: gộp 3 report → results.md, bug_groups.md (3 nhóm), 24 ảnh lỗi; `597bda7` HW04: tắt trace để report < 20 MB (Z1=d); … (+5) |
| A6 | A_FR01 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng | Claude Code · 17/11/2026 01:14 · `9905eca` (HW04[A-FR01] 6/6: gộp 3 report → results.md, bug_groups.md (3 nhóm), 24 ảnh lỗi) · – | Pass/Fail/Blocked theo trình duyệt, nhóm Fail (dữ kiện) · `HW04/appendix/ai-outputs/A_FR01/step6/results.md`, `HW04/appendix/ai-outputs/A_FR01/step6/bug_groups.md` | không có |
| A7 | A_FR01 `not_automated.md` – TC/phần expected không tự động | Claude Code · 18/11/2026 02:07 · `e3ae77f` (HW04: link video Agent Skill, chép skill v2.1 vào HW04/skills, report điền dữ kiện, AI-02 khung, Mandatory Disclosure nháp) · – | từ selection.json + annotation report · `HW04/A_FR01/not_automated.md` | không có |
| B1 | B_FR07 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng | Claude Code · 17/11/2026 01:18 · `656962c` (HW04[B-FR07] 1/6: chọn 15 TC UI + data JSON (oracle giỏ = trạng thái UI)) · – | selection + data · `HW04/appendix/ai-outputs/B_FR07/step1/selection.json`, `HW04/appendix/ai-outputs/B_FR07/step1/B_FR07.json`, `HW04/appendix/ai-outputs/B_FR07/step1/selection.md` | không có |
| B2 | B_FR07 bước 2: fixture + page object – bản đóng băng | Claude Code · 17/11/2026 01:33 · `8b77124` (HW04[B-FR07] 2/6: fixture + page object (trang chủ, chi tiết, giỏ qua navbar; oracle giỏ từ UI)) · – | selector theo mã UI thật · `HW04/appendix/ai-outputs/B_FR07/step2/b_fr07.ts`, `HW04/appendix/ai-outputs/B_FR07/step2/shop.pages.ts` | không có |
| B3 | B_FR07 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng | Claude Code · 17/11/2026 01:43 · `7e75536` (HW04[B-FR07] 3/6: spec data-driven + parser oracle + bảng assertion (45 test)) · – | 45 test (15 TC × 3) · `HW04/appendix/ai-outputs/B_FR07/step3/B_FR07.spec.ts`, `HW04/appendix/ai-outputs/B_FR07/step3/b_fr07.oracle.ts`, `HW04/appendix/ai-outputs/B_FR07/step3/assertions.md` | không có |
| B4 | B_FR07 `RUN.md` – dữ kiện lượt thử/chính thức | Claude Code · 17/11/2026 01:52 · `6d9f402` (HW04[B-FR07] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md) · – | bảng lượt chạy, ghi chú lỗi hạ tầng · `HW04/B_FR07/RUN.md` | `ef419f2` HW04[B-FR07] 5/6: lượt thử 2 (3 trình duyệt) + RUN.md (TC-60 firefox: worker crash); `d676bf9` HW04[B-FR07] 5/6: RUN.md – TC-60 firefox lỗi hạ tầng (3/3 Pass khi chạy riêng), xoá 3 report rỗng; `072e47f` HW04[B-FR07] 6/6 – lượt chính thức |
| B6 | B_FR07 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng | Claude Code · 17/11/2026 14:18 · `072e47f` (HW04[B-FR07] 6/6 – lượt chính thức) · – | Pass/Fail/Blocked theo trình duyệt, nhóm Fail (dữ kiện) · `HW04/appendix/ai-outputs/B_FR07/step6/results.md`, `HW04/appendix/ai-outputs/B_FR07/step6/bug_groups.md` | không có |
| B7 | B_FR07 `not_automated.md` – TC/phần expected không tự động | Claude Code · 17/11/2026 13:42 · `841c7e2` (HW04[B-FR07] 5/6: ghi phần không tự động (TC-08 dialog đang mở)) · – | từ selection.json + annotation report · `HW04/B_FR07/not_automated.md` | không có |
| C1 | C_FR15 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng | Claude Code · 17/11/2026 14:14 · `25f6e6e` (HW04[C-FR15] 1/6: chọn 15 TC UI (Thêm/Sửa/Xóa) + data JSON + rủi ro sập backend (chưa quyết)) · – | selection + data · `HW04/appendix/ai-outputs/C_FR15/step1/selection.json`, `HW04/appendix/ai-outputs/C_FR15/step1/C_FR15.json`, `HW04/appendix/ai-outputs/C_FR15/step1/selection.md` | không có |
| C2 | C_FR15 bước 2: fixture + page object – bản đóng băng | Claude Code · 17/11/2026 14:20 · `16d791d` (HW04[C-FR15] 2/6: fixture + page object admin (login, form theo placeholder, bảng, dialog, API trước/sau, health-check backend)) · – | selector theo mã UI thật · `HW04/appendix/ai-outputs/C_FR15/step2/c_fr15.ts`, `HW04/appendix/ai-outputs/C_FR15/step2/admin.pages.ts` | không có |
| C3 | C_FR15 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng | Claude Code · 17/11/2026 14:28 · `370c9cd` (HW04[C-FR15] 3/6: spec data-driven + parser oracle + bảng assertion (45 test); giả định ngoài expected vào data) · – | 45 test (15 TC × 3) · `HW04/appendix/ai-outputs/C_FR15/step3/C_FR15.spec.ts`, `HW04/appendix/ai-outputs/C_FR15/step3/c_fr15.oracle.ts`, `HW04/appendix/ai-outputs/C_FR15/step3/assertions.md` | không có |
| C4 | C_FR15 `RUN.md` – dữ kiện lượt thử/chính thức | Claude Code · 17/11/2026 14:47 · `0631be5` (HW04[C-FR15] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md) · – | bảng lượt chạy, ghi chú lỗi hạ tầng · `HW04/C_FR15/RUN.md` | `2c54f76` HW04[C-FR15] 6/6 – lượt chính thức |
| C6 | C_FR15 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng | Claude Code · 17/11/2026 15:17 · `2c54f76` (HW04[C-FR15] 6/6 – lượt chính thức) · – | Pass/Fail/Blocked theo trình duyệt, nhóm Fail (dữ kiện) · `HW04/appendix/ai-outputs/C_FR15/step6/results.md`, `HW04/appendix/ai-outputs/C_FR15/step6/bug_groups.md` | không có |
| C7 | C_FR15 `not_automated.md` – TC/phần expected không tự động | Claude Code · 18/11/2026 02:07 · `e3ae77f` (HW04: link video Agent Skill, chép skill v2.1 vào HW04/skills, report điền dữ kiện, AI-02 khung, Mandatory Disclosure nháp) · – | từ selection.json + annotation report · `HW04/C_FR15/not_automated.md` | không có |
| K1 | Dữ kiện nhóm Fail A+B, C (`_groups_AB.md`, `_groups_C.md`) | Claude Code · 17/11/2026 14:48 · `961d61d` (HW04: dữ kiện nhóm Fail A + B để SV quyết G → BUG) · – | triệu chứng, vị trí mã SUT, issue HW02 · `HW04/bugs/_groups_AB.md`, `HW04/bugs/_groups_C.md` | `f497ee8` HW04: dữ kiện nhóm Fail C + README nháp (test summary sinh bằng tools/hw04_summary.py) |
| K2 | Khung 18 bug (Cách 2, chỉ dữ kiện) + `bugs/README.md` | Claude Code · 17/11/2026 15:34 · `2667147` (HW04: khung 18 bug (Cách 2)) · – | nội dung bug do SV viết · `HW04/bugs/README.md`, `HW04/bugs/BUG-86.md` | `2775914` HW04: SV viết 18 bug; `8f47846` HW04: SV sửa bug theo kiểm dữ kiện; `1881c16` HW04: SV sửa bug theo kiểm dữ kiện; `78873e0` HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug |
| K3 | Kiểm tái hiện 18 bug bằng Playwright (`repro_check.md`) | Claude Code · 17/11/2026 20:59 · `9e9f88f` (HW04: kiểm tái hiện 18 bug (dữ kiện, chờ SV sửa)) · – | lần 1 lệch, lần 2 không lệch · `HW04/bugs/repro_check.md` | `78873e0` HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug |
| K4 | Tạo 18 GitHub Issue `gh issue create --body-file` (file SV viết) + ảnh trang Issues | Claude Code · 17/11/2026 21:22 · `78873e0` (HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug) · – | #298–#315 trên tkob-team/eshop-sut · `HW04/bugs/issues_page_1.png` | không có |
| R1 | README test summary (`tools/hw04_summary.py`) | Claude Code · 17/11/2026 15:18 · `f497ee8` (HW04: dữ kiện nhóm Fail C + README nháp (test summary sinh bằng tools/hw04_summary.py)) · – | khối SUMMARY · `tools/hw04_summary.py`, `HW04/README.md` | `78873e0` HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug; `2d3660b` HW04: link video Task 2 (README, report §7, skills/VideoLinks.md); RUN.md A ghi 3 lượt quay video; `e3ae77f` HW04: link video Agent Skill, chép skill v2.1 vào HW04/skills, report điền dữ kiện, AI-02 khung, Mandatory Disclosure nháp; `6ceb790` HW04: AI-02 mã artifact duy nhất, README repo + bảng tự chấm, users.list vào Khai Audit, placeholders_left.md; … (+1) |
| R2 | Dàn ý report + khối REPORT (`tools/hw04_report.py`) | Claude Code · 17/11/2026 21:36 · `ac813b0` (HW04: report_plan + dàn ý report (khối REPORT sinh bằng tools/hw04_report.py) + prompt log 28 lượt) · – | bảng chọn TC/kết quả/review/bug/audit · `tools/hw04_report.py`, `HW04/23120255_HW04_Report.md` | `2d3660b` HW04: link video Task 2 (README, report §7, skills/VideoLinks.md); RUN.md A ghi 3 lượt quay video; `e3ae77f` HW04: link video Agent Skill, chép skill v2.1 vào HW04/skills, report điền dữ kiện, AI-02 khung, Mandatory Disclosure nháp; `6ceb790` HW04: AI-02 mã artifact duy nhất, README repo + bảng tự chấm, users.list vào Khai Audit, placeholders_left.md; `a99d6ee` HW04: report §9 bảng audit cập nhật tới 6ceb790; … (+4) |
| R3 | Khung AI-02 + khối Mandatory Disclosure §10 (`tools/forms_hw04.py`) | Claude Code · 18/11/2026 02:07 · `e3ae77f` (HW04: link video Agent Skill, chép skill v2.1 vào HW04/skills, report điền dữ kiện, AI-02 khung, Mandatory Disclosure nháp) · – | file này · `tools/forms_hw04.py`, `HW04/ai-forms/AI-02_Audit_Report_23120255.md` | `6ceb790` HW04: AI-02 mã artifact duy nhất, README repo + bảng tự chấm, users.list vào Khai Audit, placeholders_left.md |
| P1 | Bộ đọc bản xuất dữ liệu claude.ai cho prompt log | Claude Code · 17/11/2026 22:12 · `86d4d78` (tools: đọc hội thoại claude.ai từ bản xuất dữ liệu (claude-ai_*.json); HW04 prompt log 65 lượt) · – | 36 lượt claude.ai vào log · `tools/extract_prompt_log.py` | `60bec96` HW04: report_plan ghi S1/T1–T4, khai bộ đọc claude.ai; notes ghi chú model lượt claude.ai (nguon_luot) |
| D1 | Chạy thử skill E2E ở chế độ demo (nhánh `skill-dryrun`, đã xoá, không commit) | Claude Code · 18/11/2026 01:26 · `99080b2` (HW04: skill v2.1 – freeze ngoài testDir, chế độ demo, chạy thử E2E sạch) · – | lỗi phát hiện → S3 · `.claude/skills/playwright-ddt-automation/scripts/demo.py` | không có |

*33 artifact. Sinh bằng `tools/forms_hw04.py` từ danh mục trong script + `git log`.*

### 3.4 Khai cho Audit (chép nguyên văn `report_plan.md` mục f)

Nguồn: `HW04/*/RUN.md`, `HW04/*/review_sv.md`, khối báo cáo các lệnh, git log.

- Harness HW04 (AI hỗ trợ tạo): skill `playwright-ddt-automation` (SKILL.md, 4 script, 3 asset), `HW04/tests/` (config, global-setup, fixture, page object), `tools/hw04_summary.py`, `tools/restart_backend.ps1`, cấu hình prompt log `tools/hw.toml`.
- Việc AI làm ngoài phạm vi lệnh / sự cố:
  - `rm -rf ../reports/chrome_*` (khi probe) xoá nhầm report đã commit → khôi phục ngay bằng `git checkout -- HW04/reports`; từ đó probe dùng `--reporter=line`, chỉ xoá thư mục mới.
  - 3 report rỗng 13:46 (global-setup không thấy backend) → xoá theo lệnh #14.
  - Tiến trình nền web/admin bị Claude Code dừng do máy thiếu bộ nhớ (17/11); AI không tự bật lại.
  - TC-60 firefox lượt thử 2 B: worker crash `0xC0000409` → SV chạy lại 3/3 Pass → lỗi hạ tầng (B RUN.md).
  - 17/11 tối, A (không chính thức): Windows Code Integrity chặn `firefox-1572\firefox.exe` (sự kiện 3077/3033, 23:05) → lượt gộp 22:56 (firefox 0/15, `spawn UNKNOWN`) và firefox riêng 23:05 (0/15); sau khi khởi động lại máy firefox 23:22 = 7P/8F, khớp chính thức. Chính thức giữ 13:47–13:52; report 3 lượt này không commit. Log: `HW04/env/firefox_blocked_20261117.txt` (A RUN.md).
- Lỗi do AI, phát hiện sau:
  - **C3 chép nhầm** vào "Yêu cầu bị vi phạm" của BUG-101, BUG-103 (generator lấy mọi dòng Yêu cầu của HW02 BUG-35/37) → sửa `d6cd474`.
  - C TC-07: ô không hợp lệ ghi 2 lần (`checkValidity()` cũng bắn `invalid`) – AI phát hiện ở lệnh #17 → sửa 5/6a `2e9e454`.
- Lỗi script AI do **phiên thảo luận** phát hiện (khi đối chiếu code):
  - A: `mode: 'serial'` (1 Fail chặn 14 TC) → 5/6a `6fc76b5`.
  - A: nhóm regex `^(…|…)` trong `oracleOf`, thiếu escape trước `new RegExp` → 5/6c `740934b`.
  - A: `users.list()` gọi ngay sau khi race kết thúc, không chờ phản hồi `POST /api/register` (A_FR01/review_sv.md "Phiên thảo luận bổ sung") → 5/6b `5a378f1`.
  - C: `errShown` đếm mọi hộp thoại (kể cả "Cập nhật thành công!") là "có thông báo lỗi" → R3=a giữ, ghi điểm yếu.
- Lỗi skill lộ ra khi chạy demo / chạy thử (18/11, lệnh #26–#28):
  - Template spec v1 còn `test.describe.configure({ mode: 'serial' })` – lỗi đã sửa ở A 5/6a nhưng chưa đưa ngược vào skill → sửa ở v2 `5bb31d1`.
  - Bản đóng băng nằm trong thư mục Playwright quét (demo đóng băng vào thư mục demo) → có thể bị nạp như spec → v2.1 `99080b2`: `freeze.py` từ chối `--out` trong testDir, đổi đuôi `*.ts.txt`.
  - Template v2 chờ riêng `POST` sau khi bấm → TC-01, TC-63 (ứng dụng tự kiểm phía client, không gửi POST) bị Blocked giả "chờ POST quá 10000 ms" → v2.1: chờ một trong các nhánh phản hồi (request / URL đổi / thông báo / hộp thoại).
  - Config chính thức (testMatch `*.spec.ts`) nạp luôn spec demo (`--list` 4 file, thừa 45 test) → v2.1: spec demo đuôi `*.demo.ts`.
  - Phiên thảo luận không ra lệnh cập nhật skill sau review A (bài học A chỉ sửa trong spec A) → B, C và template vẫn mang bản v1 tới lệnh #27.
- Script tạm AI viết, **không commit**: sinh 18 khung bug (`gen_bugs.py`), Playwright tái hiện 18 bug (`repro.spec.ts`), tạo issue (`mk_issues.py`), chụp trang Issues (`shot.cjs`), đọc phiên bản trình duyệt.
- AI chạy `gh issue create` 18 lần (#298–#315) với file SV viết; chụp `issues_page_1.png` (chưa đăng nhập GitHub).
- AI chỉ xem mẫu ảnh evidence (A 3/48, B 3/54, C 2/54) – SV xem phần còn lại.
- Prompt log: AI thêm bộ đọc bản xuất dữ liệu claude.ai (`conversations.json`) vào `tools/extract_prompt_log.py` (`86d4d78`); hội thoại chép nguyên văn vào `.transcripts/claude-ai_session_HW04_p1.json` (không nộp). 36 lượt claude.ai ghi "Claude (không rõ model)" vì bản xuất không ghi model; SV xác nhận dùng Opus 5.5 (ghi ở `prompt_log_notes.toml`, trường `ghi_chu_model`, chỉ áp cho lượt claude.ai qua `nguon_luot`).

## 4. Kết luận chung

`<SV viết>`

## 5. AI Critique

Xem report chính `23120255_HW04_Report.md` §8.

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
