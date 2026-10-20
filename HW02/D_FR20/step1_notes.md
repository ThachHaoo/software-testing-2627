# D_FR20 – Ghi chú bước 0–1 (AI, chờ SV review)

## 1. Môi trường của D (P2)

- Thiết bị: Android thật, Expo Go (bản cho SDK 54). Model/phiên bản Android/locale/bàn phím: SV bổ sung khi chạy (D15).
- `frontend-mobile/package.json`: `expo ~54.0.33`, `react-native 0.81.5`, `react 19.1.0`.
- `frontend-mobile/App.js` dòng 16 (thay đổi cục bộ, `git -C ../eshop-sut diff`):
  `const API_URL = "http://172.21.0.137:3000/api";` (gốc: `http://192.168.10.13:3000/api`).
- SUT `tkob-team/eshop-sut` @ `de0f48f`; diff cục bộ chỉ có `frontend-mobile/App.js` và `backend/database.sqlite` (CSDL seed lại khi khởi động).
- Chưa có `HW02/env/mobile_api_url.patch` (CLAUDE.md yêu cầu) — ngoài phạm vi lệnh này.

## 2. SRS nguyên văn (`../eshop-sut/README.md`)

FR-20 nằm ở **§7** (lệnh ghi §6).

```
231: ## 7. Phân hệ Mobile (React Native)
233: ### FR-20: Tính năng Mobile
235: - Đầy đủ các chức năng: Xem sản phẩm, Đăng nhập, Đăng xuất, Đăng ký, Giỏ hàng, Thanh toán, Hồ sơ, Lịch sử đơn hàng.
236: - Chức năng Hủy đơn hàng tuân theo đúng State Machine ở FR-10 (chỉ được hủy khi `pending` hoặc `confirmed`).
```

FR-20 không dẫn tới FR nào cho chức năng Đăng ký; FR-01 áp cho mobile theo giả định D2. Các mục áp chung cho mobile/đăng ký:

```
 19: | Mobile App   | React Native + Expo         | IP LAN của máy chủ      |
 23: - Admin: `admin@eshop.com` / `Admin123!`
 24: - User test: `test@eshop.com` / `Test1234!`

 30: ### FR-01: Đăng ký tài khoản
 32: - Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.
 33: - Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
 34: - **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
 35: - Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp.
 36: - Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

242: ### FR-21: Tiêu chuẩn Giao diện Chung
244: - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
245: - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
246: - **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
247: - **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
248: - **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.

250: ### FR-22: Form Requirements
252: - Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
253: - Trường Email phải dùng `type="email"`.
254: - Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
255: - Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
256: - Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.

278: | SEC-01 | Mật khẩu **không** được lưu dưới dạng plaintext. |
```

Không liên quan đăng ký: FR-21.3 (tiền), FR-22.5 (form một bước), FR-23, FR-24.

## 3. Mã nguồn mobile – chỉ tên trường, loại ô, nút, điểm quan sát, endpoint

`../eshop-sut/frontend-mobile/App.js`:

| Dòng | Nội dung |
|---|---|
| 21 | view mặc định `home` |
| 42–46 | state của form: `registerName`, `registerEmail`, `registerPassword`, `registerError` |
| 222–230 | `POST ${API_URL}/register`, `Content-Type: application/json`, body `{name, email, password}` (cùng endpoint với web) |
| 233 | `Alert.alert("Thành công", "Đăng ký tài khoản thành công.")` |
| 236 | `setView("login")` |
| 238, 801–803 | chữ lỗi `errorBoxText` đặt **trên** nhãn 'Họ Tên' |
| 422–440 | header: 'EShop Mobile', 'Đăng nhập' / `Chào, ${user.name}`, `Giỏ (n)` |
| 759–795 | màn 'Đăng Nhập'; link 'Chưa có tài khoản? Đăng ký ngay' (785–789) |
| 800 | tiêu đề 'Đăng Ký Tài Khoản' |
| 804–809 | nhãn 'Họ Tên' + TextInput (không keyboardType, không autoCapitalize) |
| 810–816 | nhãn 'Email' + TextInput `autoCapitalize="none"` (không keyboardType) |
| 817–823 | nhãn 'Mật khẩu' + TextInput `secureTextEntry` |
| 824–827 | gợi ý 'Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt.' |
| 828–830 | nút 'Đăng Ký' |
| 831–835 | link 'Đã có tài khoản? Đăng nhập' |

Không có ô Xác nhận mật khẩu trên màn hình. Logic kiểm tra của `handleRegister` (dòng 209–240) không dùng làm căn cứ Expected; chỉ dùng dữ kiện "client chỉ kiểm Mật khẩu trước khi gửi" (dòng 211–219) để nêu phương án phạm vi D1 (a).

`../eshop-sut/frontend-admin/src/App.jsx` dòng 881–892: trang 'Quản lý Người dùng', cột ID, Email, Role, Số ĐT, Hành động — **không có cột Họ Tên**.

## 4. Đối chiếu biến web (A_FR01) ↔ mobile (D_FR20)

