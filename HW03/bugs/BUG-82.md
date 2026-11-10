# BUG-82

- **ID:** BUG-82
- **Tiêu đề:** [Đăng nhập, Quên MK, Hồ sơ] Không sử dụng được tính năng tự động điền (Autofill) của trình duyệt
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-82]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay · SV-02: lượt `runs/P1_manual_20261109-2257.md`, 22:58 09/11/2026 - 00:10 10/11/2026
- P2 – Firefox 159.0.1 / Windows 11 – chạy tay · SV-02: lượt `runs/P2_manual_20261110-0010.md`, 00:10 10/11/2026 - 00:38 10/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay · SV-02: lượt `runs/P3_manual_20261110-0046.md`, 00:46 10/11/2026 - 01:54 10/11/2026
- Màn hình: SV-02 – Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend server đang hoạt động bình thường. Trình duyệt đã được lưu sẵn thông tin biểu mẫu / tài khoản tự động điền (Autofill). Màn hình Hồ sơ (`http://localhost:5173/profile`) yêu cầu đã đăng nhập.

## Các bước tái hiện

1. Sử dụng trình duyệt đã có lưu thông tin Autofill.
2. Truy cập lần lượt các trang: Đăng nhập (`http://localhost:5173/login`), Quên mật khẩu (`http://localhost:5173/forgot-password`), và Hồ sơ (`http://localhost:5173/profile`).
3. Nhấp vào các ô nhập liệu (Email, Mật khẩu, OTP, Họ Tên, SĐT, Địa chỉ) và kiểm tra khả năng xuất hiện/chọn gợi ý tự động điền (Autofill) của trình duyệt.
4. Thử thực hiện thao tác dán dữ liệu (Paste / Ctrl+V) vào từng ô nhập liệu.

## Expected (trích căn cứ)

- SV-02 – căn cứ: Shneiderman #8 (Giảm tải trí nhớ ngắn hạn); Nielsen #7 (Linh hoạt và hiệu quả); Slide "Checklist - Text Box"
- Expected của bug: Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit.

## Actual

- **Thao tác Dán (Paste):** Tất cả các ô nhập liệu trên P1, P2 và P3 đều dán được bình thường.
- **Tính năng Tự động điền (Autofill):**
  - **Trên P1 (Cốc Cốc):** Gợi ý Autofill chỉ xuất hiện và sử dụng được ở trang Quên mật khẩu (`/forgot-password`). Màn hình Đăng nhập và Hồ sơ không Autofill được.
  - **Trên P2 (Firefox) và P3 (Chrome Android):** Tất cả các ô nhập liệu ở cả 3 trang đều hoàn toàn không sử dụng được tính năng Autofill.

## Bằng chứng

- SV-02 P1 (tay): `../checklist/evidence/P1_chrome/P1_SV-02_1.png`, `../checklist/evidence/P1_chrome/P1_SV-02_2.png`, `../checklist/evidence/P1_chrome/P1_SV-02_3.png`, `../checklist/evidence/P1_chrome/P1_SV-02_4.png`
- SV-02 P2 (tay): `../checklist/evidence/P2_firefox/P2_SV-02_1.png`, `../checklist/evidence/P2_firefox/P2_SV-02_2.png`, `../checklist/evidence/P2_firefox/P2_SV-02_3.png`, `../checklist/evidence/P2_firefox/P2_SV-02_4.png`
- SV-02 P3 (tay): `../checklist/evidence/P3_android/P3_SV-02_1.png`, `../checklist/evidence/P3_android/P3_SV-02_2.png`, `../checklist/evidence/P3_android/P3_SV-02_3.png`, `../checklist/evidence/P3_android/P3_SV-02_4.png`

## Item liên quan

- SV-02 – Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu – Failed: P1, P2, P3
- Nhóm dữ kiện: G-25 trong `HW03/bugs/bug_groups.md` (Autofill của trình duyệt không điền được (dán được)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Shneiderman #8 (Giảm tải trí nhớ ngắn hạn); Nielsen #7 (Linh hoạt và hiệu quả); Slide "Checklist - Text Box":** Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu (SV-02)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn SV-02 P1 (tay): `Tất cả đều có thể Paste vào, nhưng Autofill chỉ có ở Forgot Password.`
- Actual nguyên văn SV-02 P2 (tay): `Tất cả đều có thể Paste vào, nhưng không thể Autofill`
- Actual nguyên văn SV-02 P3 (tay): `Tất cả đều có thể Paste vào, nhưng không thể Autofill`
- Nguồn bước tái hiện SV-02: tiền điều kiện (checklist): Trình duyệt đã lưu thông tin đăng nhập/tài khoản trước đó. · cách kiểm: auto (P1): dán bằng Ctrl+V vào ô Email; Autofill + P2 → chạy tay · test tự động: `HW03/tests/C2.spec.ts:854`

### Nhận định

Các trường nhập liệu có thể đang thiếu thuộc tính HTML chuẩn (`autocomplete`, `name`, `id` phù hợp) khiến trình duyệt không nhận diện đúng ngữ cảnh để hỗ trợ điền nhanh, làm tăng thao tác nhập tay của người dùng (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).