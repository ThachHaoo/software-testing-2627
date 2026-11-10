/**
 * HW03 T1 bước 5/6e – AI chạy lại Steps SV viết trong ../bugs/BUG-58…85.md trên P1 (Chrome) / P2 (Firefox Playwright).
 * Chỉ ghi quan sát (giá trị đo được) vào ../bugs/repro/repro_<P>.json; kết luận "tái hiện được / không" ghi ở bugs/bug_check.md.
 * Chỗ Steps không nêu giá trị cụ thể → giá trị AI chọn ghi trong quan sát. Bước "(cô lập)" = ngoài Steps SV, để tách nguyên nhân.
 */
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { Page, APIRequestContext } from '@playwright/test';
import { test, expect, USER, H, byLabel, submitBtn, loginInputs, dialogs, countRequests, tabWalk, fmtSeq,
  textColors, rgb, contrast, restoreProfile, restorePassword, mainLines } from './lib';

const OUT: Record<string, Record<string, any>> = {};
let P = '';
const rec = (bug: string, k: string, v: any) => { (OUT[bug] ??= {})[k] = v; };
test.afterAll(() => {
  const dir = path.resolve(__dirname, '../bugs/repro');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `repro_${P}.json`), JSON.stringify({ project: P, run_at: new Date().toISOString(), bugs: OUT }, null, 1), 'utf-8');
});
test.beforeEach(({}, info) => { P = info.project.name; });

async function uiLogin(page: Page, pw = USER.password) {
  await page.goto('/login');
  await loginInputs(page).nth(0).fill(USER.email);
  await loginInputs(page).nth(1).fill(pw);
  await submitBtn(page).click();
  await page.waitForTimeout(1200);
}
async function toProfile(page: Page) {
  await uiLogin(page);
  await H(page).locator('a[href="/profile"]').click();
  await expect(byLabel(page, 'Họ Tên')).toBeVisible({ timeout: 5000 });
}
async function toStep2(page: Page) {
  await page.goto('/forgot-password');
  await page.locator('form input').first().fill(USER.email);
  await submitBtn(page).click();
  await expect(page.getByRole('button', { name: 'Đặt lại mật khẩu' })).toBeVisible({ timeout: 5000 });
  return /Mã OTP của bạn là:\s*(\S+)/.exec(await page.locator('body').innerText())?.[1] ?? '';
}
const activeInfo = (page: Page) => page.evaluate(() => {
  const e = document.activeElement as HTMLElement | null;
  if (!e || e === document.body) return 'body';
  const lab = e.previousElementSibling?.tagName === 'LABEL' ? (e.previousElementSibling as HTMLElement).innerText : '';
  return `${e.tagName.toLowerCase()}${lab ? ` (sau nhãn "${lab}")` : ''}${(e as any).innerText ? ` "${(e as any).innerText}"` : ''}`;
});
async function slow(page: Page, part: string, ms = 3000) {
  // Thay Slow 3G bằng trễ request khớp `part` (cùng cách trên P1, P2; Firefox Playwright không có throttling DevTools)
  await page.route(u => u.href.includes(part), async r => { await new Promise(res => setTimeout(res, ms)); await r.continue().catch(() => {}); });
  return `route trễ ${ms} ms cho request chứa "${part}" (thay cho Slow 3G)`;
}
const seedOrders = () => execSync(`python "${path.resolve(__dirname, 'seed_orders.py')}"`, { encoding: 'utf-8' });
let seeded = false;

test('BUG-58 Tab order Đăng nhập + Quên MK B2', async ({ page }) => {
  await page.goto('/login'); await page.waitForTimeout(500);
  rec('BUG-58', 'login: Tab từ khi tải trang', fmtSeq(await tabWalk(page, 15)));
  await toStep2(page);
  rec('BUG-58', 'quên MK B2: Tab từ đầu trang', fmtSeq(await tabWalk(page, 15)));
});

test('BUG-59 document.title', async ({ page }) => {
  const t: string[] = [];
  await page.goto('/login'); t.push(await page.title());
  await page.goto('/forgot-password'); t.push(await page.title());
  await toProfile(page); t.push(await page.title());
  rec('BUG-59', 'title /login, /forgot-password, /profile', t);
});

