# BUG-94

- **ID:** BUG-94
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

`<SV viết>`

## Liên quan

- HW02 BUG-15: https://github.com/tkob-team/eshop-sut/issues/161

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
