# BUG-75

- **ID:** BUG-75
- **Tiêu đề:** [Hồ sơ, Navbar] Đổi Họ Tên không cập nhật ngay trên Navbar khi chưa tải lại trang
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-75]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-56: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-56: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-56: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-56 – Hồ sơ, Navbar
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Đã đăng nhập bằng tài khoản `test@eshop.com` / `Test1234!` (tên hiển thị mặc định là "Test User") và đang ở trang Hồ sơ (`http://localhost:5173/profile`).

## Các bước tái hiện

1. Truy cập trang Đăng nhập (`http://localhost:5173/login`) và đăng nhập bằng tài khoản `test@eshop.com` / `Test1234!`.
2. Mở trang Hồ sơ (`http://localhost:5173/profile`).
3. Nhập tên mới 'Test Đổi' vào ô "Họ Tên".
4. Bấm nút 'Cập nhật'.
5. Quan sát thông tin tên người dùng hiển thị trên thanh Navbar mà không bấm tải lại trang (F5).

## Expected (trích căn cứ)

- CL-56 – căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống); Shneiderman #1
- Expected của bug: Đổi Họ Tên thành 'Test Đổi' -> bấm Cập nhật -> Navbar phải cập nhật ngay tên mới 'Test Đổi' mà không cần tải lại trang.

## Actual

- Cả P1, P2 và P3: Sau khi đổi Họ Tên thành 'Test Đổi' và bấm 'Cập nhật', thanh Navbar vẫn giữ nguyên tên cũ ("EShop | Giỏ hàng | Chào, Test User | Thoát") dù đã chờ 3000 ms, chỉ cập nhật tên mới sau khi tải lại trang (F5).

## Bằng chứng

- CL-56 P1 (auto): `../checklist/evidence/auto/P1_CL-56_1.png`
- CL-56 P2 (auto): `../checklist/evidence/auto/P2_CL-56_1.png`
- CL-56 P3 (auto): `../checklist/evidence/auto/P3_CL-56_1.png`

## Item liên quan

- CL-56 – Đổi Họ Tên cập nhật ngay trên navbar – Failed: P1, P2, P3
- Nhóm dữ kiện: G-18 trong `HW03/bugs/bug_groups.md` (Navbar: đổi Họ Tên, navbar giữ tên cũ tới khi tải lại); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Nielsen #1 (hiển thị trạng thái hệ thống); Shneiderman #1:** Đổi Họ Tên cập nhật ngay trên navbar (CL-56)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-56 P1 (auto): `Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát"`
- Actual nguyên văn CL-56 P2 (auto): `Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát"`
- Actual nguyên văn CL-56 P3 (auto): `Lỗi: Error: navbar vẫn tên cũ khi chưa tải lại · navbar sau 3000 ms (không tải lại): "EShop | Giỏ hàng | Chào, Test User | Thoát"`
- Nguồn bước tái hiện CL-56: tiền điều kiện (checklist): Khôi phục 'Test User' sau khi kiểm. · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:562`

### Nhận định

State quản lý thông tin người dùng trên Navbar chưa phản ánh kịp thời sự thay đổi dữ liệu ở giao diện Hồ sơ, làm giảm khả năng phản hồi trạng thái hệ thống theo thời gian thực (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).