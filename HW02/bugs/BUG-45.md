# BUG-45

- **ID:** BUG-45
- **Tiêu đề:** Form Sửa sản phẩm (UI Admin) cập nhật đè tên của sản phẩm vừa sửa lên toàn bộ các sản phẩm khác trên bảng danh sách UI và không cập nhật lại Giá tiền mới trên bảng
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', form 'Sửa sản phẩm' và bảng sản phẩm (frontend-admin)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.

- Backend node server.js đang chạy bình thường ở cổng http://localhost:3000.

- Frontend Admin frontend-admin đang chạy ở trang http://localhost:5174.

- Đã đăng nhập trang Admin bằng tài khoản `admin@eshop.com` / `Admin123!`.

- Đã truy cập vào trang Admin tại http://localhost:5174, chọn mục "Sản phẩm" và bấm nút "Sửa" tại một sản phẩm bất kỳ để mở form "Sửa sản phẩm".

## Các bước tái hiện

1. Mở giao diện Admin ở link http://localhost:5174 rồi bấm chọn mục "Sản phẩm".

2. Tại bảng danh sách sản phẩm, chọn một sản phẩm mục tiêu (ví dụ dòng "iPhone 15 Pro Max", id = 1) và bấm nút "Sửa".

3. Nhập dữ liệu hợp lệ mới để cập nhật cho sản phẩm (ví dụ đổi Tên sản phẩm thành Sửa UI03 và Giá tiền thành 2500000).

4. Bấm nút "Lưu sản phẩm".

5. Quan sát dữ liệu hiển thị trên bảng danh sách sản phẩm ở giao diện UI Admin và đối chiếu với dữ liệu thực tế lưu trong CSDL.

## Expected (trích SRS)

- Theo yêu cầu FR-15.5, khi sửa một sản phẩm thì chỉ sản phẩm đó bị thay đổi thông tin, tất cả các sản phẩm khác phải giữ nguyên.

- Bảng danh sách sản phẩm trên giao diện phải hiển thị đúng tên mới và giá tiền mới của riêng sản phẩm vừa sửa, thông tin của các sản phẩm còn lại không bị ảnh hưởng.

- Dữ liệu trong CSDL và dữ liệu hiển thị trên bảng UI phải đồng nhất với nhau.

## Actual

- Trong CSDL thì dữ liệu sản phẩm mục tiêu đã được cập nhật đúng tên mới và giá mới (name = "Sửa UI03", price = 2500000).

- Tuy nhiên trên giao diện bảng sản phẩm UI Admin bị lỗi hiển thị nghiêm trọng:
  + Tất cả các sản phẩm khác trong danh sách đều bị đè tên thành Tên sản phẩm vừa sửa (Sửa UI03).
  + Dòng hiển thị của sản phẩm vừa sửa không cập nhật lại Giá tiền mới (2500000) mà vẫn giữ nguyên giá cũ trên bảng UI (TC-FR15-03: 1000000 ₫; tái hiện 7c với "iPhone 15 Pro Max": 30000000 ₫).

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

- Ở Frontend (frontend-admin/src/App.jsx, dòng 105–116): Trong hàm handleProductSubmit xử lý khi sửa sản phẩm (luồng if (productForm.id)), code cập nhật state bị viết sai logic trầm trọng tại dòng 110–114:
  + Code dùng products.map((p) => ({ ...p, name: productForm.name })) để duyệt qua toàn bộ danh sách và gán lại name mới cho MỌI sản phẩm thay vì chỉ tìm đúng sản phẩm có id === productForm.id để cập nhật.
  + Đồng thời code hoàn toàn không cập nhật lại price mới vào state products, khiến cho giá tiền trên bảng hiển thị vẫn bị giữ nguyên giá cũ.

- Mặc dù CSDL được lưu đúng nhưng giao diện quản trị bị hỏng hoàn toàn hiển thị sau thao tác sửa, làm sai lệch tên toàn bộ danh sách và hiển thị sai giá thực tế của sản phẩm.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/191

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
