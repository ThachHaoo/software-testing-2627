/**
 * A_FR01 – FR-01 Đăng ký tài khoản (web /register). Skill playwright-ddt-automation, bước 3.
 * Data-driven: mọi giá trị vào và oracle đọc từ HW04/data/A_FR01.json (expected nguyên văn HW02 + sha1, kiểm khi nạp).
 * Oracle được ĐỌC từ chuỗi expected (oracleOf) — spec không chứa hằng dữ liệu test.
 * Assertion: trạng thái UI (toHaveURL/toBeVisible), nội dung thông báo (toHaveText/toContainText),
 * oracle dữ liệu API trước/sau (toEqual), đếm/giá trị (toHaveCount/toHaveValue). Dùng expect.soft.
 */
import { test, expect, loadData, fill, resetDb, blocked, diffUsers, type User } from './fixtures/a_fr01';
import type { Case } from './fixtures/ddt';
import { WEB } from './fixtures/ddt';

const DATA = loadData('A_FR01');           // ném lỗi nếu sha1(expected) lệch → cả file không chạy
const COL = { name: 'Họ Tên', email: 'Email', pwd: 'Mật khẩu', conf: 'Xác nhận mật khẩu', inDb: 'Email trong CSDL', extra: 'Thao tác riêng' };

type Oracle = {
  kind: 'success' | 'reject';
  url?: string;                         // "chuyển tới /login" | "URL vẫn là /register"
  vmField?: string;                     // A16: "ô 'X' có validationMessage không rỗng"
  user?: { name: string; email: string };   // "đúng 1 user mới, có name '…' và email '…'"
  hint?: RegExp[];                      // "Hệ thống báo <trường> thiếu <điều kiện>" → thông báo phải nói về các ý này
  seedKept: boolean;                    // "user seed không bị sửa"
  relogin: boolean;                     // "đăng nhập lại … thành công"
};

