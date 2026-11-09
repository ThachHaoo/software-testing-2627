# BUG-76

- **ID:** BUG-76
- **Nhóm dữ kiện:** G-19 (CL-49)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-49 – /profile khi chưa đăng nhập dẫn được tới Đăng nhập

- Màn hình: Hồ sơ
- Căn cứ: Nielsen #3 (lối thoát); Nielsen #9
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:256`

**Expected (chép từ checklist)**

> Chưa đăng nhập, mở /profile → hoặc tự chuyển tới /login, hoặc thông báo có link/nút tới Đăng nhập (1 lần bấm). Fail nếu chỉ có chữ, không có đường tới Đăng nhập ngoài navbar.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0
- P2 (auto): Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0
- P3 (auto): Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-49_1.png`, `../checklist/evidence/auto/P1_CL-49_2.png`
- P2: `../checklist/evidence/auto/P2_CL-49_1.png`, `../checklist/evidence/auto/P2_CL-49_2.png`
- P3: `../checklist/evidence/auto/P3_CL-49_1.png`, `../checklist/evidence/auto/P3_CL-49_2.png`
