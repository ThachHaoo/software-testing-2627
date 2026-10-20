# BUG-47

- **ID:** BUG-47
- **Tiêu đề:** Các API POST, PUT, DELETE /api/products hoàn toàn không có cơ chế xác thực JWT và phân quyền Admin, cho phép người dùng ẩn danh hoặc user thường thực hiện thêm, sửa, xóa sản phẩm
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Client: Playwright 1.48.2 APIRequestContext (lượt 6); kiểm tái hiện bằng PowerShell 5.1 Invoke-WebRequest (7/7a)
- API POST http://localhost:3000/api/products; PUT, DELETE http://localhost:3000/api/products/:id
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.

- Backend node server.js đang chạy bình thường ở cổng http://localhost:3000.

- Người dùng/Client có khả năng gửi HTTP Request trực tiếp tới các API endpoint POST /api/products, PUT /api/products/:id, DELETE /api/products/:id (ví dụ sử dụng Postman, cURL hoặc Scripts).

## Các bước tái hiện

1. Chuẩn bị các dạng Token/Header vi phạm để kiểm tra tính bảo mật của API:
  + Trường hợp 1: Không gửi Header Authorization (truy cập ẩn danh)
  + Trường hợp 2: Gửi Header Authorization với Token không hợp lệ / sai Chữ ký
  + Trường hợp 3: Gửi Header Authorization với Token JWT hợp lệ của tài khoản người dùng thông thường (role: 'user')

2. Lần lượt gửi request tới các API quản lý sản phẩm với một trong các dạng Token/Header vi phạm nêu trên:
  + Gửi request POST http://localhost:3000/api/products tạo sản phẩm mới (TC-FR15-50, TC-FR15-51, TC-FR15-52).
  + Gửi request PUT http://localhost:3000/api/products/:id sửa thông tin sản phẩm (TC-FR15-53, TC-FR15-54, TC-FR15-55).
  + Gửi request DELETE http://localhost:3000/api/products/:id xóa sản phẩm (TC-FR15-56, TC-FR15-57, TC-FR15-58).

3. Kiểm tra HTTP Status Code và nội dung Response Body trả về ở từng request.

4. Thực hiện gửi request GET /api/products để kiểm tra sự thay đổi dữ liệu trong CSDL.

## Expected (trích SRS)

- Theo yêu cầu FR-12.2, SEC-02, SEC-03 và quy định C5:
  + Các API thay đổi dữ liệu (POST, PUT, DELETE /api/products) bắt buộc phải yêu cầu xác thực Token JWT hợp lệ.
  + Phải kiểm tra phân quyền tài khoản, chỉ cho phép Token có role = 'admin' mới được thực hiện thao tác.

- Nếu không có Token hoặc Token không hợp lệ, API phải trả về lỗi 4xx (Ví dụ: 401 Unauthorized).

- Nếu Token thuộc tài khoản thường (role = 'user'), API phải từ chối truy cập và trả về lỗi 403 Forbidden.

- Dữ liệu trong CSDL không được phép thay đổi khi chưa được xác thực và phân quyền hợp lệ.

## Actual

- Tất cả các request POST, PUT, DELETE không truyền Token, truyền Token sai hoặc Token của user thường đều trả về HTTP Status Code 200 OK thành công.

