# BUG-31

- **ID:** BUG-31
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
<summary>Evidence từng TC (2)</summary>

- TC-FR07-22: `HW02/B_FR07/evidence/TC-FR07-22_api.png`, `HW02/B_FR07/evidence/TC-FR07-22_req.json`, `HW02/B_FR07/evidence/TC-FR07-22_res.json`
- TC-FR07-210: `HW02/B_FR07/evidence/TC-FR07-210_api.png`, `HW02/B_FR07/evidence/TC-FR07-210_req.json`, `HW02/B_FR07/evidence/TC-FR07-210_res.json`
</details>

## TC liên quan

- Fail (2): TC-FR07-22, TC-FR07-210
- Nhóm dữ kiện: G17 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-08.2:** Tổng tiền thanh toán được tính tự động từ giỏ hàng và không cho phép người dùng chỉnh sửa trực tiếp (README.md dòng 105) — căn cứ của B8.
- **API-CART:** GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ.
- **B8 (giả định):** B8 (giá do client gửi ở POST /api/cart) (SV chốt 2026-10-20): giá lấy từ CSDL, không tin giá client — lý do: FR-08.2 'tổng tiền được tính tự động từ giỏ hàng và không cho phép người dùng chỉnh sửa trực tiếp'. EC16 hợp lệ, oracle = giá CSDL.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G17: API · POST /api/cart với price khác giá CSDL → HTTP 200, GET lưu đúng price client gửi
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-22, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":1},{"id":4,"name":"Tai nghe AirPods Pro 2","price":1,"quantity":1}]
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295 (xem `bugs_facts.md`, G17)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
