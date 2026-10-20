# BUG-08

- **ID:** BUG-08
- **Tiêu đề:** Backend API POST /api/register không Trim khoảng trắng thừa ở hai đầu Email trước khi lưu vào CSDL
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

Backend vừa khởi động lại, CSDL seed sạch. Họ Tên và Mật khẩu trong payload hợp lệ theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi email có chứa khoảng trắng ở hai đầu:
   `{"name": "Nguyen Van A", "email": "  api30_1792424692167@domain.com  ", "password": "Abcd1234!"}`

## Expected (trích SRS)

Theo quy chuẩn xử lý dữ liệu chuẩn (A3) và nguyên tắc duy nhất của Email (FR-01.4), khoảng trắng thừa ở hai đầu email phải được tự động cắt chuẩn hóa (`.trim()`) trước khi lưu vào CSDL. Phản hồi API trả **HTTP 200** và email lưu trong CSDL phải là `api30_1792424692167@domain.com` (đã cắt hết dấu cách thừa).

## Actual

API trả về **HTTP 200** `{"message":"User registered successfully","id": 5}`, nhưng email trong CSDL bị lưu nguyên văn cả các khoảng trắng hai đầu: `"  api30_1792424692167@domain.com  "`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-30_api.png`
- TC-FR01-30: `HW02/A_FR01/evidence/TC-FR01-30_req.json`, `HW02/A_FR01/evidence/TC-FR01-30_res.json`, `HW02/A_FR01/evidence/TC-FR01-30_api.png`

## TC liên quan

- Fail (1): TC-FR01-30
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **A3** (giả định, SRS im lặng): A3 (Email – duy nhất): Email so sánh sau khi cắt khoảng trắng đầu/cuối; phần local phân biệt hoa/thường, phần domain không phân biệt (RFC 5321 §2.4). SV sửa ở bước 5.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G7): `backend/server.js dòng 20–29`

### Nhận định

- Người dùng khi đăng nhập lại bằng email chính xác (không gõ khoảng trắng) sẽ bị báo sai tài khoản/mật khẩu vì chuỗi so sánh không khớp với giá trị lưu trong CSDL (chưa kiểm chứng).

- Tạo kẽ hở cho phép đăng ký trùng email ảo (một email có khoảng trắng và một email không có khoảng trắng được coi là 2 bản ghi khác nhau) (xem TC-FR01-42, BUG-05).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/24

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
