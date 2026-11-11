# BUG-58

- **ID:** BUG-58
- **Tiêu đề:** [Đăng nhập, Quên MK] Focus nhảy ngược và bỏ qua Navbar khi nhấn Tab
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-58]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-10: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-12: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-10: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-12: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- Màn hình: CL-10 – Đăng nhập; CL-12 – Quên mật khẩu (bước 2)
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend đang hoạt động. Trạng thái người dùng chưa đăng nhập.

## Các bước tái hiện

1. Mở trình duyệt và truy cập vào trang Đăng nhập (http://localhost:5173/login).
2. Từ lúc trang vừa tải xong, nhấn phím `Tab` liên tục và quan sát thứ tự focus của các phần tử trên màn hình.
3. Chuyển sang màn hình Quên mật khẩu bước 2 (http://localhost:5173/forgot-password, nhập email rồi qua bước 2), tiếp tục nhấn phím `Tab` liên tục từ đầu trang và quan sát.

## Expected (trích căn cứ)

- CL-10 – căn cứ: FR-21.5 (README.md:248)
  - FR-21.5, README.md:248 (AI chép nguyên văn): **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.
- CL-12 – căn cứ: FR-21.5 (README.md:248)
  - FR-21.5, README.md:248 (AI chép nguyên văn): **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.
- Expected của bug: Từ đầu trang bấm Tab liên tục, focus phải đi qua mọi control tương tác được theo vị trí hiển thị — từ trên xuống dưới, trái sang phải. Không được nhảy tới control nằm phía trên (hoặc bên trái) control trước đó, và không được bỏ qua các control trên Navbar.

## Actual

- **Tại trang Đăng nhập (CL-10):**
  - Cả P1 và P2: Focus nhảy ngược vị trí hiển thị. Điểm focus đầu tiên rơi vào nút 'Sign In' ở form, sau đó mới nhảy ngược lên liên kết 'EShop' ở Navbar rồi đi tiếp tuần tự.
  - Trên P2: Khi focus đến liên kết 'Đăng ký ngay', tiếp tục bấm Tab sẽ bị lặp vô tận tại liên kết này.
- **Tại trang Quên mật khẩu B2 (CL-12):**
  - Cả P1 và P2: Focus bỏ qua hoàn toàn các liên kết trên Navbar ('EShop', 'Giỏ hàng', 'Đăng nhập', 'Đăng ký'), chỉ đi qua các ô nhập liệu và nút trong form.
  - Trên P2: Khi focus đến nút '← Quay lại', tiếp tục bấm Tab sẽ bị lặp vô tận tại nút này.

## Bằng chứng

- CL-10 P1 (auto): `../checklist/evidence/auto/P1_CL-10_1.png`
- CL-10 P2 (auto): `../checklist/evidence/auto/P2_CL-10_1.png`
- CL-12 P1 (auto): `../checklist/evidence/auto/P1_CL-12_1.png`
- CL-12 P2 (auto): `../checklist/evidence/auto/P2_CL-12_1.png`

## Item liên quan

- CL-10 – Thứ tự Tab theo vị trí hiển thị (trên→dưới, trái→phải) – Failed: P1, P2
- CL-12 – Thứ tự Tab ở bước 2 theo vị trí hiển thị (trên→dưới, trái→phải) – Failed: P1, P2
- Nhóm dữ kiện: G-01 trong `HW03/bugs/bug_groups.md` (Thứ tự Tab không theo vị trí hiển thị (focus bắt đầu ở form, navbar bị đi sau / bỏ qua)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-21.5 (README.md:248):** Thứ tự Tab theo vị trí hiển thị (trên→dưới, trái→phải) (CL-10)
- **FR-21.5 (README.md:248):** Thứ tự Tab ở bước 2 theo vị trí hiển thị (trên→dưới, trái→phải) (CL-12)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-10 P1 (auto): `Lỗi: Error: nhảy ngược: 'Sign In'(449,425) → 'EShop'(16,16) · chuỗi Tab: button'Sign In'@(449,425) → a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) → input'text'@(449,241) → input'text'@(449,331) → a'Quên mật khẩu?'@(729,389) → a'Đăng ký ngay'@(659,481)`
- Actual nguyên văn CL-10 P2 (auto): `Lỗi: Error: nhảy ngược: 'Sign In'(449,425) → 'EShop'(16,16) · chuỗi Tab: button'Sign In'@(449,425) → a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) → input'text'@(449,241) → input'text'@(449,331) → a'Quên mật khẩu?'@(729,390) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482) → a'Đăng ký ngay'@(658,482)`
- Nguồn bước tái hiện CL-10: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:230`
- Actual nguyên văn CL-12 P1 (auto): `Lỗi: Error: bỏ qua: a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) · chuỗi Tab: input'text'@(449,301) → input'password'@(449,391) → button'Đặt lại mật khẩu'@(449,449) → button'← Quay lại'@(449,505)`
- Actual nguyên văn CL-12 P2 (auto): `Lỗi: Error: bỏ qua: a'EShop'@(16,16) → a'Giỏ hàng'@(1032,20) → a'Đăng nhập'@(1112,20) → a'Đăng ký'@(1206,20) · chuỗi Tab: input'text'@(449,301) → input'password'@(449,391) → button'Đặt lại mật khẩu'@(449,449) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505) → button'← Quay lại'@(449,505)`
- Nguồn bước tái hiện CL-12: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:390`

### Nhận định

Người dùng điều hướng bằng bàn phím sẽ gặp rắc rối lớn do con trỏ focus bị nhảy lộn xộn, không tuân thủ thứ tự hiển thị tự nhiên của mắt (chưa kiểm chứng). Tại màn Quên mật khẩu B2, họ không thể truy cập các chức năng trên Navbar theo chiều bấm Tab thông thường (chưa kiểm chứng). Hiện tượng vòng lặp focus trên Firefox (P2) sẽ gây kẹt và chặn thao tác bàn phím (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/261

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
