# BUG-24

- **ID:** BUG-24
- **Tiêu đề:** Giá sản phẩm ở thẻ sản phẩm trang chủ hiển thị đơn vị tiền tệ là 'VND' thay vì '₫' theo quy chuẩn
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/ (frontend-web); đối chiếu /product/4, /cart
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang hoạt động bình thường.

- Trình duyệt đang ở ngôn ngữ / locale tiếng Việt (vi-VN).

## Các bước tái hiện

1. Mở trình duyệt và truy cập vào trang chủ http://localhost:5173/.

2. Quan sát phần hiển thị giá tiền trên các thẻ sản phẩm ở trang chủ (ví dụ: sản phẩm Tai nghe AirPods Pro 2).

3. Mở trang chi tiết sản phẩm (/product/4) và trang giỏ hàng (/cart) để so sánh cách hiển thị ký hiệu đơn vị tiền tệ.

## Expected (trích SRS)

Theo yêu cầu FR-21.3 (kèm giả định B16): Hệ thống bắt buộc phải nhất quán hiển thị giá tiền bằng ký hiệu ₫ đi kèm định dạng phân cách hàng nghìn (ví dụ: 6.000.000 ₫) trên toàn bộ các trang giao diện (bao gồm cả trang chủ, trang chi tiết và giỏ hàng).

## Actual

- Tại trang chủ (/), giá tiền trên các thẻ sản phẩm lại hiển thị ký hiệu đơn vị là VND (ví dụ: 6.000.000 VND).

- Trong khi đó, ở trang chi tiết sản phẩm (/product/4) và trang giỏ hàng (/cart), giá tiền lại hiển thị đúng chuẩn với ký hiệu ₫ (ví dụ: 6.000.000 ₫). Việc này gây ra sự không đồng nhất về mặt giao diện giữa các trang.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-93_ui.png`
- TC-FR07-93: `HW02/B_FR07/evidence/TC-FR07-93_ui.png`

## TC liên quan

- Fail (1): TC-FR07-93
- Nhóm dữ kiện: G10 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-21.3:** (GUI, B16) Luôn dùng ký hiệu ₫ với định dạng phân cách hàng nghìn. — vi phạm ở: trang chủ dùng 'VND'
- Đạt trong cùng case: B13 (có phân cách '.' ở cả 5 chỗ), FR-21.3 ở trang chi tiết, trang giỏ (dùng '₫')
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-93): `locale trình duyệt=vi-VN; trang chủ (thẻ)="6.000.000 VND"; trang chi tiết="6.000.000 ₫"; giỏ: Đơn giá="6.000.000 ₫"; giỏ: Thành tiền="6.000.000 ₫"; giỏ: Tổng="6.000.000 ₫"`
- Cùng case: trang chi tiết và trang giỏ dùng '₫' (đạt).
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Home.jsx` dòng 86–88

  ```jsx
    86                <p className="text-red-500 font-bold mb-2">
    87                  {Number(p.price).toLocaleString()} VND
    88                </p>
  ```

### Nhận định

- Nguyên nhân: Trong file frontend-web/src/pages/Home.jsx (dòng 86–88), developer đã nối cứng (hardcode) chuỗi chữ "VND" đằng sau giá trị tiền tệ:

```jsx
<p className="text-red-500 font-bold mb-2">
  {Number(p.price).toLocaleString()} VND
</p>
```

- Việc hardcode chữ "VND" ở Home.jsx thay vì dùng chung helper format tiền tệ hoặc dùng ký hiệu ₫ (như các trang ProductDetail.jsx và Cart.jsx đang làm) khiến trang chủ bị lệch quy chuẩn giao diện so với phần còn lại của ứng dụng, vi phạm FR-21.3.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
