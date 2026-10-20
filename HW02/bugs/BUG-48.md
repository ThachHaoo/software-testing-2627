# BUG-48

- **ID:** BUG-48
- **Tiêu đề:** API GET /api/products/:id trả về trường price dạng chuỗi (String) thay vì kiểu số (Number) đối với các sản phẩm có id là số chẵn
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Client: Playwright 1.48.2 APIRequestContext (lượt 6); kiểm tái hiện bằng PowerShell 5.1 Invoke-WebRequest (7/7a)
- API GET http://localhost:3000/api/products/:id
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.

- Backend node server.js đang chạy bình thường ở cổng http://localhost:3000.

- Người dùng/Client có khả năng gửi HTTP Request trực tiếp tới API endpoint GET /api/products/:id (ví dụ sử dụng Postman, cURL hoặc Scripts).

## Các bước tái hiện

1. Chọn một sản phẩm có :id là số chẵn trong CSDL (ví dụ sản phẩm Samsung Galaxy S24 Ultra có id = 2).

2. Thực hiện gửi request GET tới URL http://localhost:3000/api/products/2 (TC-FR15-22).

3. Kiểm tra HTTP Status Code, Response Body và kiểu dữ liệu của trường price nhận được từ Server.

## Expected (trích SRS)

- Theo quy định C15, trong phản hồi JSON của API GET /api/products/:id, trường price phải luôn có kiểu dữ liệu là số (Number, ví dụ: "price": 28000000).

- Giá trị price trả về dạng chuỗi (như "price": "28000000") là không hợp lệ và không đúng thiết kế chuẩn API.

## Actual

- Response body trả về HTTP Status Code 200 OK.

- Tuy nhiên, đối với sản phẩm có id = 2 (số chẵn), trường price trong JSON phản hồi bị chuyển thành kiểu chuỗi: {"id":2, "name":"Samsung Galaxy S24 Ultra", "price":"28000000", ...}.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-22_api.png`
- TC-FR15-22: `HW02/C_FR15/evidence/TC-FR15-22_req.json`, `HW02/C_FR15/evidence/TC-FR15-22_res.json`, `HW02/C_FR15/evidence/TC-FR15-22_api.png`

## TC liên quan

- Fail (1): TC-FR15-22
- Nhóm dữ kiện: G12 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **C15 (giả định SV chốt):** (kiểu dữ liệu price trong phản hồi GET) price trong phản hồi GET /api/products/:id phải là số JSON; price dạng chuỗi (kể cả chuỗi số) lệch Expected. Kiểu dữ liệu price chỉ khẳng định ở EC59; EC56/EC57 so price theo giá trị số.
- Đạt trong cùng case: name, category_id đúng giá trị seed
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-22): `HTTP 200 {"id":2,"name":"Samsung Galaxy S24 Ultra","price":"28000000","description":"Màn hình hiển thị xuất sắc, camera siêu zoom","imageUrl":"https://placehold.co/300x300/png?text=Samsung+S24","category_id":1; bản ghi TRƯỚC → SAU: 5 → 5`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 159–165

  ```js
   159  app.get("/api/products/:id", (req, res) => {
   160    db.get("SELECT * FROM products WHERE id = ?", [req.params.id], (err, row) => {
   161      if (!row) return res.status(200).json({});
   162      if (row.id % 2 === 0) row.price = row.price.toString();
   163      res.json(row);
   164    });
   165  });
  ```

### Nhận định

- Ở Backend (backend/server.js, dòng 159–165): Trong handler của endpoint GET /api/products/:id, code cố tình chứa câu lệnh ép kiểu không hợp lý ở dòng 162: if (row.id % 2 === 0) row.price = row.price.toString();.

- Logic này khiến tất cả các sản phẩm có id chẵn bị ép kiểu giá tiền từ số thành chuỗi trước khi trả về client.

- Việc trả về không đồng nhất kiểu dữ liệu (id lẻ là Number, id chẵn là String) gây ra lỗi không nhất quán dữ liệu API (Data Inconsistency), có thể khiến các ứng dụng Client (Mobile/Frontend) bị crash hoặc tính toán toán học sai khi parse JSON.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
