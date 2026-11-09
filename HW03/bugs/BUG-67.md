# BUG-67

- **ID:** BUG-67
- **Nhóm dữ kiện:** G-10 (CL-26)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-26 – Có ô 'Xác nhận mật khẩu mới'

- Màn hình: Quên mật khẩu (bước 2)
- Căn cứ: FR-03.5 (README.md:57)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #30 (#30 là form Đăng ký; Quên MK bước 2 chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:299`

**Expected (chép từ checklist)**

> Bước 2 có đủ 3 ô: OTP, Mật khẩu mới, Xác nhận mật khẩu mới. Fail nếu thiếu ô xác nhận.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"]
- P2 (auto): Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"]
- P3 (auto): Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"]

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-26_1.png`
- P2: `../checklist/evidence/auto/P2_CL-26_1.png`
- P3: `../checklist/evidence/auto/P3_CL-26_1.png`