test('BUG-60 html lang', async ({ page }) => {
  await page.goto('/login');
  rec('BUG-60', '<html lang>', await page.getAttribute('html', 'lang'));
});

test('BUG-61 số thẻ h1', async ({ page }) => {
  const r: Record<string, number> = {};
  await page.goto('/login'); r['/login'] = await page.locator('h1').count();
  await page.goto('/forgot-password'); r['/forgot-password'] = await page.locator('h1').count();
  await toProfile(page); r['/profile'] = await page.locator('h1').count();
  rec('BUG-61', "document.querySelectorAll('h1').length", r);
});

test('BUG-62 type ô Email + nhập abc', async ({ page }) => {
  for (const [p, api] of [['/login', '/api/login'], ['/forgot-password', '/api/forgot-password']] as const) {
    await page.goto(p);
    const inp = page.locator('form input').first();
    const type = await inp.getAttribute('type');
    if (p === '/login') {   // Steps SV chỉ nhập ô Email → ghi thêm trạng thái ô Mật khẩu trống
      const c0 = countRequests(page, api);
      await inp.fill('abc'); await submitBtn(page).click(); await page.waitForTimeout(1000);
      rec('BUG-62', '/login đúng Steps SV (chỉ nhập abc, Mật khẩu để trống)', { request: `${c0.n} request ${api}`,
        validationMessage_o_Email: await inp.evaluate(e => (e as HTMLInputElement).validationMessage),
        validationMessage_o_MatKhau: await loginInputs(page).nth(1).evaluate(e => (e as HTMLInputElement).validationMessage) });
      await page.goto(p);
      await loginInputs(page).nth(1).fill('Test1234!');
    }
    const d = dialogs(page), c = countRequests(page, api);
    const before = await mainLines(page);
    await inp.fill('abc');
    await submitBtn(page).click();
    await page.waitForTimeout(1500);
    const msg = await inp.evaluate(e => (e as HTMLInputElement).validationMessage);
    rec('BUG-62', p === '/login' ? '/login (cô lập: có nhập Mật khẩu Test1234!)' : p, { type, request: `${c.n} request ${api}`, validationMessage: msg, hop_thoai: d.map(x => x.message),
      chu_moi: (await mainLines(page)).filter(l => !before.includes(l)) });
    page.removeAllListeners('dialog');
  }
});

test('BUG-63 nhãn + dấu *', async ({ page }) => {
  await page.goto('/login');
  rec('BUG-63', 'nhãn /login', await page.locator('form label').allInnerTexts());
  await page.goto('/forgot-password');
  rec('BUG-63', 'nhãn quên MK B1', await page.locator('form label').allInnerTexts());
  await toStep2(page);
  rec('BUG-63', 'nhãn quên MK B2', await page.locator('form label').allInnerTexts());
  await toProfile(page);
  rec('BUG-63', 'nhãn /profile', await page.locator('form label').allInnerTexts());
  rec('BUG-63', 'giá trị ban đầu Hồ sơ (sau restart)', [await byLabel(page, 'Họ Tên').inputValue(), await byLabel(page, 'Số điện thoại').inputValue(), await byLabel(page, 'Địa chỉ giao hàng').inputValue()]);
  const d = dialogs(page), put = countRequests(page, '/api/users/me');
  const res: Record<string, any> = {};
  for (const f of ['Họ Tên', 'Số điện thoại', 'Địa chỉ giao hàng']) {
    await page.reload(); await expect(byLabel(page, 'Họ Tên')).toBeVisible();
    d.length = 0; const n0 = put.n;
    const el = byLabel(page, f);
    await el.fill('');
    await submitBtn(page).click(); await page.waitForTimeout(1200);
    res[f] = { hop_thoai: d.map(x => x.message), validationMessage: await el.evaluate(e => (e as HTMLInputElement).validationMessage), request_PUT: put.n - n0 };
  }
  rec('BUG-63', 'xoá trống từng trường (các trường khác giữ nguyên) → Cập nhật', res);
  await restoreProfile(page.request);
});

