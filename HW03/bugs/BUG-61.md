# BUG-61

- **ID:** BUG-61
- **Tiêu đề:** [Đăng nhập, Quên MK, Hồ sơ] Các trang thiếu thẻ <h1> tiêu đề chính
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-61]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-02: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-02: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-02: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-02 – Đăng nhập, Quên mật khẩu, Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Màn hình Hồ sơ (`/profile`) yêu cầu đã đăng nhập bằng tài khoản `test@eshop.com` / `Test1234!`.

## Các bước tái hiện

1. Mở trình duyệt và truy cập lần lượt các trang: Đăng nhập (`http://localhost:5173/login`), Quên mật khẩu (`http://localhost:5173/forgot-password`), và Hồ sơ (`http://localhost:5173/profile`).
2. Mở DevTools -> tab Elements (hoặc Console) và kiểm tra số lượng thẻ `<h1>` trên từng trang bằng lệnh: `document.querySelectorAll('h1').length`.

## Expected (trích căn cứ)

- CL-02 – căn cứ: FR-21.4 (README.md:247)
  - FR-21.4, README.md:247 (AI chép nguyên văn): **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
- Expected của bug: Trên mỗi trang `/login`, `/forgot-password`, và `/profile`, lệnh DevTools `document.querySelectorAll('h1').length` phải trả về đúng 1.

## Actual

- Cả P1, P2 và P3: Trên cả 3 trang (`/login`, `/forgot-password`, `/profile`), lệnh kiểm tra DevTools đều trả về 0 thẻ `<h1>` (`/login: 0 h1`, `/forgot-password: 0 h1`, `/profile: 0 h1`).

## Bằng chứng

- CL-02 P1 (auto): `../checklist/evidence/auto/P1_CL-02_1.png`
- CL-02 P2 (auto): `../checklist/evidence/auto/P2_CL-02_1.png`
- CL-02 P3 (auto): `../checklist/evidence/auto/P3_CL-02_1.png`

## Item liên quan

- CL-02 – Mỗi trang có đúng 1 thẻ <h1> – Failed: P1, P2, P3
- Nhóm dữ kiện: G-04 trong `HW03/bugs/bug_groups.md` (Trang không có thẻ <h1>); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-21.4 (README.md:247):** Mỗi trang có đúng 1 thẻ <h1> (CL-02)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-02 P1 (auto): `Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1`
- Actual nguyên văn CL-02 P2 (auto): `Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1`
- Actual nguyên văn CL-02 P3 (auto): `Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1`
- Nguồn bước tái hiện CL-02: tiền điều kiện (checklist): P3: mở DevTools qua chrome://inspect (adb). · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:52`

### Nhận định

Trang web thiếu thẻ `<h1>` làm giảm tính tiếp cận (Accessibility) đối với người dùng sử dụng trình đọc màn hình và ảnh hưởng tới chuẩn cấu trúc ngữ nghĩa của trang (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/249

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).