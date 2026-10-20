# BUG-41

- **ID:** BUG-41
- **Tiêu đề:** API POST /api/products không kiểm tra validation dữ liệu đầu vào, trả về HTTP 200 OK và tạo sản phẩm không hợp lệ khi truyền sai name, price hoặc category_id
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Client: Playwright 1.48.2 APIRequestContext (lượt 6); kiểm tái hiện bằng PowerShell 5.1 Invoke-WebRequest (7/7a)
- API POST http://localhost:3000/api/products
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.   

- Backend node server.js đang chạy bình thường ở cổng http://localhost:3000.   

- Người dùng/Client có khả năng gửi HTTP Request trực tiếp tới API endpoint POST /api/products (ví dụ sử dụng Postman, cURL hoặc Scripts).

## Các bước tái hiện

1. Thực hiện gửi request POST tới URL http://localhost:3000/api/products với các payload vi phạm dữ liệu theo một trong các trường hợp sau:

- Vi phạm trường name:
  + Chuỗi rỗng "" (TC-FR15-23, TC-FR15-84)
  + Chuỗi quá 255 ký tự (256 ký tự ở TC-FR15-100; 300 ký tự ở TC-FR15-24)
  + Chuỗi chỉ gồm khoảng trắng "   " (TC-FR15-25)
  + Truyền null (TC-FR15-26)
  + Truyền sai kiểu dữ liệu kiểu số 123 (TC-FR15-27)

- Vi phạm trường price:
  + Giá âm như -1000, -999999999999 (TC-FR15-28, TC-FR15-208)
  + Giá bằng 0 hoặc giá quá nhỏ bị underflow về 0 (TC-FR15-101, TC-FR15-214)
  + Truyền null (TC-FR15-29)
  + Truyền sai kiểu dữ liệu là chuỗi chữ "abc" hoặc chuỗi số "100000" (TC-FR15-30, TC-FR15-31)

- Vi phạm trường category_id:
  + Danh mục không tồn tại trong CSDL như 999 (TC-FR15-32)
  + Truyền null (TC-FR15-33)
  + Truyền sai kiểu dữ liệu là chuỗi chữ "abc" (TC-FR15-34)

2. Kiểm tra HTTP Status Code và Response nhận được từ Server.

3. Thực hiện gửi request GET /api/products để kiểm tra danh sách sản phẩm trong CSDL.

## Expected (trích SRS)

- Theo các yêu cầu FR-15.2, FR-15.3, FR-15.4 và các quy định C6, C9, C11, API phải kiểm tra validation chặt chẽ dữ liệu đầu vào ở tầng backend.

- Khi dữ liệu gửi lên bị thiếu, sai kiểu, vi phạm độ dài, là giá trị âm/0 hoặc chứa category_id không tồn tại, API phải từ chối request, trả về mã lỗi 4xx (Client Error) cùng phản hồi chứa thông tin lỗi (error).

- Hệ thống tuyệt đối không được chèn bản ghi hỏng/không hợp lệ nào vào CSDL.

## Actual

- Backend không kiểm tra validation bất kỳ trường dữ liệu nào, luôn trả về HTTP Status Code 200 OK cùng message {"message":"Product created","id": ...}.

- Tất cả các payload vi phạm (tên rỗng, tên quá 255 ký tự, tên null, giá âm, giá null, giá chuỗi, category_id không tồn tại,...) đều tạo thành công bản ghi mới và lưu trực tiếp vào CSDL.

