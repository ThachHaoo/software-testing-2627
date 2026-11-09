# BUG-70

- **ID:** BUG-70
- **Nhóm dữ kiện:** G-13 (CL-29)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-29 – Mật khẩu mới hợp lệ theo FR-01 được chấp nhận

- Màn hình: Quên mật khẩu (bước 2)
- Căn cứ: FR-03.6 (README.md:58, 34)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #17 (#17 cùng thông báo "Mật khẩu quá yếu!" ở Đăng ký; Quên MK bước 2 chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Dùng tài khoản test@eshop.com; restart backend sau khi kiểm để khôi phục mật khẩu Test1234!.
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:334`

**Expected (chép từ checklist)**

> Với OTP đúng, Mật khẩu mới 'Abcdef1!' (8 ký tự, có hoa, thường, số, '!') → đổi thành công; đăng nhập lại bằng mật khẩu mới được. Fail nếu bị báo mật khẩu yếu.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]
- P2 (auto): Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]
- P3 (auto): Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-29_1.png`
- P2: `../checklist/evidence/auto/P2_CL-29_1.png`
- P3: `../checklist/evidence/auto/P3_CL-29_1.png`
