# BUG-32

- **ID:** BUG-32
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/cart (backend)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-30_api.png`

### G18 — API · POST /api/cart với quantity không hợp lệ (≤ 0, thập phân, chuỗi, thiếu) → HTTP 200, GET có phần tử mới mang quantity đó

- Ảnh tiêu biểu nhóm: `TC-FR07-30_api.png`
- TC-FR07-30: `HW02/B_FR07/evidence/TC-FR07-30_api.png`, `HW02/B_FR07/evidence/TC-FR07-30_req.json`, `HW02/B_FR07/evidence/TC-FR07-30_res.json`
- TC-FR07-31: `HW02/B_FR07/evidence/TC-FR07-31_api.png`, `HW02/B_FR07/evidence/TC-FR07-31_req.json`, `HW02/B_FR07/evidence/TC-FR07-31_res.json`
- TC-FR07-32: `HW02/B_FR07/evidence/TC-FR07-32_api.png`, `HW02/B_FR07/evidence/TC-FR07-32_req.json`, `HW02/B_FR07/evidence/TC-FR07-32_res.json`
- TC-FR07-33: `HW02/B_FR07/evidence/TC-FR07-33_api.png`, `HW02/B_FR07/evidence/TC-FR07-33_req.json`, `HW02/B_FR07/evidence/TC-FR07-33_res.json`
- TC-FR07-34: `HW02/B_FR07/evidence/TC-FR07-34_api.png`, `HW02/B_FR07/evidence/TC-FR07-34_req.json`, `HW02/B_FR07/evidence/TC-FR07-34_res.json`
- TC-FR07-35: `HW02/B_FR07/evidence/TC-FR07-35_api.png`, `HW02/B_FR07/evidence/TC-FR07-35_req.json`, `HW02/B_FR07/evidence/TC-FR07-35_res.json`
- TC-FR07-70: `HW02/B_FR07/evidence/TC-FR07-70_api.png`, `HW02/B_FR07/evidence/TC-FR07-70_req.json`, `HW02/B_FR07/evidence/TC-FR07-70_res.json`
- TC-FR07-208: `HW02/B_FR07/evidence/TC-FR07-208_api.png`, `HW02/B_FR07/evidence/TC-FR07-208_req.json`, `HW02/B_FR07/evidence/TC-FR07-208_res.json`

### G19 — API · POST /api/cart với id không hợp lệ (không tồn tại, chuỗi, mảng, object, thiếu) → HTTP 200, GET có phần tử mới mang id đó

- Ảnh tiêu biểu nhóm: `TC-FR07-36_api.png`
- TC-FR07-36: `HW02/B_FR07/evidence/TC-FR07-36_api.png`, `HW02/B_FR07/evidence/TC-FR07-36_req.json`, `HW02/B_FR07/evidence/TC-FR07-36_res.json`
- TC-FR07-37: `HW02/B_FR07/evidence/TC-FR07-37_api.png`, `HW02/B_FR07/evidence/TC-FR07-37_req.json`, `HW02/B_FR07/evidence/TC-FR07-37_res.json`
- TC-FR07-40: `HW02/B_FR07/evidence/TC-FR07-40_api.png`, `HW02/B_FR07/evidence/TC-FR07-40_req.json`, `HW02/B_FR07/evidence/TC-FR07-40_res.json`
- TC-FR07-211: `HW02/B_FR07/evidence/TC-FR07-211_api.png`, `HW02/B_FR07/evidence/TC-FR07-211_req.json`, `HW02/B_FR07/evidence/TC-FR07-211_res.json`
- TC-FR07-212: `HW02/B_FR07/evidence/TC-FR07-212_api.png`, `HW02/B_FR07/evidence/TC-FR07-212_req.json`, `HW02/B_FR07/evidence/TC-FR07-212_res.json`

### G21 — API · POST /api/cart với Content-Type: text/plain (body JSON hợp lệ) → HTTP 200, GET có phần tử null

- Ảnh tiêu biểu nhóm: `TC-FR07-214_api.png`
- TC-FR07-214: `HW02/B_FR07/evidence/TC-FR07-214_api.png`, `HW02/B_FR07/evidence/TC-FR07-214_req.json`, `HW02/B_FR07/evidence/TC-FR07-214_res.json`

## TC liên quan

- G18 — Fail (8): TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-70, TC-FR07-208
- G19 — Fail (5): TC-FR07-36, TC-FR07-37, TC-FR07-40, TC-FR07-211, TC-FR07-212
- G21 — Fail (1): TC-FR07-214
- Nhóm dữ kiện: G18 + G19 + G21 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

### G18

- **FR-06.2:** (B6 SV chốt) Trang chi tiết có ô nhập Số lượng, chỉ nhận số nguyên dương, tối thiểu là 1.
- **B17 (giả định SV chốt):** (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).
- **B18 (giả định SV chốt):** (sai kiểu / id không tồn tại ở API) (SV chốt 2026-10-20): giữ 5 lớp chỉ có ở tầng API — EC6, EC7 (quantity) và EC12, EC13, EC53 (id) — phải bị từ chối 4xx, giỏ không đổi. EC53 tách từ EC13 ở review bước 3. — vi phạm ở: TC-34, TC-35
- Đạt trong cùng case: API-CART (định dạng request/response của endpoint)
- Chưa đánh giá được: —

### G19

- **B18 (giả định SV chốt):** (sai kiểu / id không tồn tại ở API) (SV chốt 2026-10-20): giữ 5 lớp chỉ có ở tầng API — EC6, EC7 (quantity) và EC12, EC13, EC53 (id) — phải bị từ chối 4xx, giỏ không đổi. EC53 tách từ EC13 ở review bước 3.
- **B17 (giả định SV chốt):** (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).
- Đạt trong cùng case: API-CART (định dạng request/response của endpoint)
- Chưa đánh giá được: —

### G21

- **API-CART:** GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ.
- **B17 (giả định SV chốt):** (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

#### G18

- Actual nguyên văn (TC-FR07-30): `POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":-3}]`
- Payload (`TC-FR07-30_req.json`): headers `{"Content-Type": "application/json", "Authorization": "Bearer <T>"}`, body thô `{"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": -3}`; GET /api/cart TRƯỚC `[{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}]`
- Phản hồi (`TC-FR07-30_res.json`): HTTP 200, body `{"message":"Added to cart"}`
- GET /api/cart SAU (`TC-FR07-30_res.json`): HTTP 200, body `[{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":-3}]`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295

  ```js
   290  app.post("/api/cart", authenticateToken, (req, res) => {
   291    const userId = req.user.id;
   292    if (!userCarts[userId]) userCarts[userId] = [];
   293    userCarts[userId].push(req.body);
   294    res.json({ message: "Added to cart" });
   295  });
  ```

