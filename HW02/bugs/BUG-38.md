# BUG-38

- **ID:** BUG-38
- **Tiêu đề:** <SV viết>
- **Severity:** <SV viết>
- **Priority:** <SV viết>

## Môi trường

<SV viết>

## Tiền điều kiện

<SV viết>

## Các bước tái hiện

<SV viết>

## Expected (trích SRS)

<SV viết>

## Actual

<SV viết>

## Bằng chứng

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-15_ui.png`

## TC liên quan

- Fail (3): TC-FR15-15, TC-FR15-16, TC-FR15-79
- Nhóm dữ kiện: G4 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-15 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "-1000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 18, name "Muc tieu 15 1792497280777", price "1000000", category_id 1} → M_SAU {id 18, name "Muc tieu 15 1792497280777", price "-1000", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 15 1792497280777 | 30000000 ₫] [Muc tieu 15 1792497280777 | 28000000 ₫] [Muc tieu 15 1792497280777 | 45000000 ₫] [Muc tieu 15 1792497280777 | 6000000 ₫] [Muc tieu 15 1792497280777 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-15_ui.png`, `HW02/C_FR15/evidence/TC-FR15-15_failed.png`

#### TC-FR15-16 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 19, name "Muc tieu 16 1792497284060", price 1000000, category_id 1} → M_SAU {id 19, name "Muc tieu 16 1792497284060", price "", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 16 1792497284060 | 30000000 ₫] [Muc tieu 16 1792497284060 | 28000000 ₫] [Muc tieu 16 1792497284060 | 45000000 ₫] [Muc tieu 16 1792497284060 | 6000000 ₫] [Muc tieu 16 1792497284060 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-16_ui.png`, `HW02/C_FR15/evidence/TC-FR15-16_failed.png`

#### TC-FR15-79 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "0"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 76, name "Muc tieu 79 1792497378516", price "1000000", category_id 1} → M_SAU {id 76, name "Muc tieu 79 1792497378516", price "0", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 79 1792497378516 | 30000000 ₫] [Muc tieu 79 1792497378516 | 28000000 ₫] [Muc tieu 79 1792497378516 | 45000000 ₫] [Muc tieu 79 1792497378516 | 6000000 ₫] [Muc tieu 79 1792497378516 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-79_ui.png`, `HW02/C_FR15/evidence/TC-FR15-79_failed.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
