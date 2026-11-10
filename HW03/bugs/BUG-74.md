# BUG-74

- **ID:** BUG-74
- **Tiêu đề:** [Navbar] Nút đăng xuất hiển thị nhãn "Thoát" thay vì "Đăng xuất"
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-74]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-42: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-42: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-42: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-42 – Navbar
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Backend vừa restart. Người dùng đã đăng nhập thành công bằng tài khoản `test@eshop.com` / `Test1234!`.

## Các bước tái hiện

1. Truy cập trang Đăng nhập (`http://localhost:5173/login`).
2. Đăng nhập bằng tài khoản `test@eshop.com` / `Test1234!`.
3. Quan sát nhãn nút đăng xuất ở thanh điều hướng Navbar phía trên cùng của trang.

## Expected (trích căn cứ)

- CL-42 – căn cứ: FR-23.3 (README.md:262)
  - FR-23.3, README.md:262 (AI chép nguyên văn): Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát").
- Expected của bug: Khi đã đăng nhập, nút đăng xuất trên thanh Navbar phải hiển thị đúng nhãn 'Đăng xuất'.

## Actual

- Cả P1, P2 và P3: Khi ở trạng thái đã đăng nhập, nút đăng xuất trên thanh Navbar hiển thị nhãn là "Thoát" thay vì "Đăng xuất".

## Bằng chứng

- CL-42 P1 (auto): `../checklist/evidence/auto/P1_CL-42_1.png`
- CL-42 P2 (auto): `../checklist/evidence/auto/P2_CL-42_1.png`
- CL-42 P3 (auto): `../checklist/evidence/auto/P3_CL-42_1.png`

## Item liên quan

- CL-42 – Nút đăng xuất có nhãn 'Đăng xuất' – Failed: P1, P2, P3
- Nhóm dữ kiện: G-17 trong `HW03/bugs/bug_groups.md` (Navbar: nút đăng xuất nhãn "Thoát"); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **FR-23.3 (README.md:262):** Nút đăng xuất có nhãn 'Đăng xuất' (CL-42)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-42 P1 (auto): `Lỗi: Error: nhãn là "Thoát" · nhãn nút: "Thoát"`
- Actual nguyên văn CL-42 P2 (auto): `Lỗi: Error: nhãn là "Thoát" · nhãn nút: "Thoát"`
- Actual nguyên văn CL-42 P3 (auto): `Lỗi: Error: nhãn là "Thoát" · nhãn nút: "Thoát"`
- Nguồn bước tái hiện CL-42: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:619`

### Nhận định

Nhãn của nút đăng xuất không tuân thủ chính xác quy định FR-23.3 trong SRS, làm ảnh hưởng đến tính nhất quán thuật ngữ trên giao diện (chưa kiểm chứng).

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/256

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).