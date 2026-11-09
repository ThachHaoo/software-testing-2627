# BUG-84

- **ID:** BUG-84
- **Nhóm dữ kiện:** G-27 (SV-02)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### SV-02 – Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu

- Màn hình: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- Căn cứ: Shneiderman #8 (Giảm tải trí nhớ ngắn hạn); Nielsen #7 (Linh hoạt và hiệu quả); Slide "Checklist - Text Box"
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Trình duyệt đã lưu thông tin đăng nhập/tài khoản trước đó.
- Cách kiểm (checklist): auto (P1): dán bằng Ctrl+V vào ô Email; Autofill + P2 → chạy tay
- Test tự động: `HW03/tests/C2.spec.ts:854`

**Expected (chép từ checklist)**

> Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit. Fail nếu bất kỳ vế nào (dán hoặc autofill) bị hệ thống ngăn chặn/làm sai lệch dữ liệu.

**Actual (chép notes / số đo)**

- P1 (tay): Tất cả đều có thể Paste vào, nhưng Autofill chỉ có ở Forgot Password.
- P2 (tay): Tất cả đều có thể Paste vào, nhưng không thể Autofill
- P3 (tay): Tất cả đều có thể Paste vào, nhưng không thể Autofill

**Ảnh**

- P1: `../checklist/evidence/P1_chrome/P1_SV-02_1.png`, `../checklist/evidence/P1_chrome/P1_SV-02_2.png`, `../checklist/evidence/P1_chrome/P1_SV-02_3.png`, `../checklist/evidence/P1_chrome/P1_SV-02_4.png`
- P2: `../checklist/evidence/P2_firefox/P2_SV-02_1.png`, `../checklist/evidence/P2_firefox/P2_SV-02_2.png`, `../checklist/evidence/P2_firefox/P2_SV-02_3.png`, `../checklist/evidence/P2_firefox/P2_SV-02_4.png`
- P3: `../checklist/evidence/P3_android/P3_SV-02_1.png`, `../checklist/evidence/P3_android/P3_SV-02_2.png`, `../checklist/evidence/P3_android/P3_SV-02_3.png`, `../checklist/evidence/P3_android/P3_SV-02_4.png`
