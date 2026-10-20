# BUG-32

- **ID:** BUG-32
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
<summary>Evidence từng TC (8)</summary>

- TC-FR07-30: `HW02/B_FR07/evidence/TC-FR07-30_api.png`, `HW02/B_FR07/evidence/TC-FR07-30_req.json`, `HW02/B_FR07/evidence/TC-FR07-30_res.json`
- TC-FR07-31: `HW02/B_FR07/evidence/TC-FR07-31_api.png`, `HW02/B_FR07/evidence/TC-FR07-31_req.json`, `HW02/B_FR07/evidence/TC-FR07-31_res.json`
- TC-FR07-32: `HW02/B_FR07/evidence/TC-FR07-32_api.png`, `HW02/B_FR07/evidence/TC-FR07-32_req.json`, `HW02/B_FR07/evidence/TC-FR07-32_res.json`
- TC-FR07-33: `HW02/B_FR07/evidence/TC-FR07-33_api.png`, `HW02/B_FR07/evidence/TC-FR07-33_req.json`, `HW02/B_FR07/evidence/TC-FR07-33_res.json`
- TC-FR07-34: `HW02/B_FR07/evidence/TC-FR07-34_api.png`, `HW02/B_FR07/evidence/TC-FR07-34_req.json`, `HW02/B_FR07/evidence/TC-FR07-34_res.json`
- TC-FR07-35: `HW02/B_FR07/evidence/TC-FR07-35_api.png`, `HW02/B_FR07/evidence/TC-FR07-35_req.json`, `HW02/B_FR07/evidence/TC-FR07-35_res.json`
- TC-FR07-70: `HW02/B_FR07/evidence/TC-FR07-70_api.png`, `HW02/B_FR07/evidence/TC-FR07-70_req.json`, `HW02/B_FR07/evidence/TC-FR07-70_res.json`
- TC-FR07-208: `HW02/B_FR07/evidence/TC-FR07-208_api.png`, `HW02/B_FR07/evidence/TC-FR07-208_req.json`, `HW02/B_FR07/evidence/TC-FR07-208_res.json`
</details>

## TC liên quan

- Fail (8): TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-70, TC-FR07-208
- Nhóm dữ kiện: G18 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-06.2:** (B6 SV chốt) Trang chi tiết có ô nhập Số lượng, chỉ nhận số nguyên dương, tối thiểu là 1.
- **API-CART:** GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G18: API · POST /api/cart với quantity không hợp lệ (≤ 0, thập phân, chuỗi, thiếu) → HTTP 200, GET có phần tử mới mang quantity đó
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-30, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":-3}]
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295 (xem `bugs_facts.md`, G18)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
