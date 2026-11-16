/**
 * Fixture riêng B_FR07 (FR-07 Giỏ hàng). Oracle = trạng thái giỏ trên UI (/cart), KHÔNG qua API:
 * giỏ web là state React (CartContext.jsx:6), không gọi API, không localStorage (HW04/B_FR07/selection.md).
 * - seed: bảng sản phẩm seed đọc từ tiền điều kiện HW02 trong file data (id → tên, giá) — không đọc qua API.
 * - startSession(login, tc, ts): mở trang đầu tiên của case ('khách' → /, 'user {ts}' → tạo user qua API + đăng nhập UI).
 *   Đây là lần mở URL trực tiếp DUY NHẤT của case (quy trình HW02 B0d).
 * - buildCart(text): dựng 'Giỏ ban đầu' theo cú pháp HW02: 'TC: id N' | 'CT: id N × n' | '—', cách nhau bởi ';'.
 * - dialogs: mọi dialog native (window.confirm/alert) được ghi lại (loại + nội dung) rồi xử lý theo dialogAction
 *   ('dismiss' mặc định; spec đặt shop.dialogAction = 'accept' trước thao tác cần xác nhận). Không xử lý → trang treo.
 * - sau mỗi case: xoá user đã tạo (DELETE /api/admin/users/:id).
 */
import { test as ddt, expect, fill, type DataFile } from './ddt';
import { WEB } from './ddt';
import { LoginPage } from '../pages/login.page';
import { NavBar, HomePage, ProductDetailPage, CartPage } from '../pages/shop.pages';

export type Product = { id: number; name: string; price: number };

/** "id 1 'iPhone 15 Pro Max' 30.000.000 ₫ · id 2 …" trong tiền điều kiện suite → danh sách sản phẩm seed. */
export function seedProducts(data: DataFile): Product[] {
  const text = Object.values(data.preconditions).flat().find(p => /Sản phẩm seed/.test(p));
  if (!text) throw new Error('[b_fr07] không thấy bảng "Sản phẩm seed" trong tiền điều kiện của file data');
  const out = [...text.matchAll(/id (\d+) '([^']+)' ([\d.]+) ₫/g)].map(m => ({ id: +m[1], name: m[2], price: +m[3].replace(/\./g, '') }));
  if (!out.length) throw new Error('[b_fr07] không đọc được sản phẩm seed: ' + text);
  return out;
}

export type CartStep = { via: 'TC' | 'CT'; id: number; qty?: string };
/** 'TC: id 1; CT: id 5 × 3' → bước dựng giỏ. '—' → []. Cú pháp lạ → ném lỗi (không đoán). */
export function parseCartSteps(text: string): CartStep[] {
  const t = text.trim();
  if (t === '—' || t === '') return [];
  return t.split(';').map(s => s.trim()).map(s => {
    let m = /^TC: id (\d+)$/.exec(s);
    if (m) return { via: 'TC' as const, id: +m[1] };
    m = /^CT: id (\d+) × (.*)$/.exec(s);
    if (m) return { via: 'CT' as const, id: +m[1], qty: m[2] };
    throw new Error(`[b_fr07] không hiểu bước dựng giỏ: "${s}"`);
  });
}

type Shop = {
  nav: NavBar; home: HomePage; detail: ProductDetailPage; cart: CartPage; login: LoginPage;
  dialogs: { type: string; message: string }[];
  dialogAction: 'accept' | 'dismiss';
  startSession: (login: string, tcId: string, ts: number) => Promise<void>;
  buildCart: (text: string) => Promise<void>;
};

export const test = ddt.extend<{ shop: Shop }>({
  shop: async ({ page, api }, use, testInfo) => {
    const nav = new NavBar(page);
    const home = new HomePage(page);
    const detail = new ProductDetailPage(page);
    const cart = new CartPage(page, nav);
    const login = new LoginPage(page);
    const shopRef = {} as Shop;
    const dialogs: Shop['dialogs'] = [];
    page.on('dialog', async d => {
      dialogs.push({ type: d.type(), message: d.message() });
      await (shopRef.dialogAction === 'accept' ? d.accept() : d.dismiss());
    });
    const created: number[] = [];

    const startSession = async (who: string, tcId: string, ts: number) => {
      if (/^user /.test(who)) {
        const email = `cart${tcId.split('-').pop()}_${ts}@domain.com`;       // quy trình HW02: cartNN_{ts}@domain.com
        const pwd = 'Abcd1234!';
        const res = await api.post('/api/register', { data: { name: 'Cart Tester', email, password: pwd } });
        if (res.status() !== 200) throw new Error(`[b_fr07] tạo user ${email}: HTTP ${res.status()}`);
        created.push((await res.json()).id);
        await login.open();                                                   // lần mở URL trực tiếp duy nhất
        await login.login(email, pwd);
        await page.waitForURL(`${WEB}/`);
        await page.locator('header').getByText(/Chào,/).waitFor();
      } else if (who === 'khách') {
        await page.goto(`${WEB}/`);
      } else {
        throw new Error(`[b_fr07] cột 'Đăng nhập' không hiểu: "${who}"`);
      }
      await home.waitLoaded();
    };

    const buildCart = async (text: string) => {
      for (const s of parseCartSteps(text)) {
        if (s.via === 'TC') {
          await home.addToCart(s.id);
        } else {
          await home.openDetail(s.id);
          await detail.waitLoaded();
          await detail.setQuantity(s.qty ?? '');
          await detail.add.click();                                           // đúng một lần (quy trình HW02)
          await nav.home.click();
          await home.waitLoaded();
        }
      }
    };

    Object.assign(shopRef, { nav, home, detail, cart, login, dialogs, dialogAction: 'dismiss', startSession, buildCart });
    await use(shopRef);

    for (const id of created) {
      const r = await api.delete(`/api/admin/users/${id}`).catch(() => null);
      if (!r || r.status() !== 200) testInfo.annotations.push({ type: 'cleanup', description: `xoá user id ${id}: HTTP ${r?.status() ?? 'lỗi'}` });
    }
  },
});
export { expect, fill };
export { loadData, loadCases, resetDb, blocked } from './ddt';
