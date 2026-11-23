# 01 – Thiết kế workflow C (bản AI, bước 1 skill `jmeter-perf-testing`)

> Bản AI sinh (Claude Code, 23/11/2026), đóng băng ở `appendix/ai-outputs/step1/`. SV duyệt và sửa ở bước 5; mỗi thay đổi ghi vào `review_log` trong `perf_plan.json`.
> Nguồn: `notes/sut_recon.md`, `HW05/CLAUDE.md` (W = C, D1, D2), mã `../eshop-sut` @ `de0f48f`, SRS `README.md`.
> Chưa có tham số tải (số thread, ramp-up, thời lượng, ngưỡng): để bước 2.

## 1. Luồng của một virtual user (mỗi vòng lặp)

| # | Label | Request | Auth | Nhóm endpoint (đề §5) | Trích | Assertion | Nguồn mã |
|---|---|---|---|---|---|---|---|
| 1 | `01_POST_login` | `POST /api/login` `{email, password}` từ `users.csv` | – | **Auth-heavy** | `token` ← `$.token` | 200; có `$.token` | `server.js:32-66` |
| 2 | `02_GET_products` | `GET /api/products` | – | **Read-heavy** | – | 200; có `$[0].id` | `server.js:141-157` |
| 3 | `03_POST_checkout` | `POST /api/checkout` `{items:[…], total_amount, coupon_id:null}` từ `orders.csv` | Bearer | **Transactional** (tạo đơn, ghi CSDL) | `orderId` ← `$.orderId` | 200; `$.message` = `Checkout successful`; có `$.orderId` | `server.js:297-309`, `frontend-web/src/pages/Checkout.jsx:45-48` |
| 4 | `04_GET_my_orders` | `GET /api/orders/my-orders` | Bearer | **Read-heavy theo user**, đồng thời kiểm kết quả giao dịch | – | 200; body chứa `"id":<orderId>,` | `server.js:311-319` |

Think time (timer chạy trước mỗi request) là giá trị tạm: uniform 1–3 s; checkout 2–5 s; my-orders 1–2 s. Bước 2 chốt lại.

## 2. Vì sao workflow phủ đủ 3 nhóm endpoint

- **Auth-heavy:**
  - Login chạy ở **mỗi** vòng lặp (giả định A1), không chỉ một lần mỗi VU.
  - Mỗi lần login có một truy vấn `SELECT * FROM users WHERE email = ?` (không có index trên email, `database.js:52-63`), một `UPDATE users` (reset bộ đếm, `server.js:47-50`) và một lần ký JWT (`server.js:51`).
  - Nhờ vậy nhóm auth chịu tải tỉ lệ với số vòng lặp.
- **Read-heavy:**
  - `GET /api/products` đọc toàn bảng `products`, không phân trang, công khai (`server.js:153-155`).
  - `GET /api/orders/my-orders` đọc `orders` lọc theo `user_id` (không có index, `database.js:76-83`). Bảng `orders` lớn dần theo số checkout, nên đây là truy vấn đọc có chi phí tăng dần trong lượt.
- **Transactional:**
  - `POST /api/checkout` ghi một dòng `orders` (`server.js:301-303`) qua kết nối SQLite duy nhất (`database.js:5`).
  - Đề lấy ví dụ "add-to-cart and checkout / order creation". Backend checkout không đọc giỏ (`server.js:297-309`, `sut_recon.md` §4), nên bỏ bước `POST /api/cart` mà vẫn giữ đúng thao tác tạo đơn.
  - Bước 4 xác nhận đơn vừa tạo xuất hiện trong lịch sử, tức giao dịch thực sự được ghi.

## 3. Dữ liệu CSV (data-driven)

| File | Cột | Dòng | Phạm vi | Dùng ở |
|---|---|---|---|---|
| `data/users.csv` | email, password, name | 200 (tạm, ≥ VU đỉnh – bước 2 chốt) | Thread Group chính, share all, recycle | setUp đăng ký + login |
| `data/lockout_users.csv` | email, password, name | 20 | Chỉ luồng lockout, recycle = false, dừng thread khi hết | setUp đăng ký + luồng cố ý sai |
| `data/orders.csv` | product_id, product_name, unit_price, quantity, total_amount | 8 | Thread Group chính, share all, recycle | body checkout |

