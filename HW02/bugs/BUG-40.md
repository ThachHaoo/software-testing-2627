# BUG-40

- **ID:** BUG-40
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

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-201_ui.png`

## TC liên quan

- Fail (1): TC-FR15-201
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-201 (Fail)

- **Expected:** Form chặn do type=number.
- **Actual:** giá trị ô Giá tiền trước khi lưu: "1e5"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 106, name "Sản phẩm E-Notation 1792497408679", price 100000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Sản phẩm E-Notation 1792497408679 | 100000 ₫]
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-201_ui.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
