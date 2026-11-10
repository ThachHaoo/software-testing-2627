# BUG-84

- **ID:** BUG-84
- **Tiêu đề:** [Đăng nhập, Hồ sơ] Độ tương phản màu sắc của chữ/nhãn so với nền không đạt tối thiểu 4.5:1
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-84]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay · SV-04: lượt `runs/P1_manual_20261109-2257.md`, 22:58 09/11/2026 - 00:10 10/11/2026
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay · SV-04: lượt `runs/P2_manual_20261110-0010.md`, 00:10 10/11/2026 - 00:38 10/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay · SV-04: lượt `runs/P3_manual_20261110-0046.md`, 00:46 10/11/2026 - 01:54 10/11/2026
- Màn hình: SV-04 – Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Màn hình Hồ sơ (`http://localhost:5173/profile`) đã đăng nhập tài khoản `test@eshop.com` / `Test1234!`.

## Các bước tái hiện

1. Mở trình duyệt và truy cập trang Đăng nhập (`http://localhost:5173/login`).
2. Mở DevTools -> dùng công cụ **Accessibility** / **Lighthouse** (hoặc Inspect phần tử) để đo tỉ lệ tương phản màu sắc (Color Contrast Ratio) giữa chữ/nhãn và màu nền.
3. Đăng nhập tài khoản `test@eshop.com` / `Test1234!` và truy cập trang Hồ sơ (`http://localhost:5173/profile`).
4. Tiến hành đo tỉ lệ tương phản màu sắc của chữ/nhãn tại trang Hồ sơ.
5. So sánh với trang Quên mật khẩu (`http://localhost:5173/forgot-password`).

## Expected (trích căn cứ)

- SV-04 – căn cứ: WCAG 2.2 SC 1.4.3 (Contrast Minimum)
- Expected của bug: Kiểm tra bằng công cụ DevTools Accessibility / Lighthouse: tỉ lệ tương phản màu sắc của chữ (văn bản, label, placeholder, text trên button) so với màu nền đạt tối thiểu 4.5:1 (đối với chữ thường).

## Actual

- Trên cả P1 (Cốc Cốc), P2 (Firefox) và P3 (Chrome Android):
  - Trang Quên mật khẩu (`/forgot-password`) đạt tỉ lệ tương phản tối thiểu 4.5:1.
  - Trang Đăng nhập (`/login`) và trang Hồ sơ (`/profile`) không đạt tỉ lệ tương phản tối thiểu 4.5:1 so với màu nền.

## Bằng chứng

- SV-04 P1 (tay): `../checklist/evidence/P1_chrome/P1_SV-04_1.png`, `../checklist/evidence/P1_chrome/P1_SV-04_2.png`, `../checklist/evidence/P1_chrome/P1_SV-04_3.png`, `../checklist/evidence/P1_chrome/P1_SV-04_4.png`
- SV-04 P2 (tay): `../checklist/evidence/P2_firefox/P2_SV-04_1.png`, `../checklist/evidence/P2_firefox/P2_SV-04_2.png`, `../checklist/evidence/P2_firefox/P2_SV-04_3.png`, `../checklist/evidence/P2_firefox/P2_SV-04_4.png`
- SV-04 P3 (tay): `../checklist/evidence/P3_android/P3_SV-04_1.png`, `../checklist/evidence/P3_android/P3_SV-04_2.png`, `../checklist/evidence/P3_android/P3_SV-04_3.png`, `../checklist/evidence/P3_android/P3_SV-04_4.png`

## Item liên quan

- SV-04 – Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) – Failed: P1, P2, P3
- Nhóm dữ kiện: G-27 trong `HW03/bugs/bug_groups.md` (Độ tương phản chữ/nhãn dưới 4.5:1 ở Đăng nhập, Hồ sơ); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **WCAG 2.2 SC 1.4.3 (Contrast Minimum):** Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) (SV-04)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn SV-04 P1 (tay): `Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không`
- Actual nguyên văn SV-04 P2 (tay): `Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không`
- Actual nguyên văn SV-04 P3 (tay): `Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không`
- Nguồn bước tái hiện SV-04: tiền điều kiện (checklist): – · cách kiểm: auto: tỉ lệ tương phản chữ/nền tính từ màu CSS; placeholder + Lighthouse → SV · test tự động: `HW03/tests/C2.spec.ts:891`

### Nhận định

Màu chữ và nhãn trên trang Đăng nhập và Hồ sơ không đạt độ tương phản tối thiểu 4.5:1 theo tiêu chuẩn WCAG 2.2 SC 1.4.3 khiến văn bản bị mờ và có thể khó đọc đối với người dùng có thị lực kém hoặc khi xem màn hình ở điều kiện ánh sáng mạnh (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/259

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).