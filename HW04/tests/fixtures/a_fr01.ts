/**
 * Fixture riêng A_FR01 (FR-01 Đăng ký): oracle dữ liệu qua API admin + dọn dữ liệu sau mỗi case.
 * - `users`: chụp danh sách user TRƯỚC thao tác UI (bước 1 quy trình HW02 TS-DOM-UI), cho phép lấy lại SAU,
 *   và sau mỗi case (kể cả khi Fail) xoá user mới tạo để case sau không phụ thuộc case trước (A19).
 * - `registerPage`, `loginPage`: page object.
 */
import { test as ddt, expect } from './ddt';
import { RegisterPage } from '../pages/register.page';
import { LoginPage } from '../pages/login.page';

export type User = { id: number; name: string | null; email: string | null; role: string };

export function diffUsers(before: User[], after: User[]) {
  const ids = new Set(before.map(u => u.id));
  return {
    added: after.filter(u => !ids.has(u.id)),
    removed: before.filter(u => !after.some(a => a.id === u.id)),
    changed: before.filter(u => {
      const a = after.find(x => x.id === u.id);
      return !!a && (a.name !== u.name || a.email !== u.email || a.role !== u.role);
    }),
  };
}

type Users = { before: User[]; list: () => Promise<User[]> };

export const test = ddt.extend<{ users: Users; registerPage: RegisterPage; loginPage: LoginPage }>({
  users: async ({ api }, use, testInfo) => {
    const list = async (): Promise<User[]> => {
      const r = await api.get('/api/admin/users');
      if (r.status() !== 200) throw new Error(`GET /api/admin/users trả HTTP ${r.status()}`);
      return r.json();
    };
    const before = await list();
    await use({ before, list });
    try {
      for (const u of diffUsers(before, await list()).added) {
        const r = await api.delete(`/api/admin/users/${u.id}`);
        if (r.status() !== 200) testInfo.annotations.push({ type: 'cleanup', description: `xoá user id ${u.id}: HTTP ${r.status()}` });
      }
    } catch (e) {
      testInfo.annotations.push({ type: 'cleanup', description: `cleanup lỗi: ${(e as Error).message}` });
    }
  },
  registerPage: async ({ page }, use) => use(new RegisterPage(page)),
  loginPage: async ({ page }, use) => use(new LoginPage(page)),
});
export { expect };
export { loadData, loadCases, fill, resetDb, blocked } from './ddt';
