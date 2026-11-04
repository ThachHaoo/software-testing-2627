# RUN – chạy tay checklist C2 (T1 bước 3, sinh bằng `HW03/tests/gen_run.py`)

Nguồn: `checklist.json` (v2 – chốt sau review SV); 74 item. Phần tự động (Playwright, P1 Chrome + P2 Firefox của Playwright) chạy trước, ghi `auto_status`; **verdict chính thức = lượt chạy tay trên trình duyệt thật** (report_plan E2). Expected không đổi; procedure sai → sửa RUN.md trước khi chạy.

## 1. Mỗi nền tảng = 1 lượt

1. Restart backend: dừng `node server.js` rồi `cd ..\eshop-sut\backend; node server.js` (CSDL seed lại). Web: `cd ..\eshop-sut\frontend-web; npx vite --host 127.0.0.1 --port 5173`.
2. Ghi phiên bản trình duyệt + OS (+ máy) vào đầu file kết quả.
3. Làm Bước A → Bước B → M1…M6 → Cuối lượt, theo bảng của nền tảng đó (mục 4).
4. Item đổi mật khẩu (CL-27, CL-29, CL-48, SV-06): xong thì `python HW03/tests/seed_orders.py --restore-password`.
5. Item đổi hồ sơ: xong thì trả Họ Tên `Test User`, xoá SĐT/địa chỉ.
6. **Cảnh báo (gray-box, `backend/server.js:54–57`):** mỗi lần sai mật khẩu bộ đếm tăng 2, ≥ 3 là khoá **180 giây** → sau một lần đăng nhập sai, đăng nhập đúng ngay để đưa bộ đếm về 0. CL-52 làm cuối lượt.

**P3 (Chrome Android, POCO F5):**

```powershell
D:\Tools\platform-tools\adb.exe devices          # phải là "<serial>  device"
D:\Tools\platform-tools\adb.exe reverse tcp:5173 tcp:5173
D:\Tools\platform-tools\adb.exe reverse tcp:3000 tcp:3000
D:\Tools\platform-tools\adb.exe reverse --list
```

Mở `http://localhost:5173` trên Chrome điện thoại. Item cần DOM/đo (h1, type, toạ độ, màu…): PC mở `chrome://inspect` → *inspect* tab của điện thoại → Console, dán `HW03/checklist/dom_probe.js`, chép JSON vào file kết quả. Rút cáp / restart adb → chạy lại 2 lệnh `reverse`.

## 2. Ảnh

- Overlay trên MỌI ảnh: `23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn`. PC: cửa sổ Sticky Notes ghi dòng này, chụp **toàn màn hình** (thấy tên trình duyệt + URL). Điện thoại: chụp rồi thêm chữ bằng trình sửa ảnh của máy ngay sau khi chụp (thấy thanh URL).
- Bắt buộc: (a) mỗi item **Failed**: `P<n>_<id>_<k>.png` (vd `P1_CL-22_1.png`); (b) Task 3: **1 ảnh tổng quan mỗi màn / nền tảng**: `P<n>_M<k>_1.png` (M1…M5).
- Không chụp: item Passed, N/A.
- Thư mục: `HW03/checklist/evidence/P1_chrome/`, `P2_firefox/`, `P3_android/`. Mỗi file ≤ 20 MB.

## 3. Ghi kết quả

Ghi vào bản sao của `runs/<P>_manual_TEMPLATE.md` → `runs/<P>_manual_<YYYYMMDD-HHMM>.md`: mỗi item một dòng `status` (Passed / Failed / N/A / Blocked) + notes (Failed: Actual nguyên văn; Blocked: item gốc) + tên ảnh. AI chép sang CSV và gộp bằng `merge_platform.py`.

## 4. Bảng theo nền tảng

### P1 – Chrome trên Windows (15 item chạy tay)

#### Bước A – ngay sau khi restart backend (tài khoản chưa có đơn)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-62 | Lịch sử đơn | Empty state có hình minh hoạ và thông báo thân thiện | Backend vừa restart (test@eshop.com chưa có đơn). | Phần chạy tay: auto: có img/svg/icon trong khu lịch sử đơn + có câu thông báo; 'thân thiện' → SV. Phần tự động: xem `runs/P1_auto_*.json`. |

**Bước B – dựng đơn:** `python HW03/tests/seed_orders.py` → ghi lại bảng mã đơn ↔ trạng thái vào file kết quả.

#### M1 – Đăng nhập · ảnh tổng quan bắt buộc: `P1_M1_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-53 | Đăng nhập | Có chỉ báo đang xử lý và chống gửi trùng | P3: throttling qua chrome://inspect. | Phần chạy tay: auto (P1, CDP Slow 3G): nút disabled/đổi chữ/aria-busy + số request; chỉ báo khác → SV; P2 chạy tay. Phần tự động: xem `runs/P1_auto_*.json`. |
| ☐ | SV-01 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Hiển thị con trỏ focus (Focus Ring/Indicator) rõ ràng khi duyệt bằng bàn phím |  | Phần chạy tay: auto: so outline/box-shadow/border lúc có và không có focus; 'rõ ràng' → SV. Phần tự động: xem `runs/P1_auto_*.json`. |
| ☐ | SV-02 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu | Trình duyệt đã lưu thông tin đăng nhập/tài khoản trước đó. | Phần chạy tay: auto (P1): dán bằng Ctrl+V vào ô Email; Autofill + P2 → chạy tay. Phần tự động: xem `runs/P1_auto_*.json`. |
| ☐ | SV-04 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) |  | Phần chạy tay: auto: tỉ lệ tương phản chữ/nền tính từ màu CSS; placeholder + Lighthouse → SV. Phần tự động: xem `runs/P1_auto_*.json`. |

