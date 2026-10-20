# BUG-03

- **ID:** BUG-03
- **Tiêu đề:** Backend API POST /api/register không kiểm tra Họ Tên (name rỗng, chỉ khoảng trắng, null, thiếu trường, sai kiểu) vẫn trả HTTP 200 và tạo user
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

Backend vừa khởi động lại, CSDL được seed sạch. Email trong payload là không trùng và mật khẩu hợp lệ theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi Họ Tên bị vi phạm (trường bắt buộc):
   - **Case 1 (rỗng):** `{"name": "", "email": "api32_1792424694242@domain.com", "password": "Abcd1234!"}`
   - **Case 2 (chỉ khoảng trắng):** `{"name": "   ", "email": "api33_1792424695658@domain.com", "password": "Abcd1234!"}`
   - **Case 3 (thiếu khoá name):** `{"email": "api52_1792424722608@domain.com", "password": "Abcd1234!"}`
   - **Case 4 (sai kiểu - số JSON):** `{"name": 123, "email": "api53_1792424724118@domain.com", "password": "Abcd1234!"}`
   - **Case 5 (LB-1 - 0 ký tự):** `{"name": "", "email": "bvapi79_1792424861193@domain.com", "password": "Abcd1234!"}`

## Expected (trích SRS)

FR-01.1 quy định Họ Tên là trường bắt buộc. Tầng API phải chặn dữ liệu không hợp lệ (A9, A15), từ chối request với mã lỗi HTTP 4xx kèm trường `error` trong body JSON (A11) và không tạo user mới trong CSDL.

## Actual

API đều trả lời **HTTP 200** `{"message":"User registered successfully","id": <id>}` và tạo thành công user mới trong CSDL với Họ Tên bị trống/null/chuỗi khoảng trắng/số.

## Bằng chứng

- Ảnh tiêu biểu đính kèm GitHub Issue: `TC-FR01-32_api.png`, `TC-FR01-52_api.png`
- TC-FR01-32: `HW02/A_FR01/evidence/TC-FR01-32_req.json`, `HW02/A_FR01/evidence/TC-FR01-32_res.json`, `HW02/A_FR01/evidence/TC-FR01-32_api.png`
- TC-FR01-33: `HW02/A_FR01/evidence/TC-FR01-33_req.json`, `HW02/A_FR01/evidence/TC-FR01-33_res.json`, `HW02/A_FR01/evidence/TC-FR01-33_api.png`
- TC-FR01-52: `HW02/A_FR01/evidence/TC-FR01-52_req.json`, `HW02/A_FR01/evidence/TC-FR01-52_res.json`, `HW02/A_FR01/evidence/TC-FR01-52_api.png`
- TC-FR01-53: `HW02/A_FR01/evidence/TC-FR01-53_req.json`, `HW02/A_FR01/evidence/TC-FR01-53_res.json`, `HW02/A_FR01/evidence/TC-FR01-53_api.png`
- TC-FR01-79: `HW02/A_FR01/evidence/TC-FR01-79_req.json`, `HW02/A_FR01/evidence/TC-FR01-79_res.json`, `HW02/A_FR01/evidence/TC-FR01-79_api.png`

## TC liên quan

- Fail (5): TC-FR01-32, TC-FR01-33, TC-FR01-52, TC-FR01-53, TC-FR01-79
- Nhóm dữ kiện: G2 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.1:** Người dùng phải cung cấp Họ Tên (trường bắt buộc).
- **A1** (giả định, SRS im lặng): A1 (Họ Tên): FR-01 chỉ nói 'phải cung cấp'. SRS không nêu độ dài tối thiểu/tối đa hay tập ký tự → chỉ coi 'rỗng' là không hợp lệ. Chuỗi chỉ gồm khoảng trắng: giả định bị coi như rỗng (bị từ chối). Không có cận trên → không sinh UB/MAX_UI cho Họ Tên trừ khi SV quyết định khác.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- **A15** (giả định, SRS im lặng): A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G2): `backend/server.js dòng 20–29`

### Nhận định

- Lỗi nằm ở Backend handler của route /api/register. Code backend nhận req.body rồi thực hiện INSERT INTO users trực tiếp vào SQLite mà hoàn toàn không thực hiện bất kỳ câu lệnh validate dữ liệu đầu vào nào cho biến name (không check null, undefined, empty string hay type).

- Vì backend không validate, nếu người dùng bỏ qua giao diện Frontend và gọi trực tiếp API (qua Postman, curl hay script), hệ thống sẽ vô tư tạo các tài khoản rác với Họ Tên bị trống hoặc null trong CSDL.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
