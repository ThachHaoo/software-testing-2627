/**
 * B_FR07 – FR-07 Giỏ hàng (web /cart + điểm thêm vào giỏ ở / và /product/:id). Skill playwright-ddt-automation, bước 3.
 * Data-driven: mọi giá trị vào và oracle đọc từ HW04/data/B_FR07.json (expected nguyên văn HW02 + sha1, kiểm khi nạp).
 * Thao tác + oracle được ĐỌC từ cột 'Thao tác' / expected (oracles/b_fr07.oracle.ts) — spec không chứa hằng dữ liệu test.
 * Quy trình HW02 TS-DOM-UI bước 1–6: mở trang 1 lần → dựng 'Giỏ ban đầu' → /cart qua navbar (TRƯỚC) → thao tác ĐÚNG 1 lần
 * → quan sát phản hồi → /cart qua navbar (SAU) → so TRƯỚC/SAU. Giỏ là state React: không goto/reload sau lần mở đầu.
 * Bấm đúng số lần ghi trong procedure; KHÔNG bấm thêm để lách hành vi "lần bấm đầu không thêm" (ProductDetail.jsx:21–25).
 * Assertion: trạng thái UI (toHaveURL/toBeVisible), nội dung (toContainText), oracle trạng thái giỏ dạng object (toEqual),
 * đếm/giá trị (toHaveCount/toHaveValue). Dùng expect.soft.
 */
import { errors, type Page } from '@playwright/test';
import { test, expect, loadData, resetDb, blocked, seedProducts, parseCartSteps } from './fixtures/b_fr07';
import { WEB } from './fixtures/ddt';
import { parseActions, parseExpected, type Oracle } from './oracles/b_fr07.oracle';
import type { CartRow, CartState } from './pages/shop.pages';

const DATA = loadData('B_FR07');           // ném lỗi nếu sha1(expected) lệch → cả file không chạy
const SEED = seedProducts(DATA);
const COL = { login: 'Đăng nhập', start: 'Giỏ ban đầu', action: 'Thao tác' };
/** Giả định SV chốt trong file data (ngoài expected). Thiếu → ném lỗi, không đoán. */
const assumption = (key: string) => {
  const a = DATA.assumptions?.[key];
  if (!a?.value) throw new Error(`[B_FR07] thiếu assumptions.${key} trong HW04/data/B_FR07.json`);
  return a;
};
/** Escape chuỗi lấy từ data trước khi dựng RegExp. */
const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
/** P1=a (5/6c): ảnh ngay sau thao tác chính, đính vào report bằng testInfo.attach (tên <TC>_after-action[-k]). */
async function attachAfterAction(page: Page, tcId: string, suffix = '') {
  await test.info().attach(`${tcId}_after-action${suffix}`, { body: await page.screenshot(), contentType: 'image/png' });
}
const FEEDBACK_WINDOW = 2_000;             // B21: phản hồi trong ≤ 2 giây sau khi bấm thêm (cửa sổ quan sát của oracle)

const nameOf = (id: number) => {
  const p = SEED.find(x => x.id === id);
  if (!p) throw new Error(`[B_FR07] id ${id} không có trong bảng sản phẩm seed`);
  return p;
};
/** So dòng giỏ không phụ thuộc thứ tự hiển thị (expected không quy định thứ tự). */
const byName = (rows: CartRow[]) => [...rows].sort((a, b) => a.name.localeCompare(b.name));

/** Trạng thái giỏ SAU mong đợi, dựng từ TRƯỚC + oracle (chỉ các thay đổi expected nêu; phần còn lại giữ nguyên). */
function expectedRows(before: CartState, o: Oracle): CartRow[] | null {
  if (o.clear) return [];
  if (o.unchanged) return before.rows;
  if (!o.add.length && !o.modify.length && !o.remove.length) return null;   // expected không nói về các dòng
  let rows = before.rows.filter(r => !o.remove.includes(r.name));
  rows = rows.map(r => {
    const m = o.modify.find(x => x.name === r.name);
    return m ? { ...r, qty: String(m.qty), subtotal: m.subtotal } : r;
  });
  for (const a of o.add) {
    const seed = SEED.find(p => p.name === a.name);
    if (a.price === undefined && !seed) throw new Error(`[B_FR07] không biết Đơn giá của '${a.name}' (không có trong expected lẫn seed)`);
    rows.push({ name: a.name, price: a.price ?? seed!.price, qty: String(a.qty), subtotal: a.subtotal });
  }
  return rows;
}

