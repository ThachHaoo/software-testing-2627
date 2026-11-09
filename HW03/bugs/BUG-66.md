# BUG-66

- **ID:** BUG-66
- **Nhóm dữ kiện:** G-09 (CL-25)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-25 – Có nút 'Quay lại đăng nhập'

- Màn hình: Quên mật khẩu (bước 1)
- Căn cứ: FR-03.4 (README.md:53)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:290`

**Expected (chép từ checklist)**

> Bước 1 có nút/link nhãn 'Quay lại đăng nhập'; bấm → về /login. Fail nếu không có, nhãn khác nghĩa, hoặc không về /login.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: bước 1 không có "Quay lại đăng nhập" · bước 1 có "Quay lại đăng nhập": false
- P2 (auto): Lỗi: Error: bước 1 không có "Quay lại đăng nhập" · bước 1 có "Quay lại đăng nhập": false
- P3 (auto): Lỗi: Error: bước 1 không có "Quay lại đăng nhập" · bước 1 có "Quay lại đăng nhập": false

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-25_1.png`
- P2: `../checklist/evidence/auto/P2_CL-25_1.png`
- P3: `../checklist/evidence/auto/P3_CL-25_1.png`
