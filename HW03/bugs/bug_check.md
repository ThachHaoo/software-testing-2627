# Kiểm bug SV viết (BUG-58…85) + tái hiện – T1 bước 5/6e (AI, chỉ đọc)

AI chỉ **liệt kê** điểm lệch so với các tiêu chí của lệnh 5/6e, không đề xuất câu chữ, không sửa file BUG. SV quyết định sửa hay giữ.

## Cách kiểm

- **Phần 1 (đọc):** với từng BUG kiểm (a) còn `<SV viết>` / 🔒 · (b) thang Severity (Critical/High/Medium/Low), Priority (High/Medium/Low) · (c) tiêu đề không có tiền tố `[HW03-C2…]` · (d) Actual khớp "Dữ kiện (AI chép)" · (e) Expected có căn cứ (SRS / căn cứ item), không quá 1 nhánh · (f) Yêu cầu chỉ ghi yêu cầu bị vi phạm · (g) câu Tác động / khẳng định không có dữ kiện mà chưa đánh dấu "(chưa kiểm chứng)" · (h) tên trường / màn / nút không có trong SUT (đối chiếu `frontend-web/src/pages/*.jsx` @ `de0f48f`).
- **Kết quả chung (a)(b)(c):** 28/28 không còn `<SV viết>`/🔒; Severity: High 7, Medium 4, Low 17; Priority: High 5, Medium 6, Low 17 (đều đúng thang); 0/28 tiêu đề có tiền tố `[HW03-C2…]` (tiền tố chỉ ở dòng "Tiền tố GitHub").
- **Phần 2 (tái hiện):** 10/11/2026, SUT `main` @ `de0f48f` (`tools\sut_main.ps1`), `tools\restart_backend.ps1` trước mỗi lượt, web `npx vite --host 127.0.0.1 --port 5173`. Chạy Steps SV bằng Playwright 1.48.2: **P1** = Google Chrome (channel `chrome`, thay cho Cốc Cốc), **P2** = Firefox bản build Playwright; viewport 1280×800, locale mặc định `en-US` (trừ chỗ ghi). Script `HW03/tests/repro_bugs.spec.ts` (+ `repro.config.ts`), số đo thô `bugs/repro/repro_P1.json`, `repro_P2.json`. Lượt chạy cuối: 23/23 test chạy hết trên P1 và P2.
  - Steps không nêu giá trị → AI chọn giá trị, ghi trong JSON. Bước **"(cô lập)"** = ngoài Steps SV, chạy thêm để tách nguyên nhân (CLAUDE.md mục 3); không đổi Expected.
  - "Slow 3G" thay bằng **trễ 3000 ms cho request tương ứng** (route của Playwright, cùng cách trên P1, P2) – không phải throttling DevTools.
  - Item chỉ quan sát bằng mắt (CL-06, CL-24, CL-25, CL-53, CL-63, SV-04): AI chỉ ghi số đo DOM/màu, không chấm.
  - **P3** không chạy lại; đối chiếu bằng Dữ kiện + ảnh. AI đã xem 7 ảnh lượt tay P3: `P3_CL-24_1`, `P3_CL-06_1`, `P3_CL-53_1`, `P3_CL-09_1`, `P3_CL-63_1`, `P3_CL-63_2`, `P3_SV-02_1`, `P3_SV-04_1`. Ảnh auto P3: không xem lại (Actual auto đối chiếu bằng Dữ kiện).

## Tổng hợp

| Nhóm | Số | Mã |
|---|---|---|
| Không có điểm lệch theo (a)–(h) | 14 | BUG-59, 60, 61, 65, 66, 67, 68, 69, 71, 74, 77, 83, 84, 85 |
| Có điểm SV cần xem | 14 | BUG-58, 62, 63, 64, 70, 72, 73, 75, 76, 78, 79, 80, 81, 82 |
| Tái hiện được trên P1 + P2 (theo Steps SV) | 24 | các bug còn lại |
| Tái hiện một phần / có bước không chạy được | 4 | BUG-62, 64, 75, 82 |
| Không tái hiện được | 0 | – |

---

## BUG-58 – Tab order Đăng nhập, Quên MK B2

