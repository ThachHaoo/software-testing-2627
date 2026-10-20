# BUG-23

- **ID:** BUG-23
- **Tiêu đề:** Thanh điều hướng Navbar không highlight link 'Giỏ hàng' khi người dùng đang ở trang Giỏ hàng
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart và / — navbar (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang chạy bình thường.

- Trình duyệt đang mở website EShop ở bất kỳ trang nào.

## Các bước tái hiện

1. Truy cập vào trang giỏ hàng http://localhost:5173/cart (hoặc nhấp chuột vào link "Giỏ hàng" trên thanh điều hướng).

2. Quan sát kiểu dáng hiển thị (màu sắc, gạch chân, độ đậm font) của link "Giỏ hàng" trên thanh điều hướng Navbar.

3. So sánh kiểu dáng của link "Giỏ hàng" khi ở trang /cart với khi chuyển sang trang chủ /.

## Expected (trích SRS)

Theo yêu cầu FR-23.1 (kèm giả định B16): Thanh điều hướng (Navbar) bắt buộc phải highlight (làm nổi bật bằng màu chữ khác, gạch chân active hoặc đổi font-weight/background) link đại diện cho trang hiện tại mà người dùng đang truy cập (cụ thể khi đang ở trang /cart thì link "Giỏ hàng" phải có kiểu dáng active khác biệt so với các link khác).

## Actual

Link "Giỏ hàng" trên Navbar khi người dùng đứng ở trang /cart có kiểu dáng hiển thị tĩnh hoàn toàn trùng hệt như khi đứng ở trang chủ / (chữ màu trắng rgb(255, 255, 255), font-weight 400, không gạch chân active, không có hiệu ứng highlight phân biệt).

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

- Nguyên nhân: Trong frontend-web/src/App.jsx (dòng 23), các đường dẫn trên Navbar sử dụng thẻ <Link> tĩnh của React Router thay vì <NavLink>:

```jsx
<Link to="/cart" className="hover:underline">Giỏ hàng</Link>
```

- Do dùng thẻ <Link> thông thường nên component không nhận diện được đường dẫn đường dẫn hiện tại (useLocation().pathname) để tự động áp dụng class css hay style active cho link "Giỏ hàng" khi URL khớp với /cart.

- Điều này khiến giao diện Navbar vi phạm yêu cầu GUI ở FR-23.1, làm người dùng không nhận biết được trang mình đang đứng thông qua thanh menu điều hướng.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/169

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
