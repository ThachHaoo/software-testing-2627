# BUG-72

- **ID:** BUG-72
- **Nhóm dữ kiện:** G-15 (CL-32)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-32 – SĐT không hợp lệ bị từ chối, thông báo nêu đúng quy tắc

- Màn hình: Hồ sơ
- Căn cứ: FR-04.2 (README.md:65); Nielsen #9
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #97, #113 (#97 (API lưu SĐT 9 số), #113 (Web nhận đầu khác 0); phần thông báo không nêu quy tắc chưa có issue)

**Môi trường**

- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): –
- Cách kiểm (checklist): –
- Test tự động: `HW03/tests/C2.spec.ts:488`

**Expected (chép từ checklist)**

> Nhập '912345678' (không bắt đầu bằng 0) → bị từ chối, không lưu; thông báo nêu 'bắt đầu bằng 0, 10–11 chữ số'. Fail nếu được lưu hoặc thông báo nêu quy tắc khác SRS.

**Actual (chép notes / số đo)**

- P1 (auto): Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"
- P2 (auto): Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"
- P3 (auto): Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"

**Ảnh**

- P1: `../checklist/evidence/auto/P1_CL-32_1.png`
- P2: `../checklist/evidence/auto/P2_CL-32_1.png`
- P3: `../checklist/evidence/auto/P3_CL-32_1.png`
