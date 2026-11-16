# A_FR01 – nhóm TC Fail (dữ kiện, SV viết bug)

Nhóm = cùng tập assertion lỗi và cùng giá trị nhận được (triệu chứng giống hệt; số dài `{ts}` chuẩn hoá).
Không đặt tên bug, không severity/priority, không kết luận nguyên nhân, không đề xuất gộp/tách.
Ảnh = screenshot Playwright chụp lúc test KẾT THÚC (screenshot: 'only-on-failure'), không phải lúc assertion đầu tiên lỗi.

## G1 – 6 TC × 3 trình duyệt (18 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: URL sau khi bấm Đăng Ký | expect(page).toHaveURL(expected) failed | Received string:  "http://localhost:5173/register"`
- `Error: không có thông báo lỗi | expect(locator).toHaveCount(expected) failed | Received: 1`
- `Error: đúng 1 user mới | expect(received).toEqual(expected) // deep equality | + Array []`

### TC-FR01-01 – Kiểm tra đăng ký thành công qua UI khi Họ Tên không dấu, email mới và mật khẩu mạnh

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / EP
- HW02: Fail · BUG-01 · issue #17 (https://github.com/tkob-team/eshop-sut/issues/17)
- Expected (HW02, nguyên văn): Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'dom01_{ts}@domain.com' như cột dữ liệu.
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-01.md mục Yêu cầu): FR-01.10: Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập; Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định)
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`; Register.jsx:17-19 (không khớp → setError 'Mật khẩu quá yếu!…', return trước POST)
- Ảnh: `evidence/TC-FR01-01_chrome.png`, `evidence/TC-FR01-01_edge.png`, `evidence/TC-FR01-01_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: URL sau khi bấm Đăng Ký

expect(page).toHaveURL(expected) failed

Expected pattern: /\/login$/
Received string:  "http://localhost:5173/register"
Timeout: 5000ms

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
-     "email": "dom01_1794852077820@domain.com",
-     "name": "Nguyen Van A",
-   },
- ]
+ Array []
```

### TC-FR01-02 – Kiểm tra đăng ký thành công qua UI khi Họ Tên có dấu và mật khẩu có thêm ký tự đặc biệt ngoài tập

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / EP
- HW02: Fail · BUG-01 · issue #17 (https://github.com/tkob-team/eshop-sut/issues/17)
- Expected (HW02, nguyên văn): Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyễn Văn Ánh' và email 'dom02_{ts}@domain.com' như cột dữ liệu.
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-01.md mục Yêu cầu): FR-01.10: Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập; Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định)
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`; Register.jsx:17-19 (không khớp → setError 'Mật khẩu quá yếu!…', return trước POST)
- Ảnh: `evidence/TC-FR01-02_chrome.png`, `evidence/TC-FR01-02_edge.png`, `evidence/TC-FR01-02_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: URL sau khi bấm Đăng Ký

expect(page).toHaveURL(expected) failed

Expected pattern: /\/login$/
Received string:  "http://localhost:5173/register"
Timeout: 5000ms

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
-     "email": "dom02_1794852093315@domain.com",
-     "name": "Nguyễn Văn Ánh",
-   },
- ]
+ Array []
```

### TC-FR01-64 – Kiểm tra chấp nhận đăng ký qua UI khi Mật khẩu dài 8 ký tự (LB)

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Boundary / BVA LB
- HW02: Fail · BUG-01 · issue #17 (https://github.com/tkob-team/eshop-sut/issues/17)
- Expected (HW02, nguyên văn): Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'bva64_{ts}@domain.com' như cột dữ liệu.
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-01.md mục Yêu cầu): FR-01.10: Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập; Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định)
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`; Register.jsx:17-19 (không khớp → setError 'Mật khẩu quá yếu!…', return trước POST)
- Ảnh: `evidence/TC-FR01-64_chrome.png`, `evidence/TC-FR01-64_edge.png`, `evidence/TC-FR01-64_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: URL sau khi bấm Đăng Ký

expect(page).toHaveURL(expected) failed

Expected pattern: /\/login$/
Received string:  "http://localhost:5173/register"
Timeout: 5000ms

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
-     "email": "bva64_1794852130386@domain.com",
-     "name": "Nguyen Van A",
-   },
- ]
+ Array []
```

### TC-FR01-68 – Kiểm tra chấp nhận đăng ký qua UI khi Mật khẩu có đúng 1 chữ hoa (LB)

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Boundary / BVA LB
- HW02: Fail · BUG-01 · issue #17 (https://github.com/tkob-team/eshop-sut/issues/17)
- Expected (HW02, nguyên văn): Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'bva68_{ts}@domain.com' như cột dữ liệu.
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-01.md mục Yêu cầu): FR-01.10: Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập; Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định)
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`; Register.jsx:17-19 (không khớp → setError 'Mật khẩu quá yếu!…', return trước POST)
- Ảnh: `evidence/TC-FR01-68_chrome.png`, `evidence/TC-FR01-68_edge.png`, `evidence/TC-FR01-68_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: URL sau khi bấm Đăng Ký

expect(page).toHaveURL(expected) failed

Expected pattern: /\/login$/
Received string:  "http://localhost:5173/register"
Timeout: 5000ms

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
-     "email": "bva68_1794852146032@domain.com",
-     "name": "Nguyen Van A",
-   },
- ]
+ Array []
```

