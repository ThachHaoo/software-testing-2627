# Nhóm dữ kiện bug – T1 checklist C2 (đề xuất, SV xác nhận 🔒)

Sinh bằng `tools/bug_groups_hw03.py` từ `checklist.json` + `failed_list.md`. 32 item Failed MỚI / trùng một phần → **28 nhóm**. Gom theo dữ kiện quan sát giống nhau (cùng phần tử hoặc cùng hành vi, khác màn/nền tảng); AI không kết luận nguyên nhân. SV tách/gộp nhóm, rồi viết BUG từ khung tương ứng. Expected/Actual chép nguyên văn từ checklist (Actual = notes chạy tay hoặc số đo auto).

| Nhóm | Khung | Dữ kiện chung | Item | Nền tảng Failed | Trùng / liên quan |
|---|---|---|---|---|---|
| G-01 | `BUG-58.md` | Thứ tự Tab không theo vị trí hiển thị (focus bắt đầu ở form, navbar bị đi sau / bỏ qua) | CL-10, CL-12 | P1, P2 | – |
| G-02 | `BUG-59.md` | Tiêu đề tab là "frontend-web" ở mọi trang | CL-13 | P1, P2, P3 | – |
| G-03 | `BUG-60.md` | <html lang="en"> | CL-14 | P1, P2, P3 | – |
| G-04 | `BUG-61.md` | Trang không có thẻ <h1> | CL-02 | P1, P2, P3 | – |
| G-05 | `BUG-62.md` | Ô Email bước 1 Quên mật khẩu: type="text", email sai định dạng vẫn gửi request (phần /login trùng #4) | CL-17, CL-66 | P1, P2, P3 | CL-17: một phần #4; CL-66: một phần #4 |
| G-06 | `BUG-63.md` | Nhãn trường bắt buộc thiếu '*' ở Quên mật khẩu B1/B2 và Hồ sơ (phần /login trùng #7) | CL-20, CL-21 | P1, P2, P3 | CL-20: một phần #7 |
| G-07 | `BUG-64.md` | Lỗi validate chỉ hiện ở hộp thoại trình duyệt (Quên MK B2, Hồ sơ) | CL-23 | P1, P2, P3 | – |
| G-08 | `BUG-65.md` | Bấm nhãn không focus ô nhập (Đăng nhập, Hồ sơ) | CL-38 | P1, P2, P3 | – |
| G-09 | `BUG-66.md` | Quên mật khẩu: không có chỉ báo bước | CL-24 | P1, P2, P3 | – |
| G-10 | `BUG-67.md` | Quên mật khẩu B1: không có 'Quay lại đăng nhập' | CL-25 | P1, P2, P3 | – |
| G-11 | `BUG-68.md` | Quên mật khẩu B2: không có ô Xác nhận mật khẩu mới | CL-26 | P1, P2, P3 | CL-26: liên quan #30 |
| G-12 | `BUG-69.md` | Mã OTP hiển thị 4 chữ số | CL-28 | P1, P2, P3 | – |
| G-13 | `BUG-70.md` | Quên mật khẩu B2: mật khẩu 'Abcdef1!' bị báo yếu | CL-29 | P1, P2, P3 | CL-29: liên quan #17 |
| G-14 | `BUG-71.md` | Quên mật khẩu B2: nút chính và nút phụ giống nhau (G-13 cũ giữ gộp; CL-04 trùng #160 nên còn CL-06) | CL-06 | P1, P2, P3 | – |
| G-15 | `BUG-72.md` | Hồ sơ: SĐT '912345678' được lưu, thông báo không nêu quy tắc (phần lưu liên quan #97/#113) | CL-32 | P1, P2, P3 | CL-32: một phần #97, #113 |
| G-16 | `BUG-73.md` | Hồ sơ: sau Cập nhật + F5, trường quay về giá trị cũ | CL-37 | P1, P2, P3 | CL-37: liên quan #111, #123 |
| G-17 | `BUG-74.md` | Navbar: nút đăng xuất nhãn "Thoát" | CL-42 | P1, P2, P3 | – |
| G-18 | `BUG-75.md` | Navbar: đổi Họ Tên, navbar giữ tên cũ tới khi tải lại | CL-56 | P1, P2, P3 | – |
| G-19 | `BUG-76.md` | /profile khi chưa đăng nhập: không chuyển, không có link tới Đăng nhập | CL-49 | P1, P2, P3 | – |
| G-20 | `BUG-77.md` | URL không tồn tại: vùng nội dung trống, không có link về trang chủ | CL-50 | P1, P2, P3 | – |
| G-21 | `BUG-78.md` | Nút submit không khoá / không có chỉ báo khi bấm nhiều lần (Đăng nhập, Quên MK B1/B2, Hồ sơ) | CL-53, SV-06 | P1, P2, P3 | – |
| G-22 | `BUG-79.md` | Lịch sử đơn: không có trạng thái đang tải | CL-63 | P1, P2, P3 | – |
| G-23 | `BUG-80.md` | Lịch sử đơn: Ngày đặt khác định dạng giữa các nền tảng | CL-09 | P1, P2, P3 | – |
| G-24 | `BUG-81.md` | Lịch sử đơn: nút 'Hủy đơn' dùng được ở đơn đang giao | CL-59 | P1, P2, P3 | – |
| G-25 | `BUG-82.md` | Autofill của trình duyệt không điền được (dán được) | SV-02 | P1, P2, P3 | – |
| G-26 | `BUG-83.md` | Submit thất bại: focus không về ô lỗi | SV-03 | P1, P2, P3 | – |
| G-27 | `BUG-84.md` | Độ tương phản chữ/nhãn dưới 4.5:1 ở Đăng nhập, Hồ sơ | SV-04 | P1, P2, P3 | – |
| G-28 | `BUG-85.md` | Link 'Quên mật khẩu?', 'Đăng ký ngay' nhỏ hơn 24×24 px | SV-05 | P1, P2, P3 | – |

## G-01 → `BUG-58.md` – Thứ tự Tab không theo vị trí hiển thị (focus bắt đầu ở form, navbar bị đi sau / bỏ qua)

### CL-10 – Thứ tự Tab theo vị trí hiển thị (trên→dưới, trái→phải) (Đăng nhập)

- Căn cứ: FR-21.5 (README.md:248)
- Expected (chép): Từ đầu trang bấm Tab liên tục: focus đi qua mọi control tương tác được theo vị trí hiển thị — từ trên xuống dưới; cùng một hàng thì từ trái sang phải. Fail nếu focus nhảy tới control nằm phía trên control trước đó (cùng hàng: nằm bên trái), hoặc bỏ qua một control tương tác được.
- Actual P1 (auto): Lỗi: Error: nhảy ngược: 'Sign In'(449,425) → 'EShop'(16,16) · chuỗi Tab: button'Sign In'@(449,425) → a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) → input'text'@(449,241) → input'text'@(449,331) → a'Quên mật khẩu?'@(729,389) → a'Đăng ký ngay'@(659,481) · ảnh: `evidence/auto/P1_CL-10_1.png`
- Actual P2 (auto): Lỗi: Error: nhảy ngược: 'Sign In'(449,425) → 'EShop'(16,16) · chuỗi Tab: button'Sign In'@(449,425) → a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) → input'text'@(449,241) → input'text'@(449,331) → a'Quên mật khẩu?'@(729,390) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) · ảnh: `evidence/auto/P2_CL-10_1.png`

### CL-12 – Thứ tự Tab ở bước 2 theo vị trí hiển thị (trên→dưới, trái→phải) (Quên mật khẩu (bước 2))

- Căn cứ: FR-21.5 (README.md:248)
- Expected (chép): Từ đầu trang bấm Tab liên tục: focus đi qua mọi control tương tác được theo vị trí hiển thị — từ trên xuống dưới; cùng một hàng thì từ trái sang phải. Fail nếu focus nhảy tới control nằm phía trên control trước đó (cùng hàng: nằm bên trái), hoặc bỏ qua một control tương tác được.
- Actual P1 (auto): Lỗi: Error: bỏ qua: a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) · chuỗi Tab: input'text'@(449,301) → input'password'@(449,391) → button'Đặt lại mật khẩu'@(449,449) → button'← Quay lại'@(449,505) · ảnh: `evidence/auto/P1_CL-12_1.png`
- Actual P2 (auto): Lỗi: Error: bỏ qua: a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) · chuỗi Tab: input'text'@(449,301) → input'password'@(449,391) → button'Đặt lại mật khẩu'@(449,449) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) · ảnh: `evidence/auto/P2_CL-12_1.png`

