# BUG-60

- **ID:** BUG-60
- **Nhóm dữ kiện:** G-03 (CL-14)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-14 – Khai báo ngôn ngữ trang là tiếng Việt

- Màn hình: Tất cả màn C2
- Căn cứ: WCAG 2.2 SC 3.1.1 (Language of Page)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:82`

**Expected (chép từ checklist)**

> Thẻ <html> có lang='vi'. Fail nếu lang khác 'vi' hoặc không có.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: lang = "en" · <html lang="en">
- P2 (auto): Lỗi: Error: lang = "en" · <html lang="en">
- P3 (auto): Lỗi: Error: lang = "en" · <html lang="en">

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-14_1.png`
- P2: `../checklist/evidence/auto/P2_CL-14_1.png`
- P3: `../checklist/evidence/auto/P3_CL-14_1.png`
