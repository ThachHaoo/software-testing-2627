# BUG-33

- **ID:** BUG-33
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

- TC-FR07-215: `HW02/B_FR07/evidence/TC-FR07-215_api.png`, `HW02/B_FR07/evidence/TC-FR07-215_req.json`, `HW02/B_FR07/evidence/TC-FR07-215_res.json`
</details>

## TC liên quan

- Fail (1): TC-FR07-215
- Nhóm dữ kiện: G22 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **API-CART:** GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ. — vi phạm ở: GET trả quantity khác giá trị đã gửi

- Đạt trong cùng case: FR-06.2 (HTTP 2xx), B1 (giá trị lớn được nhận)
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G22: API · POST /api/cart quantity 9007199254740993 → HTTP 200, GET trả quantity 9007199254740992
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-215, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: []; SAU: [{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":9007199254740992}]
- SV ghi giả định B1 (không có cận trên) cho Expected của case.
- Đoạn code trích nguyên văn: `backend/server.js` dòng 12; `backend/server.js` dòng 290–295 (xem `_groups_B_FR07.md`, G22)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
