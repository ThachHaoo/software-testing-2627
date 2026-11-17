/**
 * MẪU fixture dùng chung (bước 2, v2) — chép sang HW04/tests/fixtures/ddt.ts rồi điều chỉnh theo feature.
 * - loadData(feature): đọc HW04/data/<feature>.json, KIỂM sha1(expected) trước khi chạy (lệch → dừng cả file spec).
 * - assumption(data, key): giả định SV chốt ngoài expected (câu chữ/từ khoá/selector không có trong expected). Thiếu → ném lỗi.
 * - resetDb() + guardWorkers(): restart backend bằng tools/restart_backend.ps1; chỉ an toàn khi workers = 1.
 * - blocked(): Blocked (annotation 'blocked' cho merge_reports.py). step(): CHỈ TimeoutError → Blocked, lỗi khác ném tiếp.
 * - until(): chờ một điều kiện cụ thể (log mạng, số hộp thoại) có hạn; settle(): chờ React render (2 khung hình).
 * - esc(): escape chuỗi trước khi dựng RegExp.
 * - test.extend: fixture `api` (APIRequestContext có token admin) + `adminToken` (worker).
 * Không đặt dữ liệu test trong file này hay trong spec: mọi giá trị vào/expected/giả định nằm ở file data.
 * Bài học review A/B/C (v2): không catch rỗng, không chờ cứng (waitForTimeout), không Promise.race nuốt lỗi.
 */
import { test as base, expect, errors, request, type APIRequestContext, type Page, type TestInfo } from '@playwright/test';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import path from 'node:path';

export const REPO = path.resolve(__dirname, '..', '..', '..');
export const API = 'http://localhost:3000';
export const ADMIN = { email: 'admin@eshop.com', password: 'Admin123!' };   // SRS README.md dòng 22
export const WAIT = 10_000;              // hạn chờ phản hồi mạng/hộp thoại sau thao tác; quá hạn → Blocked

export type Case = {
  tc_id: string; title: string; suite: string; type: string; technique: string; bva_point: string;
  inputs: Record<string, string>; expected: string; expected_sha1: string; notes: string;
  hw02: { status: string; auto_status: string; bug_id: string };
};
export type DataFile = {
  feature: string; source: { file: string; commit: string };
  preconditions: Record<string, string[]>; testcases: Case[];
  assumptions?: Record<string, { value: string; note: string }>;   // giả định SV chốt (không tính sha1)
};

export function loadData(feature: string, file = path.join(REPO, 'HW04', 'data', `${feature}.json`)): DataFile {
  const data = JSON.parse(readFileSync(file, 'utf-8')) as DataFile;
  for (const c of data.testcases) {
    const h = createHash('sha1').update(c.expected, 'utf8').digest('hex');
    if (h !== c.expected_sha1)
      throw new Error(`[ddt] ${c.tc_id}: sha1(expected) lệch — expected đã bị sửa so với HW02 ${data.source.file}@${data.source.commit}`);
  }
  return data;
}

/** Giả định ngoài expected (vd từ khoá thông báo, selector khối thông báo). Thiếu → ném lỗi, KHÔNG đoán, KHÔNG gõ cứng ở spec. */
export function assumption(data: DataFile, key: string) {
  const a = data.assumptions?.[key];
  if (!a?.value) throw new Error(`[ddt] thiếu assumptions.${key} trong HW04/data/${data.feature}.json (giả định chờ SV duyệt)`);
  return a;
}

/** {ts} trong dữ liệu → mốc thời gian của case (email/tên duy nhất). */
export const fill = (v: string | undefined, ts: number | string) => (v ?? '').split('{ts}').join(String(ts));