- Số lượng bản ghi trong CSDL sau mỗi request tăng từ 5 lên 6.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-23_api.png`
- TC-FR15-23: `HW02/C_FR15/evidence/TC-FR15-23_req.json`, `HW02/C_FR15/evidence/TC-FR15-23_res.json`, `HW02/C_FR15/evidence/TC-FR15-23_api.png`
- TC-FR15-24: `HW02/C_FR15/evidence/TC-FR15-24_req.json`, `HW02/C_FR15/evidence/TC-FR15-24_res.json`, `HW02/C_FR15/evidence/TC-FR15-24_api.png`, `HW02/C_FR15/evidence/TC-FR15-24_failed.png`
- TC-FR15-25: `HW02/C_FR15/evidence/TC-FR15-25_req.json`, `HW02/C_FR15/evidence/TC-FR15-25_res.json`, `HW02/C_FR15/evidence/TC-FR15-25_api.png`
- TC-FR15-26: `HW02/C_FR15/evidence/TC-FR15-26_req.json`, `HW02/C_FR15/evidence/TC-FR15-26_res.json`, `HW02/C_FR15/evidence/TC-FR15-26_api.png`
- TC-FR15-27: `HW02/C_FR15/evidence/TC-FR15-27_req.json`, `HW02/C_FR15/evidence/TC-FR15-27_res.json`, `HW02/C_FR15/evidence/TC-FR15-27_api.png`
- TC-FR15-84: `HW02/C_FR15/evidence/TC-FR15-84_req.json`, `HW02/C_FR15/evidence/TC-FR15-84_res.json`, `HW02/C_FR15/evidence/TC-FR15-84_api.png`
- TC-FR15-100: `HW02/C_FR15/evidence/TC-FR15-100_req.json`, `HW02/C_FR15/evidence/TC-FR15-100_res.json`, `HW02/C_FR15/evidence/TC-FR15-100_api.png`, `HW02/C_FR15/evidence/TC-FR15-100_failed.png`
- TC-FR15-28: `HW02/C_FR15/evidence/TC-FR15-28_req.json`, `HW02/C_FR15/evidence/TC-FR15-28_res.json`, `HW02/C_FR15/evidence/TC-FR15-28_api.png`
- TC-FR15-29: `HW02/C_FR15/evidence/TC-FR15-29_req.json`, `HW02/C_FR15/evidence/TC-FR15-29_res.json`, `HW02/C_FR15/evidence/TC-FR15-29_api.png`
- TC-FR15-30: `HW02/C_FR15/evidence/TC-FR15-30_req.json`, `HW02/C_FR15/evidence/TC-FR15-30_res.json`, `HW02/C_FR15/evidence/TC-FR15-30_api.png`
- TC-FR15-31: `HW02/C_FR15/evidence/TC-FR15-31_req.json`, `HW02/C_FR15/evidence/TC-FR15-31_res.json`, `HW02/C_FR15/evidence/TC-FR15-31_api.png`
- TC-FR15-101: `HW02/C_FR15/evidence/TC-FR15-101_req.json`, `HW02/C_FR15/evidence/TC-FR15-101_res.json`, `HW02/C_FR15/evidence/TC-FR15-101_api.png`
- TC-FR15-208: `HW02/C_FR15/evidence/TC-FR15-208_req.json`, `HW02/C_FR15/evidence/TC-FR15-208_res.json`, `HW02/C_FR15/evidence/TC-FR15-208_api.png`
- TC-FR15-214: `HW02/C_FR15/evidence/TC-FR15-214_req.json`, `HW02/C_FR15/evidence/TC-FR15-214_res.json`, `HW02/C_FR15/evidence/TC-FR15-214_api.png`
- TC-FR15-32: `HW02/C_FR15/evidence/TC-FR15-32_req.json`, `HW02/C_FR15/evidence/TC-FR15-32_res.json`, `HW02/C_FR15/evidence/TC-FR15-32_api.png`
- TC-FR15-33: `HW02/C_FR15/evidence/TC-FR15-33_req.json`, `HW02/C_FR15/evidence/TC-FR15-33_res.json`, `HW02/C_FR15/evidence/TC-FR15-33_api.png`
- TC-FR15-34: `HW02/C_FR15/evidence/TC-FR15-34_req.json`, `HW02/C_FR15/evidence/TC-FR15-34_res.json`, `HW02/C_FR15/evidence/TC-FR15-34_api.png`

## TC liên quan

- Fail (17): TC-FR15-23, TC-FR15-24, TC-FR15-25, TC-FR15-26, TC-FR15-27, TC-FR15-84, TC-FR15-100, TC-FR15-28, TC-FR15-29, TC-FR15-30, TC-FR15-31, TC-FR15-101, TC-FR15-208, TC-FR15-214, TC-FR15-32, TC-FR15-33, TC-FR15-34
- Nhóm dữ kiện: G8 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-15.2:** (SRS) Tên sản phẩm: bắt buộc, tối đa 255 ký tự. — (name: 23, 24, 25, 26, 27, 84, 100)
- **FR-15.3:** (SRS) Giá: bắt buộc, phải là số dương (> 0). — (price: 28, 29, 30, 31, 101, 208, 214)
- **FR-15.4:** (SRS) Danh mục: bắt buộc, phải chọn từ danh sách có sẵn. — (category_id: 32, 33, 34)
- **C6 (giả định SV chốt):** (tầng API áp FR-15) API là tầng riêng, suite riêng: POST/PUT gọi trực tiếp với dữ liệu vi phạm FR-15.2–15.4 → 4xx (không 2xx, không 5xx) kèm trường error, không tạo/không đổi bản ghi; không cố định mã cụ thể.
- **C9 (giả định SV chốt):** (thiếu trường / sai kiểu ở API) name/price/category_id thiếu, null hoặc sai kiểu JSON (name là số; price là chuỗi — kể cả chuỗi số như "100000"; category_id là chuỗi chữ) → 4xx, không tạo/không đổi bản ghi. — (26, 27, 29, 30, 31, 33, 34)
- **C3 (giả định SV chốt):** (Tên – chuỗi chỉ gồm khoảng trắng) chuỗi chỉ gồm khoảng trắng coi như trống → bị từ chối; tách lớp riêng với chuỗi rỗng. — (25)
- **C11 (giả định SV chốt):** (Danh mục – 'danh sách có sẵn') danh sách có sẵn = các danh mục tồn tại trong bảng categories (GET /api/categories) tại thời điểm lưu. category_id không có trong danh sách hoặc thiếu → không hợp lệ. Quan sát (gray-box): ô chọn danh mục trên UI luôn có … — (32)
- **C23 (giả định SV chốt):** (giá cực nhỏ bị làm tròn về 0 khi parse) dùng ở TC-FR15-214. — (214)
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-23): `HTTP 200 {"message":"Product created","id":22}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 22, name "", price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-24): `HTTP 200 {"message":"Product created","id":23}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 23, name ""x"×300", price 1500000, category_id 2}` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
- Actual nguyên văn (TC-FR15-25): `HTTP 200 {"message":"Product created","id":24}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 24, name "   ", price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-26): `HTTP 200 {"message":"Product created","id":25}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 25, name null, price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-27): `HTTP 200 {"message":"Product created","id":26}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 26, name "123", price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-84): `HTTP 200 {"message":"Product created","id":81}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 81, name "", price 1500000, category_id 2}`
- Actual nguyên văn (TC-FR15-100): `HTTP 200 {"message":"Product created","id":87}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 87, name ""x"×256", price 1500000, category_id 2}` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
- Actual nguyên văn (TC-FR15-28): `HTTP 200 {"message":"Product created","id":27}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 27, name "SP API28 1792497292506", price -1000, category_id 2}`
- Actual nguyên văn (TC-FR15-29): `HTTP 200 {"message":"Product created","id":28}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 28, name "SP API29 1792497293415", price null, category_id 2}`
- Actual nguyên văn (TC-FR15-30): `HTTP 200 {"message":"Product created","id":29}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 29, name "SP API30 1792497294325", price "abc", category_id 2}`
- Actual nguyên văn (TC-FR15-31): `HTTP 200 {"message":"Product created","id":30}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 30, name "SP API31 1792497295222", price 100000, category_id 2}`
- Actual nguyên văn (TC-FR15-101): `HTTP 200 {"message":"Product created","id":88}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 88, name "SP BVA 101 1792497398040", price 0, category_id 2}`
- Actual nguyên văn (TC-FR15-208): `HTTP 200 {"message":"Product created","id":112}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 112, name "SP Giá Âm Cực Đại 1792497423262", price -999999999999, category_id 2}`
- Actual nguyên văn (TC-FR15-214): `HTTP 200 {"message":"Product created","id":114}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 114, name "SP Underflow Price 1792497426240", price 0, category_id 2}`
- Actual nguyên văn (TC-FR15-32): `HTTP 200 {"message":"Product created","id":31}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 31, name "SP API32 1792497296103", price 1500000, category_id 999}`
- Actual nguyên văn (TC-FR15-33): `HTTP 200 {"message":"Product created","id":32}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 32, name "SP API33 1792497297046", price 1500000, category_id null}`
- Actual nguyên văn (TC-FR15-34): `HTTP 200 {"message":"Product created","id":33}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 33, name "SP API34 1792497297969", price 1500000, category_id "abc"}`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 167–177

  ```js
   167  app.post("/api/products", (req, res) => {
   168    const { name, price, description, imageUrl, category_id } = req.body;
   169    db.run(
   170      "INSERT INTO products (name, price, description, imageUrl, category_id) VALUES (?, ?, ?, ?, ?)",
   171      [name, price, description, imageUrl, category_id],
   172      function (err) {
   173        if (err) return res.status(500).json({ error: err.message });
   174        res.json({ message: "Product created", id: this.lastID });
   175      },
   176    );
   177  });
  ```

### Nhận định

- Ở Backend (backend/server.js, dòng 167–177): Endpoint POST /api/products chỉ đơn thuần bóc tách req.body và đẩy thẳng các biến vào câu lệnh INSERT INTO products của SQLite mà không có bất cứ dòng code nào để validate kiểu dữ liệu, độ dài hay sự tồn tại của khóa ngoại category_id.

- Đây là lỗi rất nghiêm trọng ở tầng API Backend. Mặc dù ở Frontend có thể có một số bước chặn cơ bản, việc Backend hoàn toàn bỏ ngỏ validation sẽ cho phép kẻ gian bypass qua UI (dùng Postman, cURL, script) để bơm dữ liệu rác, phá hoại CSDL và gây sai lệch toàn bộ hệ thống.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
