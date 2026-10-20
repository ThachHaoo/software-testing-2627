# BUG-29

- **ID:** BUG-29
- **Tiêu đề:** Nhãn tổng tiền tại trang Giỏ hàng hiển thị sai thành 'Tổng tạm tính:' thay vì 'Tổng cộng' theo quy định SRS
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

- Giỏ hàng đã có chứa sản phẩm (được thêm từ trang chủ) để hiển thị khu vực tổng tiền ở trang /cart.

## Các bước tái hiện

1. Mở trình duyệt và truy cập vào trang chủ http://localhost:5173/.

2. Bấm nút "Thêm vào giỏ" trên thẻ một sản phẩm bất kỳ (ví dụ: Tai nghe AirPods Pro 2).

3. Bấm vào link "Giỏ hàng" trên thanh điều hướng Navbar để sang trang /cart.

4. Quan sát nhãn văn bản hiển thị ngay trước số tiền ở phần tổng kết giỏ hàng.

## Expected (trích SRS)

Theo yêu cầu FR-07.6: Nhãn hiển thị cho phần tổng tiền ở trang giỏ hàng bắt buộc phải ghi chính xác là Tổng cộng (SRS có quy định câu rõ ràng: không được ghi thành "Tổng tạm tính").

## Actual

Nhãn hiển thị thực tế tại góc tổng tiền lại ghi là Tổng tạm tính: (ví dụ: Tổng tạm tính: 6.000.000 ₫), trực tiếp vi phạm câu cấm của SRS.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-98_ui.png`
- TC-FR07-98: `HW02/B_FR07/evidence/TC-FR07-98_ui.png`

## TC liên quan

- Fail (1): TC-FR07-98
- Nhóm dữ kiện: G15 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.6:** Tổng tiền hiển thị nhãn chính xác "Tổng cộng" (không phải "Tổng tạm tính").
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-98): `nhãn đọc được=["Tổng tạm tính:"]`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 62–64

  ```jsx
    62          <div className="text-xl font-bold">
    63            Tổng tạm tính: <span className="text-red-600">{cartTotal.toLocaleString()} ₫</span>
    64          </div>
  ```

### Nhận định

- Nguyên nhân: Trong file frontend-web/src/pages/Cart.jsx (dòng 63), developer đã gán cứng chuỗi văn bản "Tổng tạm tính:":

```jsx
<div className="text-xl font-bold">
  Tổng tạm tính: <span className="text-red-600">{cartTotal.toLocaleString()} ₫</span>
</div>
```

- Việc hardcode từ "Tổng tạm tính:" thay vì "Tổng cộng:" làm sai lệch nhãn giao diện và vi phạm trực tiếp quy định cụ thể của SRS tại FR-07.6.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
