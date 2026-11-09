# BUG-85

- **ID:** BUG-85
- **Nhóm dữ kiện:** G-28 (SV-05)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### SV-05 – Kích thước vùng tương tác của con trỏ (Target Size) đối với các nút và link

- Màn hình: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- Căn cứ: WCAG 2.2 SC 2.5.8 (Target Size Minimum - 24x24px)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:900`

**Expected (chép từ checklist)**

> Dùng thước đo DevTools kiểm tra chiều cao và chiều rộng vùng bấm của các nút ('Sign In', 'Lấy mã OTP', 'Cập nhật') và các liên kết ('Quên mật khẩu?', 'Đăng ký ngay'): vùng bấm nhận con trỏ (chuột hoặc ngón tay) phải đạt kích thước tối thiểu 24x24 px. Fail nếu có nút/link kích thước < 24x24 px.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 382×40 · Quên mật khẩu?: 102×19 · Đăng ký ngay: 85×19 · Lấy mã OTP: 382×40 · Cập nhật: 271×40
- P2 (auto): Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 382×40 · Quên mật khẩu?: 102×19 · Đăng ký ngay: 85×19 · Lấy mã OTP: 382×40 · Cập nhật: 271×40
- P3 (auto): Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 295×40 · Quên mật khẩu?: 100×16 · Đăng ký ngay: 82×16 · Lấy mã OTP: 295×40 · Cập nhật: 311×40

**Ảnh**

- P1: `../checklist/evidence/auto/P1_SV-05_1.png`
- P2: `../checklist/evidence/auto/P2_SV-05_1.png`
- P3: `../checklist/evidence/auto/P3_SV-05_1.png`
