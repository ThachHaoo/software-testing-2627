# BUG-33

- **ID:** BUG-33
- **Tiêu đề:** Endpoint POST /api/cart bị tràn số khi gửi quantity vượt quá Number.MAX_SAFE_INTEGER, làm sai lệch giá trị số lượng lưu trong giỏ
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

- Đã đăng nhập lấy token xác thực JWT hợp lệ (<T>).

- Giỏ hàng của người dùng hiện đang trống ([]).

## Các bước tái hiện

1. Đăng nhập lấy token:
```powershell
$loginRes = Invoke-RestMethod -Uri "http://localhost:3000/api/login" -Method Post -ContentType "application/json" -Body '{"email":"test@eshop.com","password":"Test1234!"}'
$token = $loginRes.token
$headers = @{ "Authorization" = "Bearer $token" }
```

2. Gửi request POST /api/cart với quantity là số nguyên cực lớn 9007199254740993 (vượt 2^53 - 1):
```powershell
$body = '{"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": 9007199254740993}'
Invoke-RestMethod -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -ContentType "application/json" -Body ([Text.Encoding]::UTF8.GetBytes($body))
```

3. Kiểm tra dữ liệu giỏ hàng bằng GET /api/cart:
```powershell
(Invoke-WebRequest -UseBasicParsing -Uri "http://localhost:3000/api/cart" -Headers $headers).Content
```

## Expected (trích SRS)

Theo giả định B1 (không quy định cận trên cho số lượng): Hệ thống chấp nhận giá trị số lượng lớn hợp lệ do client gửi lên. Khi client gửi request chứa quantity: 9007199254740993, backend phải tiếp nhận và lưu trữ chính xác tuyệt đối con số 9007199254740993 trong giỏ hàng (hoặc nếu giới hạn độ rộng số nguyên thì phải có cơ chế validate chặn từ chối mã 4xx từ đầu).

## Actual

- Request POST /api/cart phản hồi HTTP 200 {"message":"Added to cart"}.

- Tuy nhiên, khi gọi GET /api/cart để kiểm tra, giá trị quantity trả về bị làm tròn / sai lệch thành 9007199254740992 (bị giảm mất 1 đơn vị so với 9007199254740993 đã gửi).

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-215_api.png`
- TC-FR07-215: `HW02/B_FR07/evidence/TC-FR07-215_api.png`, `HW02/B_FR07/evidence/TC-FR07-215_req.json`, `HW02/B_FR07/evidence/TC-FR07-215_res.json`

## TC liên quan

- Fail (1): TC-FR07-215
- Nhóm dữ kiện: G22 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **API-CART:** GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ. — vi phạm ở: GET trả quantity khác giá trị đã gửi
- Đạt trong cùng case: FR-06.2 (HTTP 2xx), B1 (giá trị lớn được nhận)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-215): `POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: []; SAU: [{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":9007199254740992}]`
- Payload (`TC-FR07-215_req.json`): headers `{"Content-Type": "application/json", "Authorization": "Bearer <T>"}`, body thô `{"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": 9007199254740993}`; GET /api/cart TRƯỚC `[]`
- Phản hồi (`TC-FR07-215_res.json`): HTTP 200, body `{"message":"Added to cart"}`
- GET /api/cart SAU (`TC-FR07-215_res.json`): HTTP 200, body `[{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":9007199254740992}]`
- SV ghi giả định B1 (không có cận trên) cho Expected của case.
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
  [{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":9007199254740992}]
  ```
- Output khớp mục Actual (quantity 9007199254740992).
- Sửa bước tái hiện 2026-10-20: tài khoản `user@domain.com`/`Password123!` → `test@eshop.com`/`Test1234!`; `$headers` chỉ còn `Authorization`; mọi POST có `-ContentType` và `-Body ([Text.Encoding]::UTF8.GetBytes(...))` (Windows PowerShell 5.1 mã hoá chuỗi -Body theo ISO-8859-1); GET đổi sang `(Invoke-WebRequest -UseBasicParsing … ).Content`.

### Nhận định

- Nguyên nhân: Trong JavaScript (Node.js backend runtime), kiểu dữ liệu Number tuân theo chuẩn IEEE 754 floating-point 64-bit, có giới hạn số nguyên an toàn tối đa là Number.MAX_SAFE_INTEGER (2^53 - 1 = 9007199254740991).
- Middleware bodyParser.json() (dòng 12) khi parse chuỗi JSON thô {"quantity": 9007199254740993} sang JS object đã tự động ép kiểu con số này về kiểu Number mặc định. Do vượt quá ngưỡng an toàn 2^53-1, giá trị bị mất độ chính xác (precision loss) và bị làm tròn thành 9007199254740992.
- Đoạn route POST /api/cart (dòng 290–295) hoàn toàn không kiểm tra ngưỡng giới hạn số nguyên hoặc validate ép kiểu BigInt/giới hạn quantity hợp lý trước khi lưu, làm sai lệch dữ liệu số lượng được lưu trữ trong giỏ.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
