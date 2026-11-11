# BUG-70

- **ID:** BUG-70
- **Tiêu đề:** [Quên MK B2] Mật khẩu hợp lệ 'Abcdef1!' bị từ chối với thông báo "Mật khẩu quá yếu!"
- **Severity:** High
- **Priority:** High
- Tiền tố GitHub: [HW03-C2-70]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-29: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-29: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-29: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-29 – Quên mật khẩu (bước 2)
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Backend vừa restart và hoạt động bình thường. Đã thực hiện bước 1 lấy mã OTP cho tài khoản `test@eshop.com`.

## Các bước tái hiện

1. Truy cập trang Quên mật khẩu (`http://localhost:5173/forgot-password`).
2. Nhập email `test@eshop.com` ở bước 1 và bấm nút 'Lấy mã OTP' để chuyển sang bước 2.
3. Tại bước 2, nhập đúng mã OTP vừa hiển thị và nhập ô Mật khẩu mới là `Abcdef1!` (đủ 8 ký tự, gồm chữ hoa, chữ thường, số và ký tự đặc biệt `!`).
4. Bấm nút 'Đặt lại mật khẩu' và kiểm tra phản hồi của hệ thống.
5. Thử dùng mật khẩu mới `Abcdef1!` để đăng nhập lại tại trang `/login`.

## Expected (trích căn cứ)

- CL-29 – căn cứ: FR-03.6 (README.md:58, 34)
  - FR-03.6, README.md:58 (AI chép nguyên văn): Mật khẩu mới phải tuân thủ điều kiện như FR-01.
  - FR-03.6, README.md:34 (AI chép nguyên văn): **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
- Expected của bug: Với OTP đúng, Mật khẩu mới 'Abcdef1!' (8 ký tự, có hoa, thường, số, '!') phải được hệ thống chấp nhận đổi thành công; sau đó người dùng đăng nhập lại bằng mật khẩu mới được.

## Actual

- Cả P1, P2 và P3: Mật khẩu "Abcdef1!" không được chấp nhận. Hệ thống từ chối đổi mật khẩu và xuất hiện thông báo lỗi: "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." Đăng nhập lại bằng mật khẩu "Abcdef1!" trả về thất bại (`false`).

## Bằng chứng

- CL-29 P1 (auto): `../checklist/evidence/auto/P1_CL-29_1.png`
- CL-29 P2 (auto): `../checklist/evidence/auto/P2_CL-29_1.png`
- CL-29 P3 (auto): `../checklist/evidence/auto/P3_CL-29_1.png`

## Item liên quan

- CL-29 – Mật khẩu mới hợp lệ theo FR-01 được chấp nhận – Failed: P1, P2, P3 · liên quan #17 (#17 cùng thông báo "Mật khẩu quá yếu!" ở Đăng ký; Quên MK bước 2 chưa có issue)
- Nhóm dữ kiện: G-13 trong `HW03/bugs/bug_groups.md` (Quên mật khẩu B2: mật khẩu 'Abcdef1!' bị báo yếu); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-03.6 (README.md:58, 34):** Mật khẩu mới hợp lệ theo FR-01 được chấp nhận (CL-29)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-29 P1 (auto): `Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]`
- Actual nguyên văn CL-29 P2 (auto): `Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]`
- Actual nguyên văn CL-29 P3 (auto): `Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."]`
- Nguồn bước tái hiện CL-29: tiền điều kiện (checklist): Dùng tài khoản test@eshop.com; restart backend sau khi kiểm để khôi phục mật khẩu Test1234!. · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:334`

### Nhận định

Bộ kiểm tra độ mạnh mật khẩu ở bước 2 Quên mật khẩu (`ForgotPassword.jsx:26` regex bắt buộc khoảng trắng) chặn người dùng sử dụng mật khẩu hoàn toàn đạt chuẩn SRS, làm ảnh hưởng đến quy trình khôi phục tài khoản (chưa kiểm chứng). Liên quan issue #17.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/265

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).