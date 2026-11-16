/**
 * Page object trang đăng nhập (frontend-web /login).
 * Selector theo mã thật ../eshop-sut/frontend-web/src/pages/Login.jsx @ de0f48f:
 *  - tiêu đề <h2> ghi "Đăng Ký" (dòng 24), nhãn ô thứ nhất "Username" (dòng 28)
 *  - <label> không gắn htmlFor → tìm input trong cùng <div> với nhãn; ô mật khẩu type="text" (dòng 39)
 *  - nút "Sign In" (dòng 53–59); hộp lỗi <div class="bg-red-100 …"> (dòng 66); đăng nhập xong điều hướng "/" (dòng 16)
 */
import type { Locator, Page } from '@playwright/test';
import { WEB } from '../fixtures/ddt';

export class LoginPage {
  readonly error: Locator;
  readonly submit: Locator;

  constructor(readonly page: Page) {
    this.error = page.locator('div.bg-red-100');
    this.submit = page.getByRole('button', { name: 'Sign In' });
  }

  field(label: string): Locator {
    return this.page.locator('form > div')
      .filter({ has: this.page.locator('label', { hasText: new RegExp(`^\\s*${label}\\s*$`) }) })
      .locator('input');
  }
  email() { return this.field('Username'); }
  password() { return this.field('Mật khẩu'); }

  async open() {
    await this.page.goto(`${WEB}/login`);
    await this.submit.waitFor();
  }

  async login(email: string, password: string) {
    await this.email().fill(email);
    await this.password().fill(password);
    await this.submit.click();
  }

  /** Token đăng nhập web lưu ở localStorage "token" (AuthContext.jsx). */
  token(): Promise<string | null> {
    return this.page.evaluate(() => localStorage.getItem('token'));
  }
}