/** Ảnh chụp các vùng có thể đổi khi thêm (toast/role=alert|status, badge navbar, nút thêm, nội dung main). */
async function feedbackSnapshot(page: Page) {
  return page.evaluate(() => ({
    toast: document.querySelectorAll('[role="alert"],[role="status"],[class*="toast" i]').length,
    nav: document.querySelector('header nav')?.textContent ?? '',
    button: Array.from(document.querySelectorAll('main button')).map(b => b.textContent).join('|'),
    main: (document.querySelector('main') as HTMLElement | null)?.innerText ?? '',
  }));
}
type Snap = Awaited<ReturnType<typeof feedbackSnapshot>>;

/** Chờ tối đa FEEDBACK_WINDOW cho một thay đổi nhìn thấy được; trả về loại phản hồi đầu tiên hoặc null (hết cửa sổ). */
async function observeFeedback(page: Page, before: Snap): Promise<string | null> {
  try {
    const h = await page.waitForFunction((b) => {
      const toast = document.querySelectorAll('[role="alert"],[role="status"],[class*="toast" i]').length;
      const nav = document.querySelector('header nav')?.textContent ?? '';
      const button = Array.from(document.querySelectorAll('main button')).map(x => x.textContent).join('|');
      const main = (document.querySelector('main') as HTMLElement | null)?.innerText ?? '';
      if (toast > b.toast) return 'toast';
      if (nav !== b.nav) return `badge/navbar đổi: "${nav}"`;
      if (button !== b.button) return `nút đổi: "${button}"`;
      if (main !== b.main) return 'nội dung trang đổi';
      return false;
    }, before, { timeout: FEEDBACK_WINDOW, polling: 100 });
    return (await h.jsonValue()) as string;
  } catch (e) {
    if (e instanceof errors.TimeoutError) return null;    // hết cửa sổ quan sát = không có phản hồi
    throw e;
  }
}

/** Bước điều hướng/chuẩn bị (không phải assertion): quá hạn → Blocked (lỗi harness/môi trường, không phải Fail). */
async function step<T>(what: string, fn: () => Promise<T>): Promise<T> {
  try { return await fn(); } catch (e) {
    if (e instanceof errors.TimeoutError) blocked(`${what}: ${String(e).split('\n')[0]}`);
    throw e;
  }
}

test.beforeAll(async ({}, testInfo) => {
  testInfo.setTimeout(120_000);
  if (testInfo.config.workers > 1)
    throw new Error(`[B_FR07] workers = ${testInfo.config.workers}: resetDb không an toàn khi chạy song song — chạy với --workers=1`);
  resetDb();                               // tiền điều kiện suite: CSDL seed sạch, userCarts rỗng (B0c)
});

