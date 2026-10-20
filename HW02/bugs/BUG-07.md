# BUG-07

- **ID:** BUG-07
- **Tiêu đề:** Backend API POST /api/register thả nổi kiểm tra Mật khẩu: yếu, ngắn, thiếu hoa/thường/số/ký tự đặc biệt, rỗng, thiếu trường hay sai kiểu đều cho tạo user
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch. Họ Tên và Email trong payload hợp lệ theo SRS, email chưa từng tồn tại.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi vi phạm trường Mật khẩu (FR-01.5 đến FR-01.8):
   - **Mật khẩu quá ngắn (7 ký tự):** `{"name": "Nguyen Van A", "email": "api43_1792424709996@domain.com", "password": "Abc12!x"}`
   - **Mật khẩu rỗng (`""`):** `{"name": "Nguyen Van A", "email": "api44_1792424711350@domain.com", "password": ""}`
   - **Thiếu chữ hoa:** `{"name": "Nguyen Van A", "email": "api45_1792424712692@domain.com", "password": "abcd1234!"}`
   - **Thiếu chữ thường:** `{"name": "Nguyen Van A", "email": "api47_1792424715601@domain.com", "password": "ABCD1234!"}`
   - **Thiếu chữ số:** `{"name": "Nguyen Van A", "email": "api49_1792424718358@domain.com", "password": "Abcdefgh!"}`
   - **Thiếu ký tự đặc biệt:** `{"name": "Nguyen Van A", "email": "api50_1792424719874@domain.com", "password": "Abcd12345"}`
   - **Ký tự đặc biệt ngoài tập cho phép (`#`):** `{"name": "Nguyen Van A", "email": "api51_1792424721327@domain.com", "password": "Abcd1234#"}`
   - **Chỉ dùng khoảng trắng làm ký tự đặc biệt:** `{"name": "Lê Tấn Hiệp", "email": "hiep.sv03@domain.com", "password": "Abcd 1234"}`
   - **Dùng ký tự full-width (`＄`):** `{"name": "Lê Tấn Hiệp", "email": "hiep.sv11@domain.com", "password": "Hiep123＄"}`
   - **Thiếu khoá `password`:** `{"name": "Nguyen Van A", "email": "api56_1792424728391@domain.com"}`
   - **Mật khẩu sai kiểu (số JSON):** `{"name": "Nguyen Van A", "email": "api57_1792424730378@domain.com", "password": 12345678}`

## Expected (trích SRS)

heo FR-01.5 tới FR-01.8, Mật khẩu là trường bắt buộc, dài tối thiểu 8 ký tự, phải có đủ chữ hoa, chữ thường, chữ số và ít nhất 1 ký tự đặc biệt thuộc tập `{@, $, !, %, *, ?, &}`. API backend phải validate dữ liệu (A9, A15), từ chối ngay các payload vi phạm bằng mã lỗi HTTP 4xx kèm trường `error` (A11) và tuyệt đối không tạo user.

## Actual

API phớt lờ toàn bộ luật mật khẩu, trả về **HTTP 200** `{"message":"User registered successfully","id": <id>}` và tạo thành công user mới trong CSDL cho cả 18 TC (11 dạng vi phạm liệt kê ở trên).

## Bằng chứng

