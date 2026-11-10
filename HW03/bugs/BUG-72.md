# BUG-72

- **ID:** BUG-72
- **Tiêu đề:** [Hồ sơ] SĐT không bắt đầu bằng 0 ('912345678') vẫn được lưu và thông báo không nêu quy tắc
- **Severity:** High
- **Priority:** Medium
- Tiền tố GitHub: [HW03-C2-72]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-32: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-32: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-32: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-32 – Hồ sơ
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Backend vừa restart. Đã đăng nhập tài khoản `test@eshop.com` / `Test1234!` và truy cập trang Hồ sơ (`http://localhost:5173/profile`).

## Các bước tái hiện

1. Mở trình duyệt và truy cập trang Đăng nhập (`http://localhost:5173/login`), đăng nhập bằng tài khoản `test@eshop.com` / `Test1234!`.
2. Truy cập vào trang Hồ sơ (`http://localhost:5173/profile`).
3. Nhập giá trị `912345678` (SĐT không bắt đầu bằng 0, gồm 9 chữ số) vào ô nhập "Số điện thoại".
4. Bấm nút 'Cập nhật' và quan sát nội dung thông báo hiển thị.
5. Tải lại trang (nhấn F5) và kiểm tra lại giá trị hiển thị ở ô "Số điện thoại".

## Expected (trích căn cứ)

- CL-32 – căn cứ: FR-04.2 (README.md:65); Nielsen #9
  - FR-04.2, README.md:65 (AI chép nguyên văn): **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.
- Expected của bug: Nhập '912345678' (không bắt đầu bằng 0) phải bị hệ thống từ chối, không lưu vào cơ sở dữ liệu; thông báo phải nêu rõ quy tắc (bắt đầu bằng 0, 10–11 chữ số).

## Actual

- Cả P1, P2 và P3: Khi nhập '912345678' và bấm 'Cập nhật', hệ thống hiển thị thông báo "Cập nhật thành công!" (không nêu quy tắc SĐT hợp lệ phải bắt đầu bằng 0 và dài 10–11 chữ số). Sau khi nhấn F5 tải lại trang, ô "Số điện thoại" vẫn lưu và hiển thị giá trị không hợp lệ "912345678".

## Bằng chứng

- CL-32 P1 (auto): `../checklist/evidence/auto/P1_CL-32_1.png`
- CL-32 P2 (auto): `../checklist/evidence/auto/P2_CL-32_1.png`
- CL-32 P3 (auto): `../checklist/evidence/auto/P3_CL-32_1.png`

## Item liên quan

- CL-32 – SĐT không hợp lệ bị từ chối, thông báo nêu đúng quy tắc – Failed: P1, P2, P3 · một phần #97, #113 (#97 (API lưu SĐT 9 số), #113 (Web nhận đầu khác 0); phần thông báo không nêu quy tắc chưa có issue)
- Nhóm dữ kiện: G-15 trong `HW03/bugs/bug_groups.md` (Hồ sơ: SĐT '912345678' được lưu, thông báo không nêu quy tắc (phần lưu liên quan #97/#113)); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-04.2 (README.md:65); Nielsen #9:** SĐT không hợp lệ bị từ chối, thông báo nêu đúng quy tắc (CL-32)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-32 P1 (auto): `Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"`
- Actual nguyên văn CL-32 P2 (auto): `Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"`
- Actual nguyên văn CL-32 P3 (auto): `Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"`
- Nguồn bước tái hiện CL-32: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:488`

### Nhận định

Hệ thống cho phép lưu thông tin số điện thoại sai định dạng vào cơ sở dữ liệu làm sai lệch dữ liệu người dùng. Việc thông báo thành công thay vì báo lỗi không hướng dẫn người dùng nhập đúng quy tắc SRS (chưa kiểm chứng). Liên quan issue #97, #113.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).