test('BUG-64 vị trí thông báo lỗi', async ({ page }) => {
  const otp = await toStep2(page);
  let d = dialogs(page); let before = await mainLines(page);
  await page.locator('form input').nth(0).fill(otp);
  await page.locator('form input').nth(1).fill('123');
  await submitBtn(page).click(); await page.waitForTimeout(1200);
  rec('BUG-64', "quên MK B2: OTP đúng + mật khẩu '123'", { hop_thoai: d.map(x => x.message), chu_moi_trong_trang: (await mainLines(page)).filter(l => !before.includes(l)) });
  page.removeAllListeners('dialog');
  await toProfile(page);
  d = dialogs(page); before = await mainLines(page);
  await byLabel(page, 'Số điện thoại').fill('123');
  await submitBtn(page).click(); await page.waitForTimeout(1200);
  rec('BUG-64', "Hồ sơ: SĐT '123' → Cập nhật", { hop_thoai: d.map(x => x.message), chu_moi_trong_trang: (await mainLines(page)).filter(l => !before.includes(l)) });
  await restoreProfile(page.request);
});

test('BUG-65 bấm nhãn → focus', async ({ page }) => {
  const r: Record<string, string> = {};
  await page.goto('/login');
  for (const l of ['Username', 'Mật khẩu']) { await page.locator('label', { hasText: l }).first().click(); r[`/login "${l}"`] = await activeInfo(page); }
  await toProfile(page);
  for (const l of ['Họ Tên', 'Số điện thoại', 'Địa chỉ giao hàng']) { await page.locator('label', { hasText: l }).first().click(); r[`/profile "${l}"`] = await activeInfo(page); }
  rec('BUG-65', 'phần tử đang focus sau khi bấm nhãn', r);
});

test('BUG-66..69 Quên MK: chỉ báo bước, Quay lại đăng nhập, ô B2, OTP', async ({ page }) => {
  await page.goto('/forgot-password');
  const b1 = await page.locator('main').innerText();
  rec('BUG-66', 'B1: chữ dạng "Bước x / y" trong trang', /bước\s*\d/i.exec(b1)?.[0] ?? 'không có');
  rec('BUG-67', 'B1: link/nút trong vùng nội dung', await page.locator('main a, main button').allInnerTexts());
  rec('BUG-67', 'B1: có chữ "Quay lại đăng nhập"', b1.includes('Quay lại đăng nhập'));
  const otp = await toStep2(page);
  const b2 = await page.locator('main').innerText();
  rec('BUG-66', 'B2: chữ dạng "Bước x / y" trong trang', /bước\s*\d/i.exec(b2)?.[0] ?? 'không có');
  rec('BUG-68', 'B2: nhãn + type các ô nhập', await page.locator('form input').evaluateAll(es => es.map(e => `${(e.previousElementSibling as HTMLElement | null)?.innerText ?? '?'} [${(e as HTMLInputElement).type}]`)));
  rec('BUG-69', 'B2: dòng chứa mã OTP', /Mã OTP của bạn là:.*/.exec(b2)?.[0] ?? '');
  rec('BUG-69', 'số chữ số của mã', otp.replace(/\D/g, '').length);
});

test('BUG-70 mật khẩu Abcdef1! ở B2', async ({ page }) => {
  const otp = await toStep2(page);
  const d = dialogs(page), c = countRequests(page, '/api/reset-password');
  await page.locator('form input').nth(0).fill(otp);
  await page.locator('form input').nth(1).fill('Abcdef1!');
  await submitBtn(page).click(); await page.waitForTimeout(1500);
  rec('BUG-70', 'B2 Abcdef1!', { hop_thoai: d.map(x => x.message), request_reset_password: c.n, url_sau: new URL(page.url()).pathname });
  page.removeAllListeners('dialog');
  await page.goto('/login');
  await loginInputs(page).nth(0).fill(USER.email); await loginInputs(page).nth(1).fill('Abcdef1!');
  await submitBtn(page).click(); await page.waitForTimeout(1500);
  rec('BUG-70', 'đăng nhập bằng Abcdef1!', { url_sau: new URL(page.url()).pathname, chu_trong_trang: (await mainLines(page)).filter(l => /thất bại|sai|lỗi/i.test(l)) });
  await restorePassword(page.request);
});

