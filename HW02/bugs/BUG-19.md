# BUG-19

- **ID:** BUG-19
- **Tiêu đề:** Bấm nút 'Xóa' ở trang giỏ hàng xóa ngay lập tức sản phẩm mà không hề hiển thị dialog xác nhận
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang chạy bình thường.

- Giỏ hàng đã có sẵn ít nhất một sản phẩm (ví dụ: Tai nghe AirPods Pro 2).

## Các bước tái hiện

1. Truy cập trang chủ http://localhost:5173/ và bấm "Thêm vào giỏ" trên thẻ 'Tai nghe AirPods Pro 2' (có thể thêm một sản phẩm khác để thấy dòng còn lại).

2. Bấm link "Giỏ hàng" trên navbar (không gõ URL /cart, không tải lại trang — giỏ web không lưu khi tải lại) và định vị dòng 'Tai nghe AirPods Pro 2'.

3. Bấm nút "Xóa" nằm ở cột Thao tác trên dòng sản phẩm đó đúng 1 lần.

4. Mắt quan sát xem giao diện có bật popup/dialog xác nhận hay không.

## Expected (trích SRS)

Theo yêu cầu FR-07.4 và FR-24.2 (kèm giả định B14): Khi bấm nút xóa sản phẩm khỏi giỏ hàng, hệ thống bắt buộc phải hiển thị một dialog/popup xác nhận trước khi thực hiện. Nếu người dùng chọn Đồng ý thì mới xóa dòng, chọn Hủy thì giữ nguyên dòng sản phẩm trong giỏ.

## Actual

Nút xóa hoàn toàn thiếu bước bật dialog xác nhận. Ngay khi bấm nút "Xóa", sản phẩm bị xóa lập tức khỏi giỏ hàng mà không cho người dùng cơ hội xác nhận hay hủy bỏ thao tác.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-08_ui.png`
- TC-FR07-08: `HW02/B_FR07/evidence/TC-FR07-08_ui.png`

## TC liên quan

- Fail (1): TC-FR07-08
- Blocked ghi case gốc (1): TC-FR07-09
- Nhóm dữ kiện: G5 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.4:** Nút Xóa sản phẩm phải có dialog xác nhận trước khi thực hiện.
- **FR-24.2:** Khi xóa item khỏi giỏ phải có dialog xác nhận (trùng FR-07.4).
- Đạt trong cùng case: B4 (Tổng SAU 4000000 = Thành tiền dòng còn lại), xoá dòng (dòng AirPods bị xoá, dòng Keychron không đổi)
- Chưa đánh giá được: FR-07.1 (nhãn cột kiểm ở TC-95)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-08): `đăng nhập cart08_1792476880905@domain.com: navbar có tên user; TRƯỚC: 2 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Bàn phím cơ Keychron Q1 | Đơn giá 4000000 | SL 1 | Thành tiền 4000000]; Tổng 10000000; không có badge; không có dialog; SAU: 1 dòng: [Bàn phím cơ Keychron Q1 | Đơn giá 4000000 | SL 1 | Thành tiền 4000000]; Tổng 4000000; không có badge`
- Các case Blocked ghi case gốc: TC-FR07-08 (A20).
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 49–55

  ```jsx
    49                <td>
    50                  <button
    51                    onClick={() => removeFromCart(index)}
    52                    className="text-red-500 hover:text-red-700"
    53                  >
    54                    Xóa
    55                  </button>
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/context/CartContext.jsx` dòng 12–16

  ```jsx
    12    const removeFromCart = (index) => {
    13      const newCart = [...cart];
    14      newCart.splice(index, 1);
    15      setCart(newCart);
    16    };
  ```

### Nhận định

- Ở file frontend-web/src/pages/Cart.jsx (dòng 51), sự kiện onClick của nút Xóa được gán thẳng hàm removeFromCart(index) mà không hề gọi qua modal custom hay hàm xác nhận mặc định của trình duyệt (chẳng hạn như window.confirm()):

```jsx
onClick={() => removeFromCart(index)}
```

- Ở file frontend-web/src/context/CartContext.jsx (dòng 12–16), hàm removeFromCart lập tức cắt phần tử ra khỏi mảng cart bằng splice và cập nhật state luôn mà không hề chặn lại kiểm tra điều kiện xác nhận.

- Việc thiếu hoàn toàn dialog xác nhận này làm cho case kiểm tra nút Hủy của dialog (TC-09) bị chặn (Blocked), đồng thời người dùng rất dễ bấm nhầm làm mất dữ liệu giỏ hàng mà không thể khôi phục.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/165

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