## G-02 → `BUG-59.md` – Tiêu đề tab là "frontend-web" ở mọi trang

### CL-13 – Tiêu đề tab trình duyệt mô tả trang (Tất cả màn C2)

- Căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống); WCAG 2.2 SC 2.4.2
- Expected (chép): Tiêu đề tab (document.title) chứa tên ứng dụng hoặc tên trang (vd 'Đăng nhập – EShop') và khác nhau giữa /login, /forgot-password, /profile. Fail nếu không chứa tên ứng dụng/tên trang hoặc giống nhau ở cả 3 trang.
- Actual P1 (auto): Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"] · ảnh: `evidence/auto/P1_CL-13_1.png`
- Actual P2 (auto): Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"] · ảnh: `evidence/auto/P2_CL-13_1.png`
- Actual P3 (auto): Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"] · ảnh: `evidence/auto/P3_CL-13_1.png`

## G-03 → `BUG-60.md` – <html lang="en">

### CL-14 – Khai báo ngôn ngữ trang là tiếng Việt (Tất cả màn C2)

- Căn cứ: WCAG 2.2 SC 3.1.1 (Language of Page)
- Expected (chép): Thẻ <html> có lang='vi'. Fail nếu lang khác 'vi' hoặc không có.
- Actual P1 (auto): Lỗi: Error: lang = "en" · <html lang="en"> · ảnh: `evidence/auto/P1_CL-14_1.png`
- Actual P2 (auto): Lỗi: Error: lang = "en" · <html lang="en"> · ảnh: `evidence/auto/P2_CL-14_1.png`
- Actual P3 (auto): Lỗi: Error: lang = "en" · <html lang="en"> · ảnh: `evidence/auto/P3_CL-14_1.png`

## G-04 → `BUG-61.md` – Trang không có thẻ <h1>

### CL-02 – Mỗi trang có đúng 1 thẻ <h1> (Đăng nhập, Quên mật khẩu, Hồ sơ)

- Căn cứ: FR-21.4 (README.md:247)
- Expected (chép): Trên mỗi trang /login, /forgot-password, /profile, lệnh DevTools `document.querySelectorAll('h1').length` trả về đúng 1. Fail nếu một trang trả 0 hoặc ≥ 2.
- Actual P1 (auto): Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1 · ảnh: `evidence/auto/P1_CL-02_1.png`
- Actual P2 (auto): Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1 · ảnh: `evidence/auto/P2_CL-02_1.png`
- Actual P3 (auto): Lỗi: Error: /login: có 0 thẻ <h1> · Lỗi: Error: /forgot-password: có 0 thẻ <h1> · Lỗi: Error: /profile: có 0 thẻ <h1> · /login: 0 h1 · /forgot-password: 0 h1 · /profile: 0 h1 · ảnh: `evidence/auto/P3_CL-02_1.png`

## G-05 → `BUG-62.md` – Ô Email bước 1 Quên mật khẩu: type="text", email sai định dạng vẫn gửi request (phần /login trùng #4)

