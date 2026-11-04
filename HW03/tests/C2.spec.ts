/**
 * HW03 T1 – checklist C2 (Tài khoản): phần tự động. Mỗi test = 1 item, tiêu đề bắt đầu bằng mã item (reporter.ts gom theo mã).
 * Ngưỡng/đầu vào lấy từ oracle.ts (khoá theo sha1 của expected). Kết quả = auto_status, không phải verdict chính thức (E2).
 * Thứ tự chạy có chủ ý: CL-62 (cần tài khoản chưa có đơn) chạy đầu; ngay sau đó ensureOrders() dựng đơn qua API.
 * Item đổi mật khẩu / hồ sơ khôi phục lại qua API ở finally. Item đăng nhập sai gọi resetAttempts() (backend khoá khi bộ đếm ≥ 3).
 */
import { Page } from '@playwright/test';
import {
  test, expect, oracle, obs, blocked, shot, USER, H, apiLogin, resetAttempts, setProfile, restoreProfile, restorePassword,
  ensureOrders, orderStatus, loginByToken, loginInputs, submitBtn, byLabel, fillLogin, forgotStep1, dialogs, countRequests,
  mainLines, newLines, tabWalk, interactive, orderViolations, fmtSeq, style, rgb, inHue, contrast, textColors,
} from './lib';

const soft = (ok: boolean, msg: string) => expect.soft(ok, msg).toBe(true);
const idOf = (title: string) => title.split(' ')[0];
const onlyOn = (info: any, plats: string[] | undefined) => {
  if (plats && !plats.includes(info.project.name)) { info.annotations.push({ type: 'manual', description: `chạy tay trên ${info.project.name}` }); test.skip(true, `chạy tay trên ${info.project.name}`); }
};
async function slow3G(page: Page) {
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('Network.enable');
  await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: 2000, downloadThroughput: 50 * 1024, uploadThroughput: 50 * 1024 });
}
async function historyPanel(page: Page) { return page.locator('main div', { has: page.locator('h2', { hasText: 'Lịch sử đơn' }) }).last(); }
async function orderRow(page: Page, id: number) { return page.locator('table tbody tr', { hasText: `#${id}` }).first(); }
async function messagesAfter(page: Page, act: () => Promise<void>, waitMs = 1500) {
  const d = dialogs(page);
  const before = await mainLines(page);
  await act();
  await page.waitForTimeout(waitMs);
  return { dialogs: d, lines: newLines(before, await mainLines(page)) };
}

test.afterEach(async ({ page }, info) => {
  if (info.status !== info.expectedStatus && info.status !== 'skipped') await shot(page, info, idOf(info.title));
});

// ============ 0. Trạng thái vừa seed (chưa có đơn) ============
test('CL-62 Empty state lịch sử đơn có hình minh hoạ và thông báo', async ({ page, request }, info) => {
  oracle('CL-62');
  await loginByToken(page, request, '/profile');
  const panel = await historyPanel(page);
  const icons = await panel.locator('img, svg, [role="img"], i[class*="icon"]').count();
  const text = (await panel.innerText()).split('\n').map(s => s.trim()).filter(Boolean);
  obs(info, `khu lịch sử: ${icons} icon/hình; chữ: ${JSON.stringify(text.slice(1))}`);
  soft(icons > 0, 'không có icon/hình minh hoạ trong khu Lịch sử đơn');
  soft(text.length > 1, 'không có câu thông báo');
  await shot(panel, info, 'CL-62');
});

