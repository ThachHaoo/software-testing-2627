# BUG-97

- **ID:** BUG-97
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

- Ảnh lúc kết thúc: `HW04/C_FR15/evidence/TC-FR15-11_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-11_edge.png`, `HW04/C_FR15/evidence/TC-FR15-11_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/C_FR15/evidence/TC-FR15-11_after-save_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-11_after-save_edge.png`, `HW04/C_FR15/evidence/TC-FR15-11_after-save_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR15-11
- Nhóm dữ kiện: C-G3 trong `HW04/bugs/_groups_C.md`; chi tiết `HW04/C_FR15/bug_groups.md` G3

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-36.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-15.3:** (SRS) Giá: bắt buộc, phải là số dương (> 0). — (TC-10: -1000; TC-67: 0; TC-11, 205: giá rỗng được lưu)
  - **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)… — (không có thông báo lỗi)
  - **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail. — (không có thông báo lỗi)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR15-11, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/C_FR15/bug_groups.md` G3):

  ```
  Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: true
  Received: false
  
  Error: bảng SAU_UI = TRƯỚC_UI
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 0
  + Received  + 5
  
  @@ -22,6 +22,11 @@
      Object {
        "name": "Bàn phím cơ Keychron Q1",
        "price": 4000000,
        "priceRaw": "4000000 ₫",
      },
  +   Object {
  +     "name": "Tai nghe UI11 1794903118181",
  +     "price": null,
  +     "priceRaw": "₫",
  +   },
    ]
  
  Error: GET /api/products SAU = TRƯỚC
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 0
  + Received  + 8
  
  @@ -37,6 +37,14 @@
        "id": 5,
        "imageUrl": "https://placehold.co/300x300/png?text=Keychron+Q1",
        "name": "Bàn phím cơ Keychron Q1",
        "price": 4000000,
      },
  +   Object {
  +     "category_id": 2,
  +     "description": "Mô tả NN 1794903118181",
  +     "id": 6,
  +     "imageUrl": "https://placehold.co/300",
  +     "name": "Tai nghe UI11 1794903118181",
  +     "price": "",
  +   },
    ]
  ```

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

`<SV viết>`

## Liên quan

- HW02 BUG-36: https://github.com/tkob-team/eshop-sut/issues/182

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
