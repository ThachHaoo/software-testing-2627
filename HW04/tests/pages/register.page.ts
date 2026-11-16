/**
 * Page object form "Đăng Ký Tài Khoản" (frontend-web /register).
 * Selector theo mã thật ../eshop-sut/frontend-web/src/pages/Register.jsx @ de0f48f:
 *  - tiêu đề <h2> "Đăng Ký Tài Khoản" (dòng 32); hộp lỗi <div class="bg-red-100 …"> (dòng 33)
 *  - <label> KHÔNG gắn htmlFor với <input> (dòng 36–63) → getByLabel không dùng được; tìm input trong cùng <div> với nhãn
 *  - nút submit "Đăng Ký" (dòng 70–75); không có ô "Xác nhận mật khẩu" (HW02 BUG-14) → confirm() có thể rỗng
 */
import type { Locator, Page } from '@playwright/test';
import { WEB } from '../fixtures/ddt';

export class RegisterPage {
  readonly heading: Locator;
  readonly error: Locator;
  readonly submit: Locator;

  constructor(readonly page: Page) {
    this.heading = page.getByRole('heading', { name: 'Đăng Ký Tài Khoản' });
    this.error = page.locator('div.bg-red-100');
    this.submit = page.getByRole('button', { name: 'Đăng Ký', exact: true });
  }

  /** Ô nhập nằm cùng khối <div> với nhãn có đúng chữ `label`. */
  field(label: string): Locator {
    return this.page.locator('form > div')
      .filter({ has: this.page.locator('label', { hasText: new RegExp(`^\\s*${label}\\s*$`) }) })
      .locator('input');
  }
  name() { return this.field('Họ Tên'); }
  email() { return this.field('Email'); }
  password() { return this.field('Mật khẩu'); }
  confirm() { return this.field('Xác nhận mật khẩu'); }

  async open() {
    await this.page.goto(`${WEB}/register`);
    await this.heading.waitFor();
  }

  /** Gõ đúng chuỗi; '' = không nhập gì (giữ ô trống, quy trình HW02 TS-DOM-UI bước 3). */
  async type(input: Locator, value: string) {
    if (value !== '') await input.pressSequentially(value);
  }

  /** validationMessage của ô (A16: trình duyệt chặn submit khi ô required trống). */
  validationMessage(input: Locator): Promise<string> {
    return input.evaluate((el: HTMLInputElement) => el.validationMessage);
  }
}
