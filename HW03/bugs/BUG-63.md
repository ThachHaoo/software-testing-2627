# BUG-63

- **ID:** BUG-63
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
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

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- CL-20 – căn cứ: FR-22.1 (README.md:252); checklist Text box – 'Red asterisk on mandatory fields'
  - FR-22.1, README.md:252 (AI chép nguyên văn): Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- CL-21 – căn cứ: FR-22.1 (README.md:252)
  - FR-22.1, README.md:252 (AI chép nguyên văn): Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
