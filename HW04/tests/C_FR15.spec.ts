/**
 * C_FR15 – FR-15 Quản lý sản phẩm (web admin :5174, tab 'Sản phẩm'). Skill playwright-ddt-automation, bước 3.
 * Data-driven: giá trị vào + oracle đọc từ HW04/data/C_FR15.json (expected nguyên văn HW02 + sha1, kiểm khi nạp);
 * selector/chữ không có trong expected nằm ở `assumptions` của file data (giả định, chờ SV duyệt) — không gõ cứng ở spec.
 * Procedure HW02 TS-DOM-UI bước 1–7: (Sửa/Xóa) dựng M qua API → GET TRƯỚC (+ M_TRƯỚC) → đăng nhập admin → tab 'Sản phẩm'
 * → TRƯỚC_UI → thao tác ĐÚNG 1 lần (bấm 'Lưu sản phẩm' / 'Xóa' một lần) → quan sát (bong bóng HTML5, hộp thoại, thông báo
 * trên trang) → SAU_UI + GET SAU (+ M_SAU). So giá như HW02 (HW02/tests/C_FR15/lib.ts dòng 147 sameNumber: so giá trị số;
 * null/"" không khớp); GET /api/products/:id id chẵn trả price dạng chuỗi (BUG-48) → annotation.
 * Assertion: trạng thái UI (toBeVisible), nội dung (toHaveText), oracle dữ liệu GET trước/sau (toEqual), đếm/giá trị
 * (toHaveCount/toHaveValue/toBe). Dùng expect.soft. C2=a (SV chốt): health-check backend sau mỗi case ở fixture.
 */
import { errors, type Page } from '@playwright/test';
import { test, expect, loadData, fill, resetDb, blocked, expandValue, type Product } from './fixtures/c_fr15';
import { API } from './fixtures/ddt';
import { parseExpectedC, type CName } from './oracles/c_fr15.oracle';
import type { TableRow } from './pages/admin.pages';

const DATA = loadData('C_FR15');           // ném lỗi nếu sha1(expected) lệch → cả file không chạy
const COL = { op: 'Thao tác CRUD', name: 'Tên sản phẩm', price: 'Giá', cat: 'Danh mục', desc: 'Mô tả', url: 'URL Ảnh' };
const KEEP = '(giữ)';                      // procedure bước 5: "ô ghi '(giữ)' không chạm"
const NONE = '—';                          // thao tác Xóa: cột không dùng
const WAIT = 10_000;                       // chờ phản hồi mạng/hộp thoại sau thao tác; quá hạn → Blocked

/** Giả định trong file data (ngoài expected). Thiếu → ném lỗi, không đoán. */
const assumption = (key: string) => {
  const a = DATA.assumptions?.[key];
  if (!a?.value) throw new Error(`[C_FR15] thiếu assumptions.${key} trong HW04/data/C_FR15.json`);
  return a;
};
/** Escape chuỗi lấy từ data trước khi dựng RegExp. */
const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** So giá trị số như HW02 (lib.ts dòng 147): null/"" không khớp; số nguyên vượt an toàn so chuỗi BigInt. */
const sameNumber = (actual: unknown, expected: number) =>
  !Number.isSafeInteger(expected) && Number.isInteger(expected)
    ? String(actual) === String(BigInt(expected))
    : actual !== null && actual !== '' && actual !== undefined && Number(actual) === expected;
/** Chuẩn hoá trường số để toEqual cùng nghĩa với sameNumber: số/chuỗi số → number; null/""/undefined giữ nguyên. */
const numish = (v: unknown) => (v === null || v === '' || v === undefined ? v : Number(v));
const nameOf = (n: CName, ts: number) => expandValue(fill(n, ts)).value;
const byId = (ps: Product[]) => [...ps].sort((a, b) => a.id - b.id);
const short = (s: string) => (s.length > 60 ? `${s.slice(0, 20)}…(${s.length} ký tự)` : s);

