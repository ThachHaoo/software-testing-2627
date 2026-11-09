# BUG-62

- **ID:** BUG-62
- **Nhóm dữ kiện:** G-05 (CL-17, CL-66)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-17 – Ô Email dùng type="email"

- Màn hình: Đăng nhập, Quên mật khẩu (bước 1)
- Căn cứ: FR-02.4 (README.md:44); FR-22.2 (README.md:253)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #4 (#4 phủ /login; /forgot-password bước 1 chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:89`

**Expected (chép từ checklist)**

> DevTools: ô Email trên /login và bước 1 /forgot-password có type="email". Fail nếu type khác "email".

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text"
- P2 (auto): Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text"
- P3 (auto): Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text"

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-17_1.png`
- P2: `../checklist/evidence/auto/P2_CL-17_1.png`
- P3: `../checklist/evidence/auto/P3_CL-17_1.png`

### CL-66 – Email sai định dạng bị chặn trước khi gửi

- Màn hình: Đăng nhập, Quên mật khẩu (bước 1)
- Căn cứ: FR-02.4 (README.md:44); FR-22.2 (README.md:253)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #4 (#4 (không kiểm tra định dạng) phủ /login; /forgot-password chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:99`

**Expected (chép từ checklist)**

> Nhập 'abc' vào ô Email rồi submit → form bị chặn, có thông báo validate, DevTools Network không có request gửi đi. Fail nếu form gửi request.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true
- P2 (auto): Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true
- P3 (auto): Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-66_1.png`
- P2: `../checklist/evidence/auto/P2_CL-66_1.png`
- P3: `../checklist/evidence/auto/P3_CL-66_1.png`
