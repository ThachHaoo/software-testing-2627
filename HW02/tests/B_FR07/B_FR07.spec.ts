/**
 * FR-07 Giỏ hàng — chạy toàn bộ test case trong HW02/B_FR07/testcases.json (62 TC, 7 suite).
 * Tiêu đề test = "<mã TC> <tiêu đề>" để merge_results.py gộp được.
 * Oracle của từng case ghi trong bảng UI_ORACLE / API_ORACLE / GUI bên dưới, chép từ expected_result;
 * trường `h` là dấu vân tay của expected_result lúc viết oracle — Expected trong JSON đổi thì test báo lỗi, không tự chạy theo bản cũ.
 * Case nhiều khẳng định dùng expect.soft; mọi chỗ lệch nằm trong Actual (annotation "actual") và lỗi của test.
 * Chạy (PowerShell, trong HW02/tests): xem HW02/B_FR07/RUN.md
 */
import { APIRequestContext, Browser, Page, TestInfo } from '@playwright/test';
import {
  test, expect, data, allCases, hashOf, PRODUCTS, UI_ACCOUNT, API_ACCOUNT, BAD_TOKEN, API, WEB, parseInitial, SetupError, apiLogin,
  shot, attachJson, renderResponse, normLabel, productLink, homeAddBtn, waitHome, toHome, toCart, openDetail, typeQty,
  readCart, rowOf, fmtCart, clickAndWatch, finish, Verdict, Cart, Acct,
} from './lib';

type Accounts = { create: (tpl: { name: string; email: string; password: string }, tc: string) => Promise<Acct> };
type Ctx = { browser: Browser; request: APIRequestContext; page?: Page; accounts: Accounts };

// =============================== Oracle UI (TS-DOM-UI, TS-BVA-UI, TS-SV-UI) ===============================
type UiOracle = {
  h: string;
  feedback?: 'yes' | 'no';                 // B21 / EC46
  rows?: [number, number];                 // số dòng TRƯỚC → SAU
  exactRows?: number;                      // SV: "đúng 1 dòng" (không có TRƯỚC)
  same?: boolean;                          // giỏ không đổi: số dòng, Số lượng, Thành tiền từng dòng, Tổng
  absent?: number[];                       // SAU không có dòng của các id này
  kept?: number[];                         // dòng của các id này SAU = TRƯỚC (Số lượng, Thành tiền)
  target?: { id: number; qty?: number | [number, number]; qtyText?: string; price?: number; line?: number | 'qty×price' };
  total?: number | 'same';
  badge?: number;
  dialog?: 'none' | 'accept' | 'dismiss' | 'optional';
  rowWhileDialog?: boolean;                // TC-08: dòng chưa bị xoá khi dialog đang mở
  home?: boolean;                          // sau khi bấm link về trang chủ trong trang giỏ: URL = '/'
  empty?: { img: boolean; badge: boolean };// trạng thái giỏ trống
  noScript?: boolean;                      // TC-200: không bật alert
};
const REJECT_UI = (h: string): UiOracle => ({ h, feedback: 'no', same: true, kept: [1], absent: [5], total: 'same' });
const ADD_LB = (h: string, q: number): UiOracle => ({ h, rows: [0, 1], target: { id: 5, qty: q, line: q * 4000000 }, total: q * 4000000 });

const UI_ORACLE: Record<string, UiOracle> = {
  'TC-FR07-01': { h: 'f5e30617', empty: { img: true, badge: true }, home: true },
  'TC-FR07-02': { h: '7b87787c', feedback: 'yes', rows: [0, 1], target: { id: 2, qty: 2, price: 28000000, line: 56000000 }, total: 56000000, home: true },
  'TC-FR07-03': { h: '07231da1', rows: [1, 1], target: { id: 5, qty: [1, 4], line: 16000000 }, total: 16000000 },
  'TC-FR07-04': { h: '595ae534', rows: [2, 2], target: { id: 4, qty: [1, 3], line: 18000000 }, kept: [1], total: 48000000, badge: 4 },
  'TC-FR07-05': { h: '2c03ebf5', rows: [1, 1], target: { id: 5, qty: [1, 2], line: 8000000 }, total: 8000000 },
  'TC-FR07-06': { h: '6f2b891b', rows: [1, 1], target: { id: 5, qty: [3, 2], line: 8000000 }, total: 8000000 },
  'TC-FR07-07': { h: '4dbd28b4', dialog: 'none', rows: [1, 1], target: { id: 5, qty: [1, 1] }, total: 'same' },
  'TC-FR07-08': { h: '1be3ed18', dialog: 'accept', rowWhileDialog: true, rows: [2, 1], absent: [4], kept: [5], total: 4000000 },
  'TC-FR07-09': { h: '28d35c52', dialog: 'dismiss', same: true, kept: [4], total: 'same' },
  'TC-FR07-10': REJECT_UI('55ad3430'), 'TC-FR07-11': REJECT_UI('55ad3430'), 'TC-FR07-12': REJECT_UI('55ad3430'), 'TC-FR07-13': REJECT_UI('55ad3430'),
  'TC-FR07-60': REJECT_UI('55ad3430'),
  'TC-FR07-61': ADD_LB('795c9d53', 1), 'TC-FR07-62': ADD_LB('73d77964', 2), 'TC-FR07-63': ADD_LB('0dc97914', 5), 'TC-FR07-64': ADD_LB('46324b89', 1000),
  'TC-FR07-65': { h: 'e2df8df5', rows: [1, 1], target: { id: 5, qty: [2, 1], line: 4000000 }, total: 4000000 },
  'TC-FR07-66': { h: '8ff84229', dialog: 'optional', rows: [1, 0], empty: { img: false, badge: false } },
  'TC-FR07-200': { h: 'efdbd0ee', noScript: true, same: true },
  'TC-FR07-201': { h: '31b088e4', exactRows: 1, target: { id: 4, qty: 20, line: 'qty×price' } },
  'TC-FR07-203': { h: '58b3678e', target: { id: 3, qty: 100000, line: 'qty×price' } },
  'TC-FR07-205': { h: '44c60892' },                               // hai pha, xem runSv205
  'TC-FR07-206': { h: 'bb8e5f2d', rows: [0, 1], target: { id: 2, qtyText: '7', line: 'qty×price' } },
};

