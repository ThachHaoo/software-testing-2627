# RUN – chạy tay checklist C2 (T1 bước 3, sinh bằng `HW03/tests/gen_run.py`)

Nguồn: `checklist.json` (v2 – chốt sau review SV); 74 item. Phần tự động (Playwright, P1 Chrome 157 – chỉ tham chiếu vì P1 chạy tay trên Cốc Cốc 160 (Q1) + P2 Firefox của Playwright + P3 Chrome Android thật qua `_android`) chạy trước, ghi `auto_status`; **verdict chính thức = lượt chạy tay trên trình duyệt thật** (report_plan E2). Expected không đổi; procedure sai → sửa RUN.md trước khi chạy.

## 1. Mỗi nền tảng = 1 lượt

1. Restart backend (CSDL seed lại): ở gốc repo chạy `powershell -ExecutionPolicy Bypass -File tools\restart_backend.ps1` (in "backend restart xong: N sản phẩm"). Lượt auto: `npm run p1` / `p2` / `p3` trong `HW03/tests` (đã gồm restart). Web: `cd ..\eshop-sut\frontend-web; npx vite --host 127.0.0.1 --port 5173`.
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

Lượt auto P3: `npx playwright test --project=P3` trong `HW03/tests` (Playwright `_android`; cần adb server đang chạy, điện thoại mở khoá, flag Chrome *Enable command line on non-rooted devices* bật). Playwright sẽ đóng rồi mở lại Chrome trên máy, xoá cookie/storage của `localhost:5173` và `localhost:3000` trước mỗi test.

Chạy tay P3: mở `http://localhost:5173` trên Chrome điện thoại. Item cần DOM/đo (h1, type, toạ độ, màu…): PC mở `chrome://inspect` → *inspect* tab của điện thoại → Console, dán `HW03/checklist/dom_probe.js`, chép JSON vào file kết quả. Rút cáp / restart adb → chạy lại 2 lệnh `reverse`.

## 2. Ảnh

- Overlay trên MỌI ảnh: `23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn`. PC: cửa sổ Sticky Notes ghi dòng này, chụp **toàn màn hình** (thấy tên trình duyệt + URL). Điện thoại: chụp rồi thêm chữ bằng trình sửa ảnh của máy ngay sau khi chụp (thấy thanh URL).
- Bắt buộc: (a) mỗi item **Failed**: `P<n>_<id>_<k>.png` (vd `P1_CL-22_1.png`); (b) Task 3: **1 ảnh tổng quan mỗi màn / nền tảng**: `P<n>_M<k>_1.png` (M1…M5).
- Không chụp: item Passed, N/A.
- Thư mục: `HW03/checklist/evidence/P1_chrome/`, `P2_firefox/`, `P3_android/`. Mỗi file ≤ 20 MB.

## 3. Ghi kết quả

Ghi vào bản sao của `runs/<P>_manual_TEMPLATE.md` → `runs/<P>_manual_<YYYYMMDD-HHMM>.md`: mỗi item một dòng `status` (Passed / Failed / N/A / Blocked) + notes (Failed: Actual nguyên văn; Blocked: item gốc) + tên ảnh. AI chép sang CSV và gộp bằng `merge_platform.py`.

## 4. Bảng theo nền tảng

### P1 – Cốc Cốc (Chromium) trên Windows (15 item chạy tay)

#### Bước A – ngay sau khi restart backend (tài khoản chưa có đơn)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-62 | Lịch sử đơn | Empty state có hình minh hoạ và thông báo thân thiện | Backend vừa restart (test@eshop.com chưa có đơn). | Phần chạy tay: auto: có img/svg/icon trong khu lịch sử đơn + có câu thông báo; 'thân thiện' → SV. Phần tự động: xem `runs/P1_auto_*.json`. |

**Bước B – dựng đơn (lượt cần đơn, ngay sau restart + Bước A):** `python HW03/tests/seed_orders.py` → ghi lại bảng mã đơn ↔ trạng thái vào file kết quả.

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

