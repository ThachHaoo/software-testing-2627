# Kiểm lượt chạy tay P1–P3 (T1 bước 4/6 – mục 1, chỉ đọc)

AI kiểm ngày 10/11/2026: đã xem từng ảnh trong `evidence/P1_chrome` (34 ảnh), `P2_firefox` (32 ảnh), `P3_android` (29 ảnh + `dom_result.json`); đọc 3 file `runs/*_manual_*`; so với `runs/P{1,2,3}_auto_20261109-22xx.json`. Không sửa chữ của SV. Kết luận Pass/Fail do SV quyết.

## 0. Lỗi chặn (phải xử lý trước khi nén, gộp)

| # | Lỗi | Phạm vi | Cần SV |
|---|---|---|---|
| B1 | **Ảnh P3 dạng `.jpg` không có overlay** (không thấy dòng `23120255 · Lê Tấn Hiệp · email`; đã xem ảnh gốc `P3_M1_1.jpg`) | 25 ảnh: tất cả `P3_*.jpg` (CL-01 ×4, CL-06, CL-08, CL-09, CL-15, CL-24, CL-52, CL-53, CL-62, CL-63 ×2, CL-64 ×2, M1, M2 ×2, M3, M4, SV-02 ×4). 4 ảnh `P3_SV-04_*.png` (chụp màn hình PC qua `chrome://inspect`) **có** overlay | Thêm overlay bằng trình sửa ảnh (O1) hoặc chụp lại. AI không được ghép overlay |
| B2 | **Thiếu ảnh Task 3 của M5 (Navbar)** | P1, P2, P3 (không có `P<n>_M5_1`) | Chụp M5, hoặc chốt dùng ảnh M3/M4 (navbar khi đã đăng nhập hiện ở đầu trang) làm ảnh M5 |
| B3 | **Nhãn ảnh M không khớp nội dung** | P1: `M2_1` = /profile, `M2_2` = Quên MK B1, `M3_1` = Quên MK B2, `M4_1` = /profile (chưa có đơn). P2: `M1_1` = /profile, `M2_1` = /login, `M2_2` = Quên MK B1, `M3_1` = Quên MK B2, `M4_1` = /profile. P3 đúng (M1 login, M2_1/M2_2 Quên MK B1/B2, M3 hồ sơ, M4 lịch sử) | Chốt bảng đổi tên (AI đổi tên được khi SV duyệt bảng) |
| B4 | **Ảnh item gắn nhầm** | P2: `P2_CL-52_1` chụp alert "Số điện thoại không hợp lệ…" (nội dung CL-64); `P2_CL-64_1` chụp đăng nhập thất bại + Network (nội dung CL-52), tức là **hai ảnh tráo nhau**. P3: `P3_CL-52_1` chụp bảng Lịch sử đơn (không phải khoá đăng nhập); ảnh khoá đăng nhập của P3 nằm ở `P3_CL-64_1`; `P3_CL-64_2` là alert SĐT | Xác nhận đổi tên. P3 CL-52 có thể thiếu ảnh đúng |
| B5 | **Lộ dữ liệu cá nhân** | `P1_SV-02-3`: gợi ý autofill hiện 2 email cá nhân (email trường + Gmail cá nhân). `P1_SV-02-4`: trình quản lý mật khẩu hiện 6 tài khoản đã lưu (Gmail cá nhân, tài khoản dự án khác `…@tickefy.*`, `accountantTest1@…`…) | Che/cắt vùng gợi ý hoặc chụp lại bằng profile trình duyệt sạch. AI không sửa nội dung ảnh |

## 1a. Ảnh – các điểm không chặn

