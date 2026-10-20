# BUG-44

- **ID:** BUG-44
- **Tiêu đề:** API POST /api/products bị lỗi server 500 (Unhandled Exception) và trả về trang HTML khi request thiếu Content-Type application/json làm req.body bị undefined
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

1. Thực hiện gửi request POST tới URL http://localhost:3000/api/products với payload bất kỳ nhưng cố tình không truyền Header Content-Type: application/json (TC-FR15-211).

2. Kiểm tra HTTP Status Code và Response Body trả về từ Server.

3. Thực hiện gửi request GET /api/products để kiểm tra lại dữ liệu trong CSDL.

## Expected (trích SRS)

- Theo các quy định C6 và C9, khi API nhận request thiếu Header Content-Type: application/json hoặc request không hợp lệ dẫn đến không parse được body, tầng API Backend phải xử lý an toàn và trả về mã lỗi 4xx (Client Error) cùng phản hồi định dạng JSON có chứa trường error.

- Server tuyệt đối không được crash hoặc quăng lỗi server 500 (Internal Server Error) ra giao diện HTML.

- Dữ liệu trong CSDL không được thay đổi.

## Actual

- Mặc dù dữ liệu CSDL không bị thay đổi, nhưng server đã quăng ra lỗi HTTP 500 Internal Server Error.

- Response body trả về là một trang HTML báo lỗi unhandled exception: TypeError: Cannot destructure property 'name' of 'req.body' as it is undefined..

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-211_api.png`
- TC-FR15-211: `HW02/C_FR15/evidence/TC-FR15-211_req.json`, `HW02/C_FR15/evidence/TC-FR15-211_res.json`, `HW02/C_FR15/evidence/TC-FR15-211_api.png`

## TC liên quan

- Fail (1): TC-FR15-211
- Nhóm dữ kiện: G14 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **C6 (giả định SV chốt):** (tầng API áp FR-15) API là tầng riêng, suite riêng: POST/PUT gọi trực tiếp với dữ liệu vi phạm FR-15.2–15.4 → 4xx (không 2xx, không 5xx) kèm trường error, không tạo/không đổi bản ghi; không cố định mã cụ thể. — (không 5xx; SV ghi căn cứ C6, C9)
- Đạt trong cùng case: Không tạo sản phẩm
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-211): `HTTP 500 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<; bản ghi TRƯỚC → SAU: 5 → 5`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 11–12

  ```js
    11  app.use(cors());
    12  app.use(bodyParser.json());
  ```
- Đoạn code trích nguyên văn: `backend/server.js` dòng 167–168

  ```js
   167  app.post("/api/products", (req, res) => {
   168    const { name, price, description, imageUrl, category_id } = req.body;
  ```

### Nhận định

- Ở Backend (backend/server.js, dòng 11–12 và dòng 167–168): Express app sử dụng bodyParser.json(). Khi request không gửi kèm header Content-Type: application/json, middleware này không parse body và để req.body thành undefined.

- Ngay sau đó tại handler của endpoint POST /api/products, code lại thực hiện destructuring trực tiếp const { name, price, description, imageUrl, category_id } = req.body; mà không kiểm tra if (!req.body) trước.

- Việc destructuring một biến undefined khiến Node.js ném ra ngoại lệ TypeError, làm crash luồng xử lý của request và nhảy vào Error Handler mặc định của Express, dẫn tới việc trả về lỗi HTTP 500 kèm giao diện trang HTML cho client.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
