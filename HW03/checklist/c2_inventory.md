# C2 – Tài khoản: khảo sát control + yêu cầu UI (AI nháp, bước T1 1/6)

SUT: `tkob-team/eshop-sut` @ `de0f48f`, thư mục `frontend-web/src`. Đường dẫn file:dòng tính từ `../eshop-sut/`.
Bảng control chỉ ghi **cái có trong mã** (tên, nhãn, loại, thuộc tính), dùng để biết control nào tồn tại. Expected của checklist lấy từ SRS và heuristic, **không** lấy từ mã.

## 1. Control theo màn hình

### 1.1 Navbar / Header (cả trang, trạng thái đã đăng nhập) – `frontend-web/src/App.jsx`

| # | Control | Loại | Nhãn / nội dung | Thuộc tính đáng chú ý | file:dòng |
|---|---|---|---|---|---|
| H1 | Logo | `Link` → `/` | "EShop" | `text-2xl font-bold` | App.jsx:21 |
| H2 | Giỏ hàng | `Link` → `/cart` | "Giỏ hàng" | `hover:underline`; không có phần tử badge | App.jsx:23 |
| H3 | Tên người dùng | `Link` → `/profile` | "Chào, {user.name}" | render qua `dangerouslySetInnerHTML`; màu `text-yellow-300` | App.jsx:26–28 |
| H4 | Đăng xuất | `button` | "Thoát" | `bg-red-500`; `onClick={logout}` | App.jsx:29 |
| H5 | Đăng nhập / Đăng ký | `Link` | "Đăng nhập", "Đăng ký" | chỉ hiện khi **chưa** đăng nhập | App.jsx:33–34 |
| H6 | Footer | text | "© 2026 EShop SUT. Dành cho mục đích kiểm thử." | | App.jsx:61–63 |
| H7 | Route | `Routes` | `/login`, `/forgot-password`, `/profile`, … | không có route 404 | App.jsx:50–59 |

Hành vi liên quan: `logout()` xoá token khỏi `localStorage`, đặt `user = null` — `context/AuthContext.jsx:37–41`; token đọc lại từ `localStorage` khi tải trang — `AuthContext.jsx:8–24`. Không có mã đánh dấu link đang chọn (active) trong `Header` (App.jsx:15–40).

Trang chung: `index.html` có `<html lang="en">`, `<title>frontend-web</title>` — `frontend-web/index.html:2,7`.

### 1.2 Đăng nhập – `/login` – `frontend-web/src/pages/Login.jsx`

| # | Control | Loại | Nhãn / nội dung | Thuộc tính đáng chú ý | file:dòng |
|---|---|---|---|---|---|
| L1 | Tiêu đề | `h2` | "Đăng Ký" | trang không có `h1` | Login.jsx:24 |
| L2 | Ô email | `input type="text"` | label "Username" | `required`; label không gắn `htmlFor`/`id` | Login.jsx:28–35 |
| L3 | Ô mật khẩu | `input type="text"` | label "Mật khẩu" | `required` | Login.jsx:38–45 |
| L4 | Quên mật khẩu? | `<a href>` → `/forgot-password` | "Quên mật khẩu?" | thẻ `a` thường (không phải `Link`) | Login.jsx:49–51 |
| L5 | Nút submit | `button type="submit"` | "Sign In" | `tabIndex={1}`; `bg-blue-600` | Login.jsx:53–59 |
| L6 | Đăng ký ngay | `Link` → `/register` | "Chưa có tài khoản? Đăng ký ngay" | | Login.jsx:61–63 |
| L7 | Thông báo lỗi | `div` | "Đăng nhập thất bại. Vui lòng kiểm tra lại." | nằm **sau** `</form>` | Login.jsx:18, 66 |

Hành vi: thành công → `navigate('/')` (Login.jsx:16); mọi lỗi API cùng một thông báo (Login.jsx:17–18). Không có trạng thái loading/disable nút khi đang gửi.

### 1.3 Quên mật khẩu – `/forgot-password` – `frontend-web/src/pages/ForgotPassword.jsx`

