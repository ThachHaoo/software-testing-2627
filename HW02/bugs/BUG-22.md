# BUG-22

- **ID:** BUG-22
- **Tiêu đề:** Trang Giỏ hàng thiếu hoàn toàn thanh điều hướng Breadcrumb ở vùng nội dung chính
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

- Hệ thống frontend web và backend server đang chạy bình thường.

- Người dùng đang ở bất kỳ trang nào trên website.

## Các bước tái hiện

1. Mở trình duyệt và truy cập vào trang giỏ hàng http://localhost:5173/cart (hoặc bấm nút/link "Giỏ hàng" trên thanh điều hướng).

2. Quan sát vùng giao diện nội dung chính phía trên tiêu đề "Giỏ Hàng".

## Expected (trích SRS)

Theo yêu cầu FR-23.4 (kèm giả định B16): Trang con Giỏ hàng (/cart) bắt buộc phải hiển thị thanh điều hướng Breadcrumb ở phía trên vùng nội dung chính (ví dụ: Trang chủ > Giỏ hàng) giúp người dùng nhận biết vị trí phân cấp trang hiện tại và dễ dàng nhấp chuyển nhanh về các trang cha.

## Actual

Tại trang /cart, vùng nội dung chính bắt đầu ngay bằng thẻ tiêu đề <h2>Giỏ Hàng</h2>. Hoàn toàn không xuất hiện bất kỳ thanh điều hướng Breadcrumb nào phía trên tiêu đề hay trong khu vực nội dung trang.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-91_ui.png`
- TC-FR07-91: `HW02/B_FR07/evidence/TC-FR07-91_ui.png`

## TC liên quan

- Fail (1): TC-FR07-91
- Nhóm dữ kiện: G8 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-23.4:** (GUI, B16) Breadcrumb bắt buộc có ở trang con Giỏ hàng.
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-91): `không tìm thấy breadcrumb ở vùng nội dung chính`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 29–31

  ```jsx
    29    return (
    30      <div className="bg-white p-6 border rounded shadow-sm">
    31        <h2 className="text-2xl font-bold mb-6">Giỏ Hàng</h2>
  ```

### Nhận định

- Nguyên nhân: Trong component frontend-web/src/pages/Cart.jsx (dòng 29–31), giao diện trang giỏ hàng được render thẳng từ thẻ <div> bọc tiêu đề <h2>:

```jsx
return (
  <div className="bg-white p-6 border rounded shadow-sm">
    <h2 className="text-2xl font-bold mb-6">Giỏ Hàng</h2>
```

- Developer hoàn toàn bỏ quên việc thiết kế hoặc nhúng component Breadcrumb (ví dụ: <Breadcrumb '/' 'Giỏ 'Trang chủ', hàng' items="{[{" label: link: { }, }]}/>) vào đầu trang con /cart.

- Việc thiếu thanh điều hướng vết trang này làm giảm khả năng điều hướng phân cấp của giao diện người dùng, vi phạm trực tiếp quy định GUI ở FR-23.4.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
