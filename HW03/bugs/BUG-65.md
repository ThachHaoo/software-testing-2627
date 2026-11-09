# BUG-65

- **ID:** BUG-65
- **Nhóm dữ kiện:** G-08 (CL-38)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-38 – Nhãn gắn với ô nhập (bấm nhãn → focus ô)

- Màn hình: Đăng nhập, Hồ sơ
- Căn cứ: Checklist Text box – 'Correct label'; WCAG 2.2 SC 1.3.1
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:239`

**Expected (chép từ checklist)**

> Bấm vào chữ nhãn (vd 'Mật khẩu', 'Họ Tên') → con trỏ nhảy vào ô tương ứng. Fail nếu bấm nhãn không có tác dụng.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: /login: bấm nhãn "Username" không focus ô · Lỗi: Error: /login: bấm nhãn "Mật khẩu" không focus ô · Lỗi: Error: /profile: bấm nhãn "Họ Tên" không focus ô · Lỗi: Error: /profile: bấm nhãn "Số điện thoại" không focus ô · Lỗi: Error: /profile: bấm nhãn "Địa chỉ giao hàng" không focus ô · /login "Username": không focus · /login "Mật khẩu": không focus · /profile "Họ Tên": không focus · /profile "Số điện thoại": không focus · /profile "Địa chỉ giao hàng": không focus
- P2 (auto): Lỗi: Error: /login: bấm nhãn "Username" không focus ô · Lỗi: Error: /login: bấm nhãn "Mật khẩu" không focus ô · Lỗi: Error: /profile: bấm nhãn "Họ Tên" không focus ô · Lỗi: Error: /profile: bấm nhãn "Số điện thoại" không focus ô · Lỗi: Error: /profile: bấm nhãn "Địa chỉ giao hàng" không focus ô · /login "Username": không focus · /login "Mật khẩu": không focus · /profile "Họ Tên": không focus · /profile "Số điện thoại": không focus · /profile "Địa chỉ giao hàng": không focus
- P3 (auto): Lỗi: Error: /login: bấm nhãn "Username" không focus ô · Lỗi: Error: /login: bấm nhãn "Mật khẩu" không focus ô · Lỗi: Error: /profile: bấm nhãn "Họ Tên" không focus ô · Lỗi: Error: /profile: bấm nhãn "Số điện thoại" không focus ô · Lỗi: Error: /profile: bấm nhãn "Địa chỉ giao hàng" không focus ô · /login "Username": không focus · /login "Mật khẩu": không focus · /profile "Họ Tên": không focus · /profile "Số điện thoại": không focus · /profile "Địa chỉ giao hàng": không focus

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-38_1.png`
- P2: `../checklist/evidence/auto/P2_CL-38_1.png`
- P3: `../checklist/evidence/auto/P3_CL-38_1.png`
