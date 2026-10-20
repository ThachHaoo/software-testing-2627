# BUG-43

- **ID:** BUG-43
- **Tiêu đề:** API POST /api/products trả về phản hồi lỗi dạng HTML thay vì JSON khi nhận payload chứa giá trị không đúng chuẩn JSON (như Infinity)
- **Severity:** Medium
- **Priority:** Medium

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

1. Thực hiện gửi request POST tới URL http://localhost:3000/api/products với body chứa giá trị không hợp lệ theo chuẩn JSON RFC 8259, cụ thể là truyền "price": Infinity (TC-FR15-209).

2. Kiểm tra HTTP Status Code, Header Content-Type và Response Body nhận được từ Server.

3. Thực hiện gửi request GET /api/products để kiểm tra lại dữ liệu trong CSDL.

## Expected (trích SRS)

- Theo quy định C20 (dựa trên chuẩn JSON RFC 8259 và C6), khi API nhận request chứa dữ liệu không đúng chuẩn JSON (như Infinity, NaN), hệ thống phải trả về phản hồi chuẩn dạng JSON với mã lỗi 4xx.

- Response body phải mang định dạng JSON có chứa thông tin báo lỗi (ví dụ {"error": ...}).

- Dữ liệu trong CSDL không được thay đổi.

## Actual

- Mặc dù CSDL không bị thay đổi và server trả về mã HTTP Status 400, nhưng nội dung Response Body trả về lại là một trang HTML tĩnh chứa thẻ <pre> hiển thị lỗi SyntaxError: Unexpected token 'I' ... do middleware mặc định sinh ra.

- API trả về chuỗi HTML thay vì cấu trúc JSON đồng nhất theo chuẩn thiết kế REST API.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-209_api.png`
- TC-FR15-209: `HW02/C_FR15/evidence/TC-FR15-209_req.json`, `HW02/C_FR15/evidence/TC-FR15-209_res.json`, `HW02/C_FR15/evidence/TC-FR15-209_api.png`
- Bản che dùng cho issue: `HW02/bugs/_issue_redacted/TC-FR15-209_api_redacted.png`, `HW02/bugs/_issue_redacted/BUG-43.txt`

## TC liên quan

- Fail (1): TC-FR15-209
- Nhóm dữ kiện: G13 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **C20 (giả định SV chốt):** (Xử lý các giá trị không hợp lệ của chuẩn JSON) C20 (Xử lý các giá trị không hợp lệ của chuẩn JSON): loại: quyết định Expected, truy vết: có, căn cứ: RFC 8259, C6. Phù hợp với B17/BUG-34: Khi nhận request chứa giá trị không đúng chuẩn JSON (như `Infinity`, `NaN`), bac…
- Đạt trong cùng case: Dữ liệu không đổi
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-209): `HTTP 400 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot; &quot;price&quot;: Infinity, &quot;... is n; bản ghi TRƯỚC → SAU: 5 → 5`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 11–12

  ```js
    11  app.use(cors());
    12  app.use(bodyParser.json());
  ```

### Nhận định

- Ở Backend (backend/server.js, dòng 11–12): Express app chỉ sử dụng bodyParser.json() mà không cấu hình Custom Error Handler Middleware cho việc parse JSON lỗi.

- Khi bodyParser.json() bắt gặp một giá trị không hợp lệ chuẩn JSON như Infinity, nó tự động throw SyntaxError và đẩy thẳng ra Error Handler mặc định của Express. Handler mặc định này render lỗi ra một trang HTML web.

- Việc trả về trang HTML khi client gọi REST API làm gãy cấu trúc giao tiếp hệ thống, gây ra lỗi parse JSON phía Client (như các ứng dụng frontend hoặc ứng dụng mobile kỳ vọng nhận JSON response) (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/189

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
