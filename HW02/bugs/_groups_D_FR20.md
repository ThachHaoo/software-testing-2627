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
