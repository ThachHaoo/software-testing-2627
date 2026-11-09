# BUG-73

- **ID:** BUG-73
- **Nhóm dữ kiện:** G-16 (CL-37)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-37 – Cập nhật hồ sơ được lưu bền

- Màn hình: Hồ sơ
- Căn cứ: FR-04.1 (README.md:64)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #111, #123 (SV xem: trường quay về giá trị cũ sau F5, có thể do #111 chặn lưu hoặc #123)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Khôi phục giá trị cũ sau khi kiểm.
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:527`

**Expected (chép từ checklist)**

> Đổi Họ Tên, SĐT hợp lệ, Địa chỉ → Cập nhật → tải lại trang (F5) → 3 trường hiển thị giá trị mới. Fail nếu ≥ 1 trường quay về giá trị cũ.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""]
- P2 (auto): Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""]
- P3 (auto): Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""]

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-37_1.png`
- P2: `../checklist/evidence/auto/P2_CL-37_1.png`
- P3: `../checklist/evidence/auto/P3_CL-37_1.png`
