/**
 * Helper cho checklist C2 (HW03 T1). Item + Expected đọc từ ../checklist/checklist.json; ngưỡng đo trong ./oracle.ts
 * (khoá h = sha1(expected)[0:8] — Expected đổi thì test dừng với "oracle cũ", không chạy theo bản cũ).
 * File này chỉ chứa cách THỰC HIỆN thao tác và cách ĐO; không chứa kết luận.
 * Annotation cho reporter: obs = quan sát ghi vào notes · evidence = đường dẫn ảnh · blocked = không chấm được (lý do).
 */
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { test as base, expect, APIRequestContext, Page, Locator, TestInfo } from '@playwright/test';
import { _android, AndroidDevice } from 'playwright';
import { ORACLE, Oracle } from './oracle';

export const API = 'http://localhost:3000';
export const WEB = 'http://localhost:5173';
export const ADMIN = { email: 'admin@eshop.com', password: 'Admin123!' };   // SRS README.md:23
export const USER = { email: 'test@eshop.com', password: 'Test1234!' };     // SRS README.md:24
export const EVIDENCE_DIR = path.resolve(__dirname, '../checklist/evidence/auto');

const doc = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../checklist/checklist.json'), 'utf-8'));
export const ITEMS: Record<string, any> = Object.fromEntries(doc.items.map((i: any) => [i.id, i]));
export const hashOf = (s: string) => crypto.createHash('sha1').update(s, 'utf8').digest('hex').slice(0, 8);

/** Oracle của item; Expected trong JSON đổi so với lúc viết oracle → lỗi. */
export function oracle(id: string): Oracle {
  const it = ITEMS[id], o = ORACLE[id];
  if (!it || !o) throw new Error(`${id}: không có trong checklist.json hoặc oracle.ts`);
  if (hashOf(it.expected) !== o.h) throw new Error(`${id}: oracle cũ (sha1 expected = ${hashOf(it.expected)}, oracle viết cho ${o.h}) — cập nhật oracle.ts theo Expected mới`);
  return o;
}

/**
 * P3 = Chrome Android thật (POCO F5) qua Playwright `_android` (adb server :5037, `adb reverse` 5173 + 3000 đã bật).
 * launchBrowser() trả về context BỀN của Chrome trên máy (không phải context sạch) → đầu mỗi test xoá cookie +
 * storage của origin web/API để tương đương context mới của P1/P2. Viewport = màn hình thật (không dùng 1280×800).
 * Item có Px ngoài nen_tang (N/A theo thiết kế, vd NA1 trên P3) → bỏ qua, reporter không ghi.
 */
export const test = base.extend<{ naGate: void }, { androidDevice: AndroidDevice | null }>({
  androidDevice: [async ({}, use, w) => {
    if (w.project.name !== 'P3') return use(null);
    const [dev] = await _android.devices();
    if (!dev) throw new Error('[P3] adb không thấy thiết bị — cắm cáp, bật USB debugging; `adb devices` phải ra "device".');
    await use(dev);
    await dev.close();
  }, { scope: 'worker' }],
  naGate: [async ({}, use, info) => {
    const it = ITEMS[info.title.split(' ')[0]];
    if (it && !it.nen_tang.includes(info.project.name)) {
      info.annotations.push({ type: 'na', description: `${info.project.name} N/A theo thiết kế` });
      info.skip(true, `${info.project.name} N/A theo thiết kế`);
    }
    await use();
  }, { auto: true }],
  context: async ({ context, androidDevice }, use) => {
    if (!androidDevice) return use(context);
    const ctx = await androidDevice.launchBrowser({ baseURL: WEB, locale: 'vi-VN', timezoneId: 'Asia/Ho_Chi_Minh' });
    await ctx.clearCookies();
    const p = ctx.pages()[0] ?? await ctx.newPage();
    const cdp = await ctx.newCDPSession(p);
    for (const origin of [WEB, API]) await cdp.send('Storage.clearDataForOrigin', { origin, storageTypes: 'all' });
    await cdp.detach();
    await use(ctx);
    await ctx.close();
  },
  // P3: dùng tab có sẵn của context Android (tab mới mở thêm có thể nằm nền → chụp ảnh/hiển thị không chạy)
  page: async ({ context, androidDevice }, use) => {
    await use(androidDevice ? (context.pages()[0] ?? await context.newPage()) : await context.newPage());
  },
});
export { expect };

