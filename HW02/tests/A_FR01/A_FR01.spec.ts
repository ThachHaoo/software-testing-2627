/**
 * FR-01 Đăng ký tài khoản — chạy toàn bộ test case trong HW02/A_FR01/testcases.json.
 * Mỗi suite một describe; tiêu đề test = "<mã TC> <tiêu đề>" để merge_results.py gộp được.
 * Assertion lấy từ expected_result (oracleOf trong lib.ts), không chỉnh theo hành vi SUT.
 * Chạy (PowerShell, trong HW02/tests): $env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/A_FR01.json"; npx playwright test A_FR01
 */
import { Browser, Page, TestInfo, APIRequestContext } from '@playwright/test';
import {
  test, expect, suites, COL, SEED_USER, WEB, API, ADMIN_WEB, materialize, sub, oracleOf, diffUsers,
  shot, attachJson, renderResponse, field, errorBox, submitBtn, validation, Oracle, User,
} from './lib';

// Tên form lấy từ procedure TS-DOM-UI bước 2 ("Form 'Đăng Ký Tài Khoản' hiển thị…").
const FORM_TITLE = /Form '(.+?)'/.exec(suites['TS-DOM-UI'].procedure[1].expected)![1];

type Ctx = { browser: Browser; request: APIRequestContext; page?: Page; admin: { token: string; before: User[]; list: () => Promise<User[]> } };

const V5_INVALID = ['EC40', 'EC41', 'EC42'];
const covers = (c: any): string[] => (Array.isArray(c.covers) ? c.covers : String(c.covers || '').split(','));

/** Kết thúc case: ghi verdict (nếu có) + actual (lý do + quan sát). */
function finish(info: TestInfo, obs: string[], v?: { verdict: 'Blocked' | 'Not run'; why: string }) {
  if (v) info.annotations.push({ type: 'verdict', description: v.verdict });
  info.annotations.push({ type: 'actual', description: (v ? `${v.verdict}: ${v.why} | ` : '') + obs.join('; ') });
}

function checkNewUser(o: Oracle, u: User | undefined, name: unknown) {
  if (!u) return;
  if (o.name !== undefined) expect.soft(u.name, 'name của user mới').toBe(o.name);
  else if (o.nameFromInput) expect.soft(u.name, 'Họ Tên lưu nguyên văn').toBe(name);
  if (o.email !== undefined) expect.soft(u.email, 'email của user mới').toBe(o.email);
  if (o.role !== undefined) expect.soft(u.role, 'role của user mới').toBe(o.role);
}

function checkSeed(d: ReturnType<typeof diffUsers>) {
  expect.soft(d.removed.map(u => u.email), 'không user nào có sẵn bị xoá').toEqual([]);
  expect.soft(d.changed.map(u => u.email), 'user có sẵn không bị sửa name/email/role').toEqual([]);
}

async function uiLogin(page: Page, email: string, password: string) {
  await page.goto(`${WEB}/login`);
  await field(page, 'Username').pressSequentially(email);
  await field(page, 'Mật khẩu').pressSequentially(password);
  const resp = page.waitForResponse(r => r.url().endsWith('/api/login'), { timeout: 5000 }).catch(() => null);
  await page.getByRole('button', { name: 'Sign In' }).click();
  const r = await resp;
  await page.waitForTimeout(500);
  return { status: r?.status() ?? 0, token: await page.evaluate(() => localStorage.getItem('token')) };
}

