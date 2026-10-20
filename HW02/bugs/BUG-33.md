# BUG-33

- **ID:** BUG-33
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

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
