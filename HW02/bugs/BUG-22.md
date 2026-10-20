# BUG-22

- **ID:** BUG-22
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

- TC-FR07-91: `HW02/B_FR07/evidence/TC-FR07-91_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-91
- Nhóm dữ kiện: G8 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-23.4:** (GUI, B16) Breadcrumb bắt buộc có ở trang con Giỏ hàng.

- Đạt trong cùng case: —
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G8: UI · trang giỏ: không có breadcrumb ở vùng nội dung chính
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-91, nguyên văn): không tìm thấy breadcrumb ở vùng nội dung chính
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 29–31 (xem `bugs_facts.md`, G8)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