// ---------------- ghi quan sát / ảnh ----------------
export function obs(info: TestInfo, text: string) { info.annotations.push({ type: 'obs', description: text }); }
export function blocked(info: TestInfo, why: string) { info.annotations.push({ type: 'blocked', description: why }); }
let shotNo: Record<string, number> = {};
export async function shot(target: Page | Locator, info: TestInfo, id: string) {
  const key = `${info.project.name}_${id}`, k = (shotNo[key] = (shotNo[key] ?? 0) + 1);
  const file = path.join(EVIDENCE_DIR, `${info.project.name}_${id}_${k}.png`);
  fs.mkdirSync(EVIDENCE_DIR, { recursive: true });
  await target.screenshot({ path: file }).catch(() => {});
  info.annotations.push({ type: 'evidence', description: path.relative(path.resolve(__dirname, '../checklist'), file).split(path.sep).join('/') });
}

// ---------------- API: đăng nhập, dựng dữ liệu, khôi phục ----------------
export async function apiLogin(req: APIRequestContext, who = USER): Promise<string> {
  const r = await req.post(`${API}/api/login`, { data: who });
  if (r.status() !== 200) throw new Error(`POST /api/login ${who.email}: HTTP ${r.status()} ${await r.text()}`);
  return (await r.json()).token;
}
/** Đăng nhập đúng để đưa bộ đếm sai về 0 sau item có đăng nhập sai (backend khoá khi bộ đếm ≥ 3). */
export const resetAttempts = (req: APIRequestContext) => apiLogin(req).then(() => undefined);
export async function setProfile(req: APIRequestContext, p: { name: string; phone?: string | null; shipping_address?: string | null }) {
  const t = await apiLogin(req);
  const r = await req.put(`${API}/api/users/me`, { headers: { Authorization: `Bearer ${t}` }, data: { phone: null, shipping_address: null, ...p } });
  if (r.status() !== 200) throw new Error(`PUT /api/users/me: HTTP ${r.status()}`);
}
export const restoreProfile = (req: APIRequestContext) => setProfile(req, { name: 'Test User', phone: null, shipping_address: null });
/** Đặt lại mật khẩu test@eshop.com về giá trị seed qua API (sau item đổi mật khẩu). */
export async function restorePassword(req: APIRequestContext) {
  const ok = await req.post(`${API}/api/login`, { data: USER });
  if (ok.status() === 200) return;
  const f = await req.post(`${API}/api/forgot-password`, { data: { email: USER.email } });
  const { resetToken } = await f.json();
  await req.post(`${API}/api/reset-password`, { data: { email: USER.email, resetToken, newPassword: USER.password } });
  const again = await req.post(`${API}/api/login`, { data: USER });
  if (again.status() !== 200) throw new Error(`Không khôi phục được mật khẩu ${USER.email}`);
}

export type Orders = Record<'pending' | 'confirmed' | 'shipping' | 'delivered' | 'canceled' | 'cancelA' | 'cancelB', number>;
let ORDERS: Orders | null = null;
/**
 * Dựng MỘT lần mỗi lượt (sau CL-62): 5 đơn ở đủ 5 trạng thái (CL-58 tiền điều kiện) + 2 đơn Chờ xác nhận để thử huỷ (CL-60, CL-61).
 * Đơn tạo bằng POST /api/checkout (test@eshop.com), trạng thái đổi bằng PUT /api/admin/orders/:id/status (admin).
 */
export async function ensureOrders(req: APIRequestContext): Promise<Orders> {
  if (ORDERS) return ORDERS;
  const u = await apiLogin(req), a = await apiLogin(req, ADMIN);
  const make = async () => {
    const r = await req.post(`${API}/api/checkout`, { headers: { Authorization: `Bearer ${u}` },
      data: { items: [{ id: 4, name: 'Tai nghe AirPods Pro 2', price: 6000000, quantity: 1 }], total_amount: 6000000 } });
    if (r.status() !== 200) throw new Error(`POST /api/checkout: HTTP ${r.status()}`);
    return (await r.json()).orderId as number;
  };
  const to = async (id: number, s: string) => {
    const r = await req.put(`${API}/api/admin/orders/${id}/status`, { headers: { Authorization: `Bearer ${a}` }, data: { status: s } });
    if (r.status() !== 200) throw new Error(`PUT /api/admin/orders/${id}/status ${s}: HTTP ${r.status()} ${await r.text()}`);
  };
  const o: any = {};
  for (const k of ['pending', 'confirmed', 'shipping', 'delivered', 'canceled', 'cancelA', 'cancelB']) o[k] = await make();
  await to(o.confirmed, 'confirmed');
  await to(o.shipping, 'confirmed'); await to(o.shipping, 'shipping');
  await to(o.delivered, 'confirmed'); await to(o.delivered, 'shipping'); await to(o.delivered, 'delivered');
  await to(o.canceled, 'canceled');
  return (ORDERS = o);
}
export async function orderStatus(req: APIRequestContext, id: number) {
  const t = await apiLogin(req);
  const r = await req.get(`${API}/api/orders/my-orders`, { headers: { Authorization: `Bearer ${t}` } });
  return ((await r.json()) as any[]).find(x => x.id === id)?.status as string | undefined;
}

