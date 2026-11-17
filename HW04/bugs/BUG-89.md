# BUG-89

- **ID:** BUG-89
- **Tiêu đề (GitHub: `[HW04][FR-07] …`):** `[HW04][FR-07] Nút 'Thêm vào giỏ hàng' ở trang chi tiết sản phẩm không hoạt động ở lần bấm đầu tiên`
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động); http://localhost:5173 → trang chi tiết / giỏ hàng (frontend-web)
- Trình duyệt: Chrome 157.0.8103.79 (channel chrome), Edge 157.0.4341.60 (channel msedge), Firefox 159.0 (Playwright build firefox-1572)
- Công cụ: Playwright 1.65.1 (`@playwright/test`), workers 1, retries 0; spec `HW04/tests/B_FR07.spec.ts` @ `c8a2ce9`
- Report chính thức (2026-11-17, Asia/Saigon):
  - chrome: `HW04/reports/chrome_20261117T141103/`
  - edge: `HW04/reports/edge_20261117T141230/`
  - firefox: `HW04/reports/firefox_20261117T141359/`
- Nhật ký lượt chạy: `HW04/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend (`http://localhost:5173`) và backend (`node server.js`) đang hoạt động bình thường.
- Giỏ hàng ban đầu đang rỗng (`0` sản phẩm).
- Người dùng đang mở trang chi tiết của một sản phẩm bất kỳ (ví dụ: `Bàn phím cơ Keychron Q1`, đơn giá `4000000`).

## Các bước tái hiện

1. Truy cập trang chi tiết sản phẩm `Bàn phím cơ Keychron Q1`.
2. Nhập **Số lượng** bằng `1` (mức biên dưới hợp lệ).
3. Nhấn nút **Thêm vào giỏ hàng** 1 lần đầu tiên.
4. Bấm link **Giỏ hàng** trên thanh điều hướng để kiểm tra trạng thái giỏ.

## Expected (trích SRS)

- Ngay sau lần bấm đầu tiên nút **Thêm vào giỏ hàng**, sản phẩm được thêm vào giỏ hàng với đúng số lượng đã nhập (`1`).
- Hiển thị phản hồi trực quan trong vòng ≤ 2 giây (**FR-06.3**, **FR-24.1**, **B21**).
- Tại trang Giỏ hàng: hiển thị 1 dòng sản phẩm `Bàn phím cơ Keychron Q1` với Số lượng `1`, Thành tiền `4000000` và **Tổng** tiền bằng `4000000`.

## Actual

- Sau lần bấm đầu tiên nút **Thêm vào giỏ hàng**, hệ thống không thêm sản phẩm vào giỏ hàng và không có bất kỳ phản hồi trực quan nào.
- Khi mở trang Giỏ hàng: giỏ hàng vẫn rỗng (`0` dòng, danh sách dòng trả về `[]`), không hiển thị **Tổng** tiền (`null`).

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-61_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-61_edge.png`, `HW04/B_FR07/evidence/TC-FR07-61_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/B_FR07/evidence/TC-FR07-61_after-action_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-61_after-action_edge.png`, `HW04/B_FR07/evidence/TC-FR07-61_after-action_firefox.png`
- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-62_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-62_edge.png`, `HW04/B_FR07/evidence/TC-FR07-62_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/B_FR07/evidence/TC-FR07-62_after-action_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-62_after-action_edge.png`, `HW04/B_FR07/evidence/TC-FR07-62_after-action_firefox.png`
- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-63_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-63_edge.png`, `HW04/B_FR07/evidence/TC-FR07-63_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/B_FR07/evidence/TC-FR07-63_after-action_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-63_after-action_edge.png`, `HW04/B_FR07/evidence/TC-FR07-63_after-action_firefox.png`
- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-64_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-64_edge.png`, `HW04/B_FR07/evidence/TC-FR07-64_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/B_FR07/evidence/TC-FR07-64_after-action_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-64_after-action_edge.png`, `HW04/B_FR07/evidence/TC-FR07-64_after-action_firefox.png`

## TC liên quan

