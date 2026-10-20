/**
 * Kiểm môi trường trước khi chạy: backend :3000, web :5173 trả lời (C_FR15: web admin :5174); đăng nhập admin được; CSDL có tài khoản seed.
 * C_FR15: CSDL phải đúng trạng thái vừa seed (sản phẩm id 1–5) — backend được khởi động lại trước MỌI lượt (C0).
 * Thiếu thì dừng toàn bộ lượt chạy và nhắc khởi động lại (backend restart = CSDL seed sạch, A13).
 */
import { request } from '@playwright/test';

const API = 'http://localhost:3000';
const WEB = 'http://localhost:5173';
const ADMIN_UI = 'http://localhost:5174';
const C_FR15 = process.argv.some(a => /C_FR15/.test(a));            // lượt chạy --project=C_FR15
const ADMIN = { email: 'admin@eshop.com', password: 'Admin123!' };   // SRS README.md dòng 22
const SEED = 'test@eshop.com';                                       // SRS README.md dòng 23
const HINT = '→ Khởi động lại backend (cd eshop-sut/backend; node server.js) để CSDL seed sạch, chạy web (cd eshop-sut/frontend-web; npm run dev) — C_FR15: web admin (cd eshop-sut/frontend-admin; npm run dev) — rồi chạy lại test.';

export default async function globalSetup() {
  const ctx = await request.newContext();
  const fail = (msg: string): never => { throw new Error(`[global-setup] ${msg}\n${HINT}`); };
  try {
    const be = await ctx.get(`${API}/api/products`).catch(() => null);
    if (!be || be.status() !== 200) fail(`Backend ${API} không trả lời (HTTP ${be?.status() ?? 'không kết nối được'}).`);
    const ui = C_FR15 ? ADMIN_UI : WEB;
    const web = await ctx.get(ui).catch(() => null);
    if (!web || web.status() !== 200) fail(`Web ${ui} không trả lời (HTTP ${web?.status() ?? 'không kết nối được'}).`);
    if (C_FR15) {
      const ids = ((await be!.json()) as { id: number }[]).map(p => p.id).sort((a, b) => a - b);
      if (ids.join(',') !== '1,2,3,4,5') fail(`CSDL không ở trạng thái vừa seed (sản phẩm id: ${ids.join(', ')}; cần đúng 1–5).`);
    }
    const login = await ctx.post(`${API}/api/login`, { data: ADMIN });
    if (login.status() !== 200) fail(`Không đăng nhập được ${ADMIN.email} (HTTP ${login.status()}) — tài khoản có thể đang bị khoá hoặc CSDL đã đổi.`);
    const { token } = await login.json();
    const users = await ctx.get(`${API}/api/admin/users`, { headers: { Authorization: `Bearer ${token}` } });
    const list: { email: string }[] = users.status() === 200 ? await users.json() : [];
    if (!list.some(u => u.email === SEED)) fail(`CSDL không có tài khoản seed ${SEED}.`);
  } finally {
    await ctx.dispose();
  }
}
