# BUG-78

- **ID:** BUG-78
- **Tiêu đề:** [Đăng nhập, Quên MK, Hồ sơ] Nút submit không khóa và thiếu chỉ báo khi bấm nhiều lần
- **Severity:** Medium
- **Priority:** Medium
- Tiền tố GitHub: [HW03-C2-78]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay · CL-53: lượt `runs/P1_manual_20261109-2257.md`, 22:58 09/11/2026 - 00:10 10/11/2026
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · SV-06: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay · CL-53: lượt `runs/P2_manual_20261110-0010.md`, 00:10 10/11/2026 - 00:38 10/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · SV-06: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay · CL-53: lượt `runs/P3_manual_20261110-0046.md`, 00:46 10/11/2026 - 01:54 10/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · SV-06: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-53 – Đăng nhập; SV-06 – Quên mật khẩu B1 / B2, Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Màn hình Hồ sơ (`http://localhost:5173/profile`) đã đăng nhập tài khoản `test@eshop.com` / `Test1234!`. Kiểm tra CL-53 cần bật DevTools Network Throttling ở chế độ Slow 3G.

## Các bước tái hiện

1. **Tại trang Đăng nhập (`http://localhost:5173/login`):** Bật throttling mạng Slow 3G, nhập thông tin đăng nhập rồi bấm nút 'Sign In' liên tục (3 lần). Quan sát trạng thái nút và số request phát sinh trong DevTools Network.
2. **Tại trang Quên mật khẩu B1 (`http://localhost:5173/forgot-password`):** Ở điều kiện mạng bình thường, nhập email hợp lệ rồi nhấp chuột thật nhanh (double-click) vào nút 'Lấy mã OTP'. Kiểm tra số request gửi đi.
3. **Tại trang Quên mật khẩu B2:** Nhập OTP đúng và mật khẩu mới, nhấp chuột thật nhanh vào nút 'Đặt lại mật khẩu'. Kiểm tra số request và số hộp thoại hiển thị.
4. **Tại trang Hồ sơ (`http://localhost:5173/profile`):** Nhập thông tin cập nhật, nhấp chuột thật nhanh vào nút 'Cập nhật'. Kiểm tra số request và số hộp thoại hiển thị.

## Expected (trích căn cứ)

- CL-53 – căn cứ: Norman – Feedback; Shneiderman #3 (phản hồi đầy đủ)
- SV-06 – căn cứ: Slide "Double-submit on double-click"; Nielsen #5 (Phòng ngừa lỗi)
- Expected của bug: Bấm nút submit, trong lúc chờ xử lý (kể cả mạng Slow 3G), nút phải bị vô hiệu hóa hoặc có chỉ báo đang tải, bấm nhiều lần chỉ phát sinh 1 request. Ở điều kiện mạng bình thường, nhấp đúp nhanh vào nút submit ('Lấy mã OTP', 'Đặt lại mật khẩu', 'Cập nhật') hệ thống phải lập tức khóa nút hoặc debounce sao cho chỉ phát sinh đúng 1 request API và không hiển thị nhiều thông báo trùng lặp.

## Actual

- **Tại trang Đăng nhập (CL-53):** Ở cả P1, P2, P3 khi thử nghiệm với Slow 3G, nút submit 'Sign In' không có chỉ báo đang xử lý (loading) và không vô hiệu hóa để chống gửi trùng.
- **Khi nhấp đúp nhanh ở điều kiện mạng bình thường (SV-06):**
  - **Nút 'Lấy mã OTP' (Quên MK B1):** Phát sinh 2 request API gửi lên server ở cả P1, P2 và P3.
  - **Nút 'Đặt lại mật khẩu' (Quên MK B2):** Bị phát sinh 0 request và xuất hiện 2 hộp thoại alert trùng lặp ở P1, P2.
  - **Nút 'Cập nhật' (Hồ sơ):** Bị phát sinh 0 request PUT và xuất hiện 2 hộp thoại alert trùng lặp ở P1, P2. Trên P3 bị TimeoutError do dblclick.