#### M6 – Chung – tất cả màn C2 · không chụp ảnh tổng quan (M6 là nhóm item chung, không phải một màn – mục 2: M1…M5)

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

**Bước B – dựng đơn (lượt cần đơn, ngay sau restart + Bước A):** `python HW03/tests/seed_orders.py` → ghi lại bảng mã đơn ↔ trạng thái vào file kết quả.

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

#### M6 – Chung – tất cả màn C2 · không chụp ảnh tổng quan (M6 là nhóm item chung, không phải một màn – mục 2: M1…M5)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-01 | Tất cả màn C2 | Ngôn ngữ giao diện nhất quán tiếng Việt |  | Mọi nhãn, nút, tiêu đề, placeholder, thông báo trên Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ, Lịch sử đơn, navbar đều bằng tiếng Việt. Fail nếu có ≥ 1 chuỗi tiếng Anh không phải thuật ngữ kỹ thuật chuẩn (chấp nhận: Email, OTP, EShop). |

#### Cuối lượt (khoá tài khoản / tắt backend – làm sau cùng)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-52 | Đăng nhập | Sai 3 lần liên tiếp → khoá 30 giây | Restart backend trước khi kiểm (bộ đếm = 0). | Sai mật khẩu 3 lần liên tiếp, ngay sau đó đăng nhập đúng → bị từ chối kèm thông báo; chờ 30 giây (+ 5 giây dung sai) đăng nhập đúng → thành công. Fail nếu lần đúng ngay sau đó thành công, hoặc sau 35 giây vẫn bị từ chối. |
| ☐ | CL-64 | Hồ sơ | Lỗi kết nối khi cập nhật có thông báo dễ hiểu, không mất dữ liệu | Khởi động lại backend sau khi kiểm (CSDL seed lại). | Tắt backend, bấm Cập nhật → thông báo tiếng Việt cho biết không kết nối được máy chủ / thử lại; dữ liệu đã nhập trong form vẫn còn. Fail nếu thông báo chung chung không nêu nguyên nhân hoặc form bị xoá. |

### P3 – Chrome Android (POCO F5, adb reverse) (13 item chạy tay)

#### Bước A – ngay sau khi restart backend (tài khoản chưa có đơn)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-62 | Lịch sử đơn | Empty state có hình minh hoạ và thông báo thân thiện | Backend vừa restart (test@eshop.com chưa có đơn). | Phần chạy tay: auto: có img/svg/icon trong khu lịch sử đơn + có câu thông báo; 'thân thiện' → SV. Phần tự động: xem `runs/P3_auto_*.json`. |

**Bước B – dựng đơn (lượt cần đơn, ngay sau restart + Bước A):** `python HW03/tests/seed_orders.py` → ghi lại bảng mã đơn ↔ trạng thái vào file kết quả.

#### M1 – Đăng nhập · ảnh tổng quan bắt buộc: `P3_M1_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-53 | Đăng nhập | Có chỉ báo đang xử lý và chống gửi trùng | P3: throttling qua chrome://inspect. | DevTools Network throttling 'Slow 3G': bấm Đăng nhập → trong lúc chờ, nút bị vô hiệu hoá hoặc có chỉ báo đang tải; bấm thêm 2 lần chỉ phát sinh 1 request /api/login. Fail nếu không có chỉ báo hoặc phát sinh nhiều request. |
| ☐ | SV-02 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu | Trình duyệt đã lưu thông tin đăng nhập/tài khoản trước đó. | Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit. Fail nếu bất kỳ vế nào (dán hoặc autofill) bị hệ thống ngăn chặn/làm sai lệch dữ liệu. |
| ☐ | SV-04 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) |  | Phần chạy tay: auto: tỉ lệ tương phản chữ/nền tính từ màu CSS; placeholder + Lighthouse → SV. Phần tự động: xem `runs/P3_auto_*.json`. |