/** Escape chuỗi lấy từ expected trước khi dựng RegExp (., (, +, ? … giữ nghĩa chữ). */
const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Đọc oracle từ expected nguyên văn. Không nhận dạng được loại kết quả → ném lỗi (không đoán). */
function oracleOf(c: Case, ts: number): Oracle {
  const e = fill(c.expected, ts);
  const success = /^(Không có thông báo lỗi|Đăng ký thành công)/.test(e);
  const reject = /Có thông báo lỗi|không tạo tài khoản|không có user mới/.test(e);
  if (success === reject) throw new Error(`${c.tc_id}: không xác định được loại kết quả từ expected: ${e}`);
  const o: Oracle = { kind: success ? 'success' : 'reject', seedKept: /user seed không bị sửa/.test(e), relogin: /đăng nhập lại .*thành công/.test(e) };
  o.url = (/chuyển tới (\/[\w-]*)/.exec(e) ?? /URL vẫn là (\/[\w-]*)/.exec(e))?.[1];
  o.vmField = /ô '([^']+)' có validationMessage/.exec(e)?.[1];
  const u = /name '([^']*)' và email '([^']*)'/.exec(e);
  if (u) o.user = { name: u[1], email: u[2] };
  else if (success) o.user = { name: c.inputs[COL.name], email: fill(c.inputs[COL.email], ts) };   // "Đăng ký thành công" (TS-SV)
  const h = /báo (mật khẩu|email|họ tên) thiếu ([^;]+)/i.exec(e);
  if (h) o.hint = [new RegExp(esc(h[1]), 'i'), new RegExp(esc(h[2].trim()), 'i')];
  return o;
}

const pick = (us: User[]) => us.map(u => ({ name: u.name, email: u.email }));
const WAIT = 10_000;                       // chờ phản hồi sau khi bấm Đăng Ký; quá hạn → Blocked
const NO_POST = 2_000;                     // cửa sổ xác nhận "không có POST /api/register"
const isRegister = (res: { request(): { method(): string }; url(): string }) =>
  res.request().method() === 'POST' && res.url().endsWith('/api/register');

test.beforeAll(async ({}, testInfo) => {
  testInfo.setTimeout(120_000);
  // resetDb() restart backend dùng chung → chạy song song (nhiều worker) sẽ restart đè lên nhau, xoá dữ liệu của worker khác
  if (testInfo.config.workers > 1)
    throw new Error(`[A_FR01] workers = ${testInfo.config.workers}: resetDb không an toàn khi chạy song song — chạy với --workers=1`);
  resetDb();                               // tiền điều kiện suite: CSDL seed sạch (A13)
});

for (const c of DATA.testcases) {
  test(`${c.tc_id} ${c.title}`, async ({ page, registerPage: r, loginPage: l, users }) => {
    const ts = Date.now();
    const o = oracleOf(c, ts);
    const v = (k: string) => fill(c.inputs[k], ts);
    test.info().annotations.push(
      { type: 'expected', description: fill(c.expected, ts) },
      { type: 'hw02', description: `${c.hw02.status}${c.hw02.bug_id ? ' ' + c.hw02.bug_id : ''}` });

    // Tiền điều kiện "Email trong CSDL: chưa có" — vi phạm thì không kiểm được đúng mục đích
    if (/chưa có/.test(c.inputs[COL.inDb] ?? 'chưa có') && users.before.some(u => u.email === v(COL.email)))
      blocked(`email ${v(COL.email)} đã có trong CSDL trước khi chạy`);

    const posts: string[] = [];
    page.on('request', req => { if (req.method() === 'POST' && req.url().endsWith('/api/register')) posts.push(req.url()); });

    // Bước 2–3: mở form, các ô trống, gõ từng ô
    await r.open();
    for (const f of [r.name(), r.email(), r.password()]) await expect.soft(f).toHaveValue('');
    await r.type(r.name(), v(COL.name));
    await r.type(r.email(), v(COL.email));
    await r.type(r.password(), v(COL.pwd));
    if (COL.conf in c.inputs) {
      if (await r.confirm().count()) await r.type(r.confirm(), v(COL.conf));
      else test.info().annotations.push({ type: 'A17', description: 'form không có ô Xác nhận mật khẩu: bỏ qua bước nhập V5' });
    }
    await expect.soft(r.name()).toHaveValue(v(COL.name));
    await expect.soft(r.email()).toHaveValue(v(COL.email));
    await expect.soft(r.password()).toHaveValue(v(COL.pwd));

    // Bước 4: bấm "Đăng Ký" đúng một lần, xác định nhánh phản hồi, đồng bộ với POST /api/register
    const regRes = page.waitForResponse(isRegister, { timeout: WAIT }).catch(() => null);   // đặt trước click để không lỡ phản hồi
    await r.submit.click();
    let branch: string;
    if (!(await page.locator('form').evaluate((f: HTMLFormElement) => f.checkValidity()))) {
      branch = 'trình duyệt chặn';                    // A16: ô required trống → trình duyệt không submit
    } else {
      branch = await Promise.any([
        page.waitForURL(u => !u.pathname.endsWith('/register'), { timeout: WAIT }).then(() => 'điều hướng'),
        r.error.waitFor({ state: 'visible', timeout: WAIT }).then(() => 'hộp lỗi'),
      ]).catch(() => 'timeout');
    }
    // Có POST → chờ phản hồi (backend ghi CSDL xong mới trả lời); chưa có → xác nhận không có POST trong NO_POST ms
    if (!posts.length) await page.waitForRequest(req => req.method() === 'POST' && req.url().endsWith('/api/register'), { timeout: NO_POST }).catch(() => null);
    const res = posts.length ? await regRes : null;
    test.info().annotations.push({ type: 'phản hồi', description: `${branch}; POST /api/register: ${posts.length} lần${res ? ` (HTTP ${res.status()})` : ''}` });
    if (branch === 'timeout') blocked(`không có phản hồi sau ${WAIT} ms (không điều hướng, không hộp lỗi, form hợp lệ)`);
    if (posts.length && !res) blocked(`đã gửi POST /api/register nhưng không nhận phản hồi sau ${WAIT} ms`);

    // Bước 5: UI
    if (o.url) await expect.soft(page, 'URL sau khi bấm Đăng Ký').toHaveURL(new RegExp(`${esc(o.url)}$`));
    if (o.kind === 'success') {
      await expect.soft(r.error, 'không có thông báo lỗi').toHaveCount(0);
    } else {
      const vm = o.vmField ? await r.validationMessage(r.field(o.vmField)) : '';
      if (vm) {                                         // A16: trình duyệt chặn, không gửi POST
        expect.soft(vm, `validationMessage ô '${o.vmField}'`).not.toEqual('');
        expect.soft(posts, 'A16: không gửi POST /api/register').toEqual([]);
      } else {
        if (!o.hint) test.info().annotations.push({ type: 'oracle thông báo yếu', description: 'expected không nêu ý của thông báo lỗi → chỉ kiểm hộp lỗi hiện và có chữ' });
        await expect.soft(r.error, 'hộp lỗi đỏ trên form').toBeVisible();
        await expect.soft(r.error, 'hộp lỗi có nội dung').toHaveText(/\S/);
        for (const h of o.hint ?? []) await expect.soft(r.error, `thông báo nói về ${h.source}`).toContainText(h);
      }
    }

    // Bước 6: oracle dữ liệu qua API (so với danh sách chụp ở bước 1)
    const d = diffUsers(users.before, await users.list());
    if (o.kind === 'success') expect.soft(pick(d.added), 'đúng 1 user mới').toEqual([o.user]);
    else expect.soft(pick(d.added), 'không có user mới').toEqual([]);
    if (o.seedKept) {
      expect.soft(pick(d.changed), 'user seed không bị sửa').toEqual([]);
      expect.soft(pick(d.removed), 'user seed không bị xoá').toEqual([]);
    }

    // "Thao tác riêng": đăng nhập lại bằng đúng chuỗi mật khẩu đã đăng ký
    if (o.relogin) {
      await l.open();
      await l.login(v(COL.email), v(COL.pwd));
      await expect.soft(page, 'đăng nhập xong về trang chủ').toHaveURL(`${WEB}/`);
      await expect.soft(l.error, 'không có lỗi đăng nhập').toHaveCount(0);
      expect.soft(await l.token(), 'có token trong localStorage').not.toBeNull();
    }
  });
}
