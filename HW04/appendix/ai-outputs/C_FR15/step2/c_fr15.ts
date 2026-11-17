/**
 * Fixture riêng C_FR15 (FR-15 Quản lý sản phẩm, web admin :5174).
 * Oracle dữ liệu = API: GET /api/products TRƯỚC/SAU (danh sách), GET /api/products/M (M_TRƯỚC/M_SAU) — procedure HW02 bước 2, 7.
 * - catalog: list(), get(id), create(body), remove(id), alive() — dùng Bearer admin (fixture `api` của ddt.ts).
 * - admin.createTarget(tcId, ts): dựng sản phẩm mục tiêu M đúng body procedure HW02 bước 1, lấy id theo name từ GET /api/products.
 * - admin.loginAndOpenProducts(): mở :5174 (lần goto duy nhất), đăng nhập admin, bấm 'Sản phẩm' trên thanh bên.
 * - dialogs: mọi dialog native được ghi lại (loại + nội dung) rồi bấm OK (accept) — procedure HW02 bước 6.
 * - Cleanup sau mỗi case (kể cả Fail): xoá mọi id có trong danh sách hiện tại mà không có trong danh sách lúc bắt đầu case
 *   (gồm M) — cleanup HW02. Xoá lỗi → annotation 'cleanup', không đổi verdict.
 * - C2=a (SV chốt): sau mỗi case kiểm backend còn sống (GET /api/products = 200). Sập → annotation 'backend sập',
 *   resetDb() (restart + seed lại) rồi ném lỗi → case Fail; case kế tiếp chạy trên backend mới. Không đổi procedure,
 *   không xoá bản ghi để tránh sập.
 */
import type { APIRequestContext } from '@playwright/test';
import { test as ddt, expect, fill, resetDb, ADMIN, API } from './ddt';
import { AdminLoginPage, AdminShell, ProductForm, ProductTable } from '../pages/admin.pages';

export type Product = { id: number; name: string; price: unknown; description: string | null; imageUrl: string | null; category_id: unknown };
export type Category = { id: number; name: string };

/** "'x' × 300" → 300 ký tự 'x'. Chuỗi khác giữ nguyên. Trả kèm cờ long (dán thay vì gõ từng phím, procedure: "gõ/dán"). */
export function expandValue(v: string): { value: string; long: boolean } {
  const m = /^'(.)' × (\d+)$/.exec(v);
  return m ? { value: m[1].repeat(+m[2]), long: true } : { value: v, long: false };
}

class Catalog {
  constructor(private api: APIRequestContext) {}
  async list(): Promise<Product[]> {
    const r = await this.api.get('/api/products');
    if (r.status() !== 200) throw new Error(`[c_fr15] GET /api/products: HTTP ${r.status()}`);
    return r.json();
  }
  async get(id: number): Promise<Product | Record<string, never>> {
    const r = await this.api.get(`/api/products/${id}`);
    if (r.status() !== 200) throw new Error(`[c_fr15] GET /api/products/${id}: HTTP ${r.status()}`);
    return r.json();
  }
  async categories(): Promise<Category[]> {
    const r = await this.api.get('/api/categories');
    if (r.status() !== 200) throw new Error(`[c_fr15] GET /api/categories: HTTP ${r.status()}`);
    return r.json();
  }
  async create(body: Record<string, unknown>) {
    const r = await this.api.post('/api/products', { data: body });
    if (r.status() !== 200) throw new Error(`[c_fr15] POST /api/products: HTTP ${r.status()} ${await r.text()}`);
  }
  async remove(id: number) { return this.api.delete(`/api/products/${id}`); }
  /** Backend còn trả lời: GET /api/products = 200 trong 5 s. Lỗi kết nối/timeout → false. */
  async alive(): Promise<boolean> {
    try {
      return (await this.api.get('/api/products', { timeout: 5_000 })).status() === 200;
    } catch (e) {
      if (e instanceof Error && /ECONNREFUSED|ECONNRESET|socket hang up|Timeout|timed out/i.test(e.message)) return false;
      throw e;
    }
  }
}

type Admin = {
  catalog: Catalog;
  login: AdminLoginPage; shell: AdminShell; form: ProductForm; table: ProductTable;
  dialogs: { type: string; message: string }[];
  /** Procedure bước 1: POST M rồi lấy id theo name 'Muc tieu NN {ts}'. */
  createTarget: (tcId: string, ts: number) => Promise<{ id: number; name: string }>;
  loginAndOpenProducts: () => Promise<void>;
};

export const test = ddt.extend<{ admin: Admin }>({
  admin: async ({ page, api }, use, testInfo) => {
    const catalog = new Catalog(api);
    const baseline = new Set((await catalog.list()).map(p => p.id));   // để cleanup xoá đúng phần case tạo ra
    const dialogs: Admin['dialogs'] = [];
    page.on('dialog', async d => { dialogs.push({ type: d.type(), message: d.message() }); await d.accept(); });

    const login = new AdminLoginPage(page);
    const shell = new AdminShell(page);
    const form = new ProductForm(page);
    const table = new ProductTable(page);

    const createTarget = async (tcId: string, ts: number) => {
      const nn = tcId.split('-').pop();
      const name = `Muc tieu ${nn} ${ts}`;
      await catalog.create({ name, price: 1000000, description: fill('Mô tả mục tiêu {ts}', ts), imageUrl: 'https://placehold.co/300', category_id: 1 });
      const found = (await catalog.list()).filter(p => p.name === name);
      if (found.length !== 1) throw new Error(`[c_fr15] dựng M: tìm thấy ${found.length} bản ghi name '${name}'`);
      return { id: found[0].id, name };
    };

    const loginAndOpenProducts = async () => {
      await login.open();                                                 // lần mở URL trực tiếp duy nhất
      await login.login(ADMIN.email, ADMIN.password);
      await shell.openProducts();
      await table.rows.first().waitFor();
    };

    await use({ catalog, login, shell, form, table, dialogs, createTarget, loginAndOpenProducts });

    // C2=a: kiểm backend còn sống trước cleanup
    if (!(await catalog.alive())) {
      testInfo.annotations.push({ type: 'backend sập', description: `GET ${API}/api/products không trả lời sau case → resetDb() trước case kế tiếp` });
      resetDb();
      throw new Error(`[C_FR15] backend sập trong/sau ${testInfo.title} (annotation 'backend sập'); đã restart backend`);
    }
    for (const p of await catalog.list()) {
      if (baseline.has(p.id)) continue;
      const r = await catalog.remove(p.id);
      if (r.status() !== 200) testInfo.annotations.push({ type: 'cleanup', description: `xoá sản phẩm id ${p.id}: HTTP ${r.status()}` });
    }
  },
});
export { expect, fill };
export { loadData, loadCases, resetDb, blocked } from './ddt';
