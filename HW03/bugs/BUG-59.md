# BUG-59

- **ID:** BUG-59
- **Tiêu đề:** [Tất cả màn C2] Tiêu đề tab hiển thị "frontend-web" giống hệt nhau ở mọi trang
- **Severity:** Low
- **Priority:** Low
- Tiền tố GitHub: [HW03-C2-59]

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)
- P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11 · CL-13: lượt `runs/P1_auto_20261109-2236.json`, 22:36 09/11/2026
- P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11 · CL-13: lượt `runs/P2_auto_20261109-2240.json`, 22:40 09/11/2026
- P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android · CL-13: lượt `runs/P3_auto_20261109-2244.json`, 22:44 09/11/2026
- Màn hình: CL-13 – Tất cả màn C2
- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5

## Tiền điều kiện

Hệ thống frontend web và backend đang hoạt động bình thường.

## Các bước tái hiện

1. Mở trình duyệt và truy cập lần lượt vào các trang: Đăng nhập (`/login`), Quên mật khẩu (`/forgot-password`), và Hồ sơ (`/profile`).
2. Quan sát tiêu đề thẻ tab hiển thị trên trình duyệt (hoặc mở DevTools -> Console và kiểm tra giá trị `document.title`).

## Expected (trích căn cứ)

- CL-13 – căn cứ: Nielsen #1 (hiển thị trạng thái hệ thống); WCAG 2.2 SC 2.4.2
- Expected của bug: Tiêu đề tab (`document.title`) phải chứa tên ứng dụng hoặc tên trang tương ứng (ví dụ: 'Đăng nhập – EShop') và phải khác biệt giữa các trang `/login`, `/forgot-password`, `/profile`.

## Actual

- Cả P1, P2 và P3: Tiêu đề tab ở cả 3 trang (`/login`, `/forgot-password`, `/profile`) đều hiển thị chung một chuỗi là `"frontend-web"`. Tiêu đề hoàn toàn giống nhau và không hề chứa tên ứng dụng hay tên trang cụ thể.

## Bằng chứng

- CL-13 P1 (auto): `../checklist/evidence/auto/P1_CL-13_1.png`
- CL-13 P2 (auto): `../checklist/evidence/auto/P2_CL-13_1.png`
- CL-13 P3 (auto): `../checklist/evidence/auto/P3_CL-13_1.png`

## Item liên quan

- CL-13 – Tiêu đề tab trình duyệt mô tả trang – Failed: P1, P2, P3
- Nhóm dữ kiện: G-02 trong `HW03/bugs/bug_groups.md` (Tiêu đề tab là "frontend-web" ở mọi trang); kiểm trùng: `HW03/bugs/dup_check.md`

## Yêu cầu

(AI điền từ `bug_groups.md`, SV duyệt)

- **Nielsen #1 (hiển thị trạng thái hệ thống); WCAG 2.2 SC 2.4.2:** Tiêu đề tab trình duyệt mô tả trang (CL-13)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn CL-13 P1 (auto): `Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"]`
- Actual nguyên văn CL-13 P2 (auto): `Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"]`
- Actual nguyên văn CL-13 P3 (auto): `Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title "frontend-web" không chứa tên ứng dụng/tên trang · Lỗi: Error: title giống nhau giữa các trang · title: ["frontend-web","frontend-web","frontend-web"]`
- Nguồn bước tái hiện CL-13: tiền điều kiện (checklist): – · cách kiểm: auto · test tự động: `HW03/tests/C2.spec.ts:71`

### Nhận định

Người dùng sẽ gặp khó khăn trong việc nhận diện và điều hướng giữa các trang khi mở nhiều tab cùng lúc do tiêu đề đều hiển thị "frontend-web", làm giảm khả năng nhận biết trạng thái hệ thống (chưa kiểm chứng).

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).
