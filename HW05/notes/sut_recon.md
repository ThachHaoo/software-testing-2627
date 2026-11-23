# HW05 – Khảo sát SUT và môi trường (23/11/2026)

Phạm vi: chuẩn bị cho workflow C (login → GET /api/products → POST /api/checkout → GET /api/orders/my-orders).
Chỉ ghi dữ kiện đọc được từ mã/máy; chưa chạy tải, chưa khởi động backend. Đường dẫn `server.js`, `database.js` tính từ `../eshop-sut/backend/`.

## 1. Repo SUT

- `../eshop-sut` đọc được (add-dir còn hiệu lực).
- `git pull` (origin = tkob-team/eshop-sut): **trước `de0f48f`, sau `de0f48f`** ("Already up to date"). `upstream/main` = `85af3ba` (không đổi).
- Working tree SUT đang bẩn (không đụng tới):
  - `M backend/database.sqlite`: file CSDL bị ghi mỗi lần chạy backend.
  - `M frontend-mobile/App.js`: 1 dòng, còn lại từ HW03.
  - Chưa track: `actual_results.md`, `reset_db.ps1`, `run_sv_cases.ps1` (từ các bài trước).
- Nhánh `usability-tunnel` (HW03) vẫn còn, không dùng cho HW05.

## 2. Chạy backend

- Lệnh: `cd ../eshop-sut/backend; node server.js` (setup_guide.md:23-33). Bước `node database.js` trong hướng dẫn là thừa vì `server.js:4` đã `require("./database")`.
- Cổng cố định `3000` (`server.js:8`, `server.js:570`), không đọc biến môi trường. **Base URL: `http://localhost:3000`**, tiền tố `/api`.
- Middleware chỉ có `cors()` (mở mọi origin) và `bodyParser.json()` (`server.js:11-12`). **Không có rate limit, helmet hay giới hạn kết nối**; grep `rateLimit|helmet` trong backend không thấy gì.
- Express 5.2.1, sqlite3 (node) 6.0.1, Node v24.15.0 trên máy.
- Lúc khảo sát backend không chạy: không tiến trình nào nghe ở 3000/5173/5174.

## 3. CSDL

- **SQLite**, một file `backend/database.sqlite` (`database.js:4-5`). Mở **một kết nối** `new sqlite3.Database` dùng chung cho mọi request (`database.js:5`).
- **Không phải WAL.** Mã không có `PRAGMA` nào; header file (byte 18-19 = `1 1`) cho thấy chế độ rollback journal mặc định.
- **Không có index** ngoài khoá chính: không có `CREATE INDEX`, `users.email` không UNIQUE (`database.js:52-63`), `orders.user_id` không index (`database.js:76-83`).
  - Hệ quả cần nhớ khi thiết kế tải: `my-orders` lọc theo `user_id` phải quét toàn bảng `orders`, còn login quét `users` theo email. Bảng càng lớn thì càng chậm.
- **Mỗi lần khởi động, CSDL bị DROP rồi seed lại**: `initDatabase()` được gọi ngay khi `require` (`database.js:14-21`, `database.js:115`).
  - Cách reset DB về seed: dừng backend rồi chạy lại `node server.js`. Script có sẵn: `../eshop-sut/reset_db.ps1 -BackendDir <...>\backend`, file chưa track trong SUT.
  - Restart thì **mất mọi user đăng ký thêm, đơn hàng và giỏ hàng** (giỏ nằm trong RAM, `server.js:14`).

## 4. Bốn endpoint của workflow C

| # | Method + path | Auth | Request | Response 200 | Mã nguồn |
|---|---|---|---|---|---|
| 1 | `POST /api/login` | không | `{"email": "...", "password": "..."}` | `{"message":"Login successful","token":"<JWT>","user":{...}}` | `server.js:32-66` |
| 2 | `GET /api/products` | không | (tuỳ chọn `?search=`) | mảng sản phẩm `[{id,name,price,description,imageUrl,category_id}, ...]`, seed 5 dòng, không phân trang | `server.js:141-157` |
| 3 | `POST /api/checkout` | Bearer | `{"total_amount": <số>, "shipping_address": "..."}` | `{"message":"Checkout successful","orderId":<id>}` | `server.js:297-309` |
| 4 | `GET /api/orders/my-orders` | Bearer | — | mảng đơn của user `[{id,user_id,total_amount,status,shipping_address,created_at}, ...]` (`ORDER BY id DESC`, không phân trang) | `server.js:311-319` |

- Auth = header `Authorization: Bearer <token>` (`server.js:100-110`). Thiếu token trả 401 `{"error":"Unauthorized"}`; token sai trả 403 `{"error":"Forbidden"}`.
- JWT ký với payload `{id, role}`, **không có `expiresIn`** (`server.js:51`): token không hết hạn, có thể login một lần mỗi VU rồi dùng lại.
- Login lỗi: email không tồn tại hoặc sai mật khẩu → 401 `{"error":"Invalid email or password"}` (`server.js:37-38`, `server.js:63`); đang bị khoá → 403 (`server.js:40-44`).
- Response login trả **nguyên bản ghi `user`** (`server.js:52`), gồm cả cột `password`. Ghi nhận để đối chiếu SRS, chưa kết luận; nằm ngoài phạm vi HW05.

### Checkout: items trong body hay bắt buộc cart?

