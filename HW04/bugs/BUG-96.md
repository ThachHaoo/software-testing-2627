# BUG-96

- **ID:** BUG-96
- **Tiêu đề (GitHub: `[HW04][FR-15] …`):** `[HW04][FR-15] Hệ thống cho phép thêm mới sản phẩm với giá âm (-1000) và lưu vào cơ sở dữ liệu mà không báo lỗi`
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

## Các bước tái hiện

1. Truy cập trang quản trị (`http://localhost:5174`), mở tab **Sản phẩm**.
2. Mở form thêm mới sản phẩm và nhập dữ liệu:
   - **Tên sản phẩm:** `Tai nghe UI10 1794903113968` (chuỗi dạng `Tai nghe UI10 {ts}`)
   - **Giá tiền:** `-1000`
   - **Danh mục:** `category_id = 2`
   - **Mô tả:** `Mô tả NN 1794903113968`
   - **Ảnh (imageUrl):** `https://placehold.co/300`
3. Nhấn nút lưu để gửi form thêm sản phẩm.
4. Quan sát thông báo lỗi, bảng danh sách sản phẩm trên UI và dữ liệu trả về từ `GET /api/products`.

## Expected (trích SRS)

- Hệ thống từ chối lưu sản phẩm vì giá phải là số dương lớn hơn `0` (**FR-15.3**).
- Hiển thị thông báo lỗi hợp lệ (bong bóng HTML5, hộp thoại trình duyệt hoặc thông báo trên trang theo giả định **C7**, **C16**).
- Bảng danh sách sản phẩm trên giao diện (`SAU_UI = TRƯỚC_UI`) và dữ liệu từ `GET /api/products` (`SAU = TRƯỚC`) giữ nguyên như trước khi thao tác, không thêm bản ghi mới.

## Actual

- Hệ thống không hiển thị bất kỳ thông báo lỗi nào (kết quả kiểm tra thông báo lỗi trả về `false`).
- Bảng danh sách sản phẩm trên UI hiển thị thêm 1 dòng mới: `Tai nghe UI10 1794903113968` với giá `-1000` (`-1000 ₫`).
- API `GET /api/products` trả về thêm bản ghi mới (id tiếp theo; ở lượt chính thức là `7`), `name = "Tai nghe UI10 1794903113968"`, `price = -1000`.

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/C_FR15/evidence/TC-FR15-10_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-10_edge.png`, `HW04/C_FR15/evidence/TC-FR15-10_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/C_FR15/evidence/TC-FR15-10_after-save_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-10_after-save_edge.png`, `HW04/C_FR15/evidence/TC-FR15-10_after-save_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR15-10
- Nhóm dữ kiện: C-G2 trong `HW04/bugs/_groups_C.md`; chi tiết `HW04/C_FR15/bug_groups.md` G2

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-36.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-15.3:** (SRS) Giá: bắt buộc, phải là số dương (> 0). — (TC-10: -1000; TC-67: 0; TC-11, 205: giá rỗng được lưu)
  - **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)… — (không có thông báo lỗi)
  - **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail. — (không có thông báo lỗi)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR15-10, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/C_FR15/bug_groups.md` G2):

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
  +     "name": "Tai nghe UI10 1794903113968",
  +     "price": -1000,
  +     "priceRaw": "-1000 ₫",
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
  +     "description": "Mô tả NN 1794903113968",
  +     "id": 7,
  +     "imageUrl": "https://placehold.co/300",
  +     "name": "Tai nghe UI10 1794903113968",
  +     "price": -1000,
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

- **Nguyên nhân gốc (Root cause):** Hệ thống thiếu kiểm tra ràng buộc giá trị dương (`price > 0`) ở cả hai tầng:
  1. **Frontend:** Tại `frontend-admin/src/App.jsx` dòng 500–507, thẻ `<input type="number" placeholder="Giá tiền" ... />` không khai báo thuộc tính `min` (ví dụ `min="1"` hoặc `min="0.01"`) và hàm xử lý submit không kiểm tra điều kiện `Number(productForm.price) > 0`.
  2. **Backend:** Tại `backend/server.js` dòng 167–177, endpoint `POST /api/products` nhận trực tiếp `price` từ `req.body` và chạy câu lệnh `INSERT INTO products ...` mà không kiểm tra `typeof price !== 'number' || price <= 0`.
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR15-10` thuộc nhóm `C-G2`.

## Liên quan

- HW02 BUG-36: https://github.com/tkob-team/eshop-sut/issues/182

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
