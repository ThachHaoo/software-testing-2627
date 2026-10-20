# Môi trường kiểm thử

| Mục | Giá trị |
|---|---|
| SUT | EShop, fork nhóm `tkob-team/eshop-sut` @ `de0f48f` (= `ttbhanh/eshop-sut` `85af3ba` + `.gitignore`, không đổi mã) |
| Máy | [...] (OS, CPU/RAM) |
| Node.js | [...] (`node -v`) |
| Trình duyệt | [...] (tên + phiên bản) |
| Backend / Web / Admin | http://localhost:3000 · :5173 · :5174 |
| Điện thoại | [...] (model, Android/iOS + phiên bản) |
| Expo Go | [...] (bản cho SDK 54) |
| Thay đổi SUT | `frontend-mobile/App.js` dòng 16 `API_URL` → IP LAN `[...]` (xem `mobile_api_url.patch`) |
| Playwright | [...] (`npx playwright --version`) |

## D_FR20 (Mobile, chạy tay — D15)

Giá trị lấy từ nhật ký lượt 1 trong `HW02/D_FR20/RUN.md` (lượt chính thức, 2026-10-21 00:15).

| Mục | Giá trị |
|---|---|
| Máy | Windows 11 Home Single Language 10.0.26200 |
| Điện thoại | POCO F5 · OS 1.0.5.0.UMRTWXM · Android 14 (UKQ1.230804.001) |
| Expo Go | 54.0.8 (SDK 54; `frontend-mobile/package.json`: `expo ~54.0.33`) |
| Locale / bàn phím | Tiếng Việt (Việt Nam) · QWERTY |
| API_URL | `http://192.168.2.12:3000/api` (`frontend-mobile/App.js` dòng 16; `mobile_api_url.patch`) |
**Đặc điểm môi trường ảnh hưởng thiết kế test**
- Backend xoá và seed lại CSDL mỗi lần khởi động; giỏ hàng lưu trong RAM.
- Tài khoản seed: admin `admin@eshop.com` / `Admin123!`, user `test@eshop.com` / `Test1234!` (setup_guide ghi `admin123`, không khớp seed).