type Op =
  | { kind: 'home' }
  | { kind: 'ct'; id: number; v: string; thenHome: boolean }
  | { kind: 'pm'; sign: '+' | '-'; id: number }
  | { kind: 'del'; id: number }
  | { kind: 'spam'; id: number; n: number; gap: number };

function parseOp(c: any): Op {
  const s: string = c.inputs['Thao tác'];
  let m: RegExpExecArray | null;
  if (/^Ở trang giỏ: bấm link về trang chủ$/.test(s)) return { kind: 'home' };
  if ((m = /^CT: id (\d+) × (.+?)(, rồi ở trang giỏ bấm link về trang chủ|, bấm 'Thêm', mở \/cart)?$/.exec(s))) {
    let v = m[2];
    const q = /^'(.*?)'/.exec(v);                       // "'abc'", "'' (xoá trắng ô)"
    if (q) v = q[1];
    return { kind: 'ct', id: Number(m[1]), v, thenHome: !!m[3] && m[3].includes('trang chủ') };
  }
  if ((m = /^Bấm '([+-])' trên dòng id (\d+)$/.exec(s))) return { kind: 'pm', sign: m[1] as '+' | '-', id: Number(m[2]) };
  if ((m = /^Bấm nút xoá trên dòng id (\d+) → dialog/.exec(s))) return { kind: 'del', id: Number(m[1]) };
  if ((m = /^bấm 'Thêm vào giỏ' id (\d+) đúng (\d+) lần trong [\d,]+ giây \(cách nhau (\d+) ms\)$/.exec(s)))
    return { kind: 'spam', id: Number(m[1]), n: Number(m[2]), gap: Number(m[3]) };
  throw new Error(`${c.id}: không hiểu cột 'Thao tác': ${s}`);
}

/** Procedure bước 1: user {ts} đăng nhập qua form /login, hoặc khách mở '/'. Lần page.goto duy nhất của case. */
async function start(page: Page, c: any, accounts: Accounts, obs: string[]) {
  if (c.inputs['Đăng nhập'] === 'user {ts}') {
    const a = await accounts.create(UI_ACCOUNT, c.id);
    await page.goto(`${WEB}/login`);
    const field = (l: string) => page.locator(`xpath=//label[starts-with(normalize-space(.), "${l}")]/following-sibling::input[1]`);
    await field('Username').pressSequentially(a.email);
    await field('Mật khẩu').pressSequentially(a.password);
    await page.locator('form button[type="submit"]').click();
    await waitHome(page);
    const hello = await page.locator('header').getByText(a.name).count();
    obs.push(`đăng nhập ${a.email}: navbar ${hello ? 'có' : 'KHÔNG có'} tên user`);
    if (!hello) throw new SetupError(`đăng nhập UI ${a.email} không thành công`);
  } else {
    await page.goto(`${WEB}/`);
    await waitHome(page);
  }
}

/** Procedure bước 2: dựng 'Giỏ ban đầu' (TC = nút trên thẻ ở trang chủ; CT = trang chi tiết rồi về trang chủ bằng logo). */
async function buildInitial(page: Page, init: ReturnType<typeof parseInitial>) {
  for (const it of init) {
    if (it.how === 'TC') await homeAddBtn(page, it.id).click();
    else {
      const d = await openDetail(page, it.id);
      await typeQty(d.qty, String(it.qty));
      await d.add.click();
      await page.waitForTimeout(300);
      await toHome(page);
    }
    await page.waitForTimeout(200);
  }
}

/** Procedure bước 3: giỏ khớp cột 'Giỏ ban đầu'? Không khớp → Blocked (B20). */
function initialMismatch(c: Cart, init: ReturnType<typeof parseInitial>): string {
  const want = init.map(i => `${PRODUCTS[i.id].name} × ${i.qty}`);
  const got = c.rows.map(r => `${r.name} × ${r.qtyText}`);
  const ok = want.length === got.length && init.every((i, k) => c.rows[k].name.includes(PRODUCTS[i.id].name) && c.rows[k].qty === i.qty);
  return ok ? '' : `giỏ ban đầu không khớp: cần [${want.join(', ')}], thấy [${got.join(', ')}]`;
}

/** Nút '+'/'-' trong ô Số lượng của dòng: theo chữ/aria (+, −, -, tăng, giảm); không rõ thì '-' là nút đầu, '+' là nút sau. */
function pmIndex(btns: { text: string; aria: string }[], sign: '+' | '-') {
  const re = sign === '+' ? /^\+$|tăng|increase|plus/i : /^[-−–]$|giảm|decrease|minus/i;
  const k = btns.findIndex(b => re.test(b.text) || re.test(b.aria));
  return k !== -1 ? { k, how: 'theo chữ/aria' } : { k: sign === '-' ? 0 : 1, how: 'theo vị trí (không có chữ/aria rõ)' };
}

const rowLoc = (page: Page, id: number) => page.locator('main table tbody tr').filter({ hasText: PRODUCTS[id].name }).first();

