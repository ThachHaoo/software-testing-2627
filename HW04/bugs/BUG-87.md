# BUG-87

- **ID:** BUG-87
- **Tiêu đề (GitHub: `[HW04][FR-01] …`):** `[HW04][FR-01] Hệ thống chấp nhận mật khẩu chỉ chứa khoảng trắng thay cho ký tự đặc biệt hợp lệ khi đăng ký tài khoản`
- **Severity:** Medium
- **Priority:** Medium

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

- Hệ thống frontend (`http://localhost:5173`) và backend (`node server.js`) đang hoạt động bình thường.
- Người dùng chưa đăng nhập và đang ở trang Đăng ký (`http://localhost:5173/register`).
- Email dùng để đăng ký chưa tồn tại trong cơ sở dữ liệu (ví dụ: `hiep.sv03@domain.com`).

## Các bước tái hiện

1. Truy cập trang đăng ký tài khoản tại `http://localhost:5173/register`.
2. Nhập **Họ và tên** hợp lệ: `Lê Tấn Hiệp`.
3. Nhập **Email** hợp lệ chưa tồn tại trong hệ thống: `hiep.sv03@domain.com`.
4. Nhập **Mật khẩu** đáp ứng độ dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, chữ số nhưng **không** chứa ký tự đặc biệt thuộc tập `@$!%*?&` mà chỉ dùng khoảng trắng thay thế.
5. Nhấn nút **Đăng Ký**.

## Expected (trích SRS)

- Hệ thống từ chối đăng ký vì mật khẩu thiếu ký tự đặc biệt hợp lệ thuộc tập `@, $, !, %, *, ?, &` (**FR-01.8**; khoảng trắng không được tính là ký tự đặc biệt theo giả định **A5**).
- Hiển thị khung thông báo lỗi trên form (`div.bg-red-100`) nêu rõ lỗi liên quan đến mật khẩu / ký tự đặc biệt và không tạo tài khoản mới trong cơ sở dữ liệu.

## Actual

- Hệ thống không hiển thị bất kỳ hộp thông báo lỗi nào (`locator('div.bg-red-100')` không tìm thấy / không hiển thị trên form).
- Hệ thống chấp nhận mật khẩu và tạo thành công tài khoản mới trong cơ sở dữ liệu (`{ "email": "hiep.sv03@domain.com", "name": "Lê Tấn Hiệp" }`).

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

- **Nguyên nhân gốc (Root cause):** Tại `frontend-web/src/pages/Register.jsx` dòng 15, biểu thức chính quy `flawedStrongPasswordRegex` kiểm tra ký tự đặc biệt bằng lookahead `(?=.*\s)` và tập ký tự `[A-Za-z\d\s]` (coi khoảng trắng `\s` là điều kiện hợp lệ thay vì tập ký tự đặc biệt `@$!%*?&` theo đặc tả FR-01.8 và giả định A5). Vì vậy, mật khẩu chứa chữ hoa, chữ thường, số và khoảng trắng đã vượt qua bước kiểm tra phía client và gửi request tạo tài khoản thành công lên server.
- **Tính tái hiện:** Lỗi xảy ra nhất quán trên cả 3 trình duyệt (Chrome, Edge, Firefox) ở `TC-FR01-202` thuộc nhóm `A-G2`.
- **Ghi chú duyệt:** Severity/Priority đang để `Medium` (lỗ hổng yếu quy tắc validation mật khẩu nhưng không chặn luồng chính của người dùng; bạn có thể đối chiếu lại mức độ trong `HW02/bugs/BUG-02.md` để đồng bộ nếu cần).

## Liên quan

- HW02 BUG-02: https://github.com/tkob-team/eshop-sut/issues/18

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.