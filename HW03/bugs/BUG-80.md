# BUG-80

- **ID:** BUG-80
- **Tiêu đề:** [Lịch sử đơn] Ngày đặt không đúng định dạng dd/mm/yyyy và không nhất quán giữa các nền tảng
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-80]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay · CL-09: lượt `runs/P1_manual_20261109-2257.md`, 22:58 09/11/2026 - 00:10 10/11/2026
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay · CL-09: lượt `runs/P2_manual_20261110-0010.md`, 00:10 10/11/2026 - 00:38 10/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay · CL-09: lượt `runs/P3_manual_20261110-0046.md`, 00:46 10/11/2026 - 01:54 10/11/2026
- Màn hình: CL-09 – Lịch sử đơn
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Đã đăng nhập tài khoản `test@eshop.com` / `Test1234!` và tài khoản có sẵn ít nhất 1 đơn hàng trong lịch sử.

## Các bước tái hiện

1. Truy cập trang Đăng nhập (`http://localhost:5173/login`) và đăng nhập bằng tài khoản `test@eshop.com` / `Test1234!`.
2. Truy cập vào trang Hồ sơ / Lịch sử đơn hàng (`http://localhost:5173/profile`).
3. Quan sát định dạng hiển thị của cột/dòng "Ngày đặt" trong danh sách đơn hàng.

## Expected (trích căn cứ)

- CL-09 – căn cứ: Nielsen #4 (nhất quán và chuẩn); SRS im lặng → giả định GA1
  - Giả định trong checklist (AI chép nguyên văn): GA1: ngày hiển thị theo chuẩn Việt Nam dd/mm/yyyy, độc lập ngôn ngữ trình duyệt.
- Expected của bug: Ngày đặt hiển thị dạng dd/mm/yyyy và giống nhau trên P1, P2, P3.

## Actual

- **Trên P1 (Cốc Cốc):** Ngày đặt hiển thị dạng "9/11/2026" (ngày 1 chữ số, không đúng chuẩn 2 chữ số dd/mm/yyyy).
- **Trên P2 (Firefox) và P3 (Chrome Android):** Ngày đặt hiển thị dạng mm/dd/yyyy ("11/9/2026") thay vì định dạng dd/mm/yyyy của người Việt.
- Định dạng ngày đặt hiển thị không nhất quán giữa các nền tảng (P1 hiện "9/11/2026" trong khi P2 và P3 hiện "11/9/2026").

## Bằng chứng

- CL-09 P1 (tay): `../checklist/evidence/P1_chrome/P1_CL-09_1.png`
- CL-09 P2 (tay): `../checklist/evidence/P2_firefox/P2_CL-09_1.png`
- CL-09 P3 (tay): `../checklist/evidence/P3_android/P3_CL-09_1.png`

## Item liên quan

- CL-09 – Ngày đặt hiển thị nhất quán theo định dạng Việt Nam – Failed: P1, P2, P3
- Nhóm dữ kiện: G-23 trong `HW03/bugs/bug_groups.md` (Lịch sử đơn: Ngày đặt khác định dạng giữa các nền tảng); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Nielsen #4 (nhất quán và chuẩn); SRS im lặng → giả định GA1:** Ngày đặt hiển thị nhất quán theo định dạng Việt Nam (CL-09)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-09 P1 (tay): `[SV chốt R11=b: Expected "dd/mm/yyyy và giống nhau trên P1, P2, P3" áp cho cả P1; ảnh P1_CL-09_1 hiện "9/11/2026" (ngày 1 chữ số, không phải dd/mm/yyyy), P2/P3 hiện "11/9/2026" → khác nhau giữa các nền tảng (lý do lấy từ khuyến nghị run_check R11, SV có thể sửa)] · [trước quyết định: auto Failed ≠ tay Passed; cả hai cùng thấy "9/11/2026" (ảnh P1_CL-09_1); khác ở cách chấm ngưỡng dd/mm/yyyy (run_check R11)]`
- Actual nguyên văn CL-09 P2 (tay): `Sử dụng định dạng mm/dd/yyyy thay vì dd/mm/yyyy của người Việt`
- Actual nguyên văn CL-09 P3 (tay): `Sử dụng định dạng mm/dd/yyyy thay vì dd/mm/yyyy của người Việt`
- Nguồn bước tái hiện CL-09: tiền điều kiện (checklist): Có ≥ 1 đơn. · cách kiểm: auto: định dạng trên từng nền tảng; so giữa P1/P2/P3 khi gộp · test tự động: `HW03/tests/C2.spec.ts:685`

### Nhận định

Ngày đặt hiển thị không đồng nhất giữa các nền tảng và vi phạm chuẩn định dạng dd/mm/yyyy của Việt Nam, gây nhầm lẫn cho người dùng khi đọc thông tin ngày tháng (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/272

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).