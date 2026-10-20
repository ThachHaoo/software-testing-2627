# BUG-52

- **ID:** BUG-52
- **Tiêu đề:** App Mobile cho phép nhập Email rỗng hoặc sai định dạng (thiếu '@', có khoảng trắng ở giữa) vẫn báo thành công và tạo tài khoản vào CSDL
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã); thay đổi cục bộ duy nhất: `frontend-mobile/App.js` dòng 16 `API_URL = "http://192.168.2.12:3000/api"` (`HW02/env/mobile_api_url.patch`)
- Máy: Windows 11 Home Single Language 10.0.26200, backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Điện thoại: POCO F5 · OS 1.0.5.0.UMRTWXM · Android 14 (UKQ1.230804.001); Expo Go 54.0.8 (SDK 54); locale/bàn phím Tiếng Việt (Việt Nam) · QWERTY
- Mobile: màn 'Đăng Ký Tài Khoản' (frontend-mobile, Expo); điểm quan sát dữ liệu: web admin http://localhost:5174 → 'Quản lý Người dùng'
- Ngày chạy: 2026-10-21 (lượt chính thức = lượt 1, bắt đầu 00:15, Asia/Saigon; chạy tay)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/D_FR20/RUN.md`

## Tiền điều kiện

- Backend đã được khởi động lại (`node server.js`) để CSDL khôi phục trạng thái dữ liệu seed sạch.

- Web Admin đã đăng nhập bằng tài khoản `admin@eshop.com` và đang mở sẵn tab 'Quản lý Người dùng' để theo dõi dữ liệu.

- App mobile được chạy bằng lệnh `npx expo start`, mở qua ứng dụng Expo Go trên điện thoại Android, kết nối cùng mạng với server và đang ở trạng thái ban đầu chưa đăng nhập.

## Các bước tái hiện

1. Trên app mobile, bấm vào 'Đăng nhập' ở thanh header, sau đó chọn 'Đăng ký ngay' để vào màn hình 'Đăng Ký Tài Khoản'.

2. Nhập Họ Tên hợp lệ (ví dụ: Nguyễn Văn Ánh).

3. Tại ô 'Email', thử nhập một trong ba trường hợp sai sau:
  + Trường hợp 1 (TC-FR20-04): Để trống hoàn toàn ô Email (không nhập gì).
  + Trường hợp 2 (TC-FR20-05): Nhập chuỗi Email thiếu ký tự '@' (ví dụ: m05_2231domain.com).
  + Trường hợp 3 (TC-FR20-204): Nhập chuỗi Email có chứa khoảng trắng ở giữa do bàn phím tự động sửa/chèn gợi ý (ví dụ: m204_2231 @domain.com).

4. Nhập Mật khẩu đúng chuẩn quy định (ví dụ: Abcd1234!).

5. Bấm nút 'Đăng Ký'.

(Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1)

## Expected (trích SRS)

- Hệ thống phải bắt buộc người dùng nhập Email theo quy định FR-01.2 và Email phải chuẩn định dạng user@domain.com theo FR-01.3 (D4).

- Khi Email rỗng hoặc sai định dạng (thiếu '@' hoặc dính khoảng trắng ở giữa), app phải chặn lại và hiển thị thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại alert hoặc toast).

- Giao diện app giữ nguyên người dùng ở màn 'Đăng Ký Tài Khoản'.

- Hệ thống từ chối đăng ký, không được tạo thêm dòng tài khoản mới nào trong CSDL (danh sách bên web admin giữ nguyên).

Trích SRS (AI chép nguyên văn): README.md dòng 32: "Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**."
Trích SRS (AI chép nguyên văn): README.md dòng 33: "Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống."

## Actual

- Trong cả ba trường hợp trên, vừa bấm Đăng Ký xong thì app hiển thị ngay hộp thoại Dialog báo 'Đăng ký tài khoản thành công'.

- Hộp thoại hiện trên nền màn 'Đăng Nhập': app đã chuyển màn ngay khi hiện hộp thoại, trước khi đóng (ảnh `TC-FR20-04_manual_1.png`; App.js 233–236 gọi `Alert.alert` rồi `setView("login")` liền nhau).

- Mở web admin kiểm tra danh sách người dùng thì thấy cả 3 case (cùng lượt 1) đều bị chèn thêm tài khoản mới vào CSDL với chuỗi Email rỗng hoặc sai định dạng như đã nhập trên app: ID 4 (Email trống), ID 5 `m05_{ts}domain.com`, ID 8 `m204_{ts}@ domain.com` (ảnh `D_admin_sau_1.png`).

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR20-04_manual_1.png`
- TC-FR20-04: `HW02/D_FR20/evidence/TC-FR20-04_manual_1.png`
- TC-FR20-05: `HW02/D_FR20/evidence/TC-FR20-05_manual_1.png`
- TC-FR20-204: `HW02/D_FR20/evidence/TC-FR20-204_manual_1.png`
- Ảnh admin cả lượt: `HW02/D_FR20/evidence/D_admin_truoc_1.png`, `HW02/D_FR20/evidence/D_admin_sau_1.png`, `HW02/D_FR20/evidence/D_admin_sau_2.png`