- Fail (4 TC × 3 trình duyệt): TC-FR07-61, TC-FR07-62, TC-FR07-63, TC-FR07-64
- Nhóm dữ kiện: B-G1 trong `HW04/bugs/_groups_AB.md`; chi tiết `HW04/B_FR07/bug_groups.md` G1

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-15.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **Chức năng thêm của nút 'Thêm vào giỏ hàng' (ngầm định):** ngầm định trong FR-06, không có câu SRS riêng
  - **FR-06.3:** (B6 SV chốt) Nút Thêm vào giỏ hàng — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).
  - **FR-24.1:** (GUI, B16) Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
  - **B21 (giả định SV chốt):** (phản hồi trực quan khi thêm) (SV chốt 2026-10-20): hiểu theo nghĩa rộng — lý do: FR-06.3/FR-24.1 ghi '(toast notification hoặc badge cập nhật)' như ví dụ minh hoạ, không phải danh sách đóng. Oracle: trong ≤ 2 giây sau khi bấm, có ít nhất một thay đổi nhìn thấy được gắn với lần thêm (toast; badge đổi; chữ/trạng thái nút thêm đổi; thông báo trên trang); ghi rõ loại phản hồi quan sát được vào Actual.
  - **B1 (giả định SV chốt):** (cận trên Số lượng) (SV chốt 2026-10-20): KHÔNG có cận trên. Lý do: SRS chỉ quy định ≥ 1 (FR-06). BVA phía trên dùng 1 đại diện 'giá trị lớn' hợp lệ thay cho UB/UB±1. — vi phạm ở: TC-64: 1000 không được thêm

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR07-61, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G1):

  ```
  Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 8
  + Received  + 1
  
  - Array [
  -   Object {
  -     "name": "Bàn phím cơ Keychron Q1",
  -     "price": 4000000,
  -     "qty": "1",
  -     "subtotal": 4000000,
  -   },
  - ]
  + Array []
  
  Error: số dòng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 1
  Received: 0
  
  Error: Tổng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 4000000
  Received: null
  ```

- Assertion lỗi nguyên văn (TC-FR07-62, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G1):

  ```
  Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 8
  + Received  + 1
  
  - Array [
  -   Object {
  -     "name": "Bàn phím cơ Keychron Q1",
  -     "price": 4000000,
  -     "qty": "2",
  -     "subtotal": 8000000,
  -   },
  - ]
  + Array []
  
  Error: số dòng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 1
  Received: 0
  
  Error: Tổng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 8000000
  Received: null
  ```

- Assertion lỗi nguyên văn (TC-FR07-63, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G1):

  ```
  Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 8
  + Received  + 1
  
  - Array [
  -   Object {
  -     "name": "Bàn phím cơ Keychron Q1",
  -     "price": 4000000,
  -     "qty": "5",
  -     "subtotal": 20000000,
  -   },
  - ]
  + Array []
  
  Error: số dòng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 1
  Received: 0
  
  Error: Tổng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 20000000
  Received: null
  ```

- Assertion lỗi nguyên văn (TC-FR07-64, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G1):

  ```
  Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 8
  + Received  + 1
  
  - Array [
  -   Object {
  -     "name": "Bàn phím cơ Keychron Q1",
  -     "price": 4000000,
  -     "qty": "1000",
  -     "subtotal": 4000000000,
  -   },
  - ]
  + Array []
  
  Error: số dòng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 1
  Received: 0
  
  Error: Tổng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 4000000000
  Received: null
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/pages/ProductDetail.jsx` dòng 21–31

  ```jsx
    21    const handleAddToCart = () => {
    22      if (clickCount === 0) {
    23        setClickCount(1);
    24        return; // Không làm gì cả ở lần đầu tiên
    25      }
    26  
    27      addToCart(product, parseInt(quantity));
    28      setAdded(true);
    29      setClickCount(0); // Reset lại
    30      setTimeout(() => setAdded(false), 2000);
    31    };
  ```

### Nhận định

- **Nguyên nhân gốc (Root cause):** Tại `frontend-web/src/pages/ProductDetail.jsx` dòng 21–25, hàm `handleAddToCart` cố tình kiểm tra điều kiện `if (clickCount === 0)` thì chỉ tăng `setClickCount(1)` và `return` sớm mà không gọi `addToCart(product, parseInt(quantity))` hay cập nhật trạng thái phản hồi `setAdded(true)`. Do đó, lần bấm đầu tiên của người dùng ở trang chi tiết sản phẩm luôn bị bỏ qua bất kể giá trị số lượng hợp lệ nào.
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) qua 4 test case thuộc nhóm `B-G1` (`TC-FR07-61`, `TC-FR07-62`, `TC-FR07-63`, `TC-FR07-64`).

## Liên quan

- HW02 BUG-15: https://github.com/tkob-team/eshop-sut/issues/161

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/301

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