// ============ 1. Đăng nhập (chưa đăng nhập) ============
test('CL-02 Mỗi trang có đúng 1 thẻ <h1>', async ({ page, request }, info) => {
  const o = oracle('CL-02');
  for (const p of o.pages) {
    if (p === '/profile') await loginByToken(page, request, p); else await page.goto(p);
    await page.waitForLoadState('networkidle');
    const n = await page.locator('h1').count();
    obs(info, `${p}: ${n} h1`);
    soft(n === o.h1, `${p}: có ${n} thẻ <h1>`);
  }
});
test('CL-03 Tiêu đề trang mô tả đúng chức năng Đăng nhập', async ({ page }, info) => {
  const o = oracle('CL-03');
  await page.goto('/login');
  const h = page.locator('main h1, main h2').first();
  const t = (await h.count()) ? (await h.innerText()).trim() : '';
  obs(info, `tiêu đề chính: "${t}"`);
  soft(t.toLowerCase().includes(o.heading.toLowerCase()), `tiêu đề là "${t}"`);
  await shot(h, info, 'CL-03');
});
test('CL-13 Tiêu đề tab trình duyệt mô tả trang', async ({ page, request }, info) => {
  const o = oracle('CL-13');
  const titles: string[] = [];
  for (const p of ['/login', '/forgot-password', '/profile']) {
    if (p === '/profile') await loginByToken(page, request, p); else await page.goto(p);
    titles.push(await page.title());
  }
  obs(info, `title: ${JSON.stringify(titles)}`);
  for (const t of titles) soft(o.names.some((n: string) => t.includes(n)), `title "${t}" không chứa tên ứng dụng/tên trang`);
  soft(new Set(titles).size === 3, 'title giống nhau giữa các trang');
});
test('CL-14 Khai báo ngôn ngữ trang là tiếng Việt', async ({ page }, info) => {
  const o = oracle('CL-14');
  await page.goto('/login');
  const lang = await page.evaluate(() => document.documentElement.lang);
  obs(info, `<html lang="${lang}">`);
  soft(lang === o.lang, `lang = "${lang}"`);
});
test('CL-17 Ô Email dùng type="email"', async ({ page }, info) => {
  const o = oracle('CL-17');
  await page.goto('/login');
  const t1 = await loginInputs(page).nth(0).getAttribute('type');
  await page.goto('/forgot-password');
  const t2 = await page.locator('form input').first().getAttribute('type');
  obs(info, `/login: type="${t1}"; /forgot-password bước 1: type="${t2}"`);
  soft(t1 === o.type, `/login ô Email type="${t1}"`);
  soft(t2 === o.type, `/forgot-password ô Email type="${t2}"`);
});
test('CL-66 Email sai định dạng bị chặn trước khi gửi', async ({ page }, info) => {
  const o = oracle('CL-66');
  for (const [p, api] of [['/login', '/api/login'], ['/forgot-password', '/api/forgot-password']]) {
    await page.goto(p);
    const c = countRequests(page, api);
    const inputs = page.locator('form input');
    await inputs.nth(0).fill(o.value);
    if (p === '/login') await inputs.nth(1).fill(USER.password);
    await submitBtn(page).click();
    await page.waitForTimeout(1000);
    const valid = await inputs.nth(0).evaluate((e: HTMLInputElement) => e.validity.valid);
    obs(info, `${p}: ${c.n} request ${api}; validity.valid=${valid}`);
    soft(c.n === 0, `${p}: form gửi ${c.n} request ${api}`);
    soft(!valid, `${p}: không có thông báo validate`);
  }
});
test('CL-18 Nhãn ô đăng nhập là Email', async ({ page }, info) => {
  const o = oracle('CL-18');
  await page.goto('/login');
  const t = (await page.locator('form label').first().innerText()).trim();
  obs(info, `nhãn ô thứ nhất: "${t}"`);
  soft(t.includes(o.label), `nhãn là "${t}"`);
});
test('CL-19 Ô mật khẩu che ký tự', async ({ page }, info) => {
  const o = oracle('CL-19');
  await page.goto('/login');
  const t1 = await loginInputs(page).nth(1).getAttribute('type');
  obs(info, `/login ô Mật khẩu type="${t1}"`);
  soft(t1 === 'password', `/login ô Mật khẩu type="${t1}"`);
  await forgotStep1(page);
  const labels = page.locator('form label', { hasText: /mật khẩu/i });
  for (let i = 0; i < await labels.count(); i++) {
    const lb = (await labels.nth(i).innerText()).trim();
    const inp = labels.nth(i).locator('xpath=following-sibling::input[1]');
    await inp.fill(o.typed);
    const t = await inp.getAttribute('type');
    obs(info, `bước 2 "${lb}": type="${t}"`);
    soft(t === 'password', `bước 2 "${lb}" type="${t}"`);
  }
});
test('CL-20 Dấu * trên nhãn trường bắt buộc', async ({ page }, info) => {
  const o = oracle('CL-20');
  const check = async (where: string) => {
    for (const lb of await page.locator('form label').allInnerTexts()) {
      obs(info, `${where} "${lb.trim()}"`);
      soft(lb.includes(o.mark), `${where}: nhãn "${lb.trim()}" thiếu '*'`);
    }
  };
  await page.goto('/login'); await check('/login');
  await page.goto('/forgot-password'); await check('bước 1');
  await forgotStep1(page); await check('bước 2');
});
test('CL-22 Thông báo lỗi đăng nhập nằm phía trên nút submit', async ({ page, request }, info) => {
  const o = oracle('CL-22');
  try {
    await fillLogin(page, USER.email, o.wrong);
    const m = await messagesAfter(page, () => submitBtn(page).click());
    const sb = await submitBtn(page).boundingBox();
    obs(info, `chữ mới: ${JSON.stringify(m.lines)}; hộp thoại: ${JSON.stringify(m.dialogs.map(d => d.message))}`);
    soft(m.lines.length > 0, 'không có thông báo lỗi trong trang');
    for (const l of m.lines) {
      const b = await page.locator('main').getByText(l).first().boundingBox();
      obs(info, `"${l}" y=${b?.y}; nút submit y=${sb?.y}`);
      soft(!!b && !!sb && b.y < sb.y, `thông báo "${l}" nằm dưới nút submit`);
    }
    await shot(page, info, 'CL-22');
  } finally { await resetAttempts(request); }
});
test('CL-35 Giữ lại Email sau khi đăng nhập thất bại', async ({ page, request }, info) => {
  const o = oracle('CL-35');
  try {
    await fillLogin(page, USER.email, o.wrong);
    await submitBtn(page).click();
    await page.waitForTimeout(1500);
    const v = await loginInputs(page).nth(0).inputValue();
    obs(info, `ô Email sau lỗi: "${v}"`);
    soft(v === USER.email, `ô Email = "${v}"`);
  } finally { await resetAttempts(request); }
});
test('CL-36 Phím Enter gửi form đăng nhập', async ({ page }, info) => {
  oracle('CL-36');
  await fillLogin(page, USER.email, USER.password);
  await loginInputs(page).nth(1).press('Enter');
  const left = await page.waitForURL(u => !u.pathname.startsWith('/login'), { timeout: 5000 }).then(() => true, () => false);
  obs(info, `sau Enter: ${page.url()}`);
  soft(left, 'Enter không gửi form');
});
test('CL-44 Đăng nhập thành công rời trang đăng nhập và navbar cập nhật', async ({ page }, info) => {
  const o = oracle('CL-44');
  await fillLogin(page, USER.email, USER.password);
  const t0 = Date.now();
  await submitBtn(page).click();
  const ok = await page.waitForURL(u => !u.pathname.startsWith('/login'), { timeout: 5000 }).then(() => true, () => false);
  const nav = await H(page).locator('a[href="/profile"]').waitFor({ timeout: 5000 }).then(() => true, () => false);
  const ms = Date.now() - t0;
  obs(info, `rời /login: ${ok}; navbar có link hồ sơ: ${nav}; ${ms} ms`);
  soft(ok && nav, 'vẫn ở /login hoặc navbar không đổi');
  soft(ms <= o.ms, `mất ${ms} ms (> ${o.ms} ms)`);
});
test('CL-51 Thông báo đăng nhập sai không lộ nguyên nhân', async ({ page, request }, info) => {
  const o = oracle('CL-51');
  try {
    const msg = async (email: string) => {
      await fillLogin(page, email, o.wrong);
      const m = await messagesAfter(page, () => submitBtn(page).click());
      return [...m.lines, ...m.dialogs.map(d => `[hộp thoại] ${d.message}`)].join(' | ');
    };
    const a = await msg(o.wrongEmail), b = await msg(USER.email);
    obs(info, `email không tồn tại: "${a}"; sai mật khẩu: "${b}"`);
    soft(!!a && a === b, 'hai thông báo khác nhau hoặc không có thông báo');
  } finally { await resetAttempts(request); }
});
test('CL-45 Link Quên mật khẩu tới đúng /forgot-password', async ({ page }, info) => {
  const o = oracle('CL-45');
  await page.goto('/login');
  await page.getByText(o.link, { exact: true }).click();
  await page.waitForLoadState();
  const path = new URL(page.url()).pathname;
  const form = await page.locator('form input').count();
  obs(info, `URL: ${path}; số ô nhập: ${form}`);
  soft(path === o.path && form > 0, `tới ${path}`);
});
test('CL-46 Link Đăng ký ngay tới trang Đăng ký', async ({ page }, info) => {
  const o = oracle('CL-46');
  await page.goto('/login');
  await page.getByText(o.link, { exact: true }).click();
  await page.waitForLoadState();
  const path = new URL(page.url()).pathname;
  obs(info, `URL: ${path}`);
  soft(path === o.path && (await page.locator('form input').count()) > 0, `tới ${path}`);
});
test('CL-10 Thứ tự Tab theo vị trí hiển thị – Đăng nhập', async ({ page }, info) => {
  const o = oracle('CL-10');
  await page.goto(o.page);
  const seq = await tabWalk(page), all = await interactive(page);
  const v = orderViolations(seq, o.tol), miss = all.filter(a => !seq.some(s => s.key === a.key));
  obs(info, `chuỗi Tab: ${fmtSeq(seq)}`);
  soft(v.length === 0, `nhảy ngược: ${v.join('; ')}`);
  soft(miss.length === 0, `bỏ qua: ${fmtSeq(miss)}`);
});
test('CL-38 Nhãn gắn với ô nhập (bấm nhãn → focus ô)', async ({ page, request }, info) => {
  oracle('CL-38');
  const check = async (where: string) => {
    const labels = page.locator('main label');
    for (let i = 0; i < await labels.count(); i++) {
      const inp = labels.nth(i).locator('xpath=following-sibling::*[self::input or self::textarea][1]');
      if (await inp.isDisabled()) continue;
      await labels.nth(i).click();
      const same = await inp.evaluate(e => e === document.activeElement);
      const t = (await labels.nth(i).innerText()).trim();
      obs(info, `${where} "${t}": ${same ? 'focus vào ô' : 'không focus'}`);
      soft(same, `${where}: bấm nhãn "${t}" không focus ô`);
    }
  };
  await page.goto('/login'); await check('/login');
  await loginByToken(page, request, '/profile'); await check('/profile');
});
test('CL-49 /profile khi chưa đăng nhập dẫn được tới Đăng nhập', async ({ page }, info) => {
  oracle('CL-49');
  await page.goto('/profile');
  await page.waitForTimeout(1500);
  const path = new URL(page.url()).pathname;
  const link = await page.locator('main a[href*="login"], main button', { hasText: /đăng nhập/i }).count();
  obs(info, `URL: ${path}; link/nút tới Đăng nhập trong trang: ${link}`);
  soft(path === '/login' || link > 0, 'không tự chuyển và không có link/nút tới Đăng nhập');
  await shot(page, info, 'CL-49');
});
test('CL-50 URL không tồn tại hiển thị trang 404 có lối về', async ({ page }, info) => {
  const o = oracle('CL-50');
  await page.goto(o.url);
  await page.waitForTimeout(800);
  const txt = (await page.locator('main').innerText()).trim();
  const home = await page.locator('main a[href="/"]').count();
  obs(info, `nội dung main: "${txt.slice(0, 80)}"; link về '/': ${home}`);
  soft(new RegExp(o.re, 'i').test(txt), 'không có thông báo không tìm thấy');
  soft(home > 0, 'không có link về trang chủ trong trang');
  await shot(page, info, 'CL-50');
});

