# BUG-14

- **ID:** BUG-14
- **Tiêu đề:** Form Đăng ký trên Frontend thiếu hẳn trường 'Xác nhận mật khẩu' theo yêu cầu SRS
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

Mở trình duyệt truy cập vào trang Đăng ký `/register`.  Các ô nhập liệu đều rỗng

## Các bước tái hiện

1. Truy cập trang `/register`.
2. Mắt quan sát các ô nhập liệu hiện có trên form Đăng ký.

## Expected (trích SRS)

Theo **FR-01.9**, form Đăng ký phải bắt buộc có trường **Xác nhận mật khẩu** (Confirm Password). Hệ thống phải kiểm tra và từ chối đăng ký nếu Mật khẩu và Xác nhận mật khẩu nhập vào không trùng khớp với nhau.

## Actual

Form Đăng ký trên giao diện hiện tại chỉ có đúng 3 ô nhập liệu (Họ Tên, Email, Mật khẩu), hoàn toàn **không có ô Xác nhận mật khẩu** (số ô 'Xác nhận mật khẩu' = 0).

## Bằng chứng

- Ảnh tiêu biểu đính kèm GitHub Issue: `TC-FR01-94_ui.png`
- TC-FR01-94: `HW02/A_FR01/evidence/TC-FR01-94_ui.png`

## TC liên quan

- Fail (1): TC-FR01-94
- Blocked ghi case gốc (3): TC-FR01-25, TC-FR01-26, TC-FR01-27
- Nhóm dữ kiện: G15 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.9:** Phải có trường Xác nhận mật khẩu; hệ thống từ chối nếu Mật khẩu và Xác nhận mật khẩu không khớp.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G15): `frontend-web/src/pages/Register.jsx dòng 63–72`
- Các case Blocked ghi case gốc: TC-FR01-94 (A17/A20).

### Nhận định

- Lỗi do Frontend dev khi dựng form Đăng ký tại Register.jsx đã bỏ sót không code ô input cho trường Xác nhận mật khẩu.

- Hậu quả:

+ Vi phạm trực tiếp yêu cầu chức năng FR-01.9 của SRS.

+ Người dùng khi gõ nhầm mật khẩu ở ô Mật khẩu chính sẽ không có bước xác nhận lại, dẫn tới việc tạo tài khoản với mật khẩu không đúng ý muốn và gặp khó khăn khi đăng nhập sau này.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
