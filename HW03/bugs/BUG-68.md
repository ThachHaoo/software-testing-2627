# BUG-68

- **ID:** BUG-68
- **Tiêu đề:** [Quên MK B2] Màn hình thiếu ô nhập 'Xác nhận mật khẩu mới'
- **Severity:** High
- **Priority:** High
- Tiền tố GitHub: [HW03-C2-68]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-26: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-26: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-26: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-26 – Quên mật khẩu (bước 2)
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Trạng thái chưa đăng nhập.

## Các bước tái hiện

1. Truy cập vào trang Quên mật khẩu (`http://localhost:5173/forgot-password`).
2. Nhập email hợp lệ ở bước 1 và bấm nút 'Lấy mã OTP' để chuyển sang bước 2.
3. Quan sát các ô nhập liệu xuất hiện ở biểu mẫu bước 2.

## Expected (trích căn cứ)

- CL-26 – căn cứ: FR-03.5 (README.md:57)
  - FR-03.5, README.md:57 (AI chép nguyên văn): Người dùng nhập OTP, Mật khẩu mới, và **Xác nhận mật khẩu mới**.
- Expected của bug: Màn hình Quên mật khẩu bước 2 phải hiển thị đủ 3 ô nhập liệu: Mã OTP, Mật khẩu mới, và Xác nhận mật khẩu mới.

## Actual

- Cả P1, P2 và P3: Màn hình Quên mật khẩu bước 2 chỉ có 2 ô nhập liệu là "Mã OTP (4 số)" và "Mật khẩu mới", hoàn toàn thiếu ô "Xác nhận mật khẩu mới".

## Bằng chứng

- CL-26 P1 (auto): `../checklist/evidence/auto/P1_CL-26_1.png`
- CL-26 P2 (auto): `../checklist/evidence/auto/P2_CL-26_1.png`
- CL-26 P3 (auto): `../checklist/evidence/auto/P3_CL-26_1.png`

## Item liên quan

- CL-26 – Có ô 'Xác nhận mật khẩu mới' – Failed: P1, P2, P3 · liên quan #30 (#30 là form Đăng ký; Quên MK bước 2 chưa có issue)
- Nhóm dữ kiện: G-11 trong `HW03/bugs/bug_groups.md` (Quên mật khẩu B2: không có ô Xác nhận mật khẩu mới); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-03.5 (README.md:57):** Có ô 'Xác nhận mật khẩu mới' (CL-26)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-26 P1 (auto): `Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"]`
- Actual nguyên văn CL-26 P2 (auto): `Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"]`
- Actual nguyên văn CL-26 P3 (auto): `Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"]`
- Nguồn bước tái hiện CL-26: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:299`

### Nhận định

Việc thiếu ô nhập Xác nhận mật khẩu mới làm tăng rủi ro người dùng gõ sai mật khẩu mà không phát hiện ra, ảnh hưởng trực tiếp đến quy trình khôi phục tài khoản an toàn (chưa kiểm chứng). Liên quan issue #30.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).