# BUG-87

- **ID:** BUG-87
- **Tiêu đề (GitHub: `[HW04][FR-01] …`):** `<SV viết>`
- **Severity:** `<SV viết>` (Critical/High/Medium/Low)
- **Priority:** `<SV viết>` (High/Medium/Low)

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động); http://localhost:5173/register (frontend-web)
- Trình duyệt: Chrome 157.0.8103.79 (channel chrome), Edge 157.0.4341.60 (channel msedge), Firefox 159.0 (Playwright build firefox-1572)
- Công cụ: Playwright 1.65.1 (`@playwright/test`), workers 1, retries 0; spec `HW04/tests/A_FR01.spec.ts` @ `9f26855`
- Report chính thức (2026-11-17, Asia/Saigon):
  - chrome: `HW04/reports/chrome_20261117T134709/`
  - edge: `HW04/reports/edge_20261117T134950/`
  - firefox: `HW04/reports/firefox_20261117T135230/`
- Nhật ký lượt chạy: `HW04/A_FR01/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh lúc kết thúc: `HW04/A_FR01/evidence/TC-FR01-202_chrome.png`, `HW04/A_FR01/evidence/TC-FR01-202_edge.png`, `HW04/A_FR01/evidence/TC-FR01-202_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/A_FR01/evidence/TC-FR01-202_after-submit_chrome.png`, `HW04/A_FR01/evidence/TC-FR01-202_after-submit_edge.png`, `HW04/A_FR01/evidence/TC-FR01-202_after-submit_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR01-202
- Nhóm dữ kiện: A-G2 trong `HW04/bugs/_groups_AB.md`; chi tiết `HW04/A_FR01/bug_groups.md` G2

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-02.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-01.8:** Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &.
  - **A5** (giả định, SRS im lặng): A5 (Mật khẩu – ký tự đặc biệt): hiểu danh sách (@, $, !, %, *, ?, &) là tập ĐÓNG: mật khẩu chỉ chứa ký tự đặc biệt ngoài tập này (ví dụ #, ^, -, khoảng trắng) bị coi là thiếu ký tự đặc biệt → bị từ chối. SRS không nói ký tự ngoài tập có được phép xuất hiện thêm hay không → giả định được phép nếu đã có ít nhất một ký tự trong tập.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR01-202, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/A_FR01/bug_groups.md` G2):

  ```
  Error: hộp lỗi đỏ trên form
  
  expect(locator).toBeVisible() failed
  
  Locator: locator('div.bg-red-100')
  Expected: visible
  Timeout: 5000ms
  Error: element(s) not found
  
  Error: hộp lỗi có nội dung
  
  expect(locator).toHaveText(expected) failed
  
  Locator: locator('div.bg-red-100')
  Expected pattern: /\S/
  Timeout: 5000ms
  Error: element(s) not found
  
  Error: thông báo nói về mật khẩu
  
  expect(locator).toContainText(expected) failed
  
  Locator: locator('div.bg-red-100')
  Expected pattern: /mật khẩu/i
  Timeout: 5000ms
  Error: element(s) not found
  
  Error: thông báo nói về ký tự đặc biệt
  
  expect(locator).toContainText(expected) failed
  
  Locator: locator('div.bg-red-100')
  Expected pattern: /ký tự đặc biệt/i
  Timeout: 5000ms
  Error: element(s) not found
  
  Error: không có user mới
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 1
  + Received  + 6
  
  - Array []
  + Array [
  +   Object {
  +     "email": "hiep.sv03@domain.com",
  +     "name": "Lê Tấn Hiệp",
  +   },
  + ]
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/pages/Register.jsx` dòng 15

  ```jsx
    15      const flawedStrongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/;
  ```

### Nhận định

`<SV viết>`

## Liên quan

- HW02 BUG-02: https://github.com/tkob-team/eshop-sut/issues/18

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
