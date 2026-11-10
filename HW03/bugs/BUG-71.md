# BUG-71

- **ID:** BUG-71
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
- Tiền tố GitHub: [HW03-C2-71]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay · CL-06: lượt `runs/P1_manual_20261109-2257.md`, 22:58 09/11/2026 - 00:10 10/11/2026
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay · CL-06: lượt `runs/P2_manual_20261110-0010.md`, 00:10 10/11/2026 - 00:38 10/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay · CL-06: lượt `runs/P3_manual_20261110-0046.md`, 00:46 10/11/2026 - 01:54 10/11/2026
- Màn hình: CL-06 – Quên mật khẩu (bước 2)
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- CL-06 – căn cứ: Shneiderman #1 (nhất quán); checklist Button – 'colour signals intent'
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- CL-06 P1 (tay): `../checklist/evidence/P1_chrome/P1_CL-06_1.png`
- CL-06 P2 (tay): `../checklist/evidence/P2_firefox/P2_CL-06_1.png`
- CL-06 P3 (tay): `../checklist/evidence/P3_android/P3_CL-06_1.png`

## Item liên quan

- CL-06 – Nút chính và nút phụ phân biệt được bằng hình thức – Failed: P1, P2, P3
- Nhóm dữ kiện: G-14 trong `HW03/bugs/bug_groups.md` (Quên mật khẩu B2: nút chính và nút phụ giống nhau (G-13 cũ giữ gộp; CL-04 trùng #160 nên còn CL-06)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Shneiderman #1 (nhất quán); checklist Button – 'colour signals intent':** Nút chính và nút phụ phân biệt được bằng hình thức (CL-06)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-06 P1 (tay): `Nút chính và nút phụ giống nhau`
- Actual nguyên văn CL-06 P2 (tay): `Nút chính và nút phụ giống nhau`
- Actual nguyên văn CL-06 P3 (tay): `Nút chính và nút phụ giống nhau`
- Nguồn bước tái hiện CL-06: tiền điều kiện (checklist): – · cách kiểm: auto: Fail khi hai nút trùng cả màu nền, kích thước, viền; khác nhau → SV xác nhận 'khác nhau rõ' · test tự động: `HW03/tests/C2.spec.ts:399`

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