for (const c of DATA.testcases) {
  test(`${c.tc_id} ${c.title}`, async ({ page, shop }) => {
    const ann = (type: string, description: string) => test.info().annotations.push({ type, description });
    ann('expected', c.expected);
    ann('hw02', `${c.hw02.status}${c.hw02.bug_id ? ' ' + c.hw02.bug_id : ''}`);
    const ts = Date.now();
    const ops = parseActions(c.inputs[COL.action]);        // cú pháp lạ → ném lỗi (không đoán)
    const o = parseExpected(c.expected, SEED);
    for (const u of o.unmapped) ann('oracle không tự động', `${u} — dialog native khoá trang / không quan sát được bằng script; kiểm tay`);
    const { nav, home, detail, cart, dialogs } = shop;
    const mains: (typeof ops)[number][] = ops.filter(x => x.k !== 'home-link');   // thao tác chính = bấm Thêm / Xoá
    const shotSuffix = (op: (typeof ops)[number]) => (mains.length > 1 ? `-${mains.indexOf(op) + 1}` : '');

    // Bước 1–2: mở trang (lần goto duy nhất) + dựng giỏ ban đầu
    await step('Mở trang / đăng nhập', () => shop.startSession(c.inputs[COL.login], c.tc_id, ts));
    await step('Dựng giỏ ban đầu', () => shop.buildCart(c.inputs[COL.start]));

    // Bước 3: /cart qua navbar, ghi TRƯỚC; giỏ phải khớp 'Giỏ ban đầu', không khớp → Blocked (B20)
    await step('Mở /cart', () => cart.open());
    const before = await cart.state();
    ann('TRƯỚC', JSON.stringify(before));
    const want = parseCartSteps(c.inputs[COL.start]).map(s => ({ name: nameOf(s.id).name, qty: s.via === 'TC' ? '1' : (s.qty ?? '') }));
    const got = before.rows.map(r => ({ name: r.name, qty: r.qty }));
    if (JSON.stringify(byName(want as CartRow[]).map(r => [r.name, r.qty])) !== JSON.stringify(byName(got as CartRow[]).map(r => [r.name, r.qty])))
      blocked(`Giỏ ban đầu không khớp cột '${COL.start}': cần ${JSON.stringify(want)}, có ${JSON.stringify(got)}`);
    if (o.countBefore !== undefined) await expect.soft(cart.rows, 'số dòng TRƯỚC').toHaveCount(o.countBefore);
    if (o.before.noTable) await expect.soft(page.locator('main table'), 'giỏ trống: không có bảng sản phẩm').toHaveCount(0);
    if (o.before.emptyText || o.before.illustration) {
      const kw = assumption('empty_cart_keyword');
      const kwRe = new RegExp(esc(kw.value), 'i');
      if (o.before.emptyText) {
        await expect.soft(cart.emptyMessage(kwRe), 'giỏ trống: dòng chữ báo giỏ trống').not.toHaveCount(0);
        await expect.soft(page.locator('main'), 'giỏ trống: nội dung dòng chữ').toContainText(kwRe);
        ann('oracle thông báo yếu', `expected chỉ nói 'dòng chữ báo giỏ trống' → kiểm chứa '${kw.value}' (${kw.note})`);
      }
      // R2: img/svg phải nằm trong cùng khối với dòng chữ giỏ trống (không nhận icon ở chỗ khác của main), không dùng .first()
      if (o.before.illustration)
        await expect.soft(cart.emptyIllustration(kwRe), 'giỏ trống: có img/svg minh hoạ trong khối chứa dòng chữ giỏ trống').not.toHaveCount(0);
    }
    if (o.before.badgeZeroOrHidden) expect.soft([null, 0], `badge ẩn hoặc 0 (đọc được: ${before.badge})`).toContain(before.badge);

    // Bước 4–6: thao tác đúng 1 lần mỗi mục; phản hồi; /cart qua navbar → SAU
    let after: CartState = before;
    for (const op of ops) {
      if (op.k === 'detail') {
        await step('Về trang chủ', async () => { await nav.home.click(); await home.waitLoaded(); });
        await step('Mở trang chi tiết', async () => { await home.openDetail(op.id); await detail.waitLoaded(); });
        await expect.soft(detail.title, 'trang chi tiết đúng sản phẩm').toHaveText(nameOf(op.id).name);
        const typed = await detail.setQuantity(op.qty);
        ann('ô Số lượng sau khi gõ', JSON.stringify({ gõ: op.qty, value: typed }));
        const snap = await feedbackSnapshot(page);
        await detail.add.click();                          // ĐÚNG 1 lần (procedure HW02 bước 4)
        // chụp song song với cửa sổ quan sát B21 để ảnh là trạng thái ngay sau khi bấm, không làm trễ việc đo phản hồi
        const [fb] = await Promise.all([
          observeFeedback(page, snap),
          attachAfterAction(page, c.tc_id, shotSuffix(op)),
        ]);
        ann('phản hồi sau khi bấm thêm', fb ?? `không có thay đổi nhìn thấy trong ${FEEDBACK_WINDOW} ms`);
        const wantFb = op.snapshot ? o.phases[op.snapshot]?.feedback && 'present' : o.feedback;
        if (wantFb === 'present') expect.soft(fb, 'B21: có phản hồi ≤ 2 s sau khi bấm thêm').not.toBeNull();
        if (wantFb === 'absent') expect.soft(fb, 'không có phản hồi báo đã thêm').toBeNull();
        if (o.noAlert) expect.soft(dialogs.filter(d => d.type === 'alert'), 'không bật alert (XSS)').toEqual([]);
        await step('Mở /cart', () => cart.open());
        after = await cart.state();
        if (op.snapshot) {
          const ph = o.phases[op.snapshot];
          ann(`SAU lần ${op.snapshot}`, JSON.stringify(after));
          for (const r of ph.rows) {
            await expect.soft(cart.row(nameOf(r.id).name), `lần ${op.snapshot}: có dòng id ${r.id}`).toHaveCount(1);
            expect.soft(after.rows.filter(x => x.name === nameOf(r.id).name).map(x => x.qty), `lần ${op.snapshot}: Số lượng id ${r.id}`).toEqual([String(r.qty)]);
          }
          if (ph.count !== undefined) await expect.soft(cart.rows, `lần ${op.snapshot}: số dòng`).toHaveCount(ph.count);
        }
      } else if (op.k === 'delete') {
        const name = nameOf(op.id).name;
        shop.dialogAction = op.dialog;
        const n0 = dialogs.length;
        await cart.removeButton(name).click();             // ĐÚNG 1 lần
        await attachAfterAction(page, c.tc_id, shotSuffix(op));
        if (o.dialogConfirm) {
          await expect.soft.poll(() => dialogs.length - n0, { message: 'hiện dialog xác nhận sau khi bấm xoá', timeout: FEEDBACK_WINDOW }).toBe(1);
          expect.soft(dialogs.slice(n0).map(d => d.type), 'dialog là confirm').toEqual(dialogs.length > n0 ? ['confirm'] : []);
        }
        ann('dialog sau khi bấm xoá', JSON.stringify(dialogs.slice(n0)));
        await step('Mở /cart', () => cart.open());
        after = await cart.state();
      } else {
        // 'Ở trang giỏ: bấm link về trang chủ' — a[href='/'] trong vùng nội dung chính (không tính navbar/logo)
        const link = page.locator('main a[href="/"]');
        await expect.soft(link, "trang giỏ có link về trang chủ trong vùng main").toHaveCount(1);
        await step('Bấm link về trang chủ', () => link.first().click());
        if (o.urlAfterHome) await expect.soft(page, 'URL sau khi bấm link về trang chủ').toHaveURL(o.urlAfterHome);
      }
    }
    ann('SAU', JSON.stringify(after));

    // Oracle trạng thái giỏ TRƯỚC → SAU (object)
    const rows = expectedRows(before, o);
    if (rows) expect.soft(byName(after.rows), 'các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)').toEqual(byName(rows));
    if (o.countAfter !== undefined) expect.soft(after.rows.length, 'số dòng SAU').toBe(o.countAfter);
    for (const k of o.keep) expect.soft(after.rows.find(r => r.name === k), `dòng '${k}' không đổi`).toEqual(before.rows.find(r => r.name === k));
    for (const k of [...o.absent, ...o.remove]) expect.soft(after.rows.map(r => r.name), `không có dòng '${k}'`).not.toContain(k);
    if (o.total === 'unchanged') expect.soft(after.total, 'Tổng SAU = Tổng TRƯỚC').toBe(before.total);
    else if (o.total !== undefined) expect.soft(after.total, 'Tổng SAU').toBe(o.total);
    if (o.totalIsSum) expect.soft(after.total, 'Tổng = Σ Thành tiền').toBe(after.rows.reduce((t, r) => t + (r.subtotal ?? 0), 0));
    if (o.badge !== undefined) expect.soft(after.badge, 'badge SAU (tổng Số lượng, B9)').toBe(o.badge);
    if (o.emptyAfter) {
      expect.soft(after.empty, 'chuyển sang trạng thái giỏ trống').toBe(true);
      if (page.url() === `${WEB}/cart`) await expect.soft(page.locator('main table'), 'không còn bảng sản phẩm').toHaveCount(0);
    }
  });
}
