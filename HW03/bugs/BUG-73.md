# BUG-73

- **ID:** BUG-73
- **Nhóm dữ kiện:** G-16 (CL-40)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-40 – Navbar highlight trang đang chọn

- Màn hình: Navbar
- Căn cứ: FR-23.1 (README.md:260)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #169 (#169 là trang Giỏ; /profile chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:583`

**Expected (chép từ checklist)**

> Ở /profile, link tên người dùng (trỏ tới /profile) có kiểu khác hẳn các link còn lại trên navbar (màu/gạch chân/nền), và kiểu đó mất khi rời /profile. Fail nếu link không khác kiểu hoặc không đổi theo trang hiện tại.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: kiểu link không đổi theo trang hiện tại · link hồ sơ ở /profile {"color":"rgb(253, 224, 71)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}; ở / {"color":"rgb(253, 224, 71)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}; link Giỏ hàng {"color":"rgb(255, 255, 255)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}
- P2 (auto): Lỗi: Error: kiểu link không đổi theo trang hiện tại · link hồ sơ ở /profile {"color":"rgb(253, 224, 71)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}; ở / {"color":"rgb(253, 224, 71)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}; link Giỏ hàng {"color":"rgb(255, 255, 255)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}
- P3 (auto): Lỗi: Error: kiểu link không đổi theo trang hiện tại · link hồ sơ ở /profile {"color":"rgb(253, 224, 71)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}; ở / {"color":"rgb(253, 224, 71)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}; link Giỏ hàng {"color":"rgb(255, 255, 255)","background-color":"rgba(0, 0, 0, 0)","text-decoration-line":"none","font-weight":"400","border-bottom-width":"0px"}

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-40_1.png`
- P2: `../checklist/evidence/auto/P2_CL-40_1.png`
- P3: `../checklist/evidence/auto/P3_CL-40_1.png`
