# D_FR20 – Test case sinh viên bổ sung (bước 5)

- Feature: D_FR20 – Đăng ký trên Mobile (FR-20 áp FR-01).
- Mã: TS-SV, bắt đầu từ `TC-FR20-200`, đánh số liên tục; bỏ case thì giữ khoảng trống số (không đánh lại).
- Một case chỉ thuộc một tầng (Mobile / GUI).
- Cách ghi giá trị nhập: `''` = để trống; `␣` = đúng một dấu cách (ghi đủ số ␣).
- Mã EC, biến, giả định: tra ở `testcases.md`.
- Expected phải có căn cứ: SRS hoặc giả định SV đã chốt. Giả định mới → mã D16, D17…, ghi "SV chốt + lý do".
- Kỹ thuật: EP / BVA / EG / ST…; Approach: black-box / gray-box (gray-box khi chọn từ mã nguồn).

## Tầng Mobile

| #TC | Tiêu đề | Kỹ thuật | Approach | EC phủ | EC mục tiêu | Họ Tên | Email | Email trong CSDL | Mật khẩu | Xác nhận mật khẩu | Expected | Căn cứ | Lý do chọn input |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-FR20-200 | Kiểm tra dán (paste) chuỗi XSS `<script>alert(1)</script>` từ Clipboard vào ô Họ Tên bằng menu ngữ cảnh mobile | Security / Input Handling | gray-box | EC1, EC3, EC6, EC8 | EC1 | `<script>alert(1)</script>` | m200_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Đăng ký thành công; app không bị giật/văng; trang Admin hiển thị nguyên văn chuỗi dạng chữ, không thực thi script. | FR-01.1, D3 | Security: Kiểm tra việc dán mã script từ bộ nhớ tạm mobile xem React Native TextInput render và lưu trữ an toàn hay không. |
| TC-FR20-201 | Kiểm tra dán chuỗi Unicode Emoji 🐻 vào ô Họ Tên qua bàn phím di động | Unicode / Encoding | black-box | EC1, EC3, EC6, EC8 | EC1 | `Lê 🐻 Hiệp ` | m201_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Đăng ký thành công; CSDL và trang Admin lưu đúng ký tự Emoji 4-byte UTF-8, không bị lỗi font/dấu '?' hoặc rách icon. | FR-01.1, D3 | Mobile Keyboard: Bàn phím di động thường xuyên gõ emoji. Kiểm tra xem chuỗi Emoji 4-byte UTF-8 có bị lỗi mã hóa CSDL không. |
| TC-FR20-202 | Kiểm tra nhập chuỗi Mật khẩu có ký tự xuống dòng `\n` bằng cách dán từ ứng dụng Ghi chú (Notes) | Injection / Format | gray-box | EC1, EC3, EC6, EC8 | EC8 | Nguyễn Văn Ánh | m202_{ts}@domain.com | chưa có | `Abcd123\n4!` | `Abcd123\n4!` | App hiển thị thông báo lỗi Mật khẩu không hợp lệ và giữ nguyên người dùng ở màn hình Đăng ký; không tạo tài khoản mới. | FR-01.8, D8 | Input Parsing: Dán mật khẩu có chứa ký tự xuống dòng `\n` từ ứng dụng khác dễ làm gãy chuỗi JSON.stringify khi gửi request. |
| TC-FR20-203 | Kiểm tra bấm chạm liên tục 10 lần nút 'Đăng Ký' khi form hợp lệ (Spam Touch / Double Tap) | Concurrency / Double Tap | gray-box | EC1, EC3, EC6, EC8 | EC1, D11 | Nguyễn Văn Ánh | m203_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Nút 'Đăng Ký' bị vô hiệu hóa trong lúc chờ phản hồi; chỉ tạo duy nhất 1 tài khoản trong CSDL, không tạo trùng lặp. | FR-20.1, D11 | UX Mobile: Người dùng mạng chậm/lag thường bấm chạm nút 'Đăng Ký' liên tục nhiều lần. |
| TC-FR20-204 | Kiểm tra tính năng Bàn phím tự động gợi ý / Tự viết hoa (Auto-correct / Auto-capitalize) tự chèn khoảng trắng ở ô Email | Mobile Keyboard Behavior | gray-box | EC1, EC5, EC6, EC8 | EC5 | Nguyễn Văn Ánh | `m205_{ts} @domain.com` | chưa có | Abcd1234! | Abcd1234! | App hiển thị thông báo lỗi Email không hợp lệ và không gửi request tạo tài khoản. | FR-01.3, D4 | Mobile Keyboard: Tính năng Auto-correct trên Gboard/iOS Keyboard rất hay tự động chèn khoảng trắng sau dấu `@` hoặc dấu `.`. |
| TC-FR20-205 | Kiểm tra nhập Mật khẩu chứa chuỗi số Full-width `１２３４５６78` bằng bộ gõ tiếng Trung/Nhật | Unicode / Type Confusion | black-box | EC1, EC3, EC6, EC8 | EC18 | Nguyễn Văn Ánh | m206_{ts}@domain.com | chưa có | `Abcd１２３4!` | `Abcd１２３4!` | App báo lỗi Mật khẩu thiếu chữ số (chuỗi `１２３` Full-width U+FF11 không phải là chữ số ASCII 0–9). | FR-01.7c, D8 | Mobile Keyboard: Bộ gõ CJK trên mobile sinh ra ký tự Full-width nhìn giống số nhưng không thuộc tập ASCII `[0-9]`. |
| TC-FR20-206 | Kiểm tra nhập Họ Tên có độ dài cực lớn (10.000 ký tự) bằng cách dán chuỗi từ bộ nhớ tạm | Boundary / Overflow | gray-box | EC1, EC3, EC6, EC8 | EC1 | 10.000 chữ 'a' | m207_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | App xử lý mượt mà không bị đơ UI; gửi request thành công, chuyển sang màn hình Đăng nhập và tạo đúng 1 tài khoản mới trong CSDL. | FR-01.1, D3 | Boundary/Performance: Dán chuỗi cực đại vào TextInput trên React Native dễ làm đơ luồng JS Thread (Main Thread) của app mobile. |

