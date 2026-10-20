# BUG-28

- **ID:** BUG-28
- **Tiêu đề:** Link quay lại trang chủ ở trang Giỏ hàng (khi giỏ có hàng) hiển thị sai nhãn '← Mua tiếp' thay vì 'Tiếp tục mua sắm' theo quy định SRS
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

- Đã thêm ít nhất một sản phẩm bất kỳ vào giỏ hàng từ trang chủ (để trang giỏ hàng ở trạng thái có sản phẩm).

## Các bước tái hiện

1. Mở trình duyệt và truy cập vào trang chủ http://localhost:5173/.

2. Bấm nút "Thêm vào giỏ" trên thẻ một sản phẩm bất kỳ (ví dụ: Tai nghe AirPods Pro 2).

3. Bấm vào link "Giỏ hàng" trên thanh điều hướng Navbar để điều hướng sang trang /cart.

4. Quan sát nhãn văn bản hiển thị trên nút/link quay về trang chủ ở bên dưới bảng giỏ hàng.

## Expected (trích SRS)

Theo yêu cầu FR-07.5 (kèm giả định B12): Nút/link để chuyển hướng quay lại trang chủ ở trang Giỏ hàng bắt buộc phải hiển thị chính xác nhãn văn bản là Tiếp tục mua sắm.

## Actual

Khi giỏ hàng có chứa sản phẩm, nút quay về trang chủ chỉ hiển thị nhãn là ← Mua tiếp, hoàn toàn sai lệch so với nhãn chuẩn "Tiếp tục mua sắm" được định nghĩa trong SRS.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-97_ui.png`
- TC-FR07-97: `HW02/B_FR07/evidence/TC-FR07-97_ui.png`

## TC liên quan

- Fail (1): TC-FR07-97
- Nhóm dữ kiện: G14 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.5:** Có nút Tiếp tục mua sắm để quay về trang chủ.
- **B12 (giả định SV chốt):** (nhãn chính xác) (SV chốt 2026-10-20): các cụm in đậm trong FR-07 là nhãn — 'Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác', 'Xóa sản phẩm', 'Tiếp tục mua sắm', 'Tổng cộng'. So khớp đúng chữ, PHÂN BIỆT hoa/thường, chuẩn hoá Unicode NFC trước khi so; coi hai cách đặt dấu 'óa'/'oá' là như nhau (vd 'Xóa' = 'Xoá'). Chỉ kiểm ở TC-FR07-95…98; case chức năng định vị nút/link không dựa vào chữ.
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-97): `nhãn đọc được=["← Mua tiếp"]`
- Trang giỏ trống có link 'Tiếp tục mua sắm' (Cart.jsx dòng 24); TC-FR07-97 kiểm khi giỏ có 1 dòng.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 65–68

  ```jsx
    65          <div className="flex gap-3">
    66            <Link to="/" className="border px-4 py-2 rounded text-gray-600 hover:bg-gray-50">
    67              ← Mua tiếp
    68            </Link>
  ```

### Nhận định

- Nguyên nhân: Trong file frontend-web/src/pages/Cart.jsx (dòng 66–68), khi giỏ hàng có sản phẩm, developer đã gán cứng nhãn cho thẻ <Link to="/"> là "← Mua tiếp":

```jsx
<Link to="/" className="border px-4 py-2 rounded text-gray-600 hover:bg-gray-50">
  ← Mua tiếp
</Link>
```

- Mặc dù khi giỏ hàng rỗng (ở dòng 24), trang có hiển thị chữ "Tiếp tục mua sắm", nhưng ở giao diện bảng giỏ hàng có hàng thì nút này lại bị đặt nhãn sai thành "← Mua tiếp", vi phạm quy chuẩn nhãn in đậm Tiếp tục mua sắm tại FR-07.5 và giả định B12.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/174

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
