/**
 * Kiểm môi trường trước MỖI lượt (một project P1 hoặc P2):
 * backend :3000 và web :5173 trả lời; đăng nhập admin + test@eshop.com được; test@eshop.com CHƯA có đơn
 * (= backend vừa khởi động lại, CSDL seed sạch — CL-62 cần trạng thái này). Thiếu → dừng cả lượt.
 * Xoá ảnh auto cũ của nền tảng đang chạy (evidence chỉ giữ lượt mới nhất).
 */
import fs from 'fs';
import path from 'path';
import { request } from '@playwright/test';
import { API, WEB, ADMIN, USER, EVIDENCE_DIR } from './lib';

const HINT = '→ Khởi động lại backend (cd ..\\eshop-sut\\backend; node server.js) để CSDL seed sạch, chạy web (cd ..\\eshop-sut\\frontend-web; npx vite --host 127.0.0.1 --port 5173), rồi chạy lại.';

export default async function globalSetup() {
  const projects = process.argv.flatMap((a, i, all) => a === '--project' ? [all[i + 1]] : a.startsWith('--project=') ? [a.slice(10)] : []);
  if (projects.length !== 1) throw new Error('[global-setup] Chạy đúng MỘT nền tảng mỗi lượt: --project=P1 hoặc --project=P2 (restart backend giữa hai lượt).');
  const ctx = await request.newContext();
  const fail = (m: string): never => { throw new Error(`[global-setup] ${m}\n${HINT}`); };
  try {
    const be = await ctx.get(`${API}/api/products`).catch(() => null);
    if (!be || be.status() !== 200) fail(`Backend ${API} không trả lời.`);
    const web = await ctx.get(WEB).catch(() => null);
    if (!web || web.status() !== 200) fail(`Web ${WEB} không trả lời.`);
    for (const who of [ADMIN, USER]) {
      const r = await ctx.post(`${API}/api/login`, { data: who });
      if (r.status() !== 200) fail(`Không đăng nhập được ${who.email} (HTTP ${r.status()}) — có thể đang bị khoá hoặc mật khẩu đã đổi.`);
      if (who === USER) {
        const { token } = await r.json();
        const o = await ctx.get(`${API}/api/orders/my-orders`, { headers: { Authorization: `Bearer ${token}` } });
        const list = o.status() === 200 ? await o.json() : null;
        if (!Array.isArray(list) || list.length) fail(`${USER.email} đã có ${Array.isArray(list) ? list.length : '?'} đơn — CSDL không ở trạng thái vừa seed.`);
      }
    }
  } finally {
    await ctx.dispose();
  }
  fs.mkdirSync(EVIDENCE_DIR, { recursive: true });
  for (const f of fs.readdirSync(EVIDENCE_DIR)) if (f.startsWith(`${projects[0]}_`)) fs.rmSync(path.join(EVIDENCE_DIR, f));
}
