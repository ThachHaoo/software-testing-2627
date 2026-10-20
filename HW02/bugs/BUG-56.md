# BUG-56

- **ID:** BUG-56
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

- Ảnh tiêu biểu: `TC-FR20-91_manual_1.png`
- TC-FR20-91: `HW02/D_FR20/evidence/TC-FR20-91_manual_1.png`

## TC liên quan

- Fail (1): TC-FR20-91
- Nhóm dữ kiện: G6 trong `HW02/bugs/_groups_D_FR20.md`

## Yêu cầu

- **FR-22.2:** Trường Email phải dùng type="email" (mobile: cách hiểu theo D13). [D13]
- **D13** (giả định, yêu cầu GUI trên mobile): FR-22.1 ('*' cạnh nhãn), FR-22.4 (thông báo lỗi phía trên nút 'Đăng Ký') áp nguyên; FR-22.2/22.3 hiểu tương đương mobile: Email → bàn phím email (keyboardType email-address), Mật khẩu → che ký tự (secureTextEntry); kiểm ở TS-GUI, không phân lớp; FR-21 ngoài phạm vi
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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
