# BUG-36

- **ID:** BUG-36
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

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-10_ui.png`

## TC liên quan

- Fail (4): TC-FR15-10, TC-FR15-11, TC-FR15-67, TC-FR15-205
- Nhóm dữ kiện: G2 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-10 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "-1000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 13, name "Tai nghe UI10 1792497264050", price -1000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Tai nghe UI10 1792497264050 | -1000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-10_ui.png`

#### TC-FR15-11 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 14, name "Tai nghe UI11 1792497267834", price "", category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Tai nghe UI11 1792497267834 | ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-11_ui.png`

#### TC-FR15-67 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "0"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 64, name "Tai nghe BVA 67 1792497343940", price 0, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Tai nghe BVA 67 1792497343940 | 0 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-67_ui.png`

#### TC-FR15-205 (Fail)

- **Expected:** Form chặn không cho nhập/dán, hoặc báo lỗi Giá tiền bắt buộc/không hợp lệ; không lưu rác vào CSDL.
- **Actual:** giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 108, name "SP FullWidth Price 1792497416268", price "", category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [SP FullWidth Price 1792497416268 | ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-205_ui.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