- Ảnh tiêu biểu đính kèm GitHub Issue: `TC-FR01-43_api.png`, `TC-FR01-44_api.png`
- TC-FR01-43: `HW02/A_FR01/evidence/TC-FR01-43_req.json`, `HW02/A_FR01/evidence/TC-FR01-43_res.json`, `HW02/A_FR01/evidence/TC-FR01-43_api.png`
- TC-FR01-44: `HW02/A_FR01/evidence/TC-FR01-44_req.json`, `HW02/A_FR01/evidence/TC-FR01-44_res.json`, `HW02/A_FR01/evidence/TC-FR01-44_api.png`
- TC-FR01-45: `HW02/A_FR01/evidence/TC-FR01-45_req.json`, `HW02/A_FR01/evidence/TC-FR01-45_res.json`, `HW02/A_FR01/evidence/TC-FR01-45_api.png`
- TC-FR01-46: `HW02/A_FR01/evidence/TC-FR01-46_req.json`, `HW02/A_FR01/evidence/TC-FR01-46_res.json`, `HW02/A_FR01/evidence/TC-FR01-46_api.png`
- TC-FR01-47: `HW02/A_FR01/evidence/TC-FR01-47_req.json`, `HW02/A_FR01/evidence/TC-FR01-47_res.json`, `HW02/A_FR01/evidence/TC-FR01-47_api.png`
- TC-FR01-48: `HW02/A_FR01/evidence/TC-FR01-48_req.json`, `HW02/A_FR01/evidence/TC-FR01-48_res.json`, `HW02/A_FR01/evidence/TC-FR01-48_api.png`
- TC-FR01-49: `HW02/A_FR01/evidence/TC-FR01-49_req.json`, `HW02/A_FR01/evidence/TC-FR01-49_res.json`, `HW02/A_FR01/evidence/TC-FR01-49_api.png`
- TC-FR01-50: `HW02/A_FR01/evidence/TC-FR01-50_req.json`, `HW02/A_FR01/evidence/TC-FR01-50_res.json`, `HW02/A_FR01/evidence/TC-FR01-50_api.png`
- TC-FR01-51: `HW02/A_FR01/evidence/TC-FR01-51_req.json`, `HW02/A_FR01/evidence/TC-FR01-51_res.json`, `HW02/A_FR01/evidence/TC-FR01-51_api.png`
- TC-FR01-56: `HW02/A_FR01/evidence/TC-FR01-56_req.json`, `HW02/A_FR01/evidence/TC-FR01-56_res.json`, `HW02/A_FR01/evidence/TC-FR01-56_api.png`
- TC-FR01-57: `HW02/A_FR01/evidence/TC-FR01-57_req.json`, `HW02/A_FR01/evidence/TC-FR01-57_res.json`, `HW02/A_FR01/evidence/TC-FR01-57_api.png`
- TC-FR01-82: `HW02/A_FR01/evidence/TC-FR01-82_req.json`, `HW02/A_FR01/evidence/TC-FR01-82_res.json`, `HW02/A_FR01/evidence/TC-FR01-82_api.png`
- TC-FR01-86: `HW02/A_FR01/evidence/TC-FR01-86_req.json`, `HW02/A_FR01/evidence/TC-FR01-86_res.json`, `HW02/A_FR01/evidence/TC-FR01-86_api.png`
- TC-FR01-89: `HW02/A_FR01/evidence/TC-FR01-89_req.json`, `HW02/A_FR01/evidence/TC-FR01-89_res.json`, `HW02/A_FR01/evidence/TC-FR01-89_api.png`
- TC-FR01-102: `HW02/A_FR01/evidence/TC-FR01-102_req.json`, `HW02/A_FR01/evidence/TC-FR01-102_res.json`, `HW02/A_FR01/evidence/TC-FR01-102_api.png`
- TC-FR01-105: `HW02/A_FR01/evidence/TC-FR01-105_req.json`, `HW02/A_FR01/evidence/TC-FR01-105_res.json`, `HW02/A_FR01/evidence/TC-FR01-105_api.png`
- TC-FR01-224: `HW02/A_FR01/evidence/TC-FR01-224_req.json`, `HW02/A_FR01/evidence/TC-FR01-224_res.json`, `HW02/A_FR01/evidence/TC-FR01-224_api.png`
- TC-FR01-228: `HW02/A_FR01/evidence/TC-FR01-228_req.json`, `HW02/A_FR01/evidence/TC-FR01-228_res.json`, `HW02/A_FR01/evidence/TC-FR01-228_api.png`

## TC liên quan

- Fail (18): TC-FR01-43, TC-FR01-44, TC-FR01-45, TC-FR01-46, TC-FR01-47, TC-FR01-48, TC-FR01-49, TC-FR01-50, TC-FR01-51, TC-FR01-56, TC-FR01-57, TC-FR01-82, TC-FR01-86, TC-FR01-89, TC-FR01-102, TC-FR01-105, TC-FR01-224, TC-FR01-228
- Nhóm dữ kiện: G5 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.5:** Người dùng phải cung cấp Mật khẩu (trường bắt buộc).
- **FR-01.6:** Mật khẩu tối thiểu 8 ký tự.
- **FR-01.7a:** Mật khẩu có ít nhất 1 chữ hoa.
- **FR-01.7b:** Mật khẩu có ít nhất 1 chữ thường.
- **FR-01.7c:** Mật khẩu có ít nhất 1 chữ số.
- **FR-01.8:** Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &.
- **A5** (giả định, SRS im lặng): A5 (Mật khẩu – ký tự đặc biệt): hiểu danh sách (@, $, !, %, *, ?, &) là tập ĐÓNG: mật khẩu chỉ chứa ký tự đặc biệt ngoài tập này (ví dụ #, ^, -, khoảng trắng) bị coi là thiếu ký tự đặc biệt → bị từ chối. SRS không nói ký tự ngoài tập có được phép xuất hiện thêm hay không → giả định được phép nếu đã có ít nhất một ký tự trong tập.
- **A6** (giả định, SRS im lặng): A6 (Mật khẩu – chữ hoa/thường): giả định chỉ tính chữ Latin A–Z / a–z; chữ có dấu tiếng Việt (Ă, ê…) không tính là chữ hoa/thường. SRS im lặng. Expected của EC27/EC30 phụ thuộc giả định này; kết quả lệch được phân tích là SRS mơ hồ trước khi kết luận lỗi.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- **A15** (giả định, SRS im lặng): A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G5): `backend/server.js dòng 20–29`

### Nhận định

- Nguyên nhân giống như BUG-03, BUG-04 và BUG-05: Backend route /api/register hoàn toàn không có hàm hay regex nào để kiểm tra độ mạnh lẫn sự tồn tại của biến password.

- Mọi logic validate mật khẩu hiện tại chỉ nằm độc nhất ở Frontend (Register.jsx). Khi bị bypass UI, backend chấp nhận lưu mọi loại mật khẩu yếu, mật khẩu rỗng, thậm chí plaintext không đúng quy chuẩn vào CSDL. Điều này gây nguy cơ bảo mật nghiêm trọng cho toàn bộ hệ thống.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
