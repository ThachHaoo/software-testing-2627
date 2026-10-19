# Dữ kiện Fail — FR-01 (A_FR01)

> Dữ kiện do AI gom, chưa phải bug report; SV quyết định gộp/tách.
> Nhãn nhóm chỉ mô tả triệu chứng quan sát được (tầng + mẫu actual + yêu cầu lệch). Không có tên bug, severity, priority hay nguyên nhân.
> Nguồn: `HW02/A_FR01/testcases.json` sau commit 6/7c. Đoạn code chỉ trích nguyên văn để SV đối chiếu, không bình luận.

**Trước khi tái hiện:** khởi động lại backend (`node server.js`) để CSDL seed sạch; chạy xong cũng khởi động lại để xoá dữ liệu thử.

## Tổng hợp

| Nhóm | Số Fail | Số Blocked ghi case gốc | Yêu cầu |
|---|---|---|---|
| G1 | 14 | 22 | FR-01.1, FR-01.2, FR-01.3, FR-01.4, FR-01.5, FR-01.6, FR-01.7a, FR-01.7b, FR-01.7c, FR-01.8, FR-01.9, FR-01.10 |
| G2 | 5 | 0 | FR-01.1 |
| G3 | 15 | 0 | FR-01.2, FR-01.3 |
| G4 | 3 | 0 | FR-01.4 |
| G5 | 18 | 0 | FR-01.5, FR-01.6, FR-01.7a, FR-01.7b, FR-01.7c, FR-01.8 |
| G6 | 1 | 0 | FR-01.1, FR-01.2, FR-01.5 |
| G7 | 1 | 0 | FR-01.1, FR-01.2, FR-01.3, FR-01.4, FR-01.5, FR-01.6, FR-01.7a, FR-01.7b, FR-01.7c, FR-01.8 |
| G8 | 1 | 0 | FR-01.4 |
| G9 | 1 | 0 | FR-01.6 |
| G10 | 1 | 0 | API-REG |
| G11 | 1 | 0 | FR-01.8 |
| G12 | 1 | 0 | FR-01.1, SEC-04 |
| G13 | 1 | 0 | FR-22.1 |
| G14 | 1 | 0 | FR-22.2 |
| G15 | 1 | 3 | FR-01.9 |

Blocked không ghi case gốc: không còn (200, 203, 204, 208 đã ghi case gốc TC-FR01-01 ở commit 7/7b).

## G1 — UI · hộp lỗi 'Mật khẩu quá yếu!…', không gửi POST /api/register, ở lại /register · mật khẩu hợp lệ theo SRS · expected đăng ký thành công

