# BUG-66

- **ID:** BUG-66
- **Tiêu đề:** [Quên mật khẩu] Thiếu chỉ báo bước (Step Indicator) ở cả bước 1 và bước 2
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-66]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay · CL-24: lượt `runs/P1_manual_20261109-2257.md`, 22:58 09/11/2026 - 00:10 10/11/2026
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay · CL-24: lượt `runs/P2_manual_20261110-0010.md`, 00:10 10/11/2026 - 00:38 10/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay · CL-24: lượt `runs/P3_manual_20261110-0046.md`, 00:46 10/11/2026 - 01:54 10/11/2026
- Màn hình: CL-24 – Quên mật khẩu
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Trạng thái chưa đăng nhập.

## Các bước tái hiện

1. Truy cập vào trang Quên mật khẩu (`http://localhost:5173/forgot-password`).
2. Quan sát giao diện ở bước 1 (nhập Email).
3. Nhập email hợp lệ (`test@eshop.com`) và bấm nút 'Lấy mã OTP' để chuyển sang bước 2.
4. Quan sát giao diện ở bước 2 (nhập OTP và Mật khẩu mới).

## Expected (trích căn cứ)

- CL-24 – căn cứ: FR-03.3 (README.md:52); FR-22.5 (README.md:256)
  - FR-03.3, README.md:52 (AI chép nguyên văn): Giao diện phải hiển thị **chỉ báo bước (Step Indicator)** — ví dụ: "Bước 1 / 2".
  - FR-22.5, README.md:256 (AI chép nguyên văn): Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.
- Expected của bug: Bước 1 hiển thị 'Bước 1 / 2' (hoặc chỉ báo tương đương thấy rõ bước hiện tại và tổng số bước); bước 2 hiển thị 'Bước 2 / 2'.

## Actual

- Cả P1 (Cốc Cốc), P2 (Firefox) và P3 (Chrome Android): Ở cả bước 1 và bước 2 của quy trình Quên mật khẩu đều hoàn toàn không hiển thị chỉ báo bước (Step Indicator).

## Bằng chứng

- CL-24 P1 (tay): `../checklist/evidence/P1_chrome/P1_CL-24_1.png`
- CL-24 P2 (tay): `../checklist/evidence/P2_firefox/P2_CL-24_1.png`
- CL-24 P3 (tay): `../checklist/evidence/P3_android/P3_CL-24_1.png`

## Item liên quan

- CL-24 – Có chỉ báo bước (Step Indicator) – Failed: P1, P2, P3
- Nhóm dữ kiện: G-09 trong `HW03/bugs/bug_groups.md` (Quên mật khẩu: không có chỉ báo bước); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-03.3 (README.md:52); FR-22.5 (README.md:256):** Có chỉ báo bước (Step Indicator) (CL-24)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-24 P1 (tay): `Không có chỉ báo bước`
- Actual nguyên văn CL-24 P2 (tay): `Không có chỉ báo bước`
- Actual nguyên văn CL-24 P3 (tay): `Không có chỉ báo bước`
- Nguồn bước tái hiện CL-24: tiền điều kiện (checklist): – · cách kiểm: auto: tìm chữ 'Bước k / 2'; không thấy → SV xác nhận không có chỉ báo tương đương · test tự động: `HW03/tests/C2.spec.ts:279`

### Nhận định

Người dùng không nhận biết được vị trí tiến trình hiện tại và tổng số bước cần thực hiện trong quy trình quên mật khẩu (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).