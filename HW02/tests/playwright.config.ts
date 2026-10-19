import { defineConfig } from '@playwright/test';

// SUT chạy local (xem HW02/env/environment.md). Backend reseed CSDL mỗi lần khởi động.
export default defineConfig({
  testDir: './specs',
  fullyParallel: false,          // các test dùng chung một CSDL SQLite
  workers: 1,
  retries: 0,                    // không che lỗi bằng chạy lại; flaky thì điều tra (skill qa-evidence-review)
  reporter: [['list'], ['json', { outputFile: process.env.PLAYWRIGHT_JSON_OUTPUT_NAME || 'results/last.json' }]],
  use: {
    screenshot: 'on',
    trace: 'retain-on-failure',
    locale: 'vi-VN',
    timezoneId: 'Asia/Ho_Chi_Minh',
  },
  projects: [
    { name: 'web',   use: { baseURL: 'http://localhost:5173' }, testMatch: /(A_FR01|B_FR07)\..*spec\.ts/ },
    { name: 'admin', use: { baseURL: 'http://localhost:5174' }, testMatch: /C_FR15\..*spec\.ts/ },
    { name: 'api',   use: { baseURL: 'http://localhost:3000' }, testMatch: /\.api\.spec\.ts/ },
  ],
});