#### M2 – Quên mật khẩu (B1, B2) · ảnh tổng quan bắt buộc: `P1_M2_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-06 | Quên mật khẩu (bước 2) | Nút chính và nút phụ phân biệt được bằng hình thức |  | Phần chạy tay: auto: Fail khi hai nút trùng cả màu nền, kích thước, viền; khác nhau → SV xác nhận 'khác nhau rõ'. Phần tự động: xem `runs/P1_auto_*.json`. |
| ☐ | CL-24 | Quên mật khẩu | Có chỉ báo bước (Step Indicator) |  | Phần chạy tay: auto: tìm chữ 'Bước k / 2'; không thấy → SV xác nhận không có chỉ báo tương đương. Phần tự động: xem `runs/P1_auto_*.json`. |

#### M3 – Hồ sơ · ảnh tổng quan bắt buộc: `P1_M3_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-11 | Hồ sơ | Thứ tự Tab theo vị trí hiển thị (trên→dưới, trái→phải) | Có ≥ 1 đơn Chờ xác nhận. | Phần chạy tay: auto: thứ tự theo toạ độ; bố cục 2 cột → SV đọc chuỗi Tab trong notes để xác nhận 'cùng hàng'. Phần tự động: xem `runs/P1_auto_*.json`. |

#### M4 – Lịch sử đơn · ảnh tổng quan bắt buộc: `P1_M4_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-08 | Lịch sử đơn | Tổng tiền dùng ký hiệu ₫ và phân cách hàng nghìn | Có ≥ 1 đơn (tạo qua Checkout). | Phần chạy tay: auto: định dạng trên từng nền tảng; so kiểu phân cách giữa P1/P2/P3 khi gộp (P3 chạy tay). Phần tự động: xem `runs/P1_auto_*.json`. |
| ☐ | CL-09 | Lịch sử đơn | Ngày đặt hiển thị nhất quán theo định dạng Việt Nam | Có ≥ 1 đơn. | Phần chạy tay: auto: định dạng trên từng nền tảng; so giữa P1/P2/P3 khi gộp. Phần tự động: xem `runs/P1_auto_*.json`. |
| ☐ | CL-15 | Hồ sơ + Lịch sử đơn | Bố cục không vỡ ở màn hình hẹp | Có ≥ 1 đơn. | Phần chạy tay: auto: thanh cuộn ngang toàn trang; phần tử bị cắt/chồng → SV xem ảnh. Phần tự động: xem `runs/P1_auto_*.json`. |
| ☐ | CL-63 | Lịch sử đơn | Có trạng thái đang tải khi lấy lịch sử đơn | Có ≥ 1 đơn. P3: throttling qua chrome://inspect. | Phần chạy tay: auto (P1, CDP Slow 3G): empty state hiện trước khi dữ liệu về / có chỉ báo tải; P2 chạy tay. Phần tự động: xem `runs/P1_auto_*.json`. |

#### M6 – Chung – tất cả màn C2 · ảnh tổng quan bắt buộc: `P1_M6_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-01 | Tất cả màn C2 | Ngôn ngữ giao diện nhất quán tiếng Việt |  | Mọi nhãn, nút, tiêu đề, placeholder, thông báo trên Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ, Lịch sử đơn, navbar đều bằng tiếng Việt. Fail nếu có ≥ 1 chuỗi tiếng Anh không phải thuật ngữ kỹ thuật chuẩn (chấp nhận: Email, OTP, EShop). |

#### Cuối lượt (khoá tài khoản / tắt backend – làm sau cùng)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-52 | Đăng nhập | Sai 3 lần liên tiếp → khoá 30 giây | Restart backend trước khi kiểm (bộ đếm = 0). | Sai mật khẩu 3 lần liên tiếp, ngay sau đó đăng nhập đúng → bị từ chối kèm thông báo; chờ 30 giây (+ 5 giây dung sai) đăng nhập đúng → thành công. Fail nếu lần đúng ngay sau đó thành công, hoặc sau 35 giây vẫn bị từ chối. |
| ☐ | CL-64 | Hồ sơ | Lỗi kết nối khi cập nhật có thông báo dễ hiểu, không mất dữ liệu | Khởi động lại backend sau khi kiểm (CSDL seed lại). | Tắt backend, bấm Cập nhật → thông báo tiếng Việt cho biết không kết nối được máy chủ / thử lại; dữ liệu đã nhập trong form vẫn còn. Fail nếu thông báo chung chung không nêu nguyên nhân hoặc form bị xoá. |

### P2 – Firefox trên Windows (15 item chạy tay)

#### Bước A – ngay sau khi restart backend (tài khoản chưa có đơn)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-62 | Lịch sử đơn | Empty state có hình minh hoạ và thông báo thân thiện | Backend vừa restart (test@eshop.com chưa có đơn). | Phần chạy tay: auto: có img/svg/icon trong khu lịch sử đơn + có câu thông báo; 'thân thiện' → SV. Phần tự động: xem `runs/P2_auto_*.json`. |

**Bước B – dựng đơn:** `python HW03/tests/seed_orders.py` → ghi lại bảng mã đơn ↔ trạng thái vào file kết quả.

