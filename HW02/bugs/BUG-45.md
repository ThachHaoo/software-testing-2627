# BUG-45

- **ID:** BUG-45
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', form 'Sửa sản phẩm' và bảng sản phẩm (frontend-admin)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-03_ui.png`
- TC-FR15-03: `HW02/C_FR15/evidence/TC-FR15-03_ui.png`
- TC-FR15-04: `HW02/C_FR15/evidence/TC-FR15-04_ui.png`, `HW02/C_FR15/evidence/TC-FR15-04_failed.png`
- TC-FR15-80: `HW02/C_FR15/evidence/TC-FR15-80_ui.png`, `HW02/C_FR15/evidence/TC-FR15-80_failed.png`
- TC-FR15-81: `HW02/C_FR15/evidence/TC-FR15-81_ui.png`, `HW02/C_FR15/evidence/TC-FR15-81_failed.png`
- TC-FR15-82: `HW02/C_FR15/evidence/TC-FR15-82_ui.png`, `HW02/C_FR15/evidence/TC-FR15-82_failed.png`
- TC-FR15-83: `HW02/C_FR15/evidence/TC-FR15-83_ui.png`, `HW02/C_FR15/evidence/TC-FR15-83_failed.png`

## TC liên quan

- Fail (1): TC-FR15-03
- Blocked ghi case gốc (5): TC-FR15-04, TC-FR15-80, TC-FR15-81, TC-FR15-82, TC-FR15-83 — case gốc TC-FR15-03
- Nhóm dữ kiện: G5 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-15.5:** (SRS) Khi Sửa một sản phẩm, chỉ sản phẩm đó bị thay đổi — các sản phẩm khác giữ nguyên. — (trên bảng UI: các sản phẩm khác hiển thị bị đổi tên)
- **FR-15.1:** (SRS) Admin có thể Thêm / Xem / Sửa / Xóa sản phẩm. — Xem (bảng không hiển thị giá mới của M; EC63)
- Đạt trong cùng case: Dữ liệu: M_SAU có name/price/category_id mới (TC-03); FR-15.5 ở tầng dữ liệu đạt ở TC-FR15-19 (API, Pass)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-03): `giá trị ô Giá tiền trước khi lưu: "2500000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 8, name "Muc tieu 03 1792497243367", price "1000000", category_id 1} → M_SAU {id 8, name "Sửa UI03 1792497243367", price "2500000", category_id 3}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Sửa UI03 1792497243367 | 30000000 ₫] [Sửa UI03 1792497243367 | 28000000 ₫] [Sửa UI03 1792497243367 | 45000000 ₫] [Sửa UI03 1792497243367 | 6000000 ₫] [Sửa UI03 1792497243367 | 4000000 ₫] [Sửa UI03 1792497243367 | 1000000 ₫]`
- Các case Blocked ghi case gốc TC-FR15-03 (A20): TC-FR15-04, TC-FR15-80, TC-FR15-81, TC-FR15-82, TC-FR15-83 — dữ liệu đạt; chỉ lệch ô 'Giá' của dòng M trên bảng sau Sửa (notes 6b/6c).
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `frontend-admin/src/App.jsx` dòng 105–116

  ```jsx
   105    const handleProductSubmit = async (e) => {
   106      e.preventDefault();
   107      try {
   108        if (productForm.id) {
   109          await axios.put(`${API_URL}/products/${productForm.id}`, productForm);
   110          const fakeMassUpdatedProducts = products.map((p) => ({
   111            ...p,
   112            name: productForm.name,
   113          }));
   114          setProducts(fakeMassUpdatedProducts);
   115          alert("Cập nhật thành công!");
   116        } else {
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