### CL-17 – Ô Email dùng type="email" (Đăng nhập, Quên mật khẩu (bước 1))

- Căn cứ: FR-02.4 (README.md:44); FR-22.2 (README.md:253)
- Expected (chép): DevTools: ô Email trên /login và bước 1 /forgot-password có type="email". Fail nếu type khác "email".
- Actual P1 (auto): Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text" · ảnh: `evidence/auto/P1_CL-17_1.png`
- Actual P2 (auto): Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text" · ảnh: `evidence/auto/P2_CL-17_1.png`
- Actual P3 (auto): Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text" · ảnh: `evidence/auto/P3_CL-17_1.png`

### CL-66 – Email sai định dạng bị chặn trước khi gửi (Đăng nhập, Quên mật khẩu (bước 1))

- Căn cứ: FR-02.4 (README.md:44); FR-22.2 (README.md:253)
- Expected (chép): Nhập 'abc' vào ô Email rồi submit → form bị chặn, có thông báo validate, DevTools Network không có request gửi đi. Fail nếu form gửi request.
- Actual P1 (auto): Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true · ảnh: `evidence/auto/P1_CL-66_1.png`
- Actual P2 (auto): Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true · ảnh: `evidence/auto/P2_CL-66_1.png`
- Actual P3 (auto): Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true · ảnh: `evidence/auto/P3_CL-66_1.png`

## G-06 → `BUG-63.md` – Nhãn trường bắt buộc thiếu '*' ở Quên mật khẩu B1/B2 và Hồ sơ (phần /login trùng #7)

### CL-20 – Dấu * trên nhãn trường bắt buộc (Đăng nhập, Quên mật khẩu)

- Căn cứ: FR-22.1 (README.md:252); checklist Text box – 'Red asterisk on mandatory fields'
- Expected (chép): Nhãn Email, Mật khẩu (/login); Email (bước 1); OTP, Mật khẩu mới, Xác nhận mật khẩu (bước 2) đều có '*' cạnh nhãn. Fail nếu ≥ 1 nhãn thiếu '*'.
- Actual P1 (auto): Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới" · ảnh: `evidence/auto/P1_CL-20_1.png`
- Actual P2 (auto): Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới" · ảnh: `evidence/auto/P2_CL-20_1.png`
- Actual P3 (auto): Lỗi: Error: /login: nhãn "Username" thiếu '*' · Lỗi: Error: /login: nhãn "Mật khẩu" thiếu '*' · Lỗi: Error: bước 1: nhãn "Nhập Email của bạn" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mã OTP (4 số)" thiếu '*' · Lỗi: Error: bước 2: nhãn "Mật khẩu mới" thiếu '*' · /login "Username" · /login "Mật khẩu" · bước 1 "Nhập Email của bạn" · bước 2 "Mã OTP (4 số)" · bước 2 "Mật khẩu mới" · ảnh: `evidence/auto/P3_CL-20_1.png`

### CL-21 – Dấu * trên trường mà form bắt buộc nhập (Hồ sơ)

- Căn cứ: FR-22.1 (README.md:252)
- Expected (chép): Với từng trường Họ Tên, Số điện thoại, Địa chỉ: để trống rồi bấm Cập nhật. Trường nào khiến form bị chặn thì nhãn phải có '*'; trường không bắt buộc thì không có '*'. Fail nếu một trường bị chặn khi trống mà nhãn không có '*'.
- Actual P1 (auto): Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng" · ảnh: `evidence/auto/P1_CL-21_1.png`
- Actual P2 (auto): Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng" · ảnh: `evidence/auto/P2_CL-21_1.png`
- Actual P3 (auto): Lỗi: Error: "Họ Tên" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Số điện thoại" bị chặn khi trống nhưng nhãn không có '*' · Lỗi: Error: "Địa chỉ giao hàng" bị chặn khi trống nhưng nhãn không có '*' · "Họ Tên" trống: bị chặn; nhãn "Họ Tên" · "Số điện thoại" trống: bị chặn; nhãn "Số điện thoại" · "Địa chỉ giao hàng" trống: bị chặn; nhãn "Địa chỉ giao hàng" · ảnh: `evidence/auto/P3_CL-21_1.png`

## G-07 → `BUG-64.md` – Lỗi validate chỉ hiện ở hộp thoại trình duyệt (Quên MK B2, Hồ sơ)

### CL-23 – Thông báo lỗi validate hiển thị trong trang, phía trên nút submit (Quên mật khẩu, Hồ sơ)

- Căn cứ: FR-22.4 (README.md:255); giả định GA3
- Expected (chép): Gây lỗi: mật khẩu mới yếu (bước 2), SĐT sai định dạng (Hồ sơ). Thông báo lỗi xuất hiện trong trang, phía trên nút submit của form đó. Fail nếu lỗi hiện dưới nút hoặc chỉ hiện ở hộp thoại trình duyệt (alert) không gắn với vị trí nào trong form.
- Actual P1 (auto): Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"] · ảnh: `evidence/auto/P1_CL-23_1.png`
- Actual P2 (auto): Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Protocol error (Browser.removeBrowserContext): this._windows[aWindow.__SSi] is undefined · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"] · ảnh: `evidence/auto/P2_CL-23_1.png`
- Actual P3 (auto): Lỗi: Error: bước 2 mật khẩu yếu: lỗi chỉ ở hộp thoại hoặc không có (GA3) · Lỗi: Error: Hồ sơ SĐT sai: lỗi chỉ ở hộp thoại hoặc không có (GA3) · bước 2 mật khẩu yếu: chữ mới []; hộp thoại ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · Hồ sơ SĐT sai: chữ mới []; hộp thoại ["Cập nhật thành công!"] · ảnh: `evidence/auto/P3_CL-23_1.png`

