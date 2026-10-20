# BUG-18

- **ID:** BUG-18
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

- TC-FR07-90: `HW02/B_FR07/evidence/TC-FR07-90_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-90
- Blocked ghi case gốc (4): TC-FR07-05, TC-FR07-06, TC-FR07-07, TC-FR07-65
- Nhóm dữ kiện: G4 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-07.2:** Cột Số lượng có nút +/- để chỉnh số lượng.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G4: UI · trang giỏ: ô Số lượng của dòng không có nút '+' / '-'
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-90, nguyên văn): dòng: 1 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 6000000; không có badge; nút trong ô Số lượng: []
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 47 (xem `bugs_facts.md`, G4)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
