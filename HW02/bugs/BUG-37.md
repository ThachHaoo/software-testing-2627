# BUG-37

- **ID:** BUG-37
- **Tiêu đề:** <SV viết>
- **Severity:** <SV viết>
- **Priority:** <SV viết>

## Môi trường

Chép nguyên văn từ `HW02/env/environment.md`:

| Mục | Giá trị |
|---|---|
| SUT | EShop, fork nhóm `tkob-team/eshop-sut` @ `de0f48f` (= `ttbhanh/eshop-sut` `85af3ba` + `.gitignore`, không đổi mã) |
| Máy | [...] (OS, CPU/RAM) |
| Node.js | [...] (`node -v`) |
| Trình duyệt | [...] (tên + phiên bản) |
| Backend / Web / Admin | http://localhost:3000 · :5173 · :5174 |
| Điện thoại | [...] (model, Android/iOS + phiên bản) |
| Expo Go | [...] (bản cho SDK 54) |
| Thay đổi SUT | `frontend-mobile/App.js` dòng 16 `API_URL` → IP LAN `[...]` (xem `mobile_api_url.patch`) |
| Playwright | [...] (`npx playwright --version`) |

**Đặc điểm môi trường ảnh hưởng thiết kế test**
- Backend xoá và seed lại CSDL mỗi lần khởi động; giỏ hàng lưu trong RAM.
- Tài khoản seed: admin `admin@eshop.com` / `Admin123!`, user `test@eshop.com` / `Test1234!` (setup_guide ghi `admin123`, không khớp seed).

- Commit SUT: `de0f48f`
- Locale trình duyệt: en-US

## Tiền điều kiện

<SV viết>

## Các bước tái hiện

<SV viết>

## Expected (trích SRS)

<SV viết>

## Actual

<SV viết>

## Bằng chứng

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-13_ui.png`

## TC liên quan

- Fail (3): TC-FR15-13, TC-FR15-14, TC-FR15-78
- Nhóm dữ kiện: G3 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-13 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 16, name "Muc tieu 13 1792497274144", price "1000000", category_id 1} → M_SAU {id 16, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price "1000000", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 30000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 28000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 45000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 6000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 4000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 1000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-13_ui.png`, `HW02/C_FR15/evidence/TC-FR15-13_failed.png`

#### TC-FR15-14 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 17, name "Muc tieu 14 1792497277406", price 1000000, category_id 1} → M_SAU {id 17, name "   ", price 1000000, category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [ | 30000000 ₫] [ | 28000000 ₫] [ | 45000000 ₫] [ | 6000000 ₫] [ | 4000000 ₫] [ | 1000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-14_ui.png`, `HW02/C_FR15/evidence/TC-FR15-14_failed.png`

#### TC-FR15-78 (Fail)

- **Expected:** Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 75, name "Muc tieu 78 1792497375297", price 1000000, category_id 1} → M_SAU {id 75, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price 1000000, category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 30000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 28000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 45000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 6000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 4000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 1000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-78_ui.png`, `HW02/C_FR15/evidence/TC-FR15-78_failed.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
