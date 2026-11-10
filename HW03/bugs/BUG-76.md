# BUG-76

- **ID:** BUG-76
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
- Tiền tố GitHub: [HW03-C2-76]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-49: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-49: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-49: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-49 – Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- CL-49 – căn cứ: Nielsen #3 (lối thoát); Nielsen #9
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- CL-49 P1 (auto): `../checklist/evidence/auto/P1_CL-49_1.png`, `../checklist/evidence/auto/P1_CL-49_2.png`
- CL-49 P2 (auto): `../checklist/evidence/auto/P2_CL-49_1.png`, `../checklist/evidence/auto/P2_CL-49_2.png`
- CL-49 P3 (auto): `../checklist/evidence/auto/P3_CL-49_1.png`, `../checklist/evidence/auto/P3_CL-49_2.png`

## Item liên quan

- CL-49 – /profile khi chưa đăng nhập dẫn được tới Đăng nhập – Failed: P1, P2, P3
- Nhóm dữ kiện: G-19 trong `HW03/bugs/bug_groups.md` (/profile khi chưa đăng nhập: không chuyển, không có link tới Đăng nhập); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Nielsen #3 (lối thoát); Nielsen #9:** /profile khi chưa đăng nhập dẫn được tới Đăng nhập (CL-49)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-49 P1 (auto): `Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0`
- Actual nguyên văn CL-49 P2 (auto): `Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0`
- Actual nguyên văn CL-49 P3 (auto): `Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0`
- Nguồn bước tái hiện CL-49: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:256`

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