test('BUG-71 hình thức nút chính / phụ B2', async ({ page }) => {
  await toStep2(page);
  const props = ['background-color', 'color', 'width', 'height', 'border-top-style', 'border-top-color', 'font-weight', 'border-radius'];
  const st = async (name: string) => page.getByRole('button', { name }).evaluate((e, ps) => { const cs = getComputedStyle(e); return Object.fromEntries((ps as string[]).map(p => [p, cs.getPropertyValue(p)])); }, props);
  rec('BUG-71', "'Đặt lại mật khẩu'", await st('Đặt lại mật khẩu'));
  rec('BUG-71', "'← Quay lại'", await st('← Quay lại'));
});

async function profileValues(page: Page) {
  return [await byLabel(page, 'Họ Tên').inputValue(), await byLabel(page, 'Số điện thoại').inputValue(), await byLabel(page, 'Địa chỉ giao hàng').inputValue()];
}
async function profileRun(page: Page, req: APIRequestContext, v: { name?: string; phone?: string; addr?: string }) {
  await toProfile(page);
  const d = dialogs(page), put = countRequests(page, '/api/users/me');
  if (v.name !== undefined) await byLabel(page, 'Họ Tên').fill(v.name);
  if (v.phone !== undefined) await byLabel(page, 'Số điện thoại').fill(v.phone);
  if (v.addr !== undefined) await byLabel(page, 'Địa chỉ giao hàng').fill(v.addr);
  await submitBtn(page).click(); await page.waitForTimeout(1500);
  const r: any = { nhap: v, hop_thoai: d.map(x => x.message), request_users_me_sau_bam: put.n };
  r.navbar_khong_tai_lai = (await H(page).innerText()).replace(/\n/g, ' | ');
  await page.reload(); await expect(byLabel(page, 'Họ Tên')).toBeVisible();
  r.sau_F5 = await profileValues(page);
  r.navbar_sau_F5 = (await H(page).innerText()).replace(/\n/g, ' | ');
  page.removeAllListeners('dialog');
  await restoreProfile(req);
  return r;
}

test('BUG-72 SĐT 912345678', async ({ page, request }) => {
  rec('BUG-72', 'Steps SV', await profileRun(page, request, { phone: '912345678' }));
});

test('BUG-73 cập nhật 3 trường + F5', async ({ page, request }) => {
  rec('BUG-73', 'Steps SV (SĐT 0912345678)', await profileRun(page, request, { name: 'Test Repro', phone: '0912345678', addr: '1 Repro, Q1' }));
  rec('BUG-73', '(cô lập) cùng thao tác, SĐT 912345678', await profileRun(page, request, { name: 'Test Repro', phone: '912345678', addr: '1 Repro, Q1' }));
});

test('BUG-74 nhãn nút đăng xuất', async ({ page }) => {
  await uiLogin(page);
  rec('BUG-74', 'navbar sau đăng nhập', (await H(page).innerText()).replace(/\n/g, ' | '));
});

test('BUG-75 đổi Họ Tên → navbar', async ({ page, request }) => {
  rec('BUG-75', "Steps SV (chỉ đổi Họ Tên = 'Test Đổi')", await profileRun(page, request, { name: 'Test Đổi' }));
  rec('BUG-75', "(cô lập) Họ Tên 'Test Đổi' + SĐT 912345678", await profileRun(page, request, { name: 'Test Đổi', phone: '912345678' }));
});

test('BUG-76 /profile khi chưa đăng nhập', async ({ page }) => {
  await page.goto('/profile'); await page.waitForTimeout(1500);
  rec('BUG-76', 'URL sau 1,5 s', new URL(page.url()).pathname);
  rec('BUG-76', 'chữ trong main', (await page.locator('main').innerText()).slice(0, 200));
  rec('BUG-76', 'link/nút tới Đăng nhập trong main', await page.locator('main a[href="/login"], main button:has-text("Đăng nhập")').count());
});

test('BUG-77 URL /profil', async ({ page }) => {
  await page.goto('/profil'); await page.waitForTimeout(1000);
  rec('BUG-77', 'nội dung main', await page.locator('main').innerText());
  rec('BUG-77', "link về '/' trong main", await page.locator('main a[href="/"]').count());
});