// ---------------- UI ----------------
export const H = (p: Page) => p.locator('header');
/** Đăng nhập không qua form: đặt token vào localStorage rồi tải lại (dùng cho item không kiểm form đăng nhập). */
export async function loginByToken(page: Page, req: APIRequestContext, to = '/') {
  const t = await apiLogin(req);
  await page.goto('/');
  await page.evaluate(tk => localStorage.setItem('token', tk), t);
  await page.goto(to);
  await expect(H(page).locator('a[href="/profile"]')).toBeVisible({ timeout: 5000 });
}
export const loginInputs = (p: Page) => p.locator('form input');
export const submitBtn = (p: Page) => p.locator('form button[type="submit"], form input[type="submit"]').first();
/** Ô nhập ngay sau nhãn có chữ `label` (nhãn của SUT không gắn for/id). */
export const byLabel = (p: Page, label: string | RegExp) =>
  p.locator('label', { hasText: label }).first().locator('xpath=following-sibling::*[self::input or self::textarea or self::select][1]');
export async function fillLogin(page: Page, email: string, pw: string) {
  await page.goto('/login');
  await loginInputs(page).nth(0).fill(email);
  await loginInputs(page).nth(1).fill(pw);
}
/** Bước 1 Quên mật khẩu → trả mã đọc được trên trang (chuỗi số) hoặc null. */
export async function forgotStep1(page: Page, email = USER.email) {
  await page.goto('/forgot-password');
  const before = await page.locator('form input').count();
  await page.locator('form input').first().fill(email);
  await submitBtn(page).click();
  await expect.poll(() => page.locator('form input').count(), { timeout: 5000 }).not.toBe(before);
  const txt = await page.locator('main').innerText();
  return /\b(\d{4,8})\b/.exec(txt)?.[1] ?? null;
}

/** Ghi mọi hộp thoại (alert/confirm) trong trang; mặc định accept. */
export function dialogs(page: Page, mode: 'accept' | 'dismiss' = 'accept') {
  const list: { type: string; message: string; at: number }[] = [];
  page.on('dialog', d => { list.push({ type: d.type(), message: d.message(), at: Date.now() }); (mode === 'accept' ? d.accept() : d.dismiss()).catch(() => {}); });
  return list;
}
/** Đếm request tới đường dẫn chứa `part`. */
export function countRequests(page: Page, part: string) {
  const c = { n: 0 };
  page.on('request', r => { if (r.url().includes(part)) c.n++; });
  return c;
}
/** Các dòng chữ mới xuất hiện trong <main> so với `before` (không tính giá trị ô nhập). */
export async function mainLines(page: Page) {
  return (await page.locator('main').innerText()).split('\n').map(s => s.trim()).filter(Boolean);
}
export const newLines = (before: string[], after: string[]) => after.filter(l => !before.includes(l));
export async function boxOfText(page: Page, text: string) {
  return page.locator('main').getByText(text, { exact: false }).first().boundingBox();
}

