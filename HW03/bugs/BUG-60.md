# BUG-60

- **ID:** BUG-60
- **Nhóm dữ kiện:** G-03 (CL-02)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-02 – Mỗi trang có đúng 1 thẻ <h1>

- Màn hình: Đăng nhập, Quên mật khẩu, Hồ sơ
- Căn cứ: FR-21.4 (README.md:247)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): P3: mở DevTools qua chrome://inspect (adb).
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:52`

**Expected (chép từ checklist)**

> Trên mỗi trang /login, /forgot-password, /profile, lệnh DevTools `document.querySelectorAll('h1').length` trả về đúng 1. Fail nếu một trang trả 0 hoặc ≥ 2.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1
- P2 (auto): Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1
- P3 (auto): Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-02_1.png`
- P2: `../checklist/evidence/auto/P2_CL-02_1.png`
- P3: `../checklist/evidence/auto/P3_CL-02_1.png`
