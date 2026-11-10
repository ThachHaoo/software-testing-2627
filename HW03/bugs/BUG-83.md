# BUG-83

- **ID:** BUG-83
- **Tiêu đề:** [Đăng nhập, Quên MK B2, Hồ sơ] Submit thất bại không tự động focus về ô nhập bị lỗi
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-83]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · SV-03: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · SV-03: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · SV-03: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: SV-03 – Đăng nhập, Quên mật khẩu B2, Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Màn hình Hồ sơ (`http://localhost:5173/profile`) đã đăng nhập tài khoản `test@eshop.com` / `Test1234!`. Màn hình Quên mật khẩu B2 đã gửi mã OTP ở bước 1.

## Các bước tái hiện

1. **Trang Đăng nhập (`http://localhost:5173/login`):** Nhập mật khẩu sai quy tắc/không đúng rồi bấm nút submit ('Sign In'). Sau khi thông báo xuất hiện, quan sát vị trí con trỏ focus.
2. **Trang Quên mật khẩu B2 (`http://localhost:5173/forgot-password`):** Nhập OTP đúng, nhập Mật khẩu mới không đủ điều kiện (ví dụ '123') rồi bấm nút 'Đặt lại mật khẩu'. Quan sát vị trí con trỏ focus.
3. **Trang Hồ sơ (`http://localhost:5173/profile`):** Nhập Số điện thoại sai định dạng (ví dụ '123') rồi bấm nút 'Cập nhật'. Quan sát vị trí con trỏ focus.

## Expected (trích căn cứ)

- SV-03 – căn cứ: Slide "Checklist - input-field validation" (Golden Rule: "On error, return focus to the offending field"); Shneiderman #5 (Xử lý lỗi đơn giản)
- Expected của bug: Nhập dữ liệu sai quy tắc (ví dụ: SĐT sai định dạng ở Hồ sơ hoặc Mật khẩu mới không đủ điều kiện ở Quên mật khẩu B2) rồi bấm submit: sau khi thông báo lỗi xuất hiện, con trỏ gõ phím (cursor) phải tự động quay lại focus ở đúng ô bị lỗi đó.

## Actual

- Cả P1, P2 và P3: Sau khi submit thất bại, con trỏ gõ phím không tự động quay lại focus ở ô bị lỗi trên cả 3 màn hình (`focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false`). Con trỏ bị mất focus hoặc không nhảy về đúng ô nhập liệu gây lỗi.

## Bằng chứng

- SV-03 P1 (auto): `../checklist/evidence/auto/P1_SV-03_1.png`
- SV-03 P2 (auto): `../checklist/evidence/auto/P2_SV-03_1.png`
- SV-03 P3 (auto): `../checklist/evidence/auto/P3_SV-03_1.png`

## Item liên quan

- SV-03 – Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại – Failed: P1, P2, P3
- Nhóm dữ kiện: G-26 trong `HW03/bugs/bug_groups.md` (Submit thất bại: focus không về ô lỗi); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Slide "Checklist - input-field validation" (Golden Rule: "On error, return focus to the offending field"); Shneiderman #5 (Xử lý lỗi đơn giản):** Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại (SV-03)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn SV-03 P1 (auto): `Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false`
- Actual nguyên văn SV-03 P2 (auto): `Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false`
- Actual nguyên văn SV-03 P3 (auto): `Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false`
- Nguồn bước tái hiện SV-03: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:868`

### Nhận định

Không trả con trỏ focus về đúng trường bị lỗi khiến người dùng phải mất thêm thao tác di chuyển chuột hoặc bấm Tab để chọn lại ô lỗi, làm gián đoạn luồng sửa lỗi biểu mẫu (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).