// ============ 2. Quên mật khẩu ============
test('CL-24 Có chỉ báo bước (Step Indicator)', async ({ page }, info) => {
  const o = oracle('CL-24');
  await page.goto('/forgot-password');
  const s1 = new RegExp(o.re1, 'i').test(await page.locator('main').innerText());
  await forgotStep1(page);
  const s2 = new RegExp(o.re2, 'i').test(await page.locator('main').innerText());
  obs(info, `bước 1 có "Bước 1 / 2": ${s1}; bước 2 có "Bước 2 / 2": ${s2}`);
  soft(s1, 'bước 1 không có chữ chỉ báo bước (SV xác nhận có/không chỉ báo tương đương)');
  soft(s2, 'bước 2 không có chữ chỉ báo bước (SV xác nhận có/không chỉ báo tương đương)');
  await shot(page, info, 'CL-24');
});
test('CL-25 Có nút Quay lại đăng nhập', async ({ page }, info) => {
  const o = oracle('CL-25');
  await page.goto('/forgot-password');
  const b = page.locator('main').getByText(new RegExp(o.label, 'i')).first();
  const n = await b.count();
  obs(info, `bước 1 có "${o.label}": ${n > 0}`);
  soft(n > 0, `bước 1 không có "${o.label}"`);
  if (n) { await b.click(); await page.waitForTimeout(800); soft(new URL(page.url()).pathname === '/login', `bấm → ${page.url()}`); }
});
test('CL-26 Có ô Xác nhận mật khẩu mới', async ({ page }, info) => {
  const o = oracle('CL-26');
  await forgotStep1(page);
  const labels = (await page.locator('form label').allInnerTexts()).map(s => s.trim());
  obs(info, `bước 2: ${labels.length} ô – ${JSON.stringify(labels)}`);
  soft(labels.some(l => l.toLowerCase().includes(o.confirm)), 'không có ô Xác nhận mật khẩu mới');
});
test('CL-27 Hai mật khẩu không khớp bị chặn', async ({ page, request }, info) => {
  const o = oracle('CL-27');
  const code = await forgotStep1(page);
  const confirm = byLabel(page, /xác nhận/i);
  if (!(await confirm.count())) { blocked(info, 'Blocked – không có ô Xác nhận mật khẩu mới (item gốc CL-26)'); test.skip(true, 'Blocked do CL-26'); }
  try {
    await page.locator('form input').nth(0).fill(code ?? '');
    await byLabel(page, /mật khẩu mới/i).fill(o.pw1);
    await confirm.fill(o.pw2);
    const m = await messagesAfter(page, () => submitBtn(page).click());
    const changed = (await request.post('http://localhost:3000/api/login', { data: { email: USER.email, password: o.pw1 } })).status() === 200;
    obs(info, `đổi được bằng mật khẩu thứ nhất: ${changed}; thông báo: ${JSON.stringify([...m.lines, ...m.dialogs.map(d => d.message)])}`);
    soft(!changed, 'mật khẩu vẫn bị đổi dù hai ô không khớp');
  } finally { await restorePassword(request); }
});
test('CL-28 Mã OTP hiển thị có đúng 6 chữ số', async ({ page }, info) => {
  const o = oracle('CL-28');
  const code = await forgotStep1(page);
  obs(info, `mã hiển thị: ${code}`);
  soft(!!code && code.length === o.digits, `mã có ${code?.length ?? 0} chữ số`);
  await shot(page.locator('main'), info, 'CL-28');
});
test('CL-54 OTP hiển thị trên màn hình', async ({ page }, info) => {
  oracle('CL-54');
  const code = await forgotStep1(page);
  obs(info, `mã hiển thị: ${code}`);
  soft(!!code, 'không thấy mã OTP trên trang');
});
test('CL-29 Mật khẩu mới hợp lệ theo FR-01 được chấp nhận', async ({ page, request }, info) => {
  const o = oracle('CL-29');
  try {
    const code = await forgotStep1(page);
    await page.locator('form input').nth(0).fill(code ?? '');
    await byLabel(page, /mật khẩu mới/i).fill(o.pw);
    const c = byLabel(page, /xác nhận/i); if (await c.count()) await c.fill(o.pw);
    const m = await messagesAfter(page, () => submitBtn(page).click(), 2000);
    const ok = (await request.post('http://localhost:3000/api/login', { data: { email: USER.email, password: o.pw } })).status() === 200;
    obs(info, `đăng nhập bằng "${o.pw}": ${ok}; thông báo: ${JSON.stringify([...m.lines, ...m.dialogs.map(d => d.message)])}`);
    soft(ok, `mật khẩu "${o.pw}" không được chấp nhận`);
  } finally { await restorePassword(request); }
});
test('CL-48 Đặt lại mật khẩu thành công có lối đi tới đăng nhập', async ({ page, request }, info) => {
  const o = oracle('CL-48');
  try {
    const code = await forgotStep1(page);
    await page.locator('form input').nth(0).fill(code ?? '');
    await byLabel(page, /mật khẩu mới/i).fill(o.pw);
    const c = byLabel(page, /xác nhận/i); if (await c.count()) await c.fill(o.pw);
    await messagesAfter(page, () => submitBtn(page).click(), 2000);
    const ok = (await request.post('http://localhost:3000/api/login', { data: { email: USER.email, password: o.pw } })).status() === 200;
    if (!ok) { blocked(info, `Blocked – không đổi được mật khẩu bằng "${o.pw}" (item gốc CL-29)`); test.skip(true, 'Blocked do CL-29'); }
    const path = new URL(page.url()).pathname;
    const link = await page.locator('main a[href*="login"]').count();
    obs(info, `sau khi đổi: URL ${path}; link tới Đăng nhập: ${link}`);
    soft(path === '/login' || link > 0, 'không có lối tới Đăng nhập');
  } finally { await restorePassword(request); }
});
test('CL-30 Mật khẩu yếu bị từ chối với thông báo nêu đúng quy tắc', async ({ page, request }, info) => {
  const o = oracle('CL-30');
  try {
    const code = await forgotStep1(page);
    await page.locator('form input').nth(0).fill(code ?? '');
    await byLabel(page, /mật khẩu mới/i).fill(o.weak);
    const c = byLabel(page, /xác nhận/i); if (await c.count()) await c.fill(o.weak);
    const m = await messagesAfter(page, () => submitBtn(page).click());
    const changed = (await request.post('http://localhost:3000/api/login', { data: { email: USER.email, password: o.weak } })).status() === 200;
    const text = [...m.lines, ...m.dialogs.map(d => d.message)].join(' ').toLowerCase();
    const missing = o.keywords.filter((k: string) => !text.includes(k));
    obs(info, `bị đổi: ${changed}; thông báo: "${text}"`);
    soft(!changed, `mật khẩu yếu "${o.weak}" được chấp nhận`);
    soft(missing.length === 0, `thông báo thiếu: ${missing.join(', ')}`);
  } finally { await restorePassword(request); }
});
test('CL-39 Quay lại bước 1 vẫn giữ email đã nhập', async ({ page }, info) => {
  oracle('CL-39');
  await forgotStep1(page);
  const back = page.locator('form button:not([type="submit"]), main a', { hasText: /quay lại/i }).first();
  if (!(await back.count())) { blocked(info, 'Blocked – bước 2 không có nút quay lại'); test.skip(true); }
  await back.click();
  await page.waitForTimeout(500);
  const v = await page.locator('form input').first().inputValue();
  obs(info, `ô email bước 1 sau khi quay lại: "${v}"`);
  soft(v === USER.email, `ô email = "${v}"`);
});
test('CL-12 Thứ tự Tab ở bước 2 theo vị trí hiển thị', async ({ page }, info) => {
  const o = oracle('CL-12');
  await forgotStep1(page);
  const seq = await tabWalk(page), all = await interactive(page);
  const v = orderViolations(seq, o.tol), miss = all.filter(a => !seq.some(s => s.key === a.key));
  obs(info, `chuỗi Tab: ${fmtSeq(seq)}`);
  soft(v.length === 0, `nhảy ngược: ${v.join('; ')}`);
  soft(miss.length === 0, `bỏ qua: ${fmtSeq(miss)}`);
});
test('CL-06 Nút chính và nút phụ phân biệt được bằng hình thức', async ({ page }, info) => {
  oracle('CL-06');
  await forgotStep1(page);
  const btns = page.locator('form button');
  if ((await btns.count()) < 2) { blocked(info, 'Blocked – bước 2 không có nút phụ'); test.skip(true); }
  const p = ['background-color', 'border-top-width', 'border-top-color', 'height', 'width'];
  const a = await style(btns.nth(0), p), b = await style(btns.nth(1), p);
  obs(info, `nút chính ${JSON.stringify(a)}; nút phụ ${JSON.stringify(b)}`);
  soft(JSON.stringify(a) !== JSON.stringify(b), 'hai nút cùng màu nền, viền, kích thước');
  await shot(page.locator('form'), info, 'CL-06');
});
test('CL-07 Các nút trên cùng form đồng nhất kích thước và font', async ({ page }, info) => {
  const o = oracle('CL-07');
  await forgotStep1(page);
  const btns = page.locator('form button');
  const s: any[] = [];
  for (let i = 0; i < await btns.count(); i++) s.push({ ...(await style(btns.nth(i), ['font-family', 'font-size'])), h: (await btns.nth(i).boundingBox())!.height });
  obs(info, JSON.stringify(s));
  const hs = s.map(x => x.h);
  soft(Math.max(...hs) - Math.min(...hs) <= o.px, `chênh chiều cao ${Math.max(...hs) - Math.min(...hs)} px`);
  soft(new Set(s.map(x => `${x['font-family']}|${x['font-size']}`)).size === 1, 'khác font-family/font-size');
});

