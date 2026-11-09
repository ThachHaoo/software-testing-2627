# BUG-82

- **ID:** BUG-82
- **Nhóm dữ kiện:** G-25 (CL-60)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-60 – Huỷ đơn có hộp xác nhận

- Màn hình: Lịch sử đơn
- Căn cứ: Shneiderman #6 (cho phép đảo ngược); checklist Button – 'Uncorrectable action → Yes/No confirmation'
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #165 (#165 là xoá dòng giỏ; huỷ đơn chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Có ≥ 1 đơn Chờ xác nhận.
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:795`

**Expected (chép từ checklist)**

> Bấm 'Hủy đơn' → hiện hộp xác nhận có lựa chọn huỷ thao tác; chọn không → đơn giữ nguyên trạng thái. Fail nếu đơn bị huỷ ngay khi bấm.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: không có hộp xác nhận · Lỗi: Error: đơn bị huỷ ngay (trạng thái canceled) · hộp thoại: ["alert: Hủy đơn thành công!"]; trạng thái đơn sau khi chọn "không": canceled
- P2 (auto): Lỗi: Error: không có hộp xác nhận · Lỗi: Error: đơn bị huỷ ngay (trạng thái canceled) · hộp thoại: ["alert: Hủy đơn thành công!"]; trạng thái đơn sau khi chọn "không": canceled
- P3 (auto): Lỗi: Error: không có hộp xác nhận · Lỗi: Error: đơn bị huỷ ngay (trạng thái canceled) · hộp thoại: ["alert: Hủy đơn thành công!"]; trạng thái đơn sau khi chọn "không": canceled

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-60_1.png`
- P2: `../checklist/evidence/auto/P2_CL-60_1.png`
- P3: `../checklist/evidence/auto/P3_CL-60_1.png`