// ---------------- đo ----------------
export type Focus = { key: string; tag: string; text: string; x: number; y: number; outline: string };
const FOCUS_INFO = () => {
  const e = document.activeElement as HTMLElement | null;
  if (!e || e === document.body || e === document.documentElement) return null;
  const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
  return { key: `${e.tagName}#${Array.from(document.querySelectorAll('*')).indexOf(e)}`, tag: e.tagName.toLowerCase(),
    text: ((e as any).innerText || (e as any).value || e.getAttribute('placeholder') || (e as any).type || '').trim().slice(0, 30),
    x: Math.round(r.x + scrollX), y: Math.round(r.y + scrollY), outline: `${cs.outlineStyle} ${cs.outlineWidth} ${cs.outlineColor} | ${cs.boxShadow} | ${cs.borderColor}` };
};
/** Bấm Tab từ đầu trang tới khi focus quay vòng / ra khỏi trang; trả chuỗi control nhận focus. */
export async function tabWalk(page: Page, max = 40): Promise<Focus[]> {
  await page.evaluate(() => { (document.activeElement as HTMLElement | null)?.blur?.(); window.scrollTo(0, 0); });
  const seq: Focus[] = [];
  for (let i = 0; i < max; i++) {
    await page.keyboard.press('Tab');
    const f = await page.evaluate(FOCUS_INFO);
    if (!f || (seq.length && f.key === seq[0].key)) break;
    seq.push(f);
  }
  return seq;
}
/** Control tương tác được, đang hiển thị (để so với chuỗi Tab). */
export async function interactive(page: Page): Promise<Focus[]> {
  return page.evaluate(() => Array.from(document.querySelectorAll<HTMLElement>('a[href], button, input, textarea, select'))
    .filter(e => !(e as any).disabled && e.offsetParent !== null && e.tabIndex >= 0)
    .map(e => { const r = e.getBoundingClientRect(); return { key: `${e.tagName}#${Array.from(document.querySelectorAll('*')).indexOf(e)}`, tag: e.tagName.toLowerCase(),
      text: ((e as any).innerText || (e as any).value || e.getAttribute('placeholder') || (e as any).type || '').trim().slice(0, 30), x: Math.round(r.x + scrollX), y: Math.round(r.y + scrollY), outline: '' }; }));
}
/** Vi phạm thứ tự theo vị trí: control sau nằm cao hơn (quá tol px), hoặc cùng hàng mà nằm bên trái. */
export function orderViolations(seq: Focus[], tol = 4) {
  const v: string[] = [];
  for (let i = 1; i < seq.length; i++) {
    const a = seq[i - 1], b = seq[i];
    if (b.y < a.y - tol || (Math.abs(b.y - a.y) <= tol && b.x < a.x)) v.push(`'${a.text}'(${a.x},${a.y}) → '${b.text}'(${b.x},${b.y})`);
  }
  return v;
}
export const fmtSeq = (s: Focus[]) => s.map(f => `${f.tag}'${f.text}'@(${f.x},${f.y})`).join(' → ');

export async function style(l: Locator, props: string[]) {
  return l.evaluate((e, ps) => { const cs = getComputedStyle(e as Element); return Object.fromEntries(ps.map(p => [p, cs.getPropertyValue(p)])); }, props);
}
export function rgb(s: string): [number, number, number, number] {
  const m = /rgba?\(([^)]+)\)/.exec(s); if (!m) return [0, 0, 0, 0];
  const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1];
}
export function hue([r, g, b]: number[]) {
  const R = r / 255, G = g / 255, B = b / 255, mx = Math.max(R, G, B), mn = Math.min(R, G, B), d = mx - mn;
  if (!d) return { h: 0, s: 0 };
  let h = mx === R ? ((G - B) / d) % 6 : mx === G ? (B - R) / d + 2 : (R - G) / d + 4;
  h = Math.round(h * 60); if (h < 0) h += 360;
  return { h, s: d / (1 - Math.abs(mx + mn - 1)) };
}
export const inHue = (c: string, [lo, hi]: [number, number], minS = 0.3) => {
  const { h, s } = hue(rgb(c)); return s >= minS && (lo <= hi ? h >= lo && h <= hi : h >= lo || h <= hi);
};
const lum = ([r, g, b]: number[]) => { const f = (v: number) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
export const contrast = (a: number[], b: number[]) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
/** Màu chữ + nền thực (đi ngược lên cha tới khi gặp nền không trong suốt; không có → trắng) của các phần tử chữ trong trang. */
export async function textColors(page: Page) {
  return page.evaluate(() => {
    const out: { text: string; fg: string; bg: string }[] = [];
    const els = Array.from(document.querySelectorAll<HTMLElement>('label, button, a, p, td, th, h1, h2, h3, span, input, textarea'));
    for (const e of els) {
      if (e.offsetParent === null) continue;
      const own = Array.from(e.childNodes).some(n => n.nodeType === 3 && n.textContent!.trim()) || e.tagName === 'INPUT' || e.tagName === 'TEXTAREA';
      if (!own) continue;
      let p: HTMLElement | null = e, bg = 'rgb(255, 255, 255)';
      while (p) { const c = getComputedStyle(p).backgroundColor; if (c && !/rgba\(0, 0, 0, 0\)|transparent/.test(c)) { bg = c; break; } p = p.parentElement; }
      out.push({ text: ((e as any).innerText || (e as any).value || '').trim().slice(0, 30), fg: getComputedStyle(e).color, bg });
    }
    return out;
  });
}
