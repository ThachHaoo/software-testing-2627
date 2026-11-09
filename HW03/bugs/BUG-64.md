# BUG-64

- **ID:** BUG-64
- **Nhóm dữ kiện:** G-07 (CL-23)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-23 – Thông báo lỗi validate hiển thị trong trang, phía trên nút submit

- Màn hình: Quên mật khẩu, Hồ sơ
- Căn cứ: FR-22.4 (README.md:255); giả định GA3
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:453`

**Expected (chép từ checklist)**

> Gây lỗi: mật khẩu mới yếu (bước 2), SĐT sai định dạng (Hồ sơ). Thông báo lỗi xuất hiện trong trang, phía trên nút submit của form đó. Fail nếu lỗi hiện dưới nút hoặc chỉ hiện ở hộp thoại trình duyệt (alert) không gắn với vị trí nào trong form.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"]
- P2 (auto): Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Protocol error (Browser.removeBrowserContext): this._windows[aWindow.__SSi] is undefined · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"]
- P3 (auto): Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"]

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-23_1.png`
- P2: `../checklist/evidence/auto/P2_CL-23_1.png`
- P3: `../checklist/evidence/auto/P3_CL-23_1.png`