- Kiểm: (a)(b)(c)(d)(e)(f)(h) không lệch. Expected 1 nhánh, căn cứ FR-21.5.
- (g) Nhận định: câu 1 ("gặp rắc rối lớn…") và câu 2 ("hoàn toàn không thể truy cập được các chức năng trên Navbar" ở B2) không có dữ kiện đi kèm, chưa đánh dấu "(chưa kiểm chứng)"; chỉ câu 3 có đánh dấu. Dữ kiện chỉ ghi chuỗi Tab, không thử Shift+Tab / cách khác để tới Navbar.
- Tái hiện: **được** (P1, P2). /login: focus đầu tiên `Sign In` → `EShop` … (giống Dữ kiện); P2 lặp ở `Đăng ký ngay`. B2: chuỗi Tab không có 4 link Navbar; P2 lặp ở `← Quay lại`. P3: N/A (không có phím Tab).

## BUG-59 – Tiêu đề tab "frontend-web"

- Kiểm: không lệch.
- Ghi chú (không chặn): Tiền điều kiện không nêu đăng nhập trước khi mở `/profile` (BUG-61, 63 có nêu); khi chưa đăng nhập `/profile` vẫn có title `frontend-web`.
- Tái hiện: **được** (P1, P2): `["frontend-web","frontend-web","frontend-web"]`. P3: Dữ kiện auto giống.

## BUG-60 – `<html lang="en">`

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): `lang = "en"`.

## BUG-61 – Thiếu `<h1>`

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): `/login 0`, `/forgot-password 0`, `/profile 0`.

## BUG-62 – Ô Email type="text", email sai định dạng không bị chặn

- Kiểm: (a)(b)(c)(e)(f)(g) không lệch.
- (h) Tên trường: Steps / Expected / Actual gọi "ô Email" ở trang Đăng nhập; nhãn thật trên `/login` là **"Username"** (`Login.jsx:28`, Dữ kiện CL-20 cũng ghi "Username"). Ở Quên MK B1 nhãn là "Nhập Email của bạn".
- (d) Actual khớp Dữ kiện (1 request `/api/login`, 1 request `/api/forgot-password`, không thông báo validate).
- Tái hiện: **một phần.**
  - `/login` đúng Steps SV (chỉ nhập `abc`, ô Mật khẩu để trống): **0 request** – trình duyệt chặn vì ô Mật khẩu `required` (validationMessage ở ô Mật khẩu "Please fill out this field."), ô Email không có thông báo. Steps không có bước nhập mật khẩu.
  - (cô lập) có nhập thêm mật khẩu `Test1234!`: 1 request `/api/login`, chữ "Đăng nhập thất bại. Vui lòng kiểm tra lại." → khớp Actual.
  - `/forgot-password`: 1 request, hộp thoại "Lỗi: User not found" → khớp Actual. `type="text"` ở cả 2 trang (P1, P2).

## BUG-63 – Nhãn trường bắt buộc thiếu '*'

- Kiểm: (a)(b)(c)(d)(f)(g) không lệch.
- (h)/(e) Expected nêu ô **"Xác nhận mật khẩu" ở Quên MK B2** – ô này không có trong SUT (B2 chỉ có "Mã OTP (4 số)", "Mật khẩu mới"; chính là BUG-68). Expected cũng gọi "Email" ở Đăng nhập, nhãn thật "Username". (Hai chỗ này chép từ Expected của item CL-20.)
- Tái hiện: **được** phần nhãn (P1, P2): `/login` ["Username","Mật khẩu"], B1 ["Nhập Email của bạn"], B2 ["Mã OTP (4 số)","Mật khẩu mới"], `/profile` ["Email (Không đổi)","Họ Tên","Số điện thoại","Địa chỉ giao hàng"] – không nhãn nào có '*'.
- Cô lập phần "bị chặn khi trống" (Hồ sơ, giá trị sau restart: Họ Tên "Test User", SĐT "", Địa chỉ ""):
  - Xoá Họ Tên → trình duyệt chặn (`required`, `Profile.jsx:133`), 0 request.
  - Xoá SĐT / xoá Địa chỉ → cùng hộp thoại "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.", 0 request. Lúc xoá Địa chỉ thì ô SĐT đang trống, nên form bị chặn do ô SĐT, không phải do Địa chỉ (Địa chỉ không có `required` / kiểm tra riêng trong `Profile.jsx`). Actual "cả 3 trường khi để trống đều khiến form bị chặn" lấy từ Dữ kiện auto, cùng điều kiện SĐT trống.

