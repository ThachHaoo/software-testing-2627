# BUG-30

- **ID:** BUG-30
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

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
