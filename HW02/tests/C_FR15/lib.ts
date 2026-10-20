/**
 * Helper cho test FR-15 Quản lý Sản phẩm (HW02/C_FR15). Dữ liệu và Expected đọc từ ../../C_FR15/testcases.json —
 * file này chỉ chứa cách THỰC HIỆN procedure và cách QUAN SÁT, không chứa dữ liệu test.
 * Quy ước annotation (merge_results.py): "actual" = quan sát, "verdict" = Blocked khi không dựng được tiền điều kiện (C14).
 * Định vị ô theo placeholder như procedure TS-DOM-UI bước 5 (form không có nhãn).
 */
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { test as base, expect, APIRequestContext, Page, TestInfo } from '@playwright/test';
import type { Name } from './oracle';

export const API = 'http://localhost:3000';
export const ADMIN_UI = 'http://localhost:5174';

export const data = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../../C_FR15/testcases.json'), 'utf-8'));
export const suites: Record<string, any> = Object.fromEntries(data.suites.map((s: any) => [s.id, s]));

/** Dấu vân tay của expected_result: oracle viết theo bản Expected này; Expected đổi → test báo lỗi để cập nhật oracle. */
export const hashOf = (s: string) => crypto.createHash('sha1').update(s, 'utf8').digest('hex').slice(0, 8);

// ---------------- Dữ liệu lấy từ testcases.json ----------------
const pre: string[] = suites['TS-DOM-UI'].preconditions;
// "Có token admin TA: POST /api/login với admin@eshop.com / Admin123! (README.md dòng 22) — …"
const adm = /với (\S+@\S+) \/ (\S+?)\s/.exec(pre.find(p => p.includes('/api/login'))!)!;
export const ADMIN = { email: adm[1], password: adm[2] };
// Procedure TS-DOM-API bước 3: "POST /api/login với test@eshop.com / Test1234! (README.md dòng 23) → token U."
const usr = /với (\S+@\S+) \/ (\S+?)\s/.exec(suites['TS-DOM-API-POST'].procedure[2].action)!;
export const USER = { email: usr[1], password: usr[2] };
// Procedure TS-DOM-API bước 4: "'sai' = 'Bearer abc.def.ghi'"
export const BAD_TOKEN = /'sai' = '(Bearer [^']+)'/.exec(suites['TS-DOM-API-POST'].procedure[3].action)![1];
// Procedure bước 1 (dựng M): "body {name: 'Muc tieu NN {ts}', price: 1000000, description: '…', imageUrl: '…', category_id: 1}"
const mb = /name: '(.+?)', price: (\d+), description: '(.+?)', imageUrl: '(.+?)', category_id: (\d+)/.exec(suites['TS-DOM-UI'].procedure[0].action)!;
export const M_TEMPLATE = { name: mb[1], price: Number(mb[2]), description: mb[3], imageUrl: mb[4], category_id: Number(mb[5]) };
// Procedure TS-DOM-UI bước 5: danh mục chọn theo tên; seed (database.js dòng 84–88) ghi trong preconditions
export const CATEGORY: Record<string, number> = {};
for (const m of pre[0].matchAll(/id (\d+) '([^']+)'/g)) CATEGORY[m[2]] = Number(m[1]);