- Sản phẩm và giá lấy từ seed (`database.js:95-101`), với `total_amount = unit_price × quantity`.
- Email ở hai tập user tách biệt (`perf*` / `lock*`). `check_plan.py` kiểm hai tập không chung user.
- Mật khẩu thoả quy tắc mật khẩu mạnh của SRS FR-01 (giả định A5).

## 4. setUp và reset (D1)

- Hai **setUp Thread Group**, mỗi nhóm 1 thread, số vòng = số dòng CSV.
- Lần lượt đăng ký mọi user trong `users.csv` và `lockout_users.csv` bằng `POST /api/register` (`server.js:20-30`). Assertion: 200, `$.message` = `User registered successfully`.
- Lý do: mỗi lần restart backend, CSDL bị DROP rồi seed lại (`database.js:14-21`, `115`), nên user đăng ký trước đó mất. `run_scenario.ps1` restart backend trước mỗi lượt, và setUp đăng ký lại.
- Sample của setUp nằm chung jtl với nhãn `00_setup_*`. Khi phân tích có thể lọc bằng `jtl_stats.py --exclude-label "^00_setup"`; khi đối chiếu với `statistics.json` thì không lọc.

## 5. Luồng lockout tách riêng (D2)

- Một Thread Group "Lockout – user riêng, cố ý sai": 1 thread, 20 vòng, mỗi vòng dùng **một** user mới từ `lockout_users.csv`. Vì vậy không phải chờ hết thời gian khoá, và không đụng user của luồng chính.
- Mỗi vòng:

| # | Label | Body | Kỳ vọng (SRS FR-02, `README.md:40-42`) | Assertion |
|---|---|---|---|---|
| L1 | `L1_POST_login_sai_1` | mật khẩu sai | Từ chối, chưa khoá | 401; không có `"token"` |
| L2 | `L2_POST_login_sai_2` | mật khẩu sai | Từ chối, chưa khoá | 401; không có `"token"` |
| L3 | `L3_POST_login_sai_3` | mật khẩu sai | Lần sai thứ 3 → bị khoá | không có `"token"` |
| L4 | `L4_POST_login_dung_khi_khoa` | mật khẩu đúng | Đang khoá → từ chối, có thông báo lỗi phù hợp | không có `"token"`; body chứa `khóa` |

- Chuỗi `khóa` lấy từ thông báo trong mã (`server.js:43`). SRS chỉ ghi "thông báo lỗi phù hợp", nên đây là giả định A4.
- Luồng chính chỉ dùng credential đúng. Vì vậy stress hoặc spike không tự gây khoá tài khoản ở luồng chính, trừ khi có lỗi dữ liệu.

## 6. Quan sát mã ↔ SRS liên quan (ghi nhận, chưa kết luận)

- Backend lưu `total_amount` do client gửi, không tự tính lại (`server.js:299-303`), lệch FR-08. Issue đã có: #281.
- Login trả cả bản ghi user (`server.js:52`). Issue #279.
- Khoá tài khoản trong mã khác SRS về bước tăng bộ đếm và thời gian khoá (`server.js:54-57`). Issue #280, #275.

## 7. Giả định AI tự đặt

Danh sách đầy đủ ở `perf_plan.json` → `assumptions` (A1–A9). Tóm tắt:

- **A1:** login chạy mỗi vòng.
- **A2:** body checkout giống web, không gửi `shipping_address`.
- **A3:** assertion my-orders dạng chứa chuỗi.
- **A4:** kỳ vọng của luồng lockout và chuỗi `khóa`.
- **A5:** mật khẩu và mẫu email của user test.
- **A6, A7:** số user và think time là giá trị tạm.
- **A8:** chưa có Duration Assertion.
- **A9:** SRS không có yêu cầu hiệu năng.
