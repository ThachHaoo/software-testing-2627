# BUG-23

- **ID:** BUG-23
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart và / — navbar (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-92_failed.png`
- TC-FR07-92: `HW02/B_FR07/evidence/TC-FR07-92_failed.png`, `HW02/B_FR07/evidence/TC-FR07-92_ui-cart.png`, `HW02/B_FR07/evidence/TC-FR07-92_ui-home.png`

## TC liên quan

- Fail (1): TC-FR07-92
- Nhóm dữ kiện: G9 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-23.1:** (GUI, B16) Thanh điều hướng (Navbar) phải highlight trang đang được chọn — xét trên trang Giỏ hàng.
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-92): `ở /cart: [{"href":"/cart","text":"Giỏ hàng","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/login","text":"Đăng nhập","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/register","text":"Đăng ký","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"}]; ở trang chủ: [{"href":"/cart","text":"Giỏ hàng","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/login","text":"Đăng nhập","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/register","text":… (rút gọn)`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/App.jsx` dòng 21–24

  ```jsx
    21        <Link to="/" className="text-2xl font-bold">EShop</Link>
    22        <nav className="flex gap-4 items-center">
    23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
    24          {user ? (
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
