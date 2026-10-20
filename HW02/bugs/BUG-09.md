# BUG-09

- **ID:** BUG-09
- **Tiêu đề:** Gửi mật khẩu hợp lệ dài 200.000 ký tự qua API làm backend trả về trang lỗi HTML HTTP 413 PayloadTooLargeError
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

Backend vừa mới khởi động lại xong, CSDL seed sạch sẽ. Họ Tên với Email trong payload là chuẩn theo SRS.

## Các bước tái hiện

1. Chuẩn bị payload `POST /api/register` có chứa trường mật khẩu siêu dài:
   - Header `Content-Type: application/json`
   - `name` = `"Lê Tấn Hiệp"`
   - `email` = `"hiep.sv13@domain.com"`
   - `password` = chuỗi hợp lệ dài 200.000 ký tự (ví dụ bắt đầu bằng `"Hiep123$"` rồi cộng thêm 199.992 ký tự `'a'`).
2. Gửi request `POST http://localhost:3000/api/register` tới server backend.

## Expected (trích SRS)

FR-01.6 và giả định A4 chỉ đặt ra độ dài tối thiểu là 8 ký tự cho mật khẩu chứ hoàn toàn không có đặt ra giới hạn cận trên (UB). Mật khẩu 200.000 ký tự vẫn có đủ chữ hoa, chữ thường, số và ký tự đặc biệt nên hoàn toàn hợp lệ. Backend phải xử lý nhận request thành công, trả về **HTTP 200** và tạo tài khoản user mới trong CSDL.

## Actual

Backend văng ra lỗi **HTTP 413** kèm trả về nguyên cục trang web HTML lỗi: `PayloadTooLargeError: request entity too large`. Đương nhiên là không có user mới nào được tạo ra trong CSDL cả.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-212_api.png`
- TC-FR01-212: `HW02/A_FR01/evidence/TC-FR01-212_req.json`, `HW02/A_FR01/evidence/TC-FR01-212_res.json`, `HW02/A_FR01/evidence/TC-FR01-212_api.png`

## TC liên quan

- Fail (1): TC-FR01-212
- Nhóm dữ kiện: G9 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.6:** Mật khẩu tối thiểu 8 ký tự.
- **A4** (giả định, SRS im lặng): A4 (Mật khẩu – độ dài): chỉ có cận dưới 8 ký tự. SRS không có cận trên → không có UB; BVA độ dài chỉ quanh LB = 8 (7, 8, 9) và NOM.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G9): `backend/server.js dòng 3–12`
- `TC-FR01-212_req.json` ghi `password` dạng rút gọn (`Hiep123$aaa… (200000 ký tự)`); chuỗi gửi thật được script dựng và kiểm độ dài = 200.000 (`tests/A_FR01/lib.ts` dòng 32–37).
- Body 413 (`TC-FR01-212_res.json`) có stack trace: 10 dòng `at ...` (raw-body, body-parser, router, cors), kèm đường dẫn tuyệt đối trên máy chạy.
- Sau TC-FR01-212, test kế tiếp trong lượt chạy (TC-FR01-213, tầng API, Fail) vẫn nhận phản hồi từ backend (HTTP 200, id 58) → tiến trình backend không dừng.

### Nhận định

- SRS không hề quy định độ dài tối đa của mật khẩu (A4) nên hệ thống lý thuyết phải chấp nhận mọi chuỗi dài.

- Tuy nhiên trong server.js, dòng 12 dùng app.use(bodyParser.json()) nguyên bản không hề cấu hình limit độ lớn payload. Thư viện body-parser mặc định sẽ chặn và văng lỗi 413 nếu body JSON vượt quá ~100 KB.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/25

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
