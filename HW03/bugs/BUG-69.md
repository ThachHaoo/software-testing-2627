# BUG-69

- **ID:** BUG-69
- **Nhóm dữ kiện:** G-12 (CL-28)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-28 – Mã OTP hiển thị có đúng 6 chữ số

- Màn hình: Quên mật khẩu (bước 2)
- Căn cứ: FR-03.2 (README.md:51)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:321`

**Expected (chép từ checklist)**

> Sau khi gửi email ở bước 1, mã OTP hiển thị trên màn hình có đúng 6 chữ số. Fail nếu mã có số chữ số khác 6.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: mã có 4 chữ số · mã hiển thị: 1846
- P2 (auto): Lỗi: Error: mã có 4 chữ số · mã hiển thị: 9894
- P3 (auto): Lỗi: Error: mã có 4 chữ số · mã hiển thị: 8382

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-28_1.png`, `../checklist/evidence/auto/P1_CL-28_2.png`
- P2: `../checklist/evidence/auto/P2_CL-28_1.png`, `../checklist/evidence/auto/P2_CL-28_2.png`
- P3: `../checklist/evidence/auto/P3_CL-28_1.png`, `../checklist/evidence/auto/P3_CL-28_2.png`
