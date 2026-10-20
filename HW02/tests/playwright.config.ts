import { defineConfig } from '@playwright/test';

// SUT chạy local (xem HW02/env/environment.md). Backend reseed CSDL mỗi lần khởi động.
export default defineConfig({
  testDir: '.',
  globalSetup: './global-setup.ts',   // kiểm backend/web/admin trước khi chạy; thiếu thì dừng
  fullyParallel: false,          // các test dùng chung một CSDL SQLite
  workers: 1,
  retries: 0,                    // không che lỗi bằng chạy lại; flaky thì điều tra (skill qa-evidence-review)
  reporter: [['list'], ['json', { outputFile: process.env.PLAYWRIGHT_JSON_OUTPUT_NAME || 'results/last.json' }]],
  use: {
    screenshot: 'only-on-failure',   // ảnh bằng chứng chính do test tự chụp (TC-xx.png); tránh ảnh trùng
    trace: 'retain-on-failure',
    video: 'off',
    locale: 'vi-VN',
    timezoneId: 'Asia/Ho_Chi_Minh',
  },
  projects: [
    { name: 'A_FR01', use: { baseURL: 'http://localhost:5173' }, testMatch: /A_FR01[\\/].*\.spec\.ts$/ },
    { name: 'B_FR07', use: { baseURL: 'http://localhost:5173' }, testMatch: /B_FR07[\\/].*\.spec\.ts$/ },
    { name: 'web',  use: { baseURL: 'http://localhost:5173' }, testMatch: /specs[\\/]B_FR07\..*spec\.ts$/ },
    { name: 'admin', use: { baseURL: 'http://localhost:5174' }, testMatch: /specs[\\/]C_FR15\..*spec\.ts$/ },
    { name: 'api',   use: { baseURL: 'http://localhost:3000' }, testMatch: /specs[\\/].*\.api\.spec\.ts$/ },
  ],
});
