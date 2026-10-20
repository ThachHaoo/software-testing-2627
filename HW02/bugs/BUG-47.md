# BUG-47

- **ID:** BUG-47
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Client: Playwright 1.48.2 APIRequestContext (lượt 6); kiểm tái hiện bằng PowerShell 5.1 Invoke-WebRequest (7/7a)
- API POST http://localhost:3000/api/products; PUT, DELETE http://localhost:3000/api/products/:id
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