## G-08 → `BUG-65.md` – Bấm nhãn không focus ô nhập (Đăng nhập, Hồ sơ)

### CL-38 – Nhãn gắn với ô nhập (bấm nhãn → focus ô) (Đăng nhập, Hồ sơ)

- Căn cứ: Checklist Text box – 'Correct label'; WCAG 2.2 SC 1.3.1
- Expected (chép): Bấm vào chữ nhãn (vd 'Mật khẩu', 'Họ Tên') → con trỏ nhảy vào ô tương ứng. Fail nếu bấm nhãn không có tác dụng.
- Actual P1 (auto): Lỗi: Error: /login: bấm nhãn "Username" không focus ô · Lỗi: Error: /login: bấm nhãn "Mật khẩu" không focus ô · Lỗi: Error: /profile: bấm nhãn "Họ Tên" không focus ô · Lỗi: Error: /profile: bấm nhãn "Số điện thoại" không focus ô · Lỗi: Error: /profile: bấm nhãn "Địa chỉ giao hàng" không focus ô · /login "Username": không focus · /login "Mật khẩu": không focus · /profile "Họ Tên": không focus · /profile "Số điện thoại": không focus · /profile "Địa chỉ giao hàng": không focus · ảnh: `evidence/auto/P1_CL-38_1.png`
- Actual P2 (auto): Lỗi: Error: /login: bấm nhãn "Username" không focus ô · Lỗi: Error: /login: bấm nhãn "Mật khẩu" không focus ô · Lỗi: Error: /profile: bấm nhãn "Họ Tên" không focus ô · Lỗi: Error: /profile: bấm nhãn "Số điện thoại" không focus ô · Lỗi: Error: /profile: bấm nhãn "Địa chỉ giao hàng" không focus ô · /login "Username": không focus · /login "Mật khẩu": không focus · /profile "Họ Tên": không focus · /profile "Số điện thoại": không focus · /profile "Địa chỉ giao hàng": không focus · ảnh: `evidence/auto/P2_CL-38_1.png`
- Actual P3 (auto): Lỗi: Error: /login: bấm nhãn "Username" không focus ô · Lỗi: Error: /login: bấm nhãn "Mật khẩu" không focus ô · Lỗi: Error: /profile: bấm nhãn "Họ Tên" không focus ô · Lỗi: Error: /profile: bấm nhãn "Số điện thoại" không focus ô · Lỗi: Error: /profile: bấm nhãn "Địa chỉ giao hàng" không focus ô · /login "Username": không focus · /login "Mật khẩu": không focus · /profile "Họ Tên": không focus · /profile "Số điện thoại": không focus · /profile "Địa chỉ giao hàng": không focus · ảnh: `evidence/auto/P3_CL-38_1.png`

## G-09 → `BUG-66.md` – Quên mật khẩu: không có chỉ báo bước

### CL-24 – Có chỉ báo bước (Step Indicator) (Quên mật khẩu)

- Căn cứ: FR-03.3 (README.md:52); FR-22.5 (README.md:256)
- Expected (chép): Bước 1 hiển thị 'Bước 1 / 2' (hoặc chỉ báo tương đương thấy rõ bước hiện tại và tổng số bước); bước 2 hiển thị 'Bước 2 / 2'. Fail nếu một bước không có chỉ báo.
- Actual P1 (tay): Không có chỉ báo bước · ảnh: `evidence/P1_chrome/P1_CL-24_1.png`
- Actual P2 (tay): Không có chỉ báo bước · ảnh: `evidence/P2_firefox/P2_CL-24_1.png`
- Actual P3 (tay): Không có chỉ báo bước · ảnh: `evidence/P3_android/P3_CL-24_1.png`

## G-10 → `BUG-67.md` – Quên mật khẩu B1: không có 'Quay lại đăng nhập'

### CL-25 – Có nút 'Quay lại đăng nhập' (Quên mật khẩu (bước 1))

- Căn cứ: FR-03.4 (README.md:53)
- Expected (chép): Bước 1 có nút/link nhãn 'Quay lại đăng nhập'; bấm → về /login. Fail nếu không có, nhãn khác nghĩa, hoặc không về /login.
- Actual P1 (auto): Lỗi: Error: bước 1 không có "Quay lại đăng nhập" · bước 1 có "Quay lại đăng nhập": false · ảnh: `evidence/auto/P1_CL-25_1.png`
- Actual P2 (auto): Lỗi: Error: bước 1 không có "Quay lại đăng nhập" · bước 1 có "Quay lại đăng nhập": false · ảnh: `evidence/auto/P2_CL-25_1.png`
- Actual P3 (auto): Lỗi: Error: bước 1 không có "Quay lại đăng nhập" · bước 1 có "Quay lại đăng nhập": false · ảnh: `evidence/auto/P3_CL-25_1.png`

## G-11 → `BUG-68.md` – Quên mật khẩu B2: không có ô Xác nhận mật khẩu mới

### CL-26 – Có ô 'Xác nhận mật khẩu mới' (Quên mật khẩu (bước 2))

- Căn cứ: FR-03.5 (README.md:57)
- Expected (chép): Bước 2 có đủ 3 ô: OTP, Mật khẩu mới, Xác nhận mật khẩu mới. Fail nếu thiếu ô xác nhận.
- Actual P1 (auto): Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"] · ảnh: `evidence/auto/P1_CL-26_1.png`
- Actual P2 (auto): Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"] · ảnh: `evidence/auto/P2_CL-26_1.png`
- Actual P3 (auto): Lỗi: Error: không có ô Xác nhận mật khẩu mới · bước 2: 2 ô – ["Mã OTP (4 số)","Mật khẩu mới"] · ảnh: `evidence/auto/P3_CL-26_1.png`