test('BUG-79..81 Lịch sử đơn', async ({ page, request }) => {
  if (!seeded) { rec('BUG-81', 'seed_orders.py', seedOrders().trim().split('\n').slice(-8)); seeded = true; }
  // BUG-79: throttling + tải lại /profile, lấy mẫu chữ trong khối Lịch sử đơn mỗi 100 ms
  await toProfile(page);
  const how = await slow(page, '/api/orders');
  const samples: string[] = [];
  await page.reload({ waitUntil: 'commit' });
  for (let i = 0; i < 80; i++) {
    const t = await page.locator('h2:has-text("Lịch sử đơn hàng")').locator('xpath=..').innerText({ timeout: 200 }).catch(() => '(chưa có khối)');
    const s = t.includes('Bạn chưa có đơn hàng nào') ? 'rỗng: "Bạn chưa có đơn hàng nào."' : t.includes('Mã ĐH') ? 'bảng đơn' : /đang tải|loading/i.test(t) ? 'đang tải' : t.slice(0, 40);
    if (samples[samples.length - 1] !== s) samples.push(s);
    if (s === 'bảng đơn') break;
    await page.waitForTimeout(100);
  }
  rec('BUG-79', 'cách giảm tốc', how);
  rec('BUG-79', 'chuỗi trạng thái khối Lịch sử đơn khi tải lại', samples);
  await page.unrouteAll({ behavior: 'ignoreErrors' }).catch(() => {});
  // BUG-80: ngày đặt (locale mặc định của Playwright + vi-VN)
  await page.reload(); await expect(page.locator('th:has-text("Ngày đặt")')).toBeVisible({ timeout: 10000 });
  rec('BUG-80', `ngày đặt (navigator.language = ${await page.evaluate(() => navigator.language)})`, await page.locator('tbody tr td:nth-child(2)').first().innerText());
  const ctx = await page.context().browser()!.newContext({ locale: 'vi-VN', baseURL: 'http://localhost:5173' });
  const p2 = await ctx.newPage(); await toProfile(p2);
  await expect(p2.locator('th:has-text("Ngày đặt")')).toBeVisible({ timeout: 10000 });
  rec('BUG-80', `ngày đặt (context locale vi-VN, navigator.language = ${await p2.evaluate(() => navigator.language)})`, await p2.locator('tbody tr td:nth-child(2)').first().innerText());
  await ctx.close();
  // BUG-81: dòng Đang giao
  const rows = await page.locator('tbody tr').evaluateAll(trs => trs.map(tr => { const td = tr.querySelectorAll('td'); const b = tr.querySelector('button'); return `${td[0]?.textContent} ${td[3]?.textContent?.trim()}: nút ${b ? `"${b.textContent?.trim()}" disabled=${(b as HTMLButtonElement).disabled}` : 'không có'}`; }));
  rec('BUG-81', 'các dòng đơn', rows);
  const ship = page.locator('tbody tr', { hasText: 'Đang giao' }).first();
  const d = dialogs(page);
  if (await ship.locator('button', { hasText: 'Hủy đơn' }).count()) {
    await ship.locator('button', { hasText: 'Hủy đơn' }).click(); await page.waitForTimeout(3000);
    const t = await request.post('http://localhost:3000/api/login', { data: USER }).then(r => r.json());
    const mine = await request.get('http://localhost:3000/api/orders/my-orders', { headers: { Authorization: `Bearer ${t.token}` } }).then(r => r.json());
    rec('BUG-81', "bấm 'Hủy đơn' ở dòng Đang giao", { hop_thoai: d.map(x => x.message), trang_thai_don_sau_bam_API: (mine as any[]).map(o => `#${o.id} ${o.status}`) });
  }
});

