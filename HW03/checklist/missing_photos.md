# Ảnh còn thiếu – T1/T3 (AI liệt kê 10/11, chỉ đọc; SV chụp/thêm overlay 🔒)

Đối chiếu: quy tắc ảnh `RUN.md` mục 2 ((a) mỗi item **Failed** ở lượt tay: `P<n>_<id>_<k>.png`; (b) 1 ảnh tổng quan mỗi màn / nền tảng `P<n>_M<k>_1.png`, M1…M5), bảng ảnh tổng quan ở report §4.3, và `evidence` của mọi ô Failed/Blocked trong `checklist.json`.

## 1. Bắt buộc – còn thiếu

| Tên file cần có | Item / màn | Nền tảng | Nội dung cần thấy trong ảnh | Hiện trạng |
|---|---|---|---|---|
| `evidence/P3_android/P3_M1_1.png` | M1 – Đăng nhập (`/login`) | P3 | Toàn màn Đăng nhập trên Chrome Android, thấy thanh URL `localhost:5173/login`, overlay `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn` | Có bản gốc `evidence_raw/P3_android/P3_M1_1.jpg`, **chưa overlay** |
| `evidence/P3_android/P3_M2_1.png` | M2 – Quên mật khẩu bước 1 (`/forgot-password`) | P3 | Màn nhập Email (bước 1), thanh URL, overlay | Có `evidence_raw/P3_android/P3_M2_1.jpg`, **chưa overlay** |
| `evidence/P3_android/P3_M2_2.png` | M2 – Quên mật khẩu bước 2 | P3 | Màn OTP + mật khẩu mới (bước 2), thanh URL, overlay | Có `evidence_raw/P3_android/P3_M2_2.jpg`, **chưa overlay** |
| `evidence/P3_android/P3_M3_1.png` | M3 – Hồ sơ (`/profile`) + **M5 – Navbar khi đã đăng nhập** (dùng lại, R-M5) | P3 | Màn Hồ sơ đã đăng nhập, thấy navbar (lời chào + nút đăng xuất), thanh URL, overlay | Có `evidence_raw/P3_android/P3_M3_1.jpg`, **chưa overlay** |
| `evidence/P3_android/P3_M4_1.png` | M4 – Lịch sử đơn (phần "Lịch sử đơn hàng" trong `/profile`, có ≥ 1 đơn) | P3 | Phần Lịch sử đơn, thanh URL, overlay (SV giữ ảnh lịch sử đơn trống lúc chụp – 4/6e) | Có `evidence_raw/P3_android/P3_M4_1.jpg`, **chưa overlay** |

Xong overlay → đặt lại vào `evidence_raw/P3_android/` rồi `python tools/compress_hw03.py --exclude ""` (handoff 10/11), chạy lại `python tools/report_t1_hw03.py` để §4.3 hết "chưa có".

Ảnh item Failed ở lượt tay: **không thiếu** (mọi ô Failed có `nguon_kq = tay` trên P1, P2, P3 đều có ảnh và file tồn tại trong `evidence/`).

## 2. Không bắt buộc theo quy tắc, ghi để SV biết

| Tên file | Item / màn | Nền tảng | Lý do không bắt buộc | Ghi chú |
|---|---|---|---|---|
| `P1_M6_1.png`, `P2_M6_1.png`, `P3_M6_1.png` | M6 – "Chung – tất cả màn C2" (nhóm item CL-01…) | P1, P2, P3 | `RUN.md` mục 2 và report §4.3 chỉ yêu cầu M1…M5; tiêu đề nhóm M6 trong bảng `RUN.md` mục 4 (dòng 81, 135, 182) sinh từ `gen_run.py` ghi "ảnh tổng quan bắt buộc" – không nhất quán với mục 2 | **SV chốt M6=a (4/6e): bỏ**; tiêu đề M6 trong `RUN.md` đã sửa |
| `P3_CL-64_1.jpg` | CL-64 (Blocked) | P3 | Quy tắc ảnh chỉ bắt buộc cho Failed | **4/6e: bỏ tham chiếu** trong file lượt P3 (không tồn tại ở đâu); notes "ảnh _1 không có; chỉ _2" |
| (không có ảnh) | CL-27, CL-48 (Blocked, kết quả từ lượt auto) | P1, P2, P3 (CL-48: P1, P2) | Blocked, lượt auto không chụp ảnh khi test dừng | – |