## G-12 → `BUG-69.md` – Mã OTP hiển thị 4 chữ số

### CL-28 – Mã OTP hiển thị có đúng 6 chữ số (Quên mật khẩu (bước 2))

- Căn cứ: FR-03.2 (README.md:51)
- Expected (chép): Sau khi gửi email ở bước 1, mã OTP hiển thị trên màn hình có đúng 6 chữ số. Fail nếu mã có số chữ số khác 6.
- Actual P1 (auto): Lỗi: Error: mã có 4 chữ số · mã hiển thị: 1846 · ảnh: `evidence/auto/P1_CL-28_1.png`, `evidence/auto/P1_CL-28_2.png`
- Actual P2 (auto): Lỗi: Error: mã có 4 chữ số · mã hiển thị: 9894 · ảnh: `evidence/auto/P2_CL-28_1.png`, `evidence/auto/P2_CL-28_2.png`
- Actual P3 (auto): Lỗi: Error: mã có 4 chữ số · mã hiển thị: 8382 · ảnh: `evidence/auto/P3_CL-28_1.png`, `evidence/auto/P3_CL-28_2.png`

## G-13 → `BUG-70.md` – Quên mật khẩu B2: mật khẩu 'Abcdef1!' bị báo yếu

### CL-29 – Mật khẩu mới hợp lệ theo FR-01 được chấp nhận (Quên mật khẩu (bước 2))

- Căn cứ: FR-03.6 (README.md:58, 34)
- Expected (chép): Với OTP đúng, Mật khẩu mới 'Abcdef1!' (8 ký tự, có hoa, thường, số, '!') → đổi thành công; đăng nhập lại bằng mật khẩu mới được. Fail nếu bị báo mật khẩu yếu.
- Actual P1 (auto): Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · ảnh: `evidence/auto/P1_CL-29_1.png`
- Actual P2 (auto): Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · ảnh: `evidence/auto/P2_CL-29_1.png`
- Actual P3 (auto): Lỗi: Error: mật khẩu "Abcdef1!" không được chấp nhận · đăng nhập bằng "Abcdef1!": false; thông báo: ["Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."] · ảnh: `evidence/auto/P3_CL-29_1.png`

## G-14 → `BUG-71.md` – Quên mật khẩu B2: nút chính và nút phụ giống nhau (G-13 cũ giữ gộp; CL-04 trùng #160 nên còn CL-06)

### CL-06 – Nút chính và nút phụ phân biệt được bằng hình thức (Quên mật khẩu (bước 2))

- Căn cứ: Shneiderman #1 (nhất quán); checklist Button – 'colour signals intent'
- Expected (chép): Nút 'Đặt lại mật khẩu' (chính) và nút quay lại (phụ) khác nhau rõ về màu hoặc kiểu (viền/nền). Fail nếu hai nút cùng màu nền, cùng kích thước, cùng kiểu.
- Actual P1 (tay): Nút chính và nút phụ giống nhau · ảnh: `evidence/P1_chrome/P1_CL-06_1.png`
- Actual P2 (tay): Nút chính và nút phụ giống nhau · ảnh: `evidence/P2_firefox/P2_CL-06_1.png`
- Actual P3 (tay): Nút chính và nút phụ giống nhau · ảnh: `evidence/P3_android/P3_CL-06_1.png`

## G-15 → `BUG-72.md` – Hồ sơ: SĐT '912345678' được lưu, thông báo không nêu quy tắc (phần lưu liên quan #97/#113)

### CL-32 – SĐT không hợp lệ bị từ chối, thông báo nêu đúng quy tắc (Hồ sơ)

- Căn cứ: FR-04.2 (README.md:65); Nielsen #9
- Expected (chép): Nhập '912345678' (không bắt đầu bằng 0) → bị từ chối, không lưu; thông báo nêu 'bắt đầu bằng 0, 10–11 chữ số'. Fail nếu được lưu hoặc thông báo nêu quy tắc khác SRS.
- Actual P1 (auto): Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678" · ảnh: `evidence/auto/P1_CL-32_1.png`
- Actual P2 (auto): Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678" · ảnh: `evidence/auto/P2_CL-32_1.png`
- Actual P3 (auto): Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678" · ảnh: `evidence/auto/P3_CL-32_1.png`

## G-16 → `BUG-73.md` – Hồ sơ: sau Cập nhật + F5, trường quay về giá trị cũ

### CL-37 – Cập nhật hồ sơ được lưu bền (Hồ sơ)

- Căn cứ: FR-04.1 (README.md:64)
- Expected (chép): Đổi Họ Tên, SĐT hợp lệ, Địa chỉ → Cập nhật → tải lại trang (F5) → 3 trường hiển thị giá trị mới. Fail nếu ≥ 1 trường quay về giá trị cũ.
- Actual P1 (auto): Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""] · ảnh: `evidence/auto/P1_CL-37_1.png`
- Actual P2 (auto): Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""] · ảnh: `evidence/auto/P2_CL-37_1.png`
- Actual P3 (auto): Lỗi: Error: có trường quay về giá trị cũ · sau F5: ["Test User","",""] · ảnh: `evidence/auto/P3_CL-37_1.png`

## G-17 → `BUG-74.md` – Navbar: nút đăng xuất nhãn "Thoát"

### CL-42 – Nút đăng xuất có nhãn 'Đăng xuất' (Navbar)

- Căn cứ: FR-23.3 (README.md:262)
- Expected (chép): Khi đã đăng nhập, nút đăng xuất trên navbar có nhãn đúng 'Đăng xuất'. Fail nếu nhãn khác (vd 'Thoát', 'Logout').
- Actual P1 (auto): Lỗi: Error: nhãn là "Thoát" · nhãn nút: "Thoát" · ảnh: `evidence/auto/P1_CL-42_1.png`
- Actual P2 (auto): Lỗi: Error: nhãn là "Thoát" · nhãn nút: "Thoát" · ảnh: `evidence/auto/P2_CL-42_1.png`
- Actual P3 (auto): Lỗi: Error: nhãn là "Thoát" · nhãn nút: "Thoát" · ảnh: `evidence/auto/P3_CL-42_1.png`