| # | Control | Loại | Nhãn / nội dung | Thuộc tính đáng chú ý | file:dòng |
|---|---|---|---|---|---|
| F1 | Tiêu đề | `h2` | "Quên Mật Khẩu" | không có `h1`; không có chỉ báo bước | ForgotPassword.jsx:43 |
| F2 | Ô email (bước 1) | `input type="text"` | "Nhập Email của bạn" | `required` | ForgotPassword.jsx:48–55 |
| F3 | Lấy mã OTP | `button type="submit"` | "Lấy mã OTP" | `bg-blue-600` | ForgotPassword.jsx:57–59 |
| F4 | Lỗi bước 1 | `alert()` | "Lỗi: " + lỗi API | hộp thoại trình duyệt | ForgotPassword.jsx:20 |
| F5 | Hộp OTP (bước 2) | `div` | "Mã OTP của bạn là: …" | `bg-green-100` | ForgotPassword.jsx:17, 65–67 |
| F6 | Ô OTP | `input type="text"` | "Mã OTP (4 số)" | `required` | ForgotPassword.jsx:69–76 |
| F7 | Ô mật khẩu mới | `input type="password"` | "Mật khẩu mới" | `required` | ForgotPassword.jsx:79–86 |
| F8 | Đặt lại mật khẩu | `button type="submit"` | "Đặt lại mật khẩu" | `bg-green-600` | ForgotPassword.jsx:90–92 |
| F9 | Quay lại | `button type="button"` | "← Quay lại" | `bg-green-600`; về bước 1 (`setStep(1)`), không về trang đăng nhập | ForgotPassword.jsx:93–95 |
| F10 | Lỗi / thành công bước 2 | `alert()` | thông báo mật khẩu yếu; "Mã OTP không đúng…"; "Đổi mật khẩu thành công!" | hộp thoại trình duyệt | ForgotPassword.jsx:28, 34, 37 |

Không có ô **Xác nhận mật khẩu mới**; không có nút **Quay lại đăng nhập** ở bước 1. Thành công → `navigate('/login')` (ForgotPassword.jsx:35).

### 1.4 Hồ sơ + Lịch sử đơn – `/profile` – `frontend-web/src/pages/Profile.jsx`

| # | Control | Loại | Nhãn / nội dung | Thuộc tính đáng chú ý | file:dòng |
|---|---|---|---|---|---|
| P1 | Chưa đăng nhập | text | "Vui lòng đăng nhập" | không có link tới `/login` | Profile.jsx:108 |
| P2 | Tiêu đề hồ sơ | `h2` | "Hồ sơ của bạn" | không có `h1` | Profile.jsx:113 |
| P3 | Email | `input type="text"` `disabled` | "Email (Không đổi)" | `bg-gray-100` | Profile.jsx:116–124 |
| P4 | Họ Tên | `input type="text"` | "Họ Tên" | `required`; nhãn không có `*` | Profile.jsx:127–134 |
| P5 | Số điện thoại | `input type="text"` | "Số điện thoại" | placeholder "VD: 0912345678" | Profile.jsx:137–144 |
| P6 | Địa chỉ giao hàng | `textarea` | "Địa chỉ giao hàng" | placeholder "Nhập địa chỉ của bạn" | Profile.jsx:147–155 |
| P7 | Cập nhật | `button type="submit"` | "Cập nhật" | `bg-blue-600` | Profile.jsx:157–162 |
| P8 | Thông báo hồ sơ | `alert()` | SĐT không hợp lệ; "Cập nhật thành công!"; "Lỗi cập nhật" | | Profile.jsx:44, 60, 62 |
| P9 | Tiêu đề lịch sử | `h2` | "Lịch sử đơn hàng" | | Profile.jsx:167 |
| P10 | Trạng thái rỗng | `p` | "Bạn chưa có đơn hàng nào." | không có icon/hình | Profile.jsx:168–170 |
| P11 | Bảng đơn | `table` | cột "Mã ĐH", "Ngày đặt", "Tổng tiền", "Trạng thái", "Thao tác" | | Profile.jsx:171–180 |
| P12 | Ô Ngày đặt | `td` | `toLocaleDateString()` | định dạng theo locale trình duyệt | Profile.jsx:185–187 |
| P13 | Ô Tổng tiền | `td` | `toLocaleString()` + " ₫" | định dạng theo locale trình duyệt | Profile.jsx:188–190 |
| P14 | Nhãn trạng thái | `span` | Chờ xác nhận / Đã xác nhận / Đang giao / Đã giao / Đã hủy | màu theo trạng thái | Profile.jsx:82–106, 191–197 |
| P15 | Hủy đơn | `button` | "Hủy đơn" | hiện khi status ≠ delivered và ≠ canceled (gồm `shipping`); không có hộp xác nhận | Profile.jsx:199–207 |
| P16 | Kết quả hủy | `alert()` | "Hủy đơn thành công!" / "Lỗi: …" | | Profile.jsx:75, 78 |