## BUG-64 – Thông báo lỗi chỉ ở hộp thoại alert

- Kiểm: (a)(b)(c)(e)(f)(h) không lệch; Expected 1 nhánh (FR-22.4 + GA3).
- (d) Actual khớp Dữ kiện, nhưng Dữ kiện auto không ghi giá trị SĐT đã nhập; Steps SV dùng SĐT `123`.
- (g) Nhận định: ý "gây nhầm lẫn khi hệ thống báo 'Cập nhật thành công!' dù SĐT nhập sai" dựa trên hộp thoại của lượt auto (xem tái hiện).
- Tái hiện: **một phần.**
  - Quên MK B2, OTP đúng + `123`: không có chữ mới trong trang; chỉ hộp thoại "Mật khẩu quá yếu! …" → **khớp**.
  - Hồ sơ, SĐT `123` (đúng Steps): không có chữ mới trong trang; hộp thoại là **"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."**, không phải "Cập nhật thành công!" như Actual. Phần "lỗi chỉ ở hộp thoại" vẫn tái hiện; nội dung hộp thoại khác. "Cập nhật thành công!" xuất hiện khi SĐT lọt kiểm tra của web (vd `912345678`, BUG-72).

## BUG-65 – Bấm nhãn không focus ô

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): sau khi bấm 5 nhãn, phần tử focus = `body`.

## BUG-66 – Thiếu chỉ báo bước

- Kiểm: không lệch.
- Tái hiện: **được** (DOM, P1, P2): không có chữ dạng "Bước x / y" ở B1 và B2. Ảnh `P3_CL-24_1` (B1) và `P3_CL-06_1` (B2): không thấy chỉ báo bước – khớp Actual P3.

## BUG-67 – Không có "Quay lại đăng nhập" ở B1

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): vùng nội dung B1 chỉ có nút "Lấy mã OTP"; không có chữ "Quay lại đăng nhập". Ảnh `P3_CL-24_1` khớp.

## BUG-68 – Thiếu ô "Xác nhận mật khẩu mới"

- Kiểm: không lệch ("Liên quan issue #30" khớp mục Item liên quan).
- Tái hiện: **được** (P1, P2): B2 có 2 ô `Mã OTP (4 số) [text]`, `Mật khẩu mới [password]`. Ảnh `P3_CL-06_1` khớp.

## BUG-69 – OTP 4 chữ số

- Kiểm: không lệch.
- Tái hiện: **được** (P1 `1187`, P2 `3708`: 4 chữ số). Ảnh `P3_CL-06_1`: "Mã OTP của bạn là: 2485".

## BUG-70 – Mật khẩu `Abcdef1!` bị từ chối

- Kiểm: (a)–(f)(h) không lệch.
- (g) Nhận định: câu khẳng định nguyên nhân ("Bộ kiểm tra độ mạnh mật khẩu (regex/validation) … bị bắt lỗi sai cấu trúc") không có dữ kiện; "(chưa kiểm chứng)" đặt sau câu "Liên quan issue #17", không gắn với câu nguyên nhân.
- Tái hiện: **được** (P1, P2): hộp thoại "Mật khẩu quá yếu! …", 0 request `/api/reset-password`, vẫn ở `/forgot-password`; đăng nhập bằng `Abcdef1!` → "Đăng nhập thất bại. Vui lòng kiểm tra lại.".

## BUG-71 – Nút chính / phụ B2 giống nhau

- Kiểm: không lệch.
- Tái hiện: **được** (computed style, P1, P2): hai nút cùng `background-color rgb(22,163,74)`, chữ trắng, 382×40, viền, bo góc 4px. Ảnh `P3_CL-06_1`: hai nút cùng màu xanh lá, cùng cỡ.

## BUG-72 – SĐT `912345678` vẫn được lưu

- Kiểm: (a)–(f)(h) không lệch.
- (g) Nhận định: câu 1 ("làm sai lệch dữ liệu người dùng") chưa đánh dấu; "(chưa kiểm chứng)" chỉ sau câu 2.
- Tái hiện: **được** (P1, P2): hộp thoại "Cập nhật thành công!", 1 request PUT `/api/users/me`, sau F5 ô SĐT = `912345678`.

