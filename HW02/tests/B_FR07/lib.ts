/**
 * Helper cho test FR-07 Giỏ hàng (HW02/B_FR07). Dữ liệu và Expected đọc từ ../../B_FR07/testcases.json —
 * file này chỉ chứa cách THỰC HIỆN procedure và cách QUAN SÁT, không chứa dữ liệu test.
 * Quy ước annotation (merge_results.py): "actual" = quan sát, "verdict" = Blocked khi không kiểm được đúng mục đích (B20).
 * Định vị phần tử theo procedure TS-DOM-UI bước 3 (cấu trúc bảng/vị trí), không dựa vào đúng chữ nhãn — trừ TC-95…98.
 */
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { test as base, expect, APIRequestContext, Locator, Page, TestInfo } from '@playwright/test';

export const API = 'http://localhost:3000';
export const WEB = 'http://localhost:5173';

export const data = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../../B_FR07/testcases.json'), 'utf-8'));
export const suites: Record<string, any> = Object.fromEntries(data.suites.map((s: any) => [s.id, s]));
export const allCases: any[] = data.suites.flatMap((s: any) => s.cases);

/** Dấu vân tay của expected_result: spec ghi oracle theo bản Expected này; Expected đổi → test báo lỗi để cập nhật oracle. */
export const hashOf = (s: string) => crypto.createHash('sha1').update(s, 'utf8').digest('hex').slice(0, 8);

// ---------------- Dữ liệu lấy từ testcases.json ----------------
const pre: string[] = suites['TS-DOM-UI'].preconditions;
// "Sản phẩm seed (database.js dòng 98–102): id 1 'iPhone 15 Pro Max' 30.000.000 ₫ · …"
export const PRODUCTS: Record<number, { name: string; price: number }> = {};
for (const m of pre.find(p => p.startsWith('Sản phẩm seed'))!.matchAll(/id (\d+) '([^']+)' ([\d.]+) ₫/g))
  PRODUCTS[Number(m[1])] = { name: m[2], price: Number(m[3].replace(/\./g, '')) };
// "Có token admin: POST /api/login với admin@eshop.com / Admin123! (dùng …"
const adm = /với (\S+@\S+) \/ (\S+?)\s/.exec(pre.find(p => p.includes('/api/login'))!)!;
export const ADMIN = { email: adm[1], password: adm[2] };
// Procedure bước 1: "POST /api/register {name: 'Cart Tester', email: 'cartNN_{ts}@domain.com', password: 'Abcd1234!'}"
function account(sid: string) {
  const m = /name: '(.+?)', email: '(.+?)', password: '(.+?)'/.exec(suites[sid].procedure[0].action)!;
  return { name: m[1], email: m[2], password: m[3] };
}
export const UI_ACCOUNT = account('TS-DOM-UI');
export const API_ACCOUNT = account('TS-DOM-API');
// Procedure TS-DOM-API bước 4: "'sai' = 'Bearer abc.def.ghi'"
export const BAD_TOKEN = /'sai' = '(Bearer [^']+)'/.exec(suites['TS-DOM-API'].procedure[3].action)![1];

/** "TC: id 1; CT: id 5 × 3" → [{how:'TC', id:1, qty:1}, {how:'CT', id:5, qty:3}] (UI) · "id 1 × 1; id 5 × 1" (API). */
export function parseInitial(s: string) {
  if (!s || s.trim() === '—') return [];
  return s.split(';').map(x => x.trim()).map(x => {
    const m = /^(?:(TC|CT): )?id (\d+)(?: × (\d+))?$/.exec(x);
    if (!m) throw new Error(`Không hiểu cột 'Giỏ ban đầu': ${x}`);
    return { how: (m[1] || 'API') as 'TC' | 'CT' | 'API', id: Number(m[2]), qty: m[3] ? Number(m[3]) : 1 };
  });
}

// ---------------- Tài khoản test {ts} + dọn dẹp (B0a, B0c) ----------------
export class SetupError extends Error {}
export type Acct = { id: number; email: string; password: string; name: string };

async function adminToken(request: APIRequestContext) {
  const r = await request.post(`${API}/api/login`, { data: ADMIN });
  if (r.status() !== 200) throw new Error(`Không đăng nhập được admin ${ADMIN.email}: HTTP ${r.status()}`);
  return (await r.json()).token as string;
}

