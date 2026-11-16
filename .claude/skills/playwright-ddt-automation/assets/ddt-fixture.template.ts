/**
 * MẪU fixture dùng chung (bước 2) — chép sang HW04/tests/fixtures/ddt.ts rồi điều chỉnh theo feature.
 * - loadCases(feature): đọc HW04/data/<feature>.json, KIỂM sha1(expected) trước khi chạy (lệch → dừng cả file).
 * - resetDb(): restart backend bằng tools/restart_backend.ps1 (CSDL seed lại) — gọi trong beforeAll khi cần.
 * - test.extend: fixture `api` (APIRequestContext có token admin) + `adminToken`.
 * Không đặt dữ liệu test trong file này hay trong spec: mọi giá trị vào/expected nằm ở file data.
 */
import { test as base, expect, request, type APIRequestContext } from '@playwright/test';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import path from 'node:path';

const REPO = path.resolve(__dirname, '..', '..', '..');
export const API = 'http://localhost:3000';
export const ADMIN = { email: 'admin@eshop.com', password: 'Admin123!' };   // SRS README.md dòng 22

export type Case = {
  tc_id: string; title: string; suite: string; type: string; technique: string; bva_point: string;
  inputs: Record<string, string>; expected: string; expected_sha1: string; notes: string;
  hw02: { status: string; auto_status: string; bug_id: string };
};

export function loadCases(feature: string): Case[] {
  const file = path.join(REPO, 'HW04', 'data', `${feature}.json`);
  const data = JSON.parse(readFileSync(file, 'utf-8')) as { testcases: Case[] };
  for (const c of data.testcases) {
    const h = createHash('sha1').update(c.expected, 'utf8').digest('hex');
    if (h !== c.expected_sha1) throw new Error(`[ddt] ${c.tc_id}: sha1(expected) lệch — expected đã bị sửa so với HW02 (${file})`);
  }
  return data.testcases;
}

/** {ts} trong dữ liệu → Date.now() để email duy nhất (quy ước HW02, giả định A19). */
export const fill = (v: string, ts: number) => v.replaceAll('{ts}', String(ts));

export function resetDb() {
  execFileSync('powershell', ['-ExecutionPolicy', 'Bypass', '-File', path.join(REPO, 'tools', 'restart_backend.ps1')],
    { stdio: 'inherit', timeout: 60_000 });
}

/** Đánh dấu Blocked (merge_reports.py đọc annotation 'blocked') rồi bỏ qua phần còn lại của test. */
export function blocked(reason: string) {
  test.info().annotations.push({ type: 'blocked', description: reason });
  test.skip(true, `Blocked: ${reason}`);
}

export const test = base.extend<{ api: APIRequestContext }, { adminToken: string }>({
  adminToken: [async ({}, use) => {
    const ctx = await request.newContext();
    const res = await ctx.post(`${API}/api/login`, { data: ADMIN });
    expect(res.status(), 'đăng nhập admin').toBe(200);
    await use((await res.json()).token);
    await ctx.dispose();
  }, { scope: 'worker' }],
  api: async ({ adminToken }, use) => {
    const ctx = await request.newContext({ baseURL: API, extraHTTPHeaders: { Authorization: `Bearer ${adminToken}` } });
    await use(ctx);
    await ctx.dispose();
  },
});
export { expect };