### TC-FR01-74 – Kiểm tra chấp nhận đăng ký qua UI khi Mật khẩu có đúng 1 chữ số (LB)

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Boundary / BVA LB
- HW02: Fail · BUG-01 · issue #17 (https://github.com/tkob-team/eshop-sut/issues/17)
- Expected (HW02, nguyên văn): Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'bva74_{ts}@domain.com' như cột dữ liệu.
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-01.md mục Yêu cầu): FR-01.10: Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập; Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định)
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`; Register.jsx:17-19 (không khớp → setError 'Mật khẩu quá yếu!…', return trước POST)
- Ảnh: `evidence/TC-FR01-74_chrome.png`, `evidence/TC-FR01-74_edge.png`, `evidence/TC-FR01-74_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: URL sau khi bấm Đăng Ký

expect(page).toHaveURL(expected) failed

Expected pattern: /\/login$/
Received string:  "http://localhost:5173/register"
Timeout: 5000ms

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
-     "email": "bva74_1794852161372@domain.com",
-     "name": "Nguyen Van A",
-   },
- ]
+ Array []
```

### TC-FR01-77 – Kiểm tra chấp nhận đăng ký qua UI khi Mật khẩu có đúng 1 ký tự đặc biệt (LB)

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Boundary / BVA LB
- HW02: Fail · BUG-01 · issue #17 (https://github.com/tkob-team/eshop-sut/issues/17)
- Expected (HW02, nguyên văn): Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'bva77_{ts}@domain.com' như cột dữ liệu.
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-01.md mục Yêu cầu): FR-01.10: Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập; Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định)
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`; Register.jsx:17-19 (không khớp → setError 'Mật khẩu quá yếu!…', return trước POST)
- Ảnh: `evidence/TC-FR01-77_chrome.png`, `evidence/TC-FR01-77_edge.png`, `evidence/TC-FR01-77_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: URL sau khi bấm Đăng Ký

expect(page).toHaveURL(expected) failed

Expected pattern: /\/login$/
Received string:  "http://localhost:5173/register"
Timeout: 5000ms

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
-     "email": "bva77_1794852177282@domain.com",
-     "name": "Nguyen Van A",
-   },
- ]
+ Array []
```

## G2 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: hộp lỗi có nội dung | expect(locator).toHaveText(expected) failed`
- `Error: hộp lỗi đỏ trên form | expect(locator).toBeVisible() failed`
- `Error: không có user mới | expect(received).toEqual(expected) // deep equality | + Array [ | +   Object { | +     "email": "hiep.sv03@domain.com", | +     "name": "Lê Tấn Hiệp", | +   }, | + ]`
- `Error: thông báo nói về ký tự đặc biệt | expect(locator).toContainText(expected) failed`
- `Error: thông báo nói về mật khẩu | expect(locator).toContainText(expected) failed`

### TC-FR01-202 – Kiểm tra từ chối đăng ký qua UI khi mật khẩu chỉ có khoảng trắng làm ký tự đặc biệt

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative (AI suy ra, SV duyệt) / EG
- HW02: Fail · BUG-02 · issue #18 (https://github.com/tkob-team/eshop-sut/issues/18)
- Expected (HW02, nguyên văn): Hệ thống báo mật khẩu thiếu ký tự đặc biệt; không tạo tài khoản
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-02.md mục Yêu cầu): FR-01.8: Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &; A5 (giả định HW02): tập ký tự đặc biệt là tập đóng – khoảng trắng không tính là ký tự đặc biệt
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`
- Ảnh: `evidence/TC-FR01-202_chrome.png`, `evidence/TC-FR01-202_edge.png`, `evidence/TC-FR01-202_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

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

## G3 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: có token trong localStorage | expect(received).not.toBeNull() | Received: null`
- `Error: không có lỗi đăng nhập | expect(locator).toHaveCount(expected) failed | Received: 1`
- `Error: không có thông báo lỗi | expect(locator).toHaveCount(expected) failed | Received: 1`
- `Error: đúng 1 user mới | expect(received).toEqual(expected) // deep equality | + Array []`
- `Error: đăng nhập xong về trang chủ | expect(page).toHaveURL(expected) failed | Received: "http://localhost:5173/login"`

### TC-FR01-211 – Kiểm tra đăng ký và đăng nhập lại qua UI khi mật khẩu có khoảng trắng ở đầu

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive (AI suy ra, SV duyệt) / EG
- HW02: Fail · BUG-01 · issue #17 (https://github.com/tkob-team/eshop-sut/issues/17)
- Expected (HW02, nguyên văn): Đăng ký thành công; đăng nhập lại bằng đúng chuỗi ␣Hiep123$ thành công
- Yêu cầu bị vi phạm (theo HW02/bugs/BUG-01.md mục Yêu cầu): FR-01.10: Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập; Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định)
- Vị trí code SUT: ../eshop-sut/frontend-web/src/pages/Register.jsx:15 `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`; Register.jsx:17-19 (không khớp → setError 'Mật khẩu quá yếu!…', return trước POST)
- Ảnh: `evidence/TC-FR01-211_chrome.png`, `evidence/TC-FR01-211_edge.png`, `evidence/TC-FR01-211_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

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

