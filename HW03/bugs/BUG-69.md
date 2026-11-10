# BUG-69

- **ID:** BUG-69
- **Tiêu đề:** [Quên MK B2] Mã OTP hiển thị 4 chữ số thay vì 6 chữ số theo SRS
- **Severity:** High
- **Priority:** High
- Tiền tố GitHub: [HW03-C2-69]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-28: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-28: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-28: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-28 – Quên mật khẩu (bước 2)
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Backend vừa restart và hoạt động bình thường. Trạng thái người dùng chưa đăng nhập.

## Các bước tái hiện

1. Truy cập vào trang Quên mật khẩu (`http://localhost:5173/forgot-password`).
2. Nhập email hợp lệ (`test@eshop.com`) ở bước 1 và bấm nút 'Lấy mã OTP'.
3. Chuyển sang bước 2, quan sát mã OTP hiển thị trên màn hình.

## Expected (trích căn cứ)

- CL-28 – căn cứ: FR-03.2 (README.md:51)
  - FR-03.2, README.md:51 (AI chép nguyên văn): Hệ thống sinh mã OTP **6 chữ số ngẫu nhiên** và gửi qua Email (trong môi trường demo: hiển thị trực tiếp trên màn hình).
- Expected của bug: Sau khi nhập email và bấm gửi ở bước 1, hệ thống phải sinh và hiển thị mã OTP có đúng 6 chữ số ngẫu nhiên.

## Actual

- Cả P1, P2 và P3: Mã OTP hiển thị trên màn hình ở bước 2 chỉ có 4 chữ số (P1 hiển thị "1846", P2 hiển thị "9894", P3 hiển thị "8382") thay vì 6 chữ số.

## Bằng chứng

- CL-28 P1 (auto): `../checklist/evidence/auto/P1_CL-28_1.png`, `../checklist/evidence/auto/P1_CL-28_2.png`
- CL-28 P2 (auto): `../checklist/evidence/auto/P2_CL-28_1.png`, `../checklist/evidence/auto/P2_CL-28_2.png`
- CL-28 P3 (auto): `../checklist/evidence/auto/P3_CL-28_1.png`, `../checklist/evidence/auto/P3_CL-28_2.png`

## Item liên quan

- CL-28 – Mã OTP hiển thị có đúng 6 chữ số – Failed: P1, P2, P3
- Nhóm dữ kiện: G-12 trong `HW03/bugs/bug_groups.md` (Mã OTP hiển thị 4 chữ số); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-03.2 (README.md:51):** Mã OTP hiển thị có đúng 6 chữ số (CL-28)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-28 P1 (auto): `Lỗi: Error: mã có 4 chữ số · mã hiển thị: 1846`
- Actual nguyên văn CL-28 P2 (auto): `Lỗi: Error: mã có 4 chữ số · mã hiển thị: 9894`
- Actual nguyên văn CL-28 P3 (auto): `Lỗi: Error: mã có 4 chữ số · mã hiển thị: 8382`
- Nguồn bước tái hiện CL-28: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:321`

### Nhận định

Mã OTP chỉ gồm 4 chữ số làm giảm độ an toàn bảo mật của tính năng khôi phục mật khẩu so với tiêu chuẩn 6 chữ số được định nghĩa trong SRS (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/254

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).