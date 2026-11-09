# BUG-59

- **ID:** BUG-59
- **Nhóm dữ kiện:** G-02 (CL-13)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-13 – Tiêu đề tab trình duyệt mô tả trang

- Màn hình: Tất cả màn C2
- Căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống); WCAG 2.2 SC 2.4.2
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:71`

**Expected (chép từ checklist)**

> Tiêu đề tab (document.title) chứa tên ứng dụng hoặc tên trang (vd 'Đăng nhập – EShop') và khác nhau giữa /login, /forgot-password, /profile. Fail nếu không chứa tên ứng dụng/tên trang hoặc giống nhau ở cả 3 trang.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"]
- P2 (auto): Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"]
- P3 (auto): Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"]

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-13_1.png`
- P2: `../checklist/evidence/auto/P2_CL-13_1.png`
- P3: `../checklist/evidence/auto/P3_CL-13_1.png`
