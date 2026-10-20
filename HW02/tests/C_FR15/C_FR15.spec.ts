/**
 * FR-15 Quản lý Sản phẩm (admin) — chạy các test case tự động trong HW02/C_FR15/testcases.json.
 * Tiêu đề test = "<mã TC> <tiêu đề>" để merge_results.py gộp được.
 * Oracle case AI: ./oracle.ts (sinh từ expected_result, khoá bằng h = sha1). Oracle case SV: bảng SV_ORACLE bên dưới, cũng khoá bằng h.
 * Expected trong JSON đổi → test báo lỗi "oracle cũ", không tự chạy theo bản cũ. Nhiều khẳng định → expect.soft; mọi chỗ lệch nằm trong Actual.
 * Case manual (TS-GUI 90–94): không có test ở đây — SV kiểm tay theo HW02/C_FR15/RUN.md.
 * Chạy (PowerShell, trong HW02/tests): xem HW02/C_FR15/RUN.md
 */
import { APIRequestContext, Page, TestInfo } from '@playwright/test';
import { ORACLE, Oracle } from './oracle';
import {
  test, expect, data, hashOf, API, ADMIN_UI, USER, BAD_TOKEN, CATEGORY, fill, nameOf, repeatOf, SetupError, login, listProducts, getProduct,
  createM, sweep, shot, attachJson, renderResponse, money, sameNumber, ERR, uiLogin, productForm, readTable, rowByName, setField,
  clickAndObserve, finish, Product,
} from './lib';

type Env = { ta: string; ts: string; startIds: Set<number> };

// =============================== Oracle case SV (TS-SV-*) ===============================
// Chép từ expected_result của SV; h khoá bản Expected. Không có trong bảng → test báo lỗi.
const SV_ORACLE: Record<string, { h: string; note: string }> = {
  'TC-FR15-200': { h: '7e15e03c', note: 'báo lỗi (C7/C16) + không có hộp thoại do script (alert(1)) (C21, SEC-04)' },
  'TC-FR15-201': { h: 'eda1506c', note: 'form chặn: không gửi được — dữ liệu SAU = TRƯỚC (C24)' },
  'TC-FR15-202': { h: '77b20ba4', note: 'thêm 1 bản ghi price = 7000000 (số); bảng Giá = 7.000.000 ₫ (C17: . hoặc ,)' },
  'TC-FR15-205': { h: '94d4ebda', note: 'ô chặn nhập/dán (value rỗng) hoặc có thông báo lỗi; dữ liệu SAU = TRƯỚC' },
  'TC-FR15-206': { h: '598fb82e', note: 'form hiện dữ liệu SP2; sau Lưu chỉ SP2 đổi, SP1 = TRƯỚC (FR-15.5)' },
  'TC-FR15-207': { h: '16f9fa91', note: '2xx; name lưu nguyên văn; bảng products nguyên vẹn (mọi id TRƯỚC còn, GET 200)' },
  'TC-FR15-208': { h: 'fae0b4d2', note: '4xx + error; dữ liệu SAU = TRƯỚC' },
  'TC-FR15-209': { h: '6db99625', note: '4xx + body JSON có error (không phải trang HTML); dữ liệu SAU = TRƯỚC (C20)' },
  'TC-FR15-211': { h: 'cb8f8bf4', note: '4xx (400 hoặc 415); không tạo sản phẩm' },
  'TC-FR15-213': { h: '0599087a', note: '(a) 2xx + name/price/category_id của M cập nhật, hoặc (b) 4xx + M = TRƯỚC; luôn: M vẫn ở id M' },
  'TC-FR15-214': { h: '906d6892', note: '4xx + error; dữ liệu SAU = TRƯỚC (C23)' },
};
const MANUAL = new Set(['TS-GUI']);
const nnOf = (id: string) => id.split('-').pop()!;
const is2xx = (s: number) => s >= 200 && s <= 299;
const is4xx = (s: number) => s >= 400 && s <= 499;
const fmt = (p: Product | undefined) => p ? `{id ${p.id}, name ${JSON.stringify(p.name)}, price ${JSON.stringify(p.price)}, category_id ${JSON.stringify(p.category_id)}}` : 'không có';
const sameList = (a: Product[], b: Product[]) => JSON.stringify([...a].sort((x, y) => x.id - y.id)) === JSON.stringify([...b].sort((x, y) => x.id - y.id));

