# BUG-90

- **ID:** BUG-90
- **Tiêu đề (GitHub: `[HW04][FR-07] …`):** `[HW04][FR-07] Trang giỏ hàng trống thiếu hình minh họa hoặc biểu tượng (img/svg)`
- **Severity:** Low
- **Priority:** Low

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
- Người dùng chưa đăng nhập (khách) và giỏ hàng đang rỗng (`0` sản phẩm).

## Các bước tái hiện

1. Truy cập trang chủ của hệ thống tại `http://localhost:5173/`.
2. Điều hướng đến trang Giỏ hàng (`http://localhost:5173/cart`) khi giỏ hàng chưa có sản phẩm nào.
3. Quan sát nội dung hiển thị ở vùng trạng thái giỏ hàng trống trên trang.

## Expected (trích SRS)

- Khi giỏ hàng trống, trang không hiển thị bảng sản phẩm; có hiển thị cả hình minh họa/icon (`img` hoặc `svg`) lẫn dòng thông báo rõ ràng, thân thiện báo giỏ trống (**FR-07.7**, **FR-24.3**); badge giỏ hàng ẩn hoặc bằng `0`.

## Actual

- Tại khối hiển thị trạng thái giỏ trống, hệ thống chỉ hiển thị dòng chữ `"Giỏ hàng của bạn đang trống"` và liên kết `"Tiếp tục mua sắm"`.
- Hoàn toàn không có hình minh họa hoặc biểu tượng (`img` hoặc `svg`) nào trong khối chứa dòng thông báo giỏ trống (`locator('main').getByText(/trống/i).locator('..').locator('img, svg')` trả về `0`).

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-01_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-01_edge.png`, `HW04/B_FR07/evidence/TC-FR07-01_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR07-01
- Nhóm dữ kiện: B-G2 trong `HW04/bugs/_groups_AB.md`; chi tiết `HW04/B_FR07/bug_groups.md` G2

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-21.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-07.7:** Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng. — vi phạm ở: thiếu hình minh hoạ; có thông báo 'Giỏ hàng của bạn đang trống'
  - **FR-24.3:** Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện (bổ sung FR-07.7). — vi phạm ở: thiếu icon/hình minh hoạ

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR07-01, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G2):

  ```
  Error: giỏ trống: có img/svg minh hoạ trong khối chứa dòng chữ giỏ trống
  
  expect(locator).not.toHaveCount(expected) failed
  
  Locator:  locator('main').getByText(/trống/i).locator('..').locator('img, svg').visible()
  Expected: not 0
  Received: 0
  Timeout:  5000ms
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 20–27

  ```jsx
    20    if (cart.length === 0) {
    21      return (
    22        <div className="text-center mt-10">
    23          <h2 className="text-2xl mb-4">Giỏ hàng của bạn đang trống</h2>
    24          <Link to="/" className="text-blue-600 hover:underline">Tiếp tục mua sắm</Link>
    25        </div>
    26      );
    27    }
  ```

### Nhận định

- **Nguyên nhân gốc (Root cause):** Tại `frontend-web/src/pages/Cart.jsx` dòng 20–27, nhánh điều kiện `if (cart.length === 0)` chỉ render thẻ tiêu đề `<h2>Giỏ hàng của bạn đang trống</h2>` và thẻ `<Link to="/">Tiếp tục mua sắm</Link>`, thiếu phần tử hình ảnh (`<img>`) hoặc biểu tượng vector (`<svg>`) minh họa trạng thái trống (Empty State) theo đặc tả FR-07.7 và FR-24.3.
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR07-01` thuộc nhóm `B-G2`.
- **Ghi chú duyệt:** Severity/Priority đang để `Low` (lỗi giao diện/UI không ảnh hưởng đến chức năng cốt lõi; bạn có thể đối chiếu lại mức độ trong `HW02/bugs/BUG-21.md` để đồng bộ nếu cần).

## Liên quan

- HW02 BUG-21: https://github.com/tkob-team/eshop-sut/issues/167

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
