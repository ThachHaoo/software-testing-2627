# BUG-58

- **ID:** BUG-58
- **Nhóm dữ kiện:** G-01 (CL-10, CL-12)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-10 – Thứ tự Tab theo vị trí hiển thị (trên→dưới, trái→phải)

- Màn hình: Đăng nhập
- Căn cứ: FR-21.5 (README.md:248)
- Nền tảng Failed: P1, P2

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:230`

**Expected (chép từ checklist)**

> Từ đầu trang bấm Tab liên tục: focus đi qua mọi control tương tác được theo vị trí hiển thị — từ trên xuống dưới; cùng một hàng thì từ trái sang phải. Fail nếu focus nhảy tới control nằm phía trên control trước đó (cùng hàng: nằm bên trái), hoặc bỏ qua một control tương tác được.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: nhảy ngược: 'Sign In'(449,425) → 'EShop'(16,16) · chuỗi Tab: button'Sign In'@(449,425) → a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) → input'text'@(449,241) → input'text'@(449,331) → a'Quên mật khẩu?'@(729,389) → a'Đăng ký ngay'@(659,481)
- P2 (auto): Lỗi: Error: nhảy ngược: 'Sign In'(449,425) → 'EShop'(16,16) · chuỗi Tab: button'Sign In'@(449,425) → a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) → input'text'@(449,241) → input'text'@(449,331) → a'Quên mật khẩu?'@(729,390) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482)

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-10_1.png`
- P2: `../checklist/evidence/auto/P2_CL-10_1.png`

### CL-12 – Thứ tự Tab ở bước 2 theo vị trí hiển thị (trên→dưới, trái→phải)

- Màn hình: Quên mật khẩu (bước 2)
- Căn cứ: FR-21.5 (README.md:248)
- Nền tảng Failed: P1, P2

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:390`

**Expected (chép từ checklist)**

> Từ đầu trang bấm Tab liên tục: focus đi qua mọi control tương tác được theo vị trí hiển thị — từ trên xuống dưới; cùng một hàng thì từ trái sang phải. Fail nếu focus nhảy tới control nằm phía trên control trước đó (cùng hàng: nằm bên trái), hoặc bỏ qua một control tương tác được.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: bỏ qua: a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) · chuỗi Tab: input'text'@(449,301) → input'password'@(449,391) → button'Đặt lại mật khẩu'@(449,449) → button'← Quay lại'@(449,505)
- P2 (auto): Lỗi: Error: bỏ qua: a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) · chuỗi Tab: input'text'@(449,301) → input'password'@(449,391) → button'Đặt lại mật khẩu'@(449,449) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505)

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-12_1.png`
- P2: `../checklist/evidence/auto/P2_CL-12_1.png`