/** Escape chuỗi lấy từ data/expected trước khi dựng RegExp; nhiều nhánh thì nhóm ^(?:a|b)$, không viết ^a|b. */
export const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Restart backend → CSDL seed sạch. Gọi trong beforeAll SAU guardWorkers(). */
export function resetDb() {
  execFileSync('powershell', ['-ExecutionPolicy', 'Bypass', '-File', path.join(REPO, 'tools', 'restart_backend.ps1')],
    { stdio: 'inherit', timeout: 90_000 });
}
/** resetDb giữa chừng phá dữ liệu của worker khác → chỉ chạy với 1 worker. */
export function guardWorkers(testInfo: TestInfo, feature: string) {
  if (testInfo.config.workers > 1)
    throw new Error(`[${feature}] workers = ${testInfo.config.workers}: resetDb không an toàn khi chạy song song — chạy với --workers=1`);
}

/** Blocked: không kiểm được đúng mục đích vì điều kiện ngoài biến mục tiêu (trường vắng mặt, timeout harness). */
export function blocked(reason: string): never {
  base.info().annotations.push({ type: 'blocked', description: reason });
  base.skip(true, `Blocked: ${reason}`);
  throw new Error('unreachable');
}

/** Bước điều hướng/chuẩn bị (không phải assertion): CHỈ TimeoutError → Blocked; lỗi khác ném tiếp (không catch rỗng). */
export async function step<T>(what: string, fn: () => Promise<T>): Promise<T> {
  try { return await fn(); } catch (e) {
    if (e instanceof errors.TimeoutError) blocked(`${what}: ${String(e).split('\n')[0]}`);
    throw e;
  }
}

/** Chờ một trạng thái rõ ràng phía Node (log mạng, số hộp thoại) tối đa `ms`; quá hạn → Blocked. Không chờ cứng. */
export async function until(what: string, cond: () => boolean, ms = WAIT) {
  const t0 = Date.now();
  while (!cond()) {
    if (Date.now() - t0 > ms) blocked(`${what}: quá ${ms} ms`);
    await new Promise(r => setTimeout(r, 50));
  }
}

/** Đợi React render xong sau khi dữ liệu về (2 khung hình) — dùng SAU khi đã chờ phản hồi mạng. */
export const settle = (page: Page) =>
  page.evaluate(() => new Promise<void>(r => requestAnimationFrame(() => requestAnimationFrame(() => r()))));

/** Ghi mọi response tới `prefix` (gắn TRƯỚC thao tác). `done` = body đã về → mới gọi API đọc dữ liệu SAU. */
export type NetEntry = { method: string; url: string; status: number; done: Promise<unknown> };
export function netLog(page: Page, prefix: string): NetEntry[] {
  const net: NetEntry[] = [];
  page.on('response', r => {
    if (r.url().startsWith(prefix)) net.push({ method: r.request().method(), url: r.url(), status: r.status(), done: r.finished() });
  });
  return net;
}

export const test = base.extend<{ api: APIRequestContext; dialogs: { type: string; message: string }[] }, { adminToken: string }>({
  adminToken: [async ({}, use) => {
    const ctx = await request.newContext();
    const res = await ctx.post(`${API}/api/login`, { data: ADMIN });
    if (res.status() !== 200) throw new Error(`[ddt] không đăng nhập được ${ADMIN.email}: HTTP ${res.status()}`);
    await use((await res.json()).token);
    await ctx.dispose();
  }, { scope: 'worker' }],
  api: async ({ adminToken }, use) => {
    const ctx = await request.newContext({ baseURL: API, extraHTTPHeaders: { Authorization: `Bearer ${adminToken}` } });
    await use(ctx);
    await ctx.dispose();
  },
  /** Ghi mọi hộp thoại (alert/confirm) rồi đóng: confirm → accept chỉ khi procedure có bước "xác nhận"; mặc định dismiss. */
  dialogs: async ({ page }, use) => {
    const log: { type: string; message: string }[] = [];
    page.on('dialog', d => { log.push({ type: d.type(), message: d.message() }); void d.dismiss(); });
    await use(log);
  },
});
export { expect };
