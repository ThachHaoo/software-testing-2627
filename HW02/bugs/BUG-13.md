# BUG-13

- **ID:** BUG-13
- **Tiêu đề:** Ô nhập Email trên form Đăng ký dùng type="text" thay vì type="email"
- **Severity:** Low
- **Priority:** Low

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
2. Inspect ô nhập liệu Email (dùng DevTools hoặc Playwright `getAttribute('type')`).

## Expected (trích SRS)

Theo **FR-22.2**, trường Email phải sử dụng thuộc tính `type="email"` để vừa hỗ trợ trình duyệt kiểm tra định dạng email nguyên bản vừa hiện bàn phím tối ưu nút `@` cho thiết bị di động.

## Actual

Ô nhập Email trên UI lại dùng thẻ `<input type="text">`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-91_ui.png`
- TC-FR01-91: `HW02/A_FR01/evidence/TC-FR01-91_ui.png`

## TC liên quan

- Fail (1): TC-FR01-91
- Nhóm dữ kiện: G14 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-22.2:** Trường Email dùng type="email".

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G14): `frontend-web/src/pages/Register.jsx dòng 45–49`
- Issue cùng loại ở trang khác: #4 — [BUG-FR02-04] Ô email form đăng nhập Web là `type="text"`, không kiểm tra định dạng

### Nhận định

- Lỗi xuất phát do frontend dev chọn sai type cho thẻ <input> khi code giao diện màn hình Register.jsx.

- Hậu quả:

+ Bỏ mất tính năng tự động validate email căn bản của HTML5 trên trình duyệt.

+ Người dùng trên điện thoại/máy tính bảng khi bấm vào ô Email sẽ không hiện bàn phím ảo chuyên dụng có sẵn ký tự @ và domain .com, làm giảm trải nghiệm người dùng (UX) (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/29

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
