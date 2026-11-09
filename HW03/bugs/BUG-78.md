# BUG-78

- **ID:** BUG-78
- **Nhóm dữ kiện:** G-21 (CL-53, SV-06)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-53 – Có chỉ báo đang xử lý và chống gửi trùng

- Màn hình: Đăng nhập
- Căn cứ: Norman – Feedback; Shneiderman #3 (phản hồi đầy đủ)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): P3: throttling qua chrome://inspect.
- Cách kiểm (checklist): auto (P1, CDP Slow 3G): nút disabled/đổi chữ/aria-busy + số request; chỉ báo khác → SV; P2 chạy tay
- Test tự động: `HW03/tests/C2.spec.ts:823`

**Expected (chép từ checklist)**

> DevTools Network throttling 'Slow 3G': bấm Đăng nhập → trong lúc chờ, nút bị vô hiệu hoá hoặc có chỉ báo đang tải; bấm thêm 2 lần chỉ phát sinh 1 request /api/login. Fail nếu không có chỉ báo hoặc phát sinh nhiều request.

**Actual (chép notes / số đo)**

- P1 (tay): Không có đang xử lý và chống gửi trùng
- P2 (tay): Không có đang xử lý và chống gửi trùng
- P3 (tay): Không có đang xử lý và chống gửi trùng

**Ảnh**

- P1: `../checklist/evidence/P1_chrome/P1_CL-53_1.png`
- P2: `../checklist/evidence/P2_firefox/P2_CL-53_1.png`
- P3: `../checklist/evidence/P3_android/P3_CL-53_1.png`

### SV-06 – Chống gửi trùng dữ liệu (Debounce/Disable) khi nhấp đúp/nhấp liên tiếp vào nút submit ở điều kiện mạng bình thường

- Màn hình: Quên mật khẩu B1 / B2, Hồ sơ
- Căn cứ: Slide "Double-submit on double-click"; Nielsen #5 (Phòng ngừa lỗi)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:914`

**Expected (chép từ checklist)**

> Ở điều kiện mạng bình thường (không bật throttling), nhấp chuột thật nhanh (double-click) vào nút 'Lấy mã OTP', 'Đặt lại mật khẩu' hoặc 'Cập nhật': hệ thống lập tức khóa nút hoặc debounce request sao cho chỉ có đúng 1 request API được gửi đi. Fail nếu gửi từ 2 request trở lên hoặc hiển thị nhiều thông báo trùng lặp.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: Error: Đặt lại mật khẩu: 0 request, 2 hộp thoại · Lỗi: Error: Cập nhật: 0 request PUT, 2 hộp thoại · Lấy mã OTP: 2 request · Đặt lại mật khẩu: 0 request, 2 hộp thoại · Cập nhật: 0 request PUT, 2 hộp thoại
- P2 (auto): Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: Error: Đặt lại mật khẩu: 0 request, 2 hộp thoại · Lỗi: Error: Cập nhật: 0 request PUT, 2 hộp thoại · Lấy mã OTP: 2 request · Đặt lại mật khẩu: 0 request, 2 hộp thoại · Cập nhật: 0 request PUT, 2 hộp thoại
- P3 (auto): Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: TimeoutError: locator.dblclick: Timeout 30000ms exceeded. · Lấy mã OTP: 2 request

**Ảnh**

- P1: `../checklist/evidence/auto/P1_SV-06_1.png`
- P2: `../checklist/evidence/auto/P2_SV-06_1.png`
- P3: `../checklist/evidence/auto/P3_SV-06_1.png`
