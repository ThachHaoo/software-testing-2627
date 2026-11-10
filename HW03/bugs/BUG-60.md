# BUG-60

- **ID:** BUG-60
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
- Tiền tố GitHub: [HW03-C2-60]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-14: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-14: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-14: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-14 – Tất cả màn C2
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- CL-14 – căn cứ: WCAG 2.2 SC 3.1.1 (Language of Page)
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- CL-14 P1 (auto): `../checklist/evidence/auto/P1_CL-14_1.png`
- CL-14 P2 (auto): `../checklist/evidence/auto/P2_CL-14_1.png`
- CL-14 P3 (auto): `../checklist/evidence/auto/P3_CL-14_1.png`

## Item liên quan

- CL-14 – Khai báo ngôn ngữ trang là tiếng Việt – Failed: P1, P2, P3
- Nhóm dữ kiện: G-03 trong `HW03/bugs/bug_groups.md` (<html lang="en">); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **WCAG 2.2 SC 3.1.1 (Language of Page):** Khai báo ngôn ngữ trang là tiếng Việt (CL-14)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-14 P1 (auto): `Lỗi: Error: lang = "en" · <html lang="en">`
- Actual nguyên văn CL-14 P2 (auto): `Lỗi: Error: lang = "en" · <html lang="en">`
- Actual nguyên văn CL-14 P3 (auto): `Lỗi: Error: lang = "en" · <html lang="en">`
- Nguồn bước tái hiện CL-14: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:82`

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