## BUG-73 – Hồ sơ quay về giá trị cũ sau Cập nhật + F5

- Kiểm: (a)(b)(c)(e)(f)(h) không lệch.
- (d) Tiêu đề nêu "Số điện thoại và Địa chỉ quay về giá trị cũ"; Actual và Dữ kiện (`sau F5: ["Test User","",""]`) cho thấy **cả Họ Tên** cũng về giá trị cũ "Test User". Actual không nhắc hộp thoại xuất hiện sau khi bấm Cập nhật.
- (g) Nhận định "(không được lưu bền vững vào hệ thống backend/CSDL)" có đánh dấu; xem kết quả cô lập dưới.
- Tái hiện: **được** hiện tượng (P1, P2): Steps SV (Họ Tên `Test Repro`, SĐT `0912345678`, Địa chỉ `1 Repro, Q1`) → sau F5 `["Test User","",""]`.
  - Cô lập: sau khi bấm Cập nhật có hộp thoại **"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."** và **0 request** PUT – web chặn trước khi gửi (`Profile.jsx:43`, regex `^[1-9][0-9]{8,9}$` không nhận SĐT bắt đầu bằng 0).
  - (cô lập) cùng thao tác với SĐT `912345678` → "Cập nhật thành công!", 1 PUT, sau F5 `["Test Repro","912345678","1 Repro, Q1"]` (cả 3 trường lưu bền).

## BUG-74 – Nhãn "Thoát"

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): navbar "EShop | Giỏ hàng | Chào, Test User | Thoát".

## BUG-75 – Đổi Họ Tên không cập nhật ngay trên Navbar

- Kiểm: (a)(b)(c)(e)(f)(h) không lệch.
- (d) Actual "chỉ cập nhật tên mới sau khi tải lại trang (F5)" **không có trong Dữ kiện** (lượt auto chỉ đo navbar sau 3000 ms, không tải lại).
- Tái hiện: **một phần.**
  - Đúng Steps (chỉ đổi Họ Tên = `Test Đổi`, SĐT đang trống sau restart): hộp thoại "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.", 0 request; navbar vẫn "Chào, Test User"; **sau F5 vẫn "Test User"** (không lưu) → phần "cập nhật sau F5" không tái hiện theo Steps.
  - (cô lập) Họ Tên `Test Đổi` + SĐT `912345678`: "Cập nhật thành công!", 1 PUT; navbar khi chưa tải lại vẫn "Chào, Test User"; sau F5 navbar "Chào, Test Đổi" → hiện tượng navbar không cập nhật ngay **có** khi lưu thành công. (P2: sau F5 ô Họ Tên đọc được rỗng trong khi navbar đã là "Test Đổi" – có thể do đọc ô trước khi trang nạp xong; chưa cô lập.)

## BUG-76 – `/profile` khi chưa đăng nhập

- Kiểm: (a)(b)(c)(d)(f)(g)(h) không lệch.
- (e) Expected có **2 nhánh** ("tự động chuyển hướng tới `/login`, **hoặc** hiển thị thông báo kèm liên kết/nút…") – chép từ Expected item CL-49.
- Tái hiện: **được** (P1, P2): URL giữ `/profile`, vùng nội dung chỉ có chữ "Vui lòng đăng nhập", 0 link/nút tới Đăng nhập trong `main`.

## BUG-77 – URL không tồn tại

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): `/profil` → nội dung `main` = "", 0 link về `/`.

## BUG-78 – Nút submit không khoá, gửi trùng