function checkHash(c: any) {
  const want = ORACLE[c.id]?.h ?? SV_ORACLE[c.id]?.h;
  if (!want) throw new Error(`${c.id}: chưa có oracle`);
  if (want !== hashOf(c.expected_result))
    throw new Error(`${c.id}: expected_result đã đổi so với lúc viết oracle (h=${want}, hiện tại ${hashOf(c.expected_result)}) — cập nhật oracle`);
}

// =============================== UI ===============================
async function runUi(c: any, page: Page, request: APIRequestContext, env: Env, info: TestInfo) {
  checkHash(c);
  const nn = nnOf(c.id), ts = env.ts, inp = c.inputs, op = inp['Thao tác CRUD'];
  const obs: string[] = [];
  let M: { id: number; body: any } | undefined, M2: { id: number; body: any } | undefined;
  try {
    if (op === 'Sửa' || op === 'Xóa') M = await createM(request, env.ta, ts, nn);
    if (c.id === 'TC-FR15-206') M2 = await createM(request, env.ta, ts, `${nn}b`);
  } catch (e) {
    if (e instanceof SetupError) return finish(info, [], { v: 'Blocked', why: e.message });
    throw e;
  }
  const before = (await listProducts(request)).list;
  const mBefore = M ? (await getProduct(request, M.id)).body : null;
  const m2Before = M2 ? (await getProduct(request, M2.id)).body : null;
  await uiLogin(page);
  const tBefore = await readTable(page, before.length);
  if (tBefore.length !== before.length) obs.push(`ghi chú: TRƯỚC_UI ${tBefore.length} dòng ≠ TRƯỚC ${before.length} bản ghi`);
  const mRowIdx = M ? tBefore.findIndex(r => r.name === M!.body.name) : -1;

  // ---- thao tác (procedure bước 5–6) ----
  let r = { dialogs: [] as string[], invalid: [] as string[] };
  const fields = ['Tên sản phẩm', 'Giá', 'Danh mục', 'URL Ảnh', 'Mô tả'] as const;
  const value = (f: string) => { const v = inp[f]; return v === undefined ? '(giữ)' : fill(v, ts, nn); };
  let formShowsSp2: string | undefined;
  let priceValue = '';
  if (op === 'Thêm' || op === 'Sửa') {
    if (op === 'Sửa') {
      if (c.id === 'TC-FR15-206') {
        // SV TC-206: Sửa SP1, chỉnh tên, rồi bấm Sửa SP2 (không Hủy sửa) — rồi nhập cột của case cho SP2
        await rowByName(page, M!.body.name).getByRole('button', { name: 'Sửa' }).click();
        await setField(page, 'Tên sản phẩm', `SP1 tạm ${ts}`);
        await rowByName(page, M2!.body.name).getByRole('button', { name: 'Sửa' }).click();
        const f = productForm(page);
        formShowsSp2 = JSON.stringify({ name: await f.getByPlaceholder('Tên sản phẩm', { exact: true }).inputValue(), price: await f.getByPlaceholder('Giá tiền', { exact: true }).inputValue(), cat: await f.locator('select').inputValue() });
      } else await rowByName(page, M!.body.name).getByRole('button', { name: 'Sửa' }).click();
    }
    for (const f of fields) await setField(page, f, value(f));
    const priceBox = productForm(page).getByPlaceholder('Giá tiền', { exact: true });
    priceValue = await priceBox.inputValue();
    obs.push(`giá trị ô Giá tiền trước khi lưu: ${JSON.stringify(priceValue)}`);
    r = await clickAndObserve(page, () => page.getByRole('button', { name: 'Lưu sản phẩm' }).click());
  } else if (op === 'Xóa') {
    r = await clickAndObserve(page, () => rowByName(page, M!.body.name).getByRole('button', { name: 'Xóa' }).click());
  }
  const after = (await listProducts(request)).list;
  const tAfter = await readTable(page, after.length);
  const mAfter = M ? (await getProduct(request, M.id)) : null;
  await shot(page, info, `${c.id}_ui`);

  const errShown = r.invalid.length > 0 || r.dialogs.some(d => ERR.test(d));
  obs.push(`hộp thoại: ${r.dialogs.length ? r.dialogs.map(d => JSON.stringify(d)).join(', ') : 'không có'}`);
  obs.push(`ô không hợp lệ (HTML5): ${r.invalid.length ? r.invalid.join(' | ') : 'không có'}`);
  obs.push(`bản ghi TRƯỚC → SAU: ${before.length} → ${after.length}`);
  const added = after.filter(p => !before.some(b => b.id === p.id));
  if (added.length) obs.push(`bản ghi mới: ${added.map(fmt).join(', ')}`);
  if (M) obs.push(`M_TRƯỚC ${fmt(mBefore)} → M_SAU ${mAfter?.body && mAfter.body.id ? fmt(mAfter.body) : `HTTP ${mAfter?.status} ${mAfter?.text.slice(0, 80)}`}`);
  obs.push(`bảng TRƯỚC → SAU: ${tBefore.length} → ${tAfter.length} dòng`);
  const tAdded = tAfter.filter(x => !tBefore.some(y => y.name === x.name && y.priceText === x.priceText));
  if (tAdded.length) obs.push(`dòng mới/đổi trên bảng: ${tAdded.map(x => `[${x.name.length > 60 ? x.name.slice(0, 20) + `…(${x.name.length} ký tự)` : x.name} | ${x.priceText}]`).join(' ')}`);
  if (formShowsSp2) obs.push(`form sau khi bấm Sửa SP2: ${formShowsSp2}; SP2 TRƯỚC ${fmt(m2Before)}`);
  finish(info, obs);

  // ---- oracle ----
  const o: Oracle | undefined = ORACLE[c.id];
  if (o?.kind === 'reject') {
    expect.soft(errShown, 'có thông báo lỗi (bong bóng HTML5 / hộp thoại / trên trang) (C7, C16)').toBe(true);
    expect.soft(tAfter, 'bảng SAU_UI = TRƯỚC_UI').toEqual(tBefore);
    expect.soft(sameList(after, before), 'GET /api/products SAU = TRƯỚC').toBe(true);
    if (o.mSame) expect.soft(mAfter?.body, 'M_SAU = M_TRƯỚC').toEqual(mBefore);
  } else if (o?.kind === 'add') {
    if (o.noErr) expect.soft(errShown, 'không có thông báo lỗi (EC73)').toBe(false);
    expect.soft(after.length, 'số bản ghi SAU = TRƯỚC + 1').toBe(before.length + 1);
    const n = added[0];
    if (o.name !== undefined) expect.soft(n?.name, 'name bản ghi mới').toBe(nameOf(o.name, ts, nn));
    if (o.price !== undefined) expect.soft(sameNumber(n?.price, o.price), `price bản ghi mới = ${o.price} (so giá trị số), thấy ${JSON.stringify(n?.price)}`).toBe(true);
    if (o.cat !== undefined) expect.soft(sameNumber(n?.category_id, o.cat), `category_id = ${o.cat}, thấy ${JSON.stringify(n?.category_id)}`).toBe(true);
    expect.soft(tAfter.length, 'bảng có thêm đúng 1 dòng').toBe(tBefore.length + 1);
    const row = tAdded.find(x => o.tName === undefined || x.name === nameOf(o.tName, ts, nn));
    if (o.tName !== undefined) expect.soft(row?.name, "dòng mới: 'Tên SP'").toBe(nameOf(o.tName, ts, nn));
    if (o.tPrice !== undefined) expect.soft(row?.price, "dòng mới: 'Giá' (so giá trị số)").toBe(o.tPrice);
  } else if (o?.kind === 'edit') {
    const m = mAfter?.body;
    if (o.name !== undefined) expect.soft(m?.name, 'M_SAU name').toBe(nameOf(o.name, ts, nn));
    if (o.price !== undefined) expect.soft(sameNumber(m?.price, o.price), `M_SAU price = ${o.price} (so giá trị số), thấy ${JSON.stringify(m?.price)}`).toBe(true);
    if (o.cat !== undefined) expect.soft(sameNumber(m?.category_id, o.cat), `M_SAU category_id = ${o.cat}`).toBe(true);
    for (const k of o.keep ?? []) {
      const key = k === 'cat' ? 'category_id' : k;
      expect.soft(String(m?.[key]), `M_SAU ${key} = M_TRƯỚC`).toBe(String(mBefore?.[key]));
    }
    expect.soft(after.length, 'số bản ghi SAU = TRƯỚC').toBe(before.length);
    const row = tAfter[mRowIdx];
    if (o.tName !== undefined) expect.soft(row?.name, "dòng của M: 'Tên SP'").toBe(nameOf(o.tName, ts, nn));
    if (o.tPrice !== undefined) expect.soft(row?.price, "dòng của M: 'Giá' (so giá trị số)").toBe(o.tPrice);
    if (o.othersSame) {
      expect.soft(tAfter.length, 'số dòng không đổi').toBe(tBefore.length);
      expect.soft(tAfter.filter((_, i) => i !== mRowIdx), 'mọi dòng khác SAU_UI = TRƯỚC_UI').toEqual(tBefore.filter((_, i) => i !== mRowIdx));
    }
  } else if (o?.kind === 'del') {
    expect.soft(tAfter.some(x => x.name === M!.body.name), `bảng không còn dòng '${M!.body.name}'`).toBe(false);
    expect.soft(tAfter.length, 'số dòng SAU_UI = TRƯỚC_UI − 1').toBe(tBefore.length - 1);
    expect.soft(after.some(p => p.id === M!.id), 'GET /api/products SAU không còn id M').toBe(false);
    expect.soft(after.length, 'số bản ghi SAU = TRƯỚC − 1').toBe(before.length - 1);
  } else if (o?.kind === 'view') {
    expect.soft(tBefore.length, 'số dòng = số bản ghi').toBe(before.length);
    for (const p of before) {
      const rows = tBefore.filter(x => x.name === String(p.name));
      expect.soft(rows.length, `đúng 1 dòng cho '${p.name}'`).toBe(1);
      expect.soft(sameNumber(rows[0]?.price, Number(p.price)), `'Giá' của '${p.name}' = ${p.price} (so giá trị số), thấy ${rows[0]?.priceText}`).toBe(true);
    }
  } else {
    // ---- case SV (TS-SV-UI) ----
    switch (c.id) {
      case 'TC-FR15-200':
        expect.soft(errShown, 'báo lỗi (C7, C16, C21)').toBe(true);
        expect.soft(r.dialogs.filter(d => d.trim() === '1'), 'không kích hoạt alert XSS (không có hộp thoại "1")').toEqual([]);
        break;
      case 'TC-FR15-201':
        expect.soft(sameList(after, before), 'form chặn: dữ liệu SAU = TRƯỚC (C24)').toBe(true);
        break;
      case 'TC-FR15-202': {
        expect.soft(after.length, 'thêm thành công: số bản ghi + 1').toBe(before.length + 1);
        expect.soft(sameNumber(added[0]?.price, 7000000) && typeof added[0]?.price === 'number', `CSDL lưu giá trị số 7000000, thấy ${JSON.stringify(added[0]?.price)}`).toBe(true);
        const row = tAdded[0];
        expect.soft(row?.price, "bảng: 'Giá' = 7000000 (giá trị)").toBe(7000000);
        expect.soft(/^7[.,]000[.,]000\s*₫$/.test(row?.priceText ?? ''), `bảng hiển thị 7.000.000 ₫ (C17), thấy '${row?.priceText}'`).toBe(true);
        break;
      }
      case 'TC-FR15-205': {
        expect.soft(priceValue === '' || errShown, 'ô chặn nhập/dán (value rỗng) hoặc có thông báo lỗi').toBe(true);
        expect.soft(sameList(after, before), 'không lưu rác vào CSDL: SAU = TRƯỚC').toBe(true);
        break;
      }
      case 'TC-FR15-206': {
        const f = JSON.parse(formShowsSp2 ?? '{}');
        expect.soft([f.name, String(f.price), String(f.cat)], 'form cập nhật đúng dữ liệu của SP2')
          .toEqual([m2Before?.name, String(m2Before?.price), String(m2Before?.category_id)]);
        const m1 = (await getProduct(request, M!.id)).body, m2 = (await getProduct(request, M2!.id)).body;
        expect.soft(m1, 'SP1 hoàn toàn giữ nguyên').toEqual(mBefore);
        expect.soft([m2?.name, Number(m2?.price), Number(m2?.category_id)], 'SP2 được cập nhật')
          .toEqual([fill(inp['Tên sản phẩm'], ts, nn), Number(inp['Giá']), CATEGORY[inp['Danh mục']]]);
        expect.soft(after.filter(p => p.id !== M2!.id), 'chỉ SP2 bị thay đổi').toEqual(before.filter(p => p.id !== M2!.id));
        break;
      }
      default: throw new Error(`${c.id}: chưa có oracle`);
    }
  }
}

