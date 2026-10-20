# BUG-17

- **ID:** BUG-17
- **Tiêu đề:** Thêm cùng một sản phẩm nhiều lần từ trang chủ không cộng dồn số lượng mà nhân bản thành nhiều dòng riêng biệt trong giỏ hàng
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/ → /cart (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon); TC-FR07-201 lấy từ lượt 3 (13:17), kết quả trùng lượt 2
- Kiểm tay: SV, 2026-10-20 (2 lần bấm cách nhau)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang chạy bình thường.
- Trạng thái giỏ hàng ban đầu đang trống.

## Các bước tái hiện

1. Truy cập vào trang chủ `http://localhost:5173/`.
2. Tìm sản phẩm `Tai nghe AirPods Pro 2` (id 4).
3. Bấm nút "Thêm vào giỏ" trên thẻ sản phẩm này 2 lần (hoặc spam click 20 lần nhanh).
4. Bấm vào link "Giỏ hàng" trên navbar để điều hướng sang trang `/cart`.
5. Kiểm tra danh sách các dòng sản phẩm hiển thị trong bảng giỏ hàng.

## Expected (trích SRS)

Theo yêu cầu FR-07.3: Khi thêm cùng một sản phẩm đã có trong giỏ hàng, hệ thống bắt buộc phải cộng dồn số lượng trên dòng sản phẩm đó chứ không được tạo thêm dòng mới (ví dụ: bấm nút thêm 2 lần thì giỏ hàng chỉ có đúng 1 dòng `Tai nghe AirPods Pro 2` với Số lượng = 2).

## Actual

Giỏ hàng không hề cộng dồn số lượng mà tự động tạo thêm dòng mới trùng hệt cho mỗi lần bấm thêm:
- Khi bấm 2 lần: Trong giỏ xuất hiện 2 dòng trùng nhau hoàn toàn (`Tai nghe AirPods Pro 2`), mỗi dòng đều có Số lượng = 1 và Thành tiền = 6.000.000 ₫.
- Khi tự động hóa test spam click 20 lần: Trong giỏ văng ra đúng 20 dòng trùng nhau liệt kê liên tiếp.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-201_manual_2lan.png` (kiểm tay, SV chụp)
- TC-FR07-201: `HW02/B_FR07/evidence/TC-FR07-201_failed.png`, `HW02/B_FR07/evidence/TC-FR07-201_manual_2lan.png`, `HW02/B_FR07/evidence/TC-FR07-201_ui.png`

## TC liên quan

- Fail (1): TC-FR07-201
- Nhóm dữ kiện: G3 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.3:** Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.
- Đạt trong cùng case: B4 (mỗi dòng Thành tiền 6000000 = 1 × 6000000)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-201): `TRƯỚC: không có bảng (giỏ trống); bấm 20 lần (element.click() trong trang) trong 410 ms [notes] thời gian thực tế 410 ms > 400 ms của cột Thao tác; SAU: 20 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe Ai… (rút gọn)`
- Thời gian bấm thực tế 405 ms (lượt 2), 410 ms (lượt 3) so với 400 ms của cột Thao tác; notes SV: không ảnh hưởng kết luận.
- Tầng API cùng dạng quan sát: nhóm API 'POST cùng id → phần tử mới' (TC-FR07-21).
- Tái hiện tối thiểu với 2 lần bấm cách nhau: SV kiểm tay 2026-10-20: 2 lần bấm → 2 dòng (evidence `TC-FR07-201_manual_2lan.png`)
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt); lượt 3 cũng giống.
- Đoạn code trích nguyên văn: `frontend-web/src/context/CartContext.jsx` dòng 8–10

  ```jsx
     8    const addToCart = (product, quantity) => {
     9      setCart([...cart, { ...product, quantity }]);
    10    };
  ```

### Nhận định

- Nguyên nhân: Trong frontend-web/src/context/CartContext.jsx (dòng 8–10), hàm addToCart xử lý cập nhật state giỏ hàng cực kỳ ngây thơ:
```jsx
const addToCart = (product, quantity) => {
  setCart([...cart, { ...product, quantity }]);
};
```
- Code không hề dùng find hay findIndex để kiểm tra xem product.id đã tồn tại trong mảng cart hay chưa. Mỗi lần hàm được gọi, nó chỉ đơn giản dùng Spread Operator ([...cart, newProduct]) để append (đẩy thêm) một object mới vào cuối mảng cart.

- Điều này dẫn đến việc giỏ hàng bị nhân bản vô tội vạ các dòng trùng id, vi phạm trực tiếp quy tắc gộp/cộng dồn số lượng của FR-07.3.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
