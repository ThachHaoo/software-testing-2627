<!-- Bản 10.3 cũ của report (em đánh giá từng TC), chuyển nguyên văn từ HW02/23120255_HW02_Report.md ngày 21/10/2026 khi 10.3 đổi sang bảng theo suite (V1, V2). -->

### 10.3 Đánh giá từng TC do AI sinh 🔒

| TC | Suite | Nguồn | Trạng thái sửa (so bản AI đóng băng cuối chứa TC; git) | Verdict |
|---|---|---|---|---|
| TC-FR01-01 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản chuẩn: Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu đều hợp lệ) |
| TC-FR01-02 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản hợp lệ: Họ Tên có dấu tiếng Việt + Mật khẩu chứa ký tự ngoài tập ASCII) |
| TC-FR01-03 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Email có chứa khoảng trắng ở đầu hoặc cuối chuỗi) |
| TC-FR01-04 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Email chỉ khác chữ hoa/chữ thường, ví dụ `Test@eshop.com`) |
| TC-FR01-05 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản để trống trường Họ Tên) |
| TC-FR01-06 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản để trống trường Mật khẩu) |
| TC-FR01-07 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản để trống trường Xác nhận mật khẩu) |
| TC-FR01-08 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản để trống trường Email) |
| TC-FR01-09 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản nhập Email sai định dạng không chứa ký tự `@`) |
| TC-FR01-10 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản nhập Email sai định dạng thiếu tên miền domain) |
| TC-FR01-11 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Mật khẩu quá ngắn dưới 6 ký tự) |
| TC-FR01-12 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Mật khẩu và Xác nhận mật khẩu không khớp nhau) |
| TC-FR01-13 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Mật khẩu chỉ toàn ký tự số) |
| TC-FR01-14 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Mật khẩu chỉ toàn ký tự chữ cái) |
| TC-FR01-15 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Mật khẩu có chứa khoảng trắng) |
| TC-FR01-16 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Họ Tên chứa chữ số) |
| TC-FR01-17 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Họ Tên chứa ký tự đặc biệt) |
| TC-FR01-18 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản để trống tất cả các trường dữ liệu) |
| TC-FR01-19 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Họ Tên có độ dài đạt ngưỡng tối đa) |
| TC-FR01-20 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Họ Tên vượt quá độ dài tối đa) |
| TC-FR01-21 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Mật khẩu vượt quá độ dài tối đa) |
| TC-FR01-22 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản nhập Email có khoảng trắng ở giữa local-part) |
| TC-FR01-23 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản nhập Email đã tồn tại sẵn trong hệ thống) |
| TC-FR01-24 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Họ Tên chỉ chứa khoảng trắng) |
| TC-FR01-25 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Mật khẩu chứa ký tự Unicode) |
| TC-FR01-26 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Email có sub-domain mở rộng) |
| TC-FR01-27 | TS-DOM-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kịch bản Email có TLD độ dài lớn) |
| TC-FR01-28 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API payload hợp lệ đủ các field) |
| TC-FR01-29 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API payload thiếu trường email) |
| TC-FR01-30 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API payload thiếu trường password) |
| TC-FR01-31 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API payload thiếu trường name) |
| TC-FR01-32 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API trùng lặp email đã đăng ký) |
| TC-FR01-33 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API email không đúng định dạng) |
| TC-FR01-34 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API password ngắn dưới 6 ký tự) |
| TC-FR01-35 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API payload chứa thêm trường không xác định) |
| TC-FR01-36 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API name chứa mã HTML / Script) |
| TC-FR01-37 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API body rỗng `{}`) |
| TC-FR01-38 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API Header Content-Type sai định dạng) |
| TC-FR01-39 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API email vượt quá 255 ký tự) |
| TC-FR01-40 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API name là chuỗi rỗng `""`) |
| TC-FR01-41 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API password là chuỗi rỗng `""`) |
| TC-FR01-42 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API email truyền giá trị `null`) |
| TC-FR01-43 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API password truyền giá trị `null`) |
| TC-FR01-44 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API name truyền kiểu dữ liệu number) |
| TC-FR01-45 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API password truyền kiểu dữ liệu boolean) |
| TC-FR01-46 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API kiểm tra việc băm mật khẩu trong DB) |
| TC-FR01-47 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API trả về dữ liệu user sau khi tạo) |
| TC-FR01-48 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API xử lý trim khoảng trắng ở hai đầu name) |
| TC-FR01-49 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API xử lý lowercase trường email) |
| TC-FR01-50 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API chống SQL Injection trong field name) |
| TC-FR01-51 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API chống XSS Payload trong field name) |
| TC-FR01-52 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API xử lý kịch bản gửi JSON lỗi cú pháp) |
| TC-FR01-53 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API name vượt quá 255 ký tự) |
| TC-FR01-54 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API password chứa ký tự null byte) |
| TC-FR01-55 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API kiểm tra giới hạn tần suất gửi request rate limit) |
| TC-FR01-56 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API gán quyền mặc định cho tài khoản đăng ký) |
| TC-FR01-57 | TS-DOM-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API từ chối cấp quyền admin qua payload đăng ký) |
| TC-FR01-60 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Mật khẩu độ dài 5 ký tự - On-bound không hợp lệ) |
| TC-FR01-61 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Mật khẩu độ dài 6 ký tự - Biên hợp lệ tối thiểu) |
| TC-FR01-62 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Mật khẩu độ dài 7 ký tự - Off-bound hợp lệ) |
| TC-FR01-63 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Email local-part có độ dài 1 ký tự) |
| TC-FR01-64 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Email local-part có độ dài 64 ký tự - Cận trên) |
| TC-FR01-65 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Email local-part vượt quá 64 ký tự) |
| TC-FR01-66 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Họ Tên độ dài 1 ký tự - Cận dưới hợp lệ) |
| TC-FR01-67 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Họ Tên độ dài 2 ký tự) |
| TC-FR01-68 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Họ Tên độ dài 254 ký tự) |
| TC-FR01-69 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Họ Tên độ dài 255 ký tự - Cận trên) |
| TC-FR01-70 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Họ Tên độ dài 256 ký tự - Vượt cận trên) |
| TC-FR01-71 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Mật khẩu độ dài 254 ký tự) |
| TC-FR01-72 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Mật khẩu độ dài 255 ký tự - Cận trên) |
| TC-FR01-73 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Mật khẩu độ dài 256 ký tự - Vượt cận trên) |
| TC-FR01-74 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Tên miền Email độ dài 253 ký tự - Cận trên) |
| TC-FR01-75 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA Tên miền Email vượt quá 253 ký tự) |
| TC-FR01-76 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA TLD Email 2 ký tự, ví dụ `.vn`) |
| TC-FR01-77 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA TLD Email 63 ký tự - Cận trên TLD) |
| TC-FR01-78 | TS-BVA-UI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (BVA TLD Email vượt quá 63 ký tự) |
| TC-FR01-79 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Password độ dài 5 ký tự) |
| TC-FR01-80 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Password độ dài 6 ký tự) |
| TC-FR01-81 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Password độ dài 7 ký tự) |
| TC-FR01-82 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Name 1 ký tự) |
| TC-FR01-83 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Name 255 ký tự) |
| TC-FR01-84 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Name 256 ký tự) |
| TC-FR01-85 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Password 255 ký tự) |
| TC-FR01-86 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Email tổng độ dài 254 ký tự) |
| TC-FR01-87 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Email tổng độ dài 255 ký tự) |
| TC-FR01-88 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Email tổng độ dài 256 ký tự) |
| TC-FR01-89 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Password 0 ký tự - chuỗi rỗng) |
| TC-FR01-100 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Email 0 ký tự - chuỗi rỗng) |
| TC-FR01-101 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Name 0 ký tự - chuỗi rỗng) |
| TC-FR01-102 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Password 256 ký tự) |
| TC-FR01-103 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Name local-part 1 ký tự) |
| TC-FR01-104 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Name local-part 64 ký tự) |
| TC-FR01-105 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Name local-part 65 ký tự) |
| TC-FR01-106 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Domain name 253 ký tự) |
| TC-FR01-107 | TS-BVA-API | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (API BVA Domain name 254 ký tự) |
| TC-FR01-90 | TS-GUI | Both | khác bản AI `A_FR01_step4_20261019-1719.json` ở expected_result, rationale, steps; commit đầu tiên khác: `6a5a17e` | MODIFIED_BY_SV (SV sửa expected & steps để cô lập nguyên nhân SUT thiếu ô Confirm Password) |
| TC-FR01-91 | TS-GUI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kiểm thử phản hồi giao diện khi bấm phím Enter gửi form) |
| TC-FR01-92 | TS-GUI | Both | khác bản AI `A_FR01_step4_20261019-1719.json` ở title, expected_result, rationale, steps; commit đầu tiên khác: `6a5a17e` | MODIFIED_BY_SV (SV sửa title & rationale do giao diện SUT thực tế không có ô Confirm Password) |
| TC-FR01-93 | TS-GUI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kiểm thử ẩn/hiện mật khẩu qua nút con mắt trên UI) |
| TC-FR01-94 | TS-GUI | AI | giữ nguyên bản AI `A_FR01_step4_20261019-1719.json` | VALID (Kiểm thử liên kết chuyển hướng sang trang Đăng nhập) |
| TC-FR01-219 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV thêm kịch bản kiểm tra đăng ký tài khoản với email chứa dấu cộng `+test`) |
| TC-FR01-223 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV bổ sung kịch bản kiểm thử thao tác Dán/Paste Mật khẩu vào form) |
| TC-FR01-224 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV bổ sung kịch bản kiểm thử tính năng Tự động điền Autofill của trình duyệt) |
| TC-FR01-225 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV bổ sung kịch bản kiểm tra tự động trim khoảng trắng ở Email) |
| TC-FR01-226 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV bổ sung kịch bản kiểm tra vô hiệu hóa nút Submit khi đang gửi dữ liệu) |
| TC-FR01-227 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV bổ sung kịch bản kiểm thử nhập chuỗi XSS ở trường Họ Tên) |
| TC-FR01-228 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV bổ sung kịch bản kiểm tra dữ liệu ô nhập khi reload trang) |
| TC-FR01-231 | TS-SV | Both | không có trong bản AI đóng băng | ADDED_BY_SV (SV bổ sung kịch bản kiểm tra hiển thị thông báo lỗi giao diện) |
| TC-FR07-01 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Thêm sản phẩm hợp lệ vào giỏ hàng thành công) |
| TC-FR07-02 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Tăng số lượng sản phẩm trong giỏ hàng) |
| TC-FR07-03 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Giảm số lượng sản phẩm trong giỏ hàng) |
| TC-FR07-04 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Xóa một sản phẩm ra khỏi giỏ hàng) |
| TC-FR07-05 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Xóa toàn bộ sản phẩm khỏi giỏ hàng) |
| TC-FR07-06 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Nhập trực tiếp số lượng 0 vào ô nhập) |
| TC-FR07-07 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Nhập số lượng âm vào giỏ hàng) |
| TC-FR07-08 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Nhập số lượng vượt quá tồn kho khả dụng) |
| TC-FR07-09 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Tính tổng tiền giỏ hàng khi có nhiều mặt hàng) |
| TC-FR07-10 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Lưu giữ trạng thái giỏ hàng sau khi tải lại trang F5) |
| TC-FR07-11 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Thêm sản phẩm đã hết hàng vào giỏ) |
| TC-FR07-12 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Thao tác giỏ hàng khi người dùng chưa đăng nhập) |
| TC-FR07-13 | TS-DOM-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Đồng bộ giỏ hàng từ khách sang tài khoản sau khi đăng nhập) |
| TC-FR07-20 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API thêm sản phẩm vào giỏ hàng với payload hợp lệ) |
| TC-FR07-21 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API cập nhật số lượng sản phẩm trong giỏ) |
| TC-FR07-22 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API xóa item khỏi giỏ hàng) |
| TC-FR07-30 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API thêm productId không tồn tại trong CSDL) |
| TC-FR07-31 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API truyền quantity = 0 khi thêm giỏ hàng) |
| TC-FR07-32 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API truyền quantity số âm) |
| TC-FR07-33 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API truyền quantity dạng chuỗi ký tự) |
| TC-FR07-34 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API truyền quantity vượt quá số lượng kho) |
| TC-FR07-35 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API thiếu trường productId trong body) |
| TC-FR07-36 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API thiếu trường quantity trong body) |
| TC-FR07-37 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API lấy danh sách giỏ hàng chi tiết) |
| TC-FR07-38 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API xóa sạch toàn bộ giỏ hàng) |
| TC-FR07-39 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API với token xác thực hết hạn) |
| TC-FR07-40 | TS-DOM-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API truy cập giỏ hàng của người dùng khác) |
| TC-FR07-60 | TS-BVA-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (BVA Số lượng bằng 1 - Biên dưới hợp lệ) |
| TC-FR07-61 | TS-BVA-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (BVA Số lượng bằng 0 - Điểm biên không hợp lệ) |
| TC-FR07-62 | TS-BVA-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (BVA Số lượng bằng tồn kho khả dụng) |
| TC-FR07-63 | TS-BVA-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (BVA Số lượng bằng tồn kho + 1) |
| TC-FR07-64 | TS-BVA-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (BVA Số lượng bằng giới hạn hệ thống 99999) |
| TC-FR07-65 | TS-BVA-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (BVA Số lượng vượt quá 99999) |
| TC-FR07-66 | TS-BVA-UI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (BVA Số lượng bằng 2 - Off-bound hợp lệ) |
| TC-FR07-70 | TS-BVA-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API BVA quantity = 1) |
| TC-FR07-71 | TS-BVA-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API BVA quantity = 0) |
| TC-FR07-72 | TS-BVA-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API BVA quantity = số lượng tồn kho) |
| TC-FR07-73 | TS-BVA-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API BVA quantity = số lượng tồn kho + 1) |
| TC-FR07-74 | TS-BVA-API | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (API BVA quantity = -1) |
| TC-FR07-90 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Hiển thị biểu tượng số lượng sản phẩm trên giỏ hàng) |
| TC-FR07-91 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Giao diện hiển thị trạng thái giỏ hàng rỗng) |
| TC-FR07-92 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Nút chuyển sang trang Thanh toán) |
| TC-FR07-93 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Hộp thoại xác nhận khi chọn xóa sản phẩm) |
| TC-FR07-94 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Định dạng tiền tệ VNĐ trên giao diện) |
| TC-FR07-95 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Giao diện giỏ hàng trên trình duyệt di động) |
| TC-FR07-96 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Hiệu ứng khi đang cập nhật số lượng) |
| TC-FR07-97 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Thông báo thành công khi thêm vào giỏ) |
| TC-FR07-98 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Trạng thái nút tăng khi đạt giới hạn tồn kho) |
| TC-FR07-99 | TS-GUI | AI | giữ nguyên bản AI `B_FR07_step4_20261020-111050.json` | VALID (Trạng thái nút giảm khi số lượng đang là 1) |
| TC-FR15-01 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Tạo mới sản phẩm với các thông tin hợp lệ) |
| TC-FR15-02 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Cập nhật Tên và Giá sản phẩm) |
| TC-FR15-03 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Xóa một sản phẩm đang có) |
| TC-FR15-04 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Để trống tên sản phẩm khi thêm mới) |
| TC-FR15-05 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Nhập giá sản phẩm bằng 0) |
| TC-FR15-06 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Nhập giá sản phẩm là số âm) |
| TC-FR15-07 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Nhập số lượng tồn kho là số âm) |
| TC-FR15-08 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Bỏ qua chọn Danh mục sản phẩm) |
| TC-FR15-09 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Tải lên ảnh sai định dạng tệp) |
| TC-FR15-10 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Tải lên tệp ảnh vượt dung lượng tối đa) |
| TC-FR15-11 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Tìm kiếm sản phẩm theo tên) |
| TC-FR15-12 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Lọc danh sách sản phẩm theo Danh mục) |
| TC-FR15-13 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Phân trang danh sách sản phẩm) |
| TC-FR15-14 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Nhập tên sản phẩm bị trùng lặp) |
| TC-FR15-15 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Nhập giá sản phẩm bằng chữ) |
| TC-FR15-16 | TS-DOM-UI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Đóng cửa sổ thêm mới mà không lưu) |
| TC-FR15-17 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST tạo sản phẩm hợp lệ) |
| TC-FR15-18 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST thiếu trường name) |
| TC-FR15-23 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST thiếu trường price) |
| TC-FR15-24 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST thiếu trường categoryId) |
| TC-FR15-25 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST price là số âm) |
| TC-FR15-26 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST stockQuantity là số âm) |
| TC-FR15-27 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST categoryId không tồn tại) |
| TC-FR15-28 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST gửi từ tài khoản không phải Admin) |
| TC-FR15-29 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST không có token xác thực) |
| TC-FR15-30 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST price là số thực thập phân) |
| TC-FR15-31 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST description nhận giá trị null) |
| TC-FR15-32 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST name trùng tên sản phẩm có sẵn) |
| TC-FR15-33 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST định dạng đường dẫn ảnh không hợp lệ) |
| TC-FR15-34 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST chứa thẻ HTML trong description) |
| TC-FR15-50 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST stockQuantity không phải số nguyên) |
| TC-FR15-51 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST price chứa ký hiệu tiền tệ) |
| TC-FR15-52 | TS-DOM-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API POST gán trạng thái hiển thị mặc định) |
| TC-FR15-19 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT cập nhật sản phẩm hợp lệ) |
| TC-FR15-20 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT ID sản phẩm không tồn tại) |
| TC-FR15-35 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT price là số âm) |
| TC-FR15-36 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT stockQuantity là số âm) |
| TC-FR15-37 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT chỉ cập nhật mô tả sản phẩm) |
| TC-FR15-38 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT chỉ cập nhật giá sản phẩm) |
| TC-FR15-39 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT thay đổi danh mục sản phẩm) |
| TC-FR15-40 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT đổi tên trùng với sản phẩm khác) |
| TC-FR15-41 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT gửi từ người dùng không phải Admin) |
| TC-FR15-42 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT ID sai định dạng) |
| TC-FR15-43 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT chuyển trạng thái ẩn sản phẩm) |
| TC-FR15-44 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT giữ nguyên thông tin các trường không truyền) |
| TC-FR15-45 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT body rỗng `{}`) |
| TC-FR15-46 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT gửi nhiều cập nhật đồng thời) |
| TC-FR15-48 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT cập nhật đường dẫn ảnh mới) |
| TC-FR15-53 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT categoryId không tồn tại trong hệ thống) |
| TC-FR15-54 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT price bằng 0) |
| TC-FR15-55 | TS-DOM-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API PUT name là chuỗi rỗng) |
| TC-FR15-21 | TS-DOM-API-OTHER | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API DELETE xóa sản phẩm) |
| TC-FR15-22 | TS-DOM-API-OTHER | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API DELETE sản phẩm đang gắn liền với đơn hàng) |
| TC-FR15-47 | TS-DOM-API-OTHER | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API GET lấy thông tin chi tiết một sản phẩm) |
| TC-FR15-49 | TS-DOM-API-OTHER | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API DELETE ID sản phẩm không tồn tại) |
| TC-FR15-56 | TS-DOM-API-OTHER | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API GET danh sách sản phẩm có tham số phân trang) |
| TC-FR15-57 | TS-DOM-API-OTHER | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API GET danh sách có tham số từ khóa tìm kiếm) |
| TC-FR15-58 | TS-DOM-API-OTHER | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API DELETE gửi từ tài khoản không phải Admin) |
| TC-FR15-60 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Tên sản phẩm 1 ký tự) |
| TC-FR15-61 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Tên sản phẩm 255 ký tự) |
| TC-FR15-62 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Tên sản phẩm 256 ký tự) |
| TC-FR15-63 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Giá sản phẩm 1 VNĐ) |
| TC-FR15-64 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Giá sản phẩm 0 VNĐ) |
| TC-FR15-65 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Giá sản phẩm 1.000.000.000 VNĐ) |
| TC-FR15-66 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Giá sản phẩm vượt 1 tỷ VNĐ) |
| TC-FR15-67 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Số lượng tồn kho bằng 0) |
| TC-FR15-68 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Số lượng tồn kho bằng 1) |
| TC-FR15-69 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Số lượng tồn kho bằng -1) |
| TC-FR15-70 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Số lượng tồn kho 999999) |
| TC-FR15-71 | TS-BVA-UI-THEM | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Thêm mới: Số lượng tồn kho 1000000) |
| TC-FR15-72 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Tên sản phẩm 1 ký tự) |
| TC-FR15-73 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Tên sản phẩm 255 ký tự) |
| TC-FR15-74 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Tên sản phẩm 256 ký tự) |
| TC-FR15-75 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Giá sản phẩm 1 VNĐ) |
| TC-FR15-76 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Giá sản phẩm 0 VNĐ) |
| TC-FR15-77 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Giá sản phẩm 1.000.000.000 VNĐ) |
| TC-FR15-78 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Giá sản phẩm vượt 1 tỷ VNĐ) |
| TC-FR15-79 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Số lượng tồn kho bằng 0) |
| TC-FR15-80 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Số lượng tồn kho bằng 1) |
| TC-FR15-81 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Số lượng tồn kho bằng -1) |
| TC-FR15-82 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Số lượng tồn kho 999999) |
| TC-FR15-83 | TS-BVA-UI-SUA | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (BVA Chỉnh sửa: Số lượng tồn kho 1000000) |
| TC-FR15-84 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Price = 0.01) |
| TC-FR15-85 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Price = 0.00) |
| TC-FR15-86 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Price = -0.01) |
| TC-FR15-87 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Stock = 0) |
| TC-FR15-88 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Stock = -1) |
| TC-FR15-89 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Tên độ dài 1 ký tự) |
| TC-FR15-100 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Tên độ dài 255 ký tự) |
| TC-FR15-101 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Tên độ dài 256 ký tự) |
| TC-FR15-102 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Mô tả độ dài 1000 ký tự) |
| TC-FR15-103 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Mô tả độ dài 1001 ký tự) |
| TC-FR15-104 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Price = 999999999.99) |
| TC-FR15-105 | TS-BVA-API-POST | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA POST: Price = 1000000000.00) |
| TC-FR15-106 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Price = 0.01) |
| TC-FR15-107 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Price = 0.00) |
| TC-FR15-108 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Price = -0.01) |
| TC-FR15-109 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Stock = 0) |
| TC-FR15-110 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Stock = -1) |
| TC-FR15-111 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Tên độ dài 1 ký tự) |
| TC-FR15-112 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Tên độ dài 255 ký tự) |
| TC-FR15-113 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Tên độ dài 256 ký tự) |
| TC-FR15-114 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Mô tả độ dài 1000 ký tự) |
| TC-FR15-115 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Mô tả độ dài 1001 ký tự) |
| TC-FR15-116 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Price = 999999999.99) |
| TC-FR15-117 | TS-BVA-API-PUT | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (API BVA PUT: Price = 1000000000.00) |
| TC-FR15-90 | TS-GUI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Hiển thị bảng danh sách sản phẩm) |
| TC-FR15-91 | TS-GUI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Nút chỉnh sửa sản phẩm trên giao diện) |
| TC-FR15-92 | TS-GUI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Hộp thoại xác nhận khi chọn xóa) |
| TC-FR15-93 | TS-GUI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Xem trước hình ảnh sản phẩm) |
| TC-FR15-94 | TS-GUI | AI | giữ nguyên bản AI `C_FR15_step4_20261020-165850.json` | VALID (Thông báo thành công khi cập nhật sản phẩm) |
| TC-FR20-01 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Đăng ký tài khoản mới hợp lệ trên app) |
| TC-FR20-02 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Nhập Email sai định dạng) |
| TC-FR20-03 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Đăng ký với Email đã tồn tại) |
| TC-FR20-04 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Mật khẩu dưới 6 ký tự) |
| TC-FR20-05 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Để trống trường Họ Tên) |
| TC-FR20-06 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Để trống trường Email) |
| TC-FR20-07 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Để trống trường Mật khẩu) |
| TC-FR20-08 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Nhập Email chứa ký tự khoảng trắng) |
| TC-FR20-09 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Mật khẩu không chứa chữ số) |
| TC-FR20-10 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Thao tác đăng ký khi thiết bị mất kết nối mạng) |
| TC-FR20-11 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Nhấn nút Đăng ký liên tục nhiều lần) |
| TC-FR20-12 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Nhập Họ Tên có chứa biểu tượng Emoji) |
| TC-FR20-13 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Thao tác Dán/Paste dữ liệu vào ô Mật khẩu) |
| TC-FR20-14 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Nút ẩn/hiện mật khẩu trên màn hình ứng dụng) |
| TC-FR20-15 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Bàn phím ảo che khuất nút thao tác Submit) |
| TC-FR20-16 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Nút chuyển sang màn hình Đăng nhập) |
| TC-FR20-17 | TS-DOM | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile: Xoay màn hình thiết bị khi đang điền form) |
| TC-FR20-60 | TS-BVA | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile BVA: Mật khẩu độ dài 5 ký tự) |
| TC-FR20-61 | TS-BVA | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile BVA: Mật khẩu độ dài 6 ký tự) |
| TC-FR20-62 | TS-BVA | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile BVA: Họ Tên độ dài 1 ký tự) |
| TC-FR20-63 | TS-BVA | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile BVA: Họ Tên độ dài 255 ký tự) |
| TC-FR20-64 | TS-BVA | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile BVA: Họ Tên độ dài 256 ký tự) |
| TC-FR20-90 | TS-GUI | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile GUI: Hiển thị giao diện vừa vặn trên màn hình thiết bị) |
| TC-FR20-91 | TS-GUI | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile GUI: Tự động cuộn trang theo ô nhập dữ liệu) |
| TC-FR20-92 | TS-GUI | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile GUI: Loại bàn phím tối ưu cho ô nhập Email) |
| TC-FR20-93 | TS-GUI | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile GUI: Hiệu ứng nút bấm khi nhấn Đăng ký) |
| TC-FR20-94 | TS-GUI | AI | giữ nguyên bản AI `D_FR20_step6_20261020-235937.json` | VALID (Mobile GUI: Cửa sổ thông báo lỗi phản hồi từ hệ thống) |