- **TC Fail (14):** 01, 02, 64, 65, 66, 68, 69, 71, 72, 74, 75, 77, 78, 211
- **Blocked ghi case gốc (22):** 03, 04, 06, 08, 09, 10, 11, 12, 13, 14, 15, 61, 62, 200, 203, 204, 205, 208, 215, 217, 218, 223
- **Yêu cầu:** FR-01.1, FR-01.2, FR-01.3, FR-01.4, FR-01.5, FR-01.6, FR-01.7a, FR-01.7b, FR-01.7c, FR-01.8, FR-01.9, FR-01.10
- **Actual tiêu biểu (TC-FR01-01, nguyên văn):** form không có ô Xác nhận mật khẩu: bỏ qua bước nhập V5 (A17); URL=/register; POST /api/register gửi 0 lần; hộp lỗi="Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."; user mới=0
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-01_ui.png`

**Đoạn code liên quan:**

`frontend-web/src/pages/Register.jsx` dòng 15–20 (commit 85af3ba):

```
15|     const flawedStrongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/;
16| 
17|     if (!flawedStrongPasswordRegex.test(password)) {
18|       setError('Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.');
19|       return;
20|     }
```

## G2 — API · expected từ chối · nhận HTTP 200 và tạo user · dữ liệu vi phạm luật Họ Tên

- **TC Fail (5):** 32, 33, 52, 53, 79
- **Yêu cầu:** FR-01.1
- **Actual tiêu biểu (TC-FR01-32, nguyên văn):** HTTP 200 {"message":"User registered successfully","id":7}; user mới=1 [api32_1792424694242@domain.com |  | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-32_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

## G3 — API · expected từ chối · nhận HTTP 200 và tạo user · dữ liệu vi phạm luật Email (bắt buộc/định dạng)

- **TC Fail (15):** 34, 35, 36, 37, 38, 39, 40, 54, 55, 201, 219, 220, 221, 225, 226
- **Yêu cầu:** FR-01.2, FR-01.3
- **Actual tiêu biểu (TC-FR01-34, nguyên văn):** HTTP 200 {"message":"User registered successfully","id":9}; user mới=1 [ | Nguyen Van A | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-34_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

## G4 — API · expected từ chối · nhận HTTP 200 và tạo user · Email trùng tài khoản đã có

- **TC Fail (3):** 41, 42, 206
- **Yêu cầu:** FR-01.4
- **Actual tiêu biểu (TC-FR01-41, nguyên văn):** HTTP 200 {"message":"User registered successfully","id":16}; user mới=1 [test@eshop.com | Nguyen Van A | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-41_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

`backend/database.js` dòng 50–54 (commit 85af3ba):

```
50|         db.run(`CREATE TABLE users (
51|             id INTEGER PRIMARY KEY AUTOINCREMENT,
52|             name TEXT,
53|             email TEXT,
54|             password TEXT,
```

## G5 — API · expected từ chối · nhận HTTP 200 và tạo user · dữ liệu vi phạm luật Mật khẩu

- **TC Fail (18):** 43, 44, 45, 46, 47, 48, 49, 50, 51, 56, 57, 82, 86, 89, 102, 105, 224, 228
- **Yêu cầu:** FR-01.5, FR-01.6, FR-01.7a, FR-01.7b, FR-01.7c, FR-01.8
- **Actual tiêu biểu (TC-FR01-43, nguyên văn):** HTTP 200 {"message":"User registered successfully","id":18}; user mới=1 [api43_1792424709996@domain.com | Nguyen Van A | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-43_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

## G6 — API · body JSON rỗng {} · nhận HTTP 200, tạo user có name/email null

- **TC Fail (1):** 213
- **Yêu cầu:** FR-01.1, FR-01.2, FR-01.5
- **Actual tiêu biểu (TC-FR01-213, nguyên văn):** HTTP 200 {"message":"User registered successfully","id":58}; user mới=1 [null | null | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-213_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

## G7 — API · email có khoảng trắng đầu/cuối · HTTP 200 · email lưu còn khoảng trắng

- **TC Fail (1):** 30
- **Yêu cầu:** FR-01.1, FR-01.2, FR-01.3, FR-01.4, FR-01.5, FR-01.6, FR-01.7a, FR-01.7b, FR-01.7c, FR-01.8
- **Actual tiêu biểu (TC-FR01-30, nguyên văn):** HTTP 200 {"message":"User registered successfully","id":5}; user mới=1 [  api30_1792424692167@domain.com   | Nguyen Van A | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-30_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

## G8 — API · 2 request đồng thời cùng email · cả hai HTTP 200, tạo 2 user cùng email

- **TC Fail (1):** 209
- **Yêu cầu:** FR-01.4
- **Actual tiêu biểu (TC-FR01-209, nguyên văn):** HTTP 200 {"message":"User registered successfully","id":56}; HTTP 200 {"message":"User registered successfully","id":57}; user mới=2 [hiep.sv10@domain.com | Lê Tấn Hiệp | user] [hiep.sv10@domain.com | Lê Tấn Hiệp | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-209_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

`backend/database.js` dòng 50–54 (commit 85af3ba):

```
50|         db.run(`CREATE TABLE users (
51|             id INTEGER PRIMARY KEY AUTOINCREMENT,
52|             name TEXT,
53|             email TEXT,
54|             password TEXT,
```

## G9 — API · mật khẩu hợp lệ dài 200.000 ký tự · HTTP 413, trang lỗi HTML

- **TC Fail (1):** 212
- **Yêu cầu:** FR-01.6
- **Actual tiêu biểu (TC-FR01-212, nguyên văn):** HTTP 413 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>PayloadTooLargeError: request entity too large<br> &nbsp; user mới=0
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-212_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 3–12 (commit 85af3ba):

```
3| const bodyParser = require("body-parser");
4| const db = require("./database");
5| const jwt = require("jsonwebtoken");
6| 
7| const app = express();
8| const PORT = 3000;
9| const SECRET_KEY = "super_secret_key_that_should_not_be_here";
10| 
11| app.use(cors());
12| app.use(bodyParser.json());
```

## G10 — API · header Content-Type: text/plain · HTTP 500, trang lỗi HTML

- **TC Fail (1):** 214
- **Yêu cầu:** API-REG
- **Actual tiêu biểu (TC-FR01-214, nguyên văn):** HTTP 500 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>TypeError: Cannot destructure property &#39;name&#39; of; user mới=0
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-214_req.json`

**Đoạn code liên quan:**

`backend/server.js` dòng 3–12 (commit 85af3ba):

```
3| const bodyParser = require("body-parser");
4| const db = require("./database");
5| const jwt = require("jsonwebtoken");
6| 
7| const app = express();
8| const PORT = 3000;
9| const SECRET_KEY = "super_secret_key_that_should_not_be_here";
10| 
11| app.use(cors());
12| app.use(bodyParser.json());
```

`backend/server.js` dòng 20–29 (commit 85af3ba):

```
20| app.post("/api/register", (req, res) => {
21|   const { name, email, password } = req.body;
22|   db.run(
23|     "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
24|     [name, email, password],
25|     function (err) {
26|       if (err) return res.status(500).json({ error: err.message });
27|       res.json({ message: "User registered successfully", id: this.lastID });
28|     },
29|   );
```

## G11 — UI · mật khẩu 'Abcd 1234' (khoảng trắng, không có ký tự trong tập @$!%*?&) · form chấp nhận, chuyển /login, tạo user

- **TC Fail (1):** 202
- **Yêu cầu:** FR-01.8
- **Actual tiêu biểu (TC-FR01-202, nguyên văn):** form không có ô Xác nhận mật khẩu: bỏ qua bước nhập V5 (A17); URL=/login; POST /api/register gửi 1 lần (HTTP 200); hộp lỗi=không có; user mới=1 [hiep.sv03@domain.com | Lê Tấn Hiệp | user]
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-202_ui.png`

**Đoạn code liên quan:**

`frontend-web/src/pages/Register.jsx` dòng 15–20 (commit 85af3ba):

```
15|     const flawedStrongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/;
16| 
17|     if (!flawedStrongPasswordRegex.test(password)) {
18|       setError('Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.');
19|       return;
20|     }
```

## G12 — UI (kiểm tay) · Họ Tên chứa <img … onerror=alert(1)> · sau đăng nhập bật hộp thoại, thanh điều hướng hiện ảnh lỗi

- **TC Fail (1):** 216
- **Yêu cầu:** FR-01.1, SEC-04
- **Actual tiêu biểu (TC-FR01-216, nguyên văn):** Ngay sau khi đăng nhập, trình duyệt bật hộp thoại 'localhost:5173 cho biết: 1' (alert(1) trong Họ Tên đã chạy), phải nhấn OK 2 lần mới tắt. Trên thanh điều hướng, sau chữ 'Chào,' hiện biểu tượng ảnh lỗi thay vì chuỗi Họ Tên. Trang Hồ sơ hiển thị nguyên văn dạng chữ.
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-216_ui.png`

**Đoạn code liên quan:**

`frontend-web/src/App.jsx` dòng 26–28 (commit 85af3ba):

```
26|             <Link to="/profile" className="hover:underline text-yellow-300">
27|               <span dangerouslySetInnerHTML={{ __html: `Chào, ${user.name}` }} />
28|             </Link>
```

## G13 — GUI · nhãn trường bắt buộc không có '*'

- **TC Fail (1):** 90
- **Yêu cầu:** FR-22.1
- **Actual tiêu biểu (TC-FR01-90, nguyên văn):** nhãn Họ Tên: "Họ Tên"; nhãn Email: "Email"; nhãn Mật khẩu: "Mật khẩu"
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-90_ui.png`

**Đoạn code liên quan:**

`frontend-web/src/pages/Register.jsx` dòng 35–37 (commit 85af3ba):

```
35|         <div>
36|           <label className="block text-gray-700 mb-2">Họ Tên</label>
37|           <input
```

## G14 — GUI · ô Email có type="text"

- **TC Fail (1):** 91
- **Yêu cầu:** FR-22.2
- **Actual tiêu biểu (TC-FR01-91, nguyên văn):** type của ô Email="text"
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-91_ui.png`

**Đoạn code liên quan:**

`frontend-web/src/pages/Register.jsx` dòng 45–49 (commit 85af3ba):

```
45|         <div>
46|           <label className="block text-gray-700 mb-2">Email</label>
47|           <input
48|             type="text"
49|             value={email}
```

## G15 — GUI · form không có ô Xác nhận mật khẩu

- **TC Fail (1):** 94
- **Blocked ghi case gốc (3):** 25, 26, 27
- **Yêu cầu:** FR-01.9
- **Actual tiêu biểu (TC-FR01-94, nguyên văn):** số ô 'Xác nhận mật khẩu'=0
- **Evidence tiêu biểu:** `HW02/A_FR01/evidence/TC-FR01-94_ui.png`

**Đoạn code liên quan:**

`frontend-web/src/pages/Register.jsx` dòng 63–72 (commit 85af3ba):

```
63|           />
64|           <p className="text-xs text-gray-400 mt-1">
65|             Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt.
66|           </p>
67|         </div>
68| 
69|             
70|         <button
71|           type="submit"
72|           className="w-full bg-red-500 text-white py-2 rounded hover:bg-red-600"
```

## Dữ kiện cô lập: TC-FR01-209 chạy lại 3 lần

Lệnh (trong `HW02/tests`): `npx playwright test A_FR01 -g "TC-FR01-209 " --repeat-each=3`; kết quả ở `HW02/tests/results/isolate_209.json` (không merge vào testcases.json).

| Lần | Playwright | Actual (nguyên văn) |
|---|---|---|
| 1 | failed | HTTP 200 {"message":"User registered successfully","id":4}; HTTP 200 {"message":"User registered successfully","id":5}; user mới=2 [hiep.sv10@domain.com \| Lê Tấn Hiệp \| user] [hiep.sv10@domain.com \| Lê Tấn Hiệp \| user] |
| 2 | failed | HTTP 200 {"message":"User registered successfully","id":6}; HTTP 200 {"message":"User registered successfully","id":7}; user mới=2 [hiep.sv10@domain.com \| Lê Tấn Hiệp \| user] [hiep.sv10@domain.com \| Lê Tấn Hiệp \| user] |
| 3 | failed | HTTP 200 {"message":"User registered successfully","id":8}; HTTP 200 {"message":"User registered successfully","id":9}; user mới=2 [hiep.sv10@domain.com \| Lê Tấn Hiệp \| user] [hiep.sv10@domain.com \| Lê Tấn Hiệp \| user] |