#### M1 – Đăng nhập · ảnh tổng quan bắt buộc: `P2_M1_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-53 | Đăng nhập | Có chỉ báo đang xử lý và chống gửi trùng | P3: throttling qua chrome://inspect. | DevTools Network throttling 'Slow 3G': bấm Đăng nhập → trong lúc chờ, nút bị vô hiệu hoá hoặc có chỉ báo đang tải; bấm thêm 2 lần chỉ phát sinh 1 request /api/login. Fail nếu không có chỉ báo hoặc phát sinh nhiều request. |
| ☐ | SV-01 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Hiển thị con trỏ focus (Focus Ring/Indicator) rõ ràng khi duyệt bằng bàn phím |  | Phần chạy tay: auto: so outline/box-shadow/border lúc có và không có focus; 'rõ ràng' → SV. Phần tự động: xem `runs/P2_auto_*.json`. |
| ☐ | SV-02 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu | Trình duyệt đã lưu thông tin đăng nhập/tài khoản trước đó. | Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit. Fail nếu bất kỳ vế nào (dán hoặc autofill) bị hệ thống ngăn chặn/làm sai lệch dữ liệu. |
| ☐ | SV-04 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) |  | Phần chạy tay: auto: tỉ lệ tương phản chữ/nền tính từ màu CSS; placeholder + Lighthouse → SV. Phần tự động: xem `runs/P2_auto_*.json`. |

#### M2 – Quên mật khẩu (B1, B2) · ảnh tổng quan bắt buộc: `P2_M2_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-06 | Quên mật khẩu (bước 2) | Nút chính và nút phụ phân biệt được bằng hình thức |  | Phần chạy tay: auto: Fail khi hai nút trùng cả màu nền, kích thước, viền; khác nhau → SV xác nhận 'khác nhau rõ'. Phần tự động: xem `runs/P2_auto_*.json`. |
| ☐ | CL-24 | Quên mật khẩu | Có chỉ báo bước (Step Indicator) |  | Phần chạy tay: auto: tìm chữ 'Bước k / 2'; không thấy → SV xác nhận không có chỉ báo tương đương. Phần tự động: xem `runs/P2_auto_*.json`. |

#### M3 – Hồ sơ · ảnh tổng quan bắt buộc: `P2_M3_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-11 | Hồ sơ | Thứ tự Tab theo vị trí hiển thị (trên→dưới, trái→phải) | Có ≥ 1 đơn Chờ xác nhận. | Phần chạy tay: auto: thứ tự theo toạ độ; bố cục 2 cột → SV đọc chuỗi Tab trong notes để xác nhận 'cùng hàng'. Phần tự động: xem `runs/P2_auto_*.json`. |

#### M4 – Lịch sử đơn · ảnh tổng quan bắt buộc: `P2_M4_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-08 | Lịch sử đơn | Tổng tiền dùng ký hiệu ₫ và phân cách hàng nghìn | Có ≥ 1 đơn (tạo qua Checkout). | Phần chạy tay: auto: định dạng trên từng nền tảng; so kiểu phân cách giữa P1/P2/P3 khi gộp (P3 chạy tay). Phần tự động: xem `runs/P2_auto_*.json`. |
| ☐ | CL-09 | Lịch sử đơn | Ngày đặt hiển thị nhất quán theo định dạng Việt Nam | Có ≥ 1 đơn. | Phần chạy tay: auto: định dạng trên từng nền tảng; so giữa P1/P2/P3 khi gộp. Phần tự động: xem `runs/P2_auto_*.json`. |
| ☐ | CL-15 | Hồ sơ + Lịch sử đơn | Bố cục không vỡ ở màn hình hẹp | Có ≥ 1 đơn. | Phần chạy tay: auto: thanh cuộn ngang toàn trang; phần tử bị cắt/chồng → SV xem ảnh. Phần tự động: xem `runs/P2_auto_*.json`. |
| ☐ | CL-63 | Lịch sử đơn | Có trạng thái đang tải khi lấy lịch sử đơn | Có ≥ 1 đơn. P3: throttling qua chrome://inspect. | Network throttling 'Slow 3G', tải lại /profile → trong lúc chờ có chỉ báo đang tải; không hiện 'chưa có đơn hàng' trước khi dữ liệu về. Fail nếu hiện empty state rồi mới hiện bảng. |

#### M6 – Chung – tất cả màn C2 · ảnh tổng quan bắt buộc: `P2_M6_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-01 | Tất cả màn C2 | Ngôn ngữ giao diện nhất quán tiếng Việt |  | Mọi nhãn, nút, tiêu đề, placeholder, thông báo trên Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ, Lịch sử đơn, navbar đều bằng tiếng Việt. Fail nếu có ≥ 1 chuỗi tiếng Anh không phải thuật ngữ kỹ thuật chuẩn (chấp nhận: Email, OTP, EShop). |

#### Cuối lượt (khoá tài khoản / tắt backend – làm sau cùng)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-52 | Đăng nhập | Sai 3 lần liên tiếp → khoá 30 giây | Restart backend trước khi kiểm (bộ đếm = 0). | Sai mật khẩu 3 lần liên tiếp, ngay sau đó đăng nhập đúng → bị từ chối kèm thông báo; chờ 30 giây (+ 5 giây dung sai) đăng nhập đúng → thành công. Fail nếu lần đúng ngay sau đó thành công, hoặc sau 35 giây vẫn bị từ chối. |
| ☐ | CL-64 | Hồ sơ | Lỗi kết nối khi cập nhật có thông báo dễ hiểu, không mất dữ liệu | Khởi động lại backend sau khi kiểm (CSDL seed lại). | Tắt backend, bấm Cập nhật → thông báo tiếng Việt cho biết không kết nối được máy chủ / thử lại; dữ liệu đã nhập trong form vẫn còn. Fail nếu thông báo chung chung không nêu nguyên nhân hoặc form bị xoá. |