// =============================== UI ===============================
async function runUi(c: any, { browser, admin }: Ctx, info: TestInfo) {
  test.setTimeout(90_000);
  const ts = String(Date.now());
  const inp = c.inputs;
  const name = materialize(inp[COL.name], ts);
  const email = materialize(inp[COL.email], ts);
  const pwd = materialize(inp[COL.pwd], ts);
  const conf = COL.conf in inp ? materialize(inp[COL.conf], ts) : pwd;   // TS-SV: Xác nhận = Mật khẩu
  const extra: string = inp[COL.extra] || '';
  const double = /2 lần/.test(extra);
  const toAdmin = /Quản lý Người dùng/.test(extra);
  const preLogin = /Đăng nhập bằng test@eshop\.com trước/.test(extra);
  const o = double ? null : oracleOf(c, ts);
  const obs: string[] = [];
  let v: { verdict: 'Blocked' | 'Not run'; why: string } | undefined;

  const ctx = await browser.newContext();           // context mới mỗi case: không token, không autofill
  const page = await ctx.newPage();
  const posts: string[] = [];
  page.on('request', r => { if (r.method() === 'POST' && r.url().endsWith('/api/register')) posts.push(r.postData() || ''); });
  const dialogs: string[] = [];
  page.on('dialog', d => { dialogs.push(d.message()); d.dismiss().catch(() => {}); });
  try {
    if (preLogin) {
      const l = await uiLogin(page, SEED_USER.email, SEED_USER.password);
      obs.push(`đăng nhập trước bằng ${SEED_USER.email}: HTTP ${l.status}, token ${l.token ? 'có' : 'không'}`);
      if (!l.token) { v = { verdict: 'Blocked', why: `không đăng nhập được ${SEED_USER.email} ở bước chuẩn bị (A20)` }; await shot(page, info, c.id); return; }
    }
    // Bước 2: mở /register → các ô trống
    await page.goto(`${WEB}/register`);
    await expect(page.getByRole('heading', { name: FORM_TITLE })).toBeVisible();
    const hasConf = (await field(page, COL.conf).count()) > 0;
    const fields: [string, unknown][] = [[COL.name, name], [COL.email, email], [COL.pwd, pwd]];
    if (hasConf) fields.push([COL.conf, conf]);
    for (const [label] of fields) expect.soft(await field(page, label).inputValue(), `ô '${label}' trống lúc đầu`).toBe('');

    if (!hasConf && covers(c).some(e => V5_INVALID.includes(e.trim()))) {
      v = { verdict: 'Blocked', why: 'form không có ô Xác nhận mật khẩu — case gây chặn TC-FR01-94 (A17)' };
      await shot(page, info, c.id);
      return;
    }
    if (!hasConf) obs.push('form không có ô Xác nhận mật khẩu: bỏ qua bước nhập V5 (A17)');

    // Bước 3: gõ đúng chuỗi; rỗng = không gõ; ␣ = đúng số dấu cách
    for (const [label, val] of fields) if (val !== undefined && val !== '') await field(page, label).pressSequentially(String(val));
    for (const [label, val] of fields) expect.soft(await field(page, label).inputValue(), `ô '${label}' hiển thị đúng giá trị đã gõ`).toBe(String(val ?? ''));

    // Bước 4: bấm 'Đăng Ký' đúng một lần (SV-09: hai lần liên tiếp theo cột Thao tác riêng)
    const respP = page.waitForResponse(r => r.url().endsWith('/api/register'), { timeout: 4000 }).catch(() => null);
    if (double) await submitBtn(page).evaluate((b: HTMLButtonElement) => { b.click(); b.click(); });
    else await submitBtn(page).click();
    const resp = await respP;
    await page.waitForTimeout(double ? 2500 : 800);

    // Bước 5: quan sát hộp lỗi / bong bóng HTML5 / URL
    const url = new URL(page.url()).pathname;
    const box = (await errorBox(page).count()) ? (await errorBox(page).first().innerText()).trim() : '';
    const vals: Record<string, { invalid: boolean; msg: string } | null> = {};
    for (const [label] of fields) vals[label] = url === '/register' ? await validation(page, label) : null;
    obs.push(`URL=${url}`, `POST /api/register gửi ${posts.length} lần${resp ? ` (HTTP ${resp.status()})` : ''}`, `hộp lỗi=${box ? JSON.stringify(box) : 'không có'}`);
    for (const [label, val] of Object.entries(vals)) if (val?.msg) obs.push(`validationMessage[${label}]=${JSON.stringify(val.msg)}`);
    await shot(page, info, c.id);

    // Bước 6: CSDL so với bước 1
    const d = diffUsers(admin.before, await admin.list());
    obs.push(`user mới=${d.added.length}${d.added.map(u => ` [${u.email} | ${u.name} | ${u.role}]`).join('')}`);

    // ---- A20: không kiểm được đúng mục đích ----
    if (double && posts.length === 0) { v = { verdict: 'Blocked', why: 'form không gửi request nào nên không kiểm được việc bấm 2 lần (A20)' }; return; }
    if (o?.hint && box && !o.hint.test(box)) { v = { verdict: 'Blocked', why: `thông báo lỗi nói về trường khác, không kiểm được mục đích của case (A20) — SV ghi mã case/bug gây chặn` }; return; }
    if (toAdmin && d.added.length !== 1) { v = { verdict: 'Blocked', why: 'đăng ký qua UI không thành công nên không kiểm được phần hiển thị (A20) — SV ghi mã case/bug gây chặn' }; return; }

    if (double) {                                   // SV-09: "chỉ tạo đúng 1 tài khoản"
      expect.soft(d.added.length, 'chỉ tạo đúng 1 tài khoản').toBe(1);
      return;
    }
    if (o!.kind === 'success') {
      expect.soft(box, 'không có thông báo lỗi').toBe('');
      expect.soft(url, 'chuyển tới /login (FR-01.10)').toBe('/login');
      expect.soft(d.added.length, 'đúng 1 user mới so với bước 1').toBe(1);
      checkNewUser(o!, d.added[0], name);
    } else {
      const target = o!.field;
      const html5 = posts.length === 0 && (target ? !!vals[target]?.msg : Object.values(vals).some(x => !!x?.msg));
      expect.soft(!!box || html5, `có thông báo lỗi trên form (hộp lỗi đỏ, hoặc A16: không gửi request và ô ${target ? `'${target}'` : 'liên quan'} có validationMessage)`).toBe(true);
      expect.soft(url, 'vẫn ở /register').toBe('/register');
      expect.soft(d.added.length, 'không có user mới so với bước 1').toBe(0);
    }
    if (o!.seedKept || o!.kind === 'reject') checkSeed(d);
    for (const m of o!.manual) obs.push(`[kiểm tay] ${m}`);

    // ---- Thao tác riêng sau khi đăng ký ----
    if (o!.login) {
      if (d.added.length === 1) {
        const l = await uiLogin(page, String(email), String(pwd));
        obs.push(`đăng nhập lại: HTTP ${l.status}, token ${l.token ? 'có' : 'không'}`);
        expect.soft(l.token, 'đăng nhập lại bằng đúng mật khẩu đã đăng ký thành công').toBeTruthy();
        await shot(page, info, `${c.id}_login`, 'sau đăng nhập');
      } else obs.push('không đăng nhập lại vì đăng ký không tạo user');
    }
    if (toAdmin) {
      const actx = await browser.newContext();
      await actx.addInitScript(t => localStorage.setItem('adminToken', t), admin.token);
      const ap = await actx.newPage();
      const adialogs: string[] = [];
      ap.on('dialog', dl => { adialogs.push(dl.message()); dl.dismiss().catch(() => {}); });
      await ap.goto(ADMIN_WEB);
      await ap.getByText('Người dùng', { exact: true }).click();
      await expect(ap.getByRole('heading', { name: 'Quản lý Người dùng' })).toBeVisible();
      await ap.waitForTimeout(800);
      const shown = await ap.getByText(String(name), { exact: false }).count();
      obs.push(`trang Quản lý Người dùng: Họ Tên hiện dạng chữ ${shown} lần; dialog=${JSON.stringify(adialogs)}`);
      await shot(ap, info, `${c.id}_admin`, 'trang Quản lý Người dùng');
      await actx.close();
      expect.soft(adialogs, 'không chạy script (không có dialog)').toEqual([]);
      // Expected "hiển thị chuỗi dạng chữ": nếu trang không hiển thị Họ Tên thì không kiểm tự động được → SV kiểm tay.
      if (shown === 0 && adialogs.length === 0) v = { verdict: 'Not run', why: 'trang Quản lý Người dùng không hiển thị Họ Tên nên không kiểm tự động được expected — SV kiểm tay' };
    }
  } finally {
    if (dialogs.length) obs.push(`dialog trên web=${JSON.stringify(dialogs)}`);
    finish(info, obs, v);
    await ctx.close();
  }
}

