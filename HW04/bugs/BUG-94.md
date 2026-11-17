# BUG-94

- **ID:** BUG-94
- **Tiêu đề (GitHub: `[HW04][FR-07] …`):** `[HW04][FR-07] Nút 'Thêm vào giỏ hàng' ở trang chi tiết sản phẩm không thêm và không cộng dồn số lượng khi thao tác thêm nhiều lần có điều hướng kiểm tra giỏ hàng`
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
- Người dùng đang mở trang chi tiết của sản phẩm `Bàn phím cơ Keychron Q1` (id `5`).

## Các bước tái hiện

1. Truy cập trang chi tiết sản phẩm `Bàn phím cơ Keychron Q1` (id `5`).
2. Nhập **Số lượng** bằng `2` và nhấn nút **Thêm vào giỏ hàng** (lần 1). Quan sát phản hồi trong ≤ 2 giây và mở trang Giỏ hàng (`http://localhost:5173/cart`) để kiểm tra.
3. Quay lại trang chi tiết sản phẩm `Bàn phím cơ Keychron Q1` (id `5`), đổi **Số lượng** thành `5` và nhấn nút **Thêm vào giỏ hàng** (lần 2).
4. Mở trang Giỏ hàng (`http://localhost:5173/cart`) để kiểm tra số dòng và số lượng sản phẩm.

## Expected (trích SRS)

- **Sau lần bấm 1:** Hiển thị phản hồi trực quan trong vòng ≤ 2 giây (**FR-06.3**, **FR-24.1**, **B21**); tại trang Giỏ hàng có 1 dòng sản phẩm `Bàn phím cơ Keychron Q1` (id `5`) với **Số lượng** bằng `2`.
- **Sau lần bấm 2:** Tại trang Giỏ hàng vẫn giữ 1 dòng sản phẩm `Bàn phím cơ Keychron Q1` (id `5`) và **Số lượng** được cộng dồn từ `2` lên `7` (**FR-07.3**).

## Actual

- **Sau lần bấm 1:** Không có phản hồi trực quan trong vòng ≤ 2 giây (kết quả kiểm tra trả về `null`); tại trang Giỏ hàng không có dòng sản phẩm `Bàn phím cơ Keychron Q1` (`0` dòng, mảng số lượng trả về `[]`).
- **Sau lần bấm 2:** Tại trang Giỏ hàng vẫn không có dòng sản phẩm `Bàn phím cơ Keychron Q1` (`0` dòng, mảng số lượng trả về `[]`).

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-205_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-205_edge.png`, `HW04/B_FR07/evidence/TC-FR07-205_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/B_FR07/evidence/TC-FR07-205_after-action-1_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-205_after-action-2_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-205_after-action-1_edge.png`, `HW04/B_FR07/evidence/TC-FR07-205_after-action-2_edge.png`, `HW04/B_FR07/evidence/TC-FR07-205_after-action-1_firefox.png`, `HW04/B_FR07/evidence/TC-FR07-205_after-action-2_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR07-205
- Nhóm dữ kiện: B-G6 trong `HW04/bugs/_groups_AB.md`; chi tiết `HW04/B_FR07/bug_groups.md` G6

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-15.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **Chức năng thêm của nút 'Thêm vào giỏ hàng' (ngầm định):** ngầm định trong FR-06, không có câu SRS riêng
  - **FR-06.3:** (B6 SV chốt) Nút Thêm vào giỏ hàng — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).
  - **FR-24.1:** (GUI, B16) Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
  - **B21 (giả định SV chốt):** (phản hồi trực quan khi thêm) (SV chốt 2026-10-20): hiểu theo nghĩa rộng — lý do: FR-06.3/FR-24.1 ghi '(toast notification hoặc badge cập nhật)' như ví dụ minh hoạ, không phải danh sách đóng. Oracle: trong ≤ 2 giây sau khi bấm, có ít nhất một thay đổi nhìn thấy được gắn với lần thêm (toast; badge đổi; chữ/trạng thái nút thêm đổi; thông báo trên trang); ghi rõ loại phản hồi quan sát được vào Actual.
  - **B1 (giả định SV chốt):** (cận trên Số lượng) (SV chốt 2026-10-20): KHÔNG có cận trên. Lý do: SRS chỉ quy định ≥ 1 (FR-06). BVA phía trên dùng 1 đại diện 'giá trị lớn' hợp lệ thay cho UB/UB±1. — vi phạm ở: TC-64: 1000 không được thêm

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR07-205, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G6):

  ```
  Error: B21: có phản hồi ≤ 2 s sau khi bấm thêm
  
  expect(received).not.toBeNull()
  
  Received: null
  
  Error: lần 1: có dòng id 5
  
  expect(locator).toHaveCount(expected) failed
  
  Locator:  locator('main table tbody tr').filter({ has: locator('td').filter({ hasText: 'Bàn phím cơ Keychron Q1' }) })
  Expected: 1
  Received: 0
  Timeout:  5000ms
  
  Error: lần 1: Số lượng id 5
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 3
  + Received  + 1
  
  - Array [
  -   "2",
  - ]
  + Array []
  
  Error: lần 2: có dòng id 5
  
  expect(locator).toHaveCount(expected) failed
  
  Locator:  locator('main table tbody tr').filter({ has: locator('td').filter({ hasText: 'Bàn phím cơ Keychron Q1' }) })
  Expected: 1
  Received: 0
  Timeout:  5000ms
  
  Error: lần 2: Số lượng id 5
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 3
  + Received  + 1
  
  - Array [
  -   "7",
  - ]
  + Array []
  
  Error: lần 2: số dòng
  
  expect(locator).toHaveCount(expected) failed
  
  Locator:  locator('main table tbody tr')
  Expected: 1
  Received: 0
  Timeout:  5000ms
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

- **Nguyên nhân gốc (Root cause):** Tại `frontend-web/src/pages/ProductDetail.jsx` dòng 21–25, biến trạng thái cục bộ `clickCount` của component `ProductDetail` được khởi tạo bằng `0` mỗi khi trang chi tiết sản phẩm mount, và hàm `handleAddToCart` kiểm tra `if (clickCount === 0)` thì chỉ gán `setClickCount(1)` rồi `return` sớm. Trong kịch bản của `TC-FR07-205`, sau lần bấm 1 tại trang chi tiết, test case điều hướng sang `/cart` để kiểm tra giỏ hàng (làm `ProductDetail` unmount) rồi quay lại trang chi tiết ở lần 2 (làm `ProductDetail` mount lại với `clickCount = 0`). Do đó, cả hai lần bấm đều rơi vào lần bấm đầu tiên của instance component, khiến `addToCart` và `setAdded(true)` không bao giờ được gọi.
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR07-205` thuộc nhóm `B-G6`.
- **Ghi chú duyệt:**
  - Nhóm dữ kiện `B-G6` có cùng nguyên nhân gốc với `B-G1` (`BUG-89`) và `B-G3` (`BUG-91`) tại `ProductDetail.jsx:21-31` (issue HW02 `#161`). Nếu bạn áp dụng quy tắc gộp theo nguyên nhân gốc ở bước tổng hợp, có thể gộp `BUG-94` vào `BUG-89`.
  - Nếu giữ tách riêng file `BUG-94.md` này, bạn có thể xóa bớt dòng bullet cuối về `B1` (`TC-64: 1000 không được thêm`) trong mục **Yêu cầu bị vi phạm** vì mục đó chỉ áp dụng cho `TC-FR07-64`.

## Liên quan

- HW02 BUG-15: https://github.com/tkob-team/eshop-sut/issues/161

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