- Dữ liệu trong CSDL bị thay đổi trực tiếp:
  + Request POST không Token/sai Token/user thường vẫn tạo thành công bản ghi mới trong CSDL.
  + Request PUT không Token/sai Token/user thường vẫn sửa thành công thông tin sản phẩm trong CSDL.
  + Request DELETE không Token/sai Token/user thường vẫn xóa vĩnh viễn sản phẩm khỏi CSDL.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-50_api.png`
- TC-FR15-50: `HW02/C_FR15/evidence/TC-FR15-50_req.json`, `HW02/C_FR15/evidence/TC-FR15-50_res.json`, `HW02/C_FR15/evidence/TC-FR15-50_api.png`
- TC-FR15-51: `HW02/C_FR15/evidence/TC-FR15-51_req.json`, `HW02/C_FR15/evidence/TC-FR15-51_res.json`, `HW02/C_FR15/evidence/TC-FR15-51_api.png`
- TC-FR15-52: `HW02/C_FR15/evidence/TC-FR15-52_req.json`, `HW02/C_FR15/evidence/TC-FR15-52_res.json`, `HW02/C_FR15/evidence/TC-FR15-52_api.png`
- TC-FR15-53: `HW02/C_FR15/evidence/TC-FR15-53_req.json`, `HW02/C_FR15/evidence/TC-FR15-53_res.json`, `HW02/C_FR15/evidence/TC-FR15-53_api.png`
- TC-FR15-54: `HW02/C_FR15/evidence/TC-FR15-54_req.json`, `HW02/C_FR15/evidence/TC-FR15-54_res.json`, `HW02/C_FR15/evidence/TC-FR15-54_api.png`
- TC-FR15-55: `HW02/C_FR15/evidence/TC-FR15-55_req.json`, `HW02/C_FR15/evidence/TC-FR15-55_res.json`, `HW02/C_FR15/evidence/TC-FR15-55_api.png`
- TC-FR15-56: `HW02/C_FR15/evidence/TC-FR15-56_req.json`, `HW02/C_FR15/evidence/TC-FR15-56_res.json`, `HW02/C_FR15/evidence/TC-FR15-56_api.png`
- TC-FR15-57: `HW02/C_FR15/evidence/TC-FR15-57_req.json`, `HW02/C_FR15/evidence/TC-FR15-57_res.json`, `HW02/C_FR15/evidence/TC-FR15-57_api.png`
- TC-FR15-58: `HW02/C_FR15/evidence/TC-FR15-58_req.json`, `HW02/C_FR15/evidence/TC-FR15-58_res.json`, `HW02/C_FR15/evidence/TC-FR15-58_api.png`

## TC liên quan

- Fail (9): TC-FR15-50, TC-FR15-51, TC-FR15-52, TC-FR15-53, TC-FR15-54, TC-FR15-55, TC-FR15-56, TC-FR15-57, TC-FR15-58
- Nhóm dữ kiện: G11 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-12.2:** (liên quan, C5) Các API có tính ảnh hưởng dữ liệu POST/PUT/DELETE /api/products phải yêu cầu (1) Token JWT hợp lệ, (2) role = 'admin' trong Token.
- **SEC-02:** (liên quan, C5) Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ (README.md dòng 279). — (thiếu/sai token: 50, 51, 53, 54, 56, 57)
- **SEC-03:** (liên quan, C5) API Admin phải kiểm tra role = 'admin' trong Token, không chỉ kiểm tra sự tồn tại của Token (README.md dòng 280). — (role user: 52, 55, 58)
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-50): `HTTP 200 {"message":"Product created","id":34}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 34, name "SP API50 1792497298877", price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-51): `HTTP 200 {"message":"Product created","id":35}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 35, name "SP API51 1792497299774", price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-52): `HTTP 200 {"message":"Product created","id":36}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 36, name "SP API52 1792497300678", price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-53): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 51, name "Muc tieu 53 1792497314256", price 1000000, category_id 1} → M_SAU {id 51, name "Sua API53 1792497314256", price 2500000, category_id 3}`
- Actual nguyên văn (TC-FR15-54): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 52, name "Muc tieu 54 1792497315170", price "1000000", category_id 1} → M_SAU {id 52, name "Sua API54 1792497315170", price "2500000", category_id 3}`
- Actual nguyên văn (TC-FR15-55): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 53, name "Muc tieu 55 1792497316069", price 1000000, category_id 1} → M_SAU {id 53, name "Sua API55 1792497316069", price 2500000, category_id 3}`
- Actual nguyên văn (TC-FR15-56): `HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 55, name "Muc tieu 56 1792497320087", price 1000000, category_id 1} → M_SAU HTTP 200 {}`
- Actual nguyên văn (TC-FR15-57): `HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 56, name "Muc tieu 57 1792497320980", price "1000000", category_id 1} → M_SAU HTTP 200 {}`
- Actual nguyên văn (TC-FR15-58): `HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 57, name "Muc tieu 58 1792497321894", price 1000000, category_id 1} → M_SAU HTTP 200 {}`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 100–110

  ```js
   100  const authenticateToken = (req, res, next) => {
   101    const authHeader = req.headers["authorization"];
   102    const token = authHeader && authHeader.split(" ")[1];
   103    if (token == null) return res.status(401).json({ error: "Unauthorized" });
   104  
   105    jwt.verify(token, SECRET_KEY, (err, user) => {
   106      if (err) return res.status(403).json({ error: "Forbidden" });
   107      req.user = user;
   108      next();
   109    });
   110  };
  ```
- Đoạn code trích nguyên văn: `backend/server.js` dòng 167

  ```js
   167  app.post("/api/products", (req, res) => {
  ```
- Đoạn code trích nguyên văn: `backend/server.js` dòng 179

  ```js
   179  app.put("/api/products/:id", (req, res) => {
  ```
- Đoạn code trích nguyên văn: `backend/server.js` dòng 191

  ```js
   191  app.delete("/api/products/:id", (req, res) => {
  ```

### Nhận định

- Ở Backend (backend/server.js): Mặc dù file server có định nghĩa sẵn middleware xác thực authenticateToken (dòng 100–110), nhưng tại các khai báo endpoint POST /api/products (dòng 167), PUT /api/products/:id (dòng 179) và DELETE /api/products/:id (dòng 191), dev lại không gắn middleware authenticateToken cũng như không có bất kỳ logic kiểm tra req.user.role === 'admin' nào.

- Đây là lỗi hổng bảo mật đặc biệt nghiêm trọng (Broken Access Control / Unauthenticated API access). Bất kỳ ai trên Internet (chưa kiểm chứng) cũng có thể gọi trực tiếp API để thêm, sửa, xóa dữ liệu sản phẩm trong CSDL hệ thống mà không cần đăng nhập hay có quyền Admin.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