- **Không bắt buộc cart và không đọc `items`.** Backend chỉ lấy `total_amount` và `shipping_address` từ body rồi `INSERT INTO orders` (`server.js:299-303`).
  - Không đọc `userCarts`, không xoá giỏ sau checkout, không kiểm tra rỗng.
  - Không tự tính tổng tiền. SRS FR-08 (README.md:102-108) yêu cầu backend tự tính và xoá giỏ, nên đây là một chỗ lệch SRS, chưa kết luận.
- Web gửi `{items: cart, total_amount, coupon_id}` (`frontend-web/src/pages/Checkout.jsx:45-48`). Backend bỏ qua `items` và `coupon_id`; `shipping_address` không được gửi nên lưu NULL.
- ⇒ **Workflow C khả thi không cần bước `POST /api/cart`.** Có thể gửi body giống web (`items` + `total_amount`) cho sát hành vi thật; backend vẫn chỉ ghi một dòng `orders`.
- Mỗi lần checkout thêm 1 dòng vào `orders`, nên `my-orders` trả mảng dài dần theo số vòng lặp của từng user. Cần tính tới khi đặt assertion và đọc kết quả.

## 5. Lockout

- Lưu trong CSDL, bảng `users`, cột `login_attempts` và `locked_until` (`database.js:52-63`).
- Mỗi lần sai mật khẩu, bộ đếm **tăng 2** (`server.js:54`). Đạt `>= 3` thì bị khoá **180000 ms = 3 phút** (`server.js:56-57`). ⇒ **Lần sai thứ 2 đã khoá.**
  - SRS FR-02 (README.md:40-42) ghi: tăng đúng 1 và khoá 30 giây sau 3 lần sai. Lệch SRS, chưa kết luận.
- Khi đang khoá, **mật khẩu đúng cũng nhận 403**, vì kiểm khoá chạy trước kiểm mật khẩu (`server.js:40`).
- Login đúng khi không bị khoá thì đặt lại `login_attempts = 0` và `locked_until = NULL` (`server.js:47-50`).
- Cách reset:
  - (a) chờ hết 3 phút rồi login đúng;
  - (b) restart backend: reseed toàn bộ, mất cả user đã đăng ký thêm;
  - không có API admin để mở khoá.
- Email không tồn tại không tăng bộ đếm (`server.js:37-38`).
- Hệ quả cho tải: CSV có dòng sai mật khẩu, hoặc nhiều VU dùng chung một tài khoản mà gửi sai, thì tài khoản bị khoá 3 phút và các VU sau nhận 403 hàng loạt.

## 6. Tồn kho

- **Không có tồn kho.** Bảng `products` không có cột stock hay quantity (`database.js:66-73`), không có bảng order_items, checkout không đụng tới `products` (`server.js:297-309`). Vì vậy checkout không bao giờ thất bại vì hết hàng, cũng không có tranh chấp trừ kho.
- Seed 5 sản phẩm, id 1-5, giá từ 4.000.000 đến 45.000.000 (`database.js:95-101`), 3 danh mục, 4 coupon.
- Reset: như mục 3 (restart backend).

## 7. Tài khoản và tạo user cho CSV

- Seed 2 tài khoản: 1 admin, 1 user (`database.js:88-91`). Mật khẩu lưu dạng plain text; không in ở đây, xem CLAUDE.md gốc mục 1.
- Tạo thêm: `POST /api/register` với body `{"name","email","password"}`. Endpoint này:
  - không cần auth, không validate, không chặn email trùng (`server.js:20-30`);
  - trả `{"message":"User registered successfully","id":<id>}`.
- Nếu email trùng, login lấy dòng đầu tiên (`db.get`, `server.js:35`). CSV nên dùng email duy nhất.
- **User đăng ký mất sau mỗi lần restart backend**, nên mỗi lần reset phải đăng ký lại danh sách CSV: script riêng, hoặc setUp Thread Group trong JMeter.
- Không thấy rate limit hay middleware nào chặn tải (mục 2). Vì vậy giới hạn thực tế là một tiến trình Node đơn luồng và một kết nối SQLite.

## 8. Môi trường máy

- Hostname: `LAPTOP-NFIGFMR1`.
- OS: Windows 11 Home Single Language 10.0.26200, 64-bit.
- CPU: 13th Gen Intel Core i5-13500H, 12 nhân / 16 luồng. RAM 15,6 GB.
- Java: OpenJDK 25.0.3 LTS (Temurin-25.0.3+9).
  - Đường dẫn: `C:\Program Files\Eclipse Adoptium\jdk-25.0.3.9-hotspot\bin\java.exe`. `JAVA_HOME` đã đặt đúng thư mục này.
- JMeter: **Apache JMeter 5.6.3**, đã có sẵn tại `D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3\` (bin\jmeter.bat).
  - Không có trong PATH; `JMETER_HOME` chưa đặt.
  - `java -jar bin\ApacheJMeter.jar --version` chạy được với Java 25. Có cảnh báo log4j "package scanning … deprecated", không chặn.
  - `lib\ext` chỉ có plugin lõi, **chưa có JMeter Plugins Manager**.
  - Không cài thêm gì.
- Node v24.15.0. SUT, JMeter và trình duyệt cùng chạy trên một máy, nên máy sinh tải tranh tài nguyên với SUT. Cần ghi vào phần giới hạn của test plan.