// =============================== API ===============================
const KEYS: [string, string][] = [['Tên sản phẩm', 'name'], ['Giá', 'price'], ['Danh mục', 'category_id'], ['Mô tả', 'description'], ['URL Ảnh', 'imageUrl']];
/** Body thô theo procedure bước 4: "…" chuỗi JSON, số/null thô, '— thiếu —' bỏ khoá, "x" × n chuỗi lặp, 'Infinity (gửi thô)' token thô. */
function rawBody(inp: any, ts: string, nn: string, extra: string[] = []) {
  const parts: string[] = [];
  for (const [col, key] of KEYS) {
    const v = inp[col];
    if (v === undefined || v === '— thiếu —' || v === '—') continue;
    const rep = repeatOf(v);
    const tok = rep !== null ? JSON.stringify(rep) : v.replace(/\s*\(gửi thô\)$/, '');
    parts.push(`${JSON.stringify(key)}: ${fill(tok, ts, nn)}`);
  }
  return `{${[...parts, ...extra].join(', ')}}`;
}

async function runApi(c: any, page: Page, request: APIRequestContext, env: Env, info: TestInfo) {
  checkHash(c);
  const nn = nnOf(c.id), ts = env.ts, inp = c.inputs;
  const method = inp['Thao tác CRUD'] as string, tokCol = inp['Danh tính người gọi / token'] as string, tgt = inp['Sản phẩm mục tiêu (khi Xem chi tiết / Sửa / Xóa)'] as string;
  const obs: string[] = [];
  let M: { id: number; body: any } | undefined;
  let U = '';
  try {
    if (tgt === 'M') M = await createM(request, env.ta, ts, nn);
    if (tokCol === 'U') U = await login(request, USER);
  } catch (e) {
    if (e instanceof SetupError) return finish(info, [], { v: 'Blocked', why: e.message });
    throw e;
  }
  const before = (await listProducts(request)).list;
  const mBefore = M ? (await getProduct(request, M.id)).body : null;
  let id: number | null = null;
  if (tgt === 'M') id = M!.id;
  else if (/^\d+/.test(tgt)) {
    id = Number(/^\d+/.exec(tgt)![0]);
    if (/không tồn tại/.test(tgt) && before.some(p => p.id === id)) {
      id = Math.max(...before.map(p => p.id)) + 1000;
      obs.push(`ghi chú: id 999999 có trong TRƯỚC → dùng id ${id}`);
    }
  }
  const url = `${API}/api/products${id !== null ? `/${id}` : ''}`;
  const headers: Record<string, string> = { 'Content-Type': c.id === 'TC-FR15-211' ? 'text/plain' : 'application/json' };
  if (tokCol === 'TA') headers.Authorization = `Bearer ${env.ta}`;
  else if (tokCol === 'U') headers.Authorization = `Bearer ${U}`;
  else if (tokCol === 'sai') headers.Authorization = BAD_TOKEN;
  const hasBody = method === 'POST' || method === 'PUT';
  const extra = c.id === 'TC-FR15-213' ? ['"id": 1', '"role": "admin"'] : [];
  const body = hasBody ? rawBody(inp, ts, nn, extra) : undefined;

  const res = await request.fetch(url, { method, headers, data: body !== undefined ? Buffer.from(body, 'utf8') : undefined });
  const status = res.status(), text = await res.text();
  let json: any = null;
  try { json = JSON.parse(text); } catch { /* không phải JSON */ }
  const shownHeaders = { ...headers, ...(headers.Authorization && headers.Authorization !== BAD_TOKEN ? { Authorization: 'Bearer <token>' } : {}) };
  await attachJson(info, `${c.id}_req`, { method, url: url.replace(API, ''), headers: shownHeaders, body: body ?? null });
  await attachJson(info, `${c.id}_res`, { status, contentType: res.headers()['content-type'] ?? '', body: text });
  await renderResponse(page, info, c.id, `${method} ${url.replace(API, '')}\n${body ?? ''}\n\nHTTP ${status}\n${text}`);

  const after = (await listProducts(request)).list;
  const mAfter = M ? (await getProduct(request, M.id)) : null;
  const added = after.filter(p => !before.some(b => b.id === p.id));
  obs.push(`HTTP ${status} ${text.slice(0, 200)}`);
  obs.push(`bản ghi TRƯỚC → SAU: ${before.length} → ${after.length}`);
  if (added.length) obs.push(`bản ghi mới: ${added.map(fmt).join(', ')}`);
  if (M) obs.push(`M_TRƯỚC ${fmt(mBefore)} → M_SAU ${mAfter?.body && mAfter.body.id ? fmt(mAfter.body) : `HTTP ${mAfter?.status} ${mAfter?.text.slice(0, 80)}`}`);
  finish(info, obs);

  const hasError = json !== null && typeof json === 'object' && 'error' in json;
  const o: Oracle | undefined = ORACLE[c.id];
  if (o?.kind === 'reject') {
    expect.soft(is4xx(status), `HTTP 4xx (không 2xx, không 5xx), nhận ${status}`).toBe(true);
    if (o.error) expect.soft(hasError, 'body có trường error').toBe(true);
    expect.soft(sameList(after, before), 'GET /api/products SAU = TRƯỚC').toBe(true);
    if (o.mSame) expect.soft(mAfter?.body, 'M_SAU = M_TRƯỚC').toEqual(mBefore);
    if (o.mStill) expect.soft(after.some(p => p.id === M!.id), 'SAU vẫn có id M').toBe(true);
  } else if (o?.kind === 'add') {
    expect.soft(is2xx(status), `HTTP 2xx, nhận ${status}`).toBe(true);
    expect.soft(after.length, 'số bản ghi SAU = TRƯỚC + 1').toBe(before.length + 1);
    const n = added[0];
    if (o.name !== undefined) expect.soft(n?.name, 'name bản ghi mới').toBe(nameOf(o.name, ts, nn));
    if (o.price !== undefined) expect.soft(sameNumber(n?.price, o.price), `price = ${o.price} (so giá trị số), thấy ${JSON.stringify(n?.price)}`).toBe(true);
    if (o.cat !== undefined) expect.soft(sameNumber(n?.category_id, o.cat), `category_id = ${o.cat}`).toBe(true);
  } else if (o?.kind === 'edit') {
    expect.soft(is2xx(status), `HTTP 2xx, nhận ${status}`).toBe(true);
    const m = mAfter?.body;
    if (o.name !== undefined) expect.soft(m?.name, 'M_SAU name').toBe(nameOf(o.name, ts, nn));
    if (o.price !== undefined) expect.soft(sameNumber(m?.price, o.price), `M_SAU price = ${o.price} (so giá trị số), thấy ${JSON.stringify(m?.price)}`).toBe(true);
    if (o.cat !== undefined) expect.soft(sameNumber(m?.category_id, o.cat), `M_SAU category_id = ${o.cat}`).toBe(true);
    expect.soft(after.length, 'số bản ghi SAU = TRƯỚC').toBe(before.length);
    if (o.othersSame) expect.soft(after.filter(p => p.id !== M!.id), 'mọi bản ghi id ≠ M: SAU = TRƯỚC').toEqual(before.filter(p => p.id !== M!.id));
  } else if (o?.kind === 'del') {
    expect.soft(is2xx(status), `HTTP 2xx, nhận ${status}`).toBe(true);
    expect.soft(after.some(p => p.id === M!.id), 'SAU không còn id M').toBe(false);
    expect.soft(after.length, 'số bản ghi SAU = TRƯỚC − 1').toBe(before.length - 1);
  } else if (o?.kind === 'get') {
    expect.soft(is2xx(status), `HTTP 2xx, nhận ${status}`).toBe(true);
    expect.soft(json?.id, 'bản ghi id 2').toBe(2);
    expect.soft(json?.name, 'name').toBe(o.name);
    expect.soft(sameNumber(json?.category_id, o.cat!), `category_id = ${o.cat}`).toBe(true);
    expect.soft(typeof json?.price, 'price là số JSON (C15)').toBe('number');
    expect.soft(sameNumber(json?.price, o.price!), `price = ${o.price}`).toBe(true);
  } else {
    // ---- case SV (TS-SV-API) ----
    const same = sameList(after, before);
    switch (c.id) {
      case 'TC-FR15-207': {
        expect.soft(is2xx(status), `HTTP 2xx, nhận ${status}`).toBe(true);
        expect.soft(added[0]?.name, 'tên lưu nguyên văn').toBe(JSON.parse(fill(inp['Tên sản phẩm'], ts, nn)));
        const all = await listProducts(request);
        expect.soft(all.status === 200 && before.every(b => all.list.some(p => p.id === b.id)), 'bảng products nguyên vẹn (GET 200, mọi id TRƯỚC còn)').toBe(true);
        break;
      }
      case 'TC-FR15-208': case 'TC-FR15-214':
        expect.soft(is4xx(status), `HTTP 4xx, nhận ${status}`).toBe(true);
        expect.soft(hasError, 'body có trường error').toBe(true);
        expect.soft(same, 'CSDL không đổi').toBe(true);
        break;
      case 'TC-FR15-209':
        expect.soft(is4xx(status), `HTTP 4xx, nhận ${status}`).toBe(true);
        expect.soft(hasError, 'body là JSON có trường error (không phải trang HTML) (C20)').toBe(true);
        expect.soft(same, 'CSDL không đổi').toBe(true);
        break;
      case 'TC-FR15-211':
        expect.soft(status === 400 || status === 415, `HTTP 4xx (400 hoặc 415), nhận ${status}`).toBe(true);
        expect.soft(added, 'không tạo sản phẩm').toEqual([]);
        break;
      case 'TC-FR15-213': {
        const m = mAfter?.body;
        expect.soft(m?.id, 'id sản phẩm M không đổi (M vẫn ở id M)').toBe(M!.id);
        const want = JSON.parse(rawBody(inp, ts, nn));
        if (is2xx(status)) expect.soft([m?.name, Number(m?.price), Number(m?.category_id)], '(a) 2xx: các trường hợp lệ được cập nhật')
          .toEqual([want.name, Number(want.price), Number(want.category_id)]);
        else if (is4xx(status)) expect.soft(m, '(b) 4xx: bản ghi không đổi').toEqual(mBefore);
        else expect.soft(status, 'HTTP 2xx hoặc 4xx').toBe('2xx|4xx');
        break;
      }
      default: throw new Error(`${c.id}: chưa có oracle`);
    }
  }
}

// =============================== Đăng ký test ===============================
let runStart = 0;
let runStartIds = new Set<number>();
test.beforeAll(async ({ request }) => {
  runStart = Date.now();
  runStartIds = new Set((await listProducts(request)).list.map(p => p.id));
});
test.afterAll(async ({ request }) => {
  const left = await sweep(request, runStartIds, runStart);
  if (left.length) console.warn(`[C_FR15] Quét cuối không xoá được: ${left.join(', ')} — khởi động lại backend trước lượt sau.`);
});

for (const s of data.suites) {
  if (MANUAL.has(s.id)) continue;
  test.describe(s.id, () => {
    for (const c of s.cases) {
      test(`${c.id} ${c.title}`, async ({ page, request, env }, info) => {
        if (c.layer === 'UI') await runUi(c, page, request, env, info);
        else await runApi(c, page, request, env, info);
      });
    }
  });
}
