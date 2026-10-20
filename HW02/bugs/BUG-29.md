# BUG-29

- **ID:** BUG-29
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

- TC-FR07-98: `HW02/B_FR07/evidence/TC-FR07-98_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-98
- Nhóm dữ kiện: G15 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.6:** Tổng tiền hiển thị nhãn chính xác "Tổng cộng" (không phải "Tổng tạm tính").

- Đạt trong cùng case: —
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G15: UI · trang giỏ: nhãn dòng tổng là 'Tổng tạm tính:' (SRS: 'Tổng cộng')
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-98, nguyên văn): nhãn đọc được=["Tổng tạm tính:"]
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 62–64 (xem `_groups_B_FR07.md`, G15)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
