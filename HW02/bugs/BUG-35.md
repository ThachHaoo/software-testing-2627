# BUG-35

- **ID:** BUG-35
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

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-08_ui.png`

## TC liên quan

- Fail (3): TC-FR15-08, TC-FR15-09, TC-FR15-66
- Nhóm dữ kiện: G1 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-08 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 11, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 1500000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-08_ui.png`

#### TC-FR15-09 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 12, name "   ", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [ | 1500000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-09_ui.png`

#### TC-FR15-66 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 63, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 1500000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-66_ui.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
