# BUG-80

- **ID:** BUG-80
- **Nhóm dữ kiện:** G-23 (CL-09)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-09 – Ngày đặt hiển thị nhất quán theo định dạng Việt Nam

- Màn hình: Lịch sử đơn
- Căn cứ: Nielsen #4 (nhất quán và chuẩn); SRS im lặng → giả định GA1
- Nền tảng Failed: P2, P3

**Môi trường**

- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Có ≥ 1 đơn.
- Cách kiểm (checklist): auto: định dạng trên từng nền tảng; so giữa P1/P2/P3 khi gộp
- Test tự động: `HW03/tests/C2.spec.ts:685`

**Expected (chép từ checklist)**

> Ngày đặt hiển thị dạng dd/mm/yyyy và giống nhau trên P1, P2, P3. Fail nếu định dạng khác (mm/dd/yyyy, yyyy-mm-dd) hoặc khác nhau giữa các nền tảng.

**Actual (chép notes / số đo)**

- P2 (tay): Sử dụng định dạng mm/dd/yyyy thay vì dd/mm/yyyy của người Việt
- P3 (tay): Sử dụng định dạng mm/dd/yyyy thay vì dd/mm/yyyy của người Việt

**Ảnh**

- P2: `../checklist/evidence/P2_firefox/P2_CL-09_1.png`
- P3: `../checklist/evidence/P3_android/P3_CL-09_1.png`