### P3 – Chrome Android (POCO F5, adb reverse) (70 item chạy tay)

#### Bước A – ngay sau khi restart backend (tài khoản chưa có đơn)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-62 | Lịch sử đơn | Empty state có hình minh hoạ và thông báo thân thiện | Backend vừa restart (test@eshop.com chưa có đơn). | Tài khoản chưa có đơn → khu Lịch sử đơn có icon/hình minh hoạ và câu thông báo thân thiện (kèm gợi ý mua sắm). Fail nếu chỉ có chữ, không có icon/hình. |

**Bước B – dựng đơn:** `python HW03/tests/seed_orders.py` → ghi lại bảng mã đơn ↔ trạng thái vào file kết quả.

#### M1 – Đăng nhập · ảnh tổng quan bắt buộc: `P3_M1_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-02 | Đăng nhập, Quên mật khẩu, Hồ sơ | Mỗi trang có đúng 1 thẻ <h1> | P3: mở DevTools qua chrome://inspect (adb). | Trên mỗi trang /login, /forgot-password, /profile, lệnh DevTools `document.querySelectorAll('h1').length` trả về đúng 1. Fail nếu một trang trả 0 hoặc ≥ 2. |
| ☐ | CL-03 | Đăng nhập | Tiêu đề trang mô tả đúng chức năng Đăng nhập |  | Tiêu đề chính hiển thị trên /login có nội dung 'Đăng nhập'. Fail nếu tiêu đề là chức năng khác (vd 'Đăng ký') hoặc không có tiêu đề. |
| ☐ | CL-17 | Đăng nhập, Quên mật khẩu (bước 1) | Ô Email dùng type="email" |  | DevTools: ô Email trên /login và bước 1 /forgot-password có type="email". Fail nếu type khác "email". |
| ☐ | CL-66 | Đăng nhập, Quên mật khẩu (bước 1) | Email sai định dạng bị chặn trước khi gửi |  | Nhập 'abc' vào ô Email rồi submit → form bị chặn, có thông báo validate, DevTools Network không có request gửi đi. Fail nếu form gửi request. |
| ☐ | CL-18 | Đăng nhập | Nhãn ô đăng nhập là 'Email' |  | Nhãn ô thứ nhất trên /login là 'Email' (hoặc chứa từ 'Email'). Fail nếu nhãn là thuật ngữ khác (vd 'Username', 'Tên đăng nhập'). |
| ☐ | CL-19 | Đăng nhập, Quên mật khẩu (bước 2) | Ô mật khẩu che ký tự |  | Mọi ô mật khẩu (Đăng nhập; Mật khẩu mới, Xác nhận mật khẩu ở bước 2) có type="password": gõ 'Abc123!' chỉ thấy ký tự che (•). Fail nếu một ô hiển thị rõ ký tự. |
| ☐ | CL-20 | Đăng nhập, Quên mật khẩu | Dấu * trên nhãn trường bắt buộc |  | Nhãn Email, Mật khẩu (/login); Email (bước 1); OTP, Mật khẩu mới, Xác nhận mật khẩu (bước 2) đều có '*' cạnh nhãn. Fail nếu ≥ 1 nhãn thiếu '*'. |
| ☐ | CL-22 | Đăng nhập | Thông báo lỗi đăng nhập nằm phía trên nút submit |  | Đăng nhập với mật khẩu sai: khối thông báo lỗi xuất hiện phía trên nút Đăng nhập (toạ độ y của thông báo < y của nút). Fail nếu thông báo nằm dưới nút hoặc không hiện. |
| ☐ | CL-35 | Đăng nhập | Giữ lại Email sau khi đăng nhập thất bại |  | Sau một lần đăng nhập sai mật khẩu, ô Email vẫn giữ giá trị đã nhập. Fail nếu ô Email bị xoá. |
| ☐ | CL-36 | Đăng nhập | Phím Enter gửi form đăng nhập |  | Con trỏ ở ô Mật khẩu, bấm Enter (P3: phím Go/Enter của bàn phím ảo) → form được gửi như bấm nút Đăng nhập. Fail nếu không có gì xảy ra. |
| ☐ | CL-38 | Đăng nhập, Hồ sơ | Nhãn gắn với ô nhập (bấm nhãn → focus ô) |  | Bấm vào chữ nhãn (vd 'Mật khẩu', 'Họ Tên') → con trỏ nhảy vào ô tương ứng. Fail nếu bấm nhãn không có tác dụng. |
| ☐ | CL-44 | Đăng nhập | Đăng nhập thành công rời trang đăng nhập và navbar cập nhật |  | Đăng nhập test@eshop.com/Test1234! → trong ≤ 1 giây rời /login và navbar hiển thị tên người dùng thay cho 'Đăng nhập'. Fail nếu vẫn ở /login, quá 1 giây, hoặc navbar không đổi. |
| ☐ | CL-45 | Đăng nhập | Link 'Quên mật khẩu?' tới đúng /forgot-password |  | Bấm 'Quên mật khẩu?' → URL là /forgot-password và trang hiển thị form Quên mật khẩu. Fail nếu sai trang hoặc không chuyển trang. |
| ☐ | CL-46 | Đăng nhập | Link 'Đăng ký ngay' tới trang Đăng ký |  | Bấm 'Đăng ký ngay' → URL /register và trang hiển thị form đăng ký. Fail nếu sai trang. |
| ☐ | CL-51 | Đăng nhập | Thông báo đăng nhập sai không lộ nguyên nhân |  | Đăng nhập (a) email không tồn tại, (b) email đúng + mật khẩu sai → hai thông báo giống hệt nhau, không nói trường nào sai. Fail nếu thông báo khác nhau hoặc chỉ rõ 'email không tồn tại'/'sai mật khẩu'. |
| ☐ | CL-53 | Đăng nhập | Có chỉ báo đang xử lý và chống gửi trùng | P3: throttling qua chrome://inspect. | DevTools Network throttling 'Slow 3G': bấm Đăng nhập → trong lúc chờ, nút bị vô hiệu hoá hoặc có chỉ báo đang tải; bấm thêm 2 lần chỉ phát sinh 1 request /api/login. Fail nếu không có chỉ báo hoặc phát sinh nhiều request. |
| ☐ | SV-02 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu | Trình duyệt đã lưu thông tin đăng nhập/tài khoản trước đó. | Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit. Fail nếu bất kỳ vế nào (dán hoặc autofill) bị hệ thống ngăn chặn/làm sai lệch dữ liệu. |
| ☐ | SV-03 | Đăng nhập, Quên mật khẩu B2, Hồ sơ | Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại |  | Nhập dữ liệu sai quy tắc (ví dụ: SĐT sai định dạng ở Hồ sơ hoặc Mật khẩu mới không đủ điều kiện ở Quên mật khẩu B2) rồi bấm submit: sau khi thông báo lỗi xuất hiện, con trỏ gõ phím (cursor) phải tự động quay lại focus ở đúng ô bị lỗi đó. Fail nếu con trỏ nhảy mất focus hoặc không quay lại ô nhập bị lỗi. |
| ☐ | SV-04 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) |  | Kiểm tra bằng công cụ DevTools Accessibility / Lighthouse: tỉ lệ tương phản màu sắc của chữ (văn bản, label, placeholder, text trên button) so với màu nền đạt tối thiểu 4.5:1 (đối với chữ thường). Fail nếu tỉ lệ tương phản < 4.5:1 khiến chữ mờ khó đọc. |
| ☐ | SV-05 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Kích thước vùng tương tác của con trỏ (Target Size) đối với các nút và link |  | Dùng thước đo DevTools kiểm tra chiều cao và chiều rộng vùng bấm của các nút ('Sign In', 'Lấy mã OTP', 'Cập nhật') và các liên kết ('Quên mật khẩu?', 'Đăng ký ngay'): vùng bấm nhận con trỏ (chuột hoặc ngón tay) phải đạt kích thước tối thiểu 24x24 px. Fail nếu có nút/link kích thước < 24x24 px. |

