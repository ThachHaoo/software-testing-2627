# Môi trường chạy HW03 (ghi 2026-11-05)

| Thành phần | Phiên bản | Ghi chú |
|---|---|---|
| OS (PC) | Windows 11 Home Single Language 10.0.26200 | P1, P2 |
| Node.js | v24.15.0 | backend :3000, vite :5173 |
| Playwright | 1.48.2 | `HW03/tests` |
| P1 – Google Chrome (Windows) | 157.0.8103.39 | cài mặc định ở Program Files; Playwright dùng `channel: "chrome"` (cả lượt auto và chạy tay) |
| P2 – Mozilla Firefox (Windows, bản thật) | 159.0.1 | chạy tay P2 (verdict chính thức) |
| P2 – Firefox của Playwright (`firefox-1465`) | 131.0 | chỉ lượt auto (`auto_status`); khác bản thật → không thay chạy tay |
| P3 – Chrome Android | 156.0.8078.79 | POCO F5 (model 23049PCD8G), Android 14, USB debugging + `adb reverse` |
| adb | platform-tools 37.0.1 | |
