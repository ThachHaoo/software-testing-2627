# BUG-63

- **ID:** BUG-63
- **Tiêu đề:** [Đăng nhập, Quên MK, Hồ sơ] Nhãn các trường bắt buộc thiếu dấu '*'
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-63]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-20: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-21: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-20: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-21: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-20: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-21: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-20 – Đăng nhập, Quên mật khẩu; CL-21 – Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Màn hình Hồ sơ (`/profile`) yêu cầu đăng nhập tài khoản `test@eshop.com` / `Test1234!`.

## Các bước tái hiện

1. Truy cập trang Đăng nhập (`http://localhost:5173/login`) và trang Quên mật khẩu (`http://localhost:5173/forgot-password` ở bước 1 và bước 2).
2. Quan sát các nhãn (label) cạnh từng ô nhập liệu.
3. Đăng nhập tài khoản `test@eshop.com` / `Test1234!`, truy cập trang Hồ sơ (`http://localhost:5173/profile`).
4. Quan sát các nhãn "Họ Tên", "Số điện thoại", "Địa chỉ giao hàng" và lần lượt thử xóa trống từng trường rồi bấm nút 'Cập nhật' để kiểm tra tính bắt buộc của form.

## Expected (trích căn cứ)

- CL-20 – căn cứ: FR-22.1 (README.md:252); checklist Text box – 'Red asterisk on mandatory fields'
  - FR-22.1, README.md:252 (AI chép nguyên văn): Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- CL-21 – căn cứ: FR-22.1 (README.md:252)
  - FR-22.1, README.md:252 (AI chép nguyên văn): Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- Expected của bug: Tất cả các nhãn trường bắt buộc nhập trên form (bao gồm Email, Mật khẩu ở Đăng nhập; Email ở Quên mật khẩu bước 1; OTP, Mật khẩu mới, Xác nhận mật khẩu ở Quên mật khẩu bước 2; và các trường bị chặn khi để trống ở Hồ sơ như Họ Tên, Số điện thoại, Địa chỉ giao hàng) đều phải hiển thị dấu `*` bên cạnh nhãn.

## Actual

- Cả P1, P2 và P3:
  - **Màn hình Đăng nhập (/login):** Nhãn "Username" và nhãn "Mật khẩu" đều thiếu dấu `*`.
  - **Màn hình Quên mật khẩu (/forgot-password):** Nhãn "Nhập Email của bạn" ở bước 1, nhãn "Mã OTP (4 số)" và "Mật khẩu mới" ở bước 2 đều thiếu dấu `*`.
  - **Màn hình Hồ sơ (/profile):** Cả 3 trường "Họ Tên", "Số điện thoại", "Địa chỉ giao hàng" khi để trống đều khiến form bị chặn không cho cập nhật, nhưng nhãn của cả 3 trường này đều thiếu dấu `*`.

## Bằng chứng

- CL-20 P1 (auto): `../checklist/evidence/auto/P1_CL-20_1.png`
- CL-20 P2 (auto): `../checklist/evidence/auto/P2_CL-20_1.png`
- CL-20 P3 (auto): `../checklist/evidence/auto/P3_CL-20_1.png`
- CL-21 P1 (auto): `../checklist/evidence/auto/P1_CL-21_1.png`
- CL-21 P2 (auto): `../checklist/evidence/auto/P2_CL-21_1.png`
- CL-21 P3 (auto): `../checklist/evidence/auto/P3_CL-21_1.png`

## Item liên quan

- CL-20 – Dấu * trên nhãn trường bắt buộc – Failed: P1, P2, P3 · một phần #7 (#7 phủ /login; Quên MK bước 1/2 chưa có issue)
- CL-21 – Dấu * trên trường mà form bắt buộc nhập – Failed: P1, P2, P3
- Nhóm dữ kiện: G-06 trong `HW03/bugs/bug_groups.md` (Nhãn trường bắt buộc thiếu '*' ở Quên mật khẩu B1/B2 và Hồ sơ (phần /login trùng #7)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-22.1 (README.md:252); checklist Text box – 'Red asterisk on mandatory fields':** Dấu * trên nhãn trường bắt buộc (CL-20)
- **FR-22.1 (README.md:252):** Dấu * trên trường mà form bắt buộc nhập (CL-21)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-20 P1 (auto): `Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới"`
- Actual nguyên văn CL-20 P2 (auto): `Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới"`
- Actual nguyên văn CL-20 P3 (auto): `Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới"`
- Nguồn bước tái hiện CL-20: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:139`
- Actual nguyên văn CL-21 P1 (auto): `Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng"`
- Actual nguyên văn CL-21 P2 (auto): `Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng"`
- Actual nguyên văn CL-21 P3 (auto): `Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng"`
- Nguồn bước tái hiện CL-21: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:435`

### Nhận định

Người dùng gặp khó khăn trong việc nhận biết các trường dữ liệu nào bắt buộc phải điền, dễ dẫn đến thao tác thiếu và gây nhầm lẫn khi thực thi biểu mẫu (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).