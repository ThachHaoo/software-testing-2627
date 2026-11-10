# BUG-73

- **ID:** BUG-73
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
- Tiền tố GitHub: [HW03-C2-73]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-37: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-37: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-37: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-37 – Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- CL-37 – căn cứ: FR-04.1 (README.md:64)
  - FR-04.1, README.md:64 (AI chép nguyên văn): Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- CL-37 P1 (auto): `../checklist/evidence/auto/P1_CL-37_1.png`
- CL-37 P2 (auto): `../checklist/evidence/auto/P2_CL-37_1.png`
- CL-37 P3 (auto): `../checklist/evidence/auto/P3_CL-37_1.png`

## Item liên quan

- CL-37 – Cập nhật hồ sơ được lưu bền – Failed: P1, P2, P3 · liên quan #111, #123 (SV xem: trường quay về giá trị cũ sau F5, có thể do #111 chặn lưu hoặc #123)
- Nhóm dữ kiện: G-16 trong `HW03/bugs/bug_groups.md` (Hồ sơ: sau Cập nhật + F5, trường quay về giá trị cũ); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-04.1 (README.md:64):** Cập nhật hồ sơ được lưu bền (CL-37)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-37 P1 (auto): `Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""]`
- Actual nguyên văn CL-37 P2 (auto): `Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""]`
- Actual nguyên văn CL-37 P3 (auto): `Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""]`
- Nguồn bước tái hiện CL-37: tiền điều kiện (checklist): Khôi phục giá trị cũ sau khi kiểm. · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:527`

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
