# BUG-81

- **ID:** BUG-81
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`
- Tiền tố GitHub: [HW03-C2-81]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-59: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-59: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-59: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-59 – Lịch sử đơn
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích căn cứ)

- CL-59 – căn cứ: FR-10 (README.md:160–161)
  - FR-10, README.md:160 (AI chép nguyên văn): Trạng thái `delivered` và `canceled` là **trạng thái kết thúc** — không được phép chuyển sang bất kỳ trạng thái nào khác.
  - FR-10, README.md:161 (AI chép nguyên văn): Khi đơn hàng đã ở trạng thái `shipping`, **User không được phép tự hủy** — chỉ Admin mới có thể thao tác.
- Expected của bug: `<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- CL-59 P1 (auto): `../checklist/evidence/auto/P1_CL-59_1.png`, `../checklist/evidence/auto/P1_CL-59_2.png`
- CL-59 P2 (auto): `../checklist/evidence/auto/P2_CL-59_1.png`, `../checklist/evidence/auto/P2_CL-59_2.png`
- CL-59 P3 (auto): `../checklist/evidence/auto/P3_CL-59_1.png`, `../checklist/evidence/auto/P3_CL-59_2.png`

## Item liên quan

- CL-59 – Không cho người dùng huỷ đơn ở trạng thái không được huỷ – Failed: P1, P2, P3
- Nhóm dữ kiện: G-24 trong `HW03/bugs/bug_groups.md` (Lịch sử đơn: nút 'Hủy đơn' dùng được ở đơn đang giao); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-10 (README.md:160–161):** Không cho người dùng huỷ đơn ở trạng thái không được huỷ (CL-59)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-59 P1 (auto): `Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false`
- Actual nguyên văn CL-59 P2 (auto): `Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false`
- Actual nguyên văn CL-59 P3 (auto): `Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false`
- Nguồn bước tái hiện CL-59: tiền điều kiện (checklist): Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:713`

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