#### M2 – Quên mật khẩu (B1, B2) · ảnh tổng quan bắt buộc: `P3_M2_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-06 | Quên mật khẩu (bước 2) | Nút chính và nút phụ phân biệt được bằng hình thức |  | Nút 'Đặt lại mật khẩu' (chính) và nút quay lại (phụ) khác nhau rõ về màu hoặc kiểu (viền/nền). Fail nếu hai nút cùng màu nền, cùng kích thước, cùng kiểu. |
| ☐ | CL-07 | Quên mật khẩu (bước 2) | Các nút trên cùng form đồng nhất kích thước và font |  | Các nút trên cùng form có cùng chiều cao (chênh ≤ 2 px theo DevTools) và cùng font-family/font-size. Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size. |
| ☐ | CL-23 | Quên mật khẩu, Hồ sơ | Thông báo lỗi validate hiển thị trong trang, phía trên nút submit |  | Gây lỗi: mật khẩu mới yếu (bước 2), SĐT sai định dạng (Hồ sơ). Thông báo lỗi xuất hiện trong trang, phía trên nút submit của form đó. Fail nếu lỗi hiện dưới nút hoặc chỉ hiện ở hộp thoại trình duyệt (alert) không gắn với vị trí nào trong form. |
| ☐ | CL-24 | Quên mật khẩu | Có chỉ báo bước (Step Indicator) |  | Bước 1 hiển thị 'Bước 1 / 2' (hoặc chỉ báo tương đương thấy rõ bước hiện tại và tổng số bước); bước 2 hiển thị 'Bước 2 / 2'. Fail nếu một bước không có chỉ báo. |
| ☐ | CL-25 | Quên mật khẩu (bước 1) | Có nút 'Quay lại đăng nhập' |  | Bước 1 có nút/link nhãn 'Quay lại đăng nhập'; bấm → về /login. Fail nếu không có, nhãn khác nghĩa, hoặc không về /login. |
| ☐ | CL-26 | Quên mật khẩu (bước 2) | Có ô 'Xác nhận mật khẩu mới' |  | Bước 2 có đủ 3 ô: OTP, Mật khẩu mới, Xác nhận mật khẩu mới. Fail nếu thiếu ô xác nhận. |
| ☐ | CL-27 | Quên mật khẩu (bước 2) | Hai mật khẩu không khớp bị chặn |  | Nhập Mật khẩu mới 'Abcdef1!' và Xác nhận 'Abcdef2!' rồi submit → không đổi mật khẩu, có thông báo hai mật khẩu không khớp. Fail nếu đổi thành công. Blocked nếu item 'Có ô Xác nhận mật khẩu mới' Failed. |
| ☐ | CL-28 | Quên mật khẩu (bước 2) | Mã OTP hiển thị có đúng 6 chữ số |  | Sau khi gửi email ở bước 1, mã OTP hiển thị trên màn hình có đúng 6 chữ số. Fail nếu mã có số chữ số khác 6. |
| ☐ | CL-29 | Quên mật khẩu (bước 2) | Mật khẩu mới hợp lệ theo FR-01 được chấp nhận | Dùng tài khoản test@eshop.com; restart backend sau khi kiểm để khôi phục mật khẩu Test1234!. | Với OTP đúng, Mật khẩu mới 'Abcdef1!' (8 ký tự, có hoa, thường, số, '!') → đổi thành công; đăng nhập lại bằng mật khẩu mới được. Fail nếu bị báo mật khẩu yếu. |
| ☐ | CL-30 | Quên mật khẩu (bước 2) | Mật khẩu yếu bị từ chối với thông báo nêu đúng quy tắc |  | Mật khẩu mới 'abcdefgh' bị từ chối; thông báo nêu quy tắc khớp FR-01 (≥ 8 ký tự, chữ hoa, chữ thường, số, ký tự đặc biệt). Fail nếu được chấp nhận hoặc thông báo nêu quy tắc khác SRS. |
| ☐ | CL-39 | Quên mật khẩu | Quay lại bước 1 vẫn giữ email đã nhập |  | Từ bước 2 bấm nút quay lại → bước 1 hiển thị lại email vừa nhập. Fail nếu ô email rỗng. |
| ☐ | CL-48 | Quên mật khẩu | Đặt lại mật khẩu thành công có lối đi tới đăng nhập | Restart backend sau khi kiểm. | Sau khi đổi mật khẩu thành công, người dùng được chuyển tới /login hoặc thấy link/nút tới Đăng nhập. Fail nếu ở lại form mà không có lối tới Đăng nhập. |
| ☐ | CL-54 | Quên mật khẩu (bước 2) | OTP hiển thị trên màn hình (môi trường demo) |  | Sau khi gửi email test@eshop.com ở bước 1, bước 2 hiển thị mã OTP rõ ràng trên trang. Fail nếu không thấy mã. |
| ☐ | SV-06 | Quên mật khẩu B1 / B2, Hồ sơ | Chống gửi trùng dữ liệu (Debounce/Disable) khi nhấp đúp/nhấp liên tiếp vào nút submit ở điều kiện mạng bình thường |  | Ở điều kiện mạng bình thường (không bật throttling), nhấp chuột thật nhanh (double-click) vào nút 'Lấy mã OTP', 'Đặt lại mật khẩu' hoặc 'Cập nhật': hệ thống lập tức khóa nút hoặc debounce request sao cho chỉ có đúng 1 request API được gửi đi. Fail nếu gửi từ 2 request trở lên hoặc hiển thị nhiều thông báo trùng lặp. |

