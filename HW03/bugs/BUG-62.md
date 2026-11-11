# BUG-62

- **ID:** BUG-62
- **Tiêu đề:** [Đăng nhập, Quên MK B1] Ô Email type="text", email sai định dạng không bị chặn
- **Severity:** High
- **Priority:** Medium
- Tiền tố GitHub: [HW03-C2-62]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-17: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-66: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-17: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-66: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-17: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-66: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-17 – Đăng nhập, Quên mật khẩu (bước 1); CL-66 – Đăng nhập, Quên mật khẩu (bước 1)
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Trạng thái người dùng chưa đăng nhập.

## Các bước tái hiện

1. Truy cập vào trang Đăng nhập (`http://localhost:5173/login`) hoặc trang Quên mật khẩu bước 1 (`http://localhost:5173/forgot-password`).
2. Mở DevTools -> tab Elements, kiểm tra thuộc tính `type` của ô nhập Email (trên trang Đăng nhập có nhãn "Username", trên trang Quên mật khẩu bước 1 có nhãn "Nhập Email của bạn").
3. Nhập giá trị sai định dạng email `abc` vào ô Email (Username). Nếu ở trang Đăng nhập, nhập thêm mật khẩu bất kỳ (ví dụ `Test1234!`).
4. Bấm nút submit ('Sign In' hoặc 'Lấy mã OTP').
5. Mở DevTools -> tab Network và kiểm tra request gửi đi.

## Expected (trích căn cứ)

- CL-17 – căn cứ: FR-02.4 (README.md:44); FR-22.2 (README.md:253)
  - FR-02.4, README.md:44 (AI chép nguyên văn): Trường email phải dùng `type="email"` (có validate HTML5 format).
  - FR-22.2, README.md:253 (AI chép nguyên văn): Trường Email phải dùng `type="email"`.
- CL-66 – căn cứ: FR-02.4 (README.md:44); FR-22.2 (README.md:253)
  - FR-02.4, README.md:44 (AI chép nguyên văn): Trường email phải dùng `type="email"` (có validate HTML5 format).
  - FR-22.2, README.md:253 (AI chép nguyên văn): Trường Email phải dùng `type="email"`.
- Expected của bug: Ô Email tại trang Đăng nhập (nhãn "Username") và bước 1 Quên mật khẩu (nhãn "Nhập Email của bạn") phải có `type="email"`. Khi nhập email sai định dạng (ví dụ 'abc') rồi submit, form phải bị chặn ở frontend, có thông báo validate và không gửi request API lên server.

## Actual

- Cả P1, P2 và P3 tại hai màn hình (/login và /forgot-password bước 1):
  - Ô nhập Email (nhãn "Username" ở Đăng nhập, "Nhập Email của bạn" ở Quên mật khẩu bước 1) khai báo `type="text"` thay vì `type="email"`.
  - Khi nhập `abc` và bấm submit, hệ thống không có thông báo validate nào và vẫn gửi 1 request API lên server (`/api/login` tại Đăng nhập, `/api/forgot-password` tại Quên mật khẩu).

## Bằng chứng

- CL-17 P1 (auto): `../checklist/evidence/auto/P1_CL-17_1.png`
- CL-17 P2 (auto): `../checklist/evidence/auto/P2_CL-17_1.png`
- CL-17 P3 (auto): `../checklist/evidence/auto/P3_CL-17_1.png`
- CL-66 P1 (auto): `../checklist/evidence/auto/P1_CL-66_1.png`
- CL-66 P2 (auto): `../checklist/evidence/auto/P2_CL-66_1.png`
- CL-66 P3 (auto): `../checklist/evidence/auto/P3_CL-66_1.png`

## Item liên quan

- CL-17 – Ô Email dùng type="email" – Failed: P1, P2, P3 · một phần #4 (#4 phủ /login; /forgot-password bước 1 chưa có issue)
- CL-66 – Email sai định dạng bị chặn trước khi gửi – Failed: P1, P2, P3 · một phần #4 (#4 (không kiểm tra định dạng) phủ /login; /forgot-password chưa có issue)
- Nhóm dữ kiện: G-05 trong `HW03/bugs/bug_groups.md` (Ô Email bước 1 Quên mật khẩu: type="text", email sai định dạng vẫn gửi request (phần /login trùng #4)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-02.4 (README.md:44); FR-22.2 (README.md:253):** Ô Email dùng type="email" (CL-17)
- **FR-02.4 (README.md:44); FR-22.2 (README.md:253):** Email sai định dạng bị chặn trước khi gửi (CL-66)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-17 P1 (auto): `Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text"`
- Actual nguyên văn CL-17 P2 (auto): `Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text"`
- Actual nguyên văn CL-17 P3 (auto): `Lỗi: Error: /login ô Email type="text" · Lỗi: Error: /forgot-password ô Email type="text" · /login: type="text"; /forgot-password bước 1: type="text"`
- Nguồn bước tái hiện CL-17: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:89`
- Actual nguyên văn CL-66 P1 (auto): `Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true`
- Actual nguyên văn CL-66 P2 (auto): `Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true`
- Actual nguyên văn CL-66 P3 (auto): `Lỗi: Error: /login: form gửi 1 request /api/login · Lỗi: Error: /login: không có thông báo validate · Lỗi: Error: /forgot-password: form gửi 1 request /api/forgot-password · Lỗi: Error: /forgot-password: không có thông báo validate · /login: 1 request /api/login; validity.valid=true · /forgot-password: 1 request /api/forgot-password; validity.valid=true`
- Nguồn bước tái hiện CL-66: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:99`

### Nhận định

Không kiểm tra định dạng email ở phía giao diện khiến các chuỗi không phải email vẫn phát sinh request gửi lên backend, gây lãng phí tài nguyên xử lý của server và không cảnh báo sớm cho người dùng (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).