async function runUi(c: any, { browser, accounts }: Ctx, info: TestInfo) {
  test.setTimeout(120_000);
  const o = UI_ORACLE[c.id];
  if (!o) throw new Error(`${c.id}: chưa có oracle UI`);
  if (o.h !== hashOf(c.expected_result)) throw new Error(`${c.id}: expected_result đã đổi so với lúc viết oracle (h=${o.h}, hiện tại ${hashOf(c.expected_result)}) — cập nhật UI_ORACLE`);
  const obs: string[] = [];
  let v: Verdict | undefined;
  const ctx = await browser.newContext();               // context mới mỗi case: không token, giỏ web rỗng
  const page = await ctx.newPage();
  const dialogs: string[] = [];
  let dialogMode: 'dismiss' | 'accept' = 'dismiss';
  let whileDialog: string | null = null;
  let probeName = '';
  const cdp = o.rowWhileDialog ? await ctx.newCDPSession(page) : null;
  page.on('dialog', async d => {
    dialogs.push(`${d.type()}: ${JSON.stringify(d.message())}`);
    if (cdp && probeName) {                             // TC-08: đọc DOM qua CDP khi dialog native đang mở (JS trang bị dừng)
      const probe = (async () => {
        const { root } = await cdp.send('DOM.getDocument', { depth: -1 });
        const { nodeIds } = await cdp.send('DOM.querySelectorAll', { nodeId: root.nodeId, selector: 'main table tbody tr' });
        let hit = false;
        for (const n of nodeIds) if ((await cdp.send('DOM.getOuterHTML', { nodeId: n })).outerHTML.includes(probeName)) hit = true;
        return hit ? 'còn' : 'không còn';
      })();
      whileDialog = await Promise.race([probe, new Promise<string>(r => setTimeout(() => r('không đọc được DOM'), 3000))]).catch(e => `lỗi CDP: ${e.message}`);
    }
    await (dialogMode === 'accept' ? d.accept() : d.dismiss()).catch(() => {});
  });
  try {
    await start(page, c, accounts, obs);
    const init = parseInitial(c.inputs['Giỏ ban đầu']);
    await buildInitial(page, init);
    await toCart(page);
    const before = await readCart(page);
    obs.push(`TRƯỚC: ${fmtCart(before)}`);
    if (before.colNote) obs.push(before.colNote);
    const mis = initialMismatch(before, init);
    if (mis) {
      const ct = init.some(i => i.how === 'CT');
      v = { verdict: 'Blocked', why: `${mis} (B20) — ${ct ? 'nghi case gốc TC-FR07-61 (thêm từ trang chi tiết), SV xác nhận' : 'SV xác định case gốc'}` };
      await shot(page, info, `${c.id}_ui`);
      return;
    }
    if (c.id === 'TC-FR07-205') return await runSv205(page, info, obs);

    // TC-01: quan sát trạng thái giỏ trống ở bước 3
    if (o.empty && !o.rows) checkEmpty(before, o.empty, obs);

    // ---------------- Bước 4–5: thao tác ----------------
    const op = parseOp(c);
    let fb: Awaited<ReturnType<typeof clickAndWatch>> | null = null;
    if (op.kind === 'home') {
      await page.locator('main a[href="/"]').first().click();
    } else if (op.kind === 'ct') {
      await toHome(page);
      const d = await openDetail(page, op.id);
      const val = await typeQty(d.qty, op.v);
      obs.push(`ô Số lượng sau khi gõ ${JSON.stringify(op.v)}: value=${JSON.stringify(val)}${op.v !== '' && val === '' ? ' (không nhập được)' : ''}`);
      fb = await clickAndWatch(page, d.add, info, c.id);
      obs.push(fb.text);
    } else if (op.kind === 'pm') {
      const r = before.rows.find(x => x.name.includes(PRODUCTS[op.id].name))!;
      if (r.qtyButtons.length < 2) {
        v = { verdict: 'Blocked', why: `ô Số lượng của dòng không có nút '+'/'-' (${r.qtyButtons.length} nút) — case gốc TC-FR07-90 (A17, B20)` };
        await shot(page, info, `${c.id}_ui`);
        return;
      }
      const { k, how } = pmIndex(r.qtyButtons, op.sign);
      obs.push(`bấm nút '${op.sign}' (${how}: ${JSON.stringify(r.qtyButtons[k])})`);
      await rowLoc(page, op.id).locator('td').nth(2).locator('button').nth(k).click();
      await page.waitForTimeout(800);
    } else if (op.kind === 'del') {
      dialogMode = o.dialog === 'dismiss' ? 'dismiss' : 'accept';
      probeName = PRODUCTS[op.id].name;
      await rowLoc(page, op.id).locator('td').last().locator('button').first().click();
      await page.waitForTimeout(1000);
      if (!dialogs.length) {                            // không có dialog native → tìm modal (B14 chấp nhận modal)
        const modal = page.locator('[role="dialog"]:visible, [role="alertdialog"]:visible, dialog[open]').first();
        if (await modal.count()) {
          const rowNow = await rowLoc(page, op.id).count();
          dialogs.push(`modal: ${JSON.stringify((await modal.innerText()).slice(0, 120))}`);
          whileDialog = rowNow ? 'còn' : 'không còn';
          const cancel = /h[uủ]y|huỷ|cancel|không|đóng/i;
          const btns = modal.locator('button');
          const n = await btns.count();
          for (let i = 0; i < n; i++) {
            const t = (await btns.nth(i).innerText()).trim();
            if (cancel.test(t) === (dialogMode === 'dismiss')) { await btns.nth(i).click(); break; }
          }
          await page.waitForTimeout(500);
        }
      }
      obs.push(dialogs.length ? `dialog: ${dialogs.join(' | ')}` : 'không có dialog');
      if (o.rowWhileDialog && whileDialog) obs.push(`dòng ${probeName} khi dialog đang mở: ${whileDialog}`);
    } else if (op.kind === 'spam') {
      await toHome(page);
      const btn = homeAddBtn(page, op.id);
      const box = (await btn.boundingBox())!;
      const t0 = Date.now();
      for (let i = 0; i < op.n; i++) {
        await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2);
        if (i < op.n - 1) await page.waitForTimeout(op.gap);
      }
      const dt = Date.now() - t0;
      obs.push(`bấm ${op.n} lần trong ${dt} ms${dt > (op.n * op.gap) ? ` [notes] thời gian thực tế ${dt} ms > ${op.n * op.gap} ms của cột Thao tác` : ''}`);
      await page.waitForTimeout(500);
    }
    if (o.dialog === 'none' && op.kind !== 'del') obs.push(dialogs.length ? `dialog: ${dialogs.join(' | ')}` : 'không có dialog');

    // ---------------- Bước 6: SAU ----------------
    if (op.kind === 'home') {
      const url = page.url();
      obs.push(`URL sau thao tác=${url}`);
      await shot(page, info, `${c.id}_ui`);
      expect.soft(url, 'URL = trang chủ').toBe(`${WEB}/`);
      return;
    }
    if (!/\/cart$/.test(page.url())) await toCart(page);
    const after = await readCart(page);
    obs.push(`SAU: ${fmtCart(after)}`);
    await shot(page, info, `${c.id}_ui`);

    // ---------------- So với Expected ----------------
    if (o.feedback === 'yes') expect.soft(fb?.kinds.length ?? 0, 'có ít nhất một phản hồi nhìn thấy được trong ≤ 2 s (B21)').toBeGreaterThan(0);
    if (o.feedback === 'no') expect.soft(fb?.kinds ?? [], 'không có phản hồi báo đã thêm (B2)').toEqual([]);
    if (o.noScript) expect.soft(dialogs, 'không bật alert (không có dialog)').toEqual([]);
    if (o.dialog === 'none') expect.soft(dialogs, 'không có dialog xoá').toEqual([]);
    if (o.dialog === 'accept' || o.dialog === 'dismiss') expect.soft(dialogs.length, 'hiện dialog xác nhận khi bấm nút xoá').toBeGreaterThan(0);
    if (o.rowWhileDialog && dialogs.length) {
      if (whileDialog === 'còn' || whileDialog === 'không còn') expect.soft(whileDialog, 'dòng chưa bị xoá khi dialog đang mở').toBe('còn');
      else obs.push(`[kiểm tay] dòng khi dialog đang mở: ${whileDialog} — SV quan sát tay`);
    }
    if (o.rows) {
      expect.soft(before.rows.length, 'số dòng TRƯỚC').toBe(o.rows[0]);
      expect.soft(after.rows.length, 'số dòng SAU').toBe(o.rows[1]);
    }
    if (o.exactRows !== undefined) expect.soft(after.rows.length, `đúng ${o.exactRows} dòng`).toBe(o.exactRows);
    if (o.same) {
      expect.soft(after.rows.length, 'số dòng SAU = TRƯỚC').toBe(before.rows.length);
      expect.soft(after.rows.map(r => [r.name, r.qty, r.line]), 'các dòng SAU = TRƯỚC').toEqual(before.rows.map(r => [r.name, r.qty, r.line]));
    }
    for (const id of o.absent ?? []) expect.soft(rowOf(after, id), `không có dòng '${PRODUCTS[id].name}'`).toBeUndefined();
    for (const id of o.kept ?? []) {
      const b = rowOf(before, id), a = rowOf(after, id);
      expect.soft(a && [a.qty, a.line], `dòng '${PRODUCTS[id].name}' không đổi`).toEqual(b && [b.qty, b.line]);
    }
    if (o.target) {
      const t = o.target, a = rowOf(after, t.id), b = rowOf(before, t.id);
      expect.soft(a, `có dòng '${PRODUCTS[t.id].name}'`).toBeTruthy();
      const nRows = after.rows.filter(r => r.name.includes(PRODUCTS[t.id].name)).length;
      if (nRows > 1) obs.push(`có ${nRows} dòng '${PRODUCTS[t.id].name}' (so dòng đầu tiên)`);
      if (Array.isArray(t.qty)) {
        expect.soft(b?.qty, `Số lượng TRƯỚC của '${PRODUCTS[t.id].name}'`).toBe(t.qty[0]);
        expect.soft(a?.qty, `Số lượng SAU của '${PRODUCTS[t.id].name}'`).toBe(t.qty[1]);
      } else if (t.qty !== undefined) expect.soft(a?.qty, `Số lượng của '${PRODUCTS[t.id].name}'`).toBe(t.qty);
      if (t.qtyText !== undefined) expect.soft(a?.qtyText, 'Số lượng hiển thị').toBe(t.qtyText);
      if (t.price !== undefined) expect.soft(a?.price, 'Đơn giá').toBe(t.price);
      if (t.line === 'qty×price') {
        const q = typeof t.qty === 'number' ? t.qty : Number(t.qtyText);
        expect.soft(a?.line, `Thành tiền = ${q} × Đơn giá hiển thị (${a?.price})`).toBe(a?.price == null ? NaN : q * a.price);
      } else if (t.line !== undefined) expect.soft(a?.line, 'Thành tiền').toBe(t.line);
    }
    if (o.total === 'same') expect.soft(after.total, 'Tổng SAU = Tổng TRƯỚC').toBe(before.total);
    else if (o.total !== undefined) expect.soft(after.total, 'Tổng SAU').toBe(o.total);
    if (o.badge !== undefined) expect.soft(after.badge, 'badge SAU (tổng Số lượng, B9)').toBe(o.badge);
    if (o.empty && o.rows) checkEmpty(after, o.empty, obs);
    if (o.home) {
      await page.locator('main a[href="/"]').first().click();
      await page.waitForTimeout(500);
      obs.push(`URL sau khi bấm link về trang chủ=${page.url()}`);
      expect.soft(page.url(), 'URL = trang chủ').toBe(`${WEB}/`);
    }
  } catch (e) {
    if (e instanceof SetupError) v = { verdict: 'Blocked', why: `không dựng được tiền điều kiện: ${e.message}` };
    else throw e;
  } finally {
    finish(info, obs, v);
    await ctx.close();
  }
}

