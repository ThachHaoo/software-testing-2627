# BUG-34

- **ID:** BUG-34
- **Tiêu đề:** Endpoint POST /api/cart khi nhận JSON không hợp lệ (Infinity) trả về trang lỗi HTML 400 kèm stack trace văng ra ngoài thay vì JSON chuẩn chứa trường
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/cart (backend)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon); TC-FR07-209 lấy từ lượt 3 (13:17), kết quả trùng lượt 2
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Backend server Express.js đang chạy tại http://localhost:3000.

- Đã thực hiện đăng ký/đăng nhập để lấy token xác thực JWT hợp lệ (<T>).

## Các bước tái hiện

1. Đăng nhập lấy token:
```powershell
$loginRes = Invoke-RestMethod -Uri "http://localhost:3000/api/login" -Method Post -ContentType "application/json" -Body '{"email":"user@domain.com","password":"Password123!"}'
$token = $loginRes.token
$headers = @{ "Authorization" = "Bearer $token"; "Content-Type" = "application/json" }
```

2. Gửi request POST /api/cart chứa giá trị quantity: Infinity trong chuỗi body JSON thô (JSON không hợp lệ vì chuẩn JSON không hỗ trợ Infinity):
```powershell
# Gửi chuỗi thô không chuẩn JSON
$bodyRaw = '{"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": Infinity}'
$response = Invoke-WebRequest -Uri "http://localhost:3000/api/cart" -Method Post -Headers $headers -Body $bodyRaw
```

3. Quan sát Content-Type và body trả về từ phản hồi của server.

## Expected (trích SRS)

Theo quy định thiết kế REST API (kèm giả định B17): Khi client gửi request có body JSON bị lỗi cú pháp (SyntaxError), backend Express phải bắt lỗi (catch error) và phản hồi bằng cấu trúc JSON nhất quán chứa trường error (ví dụ: {"error": "Invalid JSON format"}) kèm mã HTTP status 400 Bad Request. Server tuyệt đối không được trả về trang HTML mặc định hay để lộ thông tin vết mã nguồn (stack trace).

## Actual

- Backend trả về mã lỗi HTTP 400 Bad Request (đúng status code) và giỏ hàng không bị thay đổi.

- Tuy nhiên, định dạng phản hồi hoàn toàn không phải JSON mà văng ra nguyên một trang HTML mẫu mặc định của Express (<!DOCTYPE html>...<pre>SyntaxError: Unexpected token 'I'...</pre>), làm lộ chi tiết vết mã nguồn JSON.parse và thông tin nội bộ của server.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-209_api.png`
- TC-FR07-209: `HW02/B_FR07/evidence/TC-FR07-209_api.png`, `HW02/B_FR07/evidence/TC-FR07-209_req.json`, `HW02/B_FR07/evidence/TC-FR07-209_res.json`
- Bản che dùng cho issue: `HW02/bugs/_issue_redacted/BUG-34.txt`

## TC liên quan

- Fail (1): TC-FR07-209
- Nhóm dữ kiện: G20 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **B17 (giả định SV chốt):** (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106). — vi phạm ở: 4xx nhưng body là trang HTML, không có trường error
- Đạt trong cùng case: API-CART (body không phải JSON bị từ chối (400), giỏ không đổi)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-209): `POST HTTP 400 <!DOCTYPE html> ↵ <html lang="en"> ↵ <head> ↵ <meta charset="utf-8"> ↵ <title>Error</title> ↵ </head> ↵ <body> ↵ <pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot;uant; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]`
- Payload (`TC-FR07-209_req.json`): headers `{"Content-Type": "application/json", "Authorization": "Bearer <T>"}`, body thô `{"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": Infinity}`; GET /api/cart TRƯỚC `[{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}]`
- Phản hồi (`TC-FR07-209_res.json`): HTTP 400, body `<!DOCTYPE html> ↵ <html lang="en"> ↵ <head> ↵ <meta charset="utf-8"> ↵ <title>Error</title> ↵ </head> ↵ <body> ↵ <pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot;uantity&quot;: Infinity}&quot; is not valid JSON<br> &nbsp; &nbsp;at JSON.parse (&lt;anonymous&gt;)<br> &nbsp; &nbsp;at parse (<SU… (rút gọn)`
- GET /api/cart SAU (`TC-FR07-209_res.json`): HTTP 200, body `[{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]`
- Lượt 1 gửi sai body do script (Playwright tự JSON.stringify); lượt 2, 3 gửi đúng chuỗi thô — kết quả trùng nhau.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt); lượt 3 cũng giống.
- Đoạn code trích nguyên văn: `backend/server.js` dòng 12

  ```js
    12  app.use(bodyParser.json());
  ```
- Client dùng /api/cart: không tìm thấy trong `frontend-mobile`, `frontend-admin`, `frontend-web` (grep "api/cart", bỏ node_modules; SUT @ de0f48f, 2026-10-20). Không có client nào đọc giá/quantity từ GET /api/cart. Hai client gọi `/api/checkout` gửi `items`, `total_amount` lấy từ giỏ state phía client: `frontend-web/src/pages/Checkout.jsx` dòng 45–48 (`axios.post('http://localhost:3000/api/checkout', { items: cart, total_amount: finalAmount, …`), `frontend-mobile/App.js` dòng 384–392 (`` fetch(`${API_URL}/checkout`, … body: JSON.stringify({ items: cart.length > 1 ? cart.slice(0, -1) : cart, total_amount: finalAmount, … ``).

### Nhận định

- Nguyên nhân: Trong backend/server.js (dòng 12), ứng dụng sử dụng middleware app.use(bodyParser.json()) để parse dữ liệu JSON từ body request.

- Khi client gửi một chuỗi JSON không đúng định dạng chuẩn (ví dụ có chứa từ khóa Infinity), bodyParser.json() gặp lỗi trong quá trình JSON.parse và lập tức ném ra ngoại lệ SyntaxError.

- Do ứng dụng Express hoàn toàn không cài đặt custom Error Handling Middleware (hàm dạng app.use((err, req, res, next) => ...)), ngoại lệ này rơi vào bộ xử lý lỗi mặc định (Default Error Handler) của Express. Bộ xử lý mặc định này tự động sinh ra trang thông báo lỗi HTML kèm stack trace chi tiết thay vì trả về một đối tượng JSON chuẩn chứa cấu trúc {"error": ...} theo định dạng giao tiếp API chuẩn hóa ở B17.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
