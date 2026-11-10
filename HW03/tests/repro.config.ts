import { defineConfig } from '@playwright/test';

/**
 * HW03 T1 bước 5/6e – AI tái hiện Steps SV viết trong bugs/BUG-58…85.md (chỉ ghi quan sát, không chấm Pass/Fail).
 *   npx playwright test -c repro.config.ts --project=P1   (backend vừa restart, web :5173 nhánh main)
 * Kết quả: ../bugs/repro/repro_<P>.json. Không dùng locale ép (mặc định của Playwright) trừ chỗ ghi rõ.
 */
export default defineConfig({
  testDir: '.',
  testMatch: /repro_bugs\.spec\.ts$/,
  fullyParallel: false,
  workers: 1,
  retries: 0,
  timeout: 90_000,
  reporter: [['list']],
  use: { baseURL: 'http://localhost:5173', viewport: { width: 1280, height: 800 }, screenshot: 'off', trace: 'off', video: 'off' },
  projects: [
    { name: 'P1', use: { browserName: 'chromium', channel: 'chrome' } },
    { name: 'P2', use: { browserName: 'firefox' } },
  ],
});
