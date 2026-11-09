# BUG-83

- **ID:** BUG-83
- **Nhóm dữ kiện:** G-26 (CL-62)
- **Tiêu đề:** 🔒 SV viết
- **Mô tả:** 🔒 SV viết
- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)
- **Severity:** 🔒 SV chọn
- **Priority:** 🔒 SV chọn
- **Nhận định:** 🔒 SV viết
- **GitHub Issue:** (sau khi tạo)

---

## Dữ kiện (AI chép từ `checklist.json`, không sửa)

### CL-62 – Empty state có hình minh hoạ và thông báo thân thiện

- Màn hình: Lịch sử đơn
- Căn cứ: FR-24.3 (README.md:269)
- Nền tảng Failed: P1, P2, P3 · trùng một phần/liên quan: #167 (#167 là giỏ trống; Lịch sử đơn trống chưa có issue)

**Môi trường**

- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay
- SUT: tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)

**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**

- Tiền điều kiện (checklist): Backend vừa restart (test@eshop.com chưa có đơn).
- Cách kiểm (checklist): auto: có img/svg/icon trong khu lịch sử đơn + có câu thông báo; 'thân thiện' → SV
- Test tự động: `HW03/tests/C2.spec.ts:39`

**Expected (chép từ checklist)**

> Tài khoản chưa có đơn → khu Lịch sử đơn có icon/hình minh hoạ và câu thông báo thân thiện (kèm gợi ý mua sắm). Fail nếu chỉ có chữ, không có icon/hình.

**Actual (chép notes / số đo)**

- P1 (tay): Mặc dù có thông báo thân thiện nhưng không có img/svg/icon
- P2 (tay): Mặc dù có thông báo thân thiện nhưng không có img/svg/icon
- P3 (tay): Mặc dù có thông báo thân thiện nhưng không có img/svg/icon

**Ảnh**

- P1: `../checklist/evidence/P1_chrome/P1_CL-62_1.png`
- P2: `../checklist/evidence/P2_firefox/P2_CL-62_1.png`
- P3: `../checklist/evidence/P3_android/P3_CL-62_1.png`
