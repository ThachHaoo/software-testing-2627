# Dữ kiện Fail — FR-20 Đăng ký trên Mobile (D_FR20)

> Dữ kiện do AI gom ở bước 7a, chưa phải bug report. **SV quyết G nào thành BUG nào** (gộp/tách), tiêu đề, severity, priority.
> Nhóm G chỉ gom case có triệu chứng quan sát được giống nhau (tầng + quan sát + biến vi phạm). Không có tên bug, severity, priority, kết luận nguyên nhân hay bước tái hiện.
> Nguồn: `HW02/D_FR20/testcases.json` sau commit 6/7b3 (lượt chính thức = lượt 1, `results/D_FR20_manual_20261021-001500.json`, chạy tay trên POCO F5 / Expo Go 54.0.8). Code SUT `tkob-team/eshop-sut` @ `de0f48f`, trích nguyên văn, không bình luận.
> BUG kế tiếp: **BUG-51**; issue mới trên tkob-team/eshop-sut sẽ từ **#197** trở đi.

## Ánh xạ nhóm → bug → issue (SV điền)

| Nhóm | BUG | Issue |
|---|---|---|
| G1 | BUG-51 | |
| G2 | BUG-52 | |
| G3 | BUG-53 | |
| G4 | BUG-54 | |
| G5 | BUG-55 | |
| G6 | BUG-56 | |
| G7 | BUG-57 | |

## SV quyết mapping (21/10/2026)

- G1 → BUG-51, G2 → BUG-52, G3 → BUG-53, G4 → BUG-54, G5 → BUG-55, G6 → BUG-56, G7 → BUG-57: cả 7 đều là bug mới.
- Tiêu chí: tách theo điểm vào (Web UI / API / Mobile). Khác tiêu chí "vị trí cần sửa" của C.
- Lý do SV: "Web, API và Mobile là các điểm vào khác nhau; bug trên Mobile được tái hiện độc lập trên app mobile."
- Khung BUG-51–53 (G1–G3) có mục "Liên quan": BUG A cùng vị trí code server + dòng code chung (AI điền dữ kiện, không nhận định).

## Tổng hợp

| Nhóm | TC Fail | Blocked ghi case gốc | Yêu cầu / giả định bị vi phạm |
|---|---|---|---|
| G1 | 03 | — | TC-03: FR-01.1, D10 |
| G2 | 04, 05, 204 | — | TC-04: FR-01.2, D10; TC-05: FR-01.3, D4, D10; TC-204: FR-01.3, D4, D10 |
| G3 | 06 | — | TC-06: FR-01.4, D5, D10 |
| G4 | 15 | — | TC-15: FR-01.8, D7, D10 |
| G5 | 90 | — | TC-90: FR-22.1 (D13) |
| G6 | 91 | — | TC-91: FR-22.2 (D13: keyboardType email-address) |
| G7 | 94 | 16, 17 | TC-94: FR-01.9 (D9) |

Tổng Fail trong nhóm: 9; cộng TC-FR20-203 (loại riêng) = 10 — khớp 10 Fail của testcases.json. Blocked: TC-16, TC-17 (case gốc TC-94, ghi ở G7).

### Loại riêng — không lập bug

- **TC-FR20-203:** Fail do lỗi thiết kế TC, không lập bug — các lần chạm sau rơi vào màn kế tiếp; procedure không quy định khi màn hình đổi → phần màn hình không đánh giá được. Phần 'đúng 1 tài khoản': ảnh TC-FR20-203_admin_1.png có đúng 1 dòng m203_{ts}@domain.com (ID 17).

## Kiểm trùng issue

`gh api user` = ThachHaoo. `gh issue list -R tkob-team/eshop-sut --state all --limit 300` (21/10/2026): 151 issue, mọi tác giả, gồm cả đã đóng; số lớn nhất #196.
- Không có issue nào về màn Đăng ký của frontend-mobile.
- Issue FR-20 hiện có thuộc màn khác của mobile: #153–#160 (henry-banana: Add to Cart, chi tiết sản phẩm); #57–#61, #69 (nphoang-itus: thanh toán, giỏ, lịch sử đơn, đăng xuất).
- Issue cùng triệu chứng hoặc cùng vị trí code liệt kê theo từng G ở dưới, chỉ để SV so; AI không kết luận trùng hay không trùng.

## Bảng đối chiếu theo nhóm