/** Bước điều hướng/chuẩn bị (không phải assertion): quá hạn → Blocked. */
async function step<T>(what: string, fn: () => Promise<T>): Promise<T> {
  try { return await fn(); } catch (e) {
    if (e instanceof errors.TimeoutError) blocked(`${what}: ${String(e).split('\n')[0]}`);
    throw e;
  }
}
/** Chờ một trạng thái rõ ràng (điều kiện phía Node: log mạng, số hộp thoại) tối đa WAIT; quá hạn → Blocked. */
async function until(what: string, cond: () => boolean) {
  const t0 = Date.now();
  while (!cond()) {
    if (Date.now() - t0 > WAIT) blocked(`${what}: quá ${WAIT} ms`);
    await new Promise(r => setTimeout(r, 50));
  }
}
/** Đợi React render xong sau khi dữ liệu về (2 khung hình). */
const settle = (page: Page) => page.evaluate(() => new Promise<void>(r => requestAnimationFrame(() => requestAnimationFrame(() => r()))));

test.beforeAll(async ({}, testInfo) => {
  testInfo.setTimeout(120_000);
  if (testInfo.config.workers > 1)
    throw new Error(`[C_FR15] workers = ${testInfo.config.workers}: resetDb không an toàn khi chạy song song — chạy với --workers=1`);
  resetDb();                               // tiền điều kiện suite: CSDL seed sạch (C0)
});

