# BUG-05

- **ID:** BUG-05
- **Tiêu đề:** Backend API POST /api/register cho phép đăng ký trùng email đã có trong CSDL (trùng y nguyên, trùng sau khi cắt khoảng trắng, hoặc trùng phần domain khác hoa/thường)
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch sẽ (đã có sẵn tài khoản seed `test@eshop.com`). Họ Tên và Mật khẩu trong payload chuẩn chỉnh theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi email đã tồn tại dưới mấy dạng này:
   - **Case 1 (trùng y nguyên):** `{"name": "Nguyen Van A", "email": "test@eshop.com", "password": "Abcd1234!"}`
   - **Case 2 (trùng sau khi cắt khoảng trắng):** `{"name": "Nguyen Van A", "email": " test@eshop.com ", "password": "Abcd1234!"}`
   - **Case 3 (trùng domain khác hoa/thường):** `{"name": "Lê Tấn Hiệp", "email": "test@ESHOP.COM", "password": "Hiep123$"}`

## Expected (trích SRS)

FR-01.4 chốt rõ: Email phải là duy nhất trong hệ thống. Nếu email đã dính với tài khoản khác (kể cả khi dính khoảng trắng đầu/cuối A3 hay viết hoa/thường phần domain theo RFC 5321), backend phải chặn ngay, trả HTTP 4xx kèm trường `error` (A11) và không tạo thêm user nào hết.

## Actual

API phớt lờ hết, vẫn báo **HTTP 200** `{"message":"User registered successfully","id": <id>}` và cho tạo ngon ơ 1 user mới trùng email trong CSDL.

## Bằng chứng

- Ảnh tiêu biểu đính kèm GitHub Issue: `TC-FR01-41_api.png`, `TC-FR01-206_api.png`
- TC-FR01-41: `HW02/A_FR01/evidence/TC-FR01-41_req.json`, `HW02/A_FR01/evidence/TC-FR01-41_res.json`, `HW02/A_FR01/evidence/TC-FR01-41_api.png`
- TC-FR01-42: `HW02/A_FR01/evidence/TC-FR01-42_req.json`, `HW02/A_FR01/evidence/TC-FR01-42_res.json`, `HW02/A_FR01/evidence/TC-FR01-42_api.png`
- TC-FR01-206: `HW02/A_FR01/evidence/TC-FR01-206_req.json`, `HW02/A_FR01/evidence/TC-FR01-206_res.json`, `HW02/A_FR01/evidence/TC-FR01-206_api.png`

## TC liên quan

- Fail (3): TC-FR01-41, TC-FR01-42, TC-FR01-206
- Nhóm dữ kiện: G4 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.4:** Email phải là duy nhất trong hệ thống.
- **A3** (giả định, SRS im lặng): A3 (Email – duy nhất): Email so sánh sau khi cắt khoảng trắng đầu/cuối; phần local phân biệt hoa/thường, phần domain không phân biệt (RFC 5321 §2.4). SV sửa ở bước 5.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G4): `backend/server.js dòng 20–29`; `backend/database.js dòng 50–54`

### Nhận định

- Dưới CSDL: Cột email trong bảng users (database.js) không được đặt ràng buộc UNIQUE.

- Trên Backend code: server.js không thèm chạy lệnh SELECT kiểm tra xem email có tồn tại chưa, mà cứ thế phang thẳng lệnh INSERT INTO.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