#### M3 – Hồ sơ · ảnh tổng quan bắt buộc: `P3_M3_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-21 | Hồ sơ | Dấu * trên trường mà form bắt buộc nhập |  | Với từng trường Họ Tên, Số điện thoại, Địa chỉ: để trống rồi bấm Cập nhật. Trường nào khiến form bị chặn thì nhãn phải có '*'; trường không bắt buộc thì không có '*'. Fail nếu một trường bị chặn khi trống mà nhãn không có '*'. |
| ☐ | CL-31 | Hồ sơ | SĐT hợp lệ (bắt đầu 0, 10–11 số) được chấp nhận |  | Lần lượt nhập '0912345678' (10 số) và '09123456789' (11 số), bấm Cập nhật → mỗi lần thành công, tải lại trang thấy giá trị đã lưu. Fail nếu một trong hai bị từ chối. |
| ☐ | CL-32 | Hồ sơ | SĐT không hợp lệ bị từ chối, thông báo nêu đúng quy tắc |  | Nhập '912345678' (không bắt đầu bằng 0) → bị từ chối, không lưu; thông báo nêu 'bắt đầu bằng 0, 10–11 chữ số'. Fail nếu được lưu hoặc thông báo nêu quy tắc khác SRS. |
| ☐ | CL-33 | Hồ sơ | Email không sửa được và trông như trường bị khoá |  | Ô Email không gõ được và có nền xám như trường bị khoá. Fail nếu sửa được hoặc trông như ô thường. |
| ☐ | CL-34 | Hồ sơ | Họ Tên chỉ gồm khoảng trắng bị từ chối |  | Nhập Họ Tên '   ' (3 dấu cách), bấm Cập nhật → bị chặn với thông báo; tải lại trang, Họ Tên cũ giữ nguyên. Fail nếu lưu thành công. |
| ☐ | CL-37 | Hồ sơ | Cập nhật hồ sơ được lưu bền | Khôi phục giá trị cũ sau khi kiểm. | Đổi Họ Tên, SĐT hợp lệ, Địa chỉ → Cập nhật → tải lại trang (F5) → 3 trường hiển thị giá trị mới. Fail nếu ≥ 1 trường quay về giá trị cũ. |
| ☐ | CL-49 | Hồ sơ | /profile khi chưa đăng nhập dẫn được tới Đăng nhập |  | Chưa đăng nhập, mở /profile → hoặc tự chuyển tới /login, hoặc thông báo có link/nút tới Đăng nhập (1 lần bấm). Fail nếu chỉ có chữ, không có đường tới Đăng nhập ngoài navbar. |
| ☐ | CL-55 | Hồ sơ | Cập nhật thành công có phản hồi rõ ràng |  | Bấm Cập nhật với dữ liệu hợp lệ → trong ≤ 1 giây có thông báo thành công bằng tiếng Việt. Fail nếu không có phản hồi hoặc phản hồi sau 1 giây. |
| ☐ | CL-56 | Hồ sơ, Navbar | Đổi Họ Tên cập nhật ngay trên navbar | Khôi phục 'Test User' sau khi kiểm. | Đổi Họ Tên thành 'Test Đổi' → Cập nhật → navbar hiển thị 'Test Đổi' mà không cần tải lại trang. Fail nếu navbar vẫn tên cũ cho tới khi F5. |

