# BUG-38

- **ID:** BUG-38
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

- Ảnh tiêu biểu: `TC-FR15-15_ui.png`
- TC-FR15-15: `HW02/C_FR15/evidence/TC-FR15-15_ui.png`, `HW02/C_FR15/evidence/TC-FR15-15_failed.png`
- TC-FR15-16: `HW02/C_FR15/evidence/TC-FR15-16_ui.png`, `HW02/C_FR15/evidence/TC-FR15-16_failed.png`
- TC-FR15-79: `HW02/C_FR15/evidence/TC-FR15-79_ui.png`, `HW02/C_FR15/evidence/TC-FR15-79_failed.png`

## TC liên quan

- Fail (3): TC-FR15-15, TC-FR15-16, TC-FR15-79
- Nhóm dữ kiện: G4 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-15.3:** (SRS) Giá: bắt buộc, phải là số dương (> 0). — (TC-15: -1000; TC-79: 0; TC-16: rỗng)
- **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)…
- **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail.
- Đạt trong cùng case: —
- Chưa đánh giá được: FR-22.4

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-15): `giá trị ô Giá tiền trước khi lưu: "-1000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 18, name "Muc tieu 15 1792497280777", price "1000000", category_id 1} → M_SAU {id 18, name "Muc tieu 15 1792497280777", price "-1000", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 15 1792497280777 | 30000000 ₫] [Muc tieu 15 1792497280777 | 28000000 ₫] [Muc tieu 15 1792497280777 | 45000000 ₫] [Muc tieu 15 1792497280777 | 6000000 ₫] [Muc tieu 15 1792497280777 | 4000000 ₫]`
- Actual nguyên văn (TC-FR15-16): `giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 19, name "Muc tieu 16 1792497284060", price 1000000, category_id 1} → M_SAU {id 19, name "Muc tieu 16 1792497284060", price "", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 16 1792497284060 | 30000000 ₫] [Muc tieu 16 1792497284060 | 28000000 ₫] [Muc tieu 16 1792497284060 | 45000000 ₫] [Muc tieu 16 1792497284060 | 6000000 ₫] [Muc tieu 16 1792497284060 | 4000000 ₫]`
- Actual nguyên văn (TC-FR15-79): `giá trị ô Giá tiền trước khi lưu: "0"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 76, name "Muc tieu 79 1792497378516", price "1000000", category_id 1} → M_SAU {id 76, name "Muc tieu 79 1792497378516", price "0", category_id 1}; bảng TRƯỚC → SAU: 6 → 6 dòng; dòng mới/đổi trên bảng: [Muc tieu 79 1792497378516 | 30000000 ₫] [Muc tieu 79 1792497378516 | 28000000 ₫] [Muc tieu 79 1792497378516 | 45000000 ₫] [Muc tieu 79 1792497378516 | 6000000 ₫] [Muc tieu 79 1792497378516 | 4000000 ₫]`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
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
