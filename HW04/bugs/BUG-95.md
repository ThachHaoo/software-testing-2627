# BUG-95

- **ID:** BUG-95
- **Tiêu đề (GitHub: `[HW04][FR-15] …`):** `[HW04][FR-15] Bảng sản phẩm hiển thị sai tên tất cả sản phẩm thành tên mới vừa sửa và không cập nhật giá mới trên UI sau khi sửa sản phẩm`
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
- Danh sách sản phẩm ban đầu gồm 5 sản phẩm có sẵn (`iPhone 15 Pro Max`, `Samsung Galaxy S24 Ultra`, `MacBook Pro M3`, `Tai nghe AirPods Pro 2`, `Bàn phím cơ Keychron Q1`) cùng sản phẩm mục tiêu `M` vừa được tạo (có giá ban đầu là `1000000`).

## Các bước tái hiện

1. Truy cập trang quản trị (`http://localhost:5174`), mở tab **Sản phẩm**.
2. Chọn thao tác **Sửa** trên dòng sản phẩm mục tiêu `M` (có giá ban đầu `1000000`).
3. Nhập dữ liệu mới hợp lệ vào form:
   - **Tên sản phẩm:** `Sửa UI03 1794903107473` (chuỗi dạng `Sửa UI03 {ts}`)
   - **Giá tiền:** `2500000`
   - **Danh mục:** chọn danh mục có `category_id = 3`
4. Nhấn nút lưu form cập nhật sản phẩm và xác nhận hộp thoại `"Cập nhật thành công!"`.
5. Quan sát bảng danh sách sản phẩm hiển thị trên giao diện.

## Expected (trích SRS)

- Khi sửa một sản phẩm, chỉ sản phẩm mục tiêu `M` bị thay đổi; tất cả các sản phẩm khác trên bảng giữ nguyên dữ liệu như trước khi sửa (**FR-15.5**).
- Bảng danh sách sản phẩm hiển thị chính xác thông tin đã cập nhật của `M` (**FR-15.1**): **Tên SP** = `Sửa UI03 {ts}`, **Giá** = `2500000`, số dòng không đổi.
- Trong dữ liệu backend: bản ghi `M` được cập nhật `name = 'Sửa UI03 {ts}'`, `price = 2500000`, `category_id = 3`.

## Actual

- Trên bảng danh sách sản phẩm UI: tất cả 5 sản phẩm khác (`iPhone 15 Pro Max`, `Samsung Galaxy S24 Ultra`, `MacBook Pro M3`, `Tai nghe AirPods Pro 2`, `Bàn phím cơ Keychron Q1`) đều bị đổi cột **Tên SP** thành tên mới của sản phẩm mục tiêu (`Sửa UI03 1794903107473`).
- Tại dòng của sản phẩm mục tiêu `M` trên bảng UI: cột **Giá** vẫn hiển thị giá cũ là `1000000` thay vì giá mới `2500000` (mặc dù API backend đã lưu dữ liệu mới).

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/C_FR15/evidence/TC-FR15-03_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-03_edge.png`, `HW04/C_FR15/evidence/TC-FR15-03_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/C_FR15/evidence/TC-FR15-03_after-save_chrome.png`, `HW04/C_FR15/evidence/TC-FR15-03_after-save_edge.png`, `HW04/C_FR15/evidence/TC-FR15-03_after-save_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR15-03
- Nhóm dữ kiện: C-G1 trong `HW04/bugs/_groups_C.md`; chi tiết `HW04/C_FR15/bug_groups.md` G1

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-45.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-15.5:** (SRS) Khi Sửa một sản phẩm, chỉ sản phẩm đó bị thay đổi — các sản phẩm khác giữ nguyên. — (trên bảng UI: các sản phẩm khác hiển thị bị đổi tên)
  - **FR-15.1:** (SRS) Admin có thể Thêm / Xem / Sửa / Xóa sản phẩm. — Xem (bảng không hiển thị giá mới của M; EC63)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR15-03, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/C_FR15/bug_groups.md` G1):

  ```
  Error: dòng của M: 'Giá' (so giá trị số)
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 2500000
  Received: 1000000
  
  Error: mọi dòng khác SAU_UI = TRƯỚC_UI
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 5
  + Received  + 5
  
    Array [
      Object {
  -     "name": "iPhone 15 Pro Max",
  +     "name": "Sửa UI03 1794903107473",
        "price": 30000000,
        "priceRaw": "30000000 ₫",
      },
      Object {
  -     "name": "Samsung Galaxy S24 Ultra",
  +     "name": "Sửa UI03 1794903107473",
        "price": 28000000,
        "priceRaw": "28000000 ₫",
      },
      Object {
  -     "name": "MacBook Pro M3",
  +     "name": "Sửa UI03 1794903107473",
        "price": 45000000,
        "priceRaw": "45000000 ₫",
      },
      Object {
  -     "name": "Tai nghe AirPods Pro 2",
  +     "name": "Sửa UI03 1794903107473",
        "price": 6000000,
        "priceRaw": "6000000 ₫",
      },
      Object {
  -     "name": "Bàn phím cơ Keychron Q1",
  +     "name": "Sửa UI03 1794903107473",
        "price": 4000000,
        "priceRaw": "4000000 ₫",
      },
    ]
  ```

- Đoạn code trích nguyên văn: `frontend-admin/src/App.jsx` dòng 105–116

  ```jsx
   105    const handleProductSubmit = async (e) => {
   106      e.preventDefault();
   107      try {
   108        if (productForm.id) {
   109          await axios.put(`${API_URL}/products/${productForm.id}`, productForm);
   110          const fakeMassUpdatedProducts = products.map((p) => ({
   111            ...p,
   112            name: productForm.name,
   113          }));
   114          setProducts(fakeMassUpdatedProducts);
   115          alert("Cập nhật thành công!");
   116        } else {
  ```

### Nhận định

- **Nguyên nhân gốc (Root cause):** Tại `frontend-admin/src/App.jsx` dòng 109–114, sau khi gọi API `await axios.put(\`${API_URL}/products/${productForm.id}\`, productForm)` thành công, hàm `handleProductSubmit` không cập nhật state `products` theo đúng sản phẩm có `id === productForm.id` hoặc gọi lại API lấy danh sách mới, mà lại chạy vòng lặp `products.map((p) => ({ ...p, name: productForm.name }))`. Đoạn mã này vừa ghi đè thuộc tính `name` của toàn bộ sản phẩm trong state UI thành `productForm.name`, vừa bỏ sót việc cập nhật các trường khác như `price` và `category_id` của sản phẩm đang sửa trên state giao diện.
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR15-03` thuộc nhóm `C-G1`.

## Liên quan

- HW02 BUG-45: https://github.com/tkob-team/eshop-sut/issues/191

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
