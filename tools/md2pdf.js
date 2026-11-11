// Xuất Markdown → PDF bằng Chromium của Playwright (giữ bảng và ảnh; đường dẫn ảnh tính từ thư mục của file .md).
// Dùng (từ gốc repo): node tools/md2pdf.js HW02/23120255_HW02_Report.md [file2.md ...]
// Cần: npm install trong HW02/tests (marked, @playwright/test) và `npx playwright install chromium`.
const path = require('path');
const fs = require('fs');
const os = require('os');
const { pathToFileURL } = require('url');
const req = (m) => require(require.resolve(m, { paths: [path.join(__dirname, '..', 'HW02', 'tests'), path.join(__dirname, '..', 'HW03', 'tests')] }));
const { marked } = req('marked');
const { chromium } = req('playwright');

const CSS = `
  body { font-family: "Segoe UI", Arial, sans-serif; font-size: 9pt; line-height: 1.35; color: #111; }
  h1 { font-size: 16pt; } h2 { font-size: 13pt; border-bottom: 1px solid #999; margin-top: 18pt; }
  h3 { font-size: 11pt; } h4 { font-size: 10pt; }
  table { border-collapse: collapse; width: 100%; margin: 6pt 0; table-layout: auto; }
  th, td { border: 1px solid #888; padding: 2pt 4pt; vertical-align: top; word-break: break-word; overflow-wrap: anywhere; }
  th { background: #eee; }
  tr { page-break-inside: avoid; }
  code { font-family: Consolas, monospace; font-size: 8.5pt; background: #f3f3f3; }
  pre { white-space: pre-wrap; word-break: break-word; background: #f6f6f6; padding: 4pt; font-size: 8pt; }
  blockquote { color: #444; border-left: 3px solid #bbb; margin: 4pt 0; padding-left: 6pt; }
  img { max-width: 100%; height: auto; page-break-inside: avoid; }
  td img { max-height: 70px; width: auto; }  /* ảnh trong ô bảng (vd chữ ký) */
`;

(async () => {
  const files = process.argv.slice(2);
  if (!files.length) { console.error('Cần ít nhất một file .md'); process.exit(1); }
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const f of files) {
    const abs = path.resolve(f);
    const md = fs.readFileSync(abs, 'utf8');
    const base = pathToFileURL(path.dirname(abs) + path.sep).href;
    const html = `<!doctype html><html><head><meta charset="utf-8"><base href="${base}"><style>${CSS}</style></head><body>${marked.parse(md)}</body></html>`;
    const tmp = path.join(os.tmpdir(), `md2pdf_${process.pid}_${path.basename(abs)}.html`);
    fs.writeFileSync(tmp, html, 'utf8');
    await page.goto(pathToFileURL(tmp).href, { waitUntil: 'load' });
    const out = abs.replace(/\.md$/i, '.pdf');
    await page.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: '12mm', bottom: '12mm', left: '10mm', right: '10mm' },
                     displayHeaderFooter: true, headerTemplate: '<span></span>',
                     footerTemplate: '<div style="font-size:7pt;width:100%;text-align:center;"><span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
    fs.unlinkSync(tmp);
    console.log(`Đã xuất ${path.relative(process.cwd(), out)} (${(fs.statSync(out).size / 1024).toFixed(0)} KB)`);
  }
  await browser.close();
})();
