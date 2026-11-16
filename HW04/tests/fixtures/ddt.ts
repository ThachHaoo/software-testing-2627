/**
 * Fixture dùng chung cho mọi feature HW04 (skill playwright-ddt-automation, bước 2).
 * - loadCases(feature): đọc HW04/data/<feature>.json, KIỂM sha1(expected) trước khi chạy (lệch → dừng cả file spec).
 * - resetDb(): restart backend bằng tools/restart_backend.ps1 (CSDL xoá + seed lại).
 * - blocked(reason): đánh dấu Blocked (annotation 'blocked' cho merge_reports.py) rồi bỏ qua phần còn lại.
 * - fixture `adminToken` (worker) + `api` (APIRequestContext có token admin, baseURL backend).
 * File này không chứa dữ liệu test: giá trị vào và expected nằm ở file data.
 */
import { test as base, expect, request, type APIRequestContext } from '@playwright/test';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import path from 'node:path';

export const REPO = path.resolve(__dirname, '..', '..', '..');
export const API = 'http://localhost:3000';
export const WEB = 'http://localhost:5173';
export const ADMIN_WEB = 'http://localhost:5174';
export const ADMIN = { email: 'admin@eshop.com', password: 'Admin123!' };   // SRS ../eshop-sut/README.md dòng 22

export type Case = {
  tc_id: string; title: string; suite: string; type: string; technique: string; bva_point: string;
  inputs: Record<string, string>; expected: string; expected_sha1: string; notes: string;
  hw02: { status: string; auto_status: string; bug_id: string };
};
export type DataFile = {
  feature: string; source: { file: string; commit: string };
  preconditions: Record<string, string[]>; testcases: Case[];
};

export function loadData(feature: string): DataFile {
  const file = path.join(REPO, 'HW04', 'data', `${feature}.json`);
  const data = JSON.parse(readFileSync(file, 'utf-8')) as DataFile;
  for (const c of data.testcases) {
    const h = createHash('sha1').update(c.expected, 'utf8').digest('hex');
    if (h !== c.expected_sha1)
      throw new Error(`[ddt] ${c.tc_id}: sha1(expected) lệch — expected đã bị sửa so với HW02 ${data.source.file}@${data.source.commit}`);
  }
  return data;
}
export const loadCases = (feature: string): Case[] => loadData(feature).testcases;

/** {ts} trong dữ liệu → mốc thời gian của case, để email là duy nhất (quy ước HW02, giả định A19). */
export const fill = (v: string | undefined, ts: number | string) => (v ?? '').split('{ts}').join(String(ts));

/** Restart backend → CSDL seed sạch. Gọi trong beforeAll; mất mọi tài khoản/giỏ đã tạo. */
export function resetDb() {
  execFileSync('powershell', ['-ExecutionPolicy', 'Bypass', '-File', path.join(REPO, 'tools', 'restart_backend.ps1')],
    { stdio: 'inherit', timeout: 90_000 });
}

/** Blocked: không kiểm được đúng mục đích vì điều kiện ngoài biến mục tiêu (trường vắng mặt, lỗi chặn đường). */
export function blocked(reason: string): never {
  base.info().annotations.push({ type: 'blocked', description: reason });
  base.skip(true, `Blocked: ${reason}`);
  throw new Error('unreachable');
}

export const test = base.extend<{ api: APIRequestContext }, { adminToken: string }>({
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
});
export { expect };