#### G19

- Actual nguyên văn (TC-FR07-36): `POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":99999,"name":"Không tồn tại","price":1000,"quantity":1}]`
- Payload (`TC-FR07-36_req.json`): headers `{"Content-Type": "application/json", "Authorization": "Bearer <T>"}`, body thô `{"id": 99999, "name": "Không tồn tại", "price": 1000, "quantity": 1}`; GET /api/cart TRƯỚC `[{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}]`
- Phản hồi (`TC-FR07-36_res.json`): HTTP 200, body `{"message":"Added to cart"}`
- GET /api/cart SAU (`TC-FR07-36_res.json`): HTTP 200, body `[{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":99999,"name":"Không tồn tại","price":1000,"quantity":1}]`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295

  ```js
   290  app.post("/api/cart", authenticateToken, (req, res) => {
   291    const userId = req.user.id;
   292    if (!userCarts[userId]) userCarts[userId] = [];
   293    userCarts[userId].push(req.body);
   294    res.json({ message: "Added to cart" });
   295  });
  ```

#### G21

- Actual nguyên văn (TC-FR07-214): `POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: []; SAU: [null]`
- Payload (`TC-FR07-214_req.json`): headers `{"Content-Type": "text/plain", "Authorization": "Bearer <T>"}`, body thô `{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}`; GET /api/cart TRƯỚC `[]`
- Phản hồi (`TC-FR07-214_res.json`): HTTP 200, body `{"message":"Added to cart"}`
- GET /api/cart SAU (`TC-FR07-214_res.json`): HTTP 200, body `[null]`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 12

  ```js
    12  app.use(bodyParser.json());
  ```

- Đoạn code trích nguyên văn: `backend/server.js` dòng 290–295

  ```js
   290  app.post("/api/cart", authenticateToken, (req, res) => {
   291    const userId = req.user.id;
   292    if (!userCarts[userId]) userCarts[userId] = [];
   293    userCarts[userId].push(req.body);
   294    res.json({ message: "Added to cart" });
   295  });
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