- **Tên trình duyệt không thấy trên ảnh PC** (RUN.md yêu cầu chụp toàn màn hình, thấy tên trình duyệt + URL). P1/P2 chỉ chụp vùng cửa sổ, không có thanh tiêu đề hay taskbar. P1 nhận ra là **Cốc Cốc** qua nút "Hỏi AI" và bộ icon; P2 nhận ra Firefox qua thanh công cụ. URL `localhost:5173/...` thấy rõ trên mọi ảnh PC.
- P3: thấy thanh URL `localhost:5173/...` trên hầu hết ảnh, **trừ** `P3_CL-09_1`, `P3_CL-15_1`, `P3_CL-52_1`, `P3_CL-08_1`, `P3_CL-63_2` (trang đã cuộn, thanh URL ẩn). Không thấy tên thiết bị/trình duyệt trên ảnh điện thoại.
- Overlay PC dùng dấu "-" (`23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn`) thay "·" như O1. Không ảnh hưởng nhận diện.
- Không thấy đường dẫn `C:\Users\…`, token, hay `chrome://version` trong ảnh nào. Mật khẩu test `Test1234!` hiện rõ trên các ảnh CL-52/CL-53/CL-64. Đây là tài khoản test công khai (README:24), nhưng việc thấy được mật khẩu chính là nội dung bug #5.
- Số điện thoại nhập thử trong ảnh: `P1_CL-64_1` (`093466821`), `P2_CL-52_1` (`0934366723`, địa chỉ "10 Lê Lợi"). **SV xác nhận đây là số giả**; nếu là số thật thì che lại.
- Không có ảnh nhoè. Ảnh cuộn trang trên P3 vẫn thấy được vùng liên quan.
- Ảnh tên sai mẫu `P<n>_<id>_<k>`: `P1_SV-01-3/-4`, `P1_SV-02-1…4`, `P1_SV-04-1…4` dùng "-". Tên ảnh trong notes (`P1_CL01_1.png`, `P1_SV01_1.png`…) không khớp tên file thật (`P1_CL-01_1.png`). Sửa ở bước đổi tên (mục 2).
- Đủ ảnh cho mọi item manual Failed: P1 9/9, P2 11/11, P3 11/11 có ≥ 1 ảnh, nhưng xem B4 về CL-52/CL-64. Item auto Failed dùng ảnh phần tử ở `evidence/auto/` (Z1).

## 1b. File kết quả `runs/*_manual_*`

| # | File | Vấn đề | Đề xuất (SV quyết) |
|---|---|---|---|
| R1 | cả 3 | Giá trị `Pass` / `Fail`, ngoài tập `Passed/Failed/N/A/Blocked` | AI ánh xạ Pass→Passed, Fail→Failed khi chuyển sang CSV gộp (không sửa file gốc) |
| R2 | cả 3 | **CL-64 = N/A** nhưng P1/P2/P3 đều nằm trong `nen_tang`, notes không có mã giả định NAx. Notes: "Bị chặn bởi form, mặc dù nhập số điện thoại đúng" | Theo quy ước skill: bị lỗi khác chặn → **Blocked** + item gốc. `merge_platform.py` từ chối N/A ở nền tảng áp dụng |
| R3 | P1 | Trình duyệt ghi **Cốc Cốc 160.0.106**, trong khi P1 = "Chrome trên Windows" (env: Chrome 157.0.8103.39; lượt auto P1 chạy Chrome 157) | Xem quyết định Q1 |
| R4 | P1 | Thời gian "22:58 09/11/2026 - 22:06 10/11/2026", restart "22:56 10/11/2026": ngày/giờ không khớp nhau (kết thúc trước khi restart?) | SV sửa |
| R5 | P2 | Tiêu đề file ghi "# P1 – kết quả chạy tay (Chrome trên Windows)", nhưng nội dung là Firefox 159.0.1 | SV sửa |
| R6 | P3 | OS ghi "Android 12"; `adb getprop ro.build.version.release` = **14** (env/environment.md) | SV kiểm lại |
| R7 | P2, P3 | Tên file thiếu đuôi `.md` (`P2_manual_20261110-0010`, `P3_manual_20261110_0046`; P3 dùng "_" thay "-") | AI đổi tên khi commit (nội dung không đổi) |
| R8 | cả 3 | "Mã đơn (seed_orders.py)" trống; bảng "Ảnh tổng quan Task 3" trống | SV điền, hoặc AI điền bảng ảnh sau khi chốt B2/B3 |
| R9 | P1 | **CL-08 Passed** trong khi P2, P3 Failed vì phân cách khác ("30.000.000 ₫" trên P1 so với "6,000,000 ₫" trên P2/P3). Expected: "cùng một kiểu phân cách trên cả 3 nền tảng… Fail nếu… kiểu phân cách khác nhau giữa các nền tảng" → vế này áp dụng cho cả P1 | **Đã chốt (4/6c): SV chọn b → P1 Failed** (override trong `tools/merge_hw03.py`, không sửa file lượt tay) |
| R10 | P2, P3 | CL-08 notes "phân cách hàng nghìn lại dùng ','": Expected **chấp nhận** dấu phẩy ("vd 30.000.000 ₫ hoặc 30,000,000 ₫"); lý do Fail đúng theo Expected là *khác kiểu giữa nền tảng*, không phải *dùng dấu phẩy* | SV chỉnh câu notes (lý do) |
| R11 | P1 | **CL-09 Passed**, nhưng ảnh `P1_CL-09_1` hiện "9/11/2026" (ngày 1 chữ số, không phải dd/mm/yyyy) và khác P2/P3 ("11/9/2026"). Expected: "dd/mm/yyyy và giống nhau trên P1, P2, P3" | **Đã chốt (4/6c): SV chọn b → P1 Failed** (override trong `tools/merge_hw03.py`, không sửa file lượt tay) |
| R12 | P1 | SV-02 notes "Autofill chỉ có ở Forgot Password": Expected Fail khi autofill "bị hệ thống ngăn chặn/làm sai lệch". Notes chưa nói hệ thống chặn hay trình duyệt không gợi ý | SV ghi rõ (không chặn gộp) |