function checkEmpty(c: Cart, e: { img: boolean; badge: boolean }, obs: string[]) {
  obs.push(`trạng thái trống: bảng=${c.hasTable ? 'có' : 'không'}, ảnh/icon=${c.hasImg ? 'có' : 'không'}, chữ="${c.mainText.slice(0, 80)}"`);
  expect.soft(c.hasTable, 'không có bảng sản phẩm').toBe(false);
  expect.soft(/trống/i.test(c.mainText), 'có dòng chữ báo giỏ trống').toBe(true);
  if (e.img) expect.soft(c.hasImg, 'có hình minh hoạ/icon (img hoặc svg)').toBe(true);
  if (e.badge) expect.soft(c.badge === null || c.badge === 0, `badge ẩn hoặc 0 (B22), thấy ${c.badge}`).toBe(true);
}

/** TC-205: nhập 2, bấm 1 lần, mở /cart; quay lại (link trong app), nhập 5, bấm 1 lần, mở /cart. */
async function runSv205(page: Page, info: TestInfo, obs: string[]) {
  await toHome(page);
  let d = await openDetail(page, 5);
  obs.push(`lần 1: value=${JSON.stringify(await typeQty(d.qty, '2'))}`);
  const fb = await clickAndWatch(page, d.add, info, 'TC-FR07-205');
  obs.push(`lần 1: ${fb.text}`);
  await toCart(page);
  const c1 = await readCart(page);
  obs.push(`sau lần 1: ${fmtCart(c1)}`);
  await shot(page, info, 'TC-FR07-205_ui_lan1', 'TC-FR07-205_ui_lan1');
  await toHome(page);
  d = await openDetail(page, 5);
  obs.push(`lần 2: value=${JSON.stringify(await typeQty(d.qty, '5'))}`);
  await d.add.click();
  await page.waitForTimeout(500);
  await toCart(page);
  const c2 = await readCart(page);
  obs.push(`sau lần 2: ${fmtCart(c2)}`);
  await shot(page, info, 'TC-FR07-205_ui');
  expect.soft(fb.kinds.length, 'lần 1: có phản hồi trong ≤ 2 s (B21)').toBeGreaterThan(0);
  expect.soft(c1.rows.map(r => [r.name, r.qty]), 'sau lần 1: id 5 × 2').toEqual([[PRODUCTS[5].name, 2]]);
  expect.soft(c2.rows.map(r => [r.name, r.qty]), 'sau lần 2: 1 dòng id 5 × 7 (FR-07.3)').toEqual([[PRODUCTS[5].name, 7]]);
}

