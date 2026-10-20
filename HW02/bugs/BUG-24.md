# BUG-24

- **ID:** BUG-24
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/ (frontend-web); đối chiếu /product/4, /cart
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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
