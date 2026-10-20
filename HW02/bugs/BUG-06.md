# BUG-06

- **ID:** BUG-06
- **Tiêu đề:** Gửi 2 request đăng ký đồng thời (race condition) cùng 1 email thì cả 2 đều trả HTTP 200, tạo ra 2 user trùng email trong CSDL
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

Backend vừa khởi động lại, CSDL seed sạch sẽ. Email dùng để test (`hiep.sv10@domain.com`) chưa từng tồn tại trong hệ thống.

## Các bước tái hiện

1. Chuẩn bị 2 request `POST http://localhost:3000/api/register` cùng payload:
   `{"name": "Lê Tấn Hiệp", "email": "hiep.sv10@domain.com", "password": "Hiep123$"}`
2. Gửi đồng thời 2 request này tới backend bằng `Promise.all` (hoặc Postman Runner / Playwright parallel execution).

## Expected (trích SRS)

FR-01.4 yêu cầu Email phải là duy nhất trong hệ thống. Ngay cả khi 2 request bắn tới cùng một lúc, hệ thống vẫn phải xử lý bất đồng bộ chuẩn: chỉ đúng 1 request được phép thành công (HTTP 200), request còn lại phải bị chặn lại với mã lỗi HTTP 4xx và báo email đã tồn tại (A9, A11), đảm bảo chỉ có duy nhất 1 user được tạo trong CSDL.

## Actual

Cả 2 request gửi đồng thời đều lọt qua ngon ơ, đều nhận về phản hồi **HTTP 200** `{"message":"User registered successfully","id": <id>}`. Kết quả là trong CSDL xuất hiện 2 bản ghi user mới có ID khác nhau nhưng xài chung y nguyên email `hiep.sv10@domain.com`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-209_api.png`
- TC-FR01-209: `HW02/A_FR01/evidence/TC-FR01-209_req.json`, `HW02/A_FR01/evidence/TC-FR01-209_res.json`, `HW02/A_FR01/evidence/TC-FR01-209_api.png`

## TC liên quan

- Fail (1): TC-FR01-209
- Nhóm dữ kiện: G8 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.4:** Email phải là duy nhất trong hệ thống.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- SV ghi chú: liên quan BUG-05.
- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G8): `backend/server.js dòng 20–29`; `backend/database.js dòng 50–54`
- TC-FR01-209 chạy lại 3 lần (`--repeat-each=3`, `HW02/tests/results/isolate_209.json`): 3/3 failed; mỗi lần cả 2 request HTTP 200 và tạo 2 user cùng email.

### Nhận định

- Thiếu Constraint ở DB: Bảng users trong database.js hoàn toàn không có ràng buộc UNIQUE cho cột email. Do đó SQLite không hề có cơ chế tự động reject khi có 2 dòng dữ liệu trùng email nạp vô cùng lúc.

- Không có Check-Then-Act hay Transaction: Kể cả backend sau này có viết thêm câu lệnh SELECT kiểm tra email trước khi INSERT, nếu không dùng Transaction/Lock DB hoặc UNIQUE constraint ở tầng database thì khi 2 request tới cùng thời điểm, cả 2 đều SELECT ra "chưa tồn tại" rồi cùng INSERT xuống.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/22

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
