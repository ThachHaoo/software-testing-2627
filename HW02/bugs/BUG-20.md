# BUG-20

- **ID:** BUG-20
- **Tiêu đề:** Link 'Giỏ hàng' trên thanh điều hướng Navbar thiếu hoàn toàn badge hiển thị số lượng sản phẩm khi trong giỏ đã có hàng
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173 — navbar, trang /cart (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang chạy bình thường.

- Người dùng đã thêm thành công ít nhất một sản phẩm vào giỏ hàng (ví dụ: đã có 2 dòng sản phẩm trong giỏ với tổng số lượng = 2).

## Các bước tái hiện

1. Truy cập vào trang web http://localhost:5173/.

2. Thêm sản phẩm bất kỳ vào giỏ hàng (ví dụ: thêm iPhone 15 Pro Max và Tai nghe AirPods Pro 2).

3. Mắt quan sát khu vực thanh điều hướng (Navbar) ở góc trên bên phải trang web, tại vị trí link/chữ "Giỏ hàng".

## Expected (trích SRS)

Theo yêu cầu FR-23.2 (kèm giả định B9/B16): Khi trong giỏ hàng đã có chứa sản phẩm (số lượng ≥ 1), link "Giỏ hàng" trên Navbar bắt buộc phải hiển thị badge con số đếm số lượng sản phẩm (ví dụ: hiển thị badge số 2 trên hoặc bên cạnh chữ "Giỏ hàng").

## Actual

Link "Giỏ hàng" trên Navbar luôn hiển thị dưới dạng thẻ văn bản thuần túy (Giỏ hàng). Hoàn toàn không có badge, icon con số hay phần tử hiển thị số lượng sản phẩm đi kèm, mặc dù kiểm tra trong trang /cart thì giỏ hàng thực tế đang chứa 2 dòng sản phẩm với tổng số lượng = 2.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-04_ui.png`
- TC-FR07-04: `HW02/B_FR07/evidence/TC-FR07-04_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-04_ui.png`

## TC liên quan

- Fail (1): TC-FR07-04
- Nhóm dữ kiện: G6 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-23.2:** (GUI, B16) Link "Giỏ hàng" phải hiển thị badge số lượng sản phẩm trong giỏ.
- Đạt trong cùng case: —
- Chưa đánh giá được: FR-07.3 (EC10/EC37: thêm từ trang chi tiết không vào giỏ, case gốc TC-61), FR-07.1 (nhãn cột kiểm ở TC-95)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-04): `đăng nhập cart04_1792476872458@domain.com: navbar có tên user; TRƯỚC: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge; ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/App.jsx` dòng 23

  ```jsx
    23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
  ```

### Nhận định

- Nguyên nhân: Trong file frontend-web/src/App.jsx tại dòng 23, thẻ <Link> dẫn đến giỏ hàng được viết cứng hoàn toàn chỉ với đoạn text tĩnh:

```jsx
<Link to="/cart" className="hover:underline">Giỏ hàng</Link>
```

- Component App không sử dụng useContext(CartContext) để lấy danh sách sản phẩm trong giỏ, cũng như không tính toán tổng số lượng (cart.reduce(...)) để render thêm thẻ badge (ví dụ: <span className="badge">...</span>) bên cạnh chữ "Giỏ hàng".

- Điều này khiến người dùng đứng ở bất kỳ trang nào cũng không thể biết được trong giỏ hàng của mình đang có bao nhiêu món đồ nếu không nhấp chuột mở trực tiếp trang /cart.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
