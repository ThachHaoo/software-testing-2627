# BUG-45

- **ID:** BUG-45
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

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-03_ui.png`

## TC liên quan

- Fail (1): TC-FR15-03
- Blocked ghi case gốc (5): TC-FR15-04, TC-FR15-80, TC-FR15-81, TC-FR15-82, TC-FR15-83 — case gốc TC-FR15-03
- Nhóm dữ kiện: G5 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-03 (Fail)

- **Expected:** Không đánh giá thông báo. Bảng: dòng của M hiển thị 'Tên SP' = 'Sửa UI03 {ts}', 'Giá' = 2500000 (so giá trị số); mọi dòng khác SAU_UI = TRƯỚC_UI; số dòng không đổi. Dữ liệu: M_SAU có name = 'Sửa UI03 {ts}', price = 2500000, category_id = 3 (so giá trị số).
- **Actual:** giá trị ô Giá tiền trước khi lưu: "2500000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 8, name "Muc tieu 03 1792497243367", price "1000000", category_id 1} → M_SAU {id 8, name "Sửa UI03 1792497243367", price "2500000", category_id 3}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Sửa UI03 1792497243367 | 30000000 ₫] [Sửa UI03 1792497243367 | 28000000 ₫] [Sửa UI03 1792497243367 | 45000000 ₫] [Sửa UI03 1792497243367 | 6000000 ₫] [Sửa UI03 1792497243367 | 4000000 ₫] [Sửa UI03 1792497243367 | 1000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-03_ui.png`

#### TC-FR15-04 (Blocked)

- **Expected:** Bảng: dòng của M hiển thị 'Giá' = 2500000.5 (so giá trị số). Dữ liệu: M_SAU có price = 2500000.5 (so giá trị số); name, category_id = M_TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "2500000.5"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 9, name "Muc tieu 04 1792497246840", price 1000000, category_id 1} → M_SAU {id 9, name "Muc tieu 04 1792497246840", price 2500000.5, category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 04 1792497246840 | 30000000 ₫] [Muc tieu 04 1792497246840 | 28000000 ₫] [Muc tieu 04 1792497246840 | 45000000 ₫] [Muc tieu 04 1792497246840 | 6000000 ₫] [Muc tieu 04 1792497246840 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-04_ui.png`, `HW02/C_FR15/evidence/TC-FR15-04_failed.png`

#### TC-FR15-80 (Blocked)

- **Expected:** Bảng: dòng của M hiển thị 'Giá' = 0.1 (so giá trị số). Dữ liệu: M_SAU có price = 0.1 (so giá trị số); name, category_id = M_TRƯỚC; số bản ghi SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "0.1"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 77, name "Muc tieu 80 1792497381784", price 1000000, category_id 1} → M_SAU {id 77, name "Muc tieu 80 1792497381784", price 0.1, category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 80 1792497381784 | 30000000 ₫] [Muc tieu 80 1792497381784 | 28000000 ₫] [Muc tieu 80 1792497381784 | 45000000 ₫] [Muc tieu 80 1792497381784 | 6000000 ₫] [Muc tieu 80 1792497381784 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-80_ui.png`, `HW02/C_FR15/evidence/TC-FR15-80_failed.png`

#### TC-FR15-81 (Blocked)

- **Expected:** Bảng: dòng của M hiển thị 'Giá' = 0.2 (so giá trị số). Dữ liệu: M_SAU có price = 0.2 (so giá trị số); name, category_id = M_TRƯỚC; số bản ghi SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "0.2"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 78, name "Muc tieu 81 1792497385011", price "1000000", category_id 1} → M_SAU {id 78, name "Muc tieu 81 1792497385011", price "0.2", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 81 1792497385011 | 30000000 ₫] [Muc tieu 81 1792497385011 | 28000000 ₫] [Muc tieu 81 1792497385011 | 45000000 ₫] [Muc tieu 81 1792497385011 | 6000000 ₫] [Muc tieu 81 1792497385011 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-81_ui.png`, `HW02/C_FR15/evidence/TC-FR15-81_failed.png`

#### TC-FR15-82 (Blocked)

- **Expected:** Bảng: dòng của M hiển thị 'Giá' = 1500000 (so giá trị số). Dữ liệu: M_SAU có price = 1500000 (so giá trị số); name, category_id = M_TRƯỚC; số bản ghi SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 79, name "Muc tieu 82 1792497388349", price 1000000, category_id 1} → M_SAU {id 79, name "Muc tieu 82 1792497388349", price 1500000, category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 82 1792497388349 | 30000000 ₫] [Muc tieu 82 1792497388349 | 28000000 ₫] [Muc tieu 82 1792497388349 | 45000000 ₫] [Muc tieu 82 1792497388349 | 6000000 ₫] [Muc tieu 82 1792497388349 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-82_ui.png`, `HW02/C_FR15/evidence/TC-FR15-82_failed.png`

#### TC-FR15-83 (Blocked)

- **Expected:** Bảng: dòng của M hiển thị 'Giá' = 1000000000000 (so giá trị số). Dữ liệu: M_SAU có price = 1000000000000 (so giá trị số); name, category_id = M_TRƯỚC; số bản ghi SAU = TRƯỚC.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1000000000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 80, name "Muc tieu 83 1792497391707", price "1000000", category_id 1} → M_SAU {id 80, name "Muc tieu 83 1792497391707", price "1000000000000", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 83 1792497391707 | 30000000 ₫] [Muc tieu 83 1792497391707 | 28000000 ₫] [Muc tieu 83 1792497391707 | 45000000 ₫] [Muc tieu 83 1792497391707 | 6000000 ₫] [Muc tieu 83 1792497391707 | 4000000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-83_ui.png`, `HW02/C_FR15/evidence/TC-FR15-83_failed.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
