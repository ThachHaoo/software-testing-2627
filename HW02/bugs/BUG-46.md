# BUG-46

- **ID:** BUG-46
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Client: Playwright 1.48.2 APIRequestContext (lượt 6); kiểm tái hiện bằng PowerShell 5.1 Invoke-WebRequest (7/7a)
- API GET, PUT, DELETE http://localhost:3000/api/products/:id
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

- Ảnh tiêu biểu: `TC-FR15-47_api.png`
- TC-FR15-47: `HW02/C_FR15/evidence/TC-FR15-47_req.json`, `HW02/C_FR15/evidence/TC-FR15-47_res.json`, `HW02/C_FR15/evidence/TC-FR15-47_api.png`
- TC-FR15-48: `HW02/C_FR15/evidence/TC-FR15-48_req.json`, `HW02/C_FR15/evidence/TC-FR15-48_res.json`, `HW02/C_FR15/evidence/TC-FR15-48_api.png`
- TC-FR15-49: `HW02/C_FR15/evidence/TC-FR15-49_req.json`, `HW02/C_FR15/evidence/TC-FR15-49_res.json`, `HW02/C_FR15/evidence/TC-FR15-49_api.png`

## TC liên quan

- Fail (3): TC-FR15-47, TC-FR15-48, TC-FR15-49
- Nhóm dữ kiện: G10 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **C10 (giả định SV chốt):** (id không tồn tại khi Xem/Sửa/Xóa) GET/PUT/DELETE /api/products/:id với id không có trong CSDL → 4xx (không 2xx, không 5xx), không tạo bản ghi mới, các sản phẩm khác không đổi. Chỉ tạo được ở tầng API (UI chỉ chọn được sản phẩm đang hiển thị).
- Đạt trong cùng case: Dữ liệu không đổi (SAU = TRƯỚC) ở cả 3 case
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-47): `HTTP 200 {}; bản ghi TRƯỚC → SAU: 5 → 5`
- Actual nguyên văn (TC-FR15-48): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 5 → 5`
- Actual nguyên văn (TC-FR15-49): `HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 5 → 5`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 159–165

  ```js
   159  app.get("/api/products/:id", (req, res) => {
   160    db.get("SELECT * FROM products WHERE id = ?", [req.params.id], (err, row) => {
   161      if (!row) return res.status(200).json({});
   162      if (row.id % 2 === 0) row.price = row.price.toString();
   163      res.json(row);
   164    });
   165  });
  ```
- Đoạn code trích nguyên văn: `backend/server.js` dòng 179–196

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
   190  
   191  app.delete("/api/products/:id", (req, res) => {
   192    db.run("DELETE FROM products WHERE id = ?", [req.params.id], function (err) {
   193      if (err) return res.status(500).json({ error: err.message });
   194      res.json({ message: "Product deleted" });
   195    });
   196  });
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
