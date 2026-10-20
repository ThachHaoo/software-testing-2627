# BUG-39

- **ID:** BUG-39
- **Tiêu đề:** Form Thêm sản phẩm (UI Admin) không kiểm tra và chặn Tên sản phẩm chứa thẻ script, cho phép lưu chuỗi XSS <script>alert(1)</script> vào hệ thống mà không có thông báo lỗi
- **Severity:** Critical
- **Priority:** High

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

2. Tại form "Thêm sản phẩm mới", nhập mã script vào ô "Tên sản phẩm": <script>alert(1)</script>.

3. Nhập Giá tiền hợp lệ (ví dụ: 1500000) và chọn Danh mục hợp lệ (ví dụ: Laptop).

4. Bấm nút "Lưu sản phẩm".

5. Quan sát phản hồi trên giao diện (xem có thông báo lỗi hay không) và kiểm tra lại danh sách sản phẩm hiển thị trên bảng UI cũng như dữ liệu chèn vào CSDL qua API GET /api/products.

## Expected (trích SRS)

- Theo yêu cầu C21 (quy định xử lý tên sản phẩm chứa mã script), hệ thống phải từ chối không cho lưu sản phẩm có tên chứa đoạn script nguy hiểm.

- Hệ thống phải hiển thị thông báo lỗi rõ ràng (qua bong bóng HTML5, alert báo lỗi hoặc thông báo trên trang) để cảnh báo dữ liệu không hợp lệ.

- Dữ liệu trong CSDL và trên bảng UI không được thay đổi (không chèn thêm bản ghi mới).

## Actual

- Hệ thống không hề đưa ra bất kỳ thông báo lỗi nào (không alert, không bong bóng HTML5 validation, không thông báo trên trang).

- Tạo mới thành công sản phẩm và lưu trực tiếp đoạn mã script vào CSDL với id mới: {id: 105, name: "<script>alert(1)</script>", price: 1500000, category_id: 2}.

- Bảng danh sách sản phẩm trên giao diện tăng từ 5 lên 6 dòng và hiển thị tên sản phẩm là <script>alert(1)</script> (mặc dù React đã encode chuỗi nên chưa kích hoạt lệnh alert(1) ngay trên UI nhưng bản ghi XSS vẫn được lưu thành công vào CSDL).

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-200_ui.png`
- TC-FR15-200: `HW02/C_FR15/evidence/TC-FR15-200_ui.png`

## TC liên quan

- Fail (1): TC-FR15-200
- Nhóm dữ kiện: G6 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **C21 (giả định SV chốt):** (tên sản phẩm chứa mã script — TC-FR15-200) (SV chưa ghi nội dung riêng; Expected nằm ở TC-FR15-200). — (SV chốt)
- **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)… — (không có thông báo lỗi)
- **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail. — (không có thông báo lỗi)
- Đạt trong cùng case: SEC-04 trong cùng case: không có hộp thoại '1'; bảng hiển thị chữ nguyên văn
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-200): `giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 105, name "<script>alert(1)</script>", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [<script>alert(1)</script> | 1500000 ₫]`
- Lặp lại: TC-FR15-200: lượt 3 passed, lượt 6 failed — lượt 3/5 là lượt thử (harness lỗi H1–H4); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
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

- Ở Frontend (frontend-admin/src/App.jsx, dòng 491–499): Ô nhập Tên sản phẩm chỉ có thuộc tính required, không có bất kỳ cơ chế sanitize, validate hoặc regex nào để lọc/chặn các đoạn script nguy hiểm trước khi gửi request về server.

- Ở Backend (backend/server.js, dòng 167–177): Endpoint POST /api/products nhận dữ liệu từ req.body và lưu thẳng vào CSDL SQLite bằng lệnh INSERT INTO products mà không hề kiểm tra hay loại bỏ mã script nguy hiểm trong chuỗi name.

- Lỗi này tạo tiền đề cho lỗ hổng Stored XSS (Stored Cross-Site Scripting) trong CSDL, cực kỳ nguy hiểm nếu các giao diện khác (như trang Web bán hàng Client, ứng dụng Mobile, hay báo cáo Admin) lấy tên sản phẩm này ra render bằng innerHTML/dangerouslySetInnerHTML mà không escape kỹ.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/185

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
