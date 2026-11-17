# BUG-98

- **ID:** BUG-98
- **Tiêu đề (GitHub: `[HW04][FR-15] …`):** `[HW04][FR-15] Hệ thống cho phép sửa sản phẩm với giá âm (-1000) và lưu vào cơ sở dữ liệu`
- **Severity:** High
- **Priority:** High

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

- Hệ thống frontend-admin (`http://localhost:5174`) và backend (`node server.js`) đang hoạt động bình thường.
- Người dùng đã đăng nhập trang quản trị (Admin) và đang ở tab Quản lý Sản phẩm.
- Sản phẩm mục tiêu `M` tồn tại trong danh sách sản phẩm với `id = 6`, `name = "Muc tieu 15 1794903121716"`, `price = 1000000`, `category_id = 1`, `description = "Mô tả mục tiêu 1794903121716"`, `imageUrl = "https://placehold.co/300"`.

## Các bước tái hiện

1. Truy cập trang quản trị (`http://localhost:5174`), mở tab **Sản phẩm**.
2. Chọn thao tác **Sửa** trên dòng sản phẩm mục tiêu `M` (`Muc tieu 15 1794903121716`).
3. Tại ô **Giá tiền**, nhập giá trị âm `-1000` (giữ nguyên các thông tin hợp lệ khác).
4. Nhấn nút lưu form cập nhật sản phẩm.
5. Quan sát hộp thoại/thông báo lỗi, bảng danh sách sản phẩm trên UI và dữ liệu trả về từ `GET /api/products` cũng như `GET /api/products/6`.

## Expected (trích SRS)

- Hệ thống từ chối cập nhật sản phẩm vì giá phải là số dương lớn hơn `0` (**FR-15.3**).
- Hiển thị thông báo lỗi hợp lệ (bong bóng HTML5, hộp thoại trình duyệt hoặc thông báo trên trang theo giả định **C7**, **C16**).
- Dữ liệu không thay đổi: bản ghi mục tiêu giữ nguyên `M_SAU = M_TRƯỚC` (`price = 1000000`), `GET /api/products SAU = TRƯỚC`, và bảng danh sách sản phẩm trên UI giữ nguyên `SAU_UI = TRƯỚC_UI`.

## Actual

- Hệ thống không từ chối mà vẫn cập nhật thành công và hiện hộp thoại `"Cập nhật thành công!"`.
- API `GET /api/products` trả về bản ghi `id = 6` có `price = -1000`; `GET /api/products/6` (`M_SAU`) trả về `price = "-1000"` (bị đổi từ `1000000` thành `-1000`).
- Ngoài ra, trên bảng danh sách sản phẩm UI (`SAU_UI`), toàn bộ 5 sản phẩm khác đều bị ghi đè cột **Tên SP** thành `"Muc tieu 15 1794903121716"` (hệ quả từ lỗi cập nhật state UI khi Sửa ở `BUG-95`).

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

- **Nguyên nhân gốc (Root cause):** Hệ thống thiếu kiểm tra ràng buộc giá trị dương (`price > 0`) ở cả hai tầng khi cập nhật sản phẩm:
  1. **Frontend:** Tại `frontend-admin/src/App.jsx` dòng 500–507, thẻ `<input type="number" placeholder="Giá tiền" ... />` không khai báo thuộc tính `min` và hàm xử lý submit không kiểm tra điều kiện `Number(productForm.price) > 0` trước khi gọi API `PUT`.
  2. **Backend:** Tại `backend/server.js` dòng 179–189, endpoint `PUT /api/products/:id` nhận trực tiếp `price` từ `req.body` và thực thi câu lệnh `UPDATE products SET ... WHERE id = ?` mà không kiểm tra tính hợp lệ (`price > 0`).
  3. **Tác động phụ trên UI:** Sau khi `PUT` thành công, logic cập nhật state ở `App.jsx:110-114` ghi đè `name` của toàn bộ danh sách sản phẩm trên giao diện thành `productForm.name` (cùng nguyên nhân gốc với `BUG-95`).
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR15-15` thuộc nhóm `C-G4`.
- **Ghi chú duyệt:** Nhóm dữ kiện `C-G4` nối tiếp issue HW02 `BUG-38` (`#184`). Nếu giữ tách riêng file `BUG-98.md` này, bạn có thể xóa bớt phần ghi chú trong ngoặc `(TC-15: -1000; TC-79: 0; TC-16: rỗng)` ở mục **Yêu cầu bị vi phạm** vì trong HW04 nhóm `C-G4` chỉ chứa `TC-FR15-15`.

## Liên quan

- HW02 BUG-38: https://github.com/tkob-team/eshop-sut/issues/184

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
