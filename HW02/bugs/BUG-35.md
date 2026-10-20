# BUG-35

- **ID:** BUG-35
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', form 'Thêm sản phẩm mới' (frontend-admin)
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

- Ảnh tiêu biểu: `TC-FR15-08_ui.png`
- TC-FR15-08: `HW02/C_FR15/evidence/TC-FR15-08_ui.png`
- TC-FR15-09: `HW02/C_FR15/evidence/TC-FR15-09_ui.png`
- TC-FR15-66: `HW02/C_FR15/evidence/TC-FR15-66_ui.png`

## TC liên quan

- Fail (3): TC-FR15-08, TC-FR15-09, TC-FR15-66
- Nhóm dữ kiện: G1 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-15.2:** (SRS) Tên sản phẩm: bắt buộc, tối đa 255 ký tự. — (TC-08, 66: 300/256 ký tự)
- **C3 (giả định SV chốt):** (Tên – chuỗi chỉ gồm khoảng trắng) chuỗi chỉ gồm khoảng trắng coi như trống → bị từ chối; tách lớp riêng với chuỗi rỗng. — (TC-09: 3 dấu cách)
- **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)… — (không có thông báo lỗi)
- **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail. — (không có thông báo lỗi)
- Đạt trong cùng case: —
- Chưa đánh giá được: FR-22.4 (không có thông báo nên chưa xét vị trí)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-08): `giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 11, name ""x"×300", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(300 ký tự) | 1500000 ₫]` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
- Actual nguyên văn (TC-FR15-09): `giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 12, name "   ", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [ | 1500000 ₫]`
- Actual nguyên văn (TC-FR15-66): `giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 63, name ""x"×256", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [xxxxxxxxxxxxxxxxxxxx…(256 ký tự) | 1500000 ₫]` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `frontend-admin/src/App.jsx` dòng 491–499

  ```jsx
   491                  <input
   492                    placeholder="Tên sản phẩm"
   493                    className="border p-2 rounded"
   494                    value={productForm.name}
   495                    onChange={(e) =>
   496                      setProductForm({ ...productForm, name: e.target.value })
   497                    }
   498                    required
   499                  />
  ```
- Đoạn code trích nguyên văn: `backend/server.js` dòng 167–177

  ```js
   167  app.post("/api/products", (req, res) => {
   168    const { name, price, description, imageUrl, category_id } = req.body;
   169    db.run(
   170      "INSERT INTO products (name, price, description, imageUrl, category_id) VALUES (?, ?, ?, ?, ?)",
   171      [name, price, description, imageUrl, category_id],
   172      function (err) {
   173        if (err) return res.status(500).json({ error: err.message });
   174        res.json({ message: "Product created", id: this.lastID });
   175      },
   176    );
   177  });
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
