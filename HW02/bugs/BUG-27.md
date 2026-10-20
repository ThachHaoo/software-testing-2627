# BUG-27

- **ID:** BUG-27
- **Tiêu đề:** Nút 'Xóa' ở cột Thao tác trang Giỏ hàng hiển thị sai nhãn 'Xóa' thay vì 'Xóa sản phẩm' theo quy định SRS
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang hoạt động bình thường.

- Đã thêm ít nhất một sản phẩm bất kỳ vào giỏ hàng từ trang chủ (để bảng giỏ hàng hiển thị các dòng sản phẩm cùng cột Thao tác).

## Các bước tái hiện

1. Mở trình duyệt và truy cập vào trang chủ http://localhost:5173/.

2. Bấm nút "Thêm vào giỏ" trên thẻ một sản phẩm bất kỳ (ví dụ: Tai nghe AirPods Pro 2).

3. Bấm vào link "Giỏ hàng" trên thanh điều hướng Navbar để vào trang /cart.

4. Quan sát nhãn văn bản hiển thị trên nút nằm ở cột Thao tác của dòng sản phẩm.

## Expected (trích SRS)

Theo yêu cầu FR-07.4 (kèm giả định B12): Nút thực hiện thao tác xóa sản phẩm khỏi giỏ hàng bắt buộc phải hiển thị chính xác nhãn văn bản là Xóa sản phẩm (hoặc Xoá sản phẩm).

## Actual

Nút bấm ở cột Thao tác chỉ hiển thị nhãn ngắn gọn là Xóa (hoặc Xoá), hoàn toàn thiếu vắng từ "sản phẩm" phía sau so với nhãn chuẩn được quy định trong SRS.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-96_ui.png`
- TC-FR07-96: `HW02/B_FR07/evidence/TC-FR07-96_ui.png`

## TC liên quan

- Fail (1): TC-FR07-96
- Nhóm dữ kiện: G13 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.4:** Nút Xóa sản phẩm phải có dialog xác nhận trước khi thực hiện.
- **B12 (giả định SV chốt):** (nhãn chính xác) (SV chốt 2026-10-20): các cụm in đậm trong FR-07 là nhãn — 'Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác', 'Xóa sản phẩm', 'Tiếp tục mua sắm', 'Tổng cộng'. So khớp đúng chữ, PHÂN BIỆT hoa/thường, chuẩn hoá Unicode NFC trước khi so; coi hai cách đặt dấu 'óa'/'oá' là như nhau (vd 'Xóa' = 'Xoá'). Chỉ kiểm ở TC-FR07-95…98; case chức năng định vị nút/link không dựa vào chữ.
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-96): `nhãn đọc được=["Xóa"]`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 50–55

  ```jsx
    50                  <button
    51                    onClick={() => removeFromCart(index)}
    52                    className="text-red-500 hover:text-red-700"
    53                  >
    54                    Xóa
    55                  </button>
  ```

### Nhận định

- Nguyên nhân: Trong file frontend-web/src/pages/Cart.jsx (dòng 54), developer đã gán cứng nhãn của nút xóa chỉ là chuỗi "Xóa":

```jx
<button
  onClick={() => removeFromCart(index)}
  className="text-red-500 hover:text-red-700"
>
  Xóa
</button>
```

- Việc viết thiếu chữ "sản phẩm" khiến nhãn nút không khớp với quy chuẩn nhãn in đậm Xóa sản phẩm được định nghĩa tại FR-07.4 và giả định B12.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
