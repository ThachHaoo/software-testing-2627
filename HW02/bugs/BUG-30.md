# BUG-30

- **ID:** BUG-30
- **Tiêu đề:** Endpoint POST /api/cart không cộng dồn số lượng khi gửi cùng sản phẩm mà push thêm phần tử mới vào giỏ
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

- Backend server đang chạy ở http://localhost:3000.

- Đã thực hiện đăng ký/đăng nhập tài khoản người dùng để lấy token xác thực (JWT token <T>).

- Giỏ hàng của người dùng trên server đã có sẵn 1 sản phẩm (ví dụ: Samsung Galaxy S24 Ultra, id: 2, quantity: 1).

## Các bước tái hiện

1. Đăng nhập lấy token:
```powershell
$loginRes = Invoke-RestMethod -Uri "http://localhost:3000/api/login" -Method Post -ContentType "application/json" -Body '{"email":"test@eshop.com","password":"Test1234!"}'
$token = $loginRes.token
$headers = @{ "Authorization" = "Bearer $token" }
```

2. Thêm sản phẩm id 2 với quantity 1 để dựng giỏ ban đầu:
```powershell
$body = '{"id": 2, "name": "Samsung Galaxy S24 Ultra", "price": 28000000, "quantity": 1}'
Invoke-RestMethod -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -ContentType "application/json" -Body $body
```

3. Gửi request thêm sản phẩm cùng ID (id: 2) vào giỏ
```powershell
$body = '{"id": 2, "name": "Samsung Galaxy S24 Ultra", "price": 28000000, "quantity": 3}'
Invoke-RestMethod -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -ContentType "application/json" -Body $body
```

4. Kiểm tra trạng thái giỏ hàng sau khi thêm
```powershell
(Invoke-WebRequest -UseBasicParsing -Uri "http://localhost:3000/api/cart" -Headers $headers).Content
```

## Expected (trích SRS)

Theo yêu cầu FR-07.3: Khi thêm một sản phẩm đã tồn tại trong giỏ hàng (cùng id), backend API phải tìm sản phẩm đó trong giỏ và thực hiện cộng dồn số lượng (quantity = 1 + 3 = 4), giữ nguyên giỏ hàng gồm 1 phần tử có quantity: 4.

## Actual

- Request POST /api/cart trả về HTTP 200 {"message":"Added to cart"}.

- Tuy nhiên, khi gọi GET /api/cart, backend trả về mảng gồm 2 phần tử riêng biệt cho cùng một sản phẩm id: 2:

