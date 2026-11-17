# BUG-88

- **ID:** BUG-88
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

- Ảnh lúc kết thúc: `HW04/A_FR01/evidence/TC-FR01-211_chrome.png`, `HW04/A_FR01/evidence/TC-FR01-211_edge.png`, `HW04/A_FR01/evidence/TC-FR01-211_firefox.png`
- Ảnh ngay sau thao tác chính: `HW04/A_FR01/evidence/TC-FR01-211_after-submit_chrome.png`, `HW04/A_FR01/evidence/TC-FR01-211_after-submit_edge.png`, `HW04/A_FR01/evidence/TC-FR01-211_after-submit_firefox.png`

## TC liên quan

- Fail (1 TC × 3 trình duyệt): TC-FR01-211
- Nhóm dữ kiện: A-G3 trong `HW04/bugs/_groups_AB.md`; chi tiết `HW04/A_FR01/bug_groups.md` G3

## Yêu cầu bị vi phạm

- Theo `HW02/bugs/BUG-01.md` mục Yêu cầu (SV duyệt lại cho HW04):
  - **FR-01.10:** Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.
  - **Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8** (ngầm định — Actual chỉ có thông báo gộp, không xác định được luật riêng nào bị cài sai)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Assertion lỗi nguyên văn (TC-FR01-211, chrome; edge, firefox cùng tập assertion lỗi và giá trị nhận được — nhóm theo signature ở `HW04/A_FR01/bug_groups.md` G3):

  ```
  Error: không có thông báo lỗi
  
  expect(locator).toHaveCount(expected) failed
  
  Locator:  locator('div.bg-red-100')
  Expected: 0
  Received: 1
  Timeout:  5000ms
  
  Error: đúng 1 user mới
  
  expect(received).toEqual(expected) // deep equality
  
  - Expected  - 6
  + Received  + 1
  
  - Array [
  -   Object {
  -     "email": "hiep.sv12@domain.com",
  -     "name": "Lê Tấn Hiệp",
  -   },
  - ]
  + Array []
  
  Error: đăng nhập xong về trang chủ
  
  expect(page).toHaveURL(expected) failed
  
  Expected: "http://localhost:5173/"
  Received: "http://localhost:5173/login"
  Timeout:  5000ms
  
  Error: không có lỗi đăng nhập
  
  expect(locator).toHaveCount(expected) failed
  
  Locator:  locator('div.bg-red-100')
  Expected: 0
  Received: 1
  Timeout:  5000ms
  
  Error: có token trong localStorage
  
  expect(received).not.toBeNull()
  
  Received: null
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/pages/Register.jsx` dòng 15–19

  ```jsx
    15      const flawedStrongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/;
    16  
    17      if (!flawedStrongPasswordRegex.test(password)) {
    18        setError('Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.');
    19        return;
  ```

### Nhận định

`<SV viết>`

## Liên quan

- HW02 BUG-01: https://github.com/tkob-team/eshop-sut/issues/17

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