## Bằng chứng

- CL-53 P1 (tay): `../checklist/evidence/P1_chrome/P1_CL-53_1.png`
- CL-53 P2 (tay): `../checklist/evidence/P2_firefox/P2_CL-53_1.png`
- CL-53 P3 (tay): `../checklist/evidence/P3_android/P3_CL-53_1.png`
- SV-06 P1 (auto): `../checklist/evidence/auto/P1_SV-06_1.png`
- SV-06 P2 (auto): `../checklist/evidence/auto/P2_SV-06_1.png`
- SV-06 P3 (auto): `../checklist/evidence/auto/P3_SV-06_1.png`

## Item liên quan

- CL-53 – Có chỉ báo đang xử lý và chống gửi trùng – Failed: P1, P2, P3
- SV-06 – Chống gửi trùng dữ liệu (Debounce/Disable) khi nhấp đúp/nhấp liên tiếp vào nút submit ở điều kiện mạng bình thường – Failed: P1, P2, P3
- Nhóm dữ kiện: G-21 trong `HW03/bugs/bug_groups.md` (Nút submit không khoá / không có chỉ báo khi bấm nhiều lần (Đăng nhập, Quên MK B1/B2, Hồ sơ)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Norman – Feedback; Shneiderman #3 (phản hồi đầy đủ):** Có chỉ báo đang xử lý và chống gửi trùng (CL-53)
- **Slide "Double-submit on double-click"; Nielsen #5 (Phòng ngừa lỗi):** Chống gửi trùng dữ liệu (Debounce/Disable) khi nhấp đúp/nhấp liên tiếp vào nút submit ở điều kiện mạng bình thường (SV-06)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-53 P1 (tay): `Không có đang xử lý và chống gửi trùng`
- Actual nguyên văn CL-53 P2 (tay): `Không có đang xử lý và chống gửi trùng`
- Actual nguyên văn CL-53 P3 (tay): `Không có đang xử lý và chống gửi trùng`
- Nguồn bước tái hiện CL-53: tiền điều kiện (checklist): P3: throttling qua chrome://inspect. · cách kiểm: auto (P1, CDP Slow 3G): nút disabled/đổi chữ/aria-busy + số request; chỉ báo khác → SV; P2 chạy tay · test tự động: `HW03/tests/C2.spec.ts:823`
- Actual nguyên văn SV-06 P1 (auto): `Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: Error: Đặt lại mật khẩu: 0 request, 2 hộp thoại · Lỗi: Error: Cập nhật: 0 request PUT, 2 hộp thoại · Lấy mã OTP: 2 request · Đặt lại mật khẩu: 0 request, 2 hộp thoại · Cập nhật: 0 request PUT, 2 hộp thoại`
- Actual nguyên văn SV-06 P2 (auto): `Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: Error: Đặt lại mật khẩu: 0 request, 2 hộp thoại · Lỗi: Error: Cập nhật: 0 request PUT, 2 hộp thoại · Lấy mã OTP: 2 request · Đặt lại mật khẩu: 0 request, 2 hộp thoại · Cập nhật: 0 request PUT, 2 hộp thoại`
- Actual nguyên văn SV-06 P3 (auto): `Lỗi: Error: Lấy mã OTP: 2 request · Lỗi: TimeoutError: locator.dblclick: Timeout 30000ms exceeded. · Lấy mã OTP: 2 request`
- Nguồn bước tái hiện SV-06: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:914`

### Nhận định

Không khóa nút submit hoặc debounce khi bấm liên tục/nhấp đúp dẫn đến việc gửi trùng lặp request API hoặc xuất hiện nhiều hộp thoại thông báo trùng lặp, tiềm ẩn rủi ro lãng phí tài nguyên máy chủ và gửi dữ liệu lặp lại (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).