- Kiểm: (a)(b)(c)(f)(g)(h) không lệch. Expected gộp 2 item (CL-53 mạng chậm, SV-06 mạng thường), mỗi item 1 tiêu chí.
- (d) Actual khớp Dữ kiện; riêng câu "Trên P3 bị TimeoutError do dblclick" là lỗi của test tự động (harness, `locator.dblclick` quá 30 s), không phải hành vi của SUT.
- Steps B2 và Hồ sơ không nêu giá trị nhập (mật khẩu mới, thông tin cập nhật).
- Tái hiện: **được** các con số trong Actual (P1, P2):
  - Đăng nhập, trễ 3000 ms, bấm Sign In 3 lần: nút không disabled, nhãn vẫn "Sign In", **3 request** `/api/login`.
  - B1 nhấp đúp "Lấy mã OTP": **2 request**.
  - B2 nhấp đúp "Đặt lại mật khẩu" với `Abcdef1!`: 0 request, 2 hộp thoại "Mật khẩu quá yếu! …" (bị kiểm tra mật khẩu của web chặn – BUG-70).
  - Hồ sơ nhấp đúp "Cập nhật" với SĐT `0912345678`: 0 request, 2 hộp thoại "Số điện thoại không hợp lệ…" (bị kiểm tra SĐT chặn – BUG-73).
  - (cô lập) Hồ sơ với SĐT `912345678`: **2 request PUT**, 2 hộp thoại "Cập nhật thành công!".
  - (cô lập) B2 với mật khẩu lọt regex của web (`Abcd efg1`): **2 request** `/api/reset-password`, hộp thoại "Đổi mật khẩu thành công!" rồi "Mã OTP không đúng hoặc có lỗi xảy ra.". (Mật khẩu đã khôi phục về `Test1234!` sau bước này.)
- P3: ảnh `P3_CL-53_1` là màn Đăng nhập tĩnh (đã nhập email/mật khẩu, nút "Sign In"); ảnh không thể hiện trạng thái nút trong lúc chờ.

## BUG-79 – Không có trạng thái đang tải ở Lịch sử đơn

- Kiểm: (a)(b)(c)(e)(f)(g)(h) không lệch.
- (d) Actual P1 "hiển thị trạng thái rỗng ('chưa có đơn hàng') trước khi danh sách đơn hàng thực tế kịp tải ra" – Dữ kiện P1 chỉ ghi "Không có trạng thái đang tải" (không nhắc trạng thái rỗng). Actual P2/P3 "toàn bộ dữ liệu hiển thị cùng lúc" khớp Dữ kiện P2/P3, nhưng **ảnh P3** `P3_CL-63_1` cho thấy "Bạn chưa có đơn hàng nào." và `P3_CL-63_2` (cùng phút 1:06) cho thấy bảng đơn #7…#2 – tức ảnh P3 thể hiện trạng thái rỗng rồi mới tới bảng, giống mô tả P1.
- Tái hiện: **được** (P1, P2, trễ 3000 ms cho `/api/orders`): chuỗi trạng thái khối Lịch sử đơn khi tải lại = `rỗng "Bạn chưa có đơn hàng nào."` → `bảng đơn`, không có chữ đang tải. Trên P2 cũng thấy trạng thái rỗng trước bảng (cách giảm tốc khác throttling thật của Firefox).

## BUG-80 – Ngày đặt không đúng dd/mm/yyyy, khác giữa nền tảng

- Kiểm: (a)–(f)(h) không lệch. Expected dựa giả định GA1 (SRS im lặng) – đúng căn cứ item.
- (g) Nhận định ("gây nhầm lẫn cho người dùng khi đọc thông tin ngày tháng") **không có "(chưa kiểm chứng)"**.
- Tái hiện: **được** (định dạng phụ thuộc ngôn ngữ trình duyệt): đơn tạo 10/11/2026 hiển thị `11/10/2026` với `navigator.language = en-US` và `10/11/2026` với context `vi-VN` (P1, P2). Mã hiển thị `new Date(o.created_at).toLocaleDateString()` không truyền locale (`Profile.jsx:186`). Trình duyệt thật (Cốc Cốc, Firefox của SV) không chạy lại. Ảnh `P3_CL-09_1`: các đơn hiện `11/9/2026` – khớp Actual P3.

## BUG-81 – Nút "Hủy đơn" ở đơn Đang giao

- Kiểm: (a)–(g) không lệch.
- (h) Steps "ví dụ đơn #10" và Actual "#8…#12" là số đơn của lượt auto; làm đúng Tiền điều kiện (restart + `seed_orders.py`) thì đơn Đang giao là **#3** (#1 Chờ xác nhận, #2 Đã xác nhận, #3 Đang giao, #4 Đã giao, #5 Đã hủy, #6, #7 Chờ xác nhận) – ảnh `P3_CL-09_1` cũng là #1…#7.
- Tái hiện: **được** (P1, P2): #3 Đang giao có nút "Hủy đơn" (disabled = false); #4 Đã giao, #5 Đã hủy không có nút. Bấm "Hủy đơn" ở #3 → hộp thoại "Hủy đơn thành công!", API trả #3 = `canceled`.

