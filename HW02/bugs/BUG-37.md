# BUG-37

- **ID:** BUG-37
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', nút 'Sửa' → form 'Sửa sản phẩm' (frontend-admin)
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

- Ảnh tiêu biểu: `TC-FR15-13_ui.png`
- TC-FR15-13: `HW02/C_FR15/evidence/TC-FR15-13_ui.png`, `HW02/C_FR15/evidence/TC-FR15-13_failed.png`
- TC-FR15-14: `HW02/C_FR15/evidence/TC-FR15-14_ui.png`, `HW02/C_FR15/evidence/TC-FR15-14_failed.png`
- TC-FR15-78: `HW02/C_FR15/evidence/TC-FR15-78_ui.png`, `HW02/C_FR15/evidence/TC-FR15-78_failed.png`

## TC liên quan

- Fail (3): TC-FR15-13, TC-FR15-14, TC-FR15-78
- Nhóm dữ kiện: G3 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-15.2:** (SRS) Tên sản phẩm: bắt buộc, tối đa 255 ký tự. — (TC-13: 300 ký tự; TC-78: 256 ký tự)
- **C3 (giả định SV chốt):** (Tên – chuỗi chỉ gồm khoảng trắng) chuỗi chỉ gồm khoảng trắng coi như trống → bị từ chối; tách lớp riêng với chuỗi rỗng. — (TC-14)
- **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)… — (không có thông báo lỗi; hộp thoại duy nhất là 'Cập nhật thành công!')
- **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail. — (không có thông báo lỗi; hộp thoại duy nhất là 'Cập nhật thành công!')
- Đạt trong cùng case: —
- Chưa đánh giá được: FR-22.4

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-13): `giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 16, name "Muc tieu 13 1792497274144", price "1000000", category_id 1} → M_SAU {id 16, name ""x"×300", price "1000000", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 30000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 28000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 45000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 6000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 4000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 1000000 ₫]` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
- Actual nguyên văn (TC-FR15-14): `giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 17, name "Muc tieu 14 1792497277406", price 1000000, category_id 1} → M_SAU {id 17, name "   ", price 1000000, category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [ | 30000000 ₫] [ | 28000000 ₫] [ | 45000000 ₫] [ | 6000000 ₫] [ | 4000000 ₫] [ | 1000000 ₫]`
- Actual nguyên văn (TC-FR15-78): `giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 75, name "Muc tieu 78 1792497375297", price 1000000, category_id 1} → M_SAU {id 75, name ""x"×256", price 1000000, category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 30000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 28000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 45000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 6000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 4000000 ₫] [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 1000000 ₫]` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
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
- Đoạn code trích nguyên văn: `backend/server.js` dòng 179–189

  ```js
   179  app.put("/api/products/:id", (req, res) => {
   180    const { name, price, description, imageUrl, category_id } = req.body;
   181    db.run(
   182      "UPDATE products SET name = ?, price = ?, description = ?, imageUrl = ?, category_id = ? WHERE id = ?",
   183      [name, price, description, imageUrl, category_id, req.params.id],
   184      function (err) {
   185        if (err) return res.status(500).json({ error: err.message });
   186        res.json({ message: "Product updated" });
   187      },
   188    );
   189  });
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
