# Chạy test tự động từ testcases.json

## Quy ước để `merge_results.py` gộp được

- **Tiêu đề test bắt đầu bằng mã TC**: `TC-FR01-03 Kiểm tra … khi …`.
- Ghi **Actual** bằng annotation `actual` (chuỗi quan sát được: chữ thông báo, URL sau submit, HTTP status + body rút gọn).
- Chụp màn hình cuối mỗi test và đính kèm (`testInfo.attach`) — đường dẫn được ghi vào `evidence`.
- Reporter JSON: `npx playwright test --reporter=list,json` với `PLAYWRIGHT_JSON_OUTPUT_NAME=results/<feature>.json`.
- Map trạng thái: `passed → Pass`, `failed/timedOut → Fail`, `skipped → Not run`, `interrupted → Blocked`.

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

## Lưu ý với EShop

- Backend xoá và seed lại CSDL **mỗi lần khởi động** `node server.js`; giỏ hàng nằm trong RAM. Test cần dữ liệu riêng thì tự tạo trong test và dọn sau (self-cleaning), hoặc dùng email/tên có hậu tố duy nhất.
- So sánh UI với API cho cùng input khi cần biết lỗi nằm ở tầng nào.
- Mobile (Expo Go): chạy tay, điền `actual_result`, `status`, `evidence` (ảnh chụp màn hình điện thoại) vào JSON.
