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
<summary>Evidence từng TC (5)</summary>

- TC-FR07-36: `HW02/B_FR07/evidence/TC-FR07-36_api.png`, `HW02/B_FR07/evidence/TC-FR07-36_req.json`, `HW02/B_FR07/evidence/TC-FR07-36_res.json`
- TC-FR07-37: `HW02/B_FR07/evidence/TC-FR07-37_api.png`, `HW02/B_FR07/evidence/TC-FR07-37_req.json`, `HW02/B_FR07/evidence/TC-FR07-37_res.json`
- TC-FR07-40: `HW02/B_FR07/evidence/TC-FR07-40_api.png`, `HW02/B_FR07/evidence/TC-FR07-40_req.json`, `HW02/B_FR07/evidence/TC-FR07-40_res.json`
- TC-FR07-211: `HW02/B_FR07/evidence/TC-FR07-211_api.png`, `HW02/B_FR07/evidence/TC-FR07-211_req.json`, `HW02/B_FR07/evidence/TC-FR07-211_res.json`
- TC-FR07-212: `HW02/B_FR07/evidence/TC-FR07-212_api.png`, `HW02/B_FR07/evidence/TC-FR07-212_req.json`, `HW02/B_FR07/evidence/TC-FR07-212_res.json`
</details>

## TC liên quan

- Fail (5): TC-FR07-36, TC-FR07-37, TC-FR07-40, TC-FR07-211, TC-FR07-212
- Nhóm dữ kiện: G19 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **B18 (giả định):** B18 (sai kiểu / id không tồn tại ở API) (SV chốt 2026-10-20): giữ 5 lớp chỉ có ở tầng API — EC6, EC7 (quantity) và EC12, EC13, EC53 (id) — phải bị từ chối 4xx, giỏ không đổi. EC53 tách từ EC13 ở review bước 3.
- **B17 (giả định):** B17 (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).

- Đạt trong cùng case: API-CART (định dạng request/response của endpoint)
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G19: API · POST /api/cart với id không hợp lệ (không tồn tại, chuỗi, mảng, object, thiếu) → HTTP 200, GET có phần tử mới mang id đó
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-36, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":99999,"name":"Không tồn tại","price":1000,"quantity":1}]
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295 (xem `bugs_facts.md`, G19)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
