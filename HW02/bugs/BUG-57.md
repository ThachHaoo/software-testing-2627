# BUG-57

- **ID:** BUG-57
- **Tiêu đề:** Màn hình Đăng ký trên Mobile thiếu hẳn ô nhập 'Xác nhận mật khẩu' theo yêu cầu SRS
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

- Backend đã khởi động.

- App EShop trên điện thoại Android đã mở và đang ở trạng thái chưa đăng nhập.

## Các bước tái hiện

1. Mở app mobile, bấm vào nút 'Đăng nhập' ở thanh header.

2. Chọn 'Đăng ký ngay' để chuyển sang màn hình 'Đăng Ký Tài Khoản'.

3. Cuộn xem toàn bộ giao diện biểu mẫu đăng ký.

(Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1)

## Expected (trích SRS)

Giao diện đăng ký tài khoản phải bắt buộc có trường 'Xác nhận mật khẩu' để người dùng nhập lại mật khẩu, và hệ thống phải đối chiếu từ chối nếu hai mật khẩu không khớp theo quy định FR-01.9 (D9).

Trích SRS (AI chép nguyên văn): README.md dòng 35: "Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp."

## Actual

Màn hình 'Đăng Ký Tài Khoản' trên app mobile chỉ có vỏn vẹn 3 ô nhập liệu là 'Họ Tên', 'Email', và 'Mật khẩu', hoàn toàn không có ô 'Xác nhận mật khẩu'.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR20-94_manual_1.png`
- TC-FR20-94: `HW02/D_FR20/evidence/TC-FR20-94_manual_1.png`

## TC liên quan

- Fail (1): TC-FR20-94
- Blocked (2, case gốc TC-FR20-94): TC-FR20-16, TC-FR20-17
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_D_FR20.md`

## Yêu cầu

- **FR-01.9:** Phải có trường Xác nhận mật khẩu; hệ thống từ chối nếu Mật khẩu và Xác nhận mật khẩu không khớp. [D2]
- **D9** (giả định, kế thừa A7 + A17 – Xác nhận mật khẩu): so khớp tuyệt đối, phân biệt hoa/thường; bỏ trống = không khớp. Nếu màn hình không có ô này: 1 case kiểm sự tồn tại → Fail; case có V5 hợp lệ bỏ bước nhập V5 và ghi notes; các case V5 không hợp lệ → Blocked (case gốc = case kiểm sự tồn tại)
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR20-94): `Không có ô "Xác nhận mật khẩu" / xem hình TC-FR20-94_manual`
- Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại.
- Đoạn code trích nguyên văn: `frontend-mobile/App.js` dòng 797–837

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

### Nhận định

- Lỗi thiếu chức năng này thể hiện rất rõ trong hàm renderRegister ở file App.js (dòng 797–837). Trong cây component JSX render ra màn hình, lập trình viên hoàn toàn bỏ quên không khai báo thêm nhãn và ô <TextInput> cho trường 'Xác nhận mật khẩu'.

- Đồng thời, hàm xử lý handleRegister (dòng 209–240) cũng hoàn toàn không có state hay logic so sánh hai mật khẩu trước khi gửi request đăng ký. Việc thiếu mất ô nhập này khiến các test case kiểm tra nhập sai/khác xác nhận mật khẩu (như TC-FR20-16 và TC-FR20-17) không thể thực thi được và bị chặn (Blocked).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
