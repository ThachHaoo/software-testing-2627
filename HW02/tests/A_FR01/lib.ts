/**
 * Helper cho test FR-01 (HW02/A_FR01). Mọi dữ liệu và Expected đọc từ ../../A_FR01/testcases.json —
 * file này chỉ chứa cách THỰC HIỆN procedure và cách KIỂM oracle, không chứa dữ liệu test.
 * Quy ước annotation (merge_results.py): "actual" = quan sát, "verdict" = Blocked/Not run khi không kiểm được đúng mục đích.
 */
import fs from 'fs';
import path from 'path';
import { test as base, expect, APIRequestContext, Page, TestInfo } from '@playwright/test';

export const API = 'http://localhost:3000';
export const WEB = 'http://localhost:5173';
export const ADMIN_WEB = 'http://localhost:5174';

export const data = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../../A_FR01/testcases.json'), 'utf-8'));
export const suites: Record<string, any> = Object.fromEntries(data.suites.map((s: any) => [s.id, s]));

// Tài khoản admin lấy từ tiền điều kiện của TS-DOM-API ("POST /api/login với admin@eshop.com / Admin123!").
const adminPre: string = suites['TS-DOM-API'].preconditions.find((p: string) => p.includes('/api/login'));
const adm = /với (\S+@\S+) \/ (\S+?)\s/.exec(adminPre)!;
export const ADMIN = { email: adm[1], password: adm[2] };
// Mật khẩu tài khoản seed test@eshop.com không có trong testcases.json → lấy từ SRS (../eshop-sut/README.md dòng 23).
export const SEED_USER = { email: 'test@eshop.com', password: 'Test1234!' };

export const COL = { name: 'Họ Tên', email: 'Email', pwd: 'Mật khẩu', conf: 'Xác nhận mật khẩu', extra: 'Thao tác riêng' };
export const MISSING = '— thiếu trường —';

/** Chuyển giá trị trong cột dữ liệu thành giá trị gửi đi (procedure TS-DOM-API bước 2). undefined = bỏ khoá khỏi body. */
export function materialize(v: string | undefined, ts: string): string | number | undefined {
  if (v === undefined || v === MISSING) return undefined;
  const num = /^số (\d+)$/.exec(v);
  if (num) return Number(num[1]);
  const long = /^Mật khẩu hợp lệ dài ([\d.]+) ký tự \(ví dụ '(.+)' \+ ([\d.]+) chữ '(.)'\)$/.exec(v);
  if (long) {
    const total = Number(long[1].replace(/\./g, ''));
    const s = long[2] + long[4].repeat(Number(long[3].replace(/\./g, '')));
    if (s.length !== total) throw new Error(`Không dựng được mật khẩu dài ${total} ký tự từ mô tả: ${v}`);
    return s;
  }
  return v.split('{ts}').join(ts);
}

export const sub = (s: string, ts: string) => (s ?? '').split('{ts}').join(ts);

// ---------------- CSDL qua API admin (oracle tương đối) ----------------
export type User = { id: number; name: string | null; email: string | null; role: string };

export async function adminToken(request: APIRequestContext): Promise<string> {
  const r = await request.post(`${API}/api/login`, { data: ADMIN });
  if (r.status() !== 200) throw new Error(`Không đăng nhập được admin ${ADMIN.email}: HTTP ${r.status()}`);
  return (await r.json()).token;
}

export async function listUsers(request: APIRequestContext, token: string): Promise<User[]> {
  const r = await request.get(`${API}/api/admin/users`, { headers: { Authorization: `Bearer ${token}` } });
  if (r.status() !== 200) throw new Error(`GET /api/admin/users trả HTTP ${r.status()}`);
  return r.json();
}

export function diffUsers(before: User[], after: User[]) {
  const ids = new Set(before.map(u => u.id));
  const added = after.filter(u => !ids.has(u.id));
  const removed = before.filter(u => !after.some(a => a.id === u.id));
  const changed = before.filter(u => {
    const a = after.find(x => x.id === u.id);
    return a && (a.name !== u.name || a.email !== u.email || a.role !== u.role);
  });
  return { added, removed, changed };
}

type Admin = { token: string; before: User[]; list: () => Promise<User[]> };

/**
 * Fixture `admin`: bước 1 của procedure (lưu danh sách user) + cleanup sau mỗi case kể cả khi Fail:
 * xoá mọi user mới so với bước 1. Xoá thất bại → annotation "cleanup", không đổi verdict (A19).
 */
