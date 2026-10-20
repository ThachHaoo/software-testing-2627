# BUG-11

- **ID:** BUG-11
- **Tiêu đề:** Họ Tên chứa thẻ HTML/Script (`<img src=x onerror=alert(1)>`) bị dính lỗi Stored XSS, chạy script và văng ảnh lỗi trên thanh điều hướng sau khi đăng nhập
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Lượt tự động: Chromium 130.0.6723.31 (Playwright 1.48.2) — Blocked (A20)
- Kiểm tay (xác định verdict): Cốc Cốc phiên bản 158.0.124 (bản 64 bit)
- Web http://localhost:5173 (đăng nhập, trang chủ, /profile)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon); kiểm tay cùng ngày
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Tạo sẵn một tài khoản thành công qua API `POST /api/register` có Họ Tên chứa mã script độc hại:
- Payload: `{"name": "<img src=x onerror=alert(1)>", "email": "hiep.sv17@domain.com", "password": "Hiep123$"}`

## Các bước tái hiện

1. Mở web http://localhost:5173/login và đăng nhập bằng tài khoản `hiep.sv17@domain.com` / `Hiep123$`.
2. Quan sát màn hình ngay sau khi đăng nhập xong (thanh điều hướng Navbar).
3. Chuyển sang các trang khác như trang Hồ sơ (`/profile`).

## Expected (trích SRS)

Theo **SEC-04** (README.md dòng 281), mọi dữ liệu do người dùng nhập vào khi render hiển thị ra giao diện UI phải được escape đúng cách, tuyệt đối không dùng `dangerouslySetInnerHTML` hay `innerHTML` trực tiếp. Chuỗi `<img src=x onerror=alert(1)>` phải được render dạng plain-text nguyên văn, không được chạy mã JavaScript hay hiển thị thẻ `<img>`.

## Actual

- Ngay sau khi đăng nhập thành công, trình duyệt bật thẳng pop-up alert: `localhost:5173 cho biết` (nội dung `1`) (do đoạn mã `onerror=alert(1)` dính XSS bị kích hoạt chạy), phải bấm OK tới 2 lần mới tắt hẳn pop-up.
- Trên thanh điều hướng Header (thẻ Navbar), sau chữ `"Chào,"` xuất hiện biểu tượng ảnh bị lỗi render thay vì hiển thị tên người dùng.
- Khi vào trang Hồ sơ (`/profile`), Họ Tên lại hiển thị dạng chuỗi chữ nguyên văn (chứng tỏ bị lỗi rải rác không đồng nhất giữa các trang).

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-216_manual_alert.png`, `TC-FR01-216_manual_header.png`
- TC-FR01-216: `HW02/A_FR01/evidence/TC-FR01-216_ui.png`, `HW02/A_FR01/evidence/TC-FR01-216_manual_alert.png`, `HW02/A_FR01/evidence/TC-FR01-216_manual_header.png`, `HW02/A_FR01/evidence/TC-FR01-216_manual_profile.png`, `HW02/A_FR01/evidence/TC-FR01-216_manual_admin.png`

## TC liên quan

- Fail (1): TC-FR01-216
- Nhóm dữ kiện: G12 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **SEC-04:** Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng innerHTML trực tiếp (README.md dòng 281).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G12): `frontend-web/src/App.jsx dòng 26–28`
- TC-FR01-216: lần chạy tự động Blocked theo A20 (auto_status Blocked, ảnh `TC-FR01-216_ui.png`); verdict Fail do SV kiểm tay qua API + web :5173 (notes TC-216, ảnh `_manual_*.png`).
- Issue cùng loại ở trang khác: #16 — [BUG-FR08-07] Địa chỉ giao hàng chứa HTML được thực thi ở Web Admin (stored XSS)

### Nhận định

- Lỗi lỗ hổng bảo mật Stored XSS nguyên nhân lòi ra trực tiếp tại dòng 27 trong App.jsx:
Code React mặc định đã tự sanitize phòng chống XSS rồi, nhưng dev lại cố tình dùng thuộc tính dangerouslySetInnerHTML={{ __html: ... }} để render thẳng chuỗi user.name lấy từ CSDL lên Header.

- Hậu quả: Bất kỳ ai chèn mã JS/HTML vào trường Họ Tên lúc đăng ký thì mỗi lần người dùng đó đăng nhập vào web là đoạn mã độc sẽ tự động thực thi trong trình duyệt, vô cùng nguy hiểm.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/27

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