// =============================== API (TS-DOM-API, TS-BVA-API, TS-SV-API) ===============================
type Res = { status: number; text: string; json: any };
type ApiCheck = (r: Res[], before: any[], after: any[], afterText: string) => void;
const is2xx = (s: number) => s >= 200 && s < 300;
const byId = (a: any[], id: number) => a.filter(x => x && x.id === id);
const ok2xx = (r: Res[]) => expect.soft(is2xx(r[0].status), `HTTP 2xx (nhận ${r[0].status})`).toBe(true);
const reject: ApiCheck = (r, b, a) => {
  expect.soft(r[0].status >= 400 && r[0].status < 500, `HTTP 4xx (nhận ${r[0].status})`).toBe(true);
  expect.soft(!!r[0].json && typeof r[0].json === 'object' && 'error' in r[0].json, 'body có trường error (B17)').toBe(true);
  expect.soft(a, 'GET /api/cart không đổi (SAU = TRƯỚC)').toEqual(b);
};
const addOne = (q: number): ApiCheck => (r, b, a) => {
  ok2xx(r);
  expect.soft(a.map(x => [x.id, x.quantity]), `[] → đúng 1 phần tử id 5, quantity ${q}`).toEqual([[5, q]]);
};
const API_ORACLE: Record<string, { h: string; check: ApiCheck }> = {
  'TC-FR07-20': { h: 'ad5a5918', check: (r, b, a) => {
    ok2xx(r);
    expect.soft(a.map(x => ({ id: x.id, name: x.name, price: x.price, quantity: x.quantity })), 'đúng 1 phần tử id 1')
      .toEqual([{ id: 1, name: 'iPhone 15 Pro Max', price: 30000000, quantity: 2 }]);
  } },
  'TC-FR07-21': { h: 'dfa4bce2', check: (r, b, a) => {
    ok2xx(r);
    expect.soft(a.length, 'vẫn 1 phần tử (không thêm phần tử mới)').toBe(b.length);
    expect.soft(byId(a, 2).map(x => x.quantity), 'phần tử id 2: quantity 1 → 4').toEqual([4]);
  } },
  'TC-FR07-22': { h: 'a32b2de1', check: (r, b, a) => {
    ok2xx(r);
    expect.soft(a.length, '2 → 3 phần tử').toBe(3);
    expect.soft(byId(a, 4).map(x => x.price), 'phần tử id 4 có price 6000000 (giá CSDL, B8)').toEqual([6000000]);
    expect.soft([...byId(a, 1), ...byId(a, 5)], 'id 1 và id 5 không đổi').toEqual([...byId(b, 1), ...byId(b, 5)]);
  } },
  'TC-FR07-30': { h: '0560100f', check: reject }, 'TC-FR07-31': { h: '0560100f', check: reject }, 'TC-FR07-32': { h: '0560100f', check: reject },
  'TC-FR07-33': { h: '0560100f', check: reject }, 'TC-FR07-34': { h: '0560100f', check: reject }, 'TC-FR07-35': { h: '0560100f', check: reject },
  'TC-FR07-36': { h: '0560100f', check: reject }, 'TC-FR07-37': { h: '0560100f', check: reject }, 'TC-FR07-38': { h: '0560100f', check: reject },
  'TC-FR07-39': { h: '0560100f', check: reject }, 'TC-FR07-40': { h: '0560100f', check: reject }, 'TC-FR07-70': { h: '0560100f', check: reject },
  'TC-FR07-71': { h: 'd4c50aa2', check: addOne(1) }, 'TC-FR07-72': { h: 'df9d74ee', check: addOne(2) },
  'TC-FR07-73': { h: '26964770', check: addOne(5) }, 'TC-FR07-74': { h: 'f1b3d4ec', check: addOne(1000) },
  'TC-FR07-208': { h: 'd836f568', check: reject }, 'TC-FR07-209': { h: 'd836f568', check: reject },
  'TC-FR07-210': { h: 'ac5dbdf5', check: (r, b, a) => {
    ok2xx(r);
    expect.soft(byId(a, 2).map(x => x.price), 'phần tử id 2 dùng giá CSDL 28000000, bỏ qua giá client (B8)').toEqual([28000000]);
  } },
  'TC-FR07-211': { h: 'd836f568', check: reject }, 'TC-FR07-212': { h: 'd836f568', check: reject },
  'TC-FR07-213': { h: '12bade95', check: (r, b, a) => {
    expect.soft(r.length, 'cả 50 request có phản hồi').toBe(50);
    expect.soft(r.filter(x => !is2xx(x.status)).map(x => x.status), 'mọi request được xử lý xong (2xx)').toEqual([]);
    expect.soft(a.map(x => [x.id, x.quantity]), 'đúng 1 phần tử id 1, quantity = 50 (FR-07.3 cho từng request)').toEqual([[1, 50]]);
  } },
  'TC-FR07-214': { h: 'eedc8aff', check: (r, b, a) => {
    expect.soft([400, 415], `HTTP 400 hoặc 415 (nhận ${r[0].status})`).toContain(r[0].status);
    expect.soft(a, 'giỏ không đổi').toEqual(b);
  } },
  'TC-FR07-215': { h: 'a1aeb000', check: (r, b, a, text) => {
    ok2xx(r);
    // so trên TEXT của response GET, không JSON.parse (JSON.parse làm tròn 9007199254740993 → 9007199254740992)
    expect.soft(/"quantity"\s*:\s*9007199254740993(?![\d.eE])/.test(text), `GET /api/cart (text) có quantity 9007199254740993 — thấy ${/"quantity"\s*:\s*[^,}]+/.exec(text)?.[0]}`).toBe(true);
  } },
};

