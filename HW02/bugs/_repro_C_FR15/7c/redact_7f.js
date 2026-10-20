// 7f — bản che để đăng issue: thay đường dẫn máy bằng <SUT_DIR> (evidence gốc giữ nguyên).
// Chạy: node redact_7f.js (NODE_PATH = HW02/tests/node_modules). Ảnh render như renderResponse() ở tests/C_FR15/lib.ts.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const HW = path.resolve(__dirname, '../../..');
const OUT = path.join(HW, 'bugs/_issue_redacted');
const SUT = /D:\\HK7\\Testing\\Exercise\\HW\\eshop-sut/g;
const esc = (s) => s.replace(/[&<>]/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[ch]));

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const [bug, tc] of [['BUG-43', 'TC-FR15-209'], ['BUG-44', 'TC-FR15-211']]) {
    const req = JSON.parse(fs.readFileSync(path.join(HW, `C_FR15/evidence/${tc}_req.json`), 'utf-8'));
    const res = JSON.parse(fs.readFileSync(path.join(HW, `C_FR15/evidence/${tc}_res.json`), 'utf-8'));
    const body = res.body.replace(SUT, '<SUT_DIR>');
    fs.writeFileSync(path.join(OUT, `${bug}.txt`), `# ${bug}: body phản hồi của ${tc} (HTTP ${res.status}), nguồn HW02/C_FR15/evidence/${tc}_res.json; đường dẫn tuyệt đối thay bằng <SUT_DIR>\n\n${body}\n`, 'utf-8');
    await page.setContent(`<pre style="font:14px monospace;white-space:pre-wrap">${esc(`${req.method} ${req.url}\n${req.body}\n\nHTTP ${res.status}\n${body}`)}</pre>`);
    await page.screenshot({ path: path.join(OUT, `${tc}_api_redacted.png`), fullPage: true });
  }
  await browser.close();
  // BUG-48: stderr khi backend dừng (7c2/7e)
  const md = fs.readFileSync(path.join(HW, 'bugs/BUG-48.md'), 'utf-8');
  const err = md.match(/```text\r?\n([\s\S]*?)\r?\n {2}```/)[1].split(/\r?\n/).map((l) => l.replace(/^ {2}/, '')).join('\n');
  fs.writeFileSync(path.join(OUT, 'BUG-48.txt'), `# BUG-48: stderr của tiến trình node server.js khi dừng (GET /api/products/6, id chẵn, price null), nguồn HW02/bugs/BUG-48.md mục "Sập backend"; đường dẫn tuyệt đối thay bằng <SUT_DIR>\n\n${err.replace(SUT, '<SUT_DIR>')}\n`, 'utf-8');
  console.log(fs.readdirSync(OUT).join('\n'));
})();