| Nhóm | BUG A/B/C (issue) — cùng gì | Issue cùng triệu chứng/vị trí (số · trạng thái · tác giả · tiêu đề nguyên văn) |
|---|---|---|
| G1 | BUG-03 (#19) — cùng yêu cầu FR-01.1; cùng vị trí server.js 20–29 (tầng API) | #19 · OPEN · ThachHaoo · [FR-01] Backend API POST /api/register không kiểm tra Họ Tên (name rỗng, chỉ khoảng trắng, null, thiếu trường, sai kiểu) vẫn trả HTTP 200 và tạo user |
| G2 | BUG-04 (#20) — cùng yêu cầu FR-01.2, FR-01.3; cùng vị trí server.js 20–29<br>BUG-08 (#24) — cùng vị trí server.js 20–29 (email lưu nguyên khoảng trắng — A3); yêu cầu khác (A3 ↔ D5) | #20 · OPEN · ThachHaoo · [FR-01] Backend API POST /api/register không kiểm tra Email (rỗng, sai định dạng, thiếu trường, sai kiểu) vẫn trả HTTP 200 và tạo user<br>#4 · OPEN · nphoang-itus · [BUG-FR02-04] Ô email form đăng nhập Web là `type="text"`, không kiểm tra định dạng |
| G3 | BUG-05 (#21) — cùng yêu cầu FR-01.4; cùng vị trí server.js 20–29, database.js<br>BUG-06 (#22) — cùng yêu cầu FR-01.4 (2 request đồng thời); cùng vị trí server.js 20–29 | #21 · OPEN · ThachHaoo · [FR-01] Backend API POST /api/register cho phép đăng ký trùng email đã có trong CSDL (trùng y nguyên, trùng sau khi cắt khoảng trắng, hoặc trùng phần domain khác hoa/thường)<br>#22 · OPEN · ThachHaoo · [FR-01] Gửi 2 request đăng ký đồng thời (race condition) cùng 1 email thì cả 2 đều trả HTTP 200, tạo ra 2 user trùng email trong CSDL |
| G4 | BUG-07 (#23) — cùng yêu cầu FR-01.8 (tầng API, TC-FR01-51 'Abcd1234#'); cùng vị trí server.js 20–29<br>BUG-02 (#18) — cùng yêu cầu FR-01.8 (web: khoảng trắng làm ký tự đặc biệt); vị trí khác (Register.jsx 15–20)<br>BUG-01 (#17) — yêu cầu FR-01.5–01.8 (web từ chối mật khẩu hợp lệ); vị trí khác (Register.jsx 15–20) | #23 · OPEN · ThachHaoo · [FR-01] Backend API POST /api/register thả nổi kiểm tra Mật khẩu: yếu, ngắn, thiếu hoa/thường/số/ký tự đặc biệt, rỗng, thiếu trường hay sai kiểu đều cho tạo user<br>#18 · OPEN · ThachHaoo · [FR-01] Mật khẩu 'Abcd 1234' thêm khoảng trắng làm ký tự đặc biệt lại lọt qua form Đăng ký, tạo user thành công |
| G5 | BUG-12 (#28) — cùng yêu cầu FR-22.1 (web Register.jsx 35–37)<br>BUG-49 (#195) — cùng yêu cầu FR-22.1 (admin, form Thêm sản phẩm) | #28 · OPEN · ThachHaoo · [FR-01] Nhãn các trường bắt buộc trên form Đăng ký (Họ Tên, Email, Mật khẩu) không có ký hiệu dấu sao '*'<br>#7 · OPEN · nphoang-itus · [BUG-FR02-07] Trường bắt buộc của form đăng nhập không có ký hiệu `*`<br>#152 · OPEN · henry-banana · [FR17-17] Coupon form omits required-field markers<br>#195 · OPEN · ThachHaoo · [FR-15] Form Thêm sản phẩm (UI Admin) thiếu nhãn (label) và dấu sao bắt buộc (*) bên cạnh các trường nhập liệu bắt buộc (Tên sản phẩm, Giá tiền, Danh mục) |
| G6 | BUG-13 (#29) — cùng yêu cầu FR-22.2 (web: type="text", Register.jsx 45–49) | #29 · OPEN · ThachHaoo · [FR-01] Ô nhập Email trên form Đăng ký dùng type="text" thay vì type="email"<br>#4 · OPEN · nphoang-itus · [BUG-FR02-04] Ô email form đăng nhập Web là `type="text"`, không kiểm tra định dạng<br>#121 · OPEN · henry-banana · [FR04-25] Disabled Web profile email uses text instead of email input type |
| G7 | BUG-14 (#30) — cùng yêu cầu FR-01.9 (web Register.jsx) | #30 · OPEN · ThachHaoo · [FR-01] Form Đăng ký trên Frontend thiếu hẳn trường 'Xác nhận mật khẩu' theo yêu cầu SRS |

Không có BUG nào của A/B/C ở `frontend-mobile/App.js` dòng 209–240 hay 797–837 (BUG-30…34 của B ghi `/api/cart` không được client nào gọi).

## G1 — Mobile · Họ Tên rỗng → hộp thoại 'Thành công', chuyển màn 'Đăng Nhập', tài khoản được tạo

- **TC Fail (1):** 03
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** TC-03: FR-01.1, D10
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Expected / Actual (lượt 1, rút gọn 300 ký tự):**
  - TC-FR20-03 (Fail) — Expected: Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại hoặc toast; nội dung chữ chỉ ghi Actual) (D10); app vẫn ở màn 'Đăng Ký Tài Khoản' (D10); danh sách ở trang admin 'Quản lý Người dùng' SAU = TRƯỚC (D10, D11). · Actual: Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-03_manual
- **Evidence:** `HW02/D_FR20/evidence/TC-FR20-03_manual_1.png`; ảnh admin cả lượt `HW02/D_FR20/evidence/D_admin_truoc_1.png`, `D_admin_sau_1.png`, `D_admin_sau_2.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-mobile/App.js` dòng 209–240:

```js
 209    const handleRegister = async () => {
 210      setRegisterError("");
 211      const strongPasswordRegex =
 212        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$/;
 213  
 214      if (!strongPasswordRegex.test(registerPassword)) {
 215        setRegisterError(
 216          "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.",
 217        );
 218        return;
 219      }
 220  
 221      try {
 222        const response = await fetch(`${API_URL}/register`, {
 223          method: "POST",
 224          headers: { "Content-Type": "application/json" },
 225          body: JSON.stringify({
 226            name: registerName,
 227            email: registerEmail,
 228            password: registerPassword,
 229          }),
 230        });
 231        const data = await response.json().catch(() => ({}));
 232        if (!response.ok) throw new Error(data.error || "Đăng ký thất bại.");
 233        Alert.alert("Thành công", "Đăng ký tài khoản thành công.");
 234        setEmail(registerEmail);
 235        setPassword("");
 236        setView("login");
 237      } catch (error) {
 238        setRegisterError(error.message || "Đăng ký thất bại.");
 239      }
 240    };
```

`frontend-mobile/App.js` dòng 804–809:

```js
 804          <Text style={styles.label}>Họ Tên</Text>
 805          <TextInput
 806            style={styles.textInput}
 807            value={registerName}
 808            onChangeText={setRegisterName}
 809          />
```

`backend/server.js` dòng 20–30:

```js
  20  app.post("/api/register", (req, res) => {
  21    const { name, email, password } = req.body;
  22    db.run(
  23      "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
  24      [name, email, password],
  25      function (err) {
  26        if (err) return res.status(500).json({ error: err.message });
  27        res.json({ message: "User registered successfully", id: this.lastID });
  28      },
  29    );
  30  });
```

## G2 — Mobile · Email rỗng hoặc sai định dạng (không '@', có dấu cách) → hộp thoại 'Thành công', chuyển màn 'Đăng Nhập', tài khoản được tạo

- **TC Fail (3):** 04, 05, 204
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** TC-04: FR-01.2, D10; TC-05: FR-01.3, D4, D10; TC-204: FR-01.3, D4, D10
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Expected / Actual (lượt 1, rút gọn 300 ký tự):**
  - TC-FR20-04 (Fail) — Expected: Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại hoặc toast; nội dung chữ chỉ ghi Actual) (D10); app vẫn ở màn 'Đăng Ký Tài Khoản' (D10); danh sách ở trang admin 'Quản lý Người dùng' SAU = TRƯỚC (D10, D11). · Actual: Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-04_manual
  - TC-FR20-05 (Fail) — Expected: Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại hoặc toast; nội dung chữ chỉ ghi Actual) (D10); app vẫn ở màn 'Đăng Ký Tài Khoản' (D10); danh sách ở trang admin 'Quản lý Người dùng' SAU = TRƯỚC (D10, D11). · Actual: Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-05_manual
  - TC-FR20-204 (Fail) — Expected: Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại hoặc toast) (D10); app vẫn ở màn 'Đăng Ký Tài Khoản' (D10); danh sách ở trang admin 'Quản lý Người dùng' SAU = TRƯỚC (D10, D11). · Actual: Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-204_manual
- **Evidence:** `HW02/D_FR20/evidence/TC-FR20-04_manual_1.png`, `HW02/D_FR20/evidence/TC-FR20-05_manual_1.png`, `HW02/D_FR20/evidence/TC-FR20-204_manual_1.png`; ảnh admin cả lượt `HW02/D_FR20/evidence/D_admin_truoc_1.png`, `D_admin_sau_1.png`, `D_admin_sau_2.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-mobile/App.js` dòng 209–240:

```js
 209    const handleRegister = async () => {
 210      setRegisterError("");
 211      const strongPasswordRegex =
 212        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$/;
 213  
 214      if (!strongPasswordRegex.test(registerPassword)) {
 215        setRegisterError(
 216          "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.",
 217        );
 218        return;
 219      }
 220  
 221      try {
 222        const response = await fetch(`${API_URL}/register`, {
 223          method: "POST",
 224          headers: { "Content-Type": "application/json" },
 225          body: JSON.stringify({
 226            name: registerName,
 227            email: registerEmail,
 228            password: registerPassword,
 229          }),
 230        });
 231        const data = await response.json().catch(() => ({}));
 232        if (!response.ok) throw new Error(data.error || "Đăng ký thất bại.");
 233        Alert.alert("Thành công", "Đăng ký tài khoản thành công.");
 234        setEmail(registerEmail);
 235        setPassword("");
 236        setView("login");
 237      } catch (error) {
 238        setRegisterError(error.message || "Đăng ký thất bại.");
 239      }
 240    };
```

`frontend-mobile/App.js` dòng 810–816:

```js
 810          <Text style={styles.label}>Email</Text>
 811          <TextInput
 812            style={styles.textInput}
 813            value={registerEmail}
 814            onChangeText={setRegisterEmail}
 815            autoCapitalize="none"
 816          />
```

`backend/server.js` dòng 20–30:

```js
  20  app.post("/api/register", (req, res) => {
  21    const { name, email, password } = req.body;
  22    db.run(
  23      "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
  24      [name, email, password],
  25      function (err) {
  26        if (err) return res.status(500).json({ error: err.message });
  27        res.json({ message: "User registered successfully", id: this.lastID });
  28      },
  29    );
  30  });
```

## G3 — Mobile · Email trùng tài khoản seed 'test@eshop.com' → hộp thoại 'Thành công', chuyển màn 'Đăng Nhập', dòng thứ hai cùng email ở admin

- **TC Fail (1):** 06
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** TC-06: FR-01.4, D5, D10
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Expected / Actual (lượt 1, rút gọn 300 ký tự):**
  - TC-FR20-06 (Fail) — Expected: Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại hoặc toast; nội dung chữ chỉ ghi Actual) (D10); app vẫn ở màn 'Đăng Ký Tài Khoản' (D10); danh sách ở trang admin 'Quản lý Người dùng' SAU = TRƯỚC (D10, D11). · Actual: Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-06_manual
- **Evidence:** `HW02/D_FR20/evidence/TC-FR20-06_manual_1.png`; ảnh admin cả lượt `HW02/D_FR20/evidence/D_admin_truoc_1.png`, `D_admin_sau_1.png`, `D_admin_sau_2.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-mobile/App.js` dòng 209–240:

```js
 209    const handleRegister = async () => {
 210      setRegisterError("");
 211      const strongPasswordRegex =
 212        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$/;
 213  
 214      if (!strongPasswordRegex.test(registerPassword)) {
 215        setRegisterError(
 216          "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.",
 217        );
 218        return;
 219      }
 220  
 221      try {
 222        const response = await fetch(`${API_URL}/register`, {
 223          method: "POST",
 224          headers: { "Content-Type": "application/json" },
 225          body: JSON.stringify({
 226            name: registerName,
 227            email: registerEmail,
 228            password: registerPassword,
 229          }),
 230        });
 231        const data = await response.json().catch(() => ({}));
 232        if (!response.ok) throw new Error(data.error || "Đăng ký thất bại.");
 233        Alert.alert("Thành công", "Đăng ký tài khoản thành công.");
 234        setEmail(registerEmail);
 235        setPassword("");
 236        setView("login");
 237      } catch (error) {
 238        setRegisterError(error.message || "Đăng ký thất bại.");
 239      }
 240    };
```

`backend/server.js` dòng 20–30:

```js
  20  app.post("/api/register", (req, res) => {
  21    const { name, email, password } = req.body;
  22    db.run(
  23      "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
  24      [name, email, password],
  25      function (err) {
  26        if (err) return res.status(500).json({ error: err.message });
  27        res.json({ message: "User registered successfully", id: this.lastID });
  28      },
  29    );
  30  });
```

`backend/database.js` dòng 50–61:

```js
  50          db.run(`CREATE TABLE users (
  51              id INTEGER PRIMARY KEY AUTOINCREMENT,
  52              name TEXT,
  53              email TEXT,
  54              password TEXT,
  55              role TEXT DEFAULT 'user',
  56              login_attempts INTEGER DEFAULT 0,
  57              locked_until DATETIME,
  58              reset_token TEXT,
  59              shipping_address TEXT,
  60              phone TEXT
  61          )`);
```

## G4 — Mobile · Mật khẩu chỉ có ký tự đặc biệt ngoài tập ('#') → hộp thoại 'Thành công', chuyển màn 'Đăng Nhập', tài khoản được tạo

- **TC Fail (1):** 15
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** TC-15: FR-01.8, D7, D10
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Expected / Actual (lượt 1, rút gọn 300 ký tự):**
  - TC-FR20-15 (Fail) — Expected: Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại hoặc toast; nội dung chữ chỉ ghi Actual) (D10); app vẫn ở màn 'Đăng Ký Tài Khoản' (D10); danh sách ở trang admin 'Quản lý Người dùng' SAU = TRƯỚC (D10, D11). · Actual: Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-15_manual
- **Evidence:** `HW02/D_FR20/evidence/TC-FR20-15_manual_1.png`; ảnh admin cả lượt `HW02/D_FR20/evidence/D_admin_truoc_1.png`, `D_admin_sau_1.png`, `D_admin_sau_2.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-mobile/App.js` dòng 209–219:

```js
 209    const handleRegister = async () => {
 210      setRegisterError("");
 211      const strongPasswordRegex =
 212        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$/;
 213  
 214      if (!strongPasswordRegex.test(registerPassword)) {
 215        setRegisterError(
 216          "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.",
 217        );
 218        return;
 219      }
```

`backend/server.js` dòng 20–30:

```js
  20  app.post("/api/register", (req, res) => {
  21    const { name, email, password } = req.body;
  22    db.run(
  23      "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
  24      [name, email, password],
  25      function (err) {
  26        if (err) return res.status(500).json({ error: err.message });
  27        res.json({ message: "User registered successfully", id: this.lastID });
  28      },
  29    );
  30  });
```

## G5 — GUI mobile · nhãn Họ Tên, Email, Mật khẩu không có ký hiệu '*'

- **TC Fail (1):** 90
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** TC-90: FR-22.1 (D13)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Expected / Actual (lượt 1, rút gọn 300 ký tự):**
  - TC-FR20-90 (Fail) — Expected: Mỗi nhãn trường bắt buộc theo FR-01 có ký hiệu '*' bên cạnh. · Actual: Mỗi nhãn không có ký hiệu '*' bên cạnh / Xem hình TC-FR20-90-manual
- **Evidence:** `HW02/D_FR20/evidence/TC-FR20-90_manual_1.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-mobile/App.js` dòng 804–818:

```js
 804          <Text style={styles.label}>Họ Tên</Text>
 805          <TextInput
 806            style={styles.textInput}
 807            value={registerName}
 808            onChangeText={setRegisterName}
 809          />
 810          <Text style={styles.label}>Email</Text>
 811          <TextInput
 812            style={styles.textInput}
 813            value={registerEmail}
 814            onChangeText={setRegisterEmail}
 815            autoCapitalize="none"
 816          />
 817          <Text style={styles.label}>Mật khẩu</Text>
 818          <TextInput
```

## G6 — GUI mobile · chạm ô Email hiện bàn phím chữ, không có phím '@'

- **TC Fail (1):** 91
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** TC-91: FR-22.2 (D13: keyboardType email-address)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Expected / Actual (lượt 1, rút gọn 300 ký tự):**
  - TC-FR20-91 (Fail) — Expected: Chạm vào ô Email hiện bàn phím email (keyboardType email-address theo D13). · Actual: Bàn phím hiện ra, nhưng không phải là bàn phím Email (không có phím '@') / xem hình TC-FR20-91_manual
- **Evidence:** `HW02/D_FR20/evidence/TC-FR20-91_manual_1.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-mobile/App.js` dòng 810–816:

```js
 810          <Text style={styles.label}>Email</Text>
 811          <TextInput
 812            style={styles.textInput}
 813            value={registerEmail}
 814            onChangeText={setRegisterEmail}
 815            autoCapitalize="none"
 816          />
```

## G7 — GUI mobile · màn 'Đăng Ký Tài Khoản' không có trường Xác nhận mật khẩu

- **TC Fail (1):** 94
- **Blocked ghi case gốc (2):** 16, 17
- **Yêu cầu / giả định bị vi phạm:** TC-94: FR-01.9 (D9)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Expected / Actual (lượt 1, rút gọn 300 ký tự):**
  - TC-FR20-94 (Fail) — Expected: Màn 'Đăng Ký Tài Khoản' có trường Xác nhận mật khẩu (FR-01.9). · Actual: Không có ô "Xác nhận mật khẩu" / xem hình TC-FR20-94_manual
- **Evidence:** `HW02/D_FR20/evidence/TC-FR20-94_manual_1.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-mobile/App.js` dòng 797–837:

```js
 797    const renderRegister = () =>
 798      renderScreen(
 799        <ScrollView contentContainerStyle={styles.formContainer}>
 800          <Text style={styles.headerCenter}>Đăng Ký Tài Khoản</Text>
 801          {!!registerError && (
 802            <Text style={styles.errorBoxText}>{registerError}</Text>
 803          )}
 804          <Text style={styles.label}>Họ Tên</Text>
 805          <TextInput
 806            style={styles.textInput}
 807            value={registerName}
 808            onChangeText={setRegisterName}
 809          />
 810          <Text style={styles.label}>Email</Text>
 811          <TextInput
 812            style={styles.textInput}
 813            value={registerEmail}
 814            onChangeText={setRegisterEmail}
 815            autoCapitalize="none"
 816          />
 817          <Text style={styles.label}>Mật khẩu</Text>
 818          <TextInput
 819            style={styles.textInput}
 820            value={registerPassword}
 821            onChangeText={setRegisterPassword}
 822            secureTextEntry
 823          />
 824          <Text style={styles.hintText}>
 825            Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc
 826            biệt.
 827          </Text>
 828          <TouchableOpacity style={styles.redButton} onPress={handleRegister}>
 829            <Text style={styles.buttonText}>Đăng Ký</Text>
 830          </TouchableOpacity>
 831          <TouchableOpacity onPress={() => setView("login")}>
 832            <Text style={styles.centerSmall}>
 833              Đã có tài khoản? <Text style={styles.linkText}>Đăng nhập</Text>
 834            </Text>
 835          </TouchableOpacity>
 836        </ScrollView>,
 837      );
```

## 7a2 — Dữ kiện vị trí cần sửa theo G (21/10/2026)

> Chỉ dữ kiện suy từ code SUT @ `de0f48f`; không đề xuất gộp/tách, không kết luận trùng bug. "Chỗ có thể phải đổi" = chỗ mà nếu thay đổi thì triệu chứng của TC trong G mất, theo luồng code bên dưới. Chỗ code của BUG lấy từ mục code trong `HW02/bugs/BUG-xx.md`.

**Đường đi dữ liệu chung (G1–G4):** ô mobile (Họ Tên `App.js` 805–809, Email 811–816, Mật khẩu 818–823; giá trị lưu nguyên vào state) → `handleRegister` (209) → chỉ kiểm `registerPassword` bằng regex (211–219) → `fetch POST ${API_URL}/register`, body `{name, email, password}` (222–230) → `server.js` 20–29: `INSERT` thẳng, không kiểm, lỗi CSDL → 500, còn lại → 200 → `App.js` 231–236: `response.ok` → `Alert 'Thành công'`, `setView("login")`; không ok → `throw` (232) → `setRegisterError` (238), ở lại màn Đăng Ký. `frontend-mobile/App.js` chỉ import `react`, `react-native`, `expo-status-bar` (dòng 1–14): không dùng chung code với `frontend-web`/`frontend-admin`.

| G | TC | Chỗ có thể phải đổi (tầng · dòng) | Chỗ của BUG A/B/C | Trùng với chỗ ở cột trước? | Sửa riêng chỗ của BUG A → triệu chứng TC mất? | Lý do (theo code) |
|---|---|---|---|---|---|---|
| G1 | 03 | (1) mobile · `App.js` 209–219 (kiểm Họ Tên trước `fetch`); (2) server · `server.js` 20–29 (kiểm `name`, trả mã không 2xx) | BUG-03: `server.js` 20–29 | trùng (2); không trùng (1) | có — nếu server trả mã không 2xx | `App.js` 232 chỉ xét `response.ok`: mã lỗi → `throw` → hiện lỗi (238), không `Alert`/`setView`, không `INSERT`; nếu server vẫn trả 200 kèm lỗi thì không mất. |
| G2 | 04, 05, 204 | (1) mobile · `App.js` 209–219 (kiểm Email rỗng/định dạng); (2) server · `server.js` 20–29 (kiểm `email`) | BUG-04: `server.js` 20–29; BUG-08: `server.js` 20–29 | BUG-04, BUG-08 trùng (2); không trùng (1) | BUG-04: có — nếu trả mã không 2xx; BUG-08: không | BUG-04 như G1 (232 → 238). BUG-08 là cắt khoảng trắng email: email rỗng/không '@'/có dấu cách giữa sau khi cắt vẫn sai định dạng, nếu chỉ cắt mà không kiểm thì `INSERT` vẫn chạy. |
| G3 | 06 | (1) server · `server.js` 20–29 (tìm email trước `INSERT`, trả mã không 2xx); (2) server · `database.js` 50–61 (cột `email TEXT` thêm UNIQUE → `db.run` lỗi → 500 ở `server.js` 26) | BUG-05: `server.js` 20–29, `database.js` 50–54; BUG-06: `server.js` 20–29, `database.js` 50–54 | BUG-05, BUG-06 trùng (1) và (2) | có (BUG-05, BUG-06) | Mobile không gọi endpoint nào để biết email đã có trước khi gửi (209–230), nên chỉ server chặn được; khi server trả mã không 2xx, `App.js` 232 → 238. |
| G4 | 15 | (1) mobile · `App.js` 211–212 (regex `(?=.*[^A-Za-z\d])` nhận '#' là ký tự đặc biệt); (2) server · `server.js` 20–29 (kiểm `password`) | BUG-07: `server.js` 20–29; BUG-01, BUG-02: `frontend-web/src/pages/Register.jsx` 15–20 | BUG-07 trùng (2); BUG-01, BUG-02 không trùng | BUG-07: có — nếu trả mã không 2xx; BUG-01/02: không | 'Abcd1234#' qua regex mobile 211–212 nên được gửi; chặn ở server → 232 → 238. Register.jsx là file của web, mobile không import (dòng 1–14). |
| G5 | 90 | mobile · `App.js` 804, 810, 817 (`<Text style={styles.label}>` Họ Tên / Email / Mật khẩu) | BUG-12: `Register.jsx` 35–37; BUG-49: `frontend-admin/src/App.jsx` 490–507 | không trùng | không | Nhãn mobile là `Text` riêng trong `App.js`; Register.jsx và admin App.jsx không được mobile dùng. |
| G6 | 91 | mobile · `App.js` 811–816 (`TextInput` Email không có `keyboardType`) | BUG-13: `Register.jsx` 45–49 | không trùng | không | Loại bàn phím do prop của `TextInput` mobile quyết định; `type` của input web không ảnh hưởng. |
| G7 | 94 (Blocked 16, 17) | mobile · `App.js` 797–837 (thêm ô Xác nhận), 209–219 (so khớp), 225–229 (body nếu server cũng kiểm); server · `server.js` 20–29 (chỉ khi body có trường xác nhận) | BUG-14: `Register.jsx` 63–72 | không trùng | không | Màn mobile dựng riêng ở `renderRegister` (797–837); thêm ô ở form web không thêm ô trên mobile. |

## 7c — AI kiểm tái hiện + sửa dữ kiện (21/10/2026, sau commit 7/7b `6d16d98`)

### Đầu vào
- 7/7b (`6d16d98`) chỉ chạm `HW02/bugs/BUG-51.md` … `BUG-57.md`. HEAD = merge `af05093` (SV) của `6d16d98` với `40052e9`; cây không đổi so với `6d16d98`.
- `git status`: chỉ có `A_prompt_log.md` (hook tự cập nhật).
- Không còn chỗ `<SV viết>` nào trong BUG-51…57.
- Severity/Priority: cả 7 BUG đúng thang (51–54, 57: High/High; 55: Low/Low; 56: Medium/Medium).
- Tiêu đề trong file không có tiền tố `[FR-20]`.

### Phần server — chạy thật (PowerShell 5.1)

Restart backend (`node server.js`, CSDL seed lại) → gửi POST /api/register với đúng giá trị trong bước tái hiện SV ghi. Body JSON theo thứ tự khoá như mobile (App.js 225–229). Kiểm dữ liệu: đăng nhập admin seed → GET /api/admin/users. Chạy xong restart backend lần nữa để xoá dữ liệu thử. BUG-55…57 là GUI, không có phần server.

Lệnh (`repro_D.ps1`, chạy bằng `powershell.exe -NoProfile -ExecutionPolicy Bypass -File`):

```powershell
$ErrorActionPreference = 'Stop'
$base = 'http://localhost:3000/api'
function Post($label, $path, $obj, $headers = @{}) {
    $body = $obj | ConvertTo-Json -Compress
    "### $label"
    "POST $path  body=$body"
    try {
        $r = Invoke-WebRequest -UseBasicParsing -Method Post -Uri "$base$path" -ContentType 'application/json' -Headers $headers -Body ([Text.Encoding]::UTF8.GetBytes($body))
        "HTTP $($r.StatusCode)  $($r.Content)"
        return $r.Content
    } catch {
        $resp = $_.Exception.Response
        if ($resp) {
            $s = $resp.GetResponseStream(); $s.Position = 0
            "HTTP $([int]$resp.StatusCode)  $((New-Object IO.StreamReader($s)).ReadToEnd())"
        } else { "ERROR $($_.Exception.Message)" }
    }
}
$cases = @(
    @('BUG-51 / TC-FR20-03', @{ name = ''; email = 'm03_2231@domain.com'; password = 'Abcd1234!' }),
    @('BUG-52 / TC-FR20-04', @{ name = 'Nguyễn Văn Ánh'; email = ''; password = 'Abcd1234!' }),
    @('BUG-52 / TC-FR20-05', @{ name = 'Nguyễn Văn Ánh'; email = 'm05_2231domain.com'; password = 'Abcd1234!' }),
    @('BUG-52 / TC-FR20-204', @{ name = 'Nguyễn Văn Ánh'; email = 'm204_2231 @domain.com'; password = 'Abcd1234!' }),
    @('BUG-53 / TC-FR20-06', @{ name = 'Nguyễn Văn Ánh'; email = 'test@eshop.com'; password = 'Abcd1234!' }),
    @('BUG-54 / TC-FR20-15', @{ name = 'Nguyễn Văn Ánh'; email = 'm15_2231@domain.com'; password = 'Abcd1234#' })
)
foreach ($c in $cases) {
    # giữ thứ tự khoá như App.js 225–229: name, email, password
    $o = [ordered]@{ name = $c[1].name; email = $c[1].email; password = $c[1].password }
    Post $c[0] '/register' $o
    ''
}
'### Kiểm dữ liệu: đăng nhập admin seed rồi GET /api/admin/users'
$login = Invoke-WebRequest -UseBasicParsing -Method Post -Uri "$base/login" -ContentType 'application/json' -Body ([Text.Encoding]::UTF8.GetBytes('{"email":"admin@eshop.com","password":"Admin123!"}'))
"POST /login (admin@eshop.com) → HTTP $($login.StatusCode)"
$token = ($login.Content | ConvertFrom-Json).token
$u = Invoke-WebRequest -UseBasicParsing -Uri "$base/admin/users" -Headers @{ Authorization = "Bearer $token" }
"GET /admin/users → HTTP $($u.StatusCode)"
($u.Content | ConvertFrom-Json) | ForEach-Object { "id=$($_.id) | name=[$($_.name)] | email=[$($_.email)] | role=$($_.role)" }
```

Output:

```text
### BUG-51 / TC-FR20-03
POST /register  body={"name":"","email":"m03_2231@domain.com","password":"Abcd1234!"}
HTTP 200  {"message":"User registered successfully","id":3}
{"message":"User registered successfully","id":3}

### BUG-52 / TC-FR20-04
POST /register  body={"name":"Nguyễn Văn Ánh","email":"","password":"Abcd1234!"}
HTTP 200  {"message":"User registered successfully","id":4}
{"message":"User registered successfully","id":4}

### BUG-52 / TC-FR20-05
POST /register  body={"name":"Nguyễn Văn Ánh","email":"m05_2231domain.com","password":"Abcd1234!"}
HTTP 200  {"message":"User registered successfully","id":5}
{"message":"User registered successfully","id":5}

### BUG-52 / TC-FR20-204
POST /register  body={"name":"Nguyễn Văn Ánh","email":"m204_2231 @domain.com","password":"Abcd1234!"}
HTTP 200  {"message":"User registered successfully","id":6}
{"message":"User registered successfully","id":6}

### BUG-53 / TC-FR20-06
POST /register  body={"name":"Nguyễn Văn Ánh","email":"test@eshop.com","password":"Abcd1234!"}
HTTP 200  {"message":"User registered successfully","id":7}
{"message":"User registered successfully","id":7}

### BUG-54 / TC-FR20-15
POST /register  body={"name":"Nguyễn Văn Ánh","email":"m15_2231@domain.com","password":"Abcd1234#"}
HTTP 200  {"message":"User registered successfully","id":8}
{"message":"User registered successfully","id":8}

### Kiểm dữ liệu: đăng nhập admin seed rồi GET /api/admin/users
POST /login (admin@eshop.com) → HTTP 200
GET /admin/users → HTTP 200
id=1 | name=[Admin User] | email=[admin@eshop.com] | role=admin
id=2 | name=[Test User] | email=[test@eshop.com] | role=user
id=3 | name=[] | email=[m03_2231@domain.com] | role=user
id=4 | name=[Nguyễn Văn Ánh] | email=[] | role=user
id=5 | name=[Nguyễn Văn Ánh] | email=[m05_2231domain.com] | role=user
id=6 | name=[Nguyễn Văn Ánh] | email=[m204_2231 @domain.com] | role=user
id=7 | name=[Nguyễn Văn Ánh] | email=[test@eshop.com] | role=user
id=8 | name=[Nguyễn Văn Ánh] | email=[m15_2231@domain.com] | role=user
```

### Phần thao tác trên mobile — đối chiếu code + evidence (AI không chạy được)

Bước SV ghi khớp code App.js, không phải sửa bước nào:
- header `Đăng nhập` (dòng 429–432);
- màn `Đăng Nhập` (762), link `Chưa có tài khoản? Đăng ký ngay` (785–787);
- màn `Đăng Ký Tài Khoản` (800); nhãn `Họ Tên`, `Email`, `Mật khẩu` (804, 810, 817); nút `Đăng Ký` (828–829).

Đã thêm dòng "(Bước trên thiết bị: AI chưa chạy lại; …)" vào cuối mục Bước tái hiện của cả 7 BUG.

### Tiền điều kiện — có đủ để dựng lại không (SV viết, AI chỉ liệt kê)

| BUG | Thiếu |
|---|---|
| 51, 52 | restart backend để CSDL seed lại; áp `mobile_api_url.patch` / IP `192.168.2.12`; `npx expo start` + mở bằng Expo Go (SDK 54) |
| 53, 54 | áp patch IP; `npx expo start` + Expo Go (đã có ý seed lại) |
| 55, 56, 57 | áp patch IP; `npx expo start` + Expo Go |

### Log sửa dữ kiện 7c (trước → sau)

| BUG | Trước | Sau |
|---|---|---|
| BUG-51 | - Sau khi bấm đóng thông báo, app tự động chuyển luôn sang màn 'Đăng Nhập'. | - Hộp thoại hiện trên nền màn 'Đăng Nhập': app đã chuyển màn ngay khi hiện hộp thoại, trước khi đóng (ảnh `TC-FR20-03_manual_1.png`; App.js 233–236 gọi `Alert.alert` rồi `setView("login")` liền nhau). |
| BUG-51 | - Kiểm tra lại danh sách bên trang admin thì thấy xuất hiện thêm một dòng tài khoản mới có email m03_2231@domain.com, nhưng cột Họ Tên bị bỏ rỗng. | - Kiểm tra lại danh sách bên trang admin thì thấy xuất hiện thêm một dòng tài khoản mới có email m03_{ts}@domain.com (ID 3, ảnh `D_admin_sau_1.png`). Trang admin không có cột Họ Tên (cột: ID, Email, Role, Số ĐT); Họ Tên rỗng chỉ thấy qua API khi AI chạy lại phần server (7c: `name=[]`). |
| BUG-51 | (cuối Các bước tái hiện) | (Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1) |
| BUG-51 | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại. | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend). Phần server AI chạy lại 21/10/2026 (7c, sau restart backend, giá trị theo bước SV): POST /api/register → HTTP 200 `User registered successfully`; GET /api/admin/users: id=3, name=[] , email=[m03_2231@domain.com]. Bước trên thiết bị chưa chạy lại. |
| BUG-52 | - Sau khi bấm đóng hộp thoại, app tự động chuyển luôn sang màn hình 'Đăng Nhập'. | - Hộp thoại hiện trên nền màn 'Đăng Nhập': app đã chuyển màn ngay khi hiện hộp thoại, trước khi đóng (ảnh `TC-FR20-04_manual_1.png`; App.js 233–236 gọi `Alert.alert` rồi `setView("login")` liền nhau). |
| BUG-52 | - Mở web admin kiểm tra danh sách người dùng thì thấy trong cả 3 lượt chạy đều bị chèn thêm tài khoản mới vào CSDL với chuỗi Email rỗng hoặc sai định dạng đúng như đã nhập trên app. | - Mở web admin kiểm tra danh sách người dùng thì thấy cả 3 case (cùng lượt 1) đều bị chèn thêm tài khoản mới vào CSDL với chuỗi Email rỗng hoặc sai định dạng như đã nhập trên app: ID 4 (Email trống), ID 5 `m05_{ts}domain.com`, ID 8 `m204_{ts}@ domain.com` (ảnh `D_admin_sau_1.png`). |
| BUG-52 | do tính năng auto-correct của bàn phím di động thì client | do tính năng auto-correct của bàn phím di động (chưa kiểm chứng) thì client |
| BUG-52 | (cuối Các bước tái hiện) | (Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1) |
| BUG-52 | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại. | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend). Phần server AI chạy lại 21/10/2026 (7c, sau restart backend, giá trị theo bước SV): POST /api/register → HTTP 200 `User registered successfully`; GET /api/admin/users: id=4 email=[], id=5 email=[m05_2231domain.com], id=6 email=[m204_2231 @domain.com]. Bước trên thiết bị chưa chạy lại. |
| BUG-53 | - Sau khi bấm đóng thông báo, app tự động chuyển luôn sang màn 'Đăng Nhập'. | - Hộp thoại hiện trên nền màn 'Đăng Nhập': app đã chuyển màn ngay khi hiện hộp thoại, trước khi đóng (ảnh `TC-FR20-06_manual_1.png`; App.js 233–236 gọi `Alert.alert` rồi `setView("login")` liền nhau). |
| BUG-53 | - Kiểm tra danh sách bên trang web admin thì thấy xuất hiện thêm một dòng tài khoản mới mang đúng email test@eshop.com, dẫn đến việc CSDL bị trùng lặp email. | - Kiểm tra danh sách bên trang web admin thì thấy xuất hiện thêm một dòng tài khoản mới mang đúng email test@eshop.com (ID 6, cùng email với ID 2; ảnh `D_admin_sau_1.png`), dẫn đến việc CSDL bị trùng lặp email. |
| BUG-53 | (cuối Các bước tái hiện) | (Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1) |
| BUG-53 | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại. | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend). Phần server AI chạy lại 21/10/2026 (7c, sau restart backend, giá trị theo bước SV): POST /api/register → HTTP 200 `User registered successfully`; GET /api/admin/users: id=7 email=[test@eshop.com] (cùng email với id=2 seed). Bước trên thiết bị chưa chạy lại. |
| BUG-54 | - Sau khi bấm đóng thông báo, app tự động chuyển luôn sang màn 'Đăng Nhập'. | - Hộp thoại hiện trên nền màn 'Đăng Nhập': app đã chuyển màn ngay khi hiện hộp thoại, trước khi đóng (ảnh `TC-FR20-15_manual_1.png`; App.js 233–236 gọi `Alert.alert` rồi `setView("login")` liền nhau). |
| BUG-54 | - Kiểm tra danh sách bên trang web admin thì thấy xuất hiện thêm một dòng tài khoản mới mang email m15_2231@domain.com với mật khẩu Abcd1234# lọt qua thành công. | - Kiểm tra danh sách bên trang web admin thì thấy xuất hiện thêm một dòng tài khoản mới mang email m15_{ts}@domain.com (ID 7, ảnh `D_admin_sau_1.png`); trang admin không hiển thị mật khẩu. |
| BUG-54 | (cuối Các bước tái hiện) | (Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1) |
| BUG-54 | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại. | - Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend). Phần server AI chạy lại 21/10/2026 (7c, sau restart backend, giá trị theo bước SV): POST /api/register → HTTP 200 `User registered successfully`; GET /api/admin/users: id=8 email=[m15_2231@domain.com]. Bước trên thiết bị chưa chạy lại. |
| BUG-55 | (cuối Các bước tái hiện) | (Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1) |
| BUG-56 | (cuối Các bước tái hiện) | (Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1) |
| BUG-57 | (cuối Các bước tái hiện) | (Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1) |

