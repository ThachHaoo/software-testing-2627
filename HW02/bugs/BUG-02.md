# BUG-02

- **ID:** BUG-02
- **Tiêu đề:** Mật khẩu 'Abcd 1234' thêm khoảng trắng làm ký tự đặc biệt lại lọt qua form Đăng ký, tạo user thành công
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2)
- Web http://localhost:5173/register (frontend-web)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, chưa đăng nhập. Email muốn đăng ký (`hiep.sv03@domain.com`) chưa tồn tại trong CSDL. Tất cả các trường trong form đều rỗng.

## Các bước tái hiện

1. Mở /register, nhập: `Lê Tấn Hiệp` · `hiep.sv03@domain.com` · `Abcd 1234`
2. Ấn "Đăng Ký"

## Expected (trích SRS)

FR-01.8 quy định mật khẩu phải chứa ít nhất 1 ký tự đặc biệt thuộc tập đóng `{@, $, !, %, *, ?, &}` (A5). `Abcd 1234` chỉ có ký tự khoảng trắng `␣`, không thuộc tập ký tự đặc biệt cho phép → Hệ thống phải từ chối, báo lỗi mật khẩu thiếu ký tự đặc biệt, ở lại /register và không tạo tài khoản.

## Actual

Form chấp nhận mật khẩu, chuyển hướng sang /login, gửi `POST /api/register` (HTTP 200) 1 lần, tạo thành công 1 user mới với email `hiep.sv03@domain.com` trong CSDL, không hiện bất kỳ thông báo lỗi nào.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-202_ui.png`
- TC-FR01-202: `HW02/A_FR01/evidence/TC-FR01-202_ui.png`

## TC liên quan

- Fail (1): TC-FR01-202
- Nhóm dữ kiện: G11 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.8:** Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &.
- **A5** (giả định, SRS im lặng): A5 (Mật khẩu – ký tự đặc biệt): hiểu danh sách (@, $, !, %, *, ?, &) là tập ĐÓNG: mật khẩu chỉ chứa ký tự đặc biệt ngoài tập này (ví dụ #, ^, -, khoảng trắng) bị coi là thiếu ký tự đặc biệt → bị từ chối. SRS không nói ký tự ngoài tập có được phép xuất hiện thêm hay không → giả định được phép nếu đã có ít nhất một ký tự trong tập.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G11): `frontend-web/src/pages/Register.jsx dòng 15–20`

### Nhận định

- Lỗi xuất phát từ regex kiểm tra ở Client (flawedStrongPasswordRegex). Regex dùng (?=.*\s) nên coi ký tự khoảng trắng \s là ký tự đặc biệt, đồng thời tập ký tự hợp lệ lại cho phép \s ([A-Za-z\d\s]{8,}$). Do đó, chuỗi Abcd 1234 vượt qua bộ lọc thành công.

- Lỗi này ngược hoàn toàn với BUG-01: mật khẩu thực sự hợp lệ theo SRS như Abcd1234! (dùng !) thì lại bị Regex chặn và báo lỗi "Mật khẩu quá yếu!", trong khi mật khẩu vi phạm SRS như Abcd 1234 (dùng khoảng trắng) thì lại lọt qua.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/18

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