// =============================== API ===============================
async function runApi(c: any, { request, page, admin }: Ctx, info: TestInfo) {
  test.setTimeout(60_000);
  const ts = String(Date.now());
  const inp = c.inputs;
  const extra: string = inp[COL.extra] || '';
  const body: Record<string, unknown> = {};
  for (const [k, col] of [['name', COL.name], ['email', COL.email], ['password', COL.pwd]] as const) {
    const val = materialize(inp[col], ts);
    if (val !== undefined) body[k] = val;
  }
  const extraField = /`"(\w+)":\s*"([^"]*)"`/.exec(extra);       // SV-23: body thêm trường
  if (extraField) body[extraField[1]] = extraField[2];
  const textPlain = /text\/plain/.test(extra);                    // SV-15
  const parallel = /đồng thời/.test(extra);                       // SV-10
  const headers = { 'Content-Type': textPlain ? 'text/plain' : 'application/json' };
  const o = parallel ? null : oracleOf(c, ts);
  const obs: string[] = [];

  const send = () => request.post(`${API}/api/register`, { headers, data: textPlain ? JSON.stringify(body) : body });
  const raw = parallel ? await Promise.all([send(), send()]) : [await send()];
  const res = await Promise.all(raw.map(async r => {
    const text = await r.text();
    let json: any = null;
    try { json = JSON.parse(text); } catch { /* không phải JSON */ }
    return { status: r.status(), text, json };
  }));
  const shortBody = (b: Record<string, unknown>) => Object.fromEntries(Object.entries(b).map(([k, x]) => [k, typeof x === 'string' && x.length > 200 ? `${x.slice(0, 40)}… (${x.length} ký tự)` : x]));
  await attachJson(info, `${c.id}_request`, { method: 'POST', url: '/api/register', headers, count: raw.length, body: shortBody(body) });
  await attachJson(info, `${c.id}_response`, res.map(r => ({ status: r.status, body: r.json ?? r.text })));
  for (const r of res) obs.push(`HTTP ${r.status} ${r.text.slice(0, 160)}`);

  let login: { status: number; token?: string } | undefined;
  if (o?.login) {
    const lr = await request.post(`${API}/api/login`, { data: { email: body.email, password: body.password } });
    const lj = await lr.json().catch(() => ({}));
    login = { status: lr.status(), token: lj.token };
    obs.push(`đăng nhập lại: HTTP ${login.status}, token ${login.token ? 'có' : 'không'}`);
  }
  const d = diffUsers(admin.before, await admin.list());
  obs.push(`user mới=${d.added.length}${d.added.map(u => ` [${u.email} | ${String(u.name).slice(0, 60)} | ${u.role}]`).join('')}`);
  await renderResponse(page!, info, c.id, res.map(r => `HTTP ${r.status}\n${r.text.slice(0, 2000)}`).join('\n\n') + `\n\nuser mới so với bước 1: ${d.added.length}`);
  info.annotations.push({ type: 'actual', description: obs.join('; ') });

  if (parallel) {                                   // SV-10: "đúng 1 request thành công, request còn lại 4xx"
    expect.soft(res.filter(r => r.status === 200).length, 'đúng 1 request thành công').toBe(1);
    expect.soft(res.filter(r => r.status >= 400 && r.status < 500).length, 'request còn lại 4xx').toBe(1);
    expect.soft(d.added.length, 'chỉ 1 user mới').toBe(1);
    return;
  }
  const r = res[0];
  if (o!.kind === 'success') {
    expect.soft(r.status, 'HTTP 200').toBe(200);
    if (o!.apiBody) {
      expect.soft(r.json?.message, 'body.message').toBe('User registered successfully');
      expect.soft(typeof r.json?.id, 'body.id là số').toBe('number');
    }
    expect.soft(d.added.length, 'đúng 1 user mới so với bước 1').toBe(1);
    checkNewUser(o!, d.added[0], body.name);
    if (o!.login) {
      expect.soft(login?.status, 'đăng nhập lại HTTP 200').toBe(200);
      expect.soft(login?.token, 'có token').toBeTruthy();
    }
  } else {
    expect.soft(r.status >= 400 && r.status < 500, `HTTP 4xx (nhận ${r.status})`).toBe(true);
    expect.soft(r.json && typeof r.json === 'object' && 'error' in r.json, 'body JSON có trường error').toBe(true);
    expect.soft(d.added.length, 'không có user mới so với bước 1').toBe(0);
  }
  if (o!.seedKept || o!.kind === 'reject') checkSeed(d);
}

