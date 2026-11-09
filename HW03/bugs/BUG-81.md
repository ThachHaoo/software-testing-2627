# BUG-81

- **ID:** BUG-81
- **Nhóm dữ kiện:** G-24 (CL-59)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-59 – Không cho người dùng huỷ đơn ở trạng thái không được huỷ

- Màn hình: Lịch sử đơn
- Căn cứ: FR-10 (README.md:160–161)
- Nền tảng Failed: P1, P2, P3

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:713`

**Expected (chép từ checklist)**

> Dòng đơn 'Đang giao', 'Đã giao', 'Đã hủy' không có nút 'Hủy đơn' (hoặc nút bị vô hiệu hoá); chỉ 'Chờ xác nhận', 'Đã xác nhận' có. Fail nếu nút dùng được ở trạng thái không được huỷ.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false
- P2 (auto): Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false
- P3 (auto): Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-59_1.png`, `../checklist/evidence/auto/P1_CL-59_2.png`
- P2: `../checklist/evidence/auto/P2_CL-59_1.png`, `../checklist/evidence/auto/P2_CL-59_2.png`
- P3: `../checklist/evidence/auto/P3_CL-59_1.png`, `../checklist/evidence/auto/P3_CL-59_2.png`
