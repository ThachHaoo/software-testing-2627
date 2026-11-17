# BUG-92

- **ID:** BUG-92
- **Tiêu đề (GitHub: `[HW04][FR-07] …`):** `[HW04][FR-07] Link 'Giỏ hàng' thiếu badge hiển thị tổng số lượng sản phẩm và không cộng dồn số lượng ở lần bấm đầu tiên khi thêm lại sản phẩm từ trang chi tiết`
- **Severity:** Medium
- **Priority:** Medium

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
- Giỏ hàng ban đầu đã có 2 dòng sản phẩm được thêm từ trang chủ: `iPhone 15 Pro Max` (đơn giá `30000000`, số lượng `1`, thành tiền `30000000`) và `Tai nghe AirPods Pro 2` (đơn giá `6000000`, số lượng `1`, thành tiền `6000000`).

## Các bước tái hiện

1. Truy cập trang chi tiết của sản phẩm `Tai nghe AirPods Pro 2`.
2. Nhập **Số lượng** bằng `2`.
3. Nhấn nút **Thêm vào giỏ hàng** 1 lần đầu tiên.
4. Quan sát khu vực liên kết **Giỏ hàng** trên thanh điều hướng và mở trang Giỏ hàng (`http://localhost:5173/cart`) để kiểm tra các dòng sản phẩm, thành tiền và tổng tiền.

## Expected (trích SRS)

- Link **Giỏ hàng** trên thanh điều hướng hiển thị badge tổng số lượng sản phẩm trong giỏ là `4` (**FR-23.2**, giả định **B9**).
- Tại trang Giỏ hàng: vẫn giữ nguyên 2 dòng sản phẩm; dòng `Tai nghe AirPods Pro 2` được cộng dồn số lượng từ `1` lên `3`, thành tiền cập nhật thành `18000000` (**FR-07.3**); dòng `iPhone 15 Pro Max` giữ nguyên; **Tổng** tiền cập nhật thành `48000000`.

## Actual

- Link **Giỏ hàng** trên thanh điều hướng không hiển thị badge số lượng sản phẩm (kết quả kiểm tra badge trả về `null`).
- Tại trang Giỏ hàng: dòng `Tai nghe AirPods Pro 2` không được cộng dồn, vẫn giữ nguyên Số lượng là `1` và Thành tiền là `6000000`; **Tổng** tiền vẫn là `36000000`.

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-04_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-04_edge.png`, `HW04/B_FR07/evidence/TC-FR07-04_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/B_FR07/evidence/TC-FR07-04_after-action_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-04_after-action_edge.png`, `HW04/B_FR07/evidence/TC-FR07-04_after-action_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR07-04
- Nhóm dữ kiện: B-G4 trong `HW04/bugs/_groups_AB.md`; chi tiết `HW04/B_FR07/bug_groups.md` G4

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-20.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-23.2:** (GUI, B16) Link "Giỏ hàng" phải hiển thị badge số lượng sản phẩm trong giỏ.
- Theo `HW02/bugs/BUG-15.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **Chức năng thêm của nút 'Thêm vào giỏ hàng' (ngầm định):** ngầm định trong FR-06, không có câu SRS riêng
  - **FR-06.3:** (B6 SV chốt) Nút Thêm vào giỏ hàng — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).
  - **FR-24.1:** (GUI, B16) Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
  - **B21 (giả định SV chốt):** (phản hồi trực quan khi thêm) (SV chốt 2026-10-20): hiểu theo nghĩa rộng — lý do: FR-06.3/FR-24.1 ghi '(toast notification hoặc badge cập nhật)' như ví dụ minh hoạ, không phải danh sách đóng. Oracle: trong ≤ 2 giây sau khi bấm, có ít nhất một thay đổi nhìn thấy được gắn với lần thêm (toast; badge đổi; chữ/trạng thái nút thêm đổi; thông báo trên trang); ghi rõ loại phản hồi quan sát được vào Actual.
  - **B1 (giả định SV chốt):** (cận trên Số lượng) (SV chốt 2026-10-20): KHÔNG có cận trên. Lý do: SRS chỉ quy định ≥ 1 (FR-06). BVA phía trên dùng 1 đại diện 'giá trị lớn' hợp lệ thay cho UB/UB±1. — vi phạm ở: TC-64: 1000 không được thêm

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR07-04, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G4):

  ```
  Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 2
  + Received  + 2
  
  @@ -6,9 +6,9 @@
        "subtotal": 30000000,
      },
      Object {
        "name": "Tai nghe AirPods Pro 2",
        "price": 6000000,
  -     "qty": "3",
  -     "subtotal": 18000000,
  +     "qty": "1",
  +     "subtotal": 6000000,
      },
    ]
  
  Error: Tổng SAU
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 48000000
  Received: 36000000
  
  Error: badge SAU (tổng Số lượng, B9)
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 4
  Received: null
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/App.jsx` dòng 23

  ```jsx
    23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
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

- **Nguyên nhân gốc (Root cause):** Nhóm fail `B-G4` (`TC-FR07-04`) đồng thời bộc lộ 2 lỗi từ 2 vị trí mã nguồn khác nhau:
  1. **Thiếu badge số lượng trên link Giỏ hàng:** Tại `frontend-web/src/App.jsx` dòng 23, thẻ `<Link to="/cart" className="hover:underline">Giỏ hàng</Link>` chỉ render văn bản tĩnh mà không đọc dữ liệu từ `CartContext` để hiển thị badge tổng số lượng sản phẩm theo đặc tả FR-23.2.
  2. **Bỏ qua lần bấm thêm đầu tiên ở trang chi tiết:** Tại `frontend-web/src/pages/ProductDetail.jsx` dòng 21–25, hàm `handleAddToCart` kiểm tra `if (clickCount === 0)` thì chỉ tăng `setClickCount(1)` và `return` sớm, khiến lần bấm đầu tiên không gọi `addToCart` nên không cộng dồn số lượng của `Tai nghe AirPods Pro 2` (giống nguyên nhân gốc của `BUG-89` / HW02 `#161`).
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR07-04` thuộc nhóm `B-G4`.
- **Ghi chú duyệt:**
  - Nếu bạn giữ tách riêng `BUG-92` cho lỗi thiếu badge trên thanh điều hướng (`App.jsx:23`, nối tiếp HW02 `BUG-20` `#166`) và quy phần không cộng dồn số lượng ở trang chi tiết về nguyên nhân đã nêu ở `BUG-89` (`ProductDetail.jsx:21-25`), bạn có thể rút gọn tiêu đề của `BUG-92` tập trung vào lỗi thiếu badge Giỏ hàng và xóa bớt các bullet thừa của `BUG-15` (`Chức năng thêm...`, `FR-06.3`, `FR-24.1`, `B21`, `B1`) trong mục **Yêu cầu bị vi phạm**.
  - Severity/Priority đang để `Medium` theo lỗi hiển thị badge bị thiếu (bạn có thể đối chiếu lại mức độ trong `HW02/bugs/BUG-20.md` để đồng bộ nếu cần).

## Liên quan

- HW02 BUG-20: https://github.com/tkob-team/eshop-sut/issues/166
- HW02 BUG-15: https://github.com/tkob-team/eshop-sut/issues/161

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
