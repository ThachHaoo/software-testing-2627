/**
 * MẪU spec data-driven (bước 3, v2) — HW04/tests/<X_FRnn>.spec.ts. Cấu trúc theo spec chính thức C_FR15.spec.ts @2e9e454.
 * - Lặp theo file data; tiêu đề "<tc_id> <title>"; giá trị vào từ c.inputs, oracle từ c.expected (nguyên văn + sha1).
 * - Câu chữ/từ khoá/selector KHÔNG có trong expected → assumptions của file data (giả định SV), không gõ cứng ở đây.
 * - ≥ 3 kiểu assertion: trạng thái UI (toBeVisible/toHaveURL), nội dung (toHaveText/toContainText),
 *   oracle dữ liệu API trước/sau (toEqual), đếm/giá trị (toHaveCount/toHaveValue/toBe). Dùng expect.soft.
 * - Không mode serial; không catch rỗng; không waitForTimeout; không Promise.race; thao tác chính ĐÚNG số lần procedure ghi.
 * Thay mọi chỗ __…__ ở bước 3 (selector lấy từ mã UI thật / page object bước 2).
 */
import {
  test, expect, loadData, assumption, fill, esc, resetDb, guardWorkers, blocked, step, until, settle, netLog, API,
} from './fixtures/ddt';

const FEATURE = 'X_FRnn';
const DATA = loadData(FEATURE);            // ném lỗi nếu sha1(expected) lệch → cả file không chạy
const COL = { email: '__Tên cột trong inputs__' };          // tên cột = khoá trong c.inputs (từ HW02)
const SEL = { submit: '__nhãn nút thật trong mã UI__' };    // selector lấy từ mã UI (nhãn/role/placeholder), không bịa
const PAGE_URL = '/__đường dẫn màn hình__';
const API_PREFIX = `${API}/api/__resource__`;
const ACTION = { method: 'POST' };                          // request mà thao tác chính gửi khi form hợp lệ

/** Oracle đọc từ expected. Không xác định được loại kết quả → NÉM LỖI (không đoán). Ý không tự động được → unmapped. */
type Oracle = { kind: 'accept' | 'reject'; msg?: RegExp; unmapped: string[] };
function parseExpected(expected: string): Oracle {
  // Tách câu: chỉ cắt ở '.'/';' theo sau là khoảng trắng hoặc hết chuỗi (giữ số thập phân "0.1").
  const parts = expected.split(/[.;](?:\s|$)/).map(s => s.trim()).filter(Boolean);
  const o: Partial<Oracle> & { unmapped: string[] } = { unmapped: [] };
  for (const p of parts) {
    // Mẫu câu lấy từ chính expected của feature; chuỗi dựng RegExp phải esc(); nhiều nhánh: ^(?:a|b)
    const ok = /^__mẫu câu chấp nhận__/i.exec(p);
    const ko = /^__mẫu câu từ chối__ '([^']+)'/i.exec(p);
    if (ok) o.kind = 'accept';
    else if (ko) { o.kind = 'reject'; o.msg = new RegExp(`^(?:${esc(ko[1])})$`); }
    else o.unmapped.push(p);
  }
  if (!o.kind) throw new Error(`[${FEATURE}] không đọc được loại kết quả từ expected: "${expected}"`);
  return o as Oracle;
}

test.beforeAll(async ({}, testInfo) => {
  testInfo.setTimeout(120_000);
  guardWorkers(testInfo, FEATURE);         // resetDb không an toàn khi song song
  resetDb();                               // tiền điều kiện suite: CSDL seed sạch
});

for (const c of DATA.testcases) {
  test(`${c.tc_id} ${c.title}`, async ({ page, api, dialogs }) => {
    const info = test.info();
    const ann = (type: string, description: string) => info.annotations.push({ type, description });
    ann('expected', c.expected);
    ann('hw02', `${c.hw02.status}${c.hw02.bug_id ? ' ' + c.hw02.bug_id : ''}`);
    const ts = Date.now();
    const o = parseExpected(c.expected);
    for (const u of o.unmapped) ann('oracle không tự động', u);

    // 1. Oracle dữ liệu TRƯỚC (API)
    const before = await (await api.get(API_PREFIX)).json();

    // 2. Điều hướng + nhập theo c.inputs (quá hạn → Blocked; lỗi khác ném tiếp)
    await step('Mở màn hình', () => page.goto(PAGE_URL));
    const field = page.getByLabel(COL.email);
    if (!(await field.count())) blocked(`UI không có ô '${COL.email}' (trường đặc tả có, UI không có)`);
    await field.fill(fill(c.inputs[COL.email], ts));

    // 3. Thao tác ĐÚNG 1 lần; gắn log mạng TRƯỚC khi bấm; chờ phản hồi/điều kiện cụ thể
    const net = netLog(page, API_PREFIX);
    const n0 = dialogs.length;
    const msgSel = assumption(DATA, 'page_message_selector').value;   // giả định SV: khối thông báo trên trang
    const pageMessages = () => page.locator(msgSel).allTextContents();
    const msgBefore = await pageMessages();
    const valid = await page.locator('form').evaluate((f: HTMLFormElement) => f.checkValidity());
    await page.getByRole('button', { name: SEL.submit }).click();      // ĐÚNG 1 lần
    if (valid) {
      await until(`chờ ${ACTION.method} ${API_PREFIX}`, () => net.some(x => x.method === ACTION.method));
      await net.find(x => x.method === ACTION.method)!.done;           // body đã về → mới đọc dữ liệu SAU
    }
    await settle(page);

    // 4. Quan sát (ghi dữ kiện, chưa kết luận) → ảnh <TC>_after-* chụp SAU khi đo xong
    const newDialogs = dialogs.slice(n0);
    const pageMsgs = (await pageMessages()).map(s => s.trim()).filter(m => m && !msgBefore.includes(m));
    ann('quan sát sau thao tác', JSON.stringify({
      'hộp thoại': newDialogs.map(d => d.message), 'thông báo mới trên trang': pageMsgs,
      request: net.map(x => `${x.method} ${x.url.replace(API, '')} → ${x.status}`),
    }));
    await info.attach(`${c.tc_id}_after-submit`, { body: await page.screenshot(), contentType: 'image/png' });

    // 5. Oracle dữ liệu SAU (API) — chỉ gọi sau khi đã có phản hồi request ở bước 3
    const after = await (await api.get(API_PREFIX)).json();

    // ---- Oracle ----
    if (o.kind === 'accept') {
      expect.soft(after.length, 'có thêm đúng 1 bản ghi').toBe(before.length + 1);
      await expect.soft(page, 'điều hướng sau khi thành công').toHaveURL(/__url sau khi thành công__/);
    } else {
      expect.soft(after, 'dữ liệu SAU = TRƯỚC').toEqual(before);
      if (o.msg) {
        const hit = pageMsgs.filter(m => o.msg!.test(m));
        expect.soft(hit, `thông báo khớp expected ${o.msg}`).not.toEqual([]);
      } else if (newDialogs.length && !pageMsgs.length) {
        // Không đếm hộp thoại (có thể là "thành công") là "thông báo lỗi" khi chưa có giả định SV phân loại nội dung.
        ann('oracle thông báo yếu', `chỉ có hộp thoại ${JSON.stringify(newDialogs.map(d => d.message))} — chưa có giả định SV phân loại, SV xét`);
      }
    }
  });
}
