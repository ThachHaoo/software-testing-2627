# BUG-04

- **ID:** BUG-04
- **Tiêu đề:** Backend API POST /api/register không kiểm tra Email (rỗng, sai định dạng, thiếu trường, sai kiểu) vẫn trả HTTP 200 và tạo user
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

Backend vừa khởi động lại, CSDL được seed sạch. Họ Tên và Mật khẩu trong payload hợp lệ theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi vi phạm trường Email (bắt buộc & định dạng hợp lệ):
   - **Case 1 (rỗng):** `{"name": "Nguyen Van A", "email": "", "password": "Abcd1234!"}`
   - **Case 2 (thiếu '@'):** `{"name": "Nguyen Van A", "email": "dom35_1792424698374domain.com", "password": "Abcd1234!"}`
   - **Case 3 (nhiều '@'):** `{"name": "Nguyen Van A", "email": "dom36@x_1792424699665@domain.com", "password": "Abcd1234!"}`
   - **Case 4 (thiếu local):** `{"name": "Nguyen Van A", "email": "@dom1792424701038.com", "password": "Abcd1234!"}`
   - **Case 5 (thiếu domain):** `{"name": "Nguyen Van A", "email": "dom38_1792424702726@", "password": "Abcd1234!"}`
   - **Case 6 (domain thiếu dấu chấm):** `{"name": "Nguyen Van A", "email": "dom39_1792424704059@domain", "password": "Abcd1234!"}`
   - **Case 7 (khoảng trắng ở giữa):** `{"name": "Nguyen Van A", "email": "dom 40_1792424705518@domain.com", "password": "Abcd1234!"}`
   - **Case 8 (thiếu khoá email):** `{"name": "Nguyen Van A", "password": "Abcd1234!"}`
   - **Case 9 (sai kiểu - số JSON):** `{"name": "Nguyen Van A", "email": 123, "password": "Abcd1234!"}`
   - **Case 10 (body rỗng {}):** `{}`

## Expected (trích SRS)

FR-01.2 và FR-01.3 yêu cầu Email là trường bắt buộc và phải đúng định dạng (`user@domain.com`). Tầng API kiểm tra dữ liệu đầu vào (A9, A15), từ chối request không hợp lệ bằng mã lỗi HTTP 4xx kèm trường `error` trong body JSON (A11) và không tạo tài khoản mới.

## Actual

