import { defineConfig, devices } from '@playwright/test';
import path from 'node:path';

// "Run by" + ISO timestamp bắt buộc trong mọi HTML report (đề HW04 §6, §11).
const STUDENT_ID = '23120255';

// Mốc thời gian của lượt chạy: tính một lần ở tiến trình chính, worker kế thừa qua biến môi trường.
function isoLocal(d: Date): string {
  const off = -d.getTimezoneOffset();
  const pad = (n: number) => String(Math.abs(n)).padStart(2, '0');
  const local = new Date(d.getTime() + off * 60_000).toISOString().slice(0, 19);
  return `${local}${off >= 0 ? '+' : '-'}${pad(Math.trunc(off / 60))}:${pad(off % 60)}`;
}
process.env.HW04_RUN_ISO ??= isoLocal(new Date());
const RUN_ISO = process.env.HW04_RUN_ISO;
const RUN_TAG = RUN_ISO.slice(0, 19).replace(/[-:]/g, '');          // 20261116T223005

// Tên thư mục report = project được chọn (--project=chrome …); chạy nhiều project một lượt → nối bằng "+".
const projects = process.argv
  .flatMap((a, i, all) => (a.startsWith('--project=') ? [a.slice(10)] : a === '--project' ? [all[i + 1]] : []))
  .filter(Boolean);
const PROJECT_TAG = projects.length ? projects.join('+') : 'all';
const RUN_BY = `Run by: ${STUDENT_ID} · ${RUN_ISO}`;
const REPORT_DIR = path.join(__dirname, '..', 'reports', `${PROJECT_TAG}_${RUN_TAG}`);

export default defineConfig({
  testDir: '.',                       // spec đặt thẳng trong HW04/tests/<X_FRnn>.spec.ts
  testMatch: /.*\.spec\.ts$/,
  globalSetup: './global-setup.ts',   // kiểm backend/web/admin trước khi chạy; thiếu thì dừng
  fullyParallel: false,               // các test dùng chung một CSDL SQLite
  workers: 1,
  retries: 0,                         // không che lỗi bằng chạy lại; flaky thì điều tra
  outputDir: './test-results',
  metadata: { 'Run by': `${STUDENT_ID} · ${RUN_ISO}` },
  reporter: [
    ['list'],
    ['html', {
      title: `HW04 EShop – ${PROJECT_TAG} – ${RUN_BY}`,
      outputFolder: REPORT_DIR,
      open: 'never',
    }],
    // results.json cạnh index.html — merge_reports.py (skill playwright-ddt-automation, bước 6) đọc file này
    ['json', { outputFile: path.join(REPORT_DIR, 'results.json') }],
  ],
  use: {
    screenshot: 'only-on-failure',
    trace: 'retain-on-failure',
    video: 'off',
    locale: 'vi-VN',
    timezoneId: 'Asia/Ho_Chi_Minh',
  },
  projects: [
    // W1=a: WebKit bị Windows Smart App Control chặn → Chrome / Edge / Firefox (đề HW04 §6 cho phép).
    { name: 'chrome', use: { ...devices['Desktop Chrome'], channel: 'chrome' } },
    { name: 'edge', use: { ...devices['Desktop Edge'], channel: 'msedge' } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
  ],
});
