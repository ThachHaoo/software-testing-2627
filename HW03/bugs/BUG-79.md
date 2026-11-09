# BUG-79

- **ID:** BUG-79
- **Nhóm dữ kiện:** G-22 (CL-63)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-63 – Có trạng thái đang tải khi lấy lịch sử đơn

- Màn hình: Lịch sử đơn
- Căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Có ≥ 1 đơn. P3: throttling qua chrome://inspect.
- Cách kiểm (checklist): auto (P1, CDP Slow 3G): empty state hiện trước khi dữ liệu về / có chỉ báo tải; P2 chạy tay
- Test tự động: `HW03/tests/C2.spec.ts:772`

**Expected (chép từ checklist)**

> Network throttling 'Slow 3G', tải lại /profile → trong lúc chờ có chỉ báo đang tải; không hiện 'chưa có đơn hàng' trước khi dữ liệu về. Fail nếu hiện empty state rồi mới hiện bảng.

**Actual (chép notes / số đo)**

- P1 (tay): Không có trạng thái đang tải
- P2 (tay): Không có trạng thái đang tải, trang tải xong là tất cả dữ liệu cũng xong hết (không giống Chrome khi tải từng phần)
- P3 (tay): Không có trạng thái đang tải, trang tải xong là tất cả dữ liệu cũng xong hết (không giống Chrome khi tải từng phần)

**Ảnh**

- P1: `../checklist/evidence/P1_chrome/P1_CL-63_1.png`, `../checklist/evidence/P1_chrome/P1_CL-63_2.png`
- P2: `../checklist/evidence/P2_firefox/P2_CL-63_1.png`
- P3: `../checklist/evidence/P3_android/P3_CL-63_1.png`, `../checklist/evidence/P3_android/P3_CL-63_2.png`
