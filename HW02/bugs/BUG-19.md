# BUG-19

- **ID:** BUG-19
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart (frontend-web)
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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
