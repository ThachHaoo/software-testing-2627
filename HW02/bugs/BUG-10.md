# BUG-10

- **ID:** BUG-10
- **Tiêu đề:** Gửi request POST /api/register với Content-Type: text/plain, văng lỗi HTTP 500 kèm trang HTML stack trace
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch sẽ. Payload chứa các thông tin name, email, password hợp lệ theo SRS.

## Các bước tái hiện

1. Chuẩn bị payload JSON hợp lệ:
   `{"name": "Lê Tấn Hiệp", "email": "hiep.sv15@domain.com", "password": "Hiep123$"}`
2. Gửi request `POST http://localhost:3000/api/register` nhưng cố tình chỉnh Header `Content-Type: text/plain` (thay vì `application/json`).

## Expected (trích SRS)

Theo spec `API-REG` và giả định A11, API chỉ nhận body định dạng JSON (`application/json`). Khi client gửi Header `Content-Type` không đúng kiểu (như `text/plain`), backend phải xử lý từ chối an toàn bằng mã lỗi client **HTTP 4xx** (ví dụ 400 Bad Request hoặc 415 Unsupported Media Type) kèm body JSON chứa trường `error`, tuyệt đối không được để sập server hay trả về lỗi 5xx.

## Actual

Server backend, trả về mã **HTTP 500 Internal Server Error** cùng nguyên cục trang HTML chứa lỗi code:
`<pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<br>…</pre>`

## Bằng chứng

- Ảnh tiêu biểu đính kèm GitHub Issue: `TC-FR01-214_api.png` 
- TC-FR01-214: `HW02/A_FR01/evidence/TC-FR01-214_req.json`, `HW02/A_FR01/evidence/TC-FR01-214_res.json`, `HW02/A_FR01/evidence/TC-FR01-214_api.png`

## TC liên quan

- Fail (1): TC-FR01-214
- Nhóm dữ kiện: G10 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **API-REG:** POST /api/register nhận body JSON {name, email, password}; thành công trả 200 {"message": "User registered successfully", "id": n} (api_specification.md dòng 14–21).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G10): `backend/server.js dòng 3–12`; `backend/server.js dòng 20–29`
- Body 500 (`TC-FR01-214_res.json`) có stack trace: 10 dòng `at ...`, dòng đầu `at D:\…\eshop-sut\backend\server.js:21:11`, kèm đường dẫn tuyệt đối trên máy chạy.
- Sau TC-FR01-214, test kế tiếp trong lượt chạy (TC-FR01-215, tầng UI, verdict Blocked theo A20, auto_status Fail) vẫn nhận phản hồi từ backend (fixture đăng nhập admin `POST /api/login` + `GET /api/admin/users` thành công, actual ghi `user mới=0`) → tiến trình backend không dừng.

### Nhận định

Có lẽ thiếu do middleware catch lỗi hoặc validate Content-Type:
- bodyParser.json() chỉ parse body khi Header là application/json. Khi gửi text/plain, middleware bỏ qua làm cho req.body bị undefined.

- Ở route handler dòng 21, code lại viết const { name, email, password } = req.body; (destructuring trực tiếp từ req.body).

- Vì req.body bị undefined nên JS quăng ra TypeError và do không có try-catch bọc lại nên Express tự động trả về trang lỗi HTML 500 mặc định.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
