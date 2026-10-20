// 7c — chạy bước tái hiện SV viết cho BUG-35…40, 45, 49, 50 (UI admin :5174)
// Chạy: node ui_7c.js (NODE_PATH = HW02/tests/node_modules). Restart backend trước mỗi thao tác và sau thao tác cuối.
// Bước đăng nhập (admin@eshop.com / Admin123!) SV không ghi — thêm vào để tới được trang 'Sản phẩm'.
const { chromium, request } = require('playwright');
const { execSync } = require('child_process');
const path = require('path');
const API = 'http://localhost:3000', UI = 'http://localhost:5174';
const restart = () => execSync(`powershell -ExecutionPolicy Bypass -File "${path.join(__dirname, 'restart_backend.ps1')}"`).toString().trim();
const short = (s) => (s == null ? s : String(s).replace(/x{20}x+/g, (m) => `"x"×${m.length}`));

(async () => {
  const api = await request.newContext();
  const list = async () => (await (await api.get(`${API}/api/products`)).json());
  const browser = await chromium.launch();

  async function open() {
    const page = await browser.newPage();
    const dialogs = [];
    page.on('dialog', (d) => { dialogs.push(d.message()); d.accept(); });
    await page.goto(UI);
    await page.getByPlaceholder('Email').fill('admin@eshop.com');
    await page.getByPlaceholder('Password').fill('Admin123!');
    await page.getByRole('button', { name: 'Login' }).click();
    await page.locator('li', { hasText: /^Sản phẩm$/ }).click();          // bước 1 của SV: chọn mục "Sản phẩm"
    await page.getByRole('button', { name: 'Lưu sản phẩm' }).waitFor();
    await page.waitForTimeout(500);
    await page.evaluate(() => { window.__invalid = []; document.addEventListener('invalid', (e) => window.__invalid.push(e.target.placeholder || e.target.tagName), true); });
    return { page, dialogs };
  }
  const rows = (page) => page.locator('table:has(th:text("Tên SP")) tbody tr').evaluateAll((trs) => trs.map((tr) => [...tr.querySelectorAll('td')].slice(1, 3).map((td) => td.textContent).join(' | ')));
  const formTitle = (page) => page.locator('h2, h3', { hasText: /sản phẩm/ }).allInnerTexts();
  const pageText = (page) => page.evaluate(() => document.body.innerText.split('\n').map((s) => s.trim()).filter(Boolean));
  async function save(page, dialogs, before) {
    const t0 = await pageText(page);
    await page.getByRole('button', { name: 'Lưu sản phẩm' }).click();
    await page.waitForTimeout(1200);
    const t1 = await pageText(page);
    const tableText = new Set((await rows(page)).flatMap((r) => r.split(' | ').map((s) => s.trim())));
    const msgs = t1.filter((s) => !t0.includes(s) && !tableText.has(s) && !/₫$/.test(s));
    const invalid = await page.evaluate(() => window.__invalid);
    return `hộp thoại=${JSON.stringify(dialogs)}; ô HTML5 invalid=${JSON.stringify(invalid)}; chữ mới trên trang (ngoài bảng)=${JSON.stringify(msgs.map(short))}`;
  }
  async function add(label, name, price, cat = 'Laptop', typePrice = true) {
    console.log(`   [${restart()}]`);
    const { page, dialogs } = await open();
    const b = await list(); const tb = await rows(page);
    await page.getByPlaceholder('Tên sản phẩm', { exact: true }).fill(name);
    if (typePrice && price !== '') await page.getByPlaceholder('Giá tiền', { exact: true }).pressSequentially(price);
    await page.locator('form select').selectOption({ label: cat });
    const v = await page.getByPlaceholder('Giá tiền', { exact: true }).inputValue();
    const obs = await save(page, dialogs);
    const a = await list(); const ta = await rows(page);
    const n = a.filter((p) => !b.some((q) => q.id === p.id)).map((p) => ({ id: p.id, name: short(p.name), price: p.price, category_id: p.category_id }));
    console.log(`${label}: giá trị ô Giá tiền lúc bấm=${JSON.stringify(v)}; ${obs}; bản ghi (GET /api/products) ${b.length} → ${a.length}; bản ghi mới=${JSON.stringify(n)}; bảng ${tb.length} → ${ta.length} dòng; dòng mới=${JSON.stringify(ta.filter((r) => !tb.includes(r)).map(short))}`);
    await page.close();
  }
  async function edit(label, rowName, set) {
    console.log(`   [${restart()}]`);
    const { page, dialogs } = await open();
    const b = await list(); const tb = await rows(page);
    const M = b.find((p) => p.name === rowName);
    await page.locator('table tbody tr', { hasText: rowName }).getByRole('button', { name: 'Sửa' }).click();
    const title = await formTitle(page);
    for (const [ph, val] of set) {
      const box = page.getByPlaceholder(ph, { exact: true });
      await box.fill('');
      if (val !== '') await (ph === 'Giá tiền' ? box.pressSequentially(val) : box.fill(val));
    }
    const obs = await save(page, dialogs);
    const a = await list(); const ta = await rows(page);
    const m = a.find((p) => p.id === M.id);
    console.log(`${label}: tiêu đề form sau khi bấm 'Sửa'=${JSON.stringify(title)}; ${obs}; bản ghi ${b.length} → ${a.length}`);
    console.log(`      M TRƯỚC (GET /api/products): ${JSON.stringify({ id: M.id, name: M.name, price: M.price, category_id: M.category_id })}`);
    console.log(`      M SAU   (GET /api/products): ${JSON.stringify({ id: m.id, name: short(m.name), price: m.price, category_id: m.category_id })}`);
    console.log(`      bảng TRƯỚC: ${JSON.stringify(tb)}`);
    console.log(`      bảng SAU:   ${JSON.stringify(ta.map(short))}`);
    await page.close();
  }

  console.log('===== BUG-35 (Thêm — Tên vi phạm; Giá 1500000; Danh mục Laptop)');
  await add('A 300×x  (TC-08)', 'x'.repeat(300), '1500000');
  await add('B "   "  (TC-09)', '   ', '1500000');
  await add('C 256×x  (TC-66)', 'x'.repeat(256), '1500000');

  console.log('===== BUG-36 (Thêm — Tên "Tai nghe UI10"; Giá vi phạm; Danh mục Laptop)');
  await add('-1000            (TC-10)', 'Tai nghe UI10', '-1000');
  await add('0                (TC-67)', 'Tai nghe UI10', '0');
  await add('để trống         (TC-11, TC-205 theo bước SV)', 'Tai nghe UI10', '');
  await add('gõ "１５０００００" (input thật của TC-205, kiểm thêm)', 'Tai nghe UI10', '１５０００００');

  console.log("===== BUG-37 (Sửa — chọn dòng 'iPhone 15 Pro Max'; Tên vi phạm)");
  await edit('300×x  (TC-13)', 'iPhone 15 Pro Max', [['Tên sản phẩm', 'x'.repeat(300)]]);
  await edit('"   "  (TC-14)', 'iPhone 15 Pro Max', [['Tên sản phẩm', '   ']]);
  await edit('256×x  (TC-78)', 'iPhone 15 Pro Max', [['Tên sản phẩm', 'x'.repeat(256)]]);

  console.log("===== BUG-38 (Sửa — chọn dòng 'iPhone 15 Pro Max'; Giá vi phạm)");
  await edit('-1000    (TC-15)', 'iPhone 15 Pro Max', [['Giá tiền', '-1000']]);
  await edit('0        (TC-79)', 'iPhone 15 Pro Max', [['Giá tiền', '0']]);
  await edit('để trống (TC-16)', 'iPhone 15 Pro Max', [['Giá tiền', '']]);

  console.log('===== BUG-39 (Thêm — Tên <script>alert(1)</script>)');
  await add('TC-200', '<script>alert(1)</script>', '1500000');

  console.log('===== BUG-40 (Thêm — Tên "Sản phẩm E-Notation"; Giá 1e5)');
  await add('TC-201', 'Sản phẩm E-Notation', '1e5');

  console.log('===== BUG-45 (Sửa — Tên "Sửa UI03", Giá 2500000)');
  console.log(`   [${restart()}]`);
  console.log(`   bước 2 SV ghi "ví dụ sản phẩm id = 8": GET /api/products/8 sau seed -> ${JSON.stringify(await (await api.get(`${API}/api/products/8`)).json())}; id trong CSDL: ${JSON.stringify((await list()).map((p) => p.id))}; bảng UI không có cột id`);
  await edit("thay bằng dòng seed 'iPhone 15 Pro Max' (id 1)", 'iPhone 15 Pro Max', [['Tên sản phẩm', 'Sửa UI03'], ['Giá tiền', '2500000']]);

  console.log("===== BUG-49 + BUG-50 (quan sát form 'Thêm sản phẩm mới' và cột 'Giá')");
  console.log(`   [${restart()}]`);
  {
    const { page } = await open();
    const f = page.locator('form', { has: page.getByRole('button', { name: 'Lưu sản phẩm' }) });
    console.log(`BUG-49: tiêu đề form=${JSON.stringify(await formTitle(page))}; số <label> trong form=${await f.locator('label').count()}; có '*' trong form=${(await f.innerText()).includes('*')}; placeholder=${JSON.stringify(await f.locator('input,textarea').evaluateAll((es) => es.map((e) => e.placeholder)))}; số <select>=${await f.locator('select').count()}`);
    console.log(`BUG-50: ô Giá dòng 'iPhone 15 Pro Max' = ${JSON.stringify(await page.locator('table tbody tr', { hasText: 'iPhone 15 Pro Max' }).locator('td').nth(2).innerText())}`);
    await page.close();
  }
  await browser.close();
  console.log(`===== kết thúc   [${restart()}]`);
  await api.dispose();
})();
