# BUG-30

- **ID:** BUG-30
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

- TC-FR07-21: `HW02/B_FR07/evidence/TC-FR07-21_api.png`, `HW02/B_FR07/evidence/TC-FR07-21_req.json`, `HW02/B_FR07/evidence/TC-FR07-21_res.json`
</details>

## TC liên quan

- Fail (1): TC-FR07-21
- Blocked ghi case gốc (1): TC-FR07-213
- Nhóm dữ kiện: G16 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-07.3:** Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.
- **API-CART:** GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G16: API · POST /api/cart cùng id đã có trong giỏ → HTTP 200, GET có thêm phần tử mới thay vì cộng quantity
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-21, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1}]; SAU: [{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1},{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":3}]
- TC-FR07-213: 50 POST song song → 50×HTTP 200, GET SAU 50 phần tử id 1 quantity 1 (Blocked, case gốc TC-FR07-21).
- Tầng UI cùng dạng quan sát: nhóm 'bấm 20 lần → 20 dòng' (TC-FR07-201).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295 (xem `bugs_facts.md`, G16)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
