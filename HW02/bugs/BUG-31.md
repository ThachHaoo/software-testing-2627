# BUG-31

- **ID:** BUG-31
- **Tiêu đề:** Endpoint POST /api/cart tin tưởng hoàn toàn giá tiền do client gửi lên, cho phép ghi đè đơn giá sản phẩm trong giỏ thành 1đ
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

- Backend server đang chạy tại http://localhost:3000.

- Đã thực hiện đăng ký/đăng nhập tài khoản người dùng để lấy token xác thực (JWT token <T>).

- Sản phẩm có ID = 4 (Tai nghe AirPods Pro 2) có giá niêm yết chuẩn trong CSDL backend là 6.000.000 ₫.

## Các bước tái hiện

1. Đăng nhập lấy token:
```powershell
$loginRes = Invoke-RestMethod -Uri "http://localhost:3000/api/login" -Method Post -ContentType "application/json" -Body '{"email":"test@eshop.com","password":"Test1234!"}'
$token = $loginRes.token
$headers = @{ "Authorization" = "Bearer $token" }
```

2. Gửi request thêm sản phẩm (id: 4) nhưng cố tình chỉnh sửa field price thành 1 trong body JSON:
```powershell
$body = '{"id": 4, "name": "Tai nghe AirPods Pro 2", "price": 1, "quantity": 1}'
Invoke-RestMethod -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -ContentType "application/json" -Body $body
```

3.Kiểm tra giỏ hàng qua GET /api/cart:
```powershell
(Invoke-WebRequest -UseBasicParsing -Uri "http://localhost:3000/api/cart" -Headers $headers).Content
```

## Expected (trích SRS)

Theo yêu cầu FR-08.2 và giả định B8: Backend phải tự tra cứu và áp dụng giá sản phẩm chuẩn lưu trong CSDL server, tuyệt đối không tin tưởng field price do client gửi lên. Khi client gửi body có price: 1, backend phải bỏ qua field price này hoặc tự động thay bằng giá chuẩn 6000000, lưu vào giỏ hàng với giá 6000000.

## Actual

- Backend chấp nhận hoàn toàn payload do client gửi lên, trả về HTTP 200 {"message":"Added to cart"}.

- Khi gọi GET /api/cart, item mới được lưu vào giỏ hàng với đơn giá bị thao túng thành 1 ₫ ("price": 1):

```json
[
  {"id": 4, "name": "Tai nghe AirPods Pro 2", "price": 1, "quantity": 1}
]
```

