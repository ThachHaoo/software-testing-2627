# BUG-70

- **ID:** BUG-70
- **Nhóm dữ kiện:** G-13 (CL-04, CL-06)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-04 – Nút hành động tích cực màu xanh dương

- Màn hình: Tất cả màn C2
- Căn cứ: FR-21.2 (README.md:245)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #160 (#160 là nút Mobile; nút C2 trên Web chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:739`

**Expected (chép từ checklist)**

> Nút 'Đăng nhập/Sign In', 'Lấy mã OTP', 'Đặt lại mật khẩu', 'Cập nhật' có nền xanh dương (họ blue). Fail nếu ≥ 1 nút tích cực có màu khác (xanh lá, xám…).

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: nút Đặt lại mật khẩu màu rgb(22, 163, 74) · {"Đăng nhập":"rgb(37, 99, 235)","Lấy mã OTP":"rgb(37, 99, 235)","Đặt lại mật khẩu":"rgb(22, 163, 74)","Cập nhật":"rgb(37, 99, 235)"} (dải hue 190–250°)
- P2 (auto): Lỗi: Error: nút Đặt lại mật khẩu màu rgb(22, 163, 74) · {"Đăng nhập":"rgb(37, 99, 235)","Lấy mã OTP":"rgb(37, 99, 235)","Đặt lại mật khẩu":"rgb(22, 163, 74)","Cập nhật":"rgb(37, 99, 235)"} (dải hue 190–250°)
- P3 (auto): Lỗi: Error: nút Đặt lại mật khẩu màu rgb(22, 163, 74) · {"Đăng nhập":"rgb(37, 99, 235)","Lấy mã OTP":"rgb(37, 99, 235)","Đặt lại mật khẩu":"rgb(22, 163, 74)","Cập nhật":"rgb(37, 99, 235)"} (dải hue 190–250°)

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-04_1.png`
- P2: `../checklist/evidence/auto/P2_CL-04_1.png`
- P3: `../checklist/evidence/auto/P3_CL-04_1.png`

### CL-06 – Nút chính và nút phụ phân biệt được bằng hình thức

- Màn hình: Quên mật khẩu (bước 2)
- Căn cứ: Shneiderman #1 (nhất quán); checklist Button – 'colour signals intent'
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): auto: Fail khi hai nút trùng cả màu nền, kích thước, viền; khác nhau → SV xác nhận 'khác nhau rõ'
- Test tự động: `HW03/tests/C2.spec.ts:399`

**Expected (chép từ checklist)**

> Nút 'Đặt lại mật khẩu' (chính) và nút quay lại (phụ) khác nhau rõ về màu hoặc kiểu (viền/nền). Fail nếu hai nút cùng màu nền, cùng kích thước, cùng kiểu.

**Actual (chép notes / số đo)**

- P1 (tay): Nút chính và nút phụ giống nhau
- P2 (tay): Nút chính và nút phụ giống nhau
- P3 (tay): Nút chính và nút phụ giống nhau

**Ảnh**

- P1: `../checklist/evidence/P1_chrome/P1_CL-06_1.png`
- P2: `../checklist/evidence/P2_firefox/P2_CL-06_1.png`
- P3: `../checklist/evidence/P3_android/P3_CL-06_1.png`
