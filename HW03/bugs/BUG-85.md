# BUG-85

- **ID:** BUG-85
- **Nhóm dữ kiện:** G-28 (SV-03)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### SV-03 – Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại

- Màn hình: Đăng nhập, Quên mật khẩu B2, Hồ sơ
- Căn cứ: Slide "Checklist - input-field validation" (Golden Rule: "On error, return focus to the offending field"); Shneiderman #5 (Xử lý lỗi đơn giản)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:868`

**Expected (chép từ checklist)**

> Nhập dữ liệu sai quy tắc (ví dụ: SĐT sai định dạng ở Hồ sơ hoặc Mật khẩu mới không đủ điều kiện ở Quên mật khẩu B2) rồi bấm submit: sau khi thông báo lỗi xuất hiện, con trỏ gõ phím (cursor) phải tự động quay lại focus ở đúng ô bị lỗi đó. Fail nếu con trỏ nhảy mất focus hoặc không quay lại ô nhập bị lỗi.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false
- P2 (auto): Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false
- P3 (auto): Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false

**Ảnh**

- P1: `../checklist/evidence/auto/P1_SV-03_1.png`
- P2: `../checklist/evidence/auto/P2_SV-03_1.png`
- P3: `../checklist/evidence/auto/P3_SV-03_1.png`