test('BUG-82 dán vào ô nhập', async ({ page, context }) => {
  rec('BUG-82', 'Autofill', 'không chạy được bằng Playwright (profile trình duyệt sạch, không có dữ liệu Autofill đã lưu) – cần chạy tay');
  if (P !== 'P1') { rec('BUG-82', 'Paste', 'Firefox Playwright không cấp quyền clipboard – không chạy'); return; }
  await context.grantPermissions(['clipboard-read', 'clipboard-write']);
  const r: Record<string, string> = {};
  const paste = async (label: string, loc: ReturnType<Page['locator']>, val: string) => {
    await page.evaluate(v => navigator.clipboard.writeText(v), val);
    await loc.click(); await page.keyboard.press('Control+V'); r[label] = await loc.inputValue();
  };
  await page.goto('/login');
  await paste('/login ô 1 (Username)', loginInputs(page).nth(0), USER.email);
  await paste('/login ô 2 (Mật khẩu)', loginInputs(page).nth(1), USER.password);
  await page.goto('/forgot-password');
  await paste('quên MK B1 Email', page.locator('form input').first(), USER.email);
  rec('BUG-82', 'Paste (Ctrl+V) → giá trị trong ô', r);
});

test('BUG-83 focus sau submit lỗi', async ({ page, request }) => {
  const r: Record<string, string> = {};
  await page.goto('/login');
  await loginInputs(page).nth(0).fill(USER.email); await loginInputs(page).nth(1).fill('Wrong123!');
  await submitBtn(page).click(); await page.waitForTimeout(1500);
  r["Đăng nhập (mật khẩu 'Wrong123!')"] = await activeInfo(page);
  r['Đăng nhập – chữ báo lỗi'] = (await mainLines(page)).filter(l => /thất bại/i.test(l)).join(' ');
  await restorePassword(request);
  await request.post('http://localhost:3000/api/login', { data: USER });
  const otp = await toStep2(page);
  let d = dialogs(page);
  await page.locator('form input').nth(0).fill(otp); await page.locator('form input').nth(1).fill('123');
  await submitBtn(page).click(); await page.waitForTimeout(1200);
  r["Quên MK B2 (mật khẩu '123')"] = `${await activeInfo(page)} · hộp thoại ${JSON.stringify(d.map(x => x.message))}`;
  page.removeAllListeners('dialog');
  await toProfile(page);
  d = dialogs(page);
  await byLabel(page, 'Số điện thoại').fill('123');
  await submitBtn(page).click(); await page.waitForTimeout(1200);
  r["Hồ sơ (SĐT '123')"] = `${await activeInfo(page)} · hộp thoại ${JSON.stringify(d.map(x => x.message))}`;
  rec('BUG-83', 'phần tử đang focus sau submit lỗi', r);
  await restoreProfile(request);
});

test('BUG-84 tương phản chữ/nền', async ({ page }) => {
  const scan = async () => (await textColors(page)).map(t => ({ ...t, ratio: +contrast(rgb(t.fg), rgb(t.bg)).toFixed(2) })).filter(t => t.ratio < 4.5)
    .map(t => `"${t.text}" ${t.fg} / ${t.bg} = ${t.ratio}`);
  await page.goto('/login'); rec('BUG-84', '/login: phần tử chữ < 4.5:1', await scan());
  await page.goto('/forgot-password'); rec('BUG-84', '/forgot-password: phần tử chữ < 4.5:1', await scan());
  await toProfile(page); rec('BUG-84', '/profile: phần tử chữ < 4.5:1', await scan());
  rec('BUG-84', 'ghi chú', 'đo bằng màu tính toán (computed color, nền = nền không trong suốt gần nhất), không phải Lighthouse; placeholder không đo');
});

test('BUG-85 kích thước vùng bấm', async ({ page }) => {
  const r: Record<string, string> = {};
  const box = async (k: string, l: ReturnType<Page['locator']>) => { const b = await l.boundingBox(); r[k] = b ? `${Math.round(b.width)}×${Math.round(b.height)}` : 'không thấy'; };
  await page.goto('/login');
  await box('Sign In', page.getByRole('button', { name: 'Sign In' }));
  await box('Quên mật khẩu?', page.getByRole('link', { name: 'Quên mật khẩu?' }));
  await box('Đăng ký ngay', page.getByRole('link', { name: 'Đăng ký ngay' }));
  await page.goto('/forgot-password'); await box('Lấy mã OTP', page.getByRole('button', { name: 'Lấy mã OTP' }));
  await toProfile(page); await box('Cập nhật', page.getByRole('button', { name: 'Cập nhật' }));
  rec('BUG-85', 'boundingBox (CSS px)', r);
});

