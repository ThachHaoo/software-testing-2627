# Còn phải làm trước khi nộp (T1 4/6) – cập nhật 10/11 sau 4/6a2

Ảnh đạt đã nén + đổi tên vào `evidence/P*/`. Ảnh còn lỗi **đang ở `evidence_raw/`** (gitignore, chưa commit). Sửa xong → đặt vào `evidence_raw/<Px_dir>/` đúng tên đích → báo AI chạy `tools/compress_hw03.py`.

## 1. Còn phải làm (SV)

| # | Việc | Tên đích (`evidence_raw/...`) | Ghi chú |
|---|---|---|---|
| 1 | Thêm overlay `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn` (trình sửa ảnh của máy) | `P3_android/P3_M1_1.jpg`, `P3_M2_1.jpg`, `P3_M2_2.jpg`, `P3_M3_1.jpg`, `P3_M4_1.jpg` | 5 ảnh tổng quan Task 3 của P3. Nội dung đúng màn, chỉ thiếu overlay |

## 2. M5 – Navbar khi đã đăng nhập: dùng lại ảnh M3/M4 (R-M5, không chép file trùng)

| Nền tảng | Ảnh dùng cho M5 | Thấy trong ảnh |
|---|---|---|
| P1 | `evidence/P1_chrome/P1_M4_1.png` (cũng thấy ở `P1_M3_1.png`) | Giỏ hàng · Chào, Test User · Thoát |
| P2 | `evidence/P2_firefox/P2_M4_1.png` (cũng thấy ở `P2_M3_1.png`) | Giỏ hàng · Chào, Test User · Thoát |
| P3 | `evidence/P3_android/P3_M3_1.png` (sau khi xong mục 1) | Giỏ hàng · Chào, Test User · Thoát. `P3_M4_1` đã cuộn qua navbar → không dùng |

## 3. Đã xong ở 4/6a2 (SV đồng ý)

- B3: P1 `M2_1` ↔ `M3_1`; P2 `M2_1`→`M1_1`, `M3_1`→`M2_1`, `M1_1`→`M3_1`.
- B4: P2 `CL-52_1` ↔ `CL-64_1`; P3 ảnh khoá đăng nhập → `P3_CL-52_1`; ảnh Lịch sử đơn sai màn đổi thành `evidence_raw/P3_android/_bo_P3_lichsudon_sai-man.jpg` (không dùng). CL-64 P3 dùng `P3_CL-64_2.png`.

## 4. File kết quả (SV)

- `runs/P1_manual_20261109-2257.md`: dòng "Bắt đầu – kết thúc" và "Restart backend lúc" lệch ngày (R4).
- Cả 3 file: "Mã đơn (seed_orders.py)" trống (R8).
- Cột `ảnh` trong file của SV ghi tên cũ; AI ánh xạ sang tên mới khi gộp (`evidence` trong `checklist.json`), không sửa file của SV.