API đều trả về **HTTP 200** `{"message":"User registered successfully","id": <id>}` và tạo thành công user mới trong CSDL với Email bị trống/null/chuỗi sai định dạng/số.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-34_api.png`, `TC-FR01-35_api.png`
- TC-FR01-34: `HW02/A_FR01/evidence/TC-FR01-34_req.json`, `HW02/A_FR01/evidence/TC-FR01-34_res.json`, `HW02/A_FR01/evidence/TC-FR01-34_api.png`
- TC-FR01-35: `HW02/A_FR01/evidence/TC-FR01-35_req.json`, `HW02/A_FR01/evidence/TC-FR01-35_res.json`, `HW02/A_FR01/evidence/TC-FR01-35_api.png`
- TC-FR01-36: `HW02/A_FR01/evidence/TC-FR01-36_req.json`, `HW02/A_FR01/evidence/TC-FR01-36_res.json`, `HW02/A_FR01/evidence/TC-FR01-36_api.png`
- TC-FR01-37: `HW02/A_FR01/evidence/TC-FR01-37_req.json`, `HW02/A_FR01/evidence/TC-FR01-37_res.json`, `HW02/A_FR01/evidence/TC-FR01-37_api.png`
- TC-FR01-38: `HW02/A_FR01/evidence/TC-FR01-38_req.json`, `HW02/A_FR01/evidence/TC-FR01-38_res.json`, `HW02/A_FR01/evidence/TC-FR01-38_api.png`
- TC-FR01-39: `HW02/A_FR01/evidence/TC-FR01-39_req.json`, `HW02/A_FR01/evidence/TC-FR01-39_res.json`, `HW02/A_FR01/evidence/TC-FR01-39_api.png`
- TC-FR01-40: `HW02/A_FR01/evidence/TC-FR01-40_req.json`, `HW02/A_FR01/evidence/TC-FR01-40_res.json`, `HW02/A_FR01/evidence/TC-FR01-40_api.png`
- TC-FR01-54: `HW02/A_FR01/evidence/TC-FR01-54_req.json`, `HW02/A_FR01/evidence/TC-FR01-54_res.json`, `HW02/A_FR01/evidence/TC-FR01-54_api.png`
- TC-FR01-55: `HW02/A_FR01/evidence/TC-FR01-55_req.json`, `HW02/A_FR01/evidence/TC-FR01-55_res.json`, `HW02/A_FR01/evidence/TC-FR01-55_api.png`
- TC-FR01-201: `HW02/A_FR01/evidence/TC-FR01-201_req.json`, `HW02/A_FR01/evidence/TC-FR01-201_res.json`, `HW02/A_FR01/evidence/TC-FR01-201_api.png`
- TC-FR01-213: `HW02/A_FR01/evidence/TC-FR01-213_req.json`, `HW02/A_FR01/evidence/TC-FR01-213_res.json`, `HW02/A_FR01/evidence/TC-FR01-213_api.png`
- TC-FR01-219: `HW02/A_FR01/evidence/TC-FR01-219_req.json`, `HW02/A_FR01/evidence/TC-FR01-219_res.json`, `HW02/A_FR01/evidence/TC-FR01-219_api.png`
- TC-FR01-220: `HW02/A_FR01/evidence/TC-FR01-220_req.json`, `HW02/A_FR01/evidence/TC-FR01-220_res.json`, `HW02/A_FR01/evidence/TC-FR01-220_api.png`
- TC-FR01-221: `HW02/A_FR01/evidence/TC-FR01-221_req.json`, `HW02/A_FR01/evidence/TC-FR01-221_res.json`, `HW02/A_FR01/evidence/TC-FR01-221_api.png`
- TC-FR01-225: `HW02/A_FR01/evidence/TC-FR01-225_req.json`, `HW02/A_FR01/evidence/TC-FR01-225_res.json`, `HW02/A_FR01/evidence/TC-FR01-225_api.png`
- TC-FR01-226: `HW02/A_FR01/evidence/TC-FR01-226_req.json`, `HW02/A_FR01/evidence/TC-FR01-226_res.json`, `HW02/A_FR01/evidence/TC-FR01-226_api.png`

## TC liên quan

- Fail (16): TC-FR01-34, TC-FR01-35, TC-FR01-36, TC-FR01-37, TC-FR01-38, TC-FR01-39, TC-FR01-40, TC-FR01-54, TC-FR01-55, TC-FR01-201, TC-FR01-213, TC-FR01-219, TC-FR01-220, TC-FR01-221, TC-FR01-225, TC-FR01-226
- Nhóm dữ kiện: G3, G6 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.1:** Người dùng phải cung cấp Họ Tên (trường bắt buộc).
- **FR-01.2:** Người dùng phải cung cấp Email (trường bắt buộc).
- **FR-01.3:** Email phải có định dạng hợp lệ (user@domain.com).
- **FR-01.5:** Người dùng phải cung cấp Mật khẩu (trường bắt buộc).
- **A2** (giả định, SRS im lặng): A2 (Email – định dạng): FR-01 chỉ đưa mẫu 'user@domain.com'. Giả định định dạng hợp lệ = <local>@<domain>.<tld>: đúng một '@', phần local không rỗng, phần domain có ít nhất một dấu '.' và không rỗng hai bên dấu chấm. FR-22 yêu cầu type="email" nên quy tắc HTML5 của trình duyệt dùng làm tham chiếu phụ. SRS không nêu độ dài tối đa → không kiểm cận trên độ dài email.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- **A15** (giả định, SRS im lặng): A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.
- **A21** (giả định, SRS im lặng): A21 (email chỉ gồm ký tự ASCII): FR-22.2 bắt ô Email dùng type="email". A2 lấy quy tắc HTML5 làm tham chiếu phụ, và theo định nghĩa “valid e-mail address” của HTML5, phần local chỉ gồm ký tự ASCII. Vì vậy email có ký tự ngoài ASCII là sai định dạng. → TC-219: tеst@eshop.com (chữ е Cyrillic) phải bị từ chối, 4xx, không tạo user. Thêm EC52 “Email có ký tự ngoài ASCII” (không hợp lệ), do TC-219 phủ. Nay case này có oracle, không còn là quan sát suông. (AI đề xuất, SV duyệt 2026-10-19)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- G6 (TC-FR01-213) đưa vào làm bằng chứng bổ sung theo quyết định SV.
- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G3, G6): `backend/server.js dòng 20–29`

### Nhận định

- Tương tự BUG-03, nguyên nhân xuất phát từ việc backend handler hoàn toàn thiếu logic validate cho biến email. Request gửi trực tiếp tới API không qua bộ kiểm tra regex/HTML5 của browser nên lọt thẳng xuống câu lệnh SQL INSERT INTO users.

- Việc cho phép tạo tài khoản với email rỗng hoặc sai định dạng khiến dữ liệu CSDL bị rác, đồng thời người dùng sẽ không thể dùng tài khoản này để đăng nhập lại sau đó (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/20

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
