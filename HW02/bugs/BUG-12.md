# BUG-12

- **ID:** BUG-12
- **Tiêu đề:** Nhãn các trường bắt buộc trên form Đăng ký (Họ Tên, Email, Mật khẩu) không có ký hiệu dấu sao '*'
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2)
- Web http://localhost:5173/register (frontend-web)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Mở trình duyệt truy cập vào trang Đăng ký `/register`. Các ô nhập liệu đều rỗng

## Các bước tái hiện

1. Truy cập trang `/register`.
2. Nhìn các label tiêu đề phía trên các ô nhập liệu của form.

## Expected (trích SRS)

Theo **FR-22.1**, mọi trường thông tin bắt buộc trong hệ thống phải có ký hiệu dấu sao `*` đặt ngay bên cạnh tên nhãn. Vì Họ Tên, Email, Mật khẩu đều là 3 trường bắt buộc theo FR-01, các nhãn này trên UI phải hiển thị dạng: `Họ Tên *`, `Email *`, `Mật khẩu *`.

## Actual

Cả 3 nhãn trường bắt buộc trên form đăng ký hoàn toàn trơn rụi không có dấu `*` nào kế bên: nhãn hiển thị nguyên văn chỉ là `"Họ Tên"`, `"Email"`, `"Mật khẩu"`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-90_ui.png`
- TC-FR01-90: `HW02/A_FR01/evidence/TC-FR01-90_ui.png`

## TC liên quan

- Fail (1): TC-FR01-90
- Nhóm dữ kiện: G13 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-22.1:** Trường bắt buộc có ký hiệu * bên cạnh nhãn.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G13): `frontend-web/src/pages/Register.jsx dòng 35–37`
- Issue cùng loại ở trang khác: #7 — [BUG-FR02-07] Trường bắt buộc của form đăng nhập không có ký hiệu `*`

### Nhận định

- Lỗi xuất phát trực tiếp từ code UI màn hình Register.jsx. Khi viết JSX, frontend dev gõ cứng chuỗi văn bản "Họ Tên", "Email", "Mật khẩu" vào thẻ <label> mà quên thêm ký tự * hay span màu đỏ đánh dấu trường bắt buộc theo đúng quy chuẩn UI/UX của SRS.

- Lỗi này tuy nhỏ (GUI bug) không gây sập app nhưng vi phạm trực tiếp yêu cầu thiết kế giao diện FR-22.1 và làm người dùng khó nhận biết trường nào bắt buộc phải điền.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/28

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
