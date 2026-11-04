import { defineConfig } from '@playwright/test';

/**
 * HW03 T1 – phần tự động của checklist C2 (item che_do = auto / phần auto của mixed).
 * P1 = Google Chrome đã cài trên máy (channel "chrome").
 * P2 = Firefox do Playwright tải về (bản build "firefox-<rev>" của Playwright, KHÔNG phải Firefox người dùng cài).
 * P3 = Chrome trên điện thoại Android thật (Playwright _android, cần `adb reverse tcp:5173` + `tcp:3000`).
 * Kết quả = auto_status; verdict chính thức là lượt chạy tay trên trình duyệt thật (report_plan E2).
 * Backend phải vừa khởi động lại (CSDL seed) trước MỖI lượt — global-setup kiểm, thiếu thì dừng.
 */
export default defineConfig({
  testDir: '.',
  testMatch: /C2\.spec\.ts$/,
  globalSetup: './global-setup.ts',
  fullyParallel: false,       // các item dùng chung một CSDL và một tài khoản seed
  workers: 1,
  retries: 0,
  timeout: 60_000,
  reporter: [['list'], ['./reporter.ts']],
  use: {
    baseURL: 'http://localhost:5173',
    viewport: { width: 1280, height: 800 },
    locale: 'vi-VN',
    timezoneId: 'Asia/Ho_Chi_Minh',
    screenshot: 'off',        // ảnh do test tự chụp vào checklist/evidence/auto/
    trace: 'off',
    video: 'off',
  },
  projects: [
    { name: 'P1', use: { browserName: 'chromium', channel: 'chrome' } },
    { name: 'P2', use: { browserName: 'firefox' } },
    // P3 = Chrome Android thật qua _android (fixture context trong lib.ts); browserName chỉ để Playwright có trình duyệt nền, test không dùng
    { name: 'P3', use: { browserName: 'chromium' } },
  ],
});
