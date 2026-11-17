/**
 * Page object cho FR-15 Quản lý sản phẩm (frontend-admin :5174). Selector theo mã thật
 * ../eshop-sut/frontend-admin/src/App.jsx @ de0f48f:
 *  - dòng 188–215  form "Admin Login": ô placeholder "Email", "Password", nút "Login"
 *  - dòng 221–260  thanh bên: <li> "Dashboard", "Danh mục", "Sản phẩm", … (không phải link/button)
 *  - dòng 483–567  form sản phẩm dùng chung Thêm/Sửa: <h3> "Thêm sản phẩm mới" | "Sửa sản phẩm";
 *                  input placeholder "Tên sản phẩm" (required), "Giá tiền" (type=number), "URL Ảnh", textarea "Mô tả",
 *                  <select> danh mục (ô chọn duy nhất), nút "Lưu sản phẩm", nút "Hủy sửa" (chỉ khi Sửa). KHÔNG có <label>.
 *  - dòng 568–607  bảng: cột Ảnh | Tên SP | Giá (`{p.price} ₫`, không phân cách) | Hành động (nút "Sửa", "Xóa")
 * Procedure HW02 TS-DOM-UI: định vị ô theo placeholder; không tải lại trang sau khi đăng nhập.
 */
import type { Locator, Page } from '@playwright/test';
import { ADMIN_WEB } from '../fixtures/ddt';

/** Giá hiển thị "1500000 ₫" / "0.1 ₫" / "-1000 ₫" / " ₫" → số (bỏ ký hiệu tiền, khoảng trắng, dấu phân cách hàng nghìn ','). Rỗng → null. */
export const priceOf = (s: string | null | undefined): number | null => {
  const t = (s ?? '').replace(/₫/g, '').replace(/[\s,]/g, '');
  if (t === '') return null;
  const n = Number(t);
  return Number.isNaN(n) ? null : n;
};

export class AdminLoginPage {
  readonly email: Locator;
  readonly password: Locator;
  readonly submit: Locator;
  constructor(readonly page: Page) {
    this.email = page.getByPlaceholder('Email', { exact: true });
    this.password = page.getByPlaceholder('Password', { exact: true });
    this.submit = page.getByRole('button', { name: 'Login', exact: true });
  }
  async open() { await this.page.goto(`${ADMIN_WEB}/`); await this.email.waitFor(); }
  /** Gõ email/mật khẩu, bấm Login đúng 1 lần, chờ thanh bên xuất hiện. */
  async login(email: string, password: string) {
    await this.email.fill(email);
    await this.password.fill(password);
    await this.submit.click();
    await this.page.getByRole('heading', { name: 'EShop Admin' }).waitFor();
  }
}

export class AdminShell {
  constructor(readonly page: Page) {}
  tab(name: string): Locator { return this.page.locator('li', { hasText: new RegExp(`^${name}$`) }); }
  async openProducts() {
    await this.tab('Sản phẩm').click();
    await this.page.locator('form', { has: this.page.getByRole('button', { name: 'Lưu sản phẩm' }) }).waitFor();
  }
}

export type FormMode = 'Thêm' | 'Sửa';

export class ProductForm {
  readonly root: Locator;
  readonly heading: Locator;
  readonly name: Locator;
  readonly price: Locator;
  readonly imageUrl: Locator;
  readonly description: Locator;
  readonly category: Locator;
  readonly save: Locator;
  readonly cancelEdit: Locator;
  constructor(readonly page: Page) {
    this.save = page.getByRole('button', { name: 'Lưu sản phẩm', exact: true });
    this.root = page.locator('form', { has: this.save });
    this.heading = this.root.locator('h3');
    this.name = this.root.getByPlaceholder('Tên sản phẩm', { exact: true });
    this.price = this.root.getByPlaceholder('Giá tiền', { exact: true });
    this.imageUrl = this.root.getByPlaceholder('URL Ảnh', { exact: true });
    this.description = this.root.getByPlaceholder('Mô tả', { exact: true });
    this.category = this.root.locator('select');                       // ô chọn duy nhất của form
    this.cancelEdit = this.root.getByRole('button', { name: 'Hủy sửa', exact: true });
  }
  /** Ô theo tên cột của data ('Tên sản phẩm' | 'Giá' | 'Mô tả' | 'URL Ảnh'). Cột lạ → ném lỗi. */
  field(col: string): Locator {
    const m: Record<string, Locator> = { 'Tên sản phẩm': this.name, 'Giá': this.price, 'Mô tả': this.description, 'URL Ảnh': this.imageUrl };
    if (!m[col]) throw new Error(`[admin.pages] không có ô cho cột '${col}'`);
    return m[col];
  }
  /** Xoá trắng rồi nhập. '' = để trống. long=true: dán (fill) thay vì gõ từng phím (chuỗi 'x' × n). Trả về value thật của ô. */
  async setText(el: Locator, v: string, long = false): Promise<string> {
    await el.fill('');
    if (v !== '') await (long ? el.fill(v) : el.pressSequentially(v));
    return el.inputValue();
  }
  /** Chọn option theo tên danh mục (chữ hiển thị). */
  async selectCategory(name: string) { await this.category.selectOption({ label: name }); }
  async selectedCategoryLabel(): Promise<string> {
    return this.category.evaluate((s: HTMLSelectElement) => s.selectedOptions[0]?.textContent ?? '');
  }
  /** Các ô không hợp lệ HTML5 trong form lúc này: [{placeholder, validationMessage}]. */
  async invalidFields(): Promise<{ field: string; message: string }[]> {
    return this.root.evaluate((f: HTMLFormElement) =>
      Array.from(f.querySelectorAll('input, textarea, select'))
        .filter(e => !(e as HTMLInputElement).checkValidity())
        .map(e => ({ field: (e as HTMLInputElement).placeholder || e.tagName, message: (e as HTMLInputElement).validationMessage })));
  }
}

export type TableRow = { name: string; priceRaw: string; price: number | null };

export class ProductTable {
  readonly rows: Locator;
  constructor(readonly page: Page) {
    this.rows = page.locator('table').filter({ has: page.getByRole('columnheader', { name: 'Tên SP' }) }).locator('tbody tr');
  }
  /** Dòng có ô 'Tên SP' đúng bằng name (so cả chuỗi). */
  row(name: string): Locator {
    return this.rows.filter({ has: this.page.locator('td:nth-child(2)').getByText(name, { exact: true }) });
  }
  editButton(name: string): Locator { return this.row(name).getByRole('button', { name: 'Sửa', exact: true }); }
  deleteButton(name: string): Locator { return this.row(name).getByRole('button', { name: 'Xóa', exact: true }); }
  /** Đọc bảng: mỗi dòng (Tên SP, Giá dạng giá trị số + chuỗi gốc). Thứ tự giữ như trên trang. */
  async read(): Promise<TableRow[]> {
    const out: TableRow[] = [];
    for (const tr of await this.rows.all()) {
      const td = await tr.locator('td').allInnerTexts();
      out.push({ name: td[1] ?? '', priceRaw: (td[2] ?? '').trim(), price: priceOf(td[2]) });
    }
    return out;
  }
}
