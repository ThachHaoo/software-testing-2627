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

### G18 — API · POST /api/cart với quantity không hợp lệ (≤ 0, thập phân, chuỗi, thiếu) → HTTP 200, GET có phần tử mới mang quantity đó

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

### G19 — API · POST /api/cart với id không hợp lệ (không tồn tại, chuỗi, mảng, object, thiếu) → HTTP 200, GET có phần tử mới mang id đó

<details>
<summary>Evidence từng TC (5)</summary>

- TC-FR07-36: `HW02/B_FR07/evidence/TC-FR07-36_api.png`, `HW02/B_FR07/evidence/TC-FR07-36_req.json`, `HW02/B_FR07/evidence/TC-FR07-36_res.json`
- TC-FR07-37: `HW02/B_FR07/evidence/TC-FR07-37_api.png`, `HW02/B_FR07/evidence/TC-FR07-37_req.json`, `HW02/B_FR07/evidence/TC-FR07-37_res.json`
- TC-FR07-40: `HW02/B_FR07/evidence/TC-FR07-40_api.png`, `HW02/B_FR07/evidence/TC-FR07-40_req.json`, `HW02/B_FR07/evidence/TC-FR07-40_res.json`
- TC-FR07-211: `HW02/B_FR07/evidence/TC-FR07-211_api.png`, `HW02/B_FR07/evidence/TC-FR07-211_req.json`, `HW02/B_FR07/evidence/TC-FR07-211_res.json`
- TC-FR07-212: `HW02/B_FR07/evidence/TC-FR07-212_api.png`, `HW02/B_FR07/evidence/TC-FR07-212_req.json`, `HW02/B_FR07/evidence/TC-FR07-212_res.json`
</details>

### G21 — API · POST /api/cart với Content-Type: text/plain (body JSON hợp lệ) → HTTP 200, GET có phần tử null

<details>
<summary>Evidence từng TC (1)</summary>

- TC-FR07-214: `HW02/B_FR07/evidence/TC-FR07-214_api.png`, `HW02/B_FR07/evidence/TC-FR07-214_req.json`, `HW02/B_FR07/evidence/TC-FR07-214_res.json`
</details>

## TC liên quan

- G18 — Fail (8): TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-70, TC-FR07-208
- G19 — Fail (5): TC-FR07-36, TC-FR07-37, TC-FR07-40, TC-FR07-211, TC-FR07-212
- G21 — Fail (1): TC-FR07-214
- Nhóm dữ kiện: G18 + G19 + G21 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

### G18 — API · POST /api/cart với quantity không hợp lệ (≤ 0, thập phân, chuỗi, thiếu) → HTTP 200, GET có phần tử mới mang quantity đó

- **FR-06.2:** (B6 SV chốt) Trang chi tiết có ô nhập Số lượng, chỉ nhận số nguyên dương, tối thiểu là 1.
- **B17 (giả định):** B17 (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).
- **B18 (giả định):** B18 (sai kiểu / id không tồn tại ở API) (SV chốt 2026-10-20): giữ 5 lớp chỉ có ở tầng API — EC6, EC7 (quantity) và EC12, EC13, EC53 (id) — phải bị từ chối 4xx, giỏ không đổi. EC53 tách từ EC13 ở review bước 3. — vi phạm ở: TC-34, TC-35

- Đạt trong cùng case: API-CART (định dạng request/response của endpoint)
- Chưa đánh giá được trong cùng case: —

### G19 — API · POST /api/cart với id không hợp lệ (không tồn tại, chuỗi, mảng, object, thiếu) → HTTP 200, GET có phần tử mới mang id đó

- **B18 (giả định):** B18 (sai kiểu / id không tồn tại ở API) (SV chốt 2026-10-20): giữ 5 lớp chỉ có ở tầng API — EC6, EC7 (quantity) và EC12, EC13, EC53 (id) — phải bị từ chối 4xx, giỏ không đổi. EC53 tách từ EC13 ở review bước 3.
- **B17 (giả định):** B17 (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).

- Đạt trong cùng case: API-CART (định dạng request/response của endpoint)
- Chưa đánh giá được trong cùng case: —

### G21 — API · POST /api/cart với Content-Type: text/plain (body JSON hợp lệ) → HTTP 200, GET có phần tử null

- **API-CART:** GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ.
- **B17 (giả định):** B17 (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).

- Đạt trong cùng case: —
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

#### G18 — API · POST /api/cart với quantity không hợp lệ (≤ 0, thập phân, chuỗi, thiếu) → HTTP 200, GET có phần tử mới mang quantity đó

- Triệu chứng nhóm G18: API · POST /api/cart với quantity không hợp lệ (≤ 0, thập phân, chuỗi, thiếu) → HTTP 200, GET có phần tử mới mang quantity đó
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-30, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":-3}]
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295 (xem `_groups_B_FR07.md`, G18)

#### G19 — API · POST /api/cart với id không hợp lệ (không tồn tại, chuỗi, mảng, object, thiếu) → HTTP 200, GET có phần tử mới mang id đó

- Triệu chứng nhóm G19: API · POST /api/cart với id không hợp lệ (không tồn tại, chuỗi, mảng, object, thiếu) → HTTP 200, GET có phần tử mới mang id đó
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-36, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":99999,"name":"Không tồn tại","price":1000,"quantity":1}]
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295 (xem `_groups_B_FR07.md`, G19)

#### G21 — API · POST /api/cart với Content-Type: text/plain (body JSON hợp lệ) → HTTP 200, GET có phần tử null

- Triệu chứng nhóm G21: API · POST /api/cart với Content-Type: text/plain (body JSON hợp lệ) → HTTP 200, GET có phần tử null
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-214, nguyên văn): POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: []; SAU: [null]
- Đoạn code trích nguyên văn: `backend/server.js` dòng 12; `backend/server.js` dòng 290–295 (xem `_groups_B_FR07.md`, G21)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
