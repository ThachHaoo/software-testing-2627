/**
 * Kiểm môi trường trước khi chạy: backend :3000, web :5173 trả lời; đăng nhập admin được; CSDL có tài khoản seed.
 * Thiếu thì dừng toàn bộ lượt chạy và nhắc khởi động lại (backend restart = CSDL seed sạch, A13).
 */
import { request } from '@playwright/test';

const API = 'http://localhost:3000';
const WEB = 'http://localhost:5173';
const ADMIN = { email: 'admin@eshop.com', password: 'Admin123!' };   // SRS README.md dòng 22
const SEED = 'test@eshop.com';                                       // SRS README.md dòng 23
const HINT = '→ Khởi động lại backend (cd eshop-sut/backend; node server.js) để CSDL seed sạch, chạy web (cd eshop-sut/frontend-web; npm run dev), rồi chạy lại test.';

export default async function globalSetup() {
  const ctx = await request.newContext();
  const fail = (msg: string): never => { throw new Error(`[global-setup] ${msg}\n${HINT}`); };
  try {
    const be = await ctx.get(`${API}/api/products`).catch(() => null);
    if (!be || be.status() !== 200) fail(`Backend ${API} không trả lời (HTTP ${be?.status() ?? 'không kết nối được'}).`);
    const web = await ctx.get(WEB).catch(() => null);
    if (!web || web.status() !== 200) fail(`Web ${WEB} không trả lời (HTTP ${web?.status() ?? 'không kết nối được'}).`);
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
