# Còn phải làm trước khi gộp (T1 4/6) – sau lượt kiểm 10/11

Ảnh đạt đã nén + đổi tên vào `evidence/P*/` (commit 4/6a1). Ảnh dưới đây **đang ở `evidence_raw/`** (gitignore, chưa commit). Sửa xong → đặt vào `evidence_raw/<Px_dir>/` đúng tên đích → báo AI chạy `tools/compress_hw03.py`.

## 1. Chụp / sửa ảnh (SV)

| # | Việc | Tên đích (`evidence_raw/...`) | Ghi chú |
|---|---|---|---|
| 1 | Thêm overlay `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn` (trình sửa ảnh của máy) | `P3_android/P3_M1_1.jpg`, `P3_M2_1.jpg`, `P3_M2_2.jpg`, `P3_M3_1.jpg`, `P3_M4_1.jpg` | 5 ảnh tổng quan Task 3 của P3 còn thiếu overlay. Nội dung đã đúng màn |
| 2 | Chụp **M5 – Navbar khi đã đăng nhập** (có overlay, thấy URL) | `P1_chrome/P1_M5_1.png`, `P2_firefox/P2_M5_1.png`, `P3_android/P3_M5_1.jpg` | Hoặc chốt dùng ảnh M3/M4 (navbar có ở đầu trang) làm M5: báo AI để ghi vào README/report thay vì chụp |
| 3 | P3 CL-52: ảnh khoá đăng nhập | `P3_android/P3_CL-52_1.jpg` | Ảnh hiện tại `P3_CL-52_1.jpg` chụp bảng Lịch sử đơn (sai màn). Có thể dùng ảnh `P3_CL-64_1.jpg` hiện tại (đăng nhập thất bại, có overlay) nếu đó đúng là ảnh của CL-52: xem mục 2 |

## 2. Đổi tên (SV xác nhận → AI làm)

| Ảnh hiện tại (`evidence_raw/`) | Nội dung thấy trong ảnh | Đổi thành (đề xuất) |
|---|---|---|
| `P1_chrome/P1_M3_1.png` | Quên MK bước 2 | `P1_M2_1.png` (M2 = Quên MK; B1 đã có ở `P1_M2_2`) |
| `P1_chrome/P1_M2_1.png` | /profile (Hồ sơ, chưa có đơn) | `P1_M3_1.png` |
| `P2_firefox/P2_M2_1.png` | /login | `P2_M1_1.png` |
| `P2_firefox/P2_M3_1.png` | Quên MK bước 2 | `P2_M2_1.png` (B1 đã có ở `P2_M2_2`) |
| `P2_firefox/P2_M1_1.png` | /profile (Hồ sơ, chưa có đơn) | `P2_M3_1.png` |
| `P2_firefox/P2_CL-52_1.png` | alert "Số điện thoại không hợp lệ…" (nội dung CL-64) | `P2_CL-64_1.png` |
| `P2_firefox/P2_CL-64_1.png` | đăng nhập thất bại + Network (nội dung CL-52) | `P2_CL-52_1.png` |
| `P3_android/P3_CL-64_1.jpg` | đăng nhập thất bại (nội dung CL-52) | `P3_CL-52_1.jpg` (thay ảnh sai màn ở mục 1.3) |
| `P3_android/P3_CL-52_1.jpg` | bảng Lịch sử đơn | bỏ (không thuộc item nào) |
| `evidence/P3_android/P3_CL-64_2.png` (đã commit) | alert SĐT (CL-64) | giữ, hoặc đổi thành `P3_CL-64_1.png` |

## 3. File kết quả (SV)

- `runs/P1_manual_20261109-2257.md`: dòng "Bắt đầu – kết thúc" và "Restart backend lúc" lệch ngày (R4).
- Cả 3 file: "Mã đơn (seed_orders.py)" trống; bảng "Ảnh tổng quan Task 3" trống (AI điền bảng ảnh sau khi xong mục 1–2).
- Cột `ảnh` ghi tên cũ (`P1_CL01_1.png`, `P1_SV01_1.png`…). AI tự ánh xạ sang tên mới khi gộp, không sửa file của SV.
- Verdict cần SV xem lại (`run_check.md`): R9 (CL-08 P1), R11 (CL-09 P1), bảng lệch auto ↔ tay L1–L8. Theo V1 thì lấy kết quả tay, nhưng SV vẫn chốt từng dòng.