export async function apiLogin(request: APIRequestContext, a: Acct) {
  const r = await request.post(`${API}/api/login`, { data: { email: a.email, password: a.password } });
  const j = await r.json().catch(() => ({}));
  if (r.status() !== 200 || !j.token) throw new SetupError(`POST /api/login ${a.email}: HTTP ${r.status()}`);
  return j.token as string;
}

/**
 * Fixture `accounts`: tạo user {ts} theo procedure bước 1; sau case (kể cả Fail) xoá bằng DELETE /api/admin/users/:id.
 * Xoá thất bại → annotation "cleanup", không đổi verdict (B0c).
 */
export const test = base.extend<{ accounts: { create: (tpl: { name: string; email: string; password: string }, tc: string) => Promise<Acct> } }>({
  accounts: async ({ request }, use, info) => {
    const made: Acct[] = [];
    await use({
      create: async (tpl, tc) => {
        const ts = String(Date.now());
        const a = { name: tpl.name, email: tpl.email.replace('NN', tc.slice(-3).replace(/^-/, '')).replace('{ts}', ts), password: tpl.password };
        const r = await request.post(`${API}/api/register`, { data: a });
        const j = await r.json().catch(() => ({}));
        if (r.status() !== 200 || typeof j.id !== 'number') throw new SetupError(`POST /api/register ${a.email}: HTTP ${r.status()} ${JSON.stringify(j)}`);
        const acct = { ...a, id: j.id };
        made.push(acct);
        return acct;
      },
    });
    if (!made.length) return;
    try {
      const t = await adminToken(request);
      for (const u of made) {
        const r = await request.delete(`${API}/api/admin/users/${u.id}`, { headers: { Authorization: `Bearer ${t}` } });
        if (r.status() !== 200)
          info.annotations.push({ type: 'cleanup', description: `Xoá user id ${u.id} (${u.email}) thất bại: HTTP ${r.status()} — B0c, không đổi verdict` });
      }
    } catch (e) {
      info.annotations.push({ type: 'cleanup', description: `Cleanup lỗi: ${(e as Error).message} — B0c, không đổi verdict` });
    }
  },
});
export { expect };

// ---------------- Bằng chứng ----------------
export async function shot(page: Page, info: TestInfo, name: string, label = 'screenshot') {
  const p = info.outputPath(`${name}.png`);
  await page.screenshot({ path: p, fullPage: true });
  await info.attach(label, { path: p, contentType: 'image/png' });
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
  await shot(page, info, `${id}_api`, 'render từ response thật');
}

// ---------------- Tiền & nhãn ----------------
/** "6.000.000 ₫" → 6000000; "NaN ₫" → NaN; không có số → null. */
export function money(s: string | null | undefined): number | null {
  if (s == null) return null;
  const m = /-?\d[\d.,\s]*/.exec(s);
  if (!m) return /NaN/.test(s) ? NaN : null;
  return Number(m[0].replace(/[^\d-]/g, ''));
}

/** B12: phân biệt hoa/thường, NFC, 'óa' = 'oá' (vị trí dấu), bỏ khoảng trắng đầu/cuối và ':' cuối. */
export function normLabel(s: string) {
  let t = (s ?? '').normalize('NFC').trim().replace(/\s*:$/, '').trim();
  const tone: Record<string, string> = { 'óa': 'oá', 'òa': 'oà', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'Óa': 'Oá', 'Òa': 'Oà', 'Ỏa': 'Oả', 'Õa': 'Oã', 'Ọa': 'Oạ' };
  for (const [k, v] of Object.entries(tone)) t = t.split(k).join(v);
  return t;
}

// ---------------- Điều hướng trong app (B0d: chỉ một page.goto mỗi case) ----------------
export const navCart = (page: Page) => page.locator('header a[href="/cart"]');
export const logo = (page: Page) => page.locator('header a[href="/"]').first();
export const productLink = (page: Page, id: number) => page.locator(`main a[href="/product/${id}"]`).first();
/** Nút thêm vào giỏ trên thẻ sản phẩm ở trang chủ: nút trong cùng khối với link 'Xem chi tiết' của sản phẩm. */
export const homeAddBtn = (page: Page, id: number) =>
  page.locator(`main a[href="/product/${id}"]`).first().locator('xpath=ancestor::div[.//button][1]').locator('button').first();

