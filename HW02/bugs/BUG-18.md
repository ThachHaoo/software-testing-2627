# BUG-18

- **ID:** BUG-18
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
