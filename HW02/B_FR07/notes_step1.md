# B_FR07 – Notes bước 1 (trích SRS, khảo sát SUT)

> Chép từ báo cáo bước 1 của Claude Code (lượt 20/10/2026, commit `b48929e`), không viết lại.
> Giả định B0a–B18 và bảng biến vào/ra đã nằm trong `testcases.json` / `testcases.md` → không lặp ở đây.

## Trích nguyên văn SRS

`../eshop-sut/README.md` (SRS v2.0, file .md, không có số trang — ghi mục + dòng):

```
§4 FR-07 (dòng 93–100)
### FR-07: Giỏ hàng (Shopping Cart)
- Hiển thị danh sách sản phẩm với các cột: **Sản phẩm**, **Đơn giá**, **Số lượng** (có nút +/- để chỉnh), **Thành tiền**, **Thao tác**.
- Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.
- Nút **Xóa sản phẩm** phải có dialog xác nhận trước khi thực hiện.
- Có nút **Tiếp tục mua sắm** để quay về trang chủ.
- Tổng tiền hiển thị nhãn chính xác: **"Tổng cộng"** (không phải "Tổng tạm tính").
- Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng.

§3 FR-06 (dòng 85–87)
- Có ô nhập **Số lượng** (chỉ nhận số nguyên dương, tối thiểu là 1).
- Nút **Thêm vào giỏ hàng** — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).

§4 FR-08 (dòng 104, 105, 108)
- Chỉ người dùng **đã đăng nhập** mới tiến hành thanh toán được.
- **Tổng tiền thanh toán** được tính tự động từ giỏ hàng và không cho phép người dùng chỉnh sửa trực tiếp.
- Sau thanh toán thành công, giỏ hàng được xóa.

§7 FR-20 (dòng 235)
- Đầy đủ các chức năng: Xem sản phẩm, Đăng nhập, Đăng xuất, Đăng ký, Giỏ hàng, Thanh toán, Hồ sơ, Lịch sử đơn hàng.

§8 FR-21 (dòng 246)
- **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
§8 FR-23 (dòng 261, 263)
- Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ.
- Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm).
§8 FR-24 (dòng 267–270)
- Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- Khi xóa item khỏi giỏ phải có dialog xác nhận.
- Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện.
- Tất cả ảnh sản phẩm phải có thuộc tính `alt` mô tả nội dung ảnh (không để rỗng).

§9 (dòng 279, 281)
| SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ. |
| SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
```

`api_specification.md` §4, dòng 110–127: GET và POST `/api/cart`, header `Authorization: Bearer <token>`, body `{id, name, price, quantity}`.

## Khảo sát SUT (chỉ để biết điểm quan sát, không dùng làm nguồn yêu cầu)

- **Endpoint giỏ hàng:**
  - `GET /api/cart` và `POST /api/cart` (`server.js:284–295`) đều cần token.
  - Thiếu token trả 401 `{"error":"Unauthorized"}`; token sai trả 403 `{"error":"Forbidden"}` (`server.js:100–110`).
  - POST thành công trả 200 `{"message":"Added to cart"}`.
  - Không có endpoint sửa hay xoá dòng giỏ.
- **userCarts:** đối tượng trong RAM, khoá là `req.user.id` lấy từ JWT. Mất khi restart backend; restart cũng seed lại CSDL.
- **Giỏ trên web:**
  - Là state React trong `CartContext.jsx`, **không gọi `/api/cart`**, không lưu localStorage. Tải lại trang hoặc `page.goto` là mất giỏ, nên script UI phải điều hướng bằng link trong app.
  - Có 3 điểm thêm vào giỏ:
    - trang chủ `/`: nút "Thêm vào giỏ" (số lượng luôn là 1);
    - `/product/:id`: ô "Số lượng:" (`input type=number`, không có min/max);
    - `/product/:id`: nút "Thêm vào giỏ hàng".
  - Trang `/cart` có:
    - tiêu đề cột "Sản phẩm/Giá/Số lượng/Thành tiền/Thao tác";
    - nút "Xóa", nhãn "Tổng tạm tính:", link "← Mua tiếp";
    - khi giỏ trống: dòng "Giỏ hàng của bạn đang trống" và link "Tiếp tục mua sắm".
  - Link navbar "Giỏ hàng" nằm ở `App.jsx:23`.
  - Mã không có thuộc tính `data-testid`, nên selector phải dựa trên role và text.
- **Sản phẩm seed:** bảng products có `id, name, price INTEGER, description, imageUrl, category_id`. **Không có tồn kho hay trạng thái.** 5 sản phẩm, giá từ 4.000.000 đến 45.000.000.
- **Ghi nhận trung lập, chưa kết luận, chờ bước 6:**
  - chưa thấy nút +/-;
  - nút "Xóa" gọi xoá trực tiếp;
  - lần bấm đầu ở trang chi tiết không gọi `addToCart` (`ProductDetail.jsx:21–31`);
  - `GET /api/products/:id` trả giá dạng chuỗi với id chẵn (`server.js:162`).
