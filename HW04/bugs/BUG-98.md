# BUG-98

- **ID:** BUG-98
- **Tiêu đề (GitHub: `[HW04][FR-15] …`):** `<SV viết>`
- **Severity:** `<SV viết>` (Critical/High/Medium/Low)
- **Priority:** `<SV viết>` (High/Medium/Low)

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động); http://localhost:5174 → tab Sản phẩm (frontend-admin)
- Trình duyệt: Chrome 157.0.8103.79 (channel chrome), Edge 157.0.4341.60 (channel msedge), Firefox 159.0 (Playwright build firefox-1572)
- Công cụ: Playwright 1.65.1 (`@playwright/test`), workers 1, retries 0; spec `HW04/tests/C_FR15.spec.ts` @ `2e9e454`
- Report chính thức (2026-11-17, Asia/Saigon):
  - chrome: `HW04/reports/chrome_20261117T151143/`
  - edge: `HW04/reports/edge_20261117T151225/`
  - firefox: `HW04/reports/firefox_20261117T151306/`
- Nhật ký lượt chạy: `HW04/C_FR15/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/C_FR15/evidence/TC-FR15-15_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-15_edge.png`, `HW04/C_FR15/evidence/TC-FR15-15_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/C_FR15/evidence/TC-FR15-15_after-save_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-15_after-save_edge.png`, `HW04/C_FR15/evidence/TC-FR15-15_after-save_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR15-15
- Nhóm dữ kiện: C-G4 trong `HW04/bugs/_groups_C.md`; chi tiết `HW04/C_FR15/bug_groups.md` G4

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-38.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-15.3:** (SRS) Giá: bắt buộc, phải là số dương (> 0). — (TC-15: -1000; TC-79: 0; TC-16: rỗng)
  - **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)…
  - **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR15-15, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/C_FR15/bug_groups.md` G4):

  ```
  Error: bảng SAU_UI = TRƯỚC_UI
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 5
  + Received  + 5
  
  @@ -1,28 +1,28 @@
    Array [
      Object {
  -     "name": "iPhone 15 Pro Max",
  +     "name": "Muc tieu 15 1794903121716",
        "price": 30000000,
        "priceRaw": "30000000 ₫",
      },
      Object {
  -     "name": "Samsung Galaxy S24 Ultra",
  +     "name": "Muc tieu 15 1794903121716",
        "price": 28000000,
        "priceRaw": "28000000 ₫",
      },
      Object {
  -     "name": "MacBook Pro M3",
  +     "name": "Muc tieu 15 1794903121716",
        "price": 45000000,
        "priceRaw": "45000000 ₫",
      },
      Object {
  -     "name": "Tai nghe AirPods Pro 2",
  +     "name": "Muc tieu 15 1794903121716",
        "price": 6000000,
        "priceRaw": "6000000 ₫",
      },
      Object {
  -     "name": "Bàn phím cơ Keychron Q1",
  +     "name": "Muc tieu 15 1794903121716",
        "price": 4000000,
        "priceRaw": "4000000 ₫",
      },
      Object {
        "name": "Muc tieu 15 1794903121716",
  
  Error: GET /api/products SAU = TRƯỚC
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 1
  + Received  + 1
  
  @@ -43,8 +43,8 @@
        "category_id": 1,
        "description": "Mô tả mục tiêu 1794903121716",
        "id": 6,
        "imageUrl": "https://placehold.co/300",
        "name": "Muc tieu 15 1794903121716",
  -     "price": 1000000,
  +     "price": -1000,
      },
    ]
  
  Error: M_SAU = M_TRƯỚC
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 1
  + Received  + 1
  
  @@ -2,7 +2,7 @@
      "category_id": 1,
      "description": "Mô tả mục tiêu 1794903121716",
      "id": 6,
      "imageUrl": "https://placehold.co/300",
      "name": "Muc tieu 15 1794903121716",
  -   "price": "1000000",
  +   "price": "-1000",
    }
  ```

- Annotation trong report (TC-FR15-15): `price dạng chuỗi (BUG-48)` — GET /api/products/:id (id chẵn) trả price dạng chuỗi; `backend/server.js` dòng 162. HW02 BUG-48: https://github.com/tkob-team/eshop-sut/issues/194

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

## Liên quan

- HW02 BUG-38: https://github.com/tkob-team/eshop-sut/issues/184

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
