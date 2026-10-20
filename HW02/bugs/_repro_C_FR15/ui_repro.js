// Tái hiện nhóm UI C_FR15 (7/7a) — chạy: node ui_repro.js (NODE_PATH = HW02/tests/node_modules)
const { chromium, request } = require('playwright');
const API = 'http://localhost:3000', UI = 'http://localhost:5174';
const ts = Date.now();

(async () => {
  const api = await request.newContext();
  const ta = (await (await api.post(`${API}/api/login`, { data: { email: 'admin@eshop.com', password: 'Admin123!' } })).json()).token;
  const H = { Authorization: `Bearer ${ta}` };
  const list = async () => (await (await api.get(`${API}/api/products`)).json());
  const startIds = new Set((await list()).map(p => p.id));
  const mk = async (name) => { await api.post(`${API}/api/products`, { headers: H, data: { name, price: 1000000, category_id: 1, description: 'repro', imageUrl: 'https://placehold.co/300' } }); return (await list()).find(p => p.name === name); };

  const browser = await chromium.launch();
  async function open() {
    const page = await browser.newPage();
    const dialogs = [];
    page.on('dialog', d => { dialogs.push(d.message()); d.accept(); });
    await page.goto(UI);
    await page.getByPlaceholder('Email').fill('admin@eshop.com');
    await page.getByPlaceholder('Password').fill('Admin123!');
    await page.getByRole('button', { name: 'Login' }).click();
    await page.locator('li', { hasText: /^Sản phẩm$/ }).click();
    await page.getByRole('button', { name: 'Lưu sản phẩm' }).waitFor();
    await page.waitForTimeout(500);
    return { page, dialogs };
  }
  const rows = (page) => page.locator('table:has(th:text("Tên SP")) tbody tr').evaluateAll(trs => trs.map(tr => [...tr.querySelectorAll('td')].slice(1, 3).map(td => td.textContent.trim()).join(' | ')));
  async function add(label, name, price, cat = 'Laptop') {
    const { page, dialogs } = await open();
    const before = (await list()).length;
    await page.getByPlaceholder('Tên sản phẩm', { exact: true }).fill(name);
    await page.getByPlaceholder('Giá tiền', { exact: true }).fill('');
    await page.getByPlaceholder('Giá tiền', { exact: true }).pressSequentially(price);
    await page.locator('form select').selectOption({ label: cat });
    await page.getByRole('button', { name: 'Lưu sản phẩm' }).click();
    await page.waitForTimeout(1200);
    const after = await list();
    const n = after.filter(p => !startIds.has(p.id)).pop();
    console.log(`${label}: hộp thoại=${JSON.stringify(dialogs)}; bản ghi ${before} → ${after.length}; bản ghi mới=${JSON.stringify(n && { ...n, name: n.name && n.name.length > 40 ? `<${n.name.length} ký tự>` : n.name })}`);
    await page.close();
  }
  async function edit(label, field, value, extra) {
    const M = await mk(`repro ${label} M ${ts}`);
    const { page, dialogs } = await open();
    const t0 = await rows(page);
    await page.locator('table tbody tr', { hasText: M.name }).getByRole('button', { name: 'Sửa' }).click();
    const box = page.getByPlaceholder(field, { exact: true });
    await box.fill('');
    if (value) await (field === 'Giá tiền' ? box.pressSequentially(value) : box.fill(value));
    if (extra) await extra(page);
    await page.getByRole('button', { name: 'Lưu sản phẩm' }).click();
    await page.waitForTimeout(1200);
    const m = await (await api.get(`${API}/api/products/${M.id}`)).json();
    const t1 = await rows(page);
    console.log(`${label}: hộp thoại=${JSON.stringify(dialogs)}; M TRƯỚC=${JSON.stringify({ name: M.name, price: M.price })}; M SAU=${JSON.stringify({ name: m.name, price: m.price, category_id: m.category_id })}`);
    console.log(`   bảng TRƯỚC: ${JSON.stringify(t0)}`);
    console.log(`   bảng SAU:   ${JSON.stringify(t1)}`);
    await page.close();
  }

  await add('G1 Thêm, tên 256 ký tự', 'x'.repeat(256), '1500000');
  await add('G1 Thêm, tên 3 dấu cách', '   ', '1500000');
  await add('G2 Thêm, giá -1000', `repro G2 ${ts}`, '-1000');
  await add('G2 Thêm, giá để trống', `repro G2b ${ts}`, '');
  await edit('G3', 'Tên sản phẩm', '   ');
  await edit('G4', 'Giá tiền', '0');
  await edit('G5', 'Tên sản phẩm', `Sửa repro G5 ${ts}`, async p => { await p.getByPlaceholder('Giá tiền', { exact: true }).fill(''); await p.getByPlaceholder('Giá tiền', { exact: true }).pressSequentially('2500000'); });
  await add('G6 Thêm, tên <script>', '<script>alert(1)</script>', '1500000');
  await add('G7 Thêm, giá 1e5', `repro G7 ${ts}`, '1e5');
  {
    const { page } = await open();
    const f = page.locator('form', { has: page.getByRole('button', { name: 'Lưu sản phẩm' }) });
    console.log(`G15: số <label> trong form=${await f.locator('label').count()}; có '*' trong form=${(await f.innerText()).includes('*')}; placeholder=${JSON.stringify(await f.locator('input,textarea').evaluateAll(es => es.map(e => e.placeholder)))}`);
    console.log(`G16: ô Giá dòng 'iPhone 15 Pro Max' = ${JSON.stringify(await page.locator('table tbody tr', { hasText: 'iPhone 15 Pro Max' }).locator('td').nth(2).innerText())}`);
    await page.close();
  }
  await browser.close();
  // dọn dữ liệu repro
  for (const p of (await list()).filter(p => !startIds.has(p.id))) await api.delete(`${API}/api/products/${p.id}`, { headers: H });
  console.log(`dọn: còn ${(await list()).length} bản ghi`);
  await api.dispose();
})();