// Thay đổi trạng thái nhiều nhất → chạy cuối
test('BUG-78 chống gửi trùng', async ({ page, request }) => {
  // CL-53: giảm tốc + bấm Sign In 3 lần
  await page.goto('/login');
  await loginInputs(page).nth(0).fill(USER.email); await loginInputs(page).nth(1).fill(USER.password);
  const how = await slow(page, '/api/login');
  const c = countRequests(page, '/api/login');
  const btn = submitBtn(page);
  const t0 = await btn.innerText();
  await btn.click(); const mid = { disabled: await btn.isDisabled().catch(() => 'n/a'), text: await btn.innerText().catch(() => 'n/a') };
  await btn.click({ timeout: 2000 }).catch(() => {}); await btn.click({ timeout: 2000 }).catch(() => {});
  await page.waitForTimeout(5000);
  rec('BUG-78', 'Đăng nhập: bấm Sign In 3 lần khi mạng chậm', { cach_giam_toc: how, nhan_truoc: t0, ngay_sau_lan_1: mid, request_api_login: c.n });
  await page.unrouteAll({ behavior: 'ignoreErrors' }).catch(() => {});
  await page.context().clearCookies(); await page.evaluate(() => localStorage.clear());
  // SV-06 B1: double-click Lấy mã OTP
  await page.goto('/forgot-password');
  await page.locator('form input').first().fill(USER.email);
  const c1 = countRequests(page, '/api/forgot-password');
  await submitBtn(page).dblclick(); await page.waitForTimeout(1500);
  rec('BUG-78', "Quên MK B1: nhấp đúp 'Lấy mã OTP'", { request_api_forgot_password: c1.n });
  // SV-06 B2: OTP đúng + mật khẩu mới (Steps không nêu giá trị → 'Abcdef1!' hợp lệ theo SRS)
  const otp = await toStep2(page);
  let d = dialogs(page); const c2 = countRequests(page, '/api/reset-password');
  await page.locator('form input').nth(0).fill(otp); await page.locator('form input').nth(1).fill('Abcdef1!');
  await submitBtn(page).dblclick(); await page.waitForTimeout(1500);
  rec('BUG-78', "Quên MK B2: nhấp đúp 'Đặt lại mật khẩu' (Abcdef1!)", { request_api_reset_password: c2.n, hop_thoai: d.map(x => x.message) });
  page.removeAllListeners('dialog');
  // SV-06 Hồ sơ: Steps "nhập thông tin cập nhật" → SĐT 0912345678 (theo SRS) và (cô lập) 912345678
  for (const [k, phone] of [['Steps SV (SĐT 0912345678)', '0912345678'], ['(cô lập) SĐT 912345678', '912345678']]) {
    await toProfile(page);
    d = dialogs(page); const c3 = countRequests(page, '/api/users/me');
    await byLabel(page, 'Số điện thoại').fill(phone);
    const n0 = c3.n;
    await submitBtn(page).dblclick(); await page.waitForTimeout(1500);
    rec('BUG-78', `Hồ sơ: nhấp đúp 'Cập nhật' – ${k}`, { request_users_me: c3.n - n0, hop_thoai: d.map(x => x.message) });
    page.removeAllListeners('dialog');
    await restoreProfile(request);
  }
  // (cô lập) B2 với mật khẩu lọt regex của SUT ('Abcd efg1', có khoảng trắng) → có gửi 2 request không; sau đó khôi phục mật khẩu
  const otp2 = await toStep2(page);
  d = dialogs(page); const c4 = countRequests(page, '/api/reset-password');
  await page.locator('form input').nth(0).fill(otp2); await page.locator('form input').nth(1).fill('Abcd efg1');
  await submitBtn(page).dblclick(); await page.waitForTimeout(2000);
  rec('BUG-78', "(cô lập) Quên MK B2: nhấp đúp với 'Abcd efg1'", { request_api_reset_password: c4.n, hop_thoai: d.map(x => x.message) });
  page.removeAllListeners('dialog');
  await restorePassword(request);
});