Không có trạng thái loading khi tải đơn; lỗi tải đơn chỉ ghi `console.error` (Profile.jsx:25–28). Dữ liệu seed không có đơn hàng (`backend/database.js:89–117`) → muốn kiểm bảng đơn phải tạo đơn trước qua Checkout.

## 2. Yêu cầu UI trích từ SRS (`../eshop-sut/README.md`, v2.0)

| Mã | Yêu cầu (nguyên văn rút gọn) | README.md:dòng |
|---|---|---|
| FR-02.1 | Người dùng nhập Email và Mật khẩu | 40 |
| FR-02.2 | Sai ≥ 3 lần liên tiếp → khoá 30 giây; thông báo lỗi phù hợp, không lộ chi tiết nguyên nhân | 42 |
| FR-02.3 | Đăng nhập thành công: token lưu phía client | 43 |
| FR-02.4 | Trường email phải dùng `type="email"` (validate HTML5) | 44 |
| FR-03.1 | Bước 1: nhập Email đã đăng ký | 50 |
| FR-03.2 | OTP 6 chữ số; demo: hiển thị trên màn hình | 51 |
| FR-03.3 | Phải có Step Indicator, ví dụ "Bước 1 / 2" | 52 |
| FR-03.4 | Có nút **Quay lại đăng nhập** | 53 |
| FR-03.5 | Bước 2: nhập OTP, Mật khẩu mới, **Xác nhận mật khẩu mới** | 57 |
| FR-03.6 | Mật khẩu mới tuân thủ FR-01 (≥ 8 ký tự, hoa, thường, số, ký tự đặc biệt `@$!%*?&`) | 58, 34 |
| FR-03.7 | Hai trường mật khẩu phải khớp | 59 |
| FR-04.1 | Cập nhật được Họ Tên, Số điện thoại, Địa chỉ giao hàng mặc định | 64 |
| FR-04.2 | SĐT hợp lệ: bắt đầu bằng `0`, 10–11 chữ số | 65 |
| FR-04.3 | Email không được đổi qua giao diện | 66 |
| FR-11.1 | Hiển thị Mã đơn, Ngày đặt, Tổng tiền, Trạng thái hiện tại | 167 |
| FR-11.2 | Trạng thái dịch sang tiếng Việt rõ ràng và phân biệt màu sắc | 168 |
| FR-10.x | Ở `shipping` User không được tự hủy; `delivered`/`canceled` là trạng thái kết thúc | 160–161 |
| FR-21.1 | Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn) | 244 |
| FR-21.2 | Nút tích cực màu xanh dương; nút nguy hiểm/hủy bỏ màu đỏ | 245 |
| FR-21.3 | Tiền luôn dùng `₫` với phân cách hàng nghìn | 246 |
| FR-21.4 | Mỗi trang có đúng 1 `<h1>` mô tả nội dung trang | 247 |
| FR-21.5 | Tab Order từ trên xuống dưới, trái sang phải | 248 |
| FR-22.1 | Trường bắt buộc có `*` cạnh nhãn | 252 |
| FR-22.2 | Trường Email dùng `type="email"` | 253 |
| FR-22.3 | Trường Mật khẩu dùng `type="password"` | 254 |
| FR-22.4 | Thông báo lỗi xuất hiện **trên** nút submit | 255 |
| FR-22.5 | Form ≥ 2 bước phải có Step Indicator rõ ràng | 256 |
| FR-23.1 | Navbar highlight trang đang chọn | 260 |
| FR-23.2 | Link "Giỏ hàng" có badge số lượng | 261 |
| FR-23.3 | Nút Đăng xuất nhãn "Đăng xuất" (không phải "Thoát") | 262 |
| FR-23.4 | Breadcrumb ở trang con (Giỏ hàng, Thanh toán, Chi tiết SP) — **không** gồm màn C2 | 263 |
| FR-24.3 | Empty State có icon/hình minh hoạ và message thân thiện | 269 |
| SEC-04 | Dữ liệu người dùng nhập hiển thị trên UI phải được escape, không dùng `innerHTML` | 281 |

FR-24.1/24.2/24.4 (thêm giỏ, xoá item giỏ, alt ảnh sản phẩm) và FR-23.4 không thuộc màn C2 → không sinh item.
