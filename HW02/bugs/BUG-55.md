# BUG-55

- **ID:** BUG-55
- **Tiêu đề:** Màn hình Đăng ký trên Mobile thiếu dấu sao * đánh dấu các trường nhập liệu bắt buộc
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã); thay đổi cục bộ duy nhất: `frontend-mobile/App.js` dòng 16 `API_URL = "http://192.168.2.12:3000/api"` (`HW02/env/mobile_api_url.patch`)
- Máy: Windows 11 Home Single Language 10.0.26200, backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Điện thoại: POCO F5 · OS 1.0.5.0.UMRTWXM · Android 14 (UKQ1.230804.001); Expo Go 54.0.8 (SDK 54); locale/bàn phím Tiếng Việt (Việt Nam) · QWERTY
- Mobile: màn 'Đăng Ký Tài Khoản' (frontend-mobile, Expo); điểm quan sát dữ liệu: web admin http://localhost:5174 → 'Quản lý Người dùng'
- Ngày chạy: 2026-10-21 (lượt chính thức = lượt 1, bắt đầu 00:15, Asia/Saigon; chạy tay)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/D_FR20/RUN.md`

## Tiền điều kiện

- Backend đã khởi động (`node server.js`).

- App mobile được chạy bằng lệnh `npx expo start`, mở qua ứng dụng Expo Go trên điện thoại Android, kết nối cùng mạng với server và đang ở trạng thái ban đầu chưa đăng nhập.

## Các bước tái hiện

1. Mở app mobile, bấm vào nút 'Đăng nhập' ở thanh header.

2. Chọn tiếp 'Đăng ký ngay' để chuyển sang giao diện màn hình 'Đăng Ký Tài Khoản'.

3. Quan sát nhãn (label) của các trường nhập liệu trên biểu mẫu đăng ký.

(Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1)

## Expected (trích SRS)

Tất cả các trường bắt buộc theo quy định FR-01 (gồm Họ Tên, Email, Mật khẩu) phải có ký hiệu dấu sao * hiển thị ngay bên cạnh nhãn theo yêu cầu FR-22.1 (D13).

Trích SRS (AI chép nguyên văn): README.md dòng 252: "Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn."

## Actual

Nhãn của cả ba trường nhập liệu chỉ hiển thị đơn thuần là 'Họ Tên', 'Email', 'Mật khẩu' mà không hề có ký hiệu dấu sao * bên cạnh để báo cho người dùng biết đây là các trường bắt buộc.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR20-90_manual_1.png`
- TC-FR20-90: `HW02/D_FR20/evidence/TC-FR20-90_manual_1.png`

## TC liên quan

- Fail (1): TC-FR20-90
- Nhóm dữ kiện: G5 trong `HW02/bugs/_groups_D_FR20.md`

## Yêu cầu

- **FR-22.1:** Trường bắt buộc có ký hiệu * bên cạnh nhãn. [phạm vi theo D13]
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR20-90): `Mỗi nhãn không có ký hiệu '*' bên cạnh / Xem hình TC-FR20-90-manual`
- Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại.
- Đoạn code trích nguyên văn: `frontend-mobile/App.js` dòng 804–818

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

### Nhận định

Lỗi giao diện này nằm trực tiếp trong file App.js tại các dòng 804, 810 và 817. Khi khai báo thẻ <Text style={styles.label}>, lập trình viên giao diện chỉ gõ chuỗi văn bản tĩnh lần lượt là Họ Tên, Email và Mật khẩu chứ không thêm ký tự * (hoặc <Text style="{styles.required}">*</Text>) ở phía sau nhãn để đáp ứng yêu cầu FR-22.1.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