| A_FR01 | D_FR20 | Khác biệt |
|---|---|---|
| V1 Họ Tên | V1 Họ Tên | — |
| V2 Email (`type="text"`) | V2 Email (TextInput, `autoCapitalize="none"`) | không có HTML5; loại bàn phím → D13 |
| V3 Email đã tồn tại | V3 | — |
| V4 Mật khẩu | V4 | — |
| V5 Xác nhận mật khẩu (không có ô) | V5 (không có ô) | — |
| — | V6 Cách nhập | mới (bàn phím ảo, dán, tự sửa) → D12 |
| V6 Thông báo lỗi (hộp lỗi + bong bóng HTML5) | V7 Thông báo trên app (chữ lỗi, Alert, kênh khác) | không có bong bóng HTML5 |
| V7 URL /login, /register | V8 Màn hình (tiêu đề) | không có URL |
| V8 Phản hồi API | — | chỉ khi D1 = c |
| V9 Bản ghi CSDL | V9 Tài khoản phía server | điểm quan sát → D11 |

Giả định A dùng lại: A1→D3, A2→D4, A3→D5, A4→D6, A5→D7, A6→D8, A7+A17→D9, A10(+A16)→D10, A12→D11, A14→D13, A13+A19→D0, A20→D14. A21–A23 không dùng lại (phát sinh từ case SV bước 5 của A; giữ bước 5 của D đo được theo P1 = b).

## 5. Ước tính phạm vi (D1)

| Phương án | Tầng | BVA | EC | TC | Thời gian chạy tay |
|---|---|---|---|---|---|
| a – gọn | Mobile | chỉ độ dài Mật khẩu (biến client mobile xử lý) | ~25–30 | ~18–22 | ~1,3–1,5 giờ |
| b – đủ UI | Mobile | đủ như suite UI của A | ~45–50 | ~45–50 | ~3–3,5 giờ |
| c – đủ UI + API | Mobile + API (chạy lại suite API của A) | đủ | ~50 | ~50 tay + 49 API | ~3,5–4 giờ |

Cơ sở: A có 52 EC; TS-DOM-UI 27, TS-BVA-UI 19, TS-GUI 5, TS-DOM-API 30, TS-BVA-API 19. ≈ 3,5 phút/case tay (tải lại app, vào màn Đăng ký, nhập bằng bàn phím ảo, chụp màn hình, kiểm trang admin/đăng nhập thử).

## 6. Khai cho Audit

- P1 = b (AI không đọc `sv_cases.md` / `ai_gap_answer.md` / `sv_questions.md` của A, B, C ở bước 1–4), nhưng ở bước 1 AI đã đọc `HW02/A_FR01/testcases.json` (bản HEAD), file này có chứa kết quả bước 5 của A. Đã thấy cụ thể (từ lệnh in `meta.scope`, `requirements`, `meta.assumptions`, `domain.variables`, và số case theo suite):
  - `meta.scope`: câu "TS-SV có kiểm thăm dò SEC-04, SEC-05, SEC-06* liên quan trực tiếp tới dữ liệu đăng ký."
  - `requirements`: mã SEC-04, SEC-05, SEC-06* ("mở rộng cho đăng ký, A23").
  - A20: nội dung quy tắc Blocked do lỗi đã biết (ghi "AI đề xuất, SV duyệt 2026-10-19").
  - A21: email có ký tự ngoài ASCII là sai định dạng; TC-219 `tеst@eshop.com` (chữ е Cyrillic) phải bị từ chối; thêm EC52.
  - A22: đăng ký khi đang đăng nhập → thành công, chuyển /login, tạo 1 user, test@eshop.com không đổi; Expected của TC-223.
  - A23: tài khoản tạo qua đăng ký luôn có role user, trường ngoài api_specification bị bỏ qua; TC-222.
  - A3 bản cuối có câu "SV sửa ở bước 5" (local phân biệt hoa/thường, domain không phân biệt).
  - Số case: TS-SV 33 case (UI 13, API 20; origin Human 25, Both 8). Không in nội dung từng case TS-SV.
  - A21–A23 không dùng lại cho D.
- D5 kế thừa giả định SV sửa ở bước 5 của A (A3 bản 2, 8d837f1) → có thể ảnh hưởng thiết kế EC của D (liên quan P1 = b; SV quyết).
- Lệnh trước giả định nhầm A có commit 1/7b (A chốt giả định ngay trong 1/7, 4e30b25).
- Bước 2: để tham chiếu TC API của A, AI in toàn bộ `domain.partitions` của A_FR01 kèm mã TC TS-DOM-API/TS-BVA-API theo `ec_target`. Bản in có EC51 ('Chỉ khác hoa/thường ở phần domain', ghi 'SV thêm ở bước 5 (A3)') và EC52 ('Email có ký tự ngoài ASCII', ghi 'A21; SV thêm ở bước 5'); EC19 ghi 'A3 (SV sửa ở bước 5)'. Không in nội dung case TS-SV. Lớp trùng email của D (EC7) có phần 'chỉ khác hoa/thường ở phần domain' — suy từ D5 do SV chốt; D không có lớp email ngoài ASCII.
- Khung sv_cases.md do AI tạo (chép cấu trúc từ HW02/C_FR15/sv_cases.md, bỏ toàn bộ case của C; bảng chỉ có tầng Mobile và GUI theo D1 = a; mã giả định mới từ D16).
- Sau khi đóng băng bước 4 (c19c666), khi tạo khung sv_cases.md AI đã in toàn văn HW02/C_FR15/sv_cases.md (gồm case SV TC-FR15-200…217 của C). Ở bước 5, AI in 40 dòng đầu HW02/C_FR15/ai_gap_answer.md (bản d1c71d8) để lấy cấu trúc file. Cả hai đều sau khi bản AI bước 1–4 của D đã đóng băng.