## BUG-82 – Autofill

- Kiểm: (a)(b)(c)(d)(f)(g)(h) không lệch.
- Tiêu đề "[Đăng nhập, Quên MK, Hồ sơ] Không sử dụng được … Autofill" trong khi Actual P1 ghi Autofill **dùng được ở Quên mật khẩu**.
- (e) Expected dùng "Paste (Ctrl+V) **hoặc** chọn gợi ý Autofill" (chép từ item SV-02) – có thể đọc thành 2 nhánh; Actual ghi Paste đạt ở mọi ô.
- Tái hiện: **bước Autofill không chạy được** bằng Playwright (profile trình duyệt sạch, không có dữ liệu Autofill đã lưu) – cần SV chạy tay. Paste (P1): dán đúng `test@eshop.com`, `Test1234!` vào 2 ô `/login` và ô Email B1; P2 không chạy (Firefox Playwright không cấp quyền clipboard). Ảnh `P3_SV-02_1`: ô Username đang gõ dở `test@eshop.co`, bàn phím có thanh biểu tượng khoá / thẻ / vị trí, không thấy gợi ý tài khoản.

## BUG-83 – Không focus về ô lỗi

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): sau submit lỗi, focus ở nút submit (`Sign In` / `Đặt lại mật khẩu` / `Cập nhật`), không ở ô lỗi. Đăng nhập dùng mật khẩu `Wrong123!` ("Đăng nhập thất bại. Vui lòng kiểm tra lại."); Hồ sơ SĐT `123` → hộp thoại "Số điện thoại không hợp lệ…".

## BUG-84 – Tương phản < 4.5:1

- Kiểm: không lệch (Actual khớp Dữ kiện; cả hai không nêu phần tử / tỉ lệ cụ thể).
- Tái hiện: **được** (computed color, không phải Lighthouse; P1 = P2): `/login` "Quên mật khẩu?" `rgb(59,130,246)` trên trắng = 3.68; `/forgot-password` không phần tử nào < 4.5; `/profile` "Chào, Test User" (vàng trên xanh) = 3.92, "Thoát" và "Hủy đơn" (trắng trên đỏ `rgb(239,68,68)`) = 3.76. Placeholder không đo. Ảnh `P3_SV-04_1`: Lighthouse `/profile` Accessibility 81, mục Contrast báo "Background and foreground colors do not have a sufficient contrast ratio".

## BUG-85 – Link < 24px chiều cao

- Kiểm: không lệch.
- Tái hiện: **được** (P1, P2): Sign In 382×40, Quên mật khẩu? 102×19, Đăng ký ngay 85×19, Lấy mã OTP 382×40, Cập nhật 271×40 (giống Dữ kiện P1/P2).

---

## Bất thường phát hiện khi tái hiện (không thuộc lời SV)

- SUT `frontend-web/src/pages/Profile.jsx:43`: regex SĐT `^[1-9][0-9]{8,9}$` – chặn SĐT bắt đầu bằng 0, nhận SĐT 9 số không có 0. Là nguyên nhân trực tiếp của kết quả theo Steps ở BUG-73, BUG-75, BUG-78 (Hồ sơ), BUG-63 (CL-21) và hộp thoại ở BUG-64 (Hồ sơ). Liên quan issue #113 (theo `dup_check.md`).
- SUT `frontend-web/src/pages/ForgotPassword.jsx:26`: regex mật khẩu bắt buộc có khoảng trắng, không nhận ký tự đặc biệt → `Abcdef1!` bị chặn, `Abcd efg1` lọt (BUG-70, BUG-78).
- SUT `frontend-web/src/pages/Login.jsx:24`: tiêu đề form trang Đăng nhập là "Đăng Ký" (thấy trong ảnh `P3_CL-53_1`, `P3_SV-02_1`); `Login.jsx:40`: ô Mật khẩu `type="text"` (mật khẩu hiện rõ, ảnh `P3_CL-53_1`). Không thuộc bug nào trong 28 bug; AI không kết luận, SV xem.
- Harness: lượt auto CL-21, CL-37, CL-56, SV-06 (Hồ sơ) chạy với SĐT trống / `0912345678` nên kết quả bị kiểm tra SĐT của web chi phối (xem từng bug). SV-06 P3 có `TimeoutError` ở `dblclick` (lỗi harness).
