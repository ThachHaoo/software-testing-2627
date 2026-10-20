# BUG-25

- **ID:** BUG-25
- **Tiêu đề:** Toàn bộ 5 ảnh sản phẩm hiển thị trên trang chủ bị cài thuộc tính alt rỗng (alt="")
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

- Hệ thống frontend web và backend server đang chạy bình thường.

- Trình duyệt mở ở chế độ ẩn danh (Incognito mode, không bật extension/tiện ích mở rộng).

## Các bước tái hiện

1. Mở trình duyệt ẩn danh và truy cập vào trang chủ http://localhost:5173/.

2. Mở DevTools (bấm F12 hoặc chuột phải chọn Inspect/Kiểm tra) để kiểm tra DOM của các thẻ ảnh <img> trên 5 thẻ sản phẩm ở trang chủ.

3. Chuyển sang trang chi tiết sản phẩm (http://localhost:5173/product/4) và kiểm tra thuộc tính alt của thẻ <img> tại trang chi tiết để so sánh.

## Expected (trích SRS)

Theo yêu cầu FR-24.4 (kèm giả định B16): Tất cả các thẻ ảnh sản phẩm trên toàn hệ thống bắt buộc phải có thuộc tính alt chứa văn bản mô tả nội dung trực quan của ảnh (không được để rỗng alt="") nhằm hỗ trợ đọc màn hình (Accessibility) và SEO.

## Actual

- Tại trang chủ (/), cả 5 thẻ ảnh sản phẩm đều bị bỏ rỗng thuộc tính alt (alt="").

- Trong khi đó, ở trang chi tiết sản phẩm (/product/4), thẻ ảnh được gắn giá trị alt chính xác là tên sản phẩm (alt="Tai nghe AirPods Pro 2").

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-94_ui.png`
- TC-FR07-94: `HW02/B_FR07/evidence/TC-FR07-94_ui.png`

## TC liên quan

- Fail (1): TC-FR07-94
- Nhóm dữ kiện: G11 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-24.4:** (GUI, B16) Tất cả ảnh sản phẩm phải có thuộc tính alt mô tả nội dung (không rỗng). — vi phạm ở: trang chủ: 5/5 alt rỗng
- Đạt trong cùng case: FR-24.4 ở trang chi tiết (alt = tên sản phẩm)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-94): `alt trang chủ=["","","","",""]; alt trang chi tiết=["Tai nghe AirPods Pro 2"]; trang giỏ không có ảnh sản phẩm (notes, không tính Fail); [kiểm tay] alt "mô tả nội dung ảnh": SV đối chiếu chữ alt với ảnh`
- Cùng case: trang chi tiết alt = tên sản phẩm (đạt); trang giỏ không có ảnh.
- Bug dùng evidence tự động TC-FR07-94_ui.png (Playwright, không tiện ích); không dùng ảnh kiểm tay.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Home.jsx` dòng 80–84

  ```jsx
    80                <img
    81                  src={p.imageUrl}
    82                  alt=""
    83                  className="w-full h-48 object-cover mb-4 rounded"
    84                />
  ```

### Nhận định

- Nguyên nhân: Trong file frontend-web/src/pages/Home.jsx (dòng 80–84), thẻ <img> của sản phẩm bị gán cứng thuộc tính alt là chuỗi rỗng:

```jsx
<img
  src={p.imageUrl}
  alt=""
  className="w-full h-48 object-cover mb-4 rounded"
/>
```

- Developer đã gán cứng alt="" thay vì trích xuất thuộc tính p.name (hoặc p.title) để truyền vào như cách làm đúng ở ProductDetail.jsx (alt={product.name}).

- Việc để rỗng alt="" trên thẻ ảnh trang chủ làm mất khả năng tiếp cận người dùng dùng trình đọc màn hình, vi phạm tiêu chuẩn thiết kế GUI ở FR-24.4.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