// ============ 3. Hồ sơ (đã đăng nhập) ============
test('CL-16 Tên người dùng hiển thị an toàn (không render HTML)', async ({ page, request }, info) => {
  const o = oracle('CL-16');
  try {
    await setProfile(request, { name: o.name });
    await loginByToken(page, request, '/');
    const link = H(page).locator('a[href="/profile"]');
    const txt = await link.innerText(), bold = await link.locator('b').count();
    obs(info, `navbar: "${txt}"; số thẻ <b>: ${bold}`);
    soft(txt.includes(o.name) && bold === 0, 'chuỗi HTML bị render (mất dấu < >)');
    await shot(H(page), info, 'CL-16');
  } finally { await restoreProfile(request); }
});
test('CL-21 Dấu * trên trường mà form bắt buộc nhập', async ({ page, request }, info) => {
  const o = oracle('CL-21');
  try {
    for (const f of o.fields) {
      await loginByToken(page, request, '/profile');
      const c = { n: 0 }; page.on('request', r => { if (r.url().includes('/api/users/me') && r.method() === 'PUT') c.n++; });
      dialogs(page);
      await byLabel(page, f).fill('');
      await page.getByRole('button', { name: 'Cập nhật' }).click();
      await page.waitForTimeout(1000);
      const lb = (await page.locator('label', { hasText: f }).first().innerText()).trim();
      const required = c.n === 0, star = lb.includes(o.mark);
      obs(info, `"${f}" trống: ${required ? 'bị chặn' : 'gửi được'}; nhãn "${lb}"`);
      soft(required === star, required ? `"${f}" bị chặn khi trống nhưng nhãn không có '*'` : `"${f}" không bắt buộc nhưng nhãn có '*'`);
      await restoreProfile(request);
    }
  } finally { await restoreProfile(request); }
});
test('CL-23 Thông báo lỗi validate hiển thị trong trang, phía trên nút submit', async ({ page, request }, info) => {
  const o = oracle('CL-23');
  const judge = async (where: string, m: { dialogs: any[]; lines: string[] }) => {
    const sb = await submitBtn(page).boundingBox();
    obs(info, `${where}: chữ mới ${JSON.stringify(m.lines)}; hộp thoại ${JSON.stringify(m.dialogs.map(d => d.message))}`);
    soft(m.lines.length > 0, `${where}: lỗi chỉ ở hộp thoại hoặc không có (GA3)`);
    for (const l of m.lines) { const b = await page.locator('main').getByText(l).first().boundingBox(); soft(!!b && !!sb && b.y < sb.y, `${where}: "${l}" nằm dưới nút submit`); }
  };
  try {
    const code = await forgotStep1(page);
    await page.locator('form input').nth(0).fill(code ?? '');
    await byLabel(page, /mật khẩu mới/i).fill(o.weak);
    await judge('bước 2 mật khẩu yếu', await messagesAfter(page, () => submitBtn(page).click()));
    await loginByToken(page, request, '/profile');
    await byLabel(page, 'Số điện thoại').fill(o.phone);
    await judge('Hồ sơ SĐT sai', await messagesAfter(page, () => submitBtn(page).click()));
  } finally { await restorePassword(request); await restoreProfile(request); }
});
test('CL-31 SĐT hợp lệ (bắt đầu 0, 10–11 số) được chấp nhận', async ({ page, request }, info) => {
  const o = oracle('CL-31');
  try {
    for (const ph of o.phones) {
      await loginByToken(page, request, '/profile');
      dialogs(page);
      await byLabel(page, 'Số điện thoại').fill(ph);
      await submitBtn(page).click();
      await page.waitForTimeout(1500);
      await page.reload();
      await expect(byLabel(page, 'Họ Tên')).toBeVisible();
      const v = await byLabel(page, 'Số điện thoại').inputValue();
      obs(info, `nhập ${ph} → sau F5: "${v}"`);
      soft(v === ph, `${ph} không được lưu (sau F5: "${v}")`);
    }
  } finally { await restoreProfile(request); }
});
test('CL-32 SĐT không hợp lệ bị từ chối, thông báo nêu đúng quy tắc', async ({ page, request }, info) => {
  const o = oracle('CL-32');
  try {
    await loginByToken(page, request, '/profile');
    await byLabel(page, 'Số điện thoại').fill(o.phone);
    const m = await messagesAfter(page, () => submitBtn(page).click());
    const text = [...m.lines, ...m.dialogs.map(d => d.message)].join(' ');
    await page.reload(); await expect(byLabel(page, 'Họ Tên')).toBeVisible();
    const v = await byLabel(page, 'Số điện thoại').inputValue();
    const missing = o.keywords.filter((k: string) => !text.includes(k));
    obs(info, `thông báo: "${text}"; sau F5: "${v}"`);
    soft(v !== o.phone, `${o.phone} được lưu`);
    soft(missing.length === 0, `thông báo không nêu: ${missing.join(', ')}`);
  } finally { await restoreProfile(request); }
});
test('CL-33 Email không sửa được và trông như trường bị khoá', async ({ page, request }, info) => {
  const o = oracle('CL-33');
  await loginByToken(page, request, '/profile');
  const e = byLabel(page, 'Email'), n = byLabel(page, 'Họ Tên');
  const before = await e.inputValue();
  await e.fill(o.try, { timeout: 1500 }).catch(() => {});
  const after = await e.inputValue();
  const be = (await style(e, ['background-color']))['background-color'], bn = (await style(n, ['background-color']))['background-color'];
  obs(info, `disabled=${await e.isDisabled()}; giá trị trước/sau gõ: "${before}"/"${after}"; nền Email ${be}, nền Họ Tên ${bn}`);
  soft(after === before, 'gõ sửa được ô Email');
  soft(be !== bn, 'ô Email cùng nền với ô thường');
});
test('CL-34 Họ Tên chỉ gồm khoảng trắng bị từ chối', async ({ page, request }, info) => {
  const o = oracle('CL-34');
  try {
    await loginByToken(page, request, '/profile');
    await byLabel(page, 'Họ Tên').fill(o.name);
    const m = await messagesAfter(page, () => submitBtn(page).click());
    await page.reload(); await expect(byLabel(page, 'Họ Tên')).toBeVisible();
    const v = await byLabel(page, 'Họ Tên').inputValue();
    obs(info, `thông báo: ${JSON.stringify([...m.lines, ...m.dialogs.map(d => d.message)])}; Họ Tên sau F5: "${v}"`);
    soft(v === 'Test User', `Họ Tên được lưu thành "${v}"`);
  } finally { await restoreProfile(request); }
});
test('CL-37 Cập nhật hồ sơ được lưu bền', async ({ page, request }, info) => {
  const o = oracle('CL-37');
  try {
    await loginByToken(page, request, '/profile');
    dialogs(page);
    await byLabel(page, 'Họ Tên').fill(o.name);
    await byLabel(page, 'Số điện thoại').fill(o.phone);
    await byLabel(page, 'Địa chỉ giao hàng').fill(o.addr);
    await submitBtn(page).click();
    await page.waitForTimeout(1500);
    await page.reload(); await expect(byLabel(page, 'Họ Tên')).toBeVisible();
    const got = [await byLabel(page, 'Họ Tên').inputValue(), await byLabel(page, 'Số điện thoại').inputValue(), await byLabel(page, 'Địa chỉ giao hàng').inputValue()];
    obs(info, `sau F5: ${JSON.stringify(got)}`);
    soft(JSON.stringify(got) === JSON.stringify([o.name, o.phone, o.addr]), 'có trường quay về giá trị cũ');
  } finally { await restoreProfile(request); }
});
test('CL-55 Cập nhật thành công có phản hồi rõ ràng', async ({ page, request }, info) => {
  const o = oracle('CL-55');
  try {
    await loginByToken(page, request, '/profile');
    const d = dialogs(page);
    const before = await mainLines(page);
    await byLabel(page, 'Số điện thoại').fill('0912345678');
    const t0 = Date.now();
    await submitBtn(page).click();
    let ms = -1, msg = '';
    for (let i = 0; i < 30 && ms < 0; i++) {
      const nl = newLines(before, await mainLines(page));
      if (d.length) { ms = d[0].at - t0; msg = d[0].message; } else if (nl.length) { ms = Date.now() - t0; msg = nl[0]; } else await page.waitForTimeout(100);
    }
    obs(info, `phản hồi sau ${ms} ms: "${msg}"`);
    soft(ms >= 0 && ms <= o.ms, ms < 0 ? 'không có phản hồi trong 3 s' : `phản hồi sau ${ms} ms`);
    soft(/[àáảãạăâđèéẻẽẹêìíỉĩịòóỏõọôơùúủũụưỳýỷỹỵ]/i.test(msg), `phản hồi không phải tiếng Việt: "${msg}"`);
  } finally { await restoreProfile(request); }
});
test('CL-56 Đổi Họ Tên cập nhật ngay trên navbar', async ({ page, request }, info) => {
  const o = oracle('CL-56');
  try {
    await loginByToken(page, request, '/profile');
    dialogs(page);
    await byLabel(page, 'Họ Tên').fill(o.name);
    await submitBtn(page).click();
    const ok = await expect(H(page)).toContainText(o.name, { timeout: o.waitMs }).then(() => true, () => false);
    obs(info, `navbar sau ${o.waitMs} ms (không tải lại): "${(await H(page).innerText()).replace(/\n/g, ' | ')}"`);
    soft(ok, 'navbar vẫn tên cũ khi chưa tải lại');
  } finally { await restoreProfile(request); }
});
test('CL-65 Phiên đăng nhập giữ sau khi tải lại trang', async ({ page, request }, info) => {
  oracle('CL-65');
  await loginByToken(page, request, '/profile');
  await page.reload();
  const ok = await H(page).locator('a[href="/profile"]').waitFor({ timeout: 5000 }).then(() => true, () => false);
  const form = await byLabel(page, 'Họ Tên').isVisible().catch(() => false);
  obs(info, `sau F5: navbar có tên ${ok}; form hồ sơ ${form}`);
  soft(ok && form, 'bị đăng xuất sau F5');
});
test('CL-40 Navbar highlight trang đang chọn', async ({ page, request }, info) => {
  const o = oracle('CL-40');
  await loginByToken(page, request, '/profile');
  const link = H(page).locator('a[href="/profile"]');
  const onProfile = await style(link, o.props), cart = await style(H(page).locator('a[href="/cart"]'), o.props);
  await H(page).getByRole('link', { name: 'EShop' }).click();
  await page.waitForURL(u => u.pathname === '/');
  const onHome = await style(link, o.props);
  obs(info, `link hồ sơ ở /profile ${JSON.stringify(onProfile)}; ở / ${JSON.stringify(onHome)}; link Giỏ hàng ${JSON.stringify(cart)}`);
  soft(JSON.stringify(onProfile) !== JSON.stringify(onHome), 'kiểu link không đổi theo trang hiện tại');
});
test('CL-47 Logo EShop về trang chủ từ mọi màn C2', async ({ page, request }, info) => {
  const o = oracle('CL-47');
  for (const p of o.pages) {
    if (p === '/profile') await loginByToken(page, request, p); else await page.goto(p);
    await H(page).getByRole('link', { name: 'EShop' }).click();
    await page.waitForTimeout(500);
    const path = new URL(page.url()).pathname;
    obs(info, `${p} → ${path}`);
    soft(path === '/', `${p}: logo dẫn tới ${path}`);
  }
});
test('CL-41 Link Giỏ hàng có badge số lượng', async ({ page, request }, info) => {
  const o = oracle('CL-41');
  await loginByToken(page, request, '/');
  dialogs(page);
  await page.locator(`a[href="${o.product}"]`).first().click();
  await page.getByRole('button', { name: o.add }).click();
  await page.waitForTimeout(800);
  await H(page).getByRole('link', { name: 'EShop' }).click();
  const cart = H(page).locator('a[href="/cart"]');
  const t = (await cart.innerText()).trim();
  obs(info, `link Giỏ hàng: "${t}"`);
  soft(/[1-9]\d*/.test(t), 'không có badge số > 0');
  await shot(H(page), info, 'CL-41');
});
test('CL-42 Nút đăng xuất có nhãn Đăng xuất', async ({ page, request }, info) => {
  const o = oracle('CL-42');
  await loginByToken(page, request, '/');
  const t = (await H(page).locator('button').first().innerText()).trim();
  obs(info, `nhãn nút: "${t}"`);
  soft(t === o.label, `nhãn là "${t}"`);
});
test('CL-43 Đăng xuất: navbar về trạng thái chưa đăng nhập', async ({ page, request }, info) => {
  oracle('CL-43');
  await loginByToken(page, request, '/');
  await H(page).locator('button').first().click();
  const login = await H(page).getByRole('link', { name: 'Đăng nhập' }).isVisible(), name = await H(page).locator('a[href="/profile"]').count();
  obs(info, `sau đăng xuất: link Đăng nhập ${login}; link tên người dùng ${name}`);
  soft(login && name === 0, 'navbar còn tên người dùng hoặc không có Đăng nhập');
});
test('CL-67 Đăng xuất giữ nguyên sau khi tải lại trang', async ({ page, request }, info) => {
  oracle('CL-67');
  await loginByToken(page, request, '/');
  await H(page).locator('button').first().click();
  await page.reload();
  await page.waitForTimeout(1000);
  const login = await H(page).getByRole('link', { name: 'Đăng nhập' }).isVisible();
  obs(info, `sau F5: link Đăng nhập ${login}`);
  soft(login, 'tự đăng nhập lại sau F5');
});