```json
[
  {"id": 2, "name": "Samsung Galaxy S24 Ultra", "price": 28000000, "quantity": 1},
  {"id": 2, "name": "Samsung Galaxy S24 Ultra", "price": 28000000, "quantity": 3}
]
```

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-21_api.png`
- TC-FR07-21: `HW02/B_FR07/evidence/TC-FR07-21_api.png`, `HW02/B_FR07/evidence/TC-FR07-21_req.json`, `HW02/B_FR07/evidence/TC-FR07-21_res.json`

## TC liên quan

- Fail (1): TC-FR07-21
- Blocked ghi case gốc (1): TC-FR07-213
- Nhóm dữ kiện: G16 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.3:** Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.
- Đạt trong cùng case: API-CART (HTTP 200, GET /api/cart trả mảng)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-21): `POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1}]; SAU: [{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1},{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":3}]`
- Payload (`TC-FR07-21_req.json`): headers `{"Content-Type": "application/json", "Authorization": "Bearer <T>"}`, body thô `{"id": 2, "name": "Samsung Galaxy S24 Ultra", "price": 28000000, "quantity": 3}`; GET /api/cart TRƯỚC `[{"id": 2, "name": "Samsung Galaxy S24 Ultra", "price": 28000000, "quantity": 1}]`
- Phản hồi (`TC-FR07-21_res.json`): HTTP 200, body `{"message":"Added to cart"}`
- GET /api/cart SAU (`TC-FR07-21_res.json`): HTTP 200, body `[{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1},{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":3}]`
- Các case Blocked ghi case gốc: TC-FR07-21 (A20).
- TC-FR07-213: 50 POST song song → 50×HTTP 200, GET SAU 50 phần tử id 1 quantity 1 (Blocked, case gốc TC-FR07-21).
- Tầng UI cùng dạng quan sát: nhóm 'bấm 20 lần → 20 dòng' (TC-FR07-201).
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
- `/api/login` (dùng ở bước 1), trích nguyên văn:
  - `api_specification.md` dòng 23–32:

  ```
    23  ### 1.2 Đăng nhập
    24  - **Endpoint:** `POST /api/login`
    25  - **Body (JSON):**
    26    ```json
    27    {
    28      "email": "test@domain.com",
    29      "password": "Password123!"
    30    }
    31    ```
    32  - **Phản hồi thành công (200 OK):** Trả về chuỗi JWT `token` và thông tin `user`.
  ```

  - `backend/server.js` dòng 32–33 và 51–52 (tên trường body `email`, `password`; phản hồi có trường `token`):

  ```js
    32  app.post("/api/login", (req, res) => {
    33    const { email, password } = req.body;
    51        const token = jwt.sign({ id: user.id, role: user.role }, SECRET_KEY);
    52        res.json({ message: "Login successful", token, user });
  ```
- AI chạy kiểm bước tái hiện 2026-10-20: restart backend (`node server.js`) ngay trước khi chạy; chạy đúng các khối PowerShell ở mục "Các bước tái hiện" bằng Windows PowerShell 5.1.26100 (`powershell.exe -File`). Output nguyên văn:

  ```text
  message      
  -------      
  Added to cart
  Added to cart
  [{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1},{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":3}]
  ```
- Output khớp mục Actual (2 phần tử id 2, quantity 1 và 3).
- Sửa bước tái hiện 2026-10-20: tài khoản `user@domain.com`/`Password123!` (không có trong seed) → `test@eshop.com`/`Test1234!` (README.md dòng 24; backend/database.js dòng 93); `$headers` bỏ `Content-Type`, các lệnh POST thêm `-ContentType "application/json"`; bước GET đổi sang `Invoke-WebRequest … .Content` để in JSON thô và thêm `-UseBasicParsing` (Windows PowerShell 5.1 báo `Object reference not set to an instance of an object.` khi thiếu). Thêm bước 2 (POST id 2 quantity 1) để dựng giỏ ban đầu; đánh số lại bước 3, 4. Khối code mục Nhận định: ```jsx → ```js.
- Client dùng /api/cart: không tìm thấy trong `frontend-mobile`, `frontend-admin`, `frontend-web` (grep "api/cart", bỏ node_modules; SUT @ de0f48f, 2026-10-20). Không có client nào đọc giá/quantity từ GET /api/cart. Hai client gọi `/api/checkout` gửi `items`, `total_amount` lấy từ giỏ state phía client: `frontend-web/src/pages/Checkout.jsx` dòng 45–48 (`axios.post('http://localhost:3000/api/checkout', { items: cart, total_amount: finalAmount, …`), `frontend-mobile/App.js` dòng 384–392 (`` fetch(`${API_URL}/checkout`, … body: JSON.stringify({ items: cart.length > 1 ? cart.slice(0, -1) : cart, total_amount: finalAmount, … ``).

### Nhận định

- Nguyên nhân: Trong backend/server.js (dòng 290–295), route POST /api/cart xử lý lưu trữ giỏ hàng cực kỳ ngây thơ:

```js
app.post("/api/cart", authenticateToken, (req, res) => {
  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  userCarts[userId].push(req.body);
  res.json({ message: "Added to cart" });
});
```

- Backend dùng lệnh push(req.body) để đẩy trực tiếp payload request vào mảng userCarts[userId] mà không có bất kỳ logic kiểm tra xem item.id đã tồn tại trong mảng giỏ hàng hay chưa.

- Logic này khiến giỏ hàng ở tầng API bị nhân bản phần tử cùng ID trùng hệt như lỗi ở tầng Frontend UI (BUG-17), vi phạm trực tiếp yêu cầu gộp/cộng dồn số lượng sản phẩm ở FR-07.3.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
