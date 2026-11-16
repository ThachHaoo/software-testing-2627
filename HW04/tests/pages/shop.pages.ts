/**
 * Page object cho FR-07 Giỏ hàng (frontend-web). Selector theo mã thật ../eshop-sut/frontend-web/src @ de0f48f:
 *  - App.jsx:21–35   navbar: link "EShop" (/), link "Giỏ hàng" (/cart) — KHÔNG có badge số lượng (HW02 BUG-20)
 *  - Home.jsx:75–103 thẻ sản phẩm: <h2> tên, link "Xem chi tiết" (/product/:id), nút "Thêm vào giỏ"
 *  - ProductDetail.jsx:47–69 <h1> tên, <label>Số lượng:</label> + <input type=number> (không gắn htmlFor), nút "Thêm vào giỏ hàng"/"Đã thêm"
 *  - Cart.jsx:20–76  giỏ trống: <h2> "Giỏ hàng của bạn đang trống" + link "Tiếp tục mua sắm";
 *                    có hàng: bảng cột Sản phẩm | Giá | Số lượng | Thành tiền | Thao tác (nút "Xóa"), "Tổng tạm tính:", link "← Mua tiếp"
 * Giỏ là state React (CartContext.jsx:6) → chỉ điều hướng bằng link trong app, không goto/reload sau lần mở đầu.
 */
import type { Locator, Page } from '@playwright/test';

/** Số tiền / số lượng hiển thị → số (bỏ ký tự không phải chữ số: "28.000.000 ₫" → 28000000). null nếu không có chữ số. */
export const num = (s: string | null | undefined): number | null => {
  const d = (s ?? '').replace(/[^\d]/g, '');
  return d === '' ? null : Number(d);
};

export class NavBar {
  readonly home: Locator;
  readonly cart: Locator;
  constructor(readonly page: Page) {
    this.home = page.locator('header').getByRole('link', { name: 'EShop', exact: true });
    this.cart = page.locator('header').getByRole('link', { name: /Giỏ hàng/ });
  }
  /** Badge = phần số trong link "Giỏ hàng" (nếu có). Mã hiện tại không render badge → null. */
  async badge(): Promise<number | null> {
    return num((await this.cart.innerText()).replace('Giỏ hàng', ''));
  }
}

export class HomePage {
  constructor(readonly page: Page) {}
  /** Thẻ sản phẩm theo id: khối chứa link /product/<id>. */
  card(id: number): Locator {
    return this.page.locator('div.grid > div').filter({ has: this.page.locator(`a[href="/product/${id}"]`) });
  }
  async waitLoaded() { await this.page.getByRole('heading', { name: 'Danh sách sản phẩm' }).waitFor(); await this.page.locator('div.grid > div').first().waitFor(); }
  addToCart(id: number) { return this.card(id).getByRole('button', { name: 'Thêm vào giỏ' }).click(); }
  openDetail(id: number) { return this.card(id).getByRole('link', { name: 'Xem chi tiết' }).click(); }
}

export class ProductDetailPage {
  readonly title: Locator;
  readonly quantity: Locator;
  readonly add: Locator;
  constructor(readonly page: Page) {
    this.title = page.locator('main h1');
    this.quantity = page.locator('main div').filter({ has: page.locator('label', { hasText: /^Số lượng:$/ }) }).locator('input');
    this.add = page.getByRole('button', { name: /Thêm vào giỏ hàng|Đã thêm/ });
  }
  /** Chờ đúng trang /product/:id đã tải xong sản phẩm (hết "Đang tải...", có ô Số lượng). */
  async waitLoaded() { await this.page.waitForURL(/\/product\/\d+$/); await this.quantity.waitFor(); }
  /** Xoá trắng ô Số lượng rồi gõ đúng chuỗi (quy trình HW02: '' = để trống). Trả về value thật của ô sau khi gõ. */
  async setQuantity(v: string): Promise<string> {
    await this.quantity.fill('');
    if (v !== '') await this.quantity.pressSequentially(v);
    return this.quantity.inputValue();
  }
}

export type CartRow = { name: string; price: number | null; qty: string; subtotal: number | null };
export type CartState = { empty: boolean; rows: CartRow[]; total: number | null; badge: number | null };

export class CartPage {
  readonly emptyHeading: Locator;
  readonly continueEmpty: Locator;
  readonly continueFull: Locator;
  readonly rows: Locator;
  readonly total: Locator;
  constructor(readonly page: Page, readonly nav: NavBar) {
    this.emptyHeading = page.getByRole('heading', { name: 'Giỏ hàng của bạn đang trống' });
    this.continueEmpty = page.getByRole('link', { name: 'Tiếp tục mua sắm' });
    this.continueFull = page.getByRole('link', { name: /Mua tiếp/ });
    this.rows = page.locator('main table tbody tr');
    this.total = page.locator('main').getByText(/^Tổng tạm tính:/).locator('span');
  }
  /** Vào /cart bằng link navbar (không goto). */
  async open() {
    await this.nav.cart.click();
    await this.page.waitForURL(/\/cart$/);
    await this.emptyHeading.or(this.page.locator('main table')).first().waitFor();
  }
  row(name: string): Locator { return this.rows.filter({ has: this.page.locator('td', { hasText: name }) }); }
  removeButton(name: string): Locator { return this.row(name).getByRole('button', { name: 'Xóa' }); }
  /** Ảnh/icon minh hoạ trong trạng thái giỏ trống (img hoặc svg trong vùng main). */
  emptyIllustration(): Locator { return this.page.locator('main img, main svg'); }

  /** Đọc trạng thái giỏ trên UI: dòng (tên, Giá, Số lượng, Thành tiền), Tổng, badge. */
  async state(): Promise<CartState> {
    const empty = await this.emptyHeading.isVisible();
    const rows: CartRow[] = [];
    if (!empty) {
      for (const tr of await this.rows.all()) {
        const td = (await tr.locator('td').allInnerTexts()).map(s => s.trim());
        rows.push({ name: td[0], price: num(td[1]), qty: td[2], subtotal: num(td[3]) });
      }
    }
    const total = empty ? null : num(await this.total.innerText());
    return { empty, rows, total, badge: await this.nav.badge() };
  }
}