// ============ 4. Lịch sử đơn (dựng đơn qua API) ============
test('CL-68 Sau đăng xuất, /profile không hiển thị dữ liệu tài khoản cũ', async ({ page, request }, info) => {
  oracle('CL-68');
  const ord = await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  await H(page).locator('button').first().click();
  await H(page).getByRole('link', { name: 'EShop' }).click();
  await page.goto('/profile');
  await page.waitForTimeout(1500);
  const txt = await page.locator('main').innerText();
  const leak = [USER.email, 'Test User', `#${ord.pending}`].filter(s => txt.includes(s));
  obs(info, `main sau đăng xuất: "${txt.slice(0, 80)}"`);
  soft(leak.length === 0, `còn thấy: ${leak.join(', ')}`);
});
test('CL-57 Bảng đơn hiển thị đủ thông tin', async ({ page, request }, info) => {
  oracle('CL-57');
  const ord = await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  const row = await orderRow(page, ord.pending);
  await row.waitFor({ timeout: 5000 }).catch(() => {});
  const cells = (await row.locator('td').allInnerTexts()).map(s => s.trim());
  obs(info, `dòng đơn #${ord.pending}: ${JSON.stringify(cells)}`);
  soft(cells.some(c => c.includes(String(ord.pending))), 'thiếu mã đơn');
  soft(cells.some(c => /\d{1,4}[/.-]\d{1,2}[/.-]\d{1,4}/.test(c)), 'thiếu ngày đặt');
  soft(cells.some(c => /\d/.test(c) && c.includes('₫')), 'thiếu tổng tiền');
  soft(cells.length >= 4 && cells.filter(Boolean).length >= 4, 'thiếu trạng thái');
});
const colIndex = async (page: Page, name: string) => (await page.locator('table thead th').allInnerTexts()).findIndex(t => t.includes(name));
test('CL-08 Tổng tiền dùng ký hiệu ₫ và phân cách hàng nghìn', async ({ page, request }, info) => {
  const o = oracle('CL-08');
  await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  await page.locator('table').waitFor({ timeout: 5000 }).catch(() => {});
  const i = await colIndex(page, 'Tổng tiền');
  if (i < 0) { blocked(info, 'Blocked – bảng đơn không có cột Tổng tiền'); test.skip(true); }
  const vals = (await page.locator(`table tbody tr td:nth-child(${i + 1})`).allInnerTexts()).map(s => s.trim());
  const bad = vals.filter(v => !new RegExp(o.re).test(v));
  obs(info, `${info.project.name} Tổng tiền: ${JSON.stringify(vals)} (so kiểu phân cách giữa nền tảng khi gộp)`);
  soft(bad.length === 0, `sai định dạng: ${JSON.stringify(bad)}`);
});
test('CL-09 Ngày đặt hiển thị nhất quán theo định dạng Việt Nam', async ({ page, request }, info) => {
  const o = oracle('CL-09');
  await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  await page.locator('table').waitFor({ timeout: 5000 }).catch(() => {});
  const i = await colIndex(page, 'Ngày');
  if (i < 0) { blocked(info, 'Blocked – bảng đơn không có cột Ngày đặt'); test.skip(true); }
  const vals = (await page.locator(`table tbody tr td:nth-child(${i + 1})`).allInnerTexts()).map(s => s.trim());
  const bad = vals.filter(v => !new RegExp(o.re).test(v));
  obs(info, `${info.project.name} Ngày đặt: ${JSON.stringify(vals)} (so giữa nền tảng khi gộp)`);
  soft(bad.length === 0, `không phải dd/mm/yyyy: ${JSON.stringify(bad)}`);
});
test('CL-58 Trạng thái tiếng Việt và phân biệt màu', async ({ page, request }, info) => {
  const o = oracle('CL-58');
  const ord = await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  const seen: { st: string; text: string; bg: string }[] = [];
  for (const st of ['pending', 'confirmed', 'shipping', 'delivered', 'canceled'] as const) {
    const row = await orderRow(page, ord[st]);
    await row.waitFor({ timeout: 5000 }).catch(() => {});
    const badge = row.locator('span').first();
    seen.push({ st, text: (await badge.innerText()).trim(), bg: (await style(badge, ['background-color']))['background-color'] });
  }
  obs(info, JSON.stringify(seen));
  for (const s of seen) soft(!o.raw.includes(s.text) && /[^\x00-\x7F]/.test(s.text), `${s.st}: nhãn "${s.text}" không phải tiếng Việt`);
  soft(new Set(seen.map(s => s.bg)).size === 5, 'có 2 trạng thái trùng màu');
  await shot(page.locator('table'), info, 'CL-58');
});
test('CL-59 Không cho người dùng huỷ đơn ở trạng thái không được huỷ', async ({ page, request }, info) => {
  const o = oracle('CL-59');
  const ord = await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  for (const st of ['pending', 'confirmed', 'shipping', 'delivered', 'canceled'] as const) {
    const row = await orderRow(page, ord[st]);
    await row.waitFor({ timeout: 5000 }).catch(() => {});
    const btn = row.getByRole('button', { name: o.label });
    const usable = (await btn.count()) > 0 && (await btn.first().isEnabled());
    obs(info, `${st} (#${ord[st]}): nút "${o.label}" dùng được = ${usable}`);
    const allowed = st === 'pending' || st === 'confirmed';
    soft(usable === allowed, allowed ? `${st}: không có nút huỷ` : `${st}: nút "${o.label}" dùng được`);
  }
  await shot(page.locator('table'), info, 'CL-59');
});
test('CL-05 Nút nguy hiểm/huỷ bỏ màu đỏ', async ({ page, request }, info) => {
  const o = oracle('CL-05');
  const ord = await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  const logout = (await style(H(page).locator('button').first(), ['background-color']))['background-color'];
  const row = await orderRow(page, ord.pending); await row.waitFor({ timeout: 5000 }).catch(() => {});
  const cancel = (await row.getByRole('button', { name: 'Hủy đơn' }).count()) ? (await style(row.getByRole('button', { name: 'Hủy đơn' }), ['background-color']))['background-color'] : 'không có nút';
  obs(info, `Đăng xuất: ${logout}; Hủy đơn: ${cancel}`);
  soft(inHue(logout, o.hue), `nút Đăng xuất màu ${logout}`);
  soft(inHue(cancel, o.hue), `nút Hủy đơn màu ${cancel}`);
});
test('CL-04 Nút hành động tích cực màu xanh dương', async ({ page, request }, info) => {
  const o = oracle('CL-04');
  const got: Record<string, string> = {};
  const bg = async () => (await style(submitBtn(page), ['background-color']))['background-color'];
  await page.goto('/login'); got['Đăng nhập'] = await bg();
  await page.goto('/forgot-password'); got['Lấy mã OTP'] = await bg();
  await forgotStep1(page); got['Đặt lại mật khẩu'] = await bg();
  await loginByToken(page, request, '/profile'); got['Cập nhật'] = await bg();
  obs(info, `${JSON.stringify(got)} (dải hue ${o.hue.join('–')}°)`);
  for (const [k, v] of Object.entries(got)) soft(inHue(v, o.hue), `nút ${k} màu ${v}`);
});
test('CL-11 Thứ tự Tab theo vị trí hiển thị – Hồ sơ', async ({ page, request }, info) => {
  const o = oracle('CL-11');
  await ensureOrders(request);
  await loginByToken(page, request, o.page);
  await page.locator('table').waitFor({ timeout: 5000 }).catch(() => {});
  const seq = await tabWalk(page, 60), all = await interactive(page);
  const v = orderViolations(seq, o.tol), miss = all.filter(a => !seq.some(s => s.key === a.key));
  obs(info, `chuỗi Tab: ${fmtSeq(seq)}`);
  soft(v.length === 0, `nhảy ngược theo toạ độ: ${v.join('; ')}`);
  soft(miss.length === 0, `bỏ qua: ${fmtSeq(miss)}`);
});
test('CL-15 Bố cục không vỡ ở màn hình hẹp', async ({ page, request }, info) => {
  const o = oracle('CL-15');
  await ensureOrders(request);
  await page.setViewportSize({ width: o.width, height: o.height });
  await loginByToken(page, request, '/profile');
  await page.locator('table').waitFor({ timeout: 5000 }).catch(() => {});
  const w = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
  obs(info, `scrollWidth=${w.sw}, clientWidth=${w.cw} (chồng lấn/bị cắt: SV xem ảnh)`);
  soft(w.sw <= w.cw, `có thanh cuộn ngang toàn trang (${w.sw} > ${w.cw})`);
  await shot(page, info, 'CL-15');
});
test('CL-63 Có trạng thái đang tải khi lấy lịch sử đơn', async ({ page, request }, info) => {
  const o = oracle('CL-63');
  onlyOn(info, o.only);
  await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  await slow3G(page);
  let pending = true, emptyWhilePending = false, loader = false;
  page.on('requestfinished', r => { if (r.url().includes('/api/orders/my-orders')) pending = false; });
  await page.reload({ waitUntil: 'commit' });
  for (let i = 0; i < 300 && !(await page.locator('table').count()); i++) {
    const panel = page.locator('main div', { has: page.locator('h2', { hasText: 'Lịch sử đơn' }) }).last();
    if (await panel.count()) {
      const t = await panel.innerText().catch(() => '');
      if (pending && t.split('\n').filter(s => s.trim()).length > 1 && !(await panel.locator('table').count())) emptyWhilePending = true;
      if (await panel.locator('[aria-busy="true"], [role="progressbar"], [class*="spin"], [class*="load"]').count()) loader = true;
      if (/đang tải|loading/i.test(t)) loader = true;
    }
    await page.waitForTimeout(100);
  }
  obs(info, `empty state hiện khi chưa có dữ liệu: ${emptyWhilePending}; chỉ báo tải: ${loader}`);
  soft(!emptyWhilePending, 'hiện empty state rồi mới hiện bảng');
  soft(loader, 'không có chỉ báo đang tải (SV xác nhận nếu chỉ báo không nhận diện được bằng DOM)');
});
test('CL-60 Huỷ đơn có hộp xác nhận', async ({ page, request }, info) => {
  const o = oracle('CL-60');
  const ord = await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  const d = dialogs(page, 'dismiss');
  const row = await orderRow(page, ord.cancelA); await row.waitFor({ timeout: 5000 }).catch(() => {});
  await row.getByRole('button', { name: o.label }).click();
  await page.waitForTimeout(1500);
  const st = await orderStatus(request, ord.cancelA);
  obs(info, `hộp thoại: ${JSON.stringify(d.map(x => `${x.type}: ${x.message}`))}; trạng thái đơn sau khi chọn "không": ${st}`);
  soft(d.some(x => x.type === 'confirm'), 'không có hộp xác nhận');
  soft(st === 'pending', `đơn bị huỷ ngay (trạng thái ${st})`);
});
test('CL-61 Sau huỷ, trạng thái cập nhật ngay', async ({ page, request }, info) => {
  const o = oracle('CL-61');
  const ord = await ensureOrders(request);
  await loginByToken(page, request, '/profile');
  dialogs(page, 'accept');
  const row = await orderRow(page, ord.cancelB); await row.waitFor({ timeout: 5000 }).catch(() => {});
  const before = (await row.innerText()).replace(/\s+/g, ' ');
  await row.getByRole('button', { name: o.label }).click();
  const gone = await expect(row.getByRole('button', { name: o.label })).toHaveCount(0, { timeout: o.waitMs }).then(() => true, () => false);
  const after = (await row.innerText()).replace(/\s+/g, ' ');
  obs(info, `dòng trước: "${before}"; sau ${o.waitMs} ms (không tải lại): "${after}"`);
  soft(gone && /hủy|huỷ/i.test(after) && after !== before, 'cần tải lại mới thấy thay đổi');
});