## G-18 → `BUG-75.md` – Navbar: đổi Họ Tên, navbar giữ tên cũ tới khi tải lại

### CL-56 – Đổi Họ Tên cập nhật ngay trên navbar (Hồ sơ, Navbar)

- Căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống); Shneiderman #1
- Expected (chép): Đổi Họ Tên thành 'Test Đổi' → Cập nhật → navbar hiển thị 'Test Đổi' mà không cần tải lại trang. Fail nếu navbar vẫn tên cũ cho tới khi F5.
- Actual P1 (auto): Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát" · ảnh: `evidence/auto/P1_CL-56_1.png`
- Actual P2 (auto): Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát" · ảnh: `evidence/auto/P2_CL-56_1.png`
- Actual P3 (auto): Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát" · ảnh: `evidence/auto/P3_CL-56_1.png`

## G-19 → `BUG-76.md` – /profile khi chưa đăng nhập: không chuyển, không có link tới Đăng nhập

### CL-49 – /profile khi chưa đăng nhập dẫn được tới Đăng nhập (Hồ sơ)

- Căn cứ: Nielsen #3 (lối thoát); Nielsen #9
- Expected (chép): Chưa đăng nhập, mở /profile → hoặc tự chuyển tới /login, hoặc thông báo có link/nút tới Đăng nhập (1 lần bấm). Fail nếu chỉ có chữ, không có đường tới Đăng nhập ngoài navbar.
- Actual P1 (auto): Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0 · ảnh: `evidence/auto/P1_CL-49_1.png`, `evidence/auto/P1_CL-49_2.png`
- Actual P2 (auto): Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0 · ảnh: `evidence/auto/P2_CL-49_1.png`, `evidence/auto/P2_CL-49_2.png`
- Actual P3 (auto): Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0 · ảnh: `evidence/auto/P3_CL-49_1.png`, `evidence/auto/P3_CL-49_2.png`

## G-20 → `BUG-77.md` – URL không tồn tại: vùng nội dung trống, không có link về trang chủ

### CL-50 – URL không tồn tại hiển thị trang 404 có lối về (Tất cả màn C2)

- Căn cứ: Nielsen #9; Nielsen #3
- Expected (chép): Mở /profil (gõ sai) → trang báo không tìm thấy, có link về trang chủ. Fail nếu trang trắng (chỉ còn header/footer) không có thông báo.
- Actual P1 (auto): Lỗi: Error: không có thông báo không tìm thấy · Lỗi: Error: không có link về trang chủ trong trang · nội dung main: ""; link về '/': 0 · ảnh: `evidence/auto/P1_CL-50_1.png`, `evidence/auto/P1_CL-50_2.png`
- Actual P2 (auto): Lỗi: Error: không có thông báo không tìm thấy · Lỗi: Error: không có link về trang chủ trong trang · nội dung main: ""; link về '/': 0 · ảnh: `evidence/auto/P2_CL-50_1.png`, `evidence/auto/P2_CL-50_2.png`
- Actual P3 (auto): Lỗi: Error: không có thông báo không tìm thấy · Lỗi: Error: không có link về trang chủ trong trang · nội dung main: ""; link về '/': 0 · ảnh: `evidence/auto/P3_CL-50_1.png`, `evidence/auto/P3_CL-50_2.png`

## G-21 → `BUG-78.md` – Nút submit không khoá / không có chỉ báo khi bấm nhiều lần (Đăng nhập, Quên MK B1/B2, Hồ sơ)

### CL-53 – Có chỉ báo đang xử lý và chống gửi trùng (Đăng nhập)

- Căn cứ: Norman – Feedback; Shneiderman #3 (phản hồi đầy đủ)
- Expected (chép): DevTools Network throttling 'Slow 3G': bấm Đăng nhập → trong lúc chờ, nút bị vô hiệu hoá hoặc có chỉ báo đang tải; bấm thêm 2 lần chỉ phát sinh 1 request /api/login. Fail nếu không có chỉ báo hoặc phát sinh nhiều request.
- Actual P1 (tay): Không có đang xử lý và chống gửi trùng · ảnh: `evidence/P1_chrome/P1_CL-53_1.png`
- Actual P2 (tay): Không có đang xử lý và chống gửi trùng · ảnh: `evidence/P2_firefox/P2_CL-53_1.png`
- Actual P3 (tay): Không có đang xử lý và chống gửi trùng · ảnh: `evidence/P3_android/P3_CL-53_1.png`

### SV-06 – Chống gửi trùng dữ liệu (Debounce/Disable) khi nhấp đúp/nhấp liên tiếp vào nút submit ở điều kiện mạng bình thường (Quên mật khẩu B1 / B2, Hồ sơ)

