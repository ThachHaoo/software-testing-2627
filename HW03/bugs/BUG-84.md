# BUG-84

- **ID:** BUG-84
- **Nhóm dữ kiện:** G-27 (SV-04)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### SV-04 – Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio)

- Màn hình: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- Căn cứ: WCAG 2.2 SC 1.4.3 (Contrast Minimum)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): auto: tỉ lệ tương phản chữ/nền tính từ màu CSS; placeholder + Lighthouse → SV
- Test tự động: `HW03/tests/C2.spec.ts:891`

**Expected (chép từ checklist)**

> Kiểm tra bằng công cụ DevTools Accessibility / Lighthouse: tỉ lệ tương phản màu sắc của chữ (văn bản, label, placeholder, text trên button) so với màu nền đạt tối thiểu 4.5:1 (đối với chữ thường). Fail nếu tỉ lệ tương phản < 4.5:1 khiến chữ mờ khó đọc.

**Actual (chép notes / số đo)**

- P1 (tay): Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không
- P2 (tay): Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không
- P3 (tay): Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không

**Ảnh**

- P1: `../checklist/evidence/P1_chrome/P1_SV-04_1.png`, `../checklist/evidence/P1_chrome/P1_SV-04_2.png`, `../checklist/evidence/P1_chrome/P1_SV-04_3.png`, `../checklist/evidence/P1_chrome/P1_SV-04_4.png`
- P2: `../checklist/evidence/P2_firefox/P2_SV-04_1.png`, `../checklist/evidence/P2_firefox/P2_SV-04_2.png`, `../checklist/evidence/P2_firefox/P2_SV-04_3.png`, `../checklist/evidence/P2_firefox/P2_SV-04_4.png`
- P3: `../checklist/evidence/P3_android/P3_SV-04_1.png`, `../checklist/evidence/P3_android/P3_SV-04_2.png`, `../checklist/evidence/P3_android/P3_SV-04_3.png`, `../checklist/evidence/P3_android/P3_SV-04_4.png`