// ============ 5. Chống gửi trùng (mạng chậm, P1) ============
test('CL-53 Có chỉ báo đang xử lý và chống gửi trùng', async ({ page, request }, info) => {
  const o = oracle('CL-53');
  onlyOn(info, o.only);
  await fillLogin(page, USER.email, USER.password);
  await slow3G(page);
  const c = countRequests(page, '/api/login');
  const b = submitBtn(page), label0 = (await b.innerText()).trim();
  await b.click();
  await page.waitForTimeout(300);
  const st = await b.evaluate((e: any) => ({ disabled: e.disabled, busy: e.getAttribute('aria-busy'), text: e.innerText.trim() })).catch(() => ({ disabled: false, busy: null, text: '(nút biến mất)' }));
  for (let i = 1; i < o.clicks; i++) await b.click({ timeout: 1000, force: true }).catch(() => {});
  await page.waitForTimeout(10_000);
  obs(info, `trong lúc chờ: ${JSON.stringify(st)} (chữ ban đầu "${label0}"); ${c.n} request /api/login sau ${o.clicks} lần bấm`);
  soft(st.disabled || st.busy === 'true' || st.text !== label0, 'không có chỉ báo đang xử lý trên nút (SV xác nhận chỉ báo khác)');
  soft(c.n === 1, `phát sinh ${c.n} request /api/login`);
  await resetAttempts(request);
});