#### M4 – Lịch sử đơn · ảnh tổng quan bắt buộc: `P3_M4_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-05 | Navbar, Lịch sử đơn | Nút nguy hiểm/huỷ bỏ màu đỏ | Có ≥ 1 đơn ở trạng thái Chờ xác nhận (tạo qua Checkout). | Nút Đăng xuất và 'Hủy đơn' có nền đỏ. Fail nếu một trong hai nút không đỏ. |
| ☐ | CL-08 | Lịch sử đơn | Tổng tiền dùng ký hiệu ₫ và phân cách hàng nghìn | Có ≥ 1 đơn (tạo qua Checkout). | Cột Tổng tiền của mọi dòng có ký hiệu '₫' và nhóm 3 chữ số được phân cách (vd 30.000.000 ₫ hoặc 30,000,000 ₫), cùng một kiểu phân cách trên cả 3 nền tảng. Fail nếu thiếu ₫, thiếu phân cách, hoặc kiểu phân cách khác nhau giữa các nền tảng. |
| ☐ | CL-09 | Lịch sử đơn | Ngày đặt hiển thị nhất quán theo định dạng Việt Nam | Có ≥ 1 đơn. | Ngày đặt hiển thị dạng dd/mm/yyyy và giống nhau trên P1, P2, P3. Fail nếu định dạng khác (mm/dd/yyyy, yyyy-mm-dd) hoặc khác nhau giữa các nền tảng. |
| ☐ | CL-15 | Hồ sơ + Lịch sử đơn | Bố cục không vỡ ở màn hình hẹp | Có ≥ 1 đơn. | Ở chiều rộng 360–390 px (P3 thật; P1/P2 thu cửa sổ hoặc DevTools responsive 375 px): trang không có thanh cuộn ngang, không phần tử nào bị cắt/chồng lên nhau; bảng đơn cuộn trong khung riêng hoặc xuống dòng. Fail nếu có cuộn ngang toàn trang hoặc chữ bị che. |
| ☐ | CL-57 | Lịch sử đơn | Bảng đơn hiển thị đủ thông tin | Đặt 1 đơn qua Checkout bằng test@eshop.com. | Sau khi đặt 1 đơn, Lịch sử đơn có dòng mới với đủ 4 thông tin: Mã đơn, Ngày đặt, Tổng tiền, Trạng thái. Fail nếu thiếu thông tin nào. |
| ☐ | CL-58 | Lịch sử đơn | Trạng thái tiếng Việt và phân biệt màu | Dựng một lần, dùng chung cho cả 3 nền tảng: đặt 5 đơn bằng test@eshop.com; dùng admin (:5174, admin@eshop.com) chuyển trạng thái để có đủ Chờ xác nhận, Đã xác nhận, Đang giao, Đã giao, Đã hủy. Không restart backend cho tới khi chạy xong CL-58, CL-59 trên P1, P2, P3. | Các đơn ở 5 trạng thái hiển thị nhãn tiếng Việt (vd Chờ xác nhận, Đã xác nhận, Đang giao, Đã giao, Đã hủy), mỗi trạng thái một màu khác nhau. Fail nếu có nhãn tiếng Anh/mã thô hoặc 2 trạng thái trùng màu. |
| ☐ | CL-59 | Lịch sử đơn | Không cho người dùng huỷ đơn ở trạng thái không được huỷ | Dùng chung bộ đơn 5 trạng thái của CL-58. | Dòng đơn 'Đang giao', 'Đã giao', 'Đã hủy' không có nút 'Hủy đơn' (hoặc nút bị vô hiệu hoá); chỉ 'Chờ xác nhận', 'Đã xác nhận' có. Fail nếu nút dùng được ở trạng thái không được huỷ. |
| ☐ | CL-60 | Lịch sử đơn | Huỷ đơn có hộp xác nhận | Có ≥ 1 đơn Chờ xác nhận. | Bấm 'Hủy đơn' → hiện hộp xác nhận có lựa chọn huỷ thao tác; chọn không → đơn giữ nguyên trạng thái. Fail nếu đơn bị huỷ ngay khi bấm. |
| ☐ | CL-61 | Lịch sử đơn | Sau huỷ, trạng thái cập nhật ngay | Có ≥ 1 đơn Chờ xác nhận. | Huỷ đơn thành công → không cần tải lại, dòng đó đổi sang 'Đã hủy' và nút 'Hủy đơn' biến mất. Fail nếu cần F5 mới thấy thay đổi. |
| ☐ | CL-63 | Lịch sử đơn | Có trạng thái đang tải khi lấy lịch sử đơn | Có ≥ 1 đơn. P3: throttling qua chrome://inspect. | Network throttling 'Slow 3G', tải lại /profile → trong lúc chờ có chỉ báo đang tải; không hiện 'chưa có đơn hàng' trước khi dữ liệu về. Fail nếu hiện empty state rồi mới hiện bảng. |