(evidence TC-FR07-22 có thêm id 1, id 5 do bước dựng giỏ của test)

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-22_api.png`
- TC-FR07-22: `HW02/B_FR07/evidence/TC-FR07-22_api.png`, `HW02/B_FR07/evidence/TC-FR07-22_req.json`, `HW02/B_FR07/evidence/TC-FR07-22_res.json`
- TC-FR07-210: `HW02/B_FR07/evidence/TC-FR07-210_api.png`, `HW02/B_FR07/evidence/TC-FR07-210_req.json`, `HW02/B_FR07/evidence/TC-FR07-210_res.json`

## TC liên quan

- Fail (2): TC-FR07-22, TC-FR07-210
- Nhóm dữ kiện: G17 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-08.2:** Tổng tiền thanh toán được tính tự động từ giỏ hàng và không cho phép người dùng chỉnh sửa trực tiếp (README.md dòng 105) — căn cứ của B8.
- **B8 (giả định SV chốt):** (giá do client gửi ở POST /api/cart) (SV chốt 2026-10-20): giá lấy từ CSDL, không tin giá client — lý do: FR-08.2 'tổng tiền được tính tự động từ giỏ hàng và không cho phép người dùng chỉnh sửa trực tiếp'. EC16 hợp lệ, oracle = giá CSDL.
- Đạt trong cùng case: API-CART (HTTP 200, GET /api/cart trả mảng)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-22): `POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":1},{"id":4,"name":"Tai nghe AirPods Pro 2","price":1,"quantity":1}]`
- Payload (`TC-FR07-22_req.json`): headers `{"Content-Type": "application/json", "Authorization": "Bearer <T>"}`, body thô `{"id": 4, "name": "Tai nghe AirPods Pro 2", "price": 1, "quantity": 1}`; GET /api/cart TRƯỚC `[{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}, {"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": 1}]`
- Phản hồi (`TC-FR07-22_res.json`): HTTP 200, body `{"message":"Added to cart"}`
- GET /api/cart SAU (`TC-FR07-22_res.json`): HTTP 200, body `[{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":1},{"id":4,"name":"Tai nghe AirPods Pro 2","price":1,"quantity":1}]`
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
  [{"id":4,"name":"Tai nghe AirPods Pro 2","price":1,"quantity":1}]
  ```
- Output khớp mục Actual (phần tử id 4, price 1).
- `/api/checkout` có đọc `userCarts` không — trích nguyên văn `backend/server.js` dòng 297–309 (route chỉ lấy `total_amount`, `shipping_address` từ `req.body`; trong đoạn này không có `userCarts`):

  ```js
   297  app.post("/api/checkout", authenticateToken, (req, res) => {
   298    const userId = req.user.id;
   299    const { total_amount, shipping_address } = req.body;
   300  
   301    db.run(
   302      "INSERT INTO orders (user_id, total_amount, status, shipping_address) VALUES (?, ?, ?, ?)",
   303      [userId, total_amount, "pending", shipping_address],
   304      function (err) {
   305        if (err) return res.status(500).json({ error: err.message });
   306        res.json({ message: "Checkout successful", orderId: this.lastID });
   307      },
   308    );
   309  });
  ```
- Sửa bước tái hiện 2026-10-20: tài khoản `user@domain.com`/`Password123!` (không có trong seed) → `test@eshop.com`/`Test1234!` (README.md dòng 24; backend/database.js dòng 93); `$headers` bỏ `Content-Type`, các lệnh POST thêm `-ContentType "application/json"`; bước GET đổi sang `Invoke-WebRequest … .Content` để in JSON thô và thêm `-UseBasicParsing` (Windows PowerShell 5.1 báo `Object reference not set to an instance of an object.` khi thiếu). Khối JSON mục Actual rút còn phần tử id 4, thêm dòng ghi chú evidence TC-FR07-22.
- Client dùng /api/cart: không tìm thấy trong `frontend-mobile`, `frontend-admin`, `frontend-web` (grep "api/cart", bỏ node_modules; SUT @ de0f48f, 2026-10-20). Không có client nào đọc giá/quantity từ GET /api/cart. Hai client gọi `/api/checkout` gửi `items`, `total_amount` lấy từ giỏ state phía client: `frontend-web/src/pages/Checkout.jsx` dòng 45–48 (`axios.post('http://localhost:3000/api/checkout', { items: cart, total_amount: finalAmount, …`), `frontend-mobile/App.js` dòng 384–392 (`` fetch(`${API_URL}/checkout`, … body: JSON.stringify({ items: cart.length > 1 ? cart.slice(0, -1) : cart, total_amount: finalAmount, … ``).

### Nhận định

- Nguyên nhân: Trong backend/server.js (dòng 290–295), route POST /api/cart đẩy nguyên object req.body do client gửi lên vào mảng giỏ hàng bằng lệnh userCarts[userId].push(req.body) mà không thực hiện bất kỳ bước kiểm tra hay map lại dữ liệu với CSDL sản phẩm (products).

- Việc tin tưởng dữ liệu client (Trusting Client Input) tạo ra lỗ hổng bảo mật gian lận giá tiền (Price Tampering) cực kỳ nghiêm trọng, cho phép kẻ gian tự ý sửa đổi đơn giá sản phẩm trị giá hàng triệu đồng thành 1đ ngay ở tầng API trước khi thanh toán.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
