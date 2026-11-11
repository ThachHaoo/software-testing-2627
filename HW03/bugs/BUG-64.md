# BUG-64

- **ID:** BUG-64
- **Tiêu đề:** [Quên MK B2, Hồ sơ] Thông báo lỗi validate chỉ hiện ở hộp thoại alert trình duyệt
- **Severity:** Medium
- **Priority:** Medium
- Tiền tố GitHub: [HW03-C2-64]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-23: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-23: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-23: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-23 – Quên mật khẩu, Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Backend vừa restart. Màn hình Hồ sơ (`http://localhost:5173/profile`) đã đăng nhập tài khoản `test@eshop.com` / `Test1234!`. Màn hình Quên mật khẩu bước 2 đã hoàn thành gửi OTP từ bước 1.

## Các bước tái hiện

1. Truy cập trang Quên mật khẩu bước 2 (`http://localhost:5173/forgot-password`). Nhập OTP đúng và Mật khẩu mới yếu (ví dụ '123'), sau đó bấm nút 'Đặt lại mật khẩu'. Quan sát vị trí xuất hiện thông báo lỗi.
2. Đăng nhập tài khoản `test@eshop.com` / `Test1234!` và truy cập trang Hồ sơ (`http://localhost:5173/profile`).
3. Nhập Số điện thoại sai định dạng (ví dụ '123') vào ô Số điện thoại rồi bấm nút 'Cập nhật'. Quan sát vị trí xuất hiện thông báo lỗi.

## Expected (trích căn cứ)

- CL-23 – căn cứ: FR-22.4 (README.md:255); giả định GA3
  - FR-22.4, README.md:255 (AI chép nguyên văn): Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
  - Giả định trong checklist (AI chép nguyên văn): GA3: thông báo lỗi chỉ ở hộp thoại alert() không thoả FR-22.4.
- Expected của bug: Khi nhập dữ liệu vi phạm quy tắc validate (mật khẩu mới yếu ở Quên mật khẩu B2, SĐT sai định dạng ở Hồ sơ), thông báo lỗi phải xuất hiện trực tiếp trong trang web tại vị trí phía trên nút submit, không phải chỉ hiển thị ở hộp thoại trình duyệt (alert).

## Actual

- **Tại trang Quên mật khẩu B2 (mật khẩu yếu):** Cả P1, P2 và P3 không có chữ thông báo lỗi nào xuất hiện trong trang phía trên nút submit; thông báo lỗi chỉ hiện ở hộp thoại alert trình duyệt ("Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.").
- **Tại trang Hồ sơ (SĐT sai định dạng '123'):** Cả P1, P2 và P3 không hiển thị chữ thông báo lỗi trong trang phía trên nút submit; hệ thống chỉ hiển thị hộp thoại alert trình duyệt với nội dung "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.".

## Bằng chứng

- CL-23 P1 (auto): `../checklist/evidence/auto/P1_CL-23_1.png`
- CL-23 P2 (auto): `../checklist/evidence/auto/P2_CL-23_1.png`
- CL-23 P3 (auto): `../checklist/evidence/auto/P3_CL-23_1.png`

## Item liên quan

- CL-23 – Thông báo lỗi validate hiển thị trong trang, phía trên nút submit – Failed: P1, P2, P3
- Nhóm dữ kiện: G-07 trong `HW03/bugs/bug_groups.md` (Lỗi validate chỉ hiện ở hộp thoại trình duyệt (Quên MK B2, Hồ sơ)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-22.4 (README.md:255); giả định GA3:** Thông báo lỗi validate hiển thị trong trang, phía trên nút submit (CL-23)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-23 P1 (auto): `Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"]`
- Actual nguyên văn CL-23 P2 (auto): `Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Protocol error (Browser.removeBrowserContext): this._windows[aWindow.__SSi] is undefined · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"]`
- Actual nguyên văn CL-23 P3 (auto): `Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"]`
- Nguồn bước tái hiện CL-23: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:453`

### Nhận định

Thông báo lỗi hiển thị qua hộp thoại alert làm gián đoạn trải nghiệm người dùng, không tuân thủ tiêu chuẩn thiết kế phản hồi lỗi trực tiếp trong trang theo quy định FR-22.4 (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/264

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).