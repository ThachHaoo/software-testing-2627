# Chạy test tự động từ testcases.json

## Quy ước để `merge_results.py` gộp được

- **Tiêu đề test bắt đầu bằng mã TC**: `TC-FR01-03 Kiểm tra … khi …`.
- Ghi **Actual** bằng annotation `actual` (chuỗi quan sát được: chữ thông báo, URL sau submit, HTTP status + body rút gọn).
- Chụp màn hình cuối mỗi test và đính kèm (`testInfo.attach`) — đường dẫn được ghi vào `evidence`.
- Reporter JSON: `npx playwright test --reporter=list,json` với `PLAYWRIGHT_JSON_OUTPUT_NAME=results/<feature>.json`.
- Map trạng thái: `passed → Pass`, `failed/timedOut → Fail`, `skipped → Not run`, `interrupted → Blocked`.
- Mỗi lượt chạy ghi results riêng có timestamp (`results/<feature>_<yyyyMMdd-HHmmss>.json`) để không ghi đè lượt trước.
- Verdict SV đã chỉnh (status khác auto_status) được `merge_results.py` giữ nguyên; chỉ auto_status, actual_result, evidence được cập nhật. Ghi đè bằng `--force`.

## Khung spec đọc dữ liệu từ JSON (TypeScript)

```ts
import { test, expect } from '@playwright/test';
import data from '../A_FR01/testcases.json';

const cases = data.suites.flatMap((s: any) => s.cases.map((c: any) => ({ ...c, suite: s.id })));

for (const c of cases.filter((c: any) => c.layer !== 'Mobile')) {
  test(`${c.id} ${c.title}`, async ({ page, request }, testInfo) => {
    // 1. Thiết lập (dữ liệu sạch, đăng nhập…) theo preconditions
    // 2. Thực hiện theo procedure của suite với c.inputs
    // 3. Thu thập quan sát được -> actual
    const actual = '...';
    testInfo.annotations.push({ type: 'actual', description: actual });
    const shot = testInfo.outputPath(`${c.id}.png`);
    await page.screenshot({ path: shot, fullPage: true });
    await testInfo.attach('screenshot', { path: shot, contentType: 'image/png' });   // dùng path để merge_results ghi được bằng chứng
    // 4. Assert theo oracle trong expected_result (viết trước khi chạy, không sửa theo actual)
    expect(actual).toContain('...');
  });
}
```

Expected nằm trong JSON và được viết **trước** khi chạy. Không chỉnh assertion cho khớp Actual; nếu Expected sai so với đặc tả thì sửa có ghi lý do trong `notes` và commit riêng.

## Mẫu cho test API (bằng chứng là request/response thật)

```ts
test(`${c.id} ${c.title}`, async ({ request, page }, testInfo) => {
  const body = { name: '...', email: '...', password: '...' };
  const res = await request.post('http://localhost:3000/api/register', { data: body });
  const resBody = await res.text();
  // Bằng chứng chính: request/response JSON, attach bằng path để merge_results chép sang evidence/
  const reqFile = testInfo.outputPath(`${c.id}_request.json`);
  const resFile = testInfo.outputPath(`${c.id}_response.json`);
  fs.writeFileSync(reqFile, JSON.stringify({ method: 'POST', url: '/api/register', headers: { 'Content-Type': 'application/json' }, body }, null, 2));
  fs.writeFileSync(resFile, JSON.stringify({ status: res.status(), body: resBody }, null, 2));
  await testInfo.attach('request', { path: reqFile, contentType: 'application/json' });
  await testInfo.attach('response', { path: resFile, contentType: 'application/json' });
  // Tuỳ chọn: ảnh cho report — render từ response thật, không phải ảnh giao diện SUT
  await page.setContent(`<pre>${escapeHtml(`HTTP ${res.status()}\n${resBody}`)}</pre>`);
  const shot = testInfo.outputPath(`${c.id}_api.png`);
  await page.screenshot({ path: shot });
  await testInfo.attach('render từ response thật', { path: shot, contentType: 'image/png' });
  testInfo.annotations.push({ type: 'actual', description: `HTTP ${res.status()} ${resBody.slice(0, 200)}` });
  expect(res.status()).toBe(200);   // theo expected_result
});
```

## Mẫu Blocked (A17/A20)

Case không kiểm được đúng mục đích vì một lỗi đã có case khác kết luận (vd form thiếu ô cần nhập) → **không** dùng `test.skip` (Playwright sẽ báo "skipped" và mất lý do). Ghi verdict bằng annotation rồi kết thúc test bình thường; `merge_results.py` lấy annotation `verdict` thay cho status của Playwright:

```ts
if (await confirmInput.count() === 0) {
  testInfo.annotations.push({ type: 'verdict', description: 'Blocked' });
  testInfo.annotations.push({ type: 'actual', description: 'Blocked: form không có ô Xác nhận mật khẩu — case gây chặn TC-FR01-94 (A17)' });
  await page.screenshot({ path: shot, fullPage: true });   // vẫn chụp làm bằng chứng
  return;
}
```

Giá trị hợp lệ của `verdict`: `Pass`, `Fail`, `Blocked`, `Not run`, `Skipped`. Chỉ case kết luận nguyên nhân gốc mới ghi Fail (A20).

## Lưu ý với EShop

- Backend xoá và seed lại CSDL **mỗi lần khởi động** `node server.js`; giỏ hàng nằm trong RAM. Test cần dữ liệu riêng thì tự tạo trong test và dọn sau (self-cleaning), hoặc dùng email/tên có hậu tố duy nhất.
- So sánh UI với API cho cùng input khi cần biết lỗi nằm ở tầng nào.
- Mobile (Expo Go): chạy tay, điền `actual_result`, `status`, `evidence` (ảnh chụp màn hình điện thoại) vào JSON.
