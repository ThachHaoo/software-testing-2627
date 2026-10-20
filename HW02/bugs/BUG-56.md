# BUG-56

- **ID:** BUG-56
- **Tiêu đề:** Ô nhập Email trên màn hình Đăng ký mobile không kích hoạt bàn phím định dạng Email (thiếu phím @)
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã); thay đổi cục bộ duy nhất: `frontend-mobile/App.js` dòng 16 `API_URL = "http://192.168.2.12:3000/api"` (`HW02/env/mobile_api_url.patch`)
- Máy: Windows 11 Home Single Language 10.0.26200, backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Điện thoại: POCO F5 · OS 1.0.5.0.UMRTWXM · Android 14 (UKQ1.230804.001); Expo Go 54.0.8 (SDK 54); locale/bàn phím Tiếng Việt (Việt Nam) · QWERTY
- Mobile: màn 'Đăng Ký Tài Khoản' (frontend-mobile, Expo); điểm quan sát dữ liệu: web admin http://localhost:5174 → 'Quản lý Người dùng'
- Ngày chạy: 2026-10-21 (lượt chính thức = lượt 1, bắt đầu 00:15, Asia/Saigon; chạy tay)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/D_FR20/RUN.md`

## Tiền điều kiện

- Backend đã khởi động (`node server.js`).

- File frontend-mobile/App.js dòng 16 đã được đặt API_URL trỏ tới IP LAN của máy chạy backend (ví dụ lượt 1 đặt [http://192.168.2.12:3000/api](http://192.168.2.12:3000/api) theo patch HW02/env/mobile_api_url.patch).

- App mobile được chạy bằng lệnh `npx expo start`, mở qua ứng dụng Expo Go trên điện thoại Android, kết nối cùng mạng với server và đang ở trạng thái ban đầu chưa đăng nhập.

## Các bước tái hiện

1. Trên app mobile, bấm vào 'Đăng nhập' ở thanh header.

2. Chọn 'Đăng ký ngay' để chuyển sang màn hình 'Đăng Ký Tài Khoản'.

3. Chạm tay vào ô nhập liệu 'Email' để gọi bàn phím ảo hiển thị.

(Bước trên thiết bị: AI chưa chạy lại; đã đối chiếu code App.js + evidence lượt 1)

## Expected (trích SRS)

Ô nhập Email phải mở bàn phím ảo được tối ưu riêng cho việc gõ email (chứa sẵn phím `@` ngay trên bàn phím chính) theo tương đương yêu cầu FR-22.2 (với thuộc tính `keyboardType="email-address"`).

Trích SRS (AI chép nguyên văn): README.md dòng 253: "Trường Email phải dùng `type="email"`."

## Actual

Bàn phím ảo bật lên chỉ là bàn phím văn bản thông thường (text/standard keyboard), hoàn toàn không xuất hiện phím @ ở giao diện bàn phím chính. Người dùng phải bấm chuyển sang trang ký tự đặc biệt mới gõ được dấu @.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR20-91_manual_1.png`
- TC-FR20-91: `HW02/D_FR20/evidence/TC-FR20-91_manual_1.png`

## TC liên quan

- Fail (1): TC-FR20-91
- Nhóm dữ kiện: G6 trong `HW02/bugs/_groups_D_FR20.md`

## Yêu cầu

- **FR-22.2:** Trường Email phải dùng `type="email"` (trên mobile theo D13: bàn phím email `keyboardType="email-address"`).
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR20-91): `Bàn phím hiện ra, nhưng không phải là bàn phím Email (không có phím '@') / xem hình TC-FR20-91_manual`
- Lặp lại: 1 lượt chính thức (lượt 1, sau restart backend); chưa chạy lại.
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

### Nhận định

Lỗi này nằm ở thẻ <TextInput> của ô Email trong file App.js (dòng 811–816). Lập trình viên chỉ mới thiết lập thuộc tính autoCapitalize="none" để tắt tự động viết hoa, nhưng lại bỏ quên việc khai báo thuộc tính keyboardType="email-address". Do đó hệ thống Android không thể nhận biết đây là ô gõ email để kích hoạt bố cục bàn phím phù hợp cho trải nghiệm người dùng.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