Không có item nào thiếu kết quả: P1 15/15, P2 15/15, P3 13/13 so với template.

## 1c. Auto ↔ manual lệch (cùng item, cùng nền tảng) – SV chốt verdict

Lượt auto: `P1_auto_20261109-2236.json` (Chrome 157), `P2_auto_20261109-2240.json` (Firefox 131 Playwright), `P3_auto_20261109-2244.json` (Chrome Android 156).

| # | Item | Nền tảng | Manual | Auto | Số đo auto (notes) | Ghi chú AI | Verdict SV |
|---|---|---|---|---|---|---|---|
| L1 | CL-09 | P1 | Pass | Failed | "không phải dd/mm/yyyy: 9/11/2026" | Ảnh manual cũng là "9/11/2026" (xem R11) | **Đã chốt: Failed (R11=b)** |
| L2 | CL-11 | P1 | Pass | Failed | "nhảy ngược theo toạ độ: 'Cập nhật'(169,557) → 'Hủy đơn'(1010,203)" | Bố cục 2 cột: theo che_do_ghi_chu, SV đọc chuỗi Tab để xác nhận "cùng hàng" | CHỜ SV |
| L3 | CL-11 | P2 | Pass | Failed | "'Cập nhật'(169,553) → 'Hủy đơn'(1009,204)" | như L2 | CHỜ SV |
| L4 | CL-15 | P1 | Pass | Failed | "thanh cuộn ngang toàn trang (381 > 375)" | Ảnh manual P1 chụp cửa sổ hẹp, không thấy thanh cuộn ngang | CHỜ SV |
| L5 | CL-15 | P2 | Pass | Failed | "(382 > 375)" | như L4 | CHỜ SV |
| L6 | CL-08 | P2 | Fail | Passed | "6.000.000 ₫" ×7 | **Auto dùng locale vi-VN** (playwright.config `locale: 'vi-VN'`) nên ra dấu chấm; Firefox thật của SV hiện "6,000,000 ₫". Lệch do môi trường, không phải do SUT đổi | CHỜ SV |
| L7 | CL-08 | P3 | Fail | Passed | "6.000.000 ₫" ×7 | như L6 (Chrome Android của SV hiện "6,000,000 ₫") | CHỜ SV |
| L8 | SV-02 | P1 | Fail | Passed | "/login sau Ctrl+V = test@eshop.com" | Auto chỉ kiểm vế dán; vế autofill chạy tay. Không mâu thuẫn bản chất | CHỜ SV |

Ghi chú: cột Ngày đặt của auto P2/P3 cũng là "9/11/2026" (locale vi-VN), còn manual P2/P3 là "11/9/2026", nhưng hai bên cùng Failed nên không đưa vào bảng.

## Quyết định cần SV

- **Q1 (P1 = Cốc Cốc):** (a) chạy lại 15 item manual P1 trên Chrome 157; (b) giữ Cốc Cốc 160 làm P1 (cùng nhân Chromium), đổi tên nền tảng P1 trong report/env/meta và khai lệch so với kế hoạch; (c) giữ kết quả, ghi giới hạn.
- **Q2 (CL-64 ×3):** (a) Blocked; (b) chạy lại, bỏ trống ô SĐT (chỉ sửa Họ Tên) để kiểm đúng việc "tắt backend". Dữ kiện: ảnh P2 nhập 10 chữ số `0934…` vẫn bị alert "…đúng 9-10 chữ số", trùng tiêu đề issue nhóm **#111** "Web rejects a valid 10-digit 0-prefixed phone"; P1 nhập 9 chữ số.
- B1–B5 ở mục 0.