## TC liên quan

- Fail (3): TC-FR20-04, TC-FR20-05, TC-FR20-204
- Nhóm dữ kiện: G2 trong `HW02/bugs/_groups_D_FR20.md`

## Yêu cầu

- **FR-01.2:** Người dùng phải cung cấp Email (trường bắt buộc). [D2]
- **FR-01.3:** Email phải có định dạng hợp lệ (user@domain.com). [D2]
- **D4** (giả định, kế thừa A2 – Email định dạng): hợp lệ = <local>@<domain>.<tld> (đúng một '@', local không rỗng, domain có ít nhất một '.', không rỗng hai bên dấu chấm). Khác A: trên mobile không có trình duyệt nên quy tắc HTML5 (tham chiếu phụ của A2) không áp dụng; không có cận trên độ dài
- **D10** (giả định, oracle khi bị từ chối): oracle chính = không có tài khoản mới phía server (D11). Kèm theo: có thông báo lỗi trên app ở bất kỳ kênh nào (chữ trên màn hình, hộp thoại, toast) + vẫn ở màn 'Đăng Ký Tài Khoản'; nội dung chữ chỉ ghi Actual, không phân loại theo chữ của SUT
- Theo TC: TC-FR20-04: FR-01.2, D10; TC-FR20-05: FR-01.3, D4, D10; TC-FR20-204: FR-01.3, D4, D10
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Liên quan

- BUG cùng vị trí code server (A_FR01): BUG-04 (#20), BUG-08 (#24)
- Dòng code chung: `backend/server.js` dòng 20–29

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR20-04): `Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-04_manual`
- Actual nguyên văn (TC-FR20-05): `Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-05_manual`
- Actual nguyên văn (TC-FR20-204): `Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-204_manual`
- Giá trị Email thực nhập ở lượt 1 (TC-FR20-204, theo ảnh `TC-FR20-204_manual_1.png` ô Username và ảnh admin ID 8): `m204_{ts}@ domain.com` (dấu cách sau '@'); input TC là `m204_{ts} @domain.com`; cả hai thuộc EC5.
- Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend). Phần server AI chạy lại 21/10/2026 (7c, sau restart backend, giá trị theo bước SV): POST /api/register → HTTP 200 `User registered successfully`; GET /api/admin/users: id=4 email=[], id=5 email=[m05_2231domain.com], id=6 email=[m204_2231 @domain.com]. Bước trên thiết bị chưa chạy lại.
- Đoạn code trích nguyên văn: `frontend-mobile/App.js` dòng 209–240

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

- Đoạn code trích nguyên văn: `frontend-mobile/App.js` dòng 810–816

  ```js
   810          <Text style={styles.label}>Email</Text>
   811          <TextInput
   812            style={styles.textInput}
   813            value={registerEmail}
   814            onChangeText={setRegisterEmail}
   815            autoCapitalize="none"
   816          />
  ```

- Đoạn code trích nguyên văn: `backend/server.js` dòng 20–30

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

### Nhận định

- Tương tự trường hợp Họ Tên, hàm handleRegister ở App.js trên app mobile hoàn toàn không viết bất kỳ dòng lệnh nào để validate biến registerEmail. Cho dù email có để trống, nhập thiếu ký tự @ hay dính khoảng trắng ở giữa do tính năng auto-correct của bàn phím di động (chưa kiểm chứng) thì client vẫn đóng gói gửi thẳng sang server qua request POST /api/register.

- Đồng thời, phía server ở file server.js cũng bỏ ngỏ không kiểm tra tính hợp lệ hay định dạng của email mà thực thi ngay lệnh INSERT vào CSDL SQLite. Việc không validate ở cả hai phía làm cho dữ liệu rác/lỗi dễ dàng lưu trữ thành công vào hệ thống.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
