# BUG-51

- **ID:** BUG-51
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã); thay đổi cục bộ duy nhất: `frontend-mobile/App.js` dòng 16 `API_URL = "http://192.168.2.12:3000/api"` (`HW02/env/mobile_api_url.patch`)
- Máy: Windows 11 Home Single Language 10.0.26200, backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Điện thoại: POCO F5 · OS 1.0.5.0.UMRTWXM · Android 14 (UKQ1.230804.001); Expo Go 54.0.8 (SDK 54); locale/bàn phím Tiếng Việt (Việt Nam) · QWERTY
- Mobile: màn 'Đăng Ký Tài Khoản' (frontend-mobile, Expo); điểm quan sát dữ liệu: web admin http://localhost:5174 → 'Quản lý Người dùng'
- Ngày chạy: 2026-10-21 (lượt chính thức = lượt 1, bắt đầu 00:15, Asia/Saigon; chạy tay)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/D_FR20/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR20-03_manual_1.png`
- TC-FR20-03: `HW02/D_FR20/evidence/TC-FR20-03_manual_1.png`
- Ảnh admin cả lượt: `HW02/D_FR20/evidence/D_admin_truoc_1.png`, `HW02/D_FR20/evidence/D_admin_sau_1.png`, `HW02/D_FR20/evidence/D_admin_sau_2.png`

## TC liên quan

- Fail (1): TC-FR20-03
- Nhóm dữ kiện: G1 trong `HW02/bugs/_groups_D_FR20.md`

## Yêu cầu

- **FR-01.1:** Người dùng phải cung cấp Họ Tên (trường bắt buộc). [áp cho mobile theo D2]
- **D10** (giả định, oracle khi bị từ chối): oracle chính = không có tài khoản mới phía server (D11). Kèm theo: có thông báo lỗi trên app ở bất kỳ kênh nào (chữ trên màn hình, hộp thoại, toast) + vẫn ở màn 'Đăng Ký Tài Khoản'; nội dung chữ chỉ ghi Actual, không phân loại theo chữ của SUT
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Liên quan

- BUG cùng vị trí code server (A_FR01): BUG-03 (#19)
- Dòng code chung: `backend/server.js` dòng 20–29

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR20-03): `Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-03_manual`
- Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại.
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

- Đoạn code trích nguyên văn: `frontend-mobile/App.js` dòng 804–809

  ```js
   804          <Text style={styles.label}>Họ Tên</Text>
   805          <TextInput
   806            style={styles.textInput}
   807            value={registerName}
   808            onChangeText={setRegisterName}
   809          />
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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
