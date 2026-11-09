# BUG-75

- **ID:** BUG-75
- **Nhóm dữ kiện:** G-18 (CL-56)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-56 – Đổi Họ Tên cập nhật ngay trên navbar

- Màn hình: Hồ sơ, Navbar
- Căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống); Shneiderman #1
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Khôi phục 'Test User' sau khi kiểm.
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:562`

**Expected (chép từ checklist)**

> Đổi Họ Tên thành 'Test Đổi' → Cập nhật → navbar hiển thị 'Test Đổi' mà không cần tải lại trang. Fail nếu navbar vẫn tên cũ cho tới khi F5.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát"
- P2 (auto): Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát"
- P3 (auto): Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát"

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-56_1.png`
- P2: `../checklist/evidence/auto/P2_CL-56_1.png`
- P3: `../checklist/evidence/auto/P3_CL-56_1.png`
