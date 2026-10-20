# BUG-23

- **ID:** BUG-23
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

- TC-FR07-92: `HW02/B_FR07/evidence/TC-FR07-92_failed.png`, `HW02/B_FR07/evidence/TC-FR07-92_ui-cart.png`, `HW02/B_FR07/evidence/TC-FR07-92_ui-home.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-92
- Nhóm dữ kiện: G9 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-23.1:** (GUI, B16) Thanh điều hướng (Navbar) phải highlight trang đang được chọn — xét trên trang Giỏ hàng.

- Đạt trong cùng case: —
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G9: UI · navbar: link tới /cart có kiểu hiển thị giống các link khác khi đang ở /cart (không highlight)
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-92, nguyên văn): ở /cart: [{"href":"/cart","text":"Giỏ hàng","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/login","text":"Đăng nhập","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/register","text":"Đăng ký","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"}]; ở trang chủ: [{"href":"/cart","text":"Giỏ hàng","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/login","text":"Đăng nhập","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/register","text":
- Đoạn code trích nguyên văn: `frontend-web/src/App.jsx` dòng 21–24 (xem `bugs_facts.md`, G9)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