#### M2 – Quên mật khẩu (B1, B2) · ảnh tổng quan bắt buộc: `P3_M2_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-06 | Quên mật khẩu (bước 2) | Nút chính và nút phụ phân biệt được bằng hình thức |  | Phần chạy tay: auto: Fail khi hai nút trùng cả màu nền, kích thước, viền; khác nhau → SV xác nhận 'khác nhau rõ'. Phần tự động: xem `runs/P3_auto_*.json`. |
| ☐ | CL-24 | Quên mật khẩu | Có chỉ báo bước (Step Indicator) |  | Phần chạy tay: auto: tìm chữ 'Bước k / 2'; không thấy → SV xác nhận không có chỉ báo tương đương. Phần tự động: xem `runs/P3_auto_*.json`. |

#### M4 – Lịch sử đơn · ảnh tổng quan bắt buộc: `P3_M4_1.png`

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-08 | Lịch sử đơn | Tổng tiền dùng ký hiệu ₫ và phân cách hàng nghìn | Có ≥ 1 đơn (tạo qua Checkout). | Phần chạy tay: auto: định dạng trên từng nền tảng; so kiểu phân cách giữa P1/P2/P3 khi gộp (P3 chạy tay). Phần tự động: xem `runs/P3_auto_*.json`. |
| ☐ | CL-09 | Lịch sử đơn | Ngày đặt hiển thị nhất quán theo định dạng Việt Nam | Có ≥ 1 đơn. | Phần chạy tay: auto: định dạng trên từng nền tảng; so giữa P1/P2/P3 khi gộp. Phần tự động: xem `runs/P3_auto_*.json`. |
| ☐ | CL-15 | Hồ sơ + Lịch sử đơn | Bố cục không vỡ ở màn hình hẹp | Có ≥ 1 đơn. | Phần chạy tay: auto: thanh cuộn ngang toàn trang; phần tử bị cắt/chồng → SV xem ảnh. Phần tự động: xem `runs/P3_auto_*.json`. |
| ☐ | CL-63 | Lịch sử đơn | Có trạng thái đang tải khi lấy lịch sử đơn | Có ≥ 1 đơn. P3: throttling qua chrome://inspect. | Network throttling 'Slow 3G', tải lại /profile → trong lúc chờ có chỉ báo đang tải; không hiện 'chưa có đơn hàng' trước khi dữ liệu về. Fail nếu hiện empty state rồi mới hiện bảng. |

#### M6 – Chung – tất cả màn C2 · không chụp ảnh tổng quan (M6 là nhóm item chung, không phải một màn – mục 2: M1…M5)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-01 | Tất cả màn C2 | Ngôn ngữ giao diện nhất quán tiếng Việt |  | Mọi nhãn, nút, tiêu đề, placeholder, thông báo trên Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ, Lịch sử đơn, navbar đều bằng tiếng Việt. Fail nếu có ≥ 1 chuỗi tiếng Anh không phải thuật ngữ kỹ thuật chuẩn (chấp nhận: Email, OTP, EShop). |

#### Cuối lượt (khoá tài khoản / tắt backend – làm sau cùng)

| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |
|---|---|---|---|---|---|
| ☐ | CL-52 | Đăng nhập | Sai 3 lần liên tiếp → khoá 30 giây | Restart backend trước khi kiểm (bộ đếm = 0). | Sai mật khẩu 3 lần liên tiếp, ngay sau đó đăng nhập đúng → bị từ chối kèm thông báo; chờ 30 giây (+ 5 giây dung sai) đăng nhập đúng → thành công. Fail nếu lần đúng ngay sau đó thành công, hoặc sau 35 giây vẫn bị từ chối. |
| ☐ | CL-64 | Hồ sơ | Lỗi kết nối khi cập nhật có thông báo dễ hiểu, không mất dữ liệu | Khởi động lại backend sau khi kiểm (CSDL seed lại). | Tắt backend, bấm Cập nhật → thông báo tiếng Việt cho biết không kết nối được máy chủ / thử lại; dữ liệu đã nhập trong form vẫn còn. Fail nếu thông báo chung chung không nêu nguyên nhân hoặc form bị xoá. |

## 5. Nhật ký lượt

| Lượt | Nền tảng | Bắt đầu – kết thúc | Restart backend | Chính thức? | Ghi chú |
|---|---|---|---|---|---|