- Căn cứ: Slide "Double-submit on double-click"; Nielsen #5 (Phòng ngừa lỗi)
- Expected (chép): Ở điều kiện mạng bình thường (không bật throttling), nhấp chuột thật nhanh (double-click) vào nút 'Lấy mã OTP', 'Đặt lại mật khẩu' hoặc 'Cập nhật': hệ thống lập tức khóa nút hoặc debounce request sao cho chỉ có đúng 1 request API được gửi đi. Fail nếu gửi từ 2 request trở lên hoặc hiển thị nhiều thông báo trùng lặp.
- Actual P1 (auto): Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: Error: Đặt lại mật khẩu: 0 request, 2 hộp thoại · Lỗi: Error: Cập nhật: 0 request PUT, 2 hộp thoại · Lấy mã OTP: 2 request · Đặt lại mật khẩu: 0 request, 2 hộp thoại · Cập nhật: 0 request PUT, 2 hộp thoại · ảnh: `evidence/auto/P1_SV-06_1.png`
- Actual P2 (auto): Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: Error: Đặt lại mật khẩu: 0 request, 2 hộp thoại · Lỗi: Error: Cập nhật: 0 request PUT, 2 hộp thoại · Lấy mã OTP: 2 request · Đặt lại mật khẩu: 0 request, 2 hộp thoại · Cập nhật: 0 request PUT, 2 hộp thoại · ảnh: `evidence/auto/P2_SV-06_1.png`
- Actual P3 (auto): Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: TimeoutError: locator.dblclick: Timeout 30000ms exceeded. · Lấy mã OTP: 2 request · ảnh: `evidence/auto/P3_SV-06_1.png`

## G-22 → `BUG-79.md` – Lịch sử đơn: không có trạng thái đang tải

### CL-63 – Có trạng thái đang tải khi lấy lịch sử đơn (Lịch sử đơn)

- Căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống)
- Expected (chép): Network throttling 'Slow 3G', tải lại /profile → trong lúc chờ có chỉ báo đang tải; không hiện 'chưa có đơn hàng' trước khi dữ liệu về. Fail nếu hiện empty state rồi mới hiện bảng.
- Actual P1 (tay): Không có trạng thái đang tải · ảnh: `evidence/P1_chrome/P1_CL-63_1.png`, `evidence/P1_chrome/P1_CL-63_2.png`
- Actual P2 (tay): Không có trạng thái đang tải, trang tải xong là tất cả dữ liệu cũng xong hết (không giống Chrome khi tải từng phần) · ảnh: `evidence/P2_firefox/P2_CL-63_1.png`
- Actual P3 (tay): Không có trạng thái đang tải, trang tải xong là tất cả dữ liệu cũng xong hết (không giống Chrome khi tải từng phần) · ảnh: `evidence/P3_android/P3_CL-63_1.png`, `evidence/P3_android/P3_CL-63_2.png`

## G-23 → `BUG-80.md` – Lịch sử đơn: Ngày đặt khác định dạng giữa các nền tảng

### CL-09 – Ngày đặt hiển thị nhất quán theo định dạng Việt Nam (Lịch sử đơn)

- Căn cứ: Nielsen #4 (nhất quán và chuẩn); SRS im lặng → giả định GA1
- Expected (chép): Ngày đặt hiển thị dạng dd/mm/yyyy và giống nhau trên P1, P2, P3. Fail nếu định dạng khác (mm/dd/yyyy, yyyy-mm-dd) hoặc khác nhau giữa các nền tảng.
- Actual P1 (tay): [SV chốt R11=b: Expected "dd/mm/yyyy và giống nhau trên P1, P2, P3" áp cho cả P1; ảnh P1_CL-09_1 hiện "9/11/2026" (ngày 1 chữ số, không phải dd/mm/yyyy), P2/P3 hiện "11/9/2026" → khác nhau giữa các nền tảng (lý do lấy từ khuyến nghị run_check R11, SV có thể sửa)] · ảnh: `evidence/P1_chrome/P1_CL-09_1.png`
- Actual P2 (tay): Sử dụng định dạng mm/dd/yyyy thay vì dd/mm/yyyy của người Việt · ảnh: `evidence/P2_firefox/P2_CL-09_1.png`
- Actual P3 (tay): Sử dụng định dạng mm/dd/yyyy thay vì dd/mm/yyyy của người Việt · ảnh: `evidence/P3_android/P3_CL-09_1.png`

## G-24 → `BUG-81.md` – Lịch sử đơn: nút 'Hủy đơn' dùng được ở đơn đang giao

### CL-59 – Không cho người dùng huỷ đơn ở trạng thái không được huỷ (Lịch sử đơn)