#### M5 – Navbar · ảnh tổng quan bắt buộc: `P3_M5_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-16 | Navbar | Tên người dùng hiển thị an toàn (không render HTML) | Đăng nhập test@eshop.com; khôi phục Họ Tên 'Test User' sau khi kiểm. | Đổi Họ Tên thành `<b>Test</b>` rồi Cập nhật, tải lại trang: navbar hiển thị nguyên văn chuỗi `<b>Test</b>` (thấy dấu < >), chữ không in đậm. Fail nếu chữ 'Test' in đậm hoặc dấu < > biến mất. |
| ☐ | CL-40 | Navbar | Navbar highlight trang đang chọn |  | Ở /profile, link tên người dùng (trỏ tới /profile) có kiểu khác hẳn các link còn lại trên navbar (màu/gạch chân/nền), và kiểu đó mất khi rời /profile. Fail nếu link không khác kiểu hoặc không đổi theo trang hiện tại. |
| ☐ | CL-41 | Navbar | Link 'Giỏ hàng' có badge số lượng | Đăng nhập test@eshop.com; thêm sản phẩm từ trang chi tiết, điều hướng bằng navbar (không tải lại trang). | Thêm 1 sản phẩm vào giỏ (từ trang chi tiết, điều hướng bằng navbar) → cạnh link 'Giỏ hàng' có badge hiển thị số > 0. Fail nếu không có badge hoặc badge không hiển thị số > 0. |
| ☐ | CL-42 | Navbar | Nút đăng xuất có nhãn 'Đăng xuất' |  | Khi đã đăng nhập, nút đăng xuất trên navbar có nhãn đúng 'Đăng xuất'. Fail nếu nhãn khác (vd 'Thoát', 'Logout'). |
| ☐ | CL-43 | Navbar | Đăng xuất: navbar về trạng thái chưa đăng nhập |  | Bấm Đăng xuất → navbar hiện 'Đăng nhập', 'Đăng ký' và không còn tên người dùng. Fail nếu navbar còn tên người dùng hoặc không có 'Đăng nhập'. |
| ☐ | CL-67 | Navbar | Đăng xuất giữ nguyên sau khi tải lại trang |  | Sau khi Đăng xuất, tải lại trang (F5) → vẫn ở trạng thái chưa đăng nhập (navbar có 'Đăng nhập'). Fail nếu tự đăng nhập lại. |
| ☐ | CL-68 | Navbar | Sau đăng xuất, /profile không hiển thị dữ liệu tài khoản cũ |  | Sau khi Đăng xuất, mở /profile → không thấy email, họ tên, lịch sử đơn của tài khoản vừa đăng xuất. Fail nếu còn thấy dữ liệu đó. |
| ☐ | CL-47 | Navbar | Logo 'EShop' về trang chủ từ mọi màn C2 |  | Từ /login, /forgot-password, /profile bấm logo → về '/'. Fail nếu một trang không về '/'. |

#### M6 – Chung – tất cả màn C2 · ảnh tổng quan bắt buộc: `P3_M6_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-01 | Tất cả màn C2 | Ngôn ngữ giao diện nhất quán tiếng Việt |  | Mọi nhãn, nút, tiêu đề, placeholder, thông báo trên Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ, Lịch sử đơn, navbar đều bằng tiếng Việt. Fail nếu có ≥ 1 chuỗi tiếng Anh không phải thuật ngữ kỹ thuật chuẩn (chấp nhận: Email, OTP, EShop). |
| ☐ | CL-04 | Tất cả màn C2 | Nút hành động tích cực màu xanh dương |  | Nút 'Đăng nhập/Sign In', 'Lấy mã OTP', 'Đặt lại mật khẩu', 'Cập nhật' có nền xanh dương (họ blue). Fail nếu ≥ 1 nút tích cực có màu khác (xanh lá, xám…). |
| ☐ | CL-13 | Tất cả màn C2 | Tiêu đề tab trình duyệt mô tả trang |  | Tiêu đề tab (document.title) chứa tên ứng dụng hoặc tên trang (vd 'Đăng nhập – EShop') và khác nhau giữa /login, /forgot-password, /profile. Fail nếu không chứa tên ứng dụng/tên trang hoặc giống nhau ở cả 3 trang. |
| ☐ | CL-14 | Tất cả màn C2 | Khai báo ngôn ngữ trang là tiếng Việt |  | Thẻ <html> có lang='vi'. Fail nếu lang khác 'vi' hoặc không có. |
| ☐ | CL-50 | Tất cả màn C2 | URL không tồn tại hiển thị trang 404 có lối về |  | Mở /profil (gõ sai) → trang báo không tìm thấy, có link về trang chủ. Fail nếu trang trắng (chỉ còn header/footer) không có thông báo. |
| ☐ | CL-65 | Tất cả màn C2 | Phiên đăng nhập giữ sau khi tải lại trang |  | Đăng nhập → ở /profile bấm F5 → vẫn đăng nhập, hồ sơ hiển thị, navbar có tên. Fail nếu bị đăng xuất. |

#### Cuối lượt (khoá tài khoản / tắt backend – làm sau cùng)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-52 | Đăng nhập | Sai 3 lần liên tiếp → khoá 30 giây | Restart backend trước khi kiểm (bộ đếm = 0). | Sai mật khẩu 3 lần liên tiếp, ngay sau đó đăng nhập đúng → bị từ chối kèm thông báo; chờ 30 giây (+ 5 giây dung sai) đăng nhập đúng → thành công. Fail nếu lần đúng ngay sau đó thành công, hoặc sau 35 giây vẫn bị từ chối. |
| ☐ | CL-64 | Hồ sơ | Lỗi kết nối khi cập nhật có thông báo dễ hiểu, không mất dữ liệu | Khởi động lại backend sau khi kiểm (CSDL seed lại). | Tắt backend, bấm Cập nhật → thông báo tiếng Việt cho biết không kết nối được máy chủ / thử lại; dữ liệu đã nhập trong form vẫn còn. Fail nếu thông báo chung chung không nêu nguyên nhân hoặc form bị xoá. |

## 5. Nhật ký lượt

| Lượt | Nền tảng | Bắt đầu – kết thúc | Restart backend | Chính thức? | Ghi chú |
|---|---|---|---|---|---|

