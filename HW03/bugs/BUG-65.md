# BUG-65

- **ID:** BUG-65
- **Nhóm dữ kiện:** G-08 (CL-24)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-24 – Có chỉ báo bước (Step Indicator)

- Màn hình: Quên mật khẩu
- Căn cứ: FR-03.3 (README.md:52); FR-22.5 (README.md:256)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): auto: tìm chữ 'Bước k / 2'; không thấy → SV xác nhận không có chỉ báo tương đương
- Test tự động: `HW03/tests/C2.spec.ts:279`

**Expected (chép từ checklist)**

> Bước 1 hiển thị 'Bước 1 / 2' (hoặc chỉ báo tương đương thấy rõ bước hiện tại và tổng số bước); bước 2 hiển thị 'Bước 2 / 2'. Fail nếu một bước không có chỉ báo.

**Actual (chép notes / số đo)**

- P1 (tay): Không có chỉ báo bước
- P2 (tay): Không có chỉ báo bước
- P3 (tay): Không có chỉ báo bước

**Ảnh**

- P1: `../checklist/evidence/P1_chrome/P1_CL-24_1.png`
- P2: `../checklist/evidence/P2_firefox/P2_CL-24_1.png`
- P3: `../checklist/evidence/P3_android/P3_CL-24_1.png`
