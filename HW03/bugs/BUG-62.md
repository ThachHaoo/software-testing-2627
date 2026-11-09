# BUG-62

- **ID:** BUG-62
- **Nhóm dữ kiện:** G-05 (CL-20, CL-21)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-20 – Dấu * trên nhãn trường bắt buộc

- Màn hình: Đăng nhập, Quên mật khẩu
- Căn cứ: FR-22.1 (README.md:252); checklist Text box – 'Red asterisk on mandatory fields'
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #7 (#7 phủ /login; Quên MK bước 1/2 chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:139`

**Expected (chép từ checklist)**

> Nhãn Email, Mật khẩu (/login); Email (bước 1); OTP, Mật khẩu mới, Xác nhận mật khẩu (bước 2) đều có '*' cạnh nhãn. Fail nếu ≥ 1 nhãn thiếu '*'.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới"
- P2 (auto): Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới"
- P3 (auto): Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới"

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-20_1.png`
- P2: `../checklist/evidence/auto/P2_CL-20_1.png`
- P3: `../checklist/evidence/auto/P3_CL-20_1.png`

### CL-21 – Dấu * trên trường mà form bắt buộc nhập

- Màn hình: Hồ sơ
- Căn cứ: FR-22.1 (README.md:252)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:435`

**Expected (chép từ checklist)**

> Với từng trường Họ Tên, Số điện thoại, Địa chỉ: để trống rồi bấm Cập nhật. Trường nào khiến form bị chặn thì nhãn phải có '*'; trường không bắt buộc thì không có '*'. Fail nếu một trường bị chặn khi trống mà nhãn không có '*'.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng"
- P2 (auto): Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng"
- P3 (auto): Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng"

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-21_1.png`
- P2: `../checklist/evidence/auto/P2_CL-21_1.png`
- P3: `../checklist/evidence/auto/P3_CL-21_1.png`
