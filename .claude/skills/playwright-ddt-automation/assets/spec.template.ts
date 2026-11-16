/**
 * MẪU spec data-driven (bước 3) — HW04/tests/<X_FRnn>.spec.ts.
 * Lặp theo file data; tiêu đề "<tc_id> <title>"; ≥ 3 kiểu assertion; expect.soft để một TC ghi đủ mọi điểm lệch.
 * Giá trị nhập và oracle lấy từ c.inputs / c.expected — không viết hằng dữ liệu trong spec.
 */
import { test, expect, loadCases, fill, blocked } from './fixtures/ddt';

const CASES = loadCases('X_FRnn');            // kiểm sha1(expected) khi nạp

test.describe.configure({ mode: 'serial' });

for (const c of CASES) {
  test(`${c.tc_id} ${c.title}`, async ({ page, api }) => {
    test.info().annotations.push({ type: 'expected', description: c.expected }, { type: 'hw02', description: c.hw02.status });
    const ts = Date.now();

    // 1. oracle dữ liệu TRƯỚC (API)
    const before = await (await api.get('/api/...')).json();

    // 2. thao tác UI theo c.inputs
    await page.goto('/...');
    // const field = page.getByLabel(...); if (!(await field.count())) return blocked('...');

    // 3. assertion — tối thiểu 3 kiểu:
    // trạng thái UI:     await expect.soft(page).toHaveURL(/\/login$/);  await expect.soft(locator).toBeVisible();
    // nội dung thông báo: await expect.soft(alert).toContainText(...);
    // oracle dữ liệu:     const after = await (await api.get('/api/...')).json(); expect.soft(diff(before, after)).toEqual([...]);
    // đếm / giá trị:      await expect.soft(rows).toHaveCount(n);  await expect.soft(input).toHaveValue(...);
  });
}
