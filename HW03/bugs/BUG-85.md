# BUG-85

- **ID:** BUG-85
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
- Tiền tố GitHub: [HW03-C2-85]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · SV-05: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · SV-05: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · SV-05: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: SV-05 – Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- SV-05 – căn cứ: WCAG 2.2 SC 2.5.8 (Target Size Minimum - 24x24px)
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- SV-05 P1 (auto): `../checklist/evidence/auto/P1_SV-05_1.png`
- SV-05 P2 (auto): `../checklist/evidence/auto/P2_SV-05_1.png`
- SV-05 P3 (auto): `../checklist/evidence/auto/P3_SV-05_1.png`

## Item liên quan

- SV-05 – Kích thước vùng tương tác của con trỏ (Target Size) đối với các nút và link – Failed: P1, P2, P3
- Nhóm dữ kiện: G-28 trong `HW03/bugs/bug_groups.md` (Link 'Quên mật khẩu?', 'Đăng ký ngay' nhỏ hơn 24×24 px); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **WCAG 2.2 SC 2.5.8 (Target Size Minimum - 24x24px):** Kích thước vùng tương tác của con trỏ (Target Size) đối với các nút và link (SV-05)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn SV-05 P1 (auto): `Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 382×40 · Quên mật khẩu?: 102×19 · Đăng ký ngay: 85×19 · Lấy mã OTP: 382×40 · Cập nhật: 271×40`
- Actual nguyên văn SV-05 P2 (auto): `Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 382×40 · Quên mật khẩu?: 102×19 · Đăng ký ngay: 85×19 · Lấy mã OTP: 382×40 · Cập nhật: 271×40`
- Actual nguyên văn SV-05 P3 (auto): `Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 295×40 · Quên mật khẩu?: 100×16 · Đăng ký ngay: 82×16 · Lấy mã OTP: 295×40 · Cập nhật: 311×40`
- Nguồn bước tái hiện SV-05: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:900`

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