/** Thay {ts} và NN (số TC) trong giá trị lấy từ JSON. */
export const fill = (s: string, ts: string, nn: string) => s.split('{ts}').join(ts).split('NN').join(nn);
export const nameOf = (n: Name, ts: string, nn: string) => typeof n === 'string' ? fill(n, ts, nn) : n.rep.repeat(n.n);
/** 'x' × 300 / "x" × 300 → 'xxx…' (UI); trả null nếu không phải dạng lặp. */
export const repeatOf = (s: string) => { const m = /^['"](.)['"] × (\d+)$/.exec(s.trim()); return m ? m[1].repeat(Number(m[2])) : null; };

// ---------------- API + dọn dẹp (C0) ----------------
export class SetupError extends Error {}
export type Product = { id: number; name: any; price: any; description: any; imageUrl: any; category_id: any };

export async function login(request: APIRequestContext, who: { email: string; password: string }) {
  const r = await request.post(`${API}/api/login`, { data: who });
  const j = await r.json().catch(() => ({}));
  if (r.status() !== 200 || !j.token) throw new SetupError(`POST /api/login ${who.email}: HTTP ${r.status()}`);
  return j.token as string;
}
export async function listProducts(request: APIRequestContext): Promise<{ list: Product[]; text: string; status: number }> {
  const r = await request.get(`${API}/api/products`);
  const text = await r.text();
  let list: Product[] = [];
  try { list = JSON.parse(text); } catch { /* giữ list rỗng; status/text ghi vào Actual */ }
  return { list: Array.isArray(list) ? list : [], text, status: r.status() };
}
export async function getProduct(request: APIRequestContext, id: number) {
  const r = await request.get(`${API}/api/products/${id}`);
  const text = await r.text();
  let body: any = null;
  try { body = JSON.parse(text); } catch { /* body không phải JSON */ }
  return { status: r.status(), text, body };
}
/** Dựng sản phẩm mục tiêu M theo procedure bước 1; trả id M (tìm theo name trong GET /api/products). */
export async function createM(request: APIRequestContext, ta: string, ts: string, nn: string) {
  const body = { ...M_TEMPLATE, name: fill(M_TEMPLATE.name, ts, nn), description: fill(M_TEMPLATE.description, ts, nn) };
  const r = await request.post(`${API}/api/products`, { data: body, headers: { Authorization: `Bearer ${ta}` } });
  const { list } = await listProducts(request);
  const hit = list.filter(p => p.name === body.name);
  if (r.status() < 200 || r.status() > 299 || hit.length !== 1)
    throw new SetupError(`Không dựng được M '${body.name}': POST HTTP ${r.status()}, tìm thấy ${hit.length} bản ghi`);
  return { id: hit[0].id, body };
}

/**
 * Fixture `env`: ghi tập id TRƯỚC khi case chạy; sau case (kể cả Fail) xoá mọi id mới xuất hiện (lớp 1, C0).
 * Xoá thất bại → annotation "cleanup", không đổi verdict.
 */
export const test = base.extend<{ env: { ta: string; ts: string; startIds: Set<number> } }>({
  env: async ({ request }, use, info) => {
    const ta = await login(request, ADMIN);
    const ts = String(Date.now());
    const startIds = new Set((await listProducts(request)).list.map(p => p.id));
    await use({ ta, ts, startIds });
    try {
      const { list } = await listProducts(request);
      for (const p of list.filter(p => !startIds.has(p.id))) {
        const r = await request.delete(`${API}/api/products/${p.id}`, { headers: { Authorization: `Bearer ${ta}` } });
        if (r.status() < 200 || r.status() > 299)
          info.annotations.push({ type: 'cleanup', description: `Xoá sản phẩm id ${p.id} thất bại: HTTP ${r.status()} — C0, không đổi verdict` });
      }
    } catch (e) {
      info.annotations.push({ type: 'cleanup', description: `Cleanup lỗi: ${(e as Error).message} — C0, không đổi verdict` });
    }
  },
});
export { expect };

/** Lớp 2 (quét cuối lượt): xoá mọi sản phẩm không thuộc tập id lúc đầu lượt hoặc có tên chứa mốc {ts} của lượt này. */
export async function sweep(request: APIRequestContext, runStartIds: Set<number>, runStart: number) {
  const ta = await login(request, ADMIN);
  const { list } = await listProducts(request);
  const stamp = (n: any) => [...String(n ?? '').matchAll(/\d{13}/g)].some(m => Number(m[0]) >= runStart);
  const left: string[] = [];
  for (const p of list.filter(p => !runStartIds.has(p.id) || stamp(p.name))) {
    const r = await request.delete(`${API}/api/products/${p.id}`, { headers: { Authorization: `Bearer ${ta}` } });
    if (r.status() < 200 || r.status() > 299) left.push(`id ${p.id} (HTTP ${r.status()})`);
  }
  return left;
}

// ---------------- Bằng chứng ----------------
export async function shot(page: Page, info: TestInfo, name: string) {
  const p = info.outputPath(`${name}.png`);
  await page.screenshot({ path: p, fullPage: true });
  await info.attach(name, { path: p, contentType: 'image/png' });
}
export async function attachJson(info: TestInfo, name: string, obj: unknown) {
  const p = info.outputPath(`${name}.json`);
  fs.writeFileSync(p, JSON.stringify(obj, null, 2), 'utf-8');
  await info.attach(name, { path: p, contentType: 'application/json' });
}
const esc = (s: string) => s.replace(/[&<>]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[ch]!));
/** Ảnh cho report: render từ response thật (không phải ảnh giao diện SUT). */
export async function renderResponse(page: Page, info: TestInfo, id: string, text: string) {
  await page.setContent(`<pre style="font:14px monospace;white-space:pre-wrap">${esc(text)}</pre>`);
  await shot(page, info, `${id}_api`);
}

// ---------------- Số tiền ----------------
/** "1.500.000 ₫" | "1,500,000 ₫" | "199999.5 ₫" | "199.999,5 ₫" → số; không đọc được → NaN (C17: '.' hoặc ',' phân cách hàng nghìn). */
export function money(s: string | null | undefined): number {
  const t = String(s ?? '').replace(/₫|đ|VND/g, '').replace(/\s/g, '');
  if (/^-?\d+([.,]\d+)?$/.test(t) && !/^-?\d{1,3}[.,]\d{3}$/.test(t)) return Number(t.replace(',', '.'));
  if (/^-?\d{1,3}(\.\d{3})+(,\d+)?$/.test(t)) return Number(t.replace(/\./g, '').replace(',', '.'));
  if (/^-?\d{1,3}(,\d{3})+(\.\d+)?$/.test(t)) return Number(t.replace(/,/g, ''));
  return NaN;
}
/** So giá trị số; số nguyên vượt Number.MAX_SAFE_INTEGER thì so trên chuỗi. */
export function sameNumber(actual: any, expected: number) {
  if (!Number.isSafeInteger(expected) && Number.isInteger(expected)) return String(actual) === String(BigInt(expected));
  return actual !== null && actual !== '' && Number(actual) === expected;
}

// ---------------- UI admin ----------------
export const ERR = /lỗi|error|không hợp lệ|invalid|bắt buộc|required|please|vui lòng/i;

export async function uiLogin(page: Page) {
  await page.goto(ADMIN_UI);
  await page.getByPlaceholder('Email').fill(ADMIN.email);
  await page.getByPlaceholder('Password').fill(ADMIN.password);
  await page.getByRole('button', { name: 'Login' }).click();
  await page.locator('li', { hasText: /^Sản phẩm$/ }).click();
  await expect(productForm(page)).toBeVisible({ timeout: 10_000 });
}
export const productForm = (page: Page) => page.locator('form', { has: page.getByRole('button', { name: 'Lưu sản phẩm' }) });
export const productTable = (page: Page) => page.locator('table', { has: page.locator('th', { hasText: 'Tên SP' }) });

export type UiRow = { name: string; priceText: string; price: number };
/** Đọc bảng sản phẩm: cột 2 = Tên SP, cột 3 = Giá. Chờ số dòng ổn định. */
export async function readTable(page: Page, wantRows?: number): Promise<UiRow[]> {
  const rows = productTable(page).locator('tbody tr');
  if (wantRows !== undefined) await expect(rows).toHaveCount(wantRows, { timeout: 5_000 }).catch(() => {});
  await page.waitForTimeout(300);
  const raw = await rows.evaluateAll(trs => trs.map(tr => [...tr.querySelectorAll('td')].map(td => (td.textContent ?? '').replace(/\s+/g, ' ').trim())));
  return raw.map(c => ({ name: c[1] ?? '', priceText: c[2] ?? '', price: money(c[2]) }));
}
export const rowByName = (page: Page, name: string) =>
  productTable(page).locator('tbody tr').filter({ has: page.locator('td:nth-child(2)', { hasText: new RegExp(`^${name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}$`) }) });

/** Nhập một ô theo procedure bước 5: '(giữ)' bỏ qua; '' để trống; 'x' × n dán; còn lại gõ đúng chuỗi. */
export async function setField(page: Page, field: 'Tên sản phẩm' | 'Giá' | 'Danh mục' | 'Mô tả' | 'URL Ảnh', v: string) {
  if (v === '(giữ)' || v === '—') return;
  const form = productForm(page);
  if (field === 'Danh mục') { await form.locator('select').selectOption({ label: v }); return; }
  const ph = { 'Tên sản phẩm': 'Tên sản phẩm', 'Giá': 'Giá tiền', 'Mô tả': 'Mô tả', 'URL Ảnh': 'URL Ảnh' }[field];
  const box = form.getByPlaceholder(ph, { exact: true });
  await box.fill('');
  if (v === '') return;
  const rep = repeatOf(v);
  if (rep !== null) { await box.fill(rep); return; }
  if (/[０-９]/.test(v)) { await box.focus(); await page.keyboard.insertText(v); return; }   // chữ số full-width: dán (SV TC-205)
  await box.pressSequentially(v);
}

/** Bấm nút một lần rồi thu: hộp thoại trình duyệt (chấp nhận), ô không hợp lệ HTML5 (validationMessage). */
export async function clickAndObserve(page: Page, click: () => Promise<void>) {
  const dialogs: string[] = [];
  const onDialog = (d: any) => { dialogs.push(d.message()); d.accept().catch(() => {}); };
  page.on('dialog', onDialog);
  const invalid = await (async () => {
    await click();
    await page.waitForTimeout(1200);
    return productForm(page).evaluate((f: HTMLFormElement) =>
      [...f.elements].filter((e: any) => e.willValidate && !e.checkValidity()).map((e: any) => `${e.placeholder || e.tagName}: ${e.validationMessage}`));
  })();
  page.off('dialog', onDialog);
  return { dialogs, invalid };
}

// ---------------- Kết thúc case ----------------
export function finish(info: TestInfo, obs: string[], verdict?: { v: 'Blocked'; why: string }) {
  if (verdict) info.annotations.push({ type: 'verdict', description: verdict.v });
  info.annotations.push({ type: 'actual', description: (verdict ? `${verdict.v}: ${verdict.why} | ` : '') + obs.join('; ') });
}