// =============================== GUI (step-by-step) ===============================
async function runGui(c: any, { browser, admin }: Ctx, info: TestInfo) {
  const ts = String(Date.now());
  const obs: string[] = [];
  let v: { verdict: 'Blocked' | 'Not run'; why: string } | undefined;
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  const steps = c.steps.map((s: any) => ({ action: sub(s.action, ts), expected: sub(s.expected, ts) }));
  const quoted = (s: string) => [...s.matchAll(/'([^']+)'/g)].map(m => m[1]);
  const label = (l: string) => page.locator(`xpath=//label[starts-with(normalize-space(.), "${l}")]`);
  try {
    await page.goto(`${WEB}/register`);                           // bước 1
    await expect(page.getByRole('heading', { name: quoted(steps[0].expected)[0] })).toBeVisible();
    const req = c.requirements[0];
    if (req === 'FR-22.1') {
      for (const l of quoted(c.test_data)) {
        const t = (await label(l).count()) ? (await label(l).first().innerText()).trim() : '(không có nhãn)';
        obs.push(`nhãn ${l}: ${JSON.stringify(t)}`);
        expect.soft(t, `nhãn '${l}' có '*'`).toContain('*');
      }
      if (await label(COL.conf).count()) obs.push(`[ghi nhận, không kết luận] nhãn ${COL.conf}: ${JSON.stringify((await label(COL.conf).first().innerText()).trim())}`);
    } else if (req === 'FR-22.2' || req === 'FR-22.3') {
      const l = req === 'FR-22.2' ? COL.email : COL.pwd;
      const want = /type là "(\w+)"/.exec(steps[1].expected)![1];
      const type = await field(page, l).getAttribute('type');
      obs.push(`type của ô ${l}=${JSON.stringify(type)}`);
      expect.soft(type, `ô '${l}' có type="${want}"`).toBe(want);
      if (req === 'FR-22.3') {
        const typed = quoted(steps[2].action)[0];
        await field(page, l).pressSequentially(typed);
        // "Ô hiển thị ký tự che": trình duyệt che ký tự khi type="password" — kiểm qua thuộc tính + ảnh chụp, không đo pixel.
        obs.push('che ký tự: xem ảnh chụp');
        if (await field(page, COL.conf).count()) obs.push(`[ghi nhận, theo notes] type của ô ${COL.conf}=${JSON.stringify(await field(page, COL.conf).getAttribute('type'))}`);
      }
    } else if (req === 'FR-22.4') {
      const [n, e, p, cf] = quoted(steps[1].action);
      await field(page, COL.name).pressSequentially(n);
      await field(page, COL.email).pressSequentially(e);
      await field(page, COL.pwd).pressSequentially(p);
      if (await field(page, COL.conf).count()) await field(page, COL.conf).pressSequentially(cf);
      else obs.push('form không có ô Xác nhận mật khẩu: bỏ qua giá trị của ô này (xem TC-FR01-94)');
      await submitBtn(page).click();
      await page.waitForTimeout(800);
      const has = (await errorBox(page).count()) > 0;
      obs.push(`hộp lỗi=${has ? JSON.stringify((await errorBox(page).first().innerText()).trim()) : 'không có'}`);
      if (!has) v = { verdict: 'Blocked', why: 'không có hộp lỗi trong DOM nên không đo được vị trí (A20)' };
      else {
        const b = (await errorBox(page).first().boundingBox())!;
        const s = (await submitBtn(page).boundingBox())!;
        obs.push(`hộp lỗi y+height=${Math.round(b.y + b.height)}, nút 'Đăng Ký' y=${Math.round(s.y)}`);
        expect.soft(b.y + b.height <= s.y, 'thông báo lỗi nằm phía trên nút Đăng Ký').toBe(true);
      }
    } else if (req === 'FR-01.9') {
      const n = await field(page, COL.conf).count();
      obs.push(`số ô '${COL.conf}'=${n}`);
      expect.soft(n, `có đúng 1 ô '${COL.conf}'`).toBe(1);
      if (n === 1) {
        const yc = (await field(page, COL.conf).boundingBox())!.y, yp = (await field(page, COL.pwd).boundingBox())!.y;
        expect.soft(yc > yp, `ô '${COL.conf}' nằm sau ô '${COL.pwd}'`).toBe(true);
      }
    } else throw new Error(`${c.id}: chưa có cách chạy cho yêu cầu ${req}`);
    await shot(page, info, c.id);
  } finally {
    finish(info, obs, v);
    await ctx.close();
  }
}

// =============================== Đăng ký test ===============================
// Test API dùng fixture `page` (chỉ để render ảnh response); test UI/GUI tự mở context mới, không lấy `page`
// để Playwright không đính kèm ảnh trang trắng khi case fail (config screenshot: 'only-on-failure').
for (const sid of ['TS-DOM-UI', 'TS-DOM-API', 'TS-BVA-UI', 'TS-BVA-API', 'TS-GUI', 'TS-SV']) {
  const s = suites[sid];
  test.describe(`${sid} ${s.name}`, () => {
    for (const c of s.cases) {
      const title = `${c.id} ${c.title}`;
      if (sid === 'TS-GUI') test(title, async ({ browser, request, admin }, info) => runGui(c, { browser, request, admin }, info));
      else if (c.layer === 'API') test(title, async ({ browser, request, page, admin }, info) => runApi(c, { browser, request, page, admin }, info));
      else test(title, async ({ browser, request, admin }, info) => runUi(c, { browser, request, admin }, info));
    }
  });
}