// ============ 6. Item SV ============
test('SV-01 Hiển thị focus rõ ràng khi duyệt bằng bàn phím', async ({ page, request }, info) => {
  const o = oracle('SV-01');
  for (const p of o.pages) {
    if (p === '/profile') await loginByToken(page, request, p); else await page.goto(p);
    const seq = await tabWalk(page);
    await page.evaluate(() => (document.activeElement as HTMLElement | null)?.blur?.());
    const plain = await page.evaluate(keys => keys.map(k => { const i = Number(k.split('#')[1]); const e = document.querySelectorAll('*')[i] as HTMLElement; const cs = getComputedStyle(e); return `${cs.outlineStyle} ${cs.outlineWidth} ${cs.outlineColor} | ${cs.boxShadow} | ${cs.borderColor}`; }), seq.map(s => s.key));
    const same = seq.filter((s, i) => s.outline === plain[i]);
    obs(info, `${p}: ${seq.length} control nhận focus, ${same.length} không đổi kiểu khi focus`);
    soft(same.length === 0, `${p}: không thấy viền focus ở ${fmtSeq(same)}`);
  }
});
test('SV-02 Dán dữ liệu vào ô nhập (phần tự động)', async ({ page, context }, info) => {
  const o = oracle('SV-02');
  onlyOn(info, o.only);
  await context.grantPermissions(['clipboard-read', 'clipboard-write'], { origin: 'http://localhost:5173' });
  await page.goto('/login');
  await page.evaluate(t => navigator.clipboard.writeText(t), o.paste);
  for (const i of [0, 1]) {
    const inp = loginInputs(page).nth(i);
    await inp.fill(''); await inp.focus(); await page.keyboard.press('Control+V');
    const v = await inp.inputValue();
    obs(info, `/login ô ${i + 1}: sau Ctrl+V = "${v}"`);
    soft(v === o.paste, `/login ô ${i + 1} không nhận dữ liệu dán`);
  }
});
test('SV-03 Trả focus về đúng ô bị lỗi sau khi submit thất bại', async ({ page, request }, info) => {
  const o = oracle('SV-03');
  const focused = (l: any) => l.evaluate((e: Element) => e === document.activeElement);
  try {
    await fillLogin(page, USER.email, o.wrong); dialogs(page);
    await submitBtn(page).click(); await page.waitForTimeout(1500);
    const a = await focused(loginInputs(page).nth(1));
    await resetAttempts(request);
    const code = await forgotStep1(page); dialogs(page);
    await page.locator('form input').nth(0).fill(code ?? '');
    await byLabel(page, /mật khẩu mới/i).fill(o.weak);
    await submitBtn(page).click(); await page.waitForTimeout(1000);
    const b = await focused(byLabel(page, /mật khẩu mới/i));
    await loginByToken(page, request, '/profile'); dialogs(page);
    await byLabel(page, 'Số điện thoại').fill(o.phone);
    await submitBtn(page).click(); await page.waitForTimeout(1000);
    const c = await focused(byLabel(page, 'Số điện thoại'));
    obs(info, `focus về ô lỗi – Đăng nhập (Mật khẩu): ${a}; Quên MK B2 (Mật khẩu mới): ${b}; Hồ sơ (SĐT): ${c}`);
    soft(a, 'Đăng nhập: focus không về ô Mật khẩu');
    soft(b, 'Quên mật khẩu B2: focus không về ô Mật khẩu mới');
    soft(c, 'Hồ sơ: focus không về ô Số điện thoại');
  } finally { await resetAttempts(request); await restorePassword(request); await restoreProfile(request); }
});
test('SV-04 Độ tương phản màu chữ so với nền (phần tự động)', async ({ page, request }, info) => {
  const o = oracle('SV-04');
  for (const p of o.pages) {
    if (p === '/profile') await loginByToken(page, request, p); else await page.goto(p);
    const low = (await textColors(page)).map(t => ({ ...t, r: contrast(rgb(t.fg), rgb(t.bg)) })).filter(t => t.text && t.r < o.min);
    obs(info, `${p}: ${low.length} phần tử < ${o.min}:1 ${JSON.stringify(low.map(t => `${t.text} ${t.r.toFixed(2)}`))}`);
    soft(low.length === 0, `${p}: tương phản < ${o.min}:1 ở ${low.map(t => `"${t.text}" ${t.r.toFixed(2)}`).join(', ')}`);
  }
});
test('SV-05 Kích thước vùng tương tác của nút và link', async ({ page, request }, info) => {
  const o = oracle('SV-05');
  const check = async (name: string, l: any) => {
    const b = await l.boundingBox();
    obs(info, `${name}: ${b ? `${Math.round(b.width)}×${Math.round(b.height)}` : 'không thấy'}`);
    soft(!!b && b.width >= o.min && b.height >= o.min, `${name} < ${o.min}×${o.min} px`);
  };
  await page.goto('/login');
  await check('Sign In', submitBtn(page));
  await check('Quên mật khẩu?', page.getByText('Quên mật khẩu?', { exact: true }));
  await check('Đăng ký ngay', page.getByText('Đăng ký ngay', { exact: true }));
  await page.goto('/forgot-password'); await check('Lấy mã OTP', submitBtn(page));
  await loginByToken(page, request, '/profile'); await check('Cập nhật', submitBtn(page));
});
test('SV-06 Chống gửi trùng khi nhấp đúp ở mạng bình thường', async ({ page, request }, info) => {
  const o = oracle('SV-06');
  try {
    await page.goto('/forgot-password');
    const c1 = countRequests(page, '/api/forgot-password');
    await page.locator('form input').first().fill(USER.email);
    await submitBtn(page).dblclick(); await page.waitForTimeout(1500);
    obs(info, `Lấy mã OTP: ${c1.n} request`);
    soft(c1.n === 1, `Lấy mã OTP: ${c1.n} request`);
    const code = /\b(\d{4,8})\b/.exec(await page.locator('main').innerText())?.[1] ?? '';
    const d2 = dialogs(page), c2 = countRequests(page, '/api/reset-password');
    await page.locator('form input').nth(0).fill(code);
    await byLabel(page, /mật khẩu mới/i).fill(o.pw);
    const cf = byLabel(page, /xác nhận/i); if (await cf.count()) await cf.fill(o.pw);
    await submitBtn(page).dblclick(); await page.waitForTimeout(1500);
    obs(info, `Đặt lại mật khẩu: ${c2.n} request, ${d2.length} hộp thoại`);
    soft(c2.n <= 1 && d2.length <= 1, `Đặt lại mật khẩu: ${c2.n} request, ${d2.length} hộp thoại`);
    await restorePassword(request);
    await loginByToken(page, request, '/profile');
    const d3 = dialogs(page);
    const c3 = { n: 0 }; page.on('request', r => { if (r.url().includes('/api/users/me') && r.method() === 'PUT') c3.n++; });
    await byLabel(page, 'Số điện thoại').fill('0912345678');
    await submitBtn(page).dblclick(); await page.waitForTimeout(1500);
    obs(info, `Cập nhật: ${c3.n} request PUT, ${d3.length} hộp thoại`);
    soft(c3.n === 1 && d3.length <= 1, `Cập nhật: ${c3.n} request PUT, ${d3.length} hộp thoại`);
  } finally { await restorePassword(request); await restoreProfile(request); }
});