/** Giá trị trong cột dữ liệu → token JSON thô (procedure TS-DOM-API bước 4). undefined = bỏ khoá khỏi body. */
function token(col: string, v: string, idCol: string): string | undefined {
  if (v === '— thiếu —') return undefined;
  const of = /^CSDL(?: của id (\d+))?$/.exec(v);
  if (of) {
    // 'CSDL' theo cột id; id không phải số (mảng/object của TC-211/212) → sản phẩm của số đầu tiên trong cột id
    const p = PRODUCTS[Number(of[1] ?? /\d+/.exec(idCol)?.[0])];
    return col === 'name' ? JSON.stringify(p.name) : String(p.price);
  }
  const raw = /^(\S+) \(gửi thô/.exec(v);                // "Infinity (gửi thô, không ngoặc kép)"
  return raw ? raw[1] : v;                              // số, "chuỗi", [mảng], {object}, 1e-324 … giữ nguyên văn
}

function rawBody(inp: any) {
  const parts: string[] = [];
  for (const k of ['id', 'name', 'price', 'quantity']) {
    const t = token(k, inp[k], inp.id);
    if (t !== undefined) parts.push(`"${k}": ${t}`);
  }
  return `{${parts.join(', ')}}`;
}

async function runApi(c: any, { request, page, accounts }: Ctx, info: TestInfo) {
  test.setTimeout(60_000);
  const o = API_ORACLE[c.id];
  if (!o) throw new Error(`${c.id}: chưa có oracle API`);
  if (o.h !== hashOf(c.expected_result)) throw new Error(`${c.id}: expected_result đã đổi so với lúc viết oracle (h=${o.h}, hiện tại ${hashOf(c.expected_result)}) — cập nhật API_ORACLE`);
  const inp = c.inputs;
  const obs: string[] = [];
  let v: Verdict | undefined;
  try {
    // Bước 1–3: user {ts}, token T, dựng giỏ ban đầu, GET TRƯỚC
    const a = await accounts.create(API_ACCOUNT, c.id);
    const T = await apiLogin(request, a);
    const auth = { Authorization: `Bearer ${T}` };
    for (const it of parseInitial(inp['Giỏ ban đầu'])) {
      const p = PRODUCTS[it.id];
      const r = await request.post(`${API}/api/cart`, { headers: auth, data: { id: it.id, name: p.name, price: p.price, quantity: it.qty } });
      if (r.status() !== 200) throw new SetupError(`dựng giỏ ban đầu id ${it.id}: HTTP ${r.status()}`);
    }
    const g0 = await request.get(`${API}/api/cart`, { headers: auth });
    const before = await g0.json();
    const want = parseInitial(inp['Giỏ ban đầu']).map(i => [i.id, i.qty]);
    if (g0.status() !== 200 || JSON.stringify(before.map((x: any) => [x.id, x.quantity])) !== JSON.stringify(want)) {
      v = { verdict: 'Blocked', why: `GET /api/cart TRƯỚC không khớp 'Giỏ ban đầu' (HTTP ${g0.status()}, ${JSON.stringify(before)}) (B20) — SV xác định case gốc` };
      return;
    }

    // Bước 4: gửi POST (body chuỗi thô; header theo cột Token; Content-Type/số request theo cột Cách thực hiện)
    const how: string = inp['Cách thực hiện'] || '';
    const headers: Record<string, string> = { 'Content-Type': /text\/plain/.test(how) ? 'text/plain' : 'application/json' };
    if (inp.Token === 'T') headers.Authorization = `Bearer ${T}`;
    else if (inp.Token === 'sai') headers.Authorization = BAD_TOKEN;
    const body = rawBody(inp);
    const n = Number(/gửi (\d+) request song song/.exec(how)?.[1] ?? 1);
    const send = () => request.post(`${API}/api/cart`, { headers, data: body });
    const raw = n > 1 ? await Promise.all(Array.from({ length: n }, send)) : [await send()];
    const res: Res[] = await Promise.all(raw.map(async r => {
      const text = await r.text();
      let json: any = null;
      try { json = JSON.parse(text); } catch { /* không phải JSON */ }
      return { status: r.status(), text, json };
    }));

    // Bước 5–6: GET SAU
    const g1 = await request.get(`${API}/api/cart`, { headers: auth });
    const afterText = await g1.text();
    let after: any[] = [];
    try { after = JSON.parse(afterText); } catch { /* giữ [] */ }

    const shownHeaders = { ...headers, ...(headers.Authorization ? { Authorization: inp.Token === 'T' ? 'Bearer <T>' : headers.Authorization } : {}) };
    await attachJson(info, `${c.id}_request`, { method: 'POST', url: '/api/cart', headers: shownHeaders, count: n, body_raw: body, before });
    await attachJson(info, `${c.id}_response`, { responses: res.map(r => ({ status: r.status, body: r.text })), get_after: { status: g1.status(), body_text: afterText } });
    const statuses = n > 1 ? Object.entries(res.reduce((m: Record<number, number>, r) => ((m[r.status] = (m[r.status] || 0) + 1), m), {})).map(([s, k]) => `${k}×HTTP ${s}`).join(', ') : `HTTP ${res[0].status} ${res[0].text.slice(0, 160)}`;
    obs.push(`POST ${n > 1 ? `${n} request song song: ` : ''}${statuses}`, `TRƯỚC: ${JSON.stringify(before)}`, `SAU: ${afterText.slice(0, 300)}`);
    await renderResponse(page!, info, c.id, `POST /api/cart\n${body}\n\n${res.slice(0, 3).map(r => `HTTP ${r.status}\n${r.text.slice(0, 500)}`).join('\n')}${n > 3 ? `\n… (${n} request)` : ''}\n\nGET /api/cart TRƯỚC: ${JSON.stringify(before)}\nGET /api/cart SAU: ${afterText.slice(0, 1500)}`);
    o.check(res, before, after, afterText);
  } catch (e) {
    if (e instanceof SetupError) v = { verdict: 'Blocked', why: `không dựng được tiền điều kiện: ${e.message}` };
    else throw e;
  } finally {
    finish(info, obs, v);
  }
}

// =============================== GUI (TS-GUI, step-by-step) ===============================
const GUI_H: Record<string, string> = {
  'TC-FR07-90': '2143e79f', 'TC-FR07-91': '50dc716b', 'TC-FR07-92': 'b8df3abd', 'TC-FR07-93': '16de2d0c', 'TC-FR07-94': '95d14c79',
  'TC-FR07-95': 'c6568a40', 'TC-FR07-96': 'fdf839f1', 'TC-FR07-97': 'de3db5ea', 'TC-FR07-98': '05a8dd52', 'TC-FR07-99': '5a3aadbd',
};
const G_ID = 4;                                         // test_data: "Sản phẩm id 4 'Tai nghe AirPods Pro 2'"
const MONEY_OK = (s: string) => /₫/.test(s) && /\d{1,3}([.,]\d{3})+/.test(s);

async function guiCart(page: Page) {
  await page.goto(`${WEB}/`);
  await waitHome(page);
  await homeAddBtn(page, G_ID).click();
  await page.waitForTimeout(300);
  await toCart(page);
  return readCart(page);
}

async function linkStyles(page: Page) {
  await page.mouse.move(5, (page.viewportSize()?.height ?? 600) - 5);   // chuột ra ngoài navbar (hover không tính)
  await page.waitForTimeout(300);
  return page.evaluate(() => [...document.querySelectorAll('header nav a')].map(a => {
    const s = getComputedStyle(a);
    return { href: a.getAttribute('href'), text: (a.textContent || '').trim(), style: [s.color, s.textDecorationLine, s.backgroundColor, s.fontWeight, s.borderBottomWidth + ' ' + s.borderBottomStyle].join(' | ') };
  }));
}

async function runGui(c: any, { browser }: Ctx, info: TestInfo) {
  test.setTimeout(90_000);
  if (GUI_H[c.id] !== hashOf(c.expected_result)) throw new Error(`${c.id}: expected_result đã đổi so với lúc viết oracle — cập nhật GUI_H`);
  const obs: string[] = [];
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  const dialogs: string[] = [];
  page.on('dialog', d => { dialogs.push(d.message()); d.dismiss().catch(() => {}); });
  try {
    switch (c.id) {
      case 'TC-FR07-90': {
        const cart = await guiCart(page);
        const r = cart.rows[0];
        obs.push(`dòng: ${fmtCart(cart)}`, `nút trong ô Số lượng: ${JSON.stringify(r?.qtyButtons ?? [])}`);
        await shot(page, info, `${c.id}_ui`);
        expect.soft(r?.qtyButtons.length ?? 0, "ô Số lượng có nút '+' và nút '-' (2 nút)").toBeGreaterThanOrEqual(2);
        break;
      }
      case 'TC-FR07-91': {
        await guiCart(page);
        const bc = page.locator('main nav, main [aria-label*="breadcrumb" i], main [class*="breadcrumb" i], main ol').first();
        const has = await bc.count();
        const items = has ? (await bc.locator('a, li, span').allInnerTexts()).map(s => s.trim()).filter(Boolean) : [];
        obs.push(has ? `breadcrumb: ${JSON.stringify(items)}` : 'không tìm thấy breadcrumb ở vùng nội dung chính');
        await shot(page, info, `${c.id}_ui`);
        expect.soft(has, 'có breadcrumb').toBeGreaterThan(0);
        if (has) {
          const homeItem = bc.locator('a[href="/"]').first();
          expect.soft(await homeItem.count(), 'có mục trỏ về trang chủ').toBeGreaterThan(0);
          expect.soft(/giỏ hàng/i.test(items[items.length - 1] ?? ''), 'mục cuối là Giỏ hàng').toBe(true);
          if (await homeItem.count()) {
            await homeItem.click();
            await page.waitForTimeout(500);
            obs.push(`URL sau khi bấm mục trang chủ=${page.url()}`);
            expect.soft(page.url(), 'URL = trang chủ').toBe(`${WEB}/`);
          }
        }
        break;
      }
      case 'TC-FR07-92': {
        await guiCart(page);
        const atCart = await linkStyles(page);
        await shot(page, info, `${c.id}_ui_cart`, `${c.id}_ui_cart`);
        await toHome(page);
        const atHome = await linkStyles(page);
        await shot(page, info, `${c.id}_ui_home`, `${c.id}_ui_home`);
        obs.push(`ở /cart: ${JSON.stringify(atCart)}`, `ở trang chủ: ${JSON.stringify(atHome)}`);
        const diff = (l: typeof atCart) => {
          const cart = l.find(x => x.href === '/cart')!;
          return l.filter(x => x.href !== '/cart').map(x => x.style !== cart.style);
        };
        expect.soft(diff(atCart).every(Boolean), 'ở /cart: link tới /cart khác kiểu hiển thị với mọi link khác').toBe(true);
        expect.soft(diff(atHome).some(Boolean), 'ở trang chủ: link tới /cart hiển thị như các link khác').toBe(false);
        break;
      }
      case 'TC-FR07-93': {
        const locale = await page.evaluate(() => navigator.language);
        await page.goto(`${WEB}/`);
        await waitHome(page);
        const cardText = await productLink(page, G_ID).locator('xpath=ancestor::div[.//img][1]').innerText();
        const homePrice = /\d[\d.,]*\d\s*(₫|đ|VND)?/.exec(cardText.replace(PRODUCTS[G_ID].name, ''))?.[0] ?? '';
        await productLink(page, G_ID).click();
        await expect(page.locator('main input').first()).toBeVisible();
        const detailText = await page.locator('main').innerText();
        const detailPrice = /\d{1,3}(?:[.,]\d{3})+\s*(₫|đ|VND)?|\d{4,}\s*(₫|đ|VND)?/.exec(detailText.replace(PRODUCTS[G_ID].name, ''))?.[0] ?? '';
        await toHome(page);
        await homeAddBtn(page, G_ID).click();
        await page.waitForTimeout(300);
        await toCart(page);
        const cells = await page.locator('main table tbody tr').first().locator('td').allInnerTexts();
        const ct = await readCart(page);
        const found = { 'trang chủ (thẻ)': homePrice, 'trang chi tiết': detailPrice, 'giỏ: Đơn giá': (cells[1] ?? '').trim(), 'giỏ: Thành tiền': (cells[3] ?? '').trim(), 'giỏ: Tổng': ct.totalText };
        obs.push(`locale trình duyệt=${locale}`, ...Object.entries(found).map(([k, s]) => `${k}=${JSON.stringify(s)}`));
        await shot(page, info, `${c.id}_ui`);
        for (const [k, s] of Object.entries(found)) expect.soft(MONEY_OK(s), `${k}: có '₫' và phân cách hàng nghìn '.' hoặc ',' (B13) — ${JSON.stringify(s)}`).toBe(true);
        break;
      }
      case 'TC-FR07-94': {
        await page.goto(`${WEB}/`);
        await waitHome(page);
        const homeAlts = await page.locator('main img').evaluateAll(els => els.map(e => e.getAttribute('alt')));
        await productLink(page, G_ID).click();
        await expect(page.locator('main input').first()).toBeVisible();
        const detailAlts = await page.locator('main img').evaluateAll(els => els.map(e => e.getAttribute('alt')));
        await toHome(page);
        await homeAddBtn(page, G_ID).click();
        await page.waitForTimeout(300);
        await toCart(page);
        const cartAlts = await page.locator('main img').evaluateAll(els => els.map(e => e.getAttribute('alt')));
        obs.push(`alt trang chủ=${JSON.stringify(homeAlts)}`, `alt trang chi tiết=${JSON.stringify(detailAlts)}`,
          cartAlts.length ? `alt trang giỏ=${JSON.stringify(cartAlts)}` : 'trang giỏ không có ảnh sản phẩm (notes, không tính Fail)',
          '[kiểm tay] alt "mô tả nội dung ảnh": SV đối chiếu chữ alt với ảnh');
        await shot(page, info, `${c.id}_ui`);
        for (const [k, l] of [['trang chủ', homeAlts], ['trang chi tiết', detailAlts], ['trang giỏ', cartAlts]] as const)
          expect.soft(l.filter(a => !a || !a.trim()).length, `${k}: mọi ảnh sản phẩm có alt không rỗng`).toBe(0);
        break;
      }
      case 'TC-FR07-95': case 'TC-FR07-96': case 'TC-FR07-97': case 'TC-FR07-98': {
        const cart = await guiCart(page);
        let got: string[], want: string[];
        if (c.id === 'TC-FR07-95') { got = cart.headers; want = ['Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác']; }
        else if (c.id === 'TC-FR07-96') { got = await page.locator('main table tbody tr').first().locator('td').nth(4).locator('button').allInnerTexts(); want = ['Xóa sản phẩm']; }
        else if (c.id === 'TC-FR07-97') { got = await page.locator('main a[href="/"]').allInnerTexts(); want = ['Tiếp tục mua sắm']; }
        else { got = [cart.totalLabel]; want = ['Tổng cộng']; }
        obs.push(`nhãn đọc được=${JSON.stringify(got)}`);
        await shot(page, info, `${c.id}_ui`);
        expect.soft(got.map(normLabel), `nhãn khớp đúng chữ theo B12: ${JSON.stringify(want)}`).toEqual(want.map(normLabel));
        break;
      }
      case 'TC-FR07-99': {
        await page.goto(`${WEB}/`);
        await waitHome(page);
        const fb = await clickAndWatch(page, homeAddBtn(page, G_ID), info, c.id);
        obs.push(fb.text);
        await shot(page, info, `${c.id}_ui`);
        expect.soft(fb.kinds.length, 'có ít nhất một phản hồi nhìn thấy được trong ≤ 2 s (B21)').toBeGreaterThan(0);
        break;
      }
      default: throw new Error(`${c.id}: chưa có cách chạy GUI`);
    }
    if (dialogs.length) obs.push(`dialog=${JSON.stringify(dialogs)}`);
  } finally {
    finish(info, obs);
    await ctx.close();
  }
}

// =============================== Đăng ký test ===============================
// In dấu vân tay Expected khi cần cập nhật bảng oracle: $env:B07_HASH=1; npx playwright test B_FR07 --list
if (process.env.B07_HASH) for (const c of allCases) console.log(`${c.id} ${hashOf(c.expected_result)}`);

// Test API dùng fixture `page` (chỉ để render ảnh response); test UI/GUI tự mở context mới.
for (const s of data.suites) {
  test.describe(`${s.id} ${s.name}`, () => {
    for (const c of s.cases) {
      const title = `${c.id} ${c.title}`;
      if (s.id === 'TS-GUI') test(title, async ({ browser, request, accounts }, info) => runGui(c, { browser, request, accounts }, info));
      else if (c.layer === 'API') test(title, async ({ browser, request, page, accounts }, info) => runApi(c, { browser, request, page, accounts }, info));
      else test(title, async ({ browser, request, accounts }, info) => runUi(c, { browser, request, accounts }, info));
    }
  });
}