## GUI

| #TC | Tiêu đề | Kỹ thuật | Approach | Yêu cầu | Các bước | Expected | Căn cứ | Lý do chọn input |
|---|---|---|---|---|---|---|---|---|
| TC-FR20-207 | Kiểm tra bàn phím tự động che khuất (Keyboard Obscure) ô Mật khẩu và nút 'Đăng Ký' khi hiện bàn phím | GUI / Mobile Usability | black-box | FR-22.4 | 1. Mở màn Đăng ký.<br>2. Chạm vào ô Mật khẩu để mở bàn phím ảo.<br>3. Quan sát vị trí ô Mật khẩu và nút 'Đăng Ký'. | Ô Mật khẩu và nút 'Đăng Ký' tự động cuộn lên (dùng KeyboardAvoidingView), không bị bàn phím ảo che khuất hoàn toàn. | FR-22.4, D13 | UX Mobile: Bàn phím ảo chiếm 1/2 màn hình mobile dễ che mất các ô phía dưới nếu không dùng KeyboardAvoidingView. |
| TC-FR20-208 | Kiểm tra sự tồn tại và hoạt động của nút 'Mắt' (Show/Hide Password) ở ô Mật khẩu | GUI / Mobile Feature | black-box | FR-22.3 | 1. Nhập 'Abcd1234!' vào ô Mật khẩu.<br>2. Bấm vào biểu tượng 'Mắt' bên phải ô Mật khẩu. | Ký tự mật khẩu chuyển từ dạng che (`••••••••`) sang dạng văn bản đọc được (`Abcd1234!`); bấm lại chuyển về dạng che. | FR-22.3, D13 | Mobile Usability: Trên bàn phím nhỏ di động, nút xem/ẩn mật khẩu giúp người dùng tránh gõ sai mật khẩu. |

## Giả định mới (nếu có)

- <mã D16…> (<chủ đề>) [loại: <loại> · truy vết: <có/không> · căn cứ: <căn cứ> · SV chốt <ngày> — <lý do>]: <nội dung>