export async function waitHome(page: Page) {
  await expect(page.locator('main a[href^="/product/"]').first()).toBeVisible({ timeout: 10_000 });
}
export async function toHome(page: Page) {
  await logo(page).click();
  await waitHome(page);
}
export async function toCart(page: Page) {
  await navCart(page).click();
  await expect(page).toHaveURL(/\/cart$/);
  await page.waitForTimeout(300);
}
/** Từ trang chủ: link 'Xem chi tiết' → trang chi tiết đã tải (ô 'Số lượng:' hiển thị). */
export async function openDetail(page: Page, id: number) {
  await productLink(page, id).click();
  const qty = page.locator('main input').first();
  await expect(qty).toBeVisible({ timeout: 10_000 });
  return { qty, add: page.locator('main button').first() };
}
/** Xoá trắng ô Số lượng rồi gõ đúng chuỗi bằng bàn phím ('' = để trống). Trả về value thực tế của ô. */
export async function typeQty(qty: Locator, v: string) {
  await qty.fill('');
  if (v !== '') await qty.pressSequentially(v);
  return qty.inputValue();
}

// ---------------- Đọc trang giỏ (procedure bước 3) ----------------
export type Row = { name: string; price: number | null; qty: number | null; qtyText: string; line: number | null; qtyButtons: { text: string; aria: string }[]; delButtons: number };
export type Cart = { hasTable: boolean; headers: string[]; rows: Row[]; total: number | null; totalText: string; totalLabel: string; badge: number | null; mainText: string; hasImg: boolean; colNote: string };

export async function readCart(page: Page): Promise<Cart> {
  const raw = await page.evaluate(() => {
    const main = document.querySelector('main')!;
    const table = main.querySelector('table');
    const txt = (e: Element | null) => (e?.textContent ?? '').replace(/\s+/g, ' ').trim();
    let after = '';
    if (table) {
      const w = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
      let n: Node | null;
      while ((n = w.nextNode())) {
        if (table.contains(n)) continue;
        if (table.compareDocumentPosition(n) & Node.DOCUMENT_POSITION_FOLLOWING) after += n.textContent + ' ';
      }
    }
    // badge = con số hiển thị trên/cạnh link tới /cart trên navbar
    const link = document.querySelector('header a[href="/cart"]');
    const near = [link, link?.nextElementSibling, link?.previousElementSibling].map(txt).join(' ');
    const badge = /\d+/.exec(near);
    return {
      hasTable: !!table,
      headers: table ? [...table.querySelectorAll('thead th')].map(txt) : [],
      rows: table ? [...table.querySelectorAll('tbody tr')].map(tr => [...tr.children].map(td => ({
        text: txt(td),
        buttons: [...td.querySelectorAll('button')].map(b => ({ text: txt(b), aria: b.getAttribute('aria-label') || '' })),
        input: (td.querySelector('input') as HTMLInputElement | null)?.value ?? null,
      }))) : [],
      after: after.replace(/\s+/g, ' ').trim(),
      badge: badge ? Number(badge[0]) : null,
      mainText: txt(main),
      hasImg: !!main.querySelector('img, svg'),
    };
  });
  // Cột theo thứ tự FR-07.1; thứ tự khác thì xác định theo tiêu đề gần nghĩa (ghi colNote)
  const want = [/sản phẩm/i, /giá/i, /số lượng/i, /thành tiền/i, /thao tác/i];
  const col = want.map((re, i) => {
    const j = raw.headers.findIndex(h => re.test(h) && !(i === 1 && /thành tiền/i.test(h)));
    return j === -1 ? i : j;
  });
  const colNote = col.some((j, i) => j !== i) ? `thứ tự cột khác FR-07.1: ${JSON.stringify(raw.headers)}` : '';
  const rows: Row[] = raw.rows.map(cells => {
    const q = cells[col[2]];
    const qText = q ? (q.input ?? q.buttons.reduce((t, b) => t.replace(b.text, ''), q.text)).trim() : '';
    return {
      name: cells[col[0]]?.text ?? '', price: money(cells[col[1]]?.text), qty: money(qText), qtyText: qText,
      line: money(cells[col[3]]?.text), qtyButtons: q?.buttons ?? [], delButtons: cells[col[4]]?.buttons.length ?? 0,
    };
  });
  const tm = /(-?\d[\d.,]*|NaN)\s*(₫|đ|VND)?/.exec(raw.after);
  return {
    hasTable: raw.hasTable, headers: raw.headers, rows, total: tm ? money(tm[0]) : null, totalText: tm ? tm[0].trim() : '',
    totalLabel: tm ? raw.after.slice(0, tm.index).trim() : '', badge: raw.badge, mainText: raw.mainText, hasImg: raw.hasImg, colNote,
  };
}

