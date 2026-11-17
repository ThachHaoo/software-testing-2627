# BUG-99

- **ID:** BUG-99
- **Tiêu đề (GitHub: `[HW04][FR-15] …`):** `[HW04][FR-15] Hệ thống không báo lỗi từ chối khi nhập chuỗi mã script XSS (<script>alert(1)</script>) vào ô 'Tên sản phẩm' ở form Thêm`
- **Severity:** Medium
- **Priority:** Medium

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
   - **Tên sản phẩm:** `<script>alert(1)</script>`
   - Các trường bắt buộc khác (giá tiền, danh mục) nhập giá trị hợp lệ.
3. Nhấn nút lưu để gửi form thêm sản phẩm.
4. Quan sát thông báo lỗi hiển thị trên giao diện/trình duyệt và kiểm tra việc thực thi script.

## Expected (trích SRS)

- Hệ thống báo lỗi từ chối dữ liệu đầu vào chứa thẻ script (`<script>alert(1)</script>`) theo giả định **C21** (và các quy tắc thông báo lỗi **C7**, **C16**); tuyệt đối không kích hoạt thực thi mã độc XSS (**SEC-04**).

## Actual

- Hệ thống không kích hoạt hộp thoại `alert(1)` (assertion kiểm tra XSS đạt do cơ chế tự động escape của React), nhưng hoàn toàn không hiển thị bất kỳ thông báo lỗi từ chối nào (bong bóng HTML5, hộp thoại trình duyệt hay thông báo trên trang đều trả về `false`).

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/C_FR15/evidence/TC-FR15-200_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-200_edge.png`, `HW04/C_FR15/evidence/TC-FR15-200_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/C_FR15/evidence/TC-FR15-200_after-save_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-200_after-save_edge.png`, `HW04/C_FR15/evidence/TC-FR15-200_after-save_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR15-200
- Nhóm dữ kiện: C-G5 trong `HW04/bugs/_groups_C.md`; chi tiết `HW04/C_FR15/bug_groups.md` G5

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-39.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **C21 (giả định SV chốt):** (tên sản phẩm chứa mã script — TC-FR15-200) (SV chưa ghi nội dung riêng; Expected nằm ở TC-FR15-200). — (SV chốt)
  - **C7 (giả định SV chốt):** (oracle khi UI từ chối) dữ liệu không đổi (GET trước/sau) + có thông báo lỗi (bong bóng HTML5 hoặc hộp thoại đều tính); vị trí kiểm riêng ở TC-91 theo FR-22.4; nội dung chữ chỉ ghi làm Actual (sửa theo C16, SV chốt 2026-10-20). Câu cũ (đã thay)… — (không có thông báo lỗi)
  - **C16 (giả định SV chốt):** (thông báo lỗi dạng hộp thoại trình duyệt) hộp thoại trình duyệt (alert) có nội dung báo lỗi được tính là thông báo lỗi cho C7. Riêng TC-FR15-91 (FR-22.4): thông báo chỉ ở dạng hộp thoại thì không nằm phía trên nút → Fail. — (không có thông báo lỗi)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR15-200, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/C_FR15/bug_groups.md` G5):

  ```
  Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: true
  Received: false
  ```

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

- **Nguyên nhân gốc (Root cause):** Cả tầng giao diện lẫn máy chủ đều không có bước kiểm tra lọc hoặc từ chối ký tự/thẻ HTML/script nguy hiểm trong tên sản phẩm:
  1. **Frontend:** Tại `frontend-admin/src/App.jsx` dòng 491–499, ô nhập liệu `<input placeholder="Tên sản phẩm" ... required />` chỉ kiểm tra không để trống (`required`) mà không có thuộc tính `pattern` hay hàm kiểm tra ký tự hợp lệ trước khi gửi form.
  2. **Backend:** Tại `backend/server.js` dòng 167–177, endpoint `POST /api/products` nhận trực tiếp chuỗi `name` thô từ `req.body` và lưu thẳng vào cơ sở dữ liệu mà không sanitize hay từ chối thẻ `<script>`.
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR15-200` thuộc nhóm `C-G5`.
- **Ghi chú duyệt:** Severity/Priority đang để `Medium` vì React tự động escape chuỗi khi render nên mã script không thực thi được trên trình duyệt (assertion XSS đạt), chỉ vi phạm yêu cầu báo lỗi từ chối dữ liệu chứa mã script; bạn có thể đối chiếu lại mức độ trong `HW02/bugs/BUG-39.md` để đồng bộ nếu cần.

## Liên quan

- HW02 BUG-39: https://github.com/tkob-team/eshop-sut/issues/185

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