for (const c of DATA.testcases) {
  test(`${c.tc_id} ${c.title}`, async ({ page, admin }) => {
    const info = test.info();
    const ann = (type: string, description: string) => info.annotations.push({ type, description });
    ann('expected', c.expected);
    ann('hw02', `${c.hw02.status}${c.hw02.bug_id ? ' ' + c.hw02.bug_id : ''}`);
    const ts = Date.now();
    const o = parseExpectedC(c.expected);                     // không xác định được loại kết quả → ném lỗi
    for (const u of o.unmapped) ann('oracle không tự động', u);
    const op = c.inputs[COL.op];
    if (!['Thêm', 'Sửa', 'Xóa'].includes(op)) throw new Error(`${c.tc_id}: cột '${COL.op}' không hỗ trợ: "${op}"`);
    const { catalog, form, table, dialogs } = admin;
    const priceIsString = (label: string, p: unknown) => {
      if (p && typeof p === 'object' && typeof (p as Product).price === 'string')
        ann('price dạng chuỗi (BUG-48)', `${label}: price = ${JSON.stringify((p as Product).price)} (GET /api/products/:id, id chẵn)`);
    };

    // Bước 1–2: dựng M (Sửa/Xóa), GET TRƯỚC (+ M_TRƯỚC)
    const M = op === 'Thêm' ? null : await step('Dựng M', () => admin.createTarget(c.tc_id, ts));
    const before = await catalog.list();
    const mBefore = M ? await catalog.get(M.id) : null;
    priceIsString('M_TRƯỚC', mBefore);

    // Bước 3–4: đăng nhập, tab 'Sản phẩm', TRƯỚC_UI
    await step('Đăng nhập admin + mở tab Sản phẩm', () => admin.loginAndOpenProducts());
    await expect.soft(form.save, "form sản phẩm có nút 'Lưu sản phẩm'").toBeVisible();
    const tBefore = await table.read();
    ann('TRƯỚC', `bản ghi ${before.length}; bảng ${tBefore.length} dòng${M ? `; M = id ${M.id} ${JSON.stringify(mBefore)}` : ''}`);
    const mRowIdx = M ? tBefore.findIndex(r => r.name === M.name) : -1;
    if (M && mRowIdx < 0) blocked(`không thấy dòng '${M.name}' trên bảng TRƯỚC_UI`);

    // Bước 5: điền form (Thêm/Sửa) theo cột; '(giữ)' không chạm
    if (op === 'Sửa') {
      await step("Bấm 'Sửa' trên dòng M", async () => {
        await table.editButton(M!.name).click();
        await expect(form.name).toHaveValue(M!.name);            // form đã nạp dữ liệu M (chờ trạng thái, không phải oracle)
      });
    }
    if (op !== 'Xóa') {
      for (const col of [COL.name, COL.price, COL.desc, COL.url]) {
        const raw = c.inputs[col];
        if (raw === KEEP || raw === NONE || raw === undefined) continue;
        const { value, long } = expandValue(fill(raw, ts));
        const got = await form.setText(form.field(col), value, long);
        if (col === COL.price) ann('ô Giá tiền sau khi nhập', JSON.stringify({ nhập: value, value: got }));
        else await expect.soft(form.field(col), `ô '${col}' giữ đúng chuỗi đã nhập`).toHaveValue(value);
      }
      const cat = c.inputs[COL.cat];
      if (cat !== KEEP && cat !== NONE && cat !== undefined) await form.selectCategory(cat);
    }

    // Bước 5–6: thao tác ĐÚNG 1 lần + quan sát (không phân loại nội dung thông báo – HW02 H4)
    const msgSel = assumption('page_message_selector').value;
    const pageMessages = () => page.evaluate((sel: string) =>
      Array.from(document.querySelectorAll(sel)).map(e => (e.textContent ?? '').replace(/\s+/g, ' ').trim()).filter(Boolean), msgSel);
    await page.evaluate(() => {                                  // ô không hợp lệ: sự kiện 'invalid' trình duyệt bắn trong lần bấm
      const w = window as unknown as { __inv: string[]; __invHooked?: boolean };
      w.__inv = [];
      if (!w.__invHooked) {
        document.addEventListener('invalid', e => {
          const el = e.target as HTMLInputElement;
          w.__inv.push(`${el.placeholder || el.tagName}: ${el.validationMessage}`);
        }, true);
        w.__invHooked = true;
      }
    });
    const msgBefore = await pageMessages();
    const n0 = dialogs.length;
    const net: { method: string; url: string; status: number; done: Promise<unknown> }[] = [];
    page.on('response', r => { if (r.url().startsWith(`${API}/api/products`)) net.push({ method: r.request().method(), url: r.url(), status: r.status(), done: r.finished() }); });
    const sent = (method: string) => net.find(x => x.method === method);
    const listAfter = (i: number) => net.slice(i + 1).find(x => x.method === 'GET' && x.url === `${API}/api/products`);

    if (op === 'Xóa') {
      await table.deleteButton(M!.name).click();                 // ĐÚNG 1 lần
      await until('chờ DELETE /api/products/M', () => !!sent('DELETE'));
      const i = net.indexOf(sent('DELETE')!);
      if (sent('DELETE')!.status === 200) { await until('chờ GET /api/products sau khi xoá', () => !!listAfter(i)); await listAfter(i)!.done; }
      else await until('chờ hộp thoại lỗi xoá', () => dialogs.length > n0);
    } else {
      const valid = await form.root.evaluate((f: HTMLFormElement) => f.checkValidity());
      await form.save.click();                                   // ĐÚNG 1 lần
      if (valid) {
        const method = op === 'Thêm' ? 'POST' : 'PUT';
        await until(`chờ ${method} /api/products`, () => !!sent(method));
        const s = sent(method)!;
        if (s.status !== 200) await until('chờ hộp thoại lỗi lưu', () => dialogs.length > n0);
        else if (op === 'Thêm') { const i = net.indexOf(s); await until('chờ GET /api/products sau khi thêm', () => !!listAfter(i)); await listAfter(i)!.done; }
        else await until("chờ hộp thoại sau khi lưu (Sửa)", () => dialogs.length > n0);
      }
    }
    await settle(page);
    const invalid: string[] = await page.evaluate(() => [...(window as unknown as { __inv: string[] }).__inv]);
    const newDialogs = dialogs.slice(n0);
    const pageMsgs = (await pageMessages()).filter(m => !msgBefore.includes(m));
    const errShown = invalid.length > 0 || newDialogs.length > 0 || pageMsgs.length > 0;
    ann('quan sát sau thao tác', JSON.stringify({
      'ô không hợp lệ HTML5': invalid, 'hộp thoại': newDialogs.map(d => d.message), 'thông báo mới trên trang': pageMsgs,
      'request': net.map(x => `${x.method} ${x.url.replace(API, '')} → ${x.status}`),
    }));
    // ảnh ngay sau thao tác chính, chụp SAU khi đo xong (không song song với việc chờ/đo)
    await info.attach(`${c.tc_id}_after-save`, { body: await page.screenshot(), contentType: 'image/png' });

    // Bước 7: SAU_UI, GET SAU (+ M_SAU)
    const tAfter = await table.read();
    const after = await catalog.list();
    const mAfter = M ? await catalog.get(M.id) : null;
    priceIsString('M_SAU', mAfter);
    const added = after.filter(p => !before.some(b => b.id === p.id));
    const tAdded = tAfter.filter(x => !tBefore.some(y => y.name === x.name && y.priceRaw === x.priceRaw));
    ann('SAU', JSON.stringify({
      'bản ghi': `${before.length} → ${after.length}`, 'bản ghi mới': added.map(p => ({ ...p, name: short(p.name) })),
      'bảng': `${tBefore.length} → ${tAfter.length} dòng`, 'dòng mới/đổi': tAdded.map(r => `${short(r.name)} | ${r.priceRaw}`),
      ...(M ? { M_SAU: mAfter } : {}),
    }));

    // ---- Oracle: thông báo ----
    if (o.noErr) expect.soft(errShown, 'không có thông báo lỗi (EC73)').toBe(false);
    if (o.errShown) {
      expect.soft(errShown, 'có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)').toBe(true);
      if (errShown && !invalid.length && !pageMsgs.length)
        ann('oracle thông báo yếu', `chỉ có hộp thoại ${JSON.stringify(newDialogs.map(d => d.message))} — đếm là "có thông báo" như HW02 (H4: không phân loại nội dung), SV xét`);
    }

    // ---- Oracle: bảng (UI) ----
    if (o.table.unchanged) expect.soft(tAfter, 'bảng SAU_UI = TRƯỚC_UI').toEqual(tBefore);
    if (o.table.addedRow) {
      expect.soft(tAfter.length, 'bảng có thêm đúng 1 dòng').toBe(tBefore.length + 1);
      const want = o.table.addedRow.name !== undefined ? nameOf(o.table.addedRow.name, ts) : undefined;
      const row: TableRow | undefined = want !== undefined ? tAdded.find(r => r.name === want) : tAdded[0];
      if (want !== undefined) {
        await expect.soft(table.row(want), `bảng có đúng 1 dòng 'Tên SP' = '${short(want)}'`).toHaveCount(1);
        await expect.soft(table.row(want).first(), `dòng mới '${short(want)}' hiển thị`).toBeVisible();
      }
      if (o.table.addedRow.price !== undefined) expect.soft(row?.price, "dòng mới: 'Giá' (so giá trị số)").toBe(o.table.addedRow.price);
    }
    if (o.table.mRow) {
      const cell = table.rows.nth(mRowIdx).locator('td').nth(1);
      if (o.table.mRow.name !== undefined) await expect.soft(cell, "dòng của M: 'Tên SP'").toHaveText(nameOf(o.table.mRow.name, ts));
      if (o.table.mRow.price !== undefined) expect.soft(tAfter[mRowIdx]?.price, "dòng của M: 'Giá' (so giá trị số)").toBe(o.table.mRow.price);
    }
    if (o.table.othersSame)
      expect.soft(tAfter.filter((_, i) => i !== mRowIdx), 'mọi dòng khác SAU_UI = TRƯỚC_UI').toEqual(tBefore.filter((_, i) => i !== mRowIdx));
    if (o.table.countSame) await expect.soft(table.rows, 'số dòng không đổi').toHaveCount(tBefore.length);
    if (o.table.gone !== undefined) await expect.soft(table.row(nameOf(o.table.gone, ts)), `bảng không còn dòng '${nameOf(o.table.gone, ts)}'`).toHaveCount(0);
    if (o.table.countDelta !== undefined) await expect.soft(table.rows, 'số dòng SAU_UI').toHaveCount(tBefore.length + o.table.countDelta);

    // ---- Oracle: dữ liệu (API GET trước/sau) ----
    if (o.data.listSame) expect.soft(byId(after), 'GET /api/products SAU = TRƯỚC').toEqual(byId(before));
    if (o.data.mSame) expect.soft(mAfter, 'M_SAU = M_TRƯỚC').toEqual(mBefore);
    if (o.data.countDelta !== undefined) expect.soft(after.length, 'số bản ghi SAU').toBe(before.length + o.data.countDelta);
    if (o.data.newRec) {
      const n = added[0];
      const want: Record<string, unknown> = {}, got: Record<string, unknown> = {};
      if (o.data.newRec.name !== undefined) { want.name = nameOf(o.data.newRec.name, ts); got.name = n?.name; }
      if (o.data.newRec.price !== undefined) { want.price = o.data.newRec.price; got.price = numish(n?.price); }
      if (o.data.newRec.category_id !== undefined) { want.category_id = o.data.newRec.category_id; got.category_id = numish(n?.category_id); }
      expect.soft(got, `bản ghi mới (so giá trị số), thấy ${n ? JSON.stringify({ ...n, name: short(n.name) }) : 'không có'}`).toEqual(want);
      if (o.data.newRec.price !== undefined) expect.soft(sameNumber(n?.price, o.data.newRec.price), 'price bản ghi mới (sameNumber như HW02)').toBe(true);
    }
    if (o.data.m) {
      const m = mAfter as Product | null;
      const want: Record<string, unknown> = {}, got: Record<string, unknown> = {};
      if (o.data.m.name !== undefined) { want.name = nameOf(o.data.m.name, ts); got.name = m?.name; }
      if (o.data.m.price !== undefined) { want.price = o.data.m.price; got.price = numish(m?.price); }
      if (o.data.m.category_id !== undefined) { want.category_id = o.data.m.category_id; got.category_id = numish(m?.category_id); }
      expect.soft(got, 'M_SAU (so giá trị số)').toEqual(want);
    }
    if (o.data.keep) {
      const k = o.data.keep;
      expect.soft(k.map(x => String((mAfter as Record<string, unknown> | null)?.[x])), `M_SAU ${k.join(', ')} = M_TRƯỚC`)
        .toEqual(k.map(x => String((mBefore as Record<string, unknown> | null)?.[x])));
    }
    if (o.data.mGone) expect.soft(after.map(p => p.id), 'GET /api/products SAU không còn id M').not.toContain(M!.id);

    // ---- Oracle: case SV ----
    if (o.noXssAlert) {
      const xss = assumption('xss_alert_text');
      const re = new RegExp(`^\\s*${esc(xss.value)}\\s*$`);
      expect.soft(newDialogs.filter(d => re.test(d.message)), `không kích hoạt alert XSS (không có hộp thoại '${xss.value}' — ${xss.note})`).toEqual([]);
    }
    if (o.formBlocked) {
      const fb = assumption('form_blocked_means');
      ann('oracle Form chặn', `${fb.value} (${fb.note})`);
      expect.soft(byId(after), `form chặn: ${fb.value}`).toEqual(byId(before));
    }
  });
}