export const rowOf = (c: Cart, id: number) => c.rows.find(r => r.name.includes(PRODUCTS[id].name));
export const fmtCart = (c: Cart) => !c.hasTable ? 'không có bảng (giỏ trống)'
  : `${c.rows.length} dòng: ` + c.rows.map(r => `[${r.name} | Đơn giá ${r.price} | SL ${r.qtyText} | Thành tiền ${r.line}]`).join(' ')
    + `; Tổng ${c.total}${c.badge !== null ? `; badge ${c.badge}` : '; không có badge'}`;

// ---------------- Phản hồi trực quan khi thêm (B21) ----------------
type Snap = { badge: string; live: string[]; body: string; btn: { text: string; disabled: boolean; cls: string } | null };
async function snap(page: Page, btn: Locator): Promise<Snap> {
  const g = await page.evaluate(() => {
    const t = (e: Element | null) => (e?.textContent ?? '').replace(/\s+/g, ' ').trim();
    const link = document.querySelector('header a[href="/cart"]');
    return {
      badge: [link, link?.nextElementSibling].map(t).join('|'),
      live: [...document.querySelectorAll('[role="alert"],[role="status"],[aria-live],[class*="toast" i],[class*="notif" i],[class*="snackbar" i]')].map(t).filter(Boolean),
      body: document.body.innerText,
    };
  });
  const b = await btn.evaluate((x: HTMLButtonElement) => ({ text: (x.textContent || '').trim(), disabled: x.disabled, cls: x.className }), undefined, { timeout: 500 }).catch(() => null);
  return { ...g, btn: b };
}
const ADDED = /(đã thêm|thêm .*thành công|added)/i;

/** Bấm nút thêm đúng một lần rồi theo dõi ≤ 2 s: toast/thông báo, badge, chữ/trạng thái nút. Trả về các loại phản hồi kèm thời điểm (ms). */
export async function clickAndWatch(page: Page, btn: Locator, info: TestInfo, id: string) {
  const before = await snap(page, btn);
  const t0 = Date.now();
  await btn.click();
  const seen: Record<string, number> = {};
  let shotDone = false;
  while (Date.now() - t0 <= 2000) {
    const s = await snap(page, btn);
    const ms = Date.now() - t0;
    if (s.badge !== before.badge) seen['badge đổi'] ??= ms;
    if (s.btn && before.btn && (s.btn.text !== before.btn.text || s.btn.disabled !== before.btn.disabled || s.btn.cls !== before.btn.cls))
      seen[`chữ/trạng thái nút đổi ('${before.btn.text}' → '${s.btn.text}')`] ??= ms;
    if (s.live.some(x => !before.live.includes(x))) seen[`toast/thông báo (${JSON.stringify(s.live.filter(x => !before.live.includes(x))[0])})`] ??= ms;
    const m = ADDED.exec(s.body);
    if (m && !ADDED.test(before.body)) seen[`chữ trên trang '${m[0]}'`] ??= ms;
    if (Object.keys(seen).length && !shotDone) { await shot(page, info, `${id}_feedback`, `${id}_feedback`); shotDone = true; }
    await page.waitForTimeout(100);
  }
  if (!shotDone) await shot(page, info, `${id}_feedback`, `${id}_feedback`);
  const kinds = Object.entries(seen).map(([k, ms]) => `${k} sau ${ms} ms`);
  return { kinds, text: kinds.length ? `phản hồi trong 2 s: ${kinds.join(', ')}` : 'không có phản hồi nhìn thấy được trong 2 s' };
}

// ---------------- Kết thúc case ----------------
export type Verdict = { verdict: 'Blocked'; why: string };
export function finish(info: TestInfo, obs: string[], v?: Verdict) {
  if (v) info.annotations.push({ type: 'verdict', description: v.verdict });
  info.annotations.push({ type: 'actual', description: (v ? `${v.verdict}: ${v.why} | ` : '') + obs.join('; ') });
}
