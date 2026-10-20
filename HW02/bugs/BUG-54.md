# BUG-54

- **ID:** BUG-54
- **Tiêu đề:** App Mobile cho phép đăng ký Mật khẩu có ký tự đặc biệt nằm ngoài tập quy định (#), vẫn báo thành công và tạo tài khoản vào CSDL
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

- Web Admin đã đăng nhập bằng tài khoản `admin@eshop.com` và đang mở sẵn tab 'Quản lý Người dùng' để kiểm tra dữ liệu.

- File frontend-mobile/App.js dòng 16 đã được đặt API_URL trỏ tới IP LAN của máy chạy backend (ví dụ lượt 1 đặt [http://192.168.2.12:3000/api](http://192.168.2.12:3000/api) theo patch HW02/env/mobile_api_url.patch).

- App mobile được chạy bằng lệnh `npx expo start`, mở qua ứng dụng Expo Go trên điện thoại Android, kết nối cùng mạng với server và đang ở trạng thái ban đầu chưa đăng nhập.

## Các bước tái hiện

1. Ở màn hình chính của app mobile, bấm vào 'Đăng nhập' trên thanh header, rồi chọn 'Đăng ký ngay' để chuyển sang màn 'Đăng Ký Tài Khoản'.

2. Nhập Họ Tên hợp lệ (ví dụ: Nguyễn Văn Ánh).

3. Nhập Email hợp lệ chưa có trong hệ thống (ví dụ: m15_2231@domain.com).

4. Tại ô 'Mật khẩu', nhập chuỗi có ký tự đặc biệt nằm ngoài tập quy định (ví dụ: Abcd1234# – dùng ký tự # thay vì một trong các ký tự @, $, !, %, *, ?, &).

5. Bấm nút 'Đăng Ký'.

(Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1)

## Expected (trích SRS)

- Mật khẩu bắt buộc phải chứa ít nhất 1 ký tự đặc biệt thuộc tập đóng `@, $, !, %, *, ?, &` theo quy định FR-01.8 (D7).

- Ký tự `#` không nằm trong tập ký tự đặc biệt cho phép, do đó hệ thống phải tính là thiếu ký tự đặc biệt, chặn đăng ký và hiển thị thông báo lỗi ở ít nhất một kênh (chữ hiển thị trên màn hình, hộp thoại alert hoặc toast).

- Giao diện app phải giữ người dùng ở lại màn 'Đăng Ký Tài Khoản'.

- Hệ thống từ chối đăng ký, không tạo tài khoản mới trong CSDL (danh sách bên web admin giữ nguyên).

Trích SRS (AI chép nguyên văn): README.md dòng 34: "**Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`)."

## Actual

- Vừa bấm nút Đăng Ký xong thì app hiển thị ngay hộp thoại Dialog báo 'Đăng ký tài khoản thành công'.

- Hộp thoại hiện trên nền màn 'Đăng Nhập': app đã chuyển màn ngay khi hiện hộp thoại, trước khi đóng (ảnh `TC-FR20-15_manual_1.png`; App.js 233–236 gọi `Alert.alert` rồi `setView("login")` liền nhau).

- Kiểm tra danh sách bên trang web admin thì thấy xuất hiện thêm một dòng tài khoản mới mang email m15_{ts}@domain.com (ID 7, ảnh `D_admin_sau_1.png`); trang admin không hiển thị mật khẩu.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR20-15_manual_1.png`
- TC-FR20-15: `HW02/D_FR20/evidence/TC-FR20-15_manual_1.png`
- Ảnh admin cả lượt: `HW02/D_FR20/evidence/D_admin_truoc_1.png`, `HW02/D_FR20/evidence/D_admin_sau_1.png`, `HW02/D_FR20/evidence/D_admin_sau_2.png`

## TC liên quan

- Fail (1): TC-FR20-15
- Nhóm dữ kiện: G4 trong `HW02/bugs/_groups_D_FR20.md`

## Yêu cầu

- **FR-01.8:** Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &. [D2]
- **D7** (giả định, kế thừa A5 – ký tự đặc biệt): tập ĐÓNG — mật khẩu chỉ có ký tự đặc biệt ngoài tập bị coi là thiếu ký tự đặc biệt; ký tự ngoài tập được phép xuất hiện thêm nếu đã có ≥ 1 ký tự trong tập
- **D10** (giả định, oracle khi bị từ chối): oracle chính = không có tài khoản mới phía server (D11). Kèm theo: có thông báo lỗi trên app ở bất kỳ kênh nào (chữ trên màn hình, hộp thoại, toast) + vẫn ở màn 'Đăng Ký Tài Khoản'; nội dung chữ chỉ ghi Actual, không phân loại theo chữ của SUT
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Liên quan

- BUG cùng vị trí code server (A_FR01): BUG-07 (#23)
- Dòng code chung: `backend/server.js` dòng 20–29
- Dòng code mobile (riêng, không có ở BUG A): `frontend-mobile/App.js` dòng 211–212

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR20-15): `Sau khi ấn đăng ký, hiển thị Dialog thông báo đăng ký thành công, đồng thời chuyển sang giao diện login / xem ảnh TC-FR20-15_manual`
- Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend). Phần server AI chạy lại 21/10/2026 (7c, sau restart backend, giá trị theo bước SV): POST /api/register → HTTP 200 `User registered successfully`; GET /api/admin/users: id=8 email=[m15_2231@domain.com]. Bước trên thiết bị chưa chạy lại.
- Đoạn code trích nguyên văn: `frontend-mobile/App.js` dòng 209–219

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

- Nguyên nhân đầu tiên là do biểu thức chính quy strongPasswordRegex trong file App.js (dòng 211–212) được viết dạng mở [^A-Za-z\d]. Đoạn regex này chỉ kiểm tra xem chuỗi có tồn tại bất kỳ ký tự nào không phải là chữ cái và chữ số hay không, chứ không giới hạn đúng tập ký tự đặc biệt @, $, !, %, *, ?, & theo yêu cầu của SRS. Vì vậy ký tự # vẫn lọt qua bộ kiểm soát ở client.

- Nguyên nhân thứ hai là phía backend ở file server.js cũng hoàn toàn không validate độ mạnh hay tập ký tự của mật khẩu trước khi lưu vào CSDL, làm cho request chứa mật khẩu không hợp lệ vẫn được thực thi và tạo tài khoản thành công.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
