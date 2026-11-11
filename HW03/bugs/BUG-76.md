# BUG-76

- **ID:** BUG-76
- **Tiêu đề:** [Hồ sơ] Truy cập /profile khi chưa đăng nhập không tự chuyển và thiếu link tới Đăng nhập
- **Severity:** Medium
- **Priority:** Medium
- Tiền tố GitHub: [HW03-C2-76]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-49: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-49: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-49: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-49 – Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Trạng thái người dùng chưa đăng nhập.

## Các bước tái hiện

1. Đảm bảo trình duyệt ở trạng thái chưa đăng nhập tài khoản.
2. Mở trình duyệt và truy cập trực tiếp vào đường dẫn trang Hồ sơ (`http://localhost:5173/profile`).
3. Quan sát hành vi điều hướng URL của trình duyệt và kiểm tra sự tồn tại của nút/liên kết Đăng nhập trong vùng nội dung trang.

## Expected (trích căn cứ)

- CL-49 – căn cứ: Nielsen #3 (lối thoát); Nielsen #9
- Expected của bug: Khi chưa đăng nhập, truy cập đường dẫn `/profile` hệ thống phải tự động chuyển hướng người dùng về trang Đăng nhập (`/login`).
- 
## Actual

- Cả P1, P2 và P3: Khi chưa đăng nhập, mở `/profile` hệ thống không tự động chuyển hướng về `/login` (URL vẫn giữ nguyên `/profile`). Trong vùng nội dung trang không có bất kỳ nút hoặc liên kết nào dẫn tới trang Đăng nhập (số liên kết/nút tới Đăng nhập trong trang = 0, ngoại trừ thanh Navbar).

## Bằng chứng

- CL-49 P1 (auto): `../checklist/evidence/auto/P1_CL-49_1.png`, `../checklist/evidence/auto/P1_CL-49_2.png`
- CL-49 P2 (auto): `../checklist/evidence/auto/P2_CL-49_1.png`, `../checklist/evidence/auto/P2_CL-49_2.png`
- CL-49 P3 (auto): `../checklist/evidence/auto/P3_CL-49_1.png`, `../checklist/evidence/auto/P3_CL-49_2.png`

## Item liên quan

- CL-49 – /profile khi chưa đăng nhập dẫn được tới Đăng nhập – Failed: P1, P2, P3
- Nhóm dữ kiện: G-19 trong `HW03/bugs/bug_groups.md` (/profile khi chưa đăng nhập: không chuyển, không có link tới Đăng nhập); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Nielsen #3 (lối thoát); Nielsen #9:** /profile khi chưa đăng nhập dẫn được tới Đăng nhập (CL-49)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-49 P1 (auto): `Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0`
- Actual nguyên văn CL-49 P2 (auto): `Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0`
- Actual nguyên văn CL-49 P3 (auto): `Lỗi: Error: không tự chuyển và không có link/nút tới Đăng nhập · URL: /profile; link/nút tới Đăng nhập trong trang: 0`
- Nguồn bước tái hiện CL-49: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:256`

### Nhận định

Trang không có cơ chế bảo vệ tuyến đường (route guard) hoặc không cung cấp lối thoát/điều hướng phù hợp cho người dùng chưa xác thực, làm ảnh hưởng đến luồng trải nghiệm người dùng (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).