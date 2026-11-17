# BUG-93

- **ID:** BUG-93
- **Tiêu đề (GitHub: `[HW04][FR-07] …`):** `<SV viết>`
- **Severity:** `<SV viết>` (Critical/High/Medium/Low)
- **Priority:** `<SV viết>` (High/Medium/Low)

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

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/B_FR07/evidence/TC-FR07-08_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-08_edge.png`, `HW04/B_FR07/evidence/TC-FR07-08_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/B_FR07/evidence/TC-FR07-08_after-action_chrome.png`, `HW04/B_FR07/evidence/TC-FR07-08_after-action_edge.png`, `HW04/B_FR07/evidence/TC-FR07-08_after-action_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR07-08
- Nhóm dữ kiện: B-G5 trong `HW04/bugs/_groups_AB.md`; chi tiết `HW04/B_FR07/bug_groups.md` G5

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-19.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-07.4:** Nút Xóa sản phẩm phải có dialog xác nhận trước khi thực hiện.
  - **FR-24.2:** Khi xóa item khỏi giỏ phải có dialog xác nhận (trùng FR-07.4).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR07-08, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/B_FR07/bug_groups.md` G5):

  ```
  Error: hiện dialog xác nhận sau khi bấm xoá
  
  hiện dialog xác nhận sau khi bấm xoá
  
  expect(received).toBe(expected) // Object.is equality
  
  Expected: 1
  Received: 0
  
  Call Log:
  - Timeout 2000ms exceeded while waiting on the predicate
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 49–55

  ```jsx
    49                <td>
    50                  <button
    51                    onClick={() => removeFromCart(index)}
    52                    className="text-red-500 hover:text-red-700"
    53                  >
    54                    Xóa
    55                  </button>
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/context/CartContext.jsx` dòng 12–16

  ```jsx
    12    const removeFromCart = (index) => {
    13      const newCart = [...cart];
    14      newCart.splice(index, 1);
    15      setCart(newCart);
    16    };
  ```

### Nhận định

`<SV viết>`

## Liên quan

- HW02 BUG-19: https://github.com/tkob-team/eshop-sut/issues/165

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
