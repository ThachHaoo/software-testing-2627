# BUG-95

- **ID:** BUG-95
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

`<SV viết>`

## Liên quan

- HW02 BUG-45: https://github.com/tkob-team/eshop-sut/issues/191

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
