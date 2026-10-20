# BUG-01

- **ID:** BUG-01
- **Tiêu đề:** Đăng ký không cho mật khẩu hợp lệ, nó nói "Mật khẩu quá yếu!"
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

Backend vừa khởi động lại, chưa đăng nhập. Email muốn đăng ký chưa tồn tại.

## Các bước tái hiện

1. Mở /register, nhập: `Nguyen Van A` · `dom01_1792424523821@domain.com` · `Abcd1234!`
2. Ấn "Đăng Ký" 

## Expected (trích SRS)

FR-01: mật khẩu "tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (@, $, !, %, *, ?, &)" → `Abcd1234!` hợp lệ → chuyển hướng sang /login và tạo 1 user.

## Actual

Hộp lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.", ở lại /register, không gửi `POST /api/register`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-01_ui.png`, `TC-FR01-64_ui.png`

<details>
<summary>Ảnh từng TC (14)</summary>

- TC-FR01-01: `HW02/A_FR01/evidence/TC-FR01-01_ui.png`, `HW02/A_FR01/evidence/TC-FR01-01_failed.png`
- TC-FR01-02: `HW02/A_FR01/evidence/TC-FR01-02_ui.png`, `HW02/A_FR01/evidence/TC-FR01-02_failed.png`
- TC-FR01-64: `HW02/A_FR01/evidence/TC-FR01-64_ui.png`, `HW02/A_FR01/evidence/TC-FR01-64_failed.png`
- TC-FR01-65: `HW02/A_FR01/evidence/TC-FR01-65_ui.png`, `HW02/A_FR01/evidence/TC-FR01-65_failed.png`
- TC-FR01-66: `HW02/A_FR01/evidence/TC-FR01-66_ui.png`, `HW02/A_FR01/evidence/TC-FR01-66_failed.png`
- TC-FR01-68: `HW02/A_FR01/evidence/TC-FR01-68_ui.png`, `HW02/A_FR01/evidence/TC-FR01-68_failed.png`
- TC-FR01-69: `HW02/A_FR01/evidence/TC-FR01-69_ui.png`, `HW02/A_FR01/evidence/TC-FR01-69_failed.png`
- TC-FR01-71: `HW02/A_FR01/evidence/TC-FR01-71_ui.png`, `HW02/A_FR01/evidence/TC-FR01-71_failed.png`
- TC-FR01-72: `HW02/A_FR01/evidence/TC-FR01-72_ui.png`, `HW02/A_FR01/evidence/TC-FR01-72_failed.png`
- TC-FR01-74: `HW02/A_FR01/evidence/TC-FR01-74_ui.png`, `HW02/A_FR01/evidence/TC-FR01-74_failed.png`
- TC-FR01-75: `HW02/A_FR01/evidence/TC-FR01-75_ui.png`, `HW02/A_FR01/evidence/TC-FR01-75_failed.png`
- TC-FR01-77: `HW02/A_FR01/evidence/TC-FR01-77_ui.png`, `HW02/A_FR01/evidence/TC-FR01-77_failed.png`
- TC-FR01-78: `HW02/A_FR01/evidence/TC-FR01-78_ui.png`, `HW02/A_FR01/evidence/TC-FR01-78_failed.png`
- TC-FR01-211: `HW02/A_FR01/evidence/TC-FR01-211_ui.png`, `HW02/A_FR01/evidence/TC-FR01-211_failed.png`
</details>

## TC liên quan

- Fail (14): TC-FR01-01, TC-FR01-02, TC-FR01-64, TC-FR01-65, TC-FR01-66, TC-FR01-68, TC-FR01-69, TC-FR01-71, TC-FR01-72, TC-FR01-74, TC-FR01-75, TC-FR01-77, TC-FR01-78, TC-FR01-211
- Blocked ghi case gốc (22): TC-FR01-03, TC-FR01-04, TC-FR01-06, TC-FR01-08, TC-FR01-09, TC-FR01-10, TC-FR01-11, TC-FR01-12, TC-FR01-13, TC-FR01-14, TC-FR01-15, TC-FR01-61, TC-FR01-62, TC-FR01-200, TC-FR01-203, TC-FR01-204, TC-FR01-205, TC-FR01-208, TC-FR01-215, TC-FR01-217, TC-FR01-218, TC-FR01-223
- Nhóm dữ kiện: G1 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.10:** Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.
- **Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8** (ngầm định — Actual chỉ có thông báo gộp, không xác định được luật riêng nào bị cài sai)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G1): `frontend-web/src/pages/Register.jsx dòng 15–20`
- Các case Blocked ghi case gốc: TC-FR01-01 (A17/A20).
- SRS `eshop-sut/README.md` dòng 34 (FR-01, mật khẩu): "- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`)."
- FR-01.8 (tập ký tự, cùng dòng 34): "1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`)"
- FR-01.10, dòng 36: "- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập."
- Dữ liệu nhập (`HW02/A_FR01/testcases.json`, `{ts}` = timestamp lúc chạy):

  | TC | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu |
  |---|---|---|---|---|
  | TC-FR01-01 | `Nguyen Van A` | `dom01_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` |
  | TC-FR01-64 (LB, 8 ký tự) | `Nguyen Van A` | `bva64_{ts}@domain.com` | `Abc12!xy` | `Abc12!xy` |

### Nhận định

Lỗi ở kiểm tra phía client (0 POST). Ngược lại, `Abcd 1234` (không có ký tự đặc biệt) lại được chấp nhận (TC-202) (xem BUG-02). 22 case Blocked vì cần mật khẩu hợp lệ để qua bước này. 

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/17

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
