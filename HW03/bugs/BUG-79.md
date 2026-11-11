# BUG-79

- **ID:** BUG-79
- **Tiêu đề:** [Lịch sử đơn] Thiếu trạng thái đang tải (loading indicator) khi lấy dữ liệu lịch sử đơn hàng
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-79]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay · CL-63: lượt `runs/P1_manual_20261109-2257.md`, 22:58 09/11/2026 - 00:10 10/11/2026
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay · CL-63: lượt `runs/P2_manual_20261110-0010.md`, 00:10 10/11/2026 - 00:38 10/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay · CL-63: lượt `runs/P3_manual_20261110-0046.md`, 00:46 10/11/2026 - 01:54 10/11/2026
- Màn hình: CL-63 – Lịch sử đơn
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Tài khoản `test@eshop.com` / `Test1234!` đã được đăng nhập và có sẵn ít nhất 1 đơn hàng trong lịch sử. Đã bật Network Throttling ở chế độ Slow 3G.

## Các bước tái hiện

1. Đăng nhập tài khoản `test@eshop.com` / `Test1234!` và đảm bảo tài khoản đã có lịch sử đơn hàng.
2. Mở DevTools -> tab Network -> chỉnh tốc độ mạng sang **Slow 3G**.
3. Tải lại trang Hồ sơ / Lịch sử đơn (`http://localhost:5173/profile`).
4. Quan sát giao diện khu vực danh sách đơn hàng trong quá trình chờ dữ liệu từ API gửi về.

## Expected (trích căn cứ)

- CL-63 – căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống)
- Expected của bug: Khi bật Network throttling 'Slow 3G' và tải lại `/profile`, trong lúc chờ phản hồi từ máy chủ giao diện phải có chỉ báo đang tải (loading indicator/spinner); không được hiển thị trạng thái rỗng "chưa có đơn hàng" trước khi dữ liệu trả về.

## Actual

- Cả P1 (Cốc Cốc), P2 (Firefox) và P3 (Chrome Android): Hoàn toàn không có chỉ báo trạng thái đang tải khi hệ thống đang lấy dữ liệu lịch sử đơn.
- Trên P1: Màn hình hiển thị trạng thái rỗng ("chưa có đơn hàng") trước khi danh sách đơn hàng thực tế kịp tải ra.
- Trên P2 và P3: Trang tải xong là tất cả dữ liệu cũng xong hết (không giống Chrome khi tải từng phần).

## Bằng chứng

- CL-63 P1 (tay): `../checklist/evidence/P1_chrome/P1_CL-63_1.png`, `../checklist/evidence/P1_chrome/P1_CL-63_2.png`
- CL-63 P2 (tay): `../checklist/evidence/P2_firefox/P2_CL-63_1.png`
- CL-63 P3 (tay): `../checklist/evidence/P3_android/P3_CL-63_1.png`, `../checklist/evidence/P3_android/P3_CL-63_2.png`

## Item liên quan

- CL-63 – Có trạng thái đang tải khi lấy lịch sử đơn – Failed: P1, P2, P3
- Nhóm dữ kiện: G-22 trong `HW03/bugs/bug_groups.md` (Lịch sử đơn: không có trạng thái đang tải); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Nielsen #1 (hiển thị trạng thái hệ thống):** Có trạng thái đang tải khi lấy lịch sử đơn (CL-63)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-63 P1 (tay): `Không có trạng thái đang tải`
- Actual nguyên văn CL-63 P2 (tay): `Không có trạng thái đang tải, trang tải xong là tất cả dữ liệu cũng xong hết (không giống Chrome khi tải từng phần)`
- Actual nguyên văn CL-63 P3 (tay): `Không có trạng thái đang tải, trang tải xong là tất cả dữ liệu cũng xong hết (không giống Chrome khi tải từng phần)`
- Nguồn bước tái hiện CL-63: tiền điều kiện (checklist): Có ≥ 1 đơn. P3: throttling qua chrome://inspect. · cách kiểm: auto (P1, CDP Slow 3G): empty state hiện trước khi dữ liệu về / có chỉ báo tải; P2 chạy tay · test tự động: `HW03/tests/C2.spec.ts:772`

### Nhận định

Thiếu phản hồi trạng thái đang tải khi kết nối mạng chậm gây ra hiểu nhầm là tài khoản chưa có đơn hàng hoặc ứng dụng bị đơ, không tuân thủ nguyên tắc Nielsen #1 về phản hồi trạng thái hệ thống (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).