# BUG-21

- **ID:** BUG-21
- **Tiêu đề:** Trang giỏ hàng trống chỉ có thông báo chữ, thiếu hoàn toàn hình minh họa/icon theo yêu cầu Empty State
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart, giỏ trống (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang chạy bình thường.

- Giỏ hàng hiện tại đang hoàn toàn trống (chưa có bất kỳ sản phẩm nào).

## Các bước tái hiện

1. Mở trình duyệt và truy cập trực tiếp vào trang giỏ hàng http://localhost:5173/cart (hoặc bấm vào link "Giỏ hàng" trên navbar khi giỏ đang trống).

2. Quan sát phần hiển thị giao diện trạng thái trống (Empty State) trên màn hình.

## Expected (trích SRS)

Theo yêu cầu FR-07.7 và FR-24.3: Khi giỏ hàng trống, giao diện bắt buộc phải có thông báo rõ ràng kèm theo hình minh họa hoặc icon trực quan (Empty State) để tăng trải nghiệm người dùng, kèm đường dẫn "Tiếp tục mua sắm" quay về trang chủ.

## Actual

Giao diện trang giỏ hàng trống chỉ hiển thị hai dòng chữ giản đơn: tiêu đề "Giỏ hàng của bạn đang trống" và đường dẫn "Tiếp tục mua sắm". Hoàn toàn không xuất hiện bất kỳ hình ảnh (<img>), hình minh họa hay icon (SVG/FontIcon) nào đi kèm theo quy định thiết kế Empty State.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-01_ui.png`
- TC-FR07-01: `HW02/B_FR07/evidence/TC-FR07-01_failed.png`, `HW02/B_FR07/evidence/TC-FR07-01_ui.png`

## TC liên quan

- Fail (1): TC-FR07-01
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.7:** Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng. — vi phạm ở: thiếu hình minh hoạ; có thông báo 'Giỏ hàng của bạn đang trống'
- **FR-24.3:** Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện (bổ sung FR-07.7). — vi phạm ở: thiếu icon/hình minh hoạ
- Đạt trong cùng case: FR-07.5 (link về trang chủ → URL '/'), FR-23.2 (badge ẩn khi giỏ trống, chấp nhận theo B22)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-01): `TRƯỚC: không có bảng (giỏ trống); trạng thái trống: bảng=không, ảnh/icon=không, chữ="Giỏ hàng của bạn đang trốngTiếp tục mua sắm"; URL sau thao tác=http://localhost:5173/`
- Cùng case: dòng chữ 'Giỏ hàng của bạn đang trống' có; link về trang chủ → URL '/' đạt.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 20–27

  ```jsx
    20    if (cart.length === 0) {
    21      return (
    22        <div className="text-center mt-10">
    23          <h2 className="text-2xl mb-4">Giỏ hàng của bạn đang trống</h2>
    24          <Link to="/" className="text-blue-600 hover:underline">Tiếp tục mua sắm</Link>
    25        </div>
    26      );
    27    }
  ```

### Nhận định

- Nguyên nhân: Trong file frontend-web/src/pages/Cart.jsx (dòng 20–27), khi kiểm tra cart.length === 0, giao diện được trả về rất sơ sài:

```jsx
if (cart.length === 0) {
  return (
    <div className="text-center mt-10">
      <h2 className="text-2xl mb-4">Giỏ hàng của bạn đang trống</h2>
      <Link to="/" className="text-blue-600 hover:underline">Tiếp tục mua sắm</Link>
    </div>
  );
}
```
- Developer chỉ chèn thẻ <h2> chứa câu thông báo chữ và thẻ <Link> để điều hướng về trang chủ mà quên không thêm bất kỳ phần tử ảnh hoặc icon minh họa nào (như ảnh chiếc giỏ hàng rỗng) phía trên dòng thông báo.

- Dù giao diện đã đáp ứng được phần thông báo chữ và link chuyển trang, việc bỏ qua hình minh họa/icon khiến giao diện vi phạm trực tiếp tiêu chuẩn thiết kế Empty State được quy định cụ thể tại FR-07.7 và FR-24.3.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
