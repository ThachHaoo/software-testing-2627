# BUG-77

- **ID:** BUG-77
- **Nhóm dữ kiện:** G-20 (CL-50)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-50 – URL không tồn tại hiển thị trang 404 có lối về

- Màn hình: Tất cả màn C2
- Căn cứ: Nielsen #9; Nielsen #3
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:266`

**Expected (chép từ checklist)**

> Mở /profil (gõ sai) → trang báo không tìm thấy, có link về trang chủ. Fail nếu trang trắng (chỉ còn header/footer) không có thông báo.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: không có thông báo không tìm thấy · Lỗi: Error: không có link về trang chủ trong trang · nội dung main: ""; link về '/': 0
- P2 (auto): Lỗi: Error: không có thông báo không tìm thấy · Lỗi: Error: không có link về trang chủ trong trang · nội dung main: ""; link về '/': 0
- P3 (auto): Lỗi: Error: không có thông báo không tìm thấy · Lỗi: Error: không có link về trang chủ trong trang · nội dung main: ""; link về '/': 0

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-50_1.png`, `../checklist/evidence/auto/P1_CL-50_2.png`
- P2: `../checklist/evidence/auto/P2_CL-50_1.png`, `../checklist/evidence/auto/P2_CL-50_2.png`
- P3: `../checklist/evidence/auto/P3_CL-50_1.png`, `../checklist/evidence/auto/P3_CL-50_2.png`
