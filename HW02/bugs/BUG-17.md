# BUG-17

- **ID:** BUG-17
- **Tiêu đề:** 
- **Severity:** 
- **Priority:** 

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173 (frontend-web), API http://localhost:3000
- Lượt chính thức: lượt 2, 2026-10-20 13:14 (Asia/Saigon); TC-FR07-201, 209 từ lượt 3 (13:17), kết quả trùng lượt 2
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện


## Các bước tái hiện


## Expected (trích SRS)


## Actual


## Bằng chứng

<details>
<summary>Evidence từng TC (1)</summary>

- TC-FR07-201: `HW02/B_FR07/evidence/TC-FR07-201_failed.png`, `HW02/B_FR07/evidence/TC-FR07-201_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-201
- Nhóm dữ kiện: G3 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-07.3:** Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.

- Đạt trong cùng case: B4 (mỗi dòng Thành tiền 6000000 = 1 × 6000000)
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G3: UI · trang chủ: bấm 'Thêm vào giỏ' cùng sản phẩm 20 lần → trang giỏ có 20 dòng riêng, mỗi dòng Số lượng 1 (không cộng dồn)
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt); lượt 3 cũng giống.
- Actual tiêu biểu (TC-FR07-201, nguyên văn): TRƯỚC: không có bảng (giỏ trống); bấm 20 lần (element.click() trong trang) trong 410 ms [notes] thời gian thực tế 410 ms > 400 ms của cột Thao tác; SAU: 20 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe Ai
- Thời gian bấm thực tế 405 ms (lượt 2), 410 ms (lượt 3) so với 400 ms của cột Thao tác; notes SV: không ảnh hưởng kết luận.
- Tầng API cùng dạng quan sát: nhóm API 'POST cùng id → phần tử mới' (TC-FR07-21).
- Đoạn code trích nguyên văn: `frontend-web/src/context/CartContext.jsx` dòng 8–10 (xem `bugs_facts.md`, G3)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
