# BUG-32

- **ID:** BUG-32
- **Tiêu đề:** Endpoint POST /api/cart hoàn toàn thiếu validate payload, chấp nhận dữ liệu sai kiểu, id không tồn tại, quantity âm/thập phân/rỗng và lưu cả null khi gửi text/plain
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/cart (backend)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Backend server đang khởi chạy tại http://localhost:3000.

- Đã thực hiện đăng ký/đăng nhập tài khoản người dùng hợp lệ để lấy JWT Token (<T>).

## Các bước tái hiện

1. Đăng nhập lấy token:
```powershell
$loginRes = Invoke-RestMethod -Uri "http://localhost:3000/api/login" -Method Post -ContentType "application/json" -Body '{"email":"test@eshop.com","password":"Test1234!"}'
$token = $loginRes.token
$headers = @{ "Authorization" = "Bearer $token" }
```

2. Tái hiện nhóm G18 (quantity không hợp lệ - âm, thập phân, thiếu, sai kiểu):
```powershell
# Gửi quantity = -3
$body1 = '{"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": -3}'
Invoke-RestMethod -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -ContentType "application/json" -Body ([Text.Encoding]::UTF8.GetBytes($body1))
```

3. Tái hiện nhóm G19 (id không hợp lệ - id 99999 không tồn tại, sai kiểu):
```powershell
# Gửi id = 99999
$body2 = '{"id": 99999, "name": "Không tồn tại", "price": 1000, "quantity": 1}'
Invoke-RestMethod -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -ContentType "application/json" -Body ([Text.Encoding]::UTF8.GetBytes($body2))
```

4. Tái hiện nhóm G21 (Content-Type: text/plain):
```powershell
$body3 = '{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}'
Invoke-RestMethod -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -ContentType "text/plain" -Body ([Text.Encoding]::UTF8.GetBytes($body3))
```

5.Kiểm tra kết quả giỏ hàng bằng GET /api/cart:
```powershell
(Invoke-WebRequest -UseBasicParsing -Uri "http://localhost:3000/api/cart" -Headers $headers).Content
```

## Expected (trích SRS)

Theo quy định validate dữ liệu hệ thống (FR-06.2) và các giả định B17, B18:
- Backend API bắt buộc phải kiểm tra (validate) dữ liệu đầu vào trong body request của POST /api/cart.
- Trường id phải là số nguyên dương tương ứng với sản phẩm thực sự tồn tại trong CSDL server.
- Trường quantity phải là số nguyên dương >= 1.
- Bất kỳ request nào chứa id không tồn tại, quantity âm/thập phân/chuỗi/rỗng, hoặc gửi sai Content-Type dẫn đến body không parse được JSON đều phải bị từ chối với mã lỗi HTTP 4xx (ví dụ 400 Bad Request) kèm mô tả lỗi, tuyệt đối không được ghi dữ liệu rác vào giỏ hàng.

## Actual

- Với tất cả các trường hợp gửi payload lỗi ở nhóm G18 và G19, backend đều nhắm mắt trả về HTTP 200 {"message":"Added to cart"} và nhét nguyên các phần tử rác (quantity: -3, id: 99999,...) vào mảng giỏ hàng của user.

- Với nhóm G21 (gửi Content-Type: text/plain), backend vẫn trả về HTTP 200 {"message":"Added to cart"}, nhưng do bodyParser.json() không parse text/plain, req.body bị undefined. Kết quả là backend push(undefined) làm cho giỏ hàng xuất hiện một phần tử null ([null]) khi gọi GET /api/cart.

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
- Client dùng /api/cart: không tìm thấy trong `frontend-mobile`, `frontend-admin`, `frontend-web` (grep "api/cart", bỏ node_modules; SUT @ de0f48f, 2026-10-20). Không có client nào đọc giá/quantity từ GET /api/cart. Hai client gọi `/api/checkout` gửi `items`, `total_amount` lấy từ giỏ state phía client: `frontend-web/src/pages/Checkout.jsx` dòng 45–48 (`axios.post('http://localhost:3000/api/checkout', { items: cart, total_amount: finalAmount, …`), `frontend-mobile/App.js` dòng 384–392 (`` fetch(`${API_URL}/checkout`, … body: JSON.stringify({ items: cart.length > 1 ? cart.slice(0, -1) : cart, total_amount: finalAmount, … ``).
- AI chạy kiểm bước tái hiện 2026-10-20: restart backend (`node server.js`) ngay trước khi chạy; chạy đúng các khối PowerShell ở mục "Các bước tái hiện" bằng Windows PowerShell 5.1.26100. Output nguyên văn:

  ```text
  message
  -------
  Added to cart
  Added to cart
  Added to cart
  [{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":-3},{"id":99999,"name":"Không tồn tại","price":1000,"quantity":1},null]
  ```
- Output khớp mục Actual (phần tử quantity -3, phần tử id 99999, phần tử `null`).
- Sửa bước tái hiện 2026-10-20: tài khoản `user@domain.com`/`Password123!` → `test@eshop.com`/`Test1234!`; `$headers` chỉ còn `Authorization`; mọi POST có `-ContentType` và `-Body ([Text.Encoding]::UTF8.GetBytes(...))` (Windows PowerShell 5.1 mã hoá chuỗi -Body theo ISO-8859-1); GET đổi sang `(Invoke-WebRequest -UseBasicParsing … ).Content`. Bước 4 (G21): bỏ `$headersText`, đặt `-ContentType "text/plain"` ở tham số (không trong `-Headers`). Khối code mục Nhận định: ```jsx → ```js.

### Nhận định

- Nguyên nhân: Trong backend/server.js (dòng 290–295), route POST /api/cart hoàn toàn không có bất kỳ dòng code validation nào đối với req.body:
```js
app.post("/api/cart", authenticateToken, (req, res) => {
  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  userCarts[userId].push(req.body);
  res.json({ message: "Added to cart" });
});
```
Lệnh userCarts[userId].push(req.body) đẩy trực tiếp mọi dữ liệu client gửi lên vào giỏ hàng RAM mà không hề kiểm tra tính hợp lệ của id hay quantity.

- Với trường hợp Content-Type: text/plain (TC-214), middleware bodyParser.json() (dòng 12) bỏ qua không parse body, làm cho req.body nhận giá trị undefined. Hàm push(undefined) dẫn đến việc mảng giỏ hàng chứa phần tử null, gây ra phản hồi [null] bất hợp lý khi client gọi GET /api/cart.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
