# BUG-29

- **ID:** BUG-29
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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
