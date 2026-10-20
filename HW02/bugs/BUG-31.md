# BUG-31

- **ID:** BUG-31
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

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
