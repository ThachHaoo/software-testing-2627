# BUG-70

- **ID:** BUG-70
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
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

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- CL-29 – căn cứ: FR-03.6 (README.md:58, 34)
  - FR-03.6, README.md:58 (AI chép nguyên văn): Mật khẩu mới phải tuân thủ điều kiện như FR-01.
  - FR-03.6, README.md:34 (AI chép nguyên văn): **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
