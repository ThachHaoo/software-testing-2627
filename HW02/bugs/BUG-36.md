# BUG-36

- **ID:** BUG-36
- **Tiêu đề:** Form Thêm sản phẩm (UI Admin) không kiểm tra điều kiện Giá tiền (> 0 và bắt buộc), cho phép nhập giá âm, giá bằng 0 hoặc để trống mà vẫn tạo sản phẩm thành công
- **Severity:** Major
- **Priority:** Major

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', form 'Thêm sản phẩm mới' (frontend-admin)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.

- Backend node server.js đang chạy bình thường ở trang http://localhost:3000.

- Frontend Admin frontend-admin đang chạy ở trang http://localhost:5174.

- Đã đăng nhập trang Admin bằng tài khoản `admin@eshop.com` / `Admin123!`.

- Đã truy cập vào trang Admin tại http://localhost:5174 và chuyển sang mục "Sản phẩm" để mở form "Thêm sản phẩm mới".

## Các bước tái hiện

1. Mở giao diện Admin ở link http://localhost:5174 rồi bấm chọn mục "Sản phẩm".

2. Nhập Tên sản phẩm hợp lệ (ví dụ: Tai nghe UI10).

3. Nhập dữ liệu vi phạm vào ô "Giá tiền" theo một trong các trường hợp sau:
  + Nhập số âm: -1000 (TC-FR15-10)
  + Nhập số 0: 0 (TC-FR15-67)
  + Để trống ô giá tiền: "" (TC-FR15-11)
  + Dán chuỗi chữ số toàn chiều rộng "１５０００００" — ô Giá tiền nhận giá trị rỗng "" (TC-FR15-205)

4. Chọn Danh mục bất kỳ rồi bấm nút "Lưu sản phẩm".

5. Quan sát màn hình xem có báo lỗi không và check lại danh sách sản phẩm hiển thị trên bảng cũng như CSDL qua API GET /api/products.

## Expected (trích SRS)

- Theo yêu cầu FR-15.3, Giá tiền là trường bắt buộc và phải là số dương (> 0).

- Hệ thống phải chặn không cho lưu khi nhập giá âm, giá bằng 0 hoặc để trống, đồng thời phải xuất hiện thông báo lỗi (bong bóng HTML5 hoặc alert/thông báo trên trang).

- Dữ liệu trong CSDL và trên bảng không thay đổi (không được tạo thêm bản ghi mới).

## Actual

- Hệ thống hoàn toàn không phát ra bất kỳ thông báo lỗi nào (không có alert, không có bong bóng HTML5, cũng không có thông báo trên trang).

- Vẫn tạo thành công sản phẩm mới và chèn trực tiếp vào CSDL:
  + TC-FR15-10 (giá -1000): Tạo bản ghi mới {id: 13, price: -1000}.
  + TC-FR15-67 (giá 0): Tạo bản ghi mới {id: 64, price: 0}.
  + TC-FR15-11 & TC-FR15-205 (giá rỗng ""): Tạo bản ghi mới với price để rỗng {id: 14/108, price: ""}.

- Bảng danh sách sản phẩm tự động tăng thêm 1 dòng hiển thị giá tiền âm, 0 ₫ hoặc trống ₫.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-10_ui.png`
- TC-FR15-10: `HW02/C_FR15/evidence/TC-FR15-10_ui.png`
- TC-FR15-11: `HW02/C_FR15/evidence/TC-FR15-11_ui.png`
- TC-FR15-67: `HW02/C_FR15/evidence/TC-FR15-67_ui.png`
- TC-FR15-205: `HW02/C_FR15/evidence/TC-FR15-205_ui.png`

## TC liên quan

- Fail (4): TC-FR15-10, TC-FR15-11, TC-FR15-67, TC-FR15-205
- Nhóm dữ kiện: G2 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-15.3:** (SRS) Giá: bắt buộc, phải là số dương (> 0). — (TC-10: -1000; TC-67: 0; TC-11, 205: giá rỗng được lưu)
- **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)… — (không có thông báo lỗi)
- **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail. — (không có thông báo lỗi)
- Đạt trong cùng case: —
- Chưa đánh giá được: FR-22.4

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-10): `giá trị ô Giá tiền trước khi lưu: "-1000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 13, name "Tai nghe UI10 1792497264050", price -1000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Tai nghe UI10 1792497264050 | -1000 ₫]`
- Actual nguyên văn (TC-FR15-11): `giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 14, name "Tai nghe UI11 1792497267834", price "", category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Tai nghe UI11 1792497267834 | ₫]`
- Actual nguyên văn (TC-FR15-67): `giá trị ô Giá tiền trước khi lưu: "0"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 64, name "Tai nghe BVA 67 1792497343940", price 0, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Tai nghe BVA 67 1792497343940 | 0 ₫]`
- Actual nguyên văn (TC-FR15-205): `giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 108, name "SP FullWidth Price 1792497416268", price "", category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [SP FullWidth Price 1792497416268 | ₫]`
- Lặp lại: auto_status giống nhau ở lượt 3 và lượt 5 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `frontend-admin/src/App.jsx` dòng 500–507

  ```jsx
   500                  <input
   501                    placeholder="Giá tiền"
   502                    type="number"
   503                    className="border p-2 rounded"
   504                    value={productForm.price}
   505                    onChange={(e) =>
   506                      setProductForm({ ...productForm, price: e.target.value })
   507                    }
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

- Frontend (frontend-admin/src/App.jsx, dòng 500–507) tuy có để type="number" nhưng lại thiếu thuộc tính required và thiếu thuộc tính min="1" (hoặc min="0.01"), dẫn đến trình duyệt không chặn submit khi để trống hay nhập số âm/số 0.

- Backend (backend/server.js, dòng 167–177) khi nhận request POST /api/products cũng bỏ qua bước validation trường price, cứ thế nhét thẳng vào câu lệnh SQL INSERT INTO products.

- Việc này làm dữ liệu trong CSDL bị sai lệch nghiêm trọng, cho phép bán sản phẩm với giá âm, giá 0 đồng hoặc không có giá (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