Không sửa: Severity, Priority, tiêu đề, Expected, câu Nhận định (ngoài nhãn "(chưa kiểm chứng)").

### Điểm SV tự sửa (chữ của SV — AI không sửa)

- **BUG-51:**
  - Tiền điều kiện: lặp chữ "máy máy tính"; thiếu các mục đã nêu ở bảng trên.
  - Mục "Expected (trích SRS)" không có câu trích nguyên văn SRS (README.md dòng 32).
- **BUG-52:**
  - Tiền điều kiện: "máy máy tính"; thiếu các mục ở bảng trên.
  - Expected không có câu trích nguyên văn SRS (dòng 33).
  - Expected "Server phải từ chối request": TC-04/05/204 Expected chỉ khẳng định danh sách admin SAU = TRƯỚC (D10); không có câu SRS/giả định làm căn cứ cho "server từ chối".
- **BUG-53:** Tiền điều kiện thiếu các mục ở bảng trên; Expected không có câu trích nguyên văn SRS (dòng 33).
- **BUG-54:**
  - Nhận định: "guyên nhân" (thiếu chữ).
  - Expected "Phía server phải từ chối request": thiếu căn cứ như BUG-52.
  - Expected không có câu trích nguyên văn SRS (dòng 34); Tiền điều kiện thiếu các mục ở bảng trên.
