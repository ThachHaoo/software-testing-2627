# BUG-18

- **ID:** BUG-18
- **Tiêu đề:** Trang giỏ hàng thiếu hoàn toàn hai nút '+' và '-' để điều chỉnh số lượng sản phẩm ở cột Số lượng
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang chạy bình thường.

- Giỏ hàng đã có sẵn ít nhất một sản phẩm (thêm từ trang chủ hoặc trang chi tiết).

## Các bước tái hiện

1. Truy cập vào trang chủ http://localhost:5173/.

2. Bấm nút "Thêm vào giỏ" trên thẻ một sản phẩm bất kỳ (ví dụ: Tai nghe AirPods Pro 2).

3. Bấm vào link "Giỏ hàng" trên navbar để điều hướng sang trang /cart.

4. Quan sát ô hiển thị ở cột "Số lượng" trên dòng sản phẩm trong bảng giỏ hàng.

## Expected (trích SRS)

Theo yêu cầu FR-07.2: Tại bảng giỏ hàng, cột Số lượng bắt buộc phải có hai nút + và - đi kèm để người dùng có thể bấm điều chỉnh tăng hoặc giảm số lượng trực tiếp cho dòng sản phẩm đó.

## Actual

Tại cột "Số lượng", giao diện chỉ hiển thị duy nhất một con số văn bản thuần túy (text tĩnh, ví dụ: 1). Hoàn toàn không có nút +, nút - hay bất kỳ ô input tương tác nào để chỉnh sửa số lượng sản phẩm ngay tại giỏ hàng.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-90_ui.png`
- TC-FR07-90: `HW02/B_FR07/evidence/TC-FR07-90_ui.png`

## TC liên quan

- Fail (1): TC-FR07-90
- Blocked ghi case gốc (4): TC-FR07-05, TC-FR07-06, TC-FR07-07, TC-FR07-65
- Nhóm dữ kiện: G4 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.2:** Cột Số lượng có nút +/- để chỉnh số lượng.
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-90): `dòng: 1 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 6000000; không có badge; nút trong ô Số lượng: []`
- Các case Blocked ghi case gốc: TC-FR07-90 (TC-FR07-06, 65: thêm TC-FR07-61) (A20).
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 47

  ```jsx
    47                <td>{item.quantity}</td>
  ```

### Nhận định

- Nguyên nhân: Trong frontend-web/src/pages/Cart.jsx tại dòng 47, developer chỉ render mỗi biến {item.quantity} ra thẻ <td> đơn thuần:

```jsx
<td>{item.quantity}</td>
```

- Code Frontend quên hẳn việc thiết kế giao diện UI và sự kiện nhấp chuột cho hai nút tăng/giảm số lượng (+ và -).

- Do thiếu mất hai nút bấm này ở mức UI, toàn bộ các test case liên quan đến chức năng chỉnh sửa số lượng bằng nút +/- trong giỏ hàng (TC-05, TC-06, TC-07, TC-65) đều bị chặn (Blocked) không thể thực hiện thao tác được.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