- Căn cứ: FR-10 (README.md:160–161)
- Expected (chép): Dòng đơn 'Đang giao', 'Đã giao', 'Đã hủy' không có nút 'Hủy đơn' (hoặc nút bị vô hiệu hoá); chỉ 'Chờ xác nhận', 'Đã xác nhận' có. Fail nếu nút dùng được ở trạng thái không được huỷ.
- Actual P1 (auto): Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false · ảnh: `evidence/auto/P1_CL-59_1.png`, `evidence/auto/P1_CL-59_2.png`
- Actual P2 (auto): Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false · ảnh: `evidence/auto/P2_CL-59_1.png`, `evidence/auto/P2_CL-59_2.png`
- Actual P3 (auto): Lỗi: Error: shipping: nút "Hủy đơn" dùng được · pending (#8): nút "Hủy đơn" dùng được = true · confirmed (#9): nút "Hủy đơn" dùng được = true · shipping (#10): nút "Hủy đơn" dùng được = true · delivered (#11): nút "Hủy đơn" dùng được = false · canceled (#12): nút "Hủy đơn" dùng được = false · ảnh: `evidence/auto/P3_CL-59_1.png`, `evidence/auto/P3_CL-59_2.png`

## G-25 → `BUG-82.md` – Autofill của trình duyệt không điền được (dán được)

### SV-02 – Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu (Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ)

- Căn cứ: Shneiderman #8 (Giảm tải trí nhớ ngắn hạn); Nielsen #7 (Linh hoạt và hiệu quả); Slide "Checklist - Text Box"
- Expected (chép): Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit. Fail nếu bất kỳ vế nào (dán hoặc autofill) bị hệ thống ngăn chặn/làm sai lệch dữ liệu.
- Actual P1 (tay): Tất cả đều có thể Paste vào, nhưng Autofill chỉ có ở Forgot Password. · ảnh: `evidence/P1_chrome/P1_SV-02_1.png`, `evidence/P1_chrome/P1_SV-02_2.png`, `evidence/P1_chrome/P1_SV-02_3.png`, `evidence/P1_chrome/P1_SV-02_4.png`
- Actual P2 (tay): Tất cả đều có thể Paste vào, nhưng không thể Autofill · ảnh: `evidence/P2_firefox/P2_SV-02_1.png`, `evidence/P2_firefox/P2_SV-02_2.png`, `evidence/P2_firefox/P2_SV-02_3.png`, `evidence/P2_firefox/P2_SV-02_4.png`
- Actual P3 (tay): Tất cả đều có thể Paste vào, nhưng không thể Autofill · ảnh: `evidence/P3_android/P3_SV-02_1.png`, `evidence/P3_android/P3_SV-02_2.png`, `evidence/P3_android/P3_SV-02_3.png`, `evidence/P3_android/P3_SV-02_4.png`

## G-26 → `BUG-83.md` – Submit thất bại: focus không về ô lỗi

### SV-03 – Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại (Đăng nhập, Quên mật khẩu B2, Hồ sơ)

- Căn cứ: Slide "Checklist - input-field validation" (Golden Rule: "On error, return focus to the offending field"); Shneiderman #5 (Xử lý lỗi đơn giản)
- Expected (chép): Nhập dữ liệu sai quy tắc (ví dụ: SĐT sai định dạng ở Hồ sơ hoặc Mật khẩu mới không đủ điều kiện ở Quên mật khẩu B2) rồi bấm submit: sau khi thông báo lỗi xuất hiện, con trỏ gõ phím (cursor) phải tự động quay lại focus ở đúng ô bị lỗi đó. Fail nếu con trỏ nhảy mất focus hoặc không quay lại ô nhập bị lỗi.
- Actual P1 (auto): Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false · ảnh: `evidence/auto/P1_SV-03_1.png`
- Actual P2 (auto): Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false · ảnh: `evidence/auto/P2_SV-03_1.png`
- Actual P3 (auto): Lỗi: Error: Đăng nhập: focus không về ô Mật khẩu · Lỗi: Error: Quên mật khẩu B2: focus không về ô Mật khẩu mới · Lỗi: Error: Hồ sơ: focus không về ô Số điện thoại · focus về ô lỗi – Đăng nhập (Mật khẩu): false; Quên MK B2 (Mật khẩu mới): false; Hồ sơ (SĐT): false · ảnh: `evidence/auto/P3_SV-03_1.png`

## G-27 → `BUG-84.md` – Độ tương phản chữ/nhãn dưới 4.5:1 ở Đăng nhập, Hồ sơ

### SV-04 – Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) (Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ)

- Căn cứ: WCAG 2.2 SC 1.4.3 (Contrast Minimum)
- Expected (chép): Kiểm tra bằng công cụ DevTools Accessibility / Lighthouse: tỉ lệ tương phản màu sắc của chữ (văn bản, label, placeholder, text trên button) so với màu nền đạt tối thiểu 4.5:1 (đối với chữ thường). Fail nếu tỉ lệ tương phản < 4.5:1 khiến chữ mờ khó đọc.
- Actual P1 (tay): Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không · ảnh: `evidence/P1_chrome/P1_SV-04_1.png`, `evidence/P1_chrome/P1_SV-04_2.png`, `evidence/P1_chrome/P1_SV-04_3.png`, `evidence/P1_chrome/P1_SV-04_4.png`
- Actual P2 (tay): Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không · ảnh: `evidence/P2_firefox/P2_SV-04_1.png`, `evidence/P2_firefox/P2_SV-04_2.png`, `evidence/P2_firefox/P2_SV-04_3.png`, `evidence/P2_firefox/P2_SV-04_4.png`
- Actual P3 (tay): Quên mật khẩu đạt nhưng mà Đăng nhập và Hồ sơ thì không · ảnh: `evidence/P3_android/P3_SV-04_1.png`, `evidence/P3_android/P3_SV-04_2.png`, `evidence/P3_android/P3_SV-04_3.png`, `evidence/P3_android/P3_SV-04_4.png`

## G-28 → `BUG-85.md` – Link 'Quên mật khẩu?', 'Đăng ký ngay' nhỏ hơn 24×24 px

### SV-05 – Kích thước vùng tương tác của con trỏ (Target Size) đối với các nút và link (Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ)

- Căn cứ: WCAG 2.2 SC 2.5.8 (Target Size Minimum - 24x24px)
- Expected (chép): Dùng thước đo DevTools kiểm tra chiều cao và chiều rộng vùng bấm của các nút ('Sign In', 'Lấy mã OTP', 'Cập nhật') và các liên kết ('Quên mật khẩu?', 'Đăng ký ngay'): vùng bấm nhận con trỏ (chuột hoặc ngón tay) phải đạt kích thước tối thiểu 24x24 px. Fail nếu có nút/link kích thước < 24x24 px.
- Actual P1 (auto): Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 382×40 · Quên mật khẩu?: 102×19 · Đăng ký ngay: 85×19 · Lấy mã OTP: 382×40 · Cập nhật: 271×40 · ảnh: `evidence/auto/P1_SV-05_1.png`
- Actual P2 (auto): Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 382×40 · Quên mật khẩu?: 102×19 · Đăng ký ngay: 85×19 · Lấy mã OTP: 382×40 · Cập nhật: 271×40 · ảnh: `evidence/auto/P2_SV-05_1.png`
- Actual P3 (auto): Lỗi: Error: Quên mật khẩu? < 24×24 px · Lỗi: Error: Đăng ký ngay < 24×24 px · Sign In: 295×40 · Quên mật khẩu?: 100×16 · Đăng ký ngay: 82×16 · Lấy mã OTP: 295×40 · Cập nhật: 311×40 · ảnh: `evidence/auto/P3_SV-05_1.png`