- **BUG-55:**
  - Nhận định ghi `<Text style="{styles.label}">`, nhưng code App.js 804 là `style={styles.label}` (không có dấu nháy).
  - Expected không trích nguyên văn FR-22.1; Tiền điều kiện thiếu các mục ở bảng trên.
- **BUG-56:**
  - Tiêu đề có dấu backtick thừa ở đầu.
  - Expected thêm "phím dấu chấm . ngay trên bàn phím chính": D13 chỉ nêu `keyboardType email-address`, thiếu căn cứ cho phím '.'.
  - Tiền điều kiện thiếu các mục ở bảng trên.
- **BUG-57:** Expected không có câu trích nguyên văn SRS (dòng 35); Tiền điều kiện thiếu các mục ở bảng trên.
- **BUG-55, BUG-56 (mục Yêu cầu, AI điền ở khung, SV duyệt):** D13 có loại "phạm vi + quyết định Expected". Quy ước C: giả định phạm vi không vào "yêu cầu bị vi phạm" → SV quyết giữ hay bỏ D13.

### AI phát hiện (ngoài bước SV; không đưa vào bug, SV quyết)

- TC-FR20-204, lượt 1: ảnh điện thoại (`TC-FR20-204_manual_1.png`, ô Username) và ảnh admin (ID 8) cho thấy email đã nhập là `m204_{ts}@ domain.com` (dấu cách **sau** '@'). Input của TC là `m204_{ts} @domain.com` (dấu cách trước '@'), cũng là ví dụ trong bước 3 của BUG-52. Cả hai giá trị đều thuộc lớp "khoảng trắng bên trong" (EC5).
- Lịch sử git có 2 commit 7/7a4 cùng cây: `40052e9` (đã lên remote) và `75da144` (AI amend để sửa message sau khi `40052e9` đã được push). SV merge lại ở `af05093`. Nguyên nhân: AI amend commit đã push.