export const test = base.extend<{ admin: Admin }>({
  admin: async ({ request }, use, testInfo) => {
    const token = await adminToken(request);
    const before = await listUsers(request, token);
    await use({ token, before, list: () => listUsers(request, token) });
    try {
      const fresh = await adminToken(request);
      const { added } = diffUsers(before, await listUsers(request, fresh));
      for (const u of added) {
        const r = await request.delete(`${API}/api/admin/users/${u.id}`, { headers: { Authorization: `Bearer ${fresh}` } });
        const still = (await listUsers(request, fresh)).some(x => x.id === u.id);
        if (r.status() !== 200 || still)
          testInfo.annotations.push({ type: 'cleanup', description: `Xoá user id ${u.id} thất bại (HTTP ${r.status()}, còn trong danh sách: ${still}) — A19` });
      }
    } catch (e) {
      testInfo.annotations.push({ type: 'cleanup', description: `Cleanup lỗi: ${(e as Error).message} — A19` });
    }
  },
});
export { expect };

// ---------------- Oracle đọc từ expected_result ----------------
export type Oracle = {
  kind: 'success' | 'reject';
  name?: string; email?: string;        // user mới phải có name/email này
  nameFromInput: boolean;               // "Họ Tên lưu nguyên văn/đúng" → so với cột Họ Tên
  field?: string;                       // "ô 'X' có validationMessage" (A16)
  hint?: RegExp;                        // SV: "Hệ thống báo email/mật khẩu …" → thông báo phải nói về trường này
  seedKept: boolean;                    // "user seed không bị sửa" / "không đổi" / "vẫn còn đủ dữ liệu"
  apiBody: boolean;                     // expected ghi rõ body {"message": "User registered successfully", "id": n}
  login: boolean;                       // "đăng nhập … thành công"
  role?: string;                        // "role 'user'"
  manual: string[];                     // phần expected không tự động hoá được
};

export function oracleOf(c: any, ts: string): Oracle {
  const e = sub(c.expected_result, ts);
  const reject = /HTTP 4xx|Có thông báo lỗi|báo .*(không hợp lệ|không có định dạng|thiếu|đã tồn tại)/.test(e);
  const o: Oracle = {
    kind: reject ? 'reject' : 'success',
    nameFromInput: /Họ Tên lưu (nguyên văn|đúng|và hiển thị)/.test(e),
    seedKept: /seed .*không bị sửa|không đổi|giữ nguyên|vẫn còn đủ dữ liệu/.test(e),
    apiBody: /User registered successfully/.test(e),
    login: /đăng nhập .*thành công/.test(e),
    manual: [],
  };
  const ne = /name '(.+?)' và email '(.+?)'/.exec(e);
  if (ne) { o.name = ne[1]; o.email = ne[2]; }
  const nl = /name lưu đúng '(.+?)'/.exec(e);
  if (nl) o.name = nl[1];
  const f = /ô '(.+?)' có validationMessage/.exec(e);
  if (f) o.field = f[1];
  const h = /báo (email|mật khẩu)/i.exec(e);
  if (h) o.hint = new RegExp(h[1], 'i');
  const role = /role '(\w+)'/.exec(e);
  if (role) o.role = role[1];
  if (/hiển thị đúng emoji/.test(e)) o.manual.push('"hiển thị đúng emoji": expected không nêu trang hiển thị → chỉ kiểm giá trị lưu trong CSDL, phần hiển thị SV kiểm tay');
  if (!reject && !/HTTP 200|Đăng ký thành công|Không có thông báo lỗi|Form dùng được/.test(e))
    throw new Error(`${c.id}: không nhận diện được oracle từ expected_result — cần SV xem lại: ${e}`);
  return o;
}

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

export const actual = (info: TestInfo, s: string) => info.annotations.push({ type: 'actual', description: s });
export const verdict = (info: TestInfo, v: 'Blocked' | 'Not run', why: string) => {
  info.annotations.push({ type: 'verdict', description: v });
  actual(info, `${v}: ${why}`);
};

// ---------------- UI: form Đăng ký ----------------
/** Ô nhập ngay sau nhãn (nhãn trong Register.jsx không gắn htmlFor). Nhãn có thể thêm '*' (FR-22.1). */
export const field = (page: Page, label: string) =>
  page.locator(`xpath=//label[starts-with(normalize-space(.), "${label}")]/following-sibling::input[1]`);
export const errorBox = (page: Page) => page.locator('div.bg-red-100');
export const submitBtn = (page: Page) => page.getByRole('button', { name: 'Đăng Ký', exact: true });

export async function validation(page: Page, label: string) {
  const loc = field(page, label);
  if (await loc.count() === 0) return null;
  return loc.evaluate((el: HTMLInputElement) => ({ invalid: el.matches(':invalid'), msg: el.validationMessage }));
}
