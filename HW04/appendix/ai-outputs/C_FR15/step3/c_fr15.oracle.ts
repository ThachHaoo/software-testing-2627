/**
 * C_FR15 – đọc expected (nguyên văn HW02) thành oracle. Không phụ thuộc Playwright (kiểm offline bằng node).
 * Không nhận dạng được loại kết quả → ném lỗi. Cụm expected không ánh xạ được assertion → `unmapped` (spec ghi annotation).
 * Tên dạng "'x' × n" giữ nguyên trong oracle (spec mở rộng bằng expandValue); {ts} spec thay lúc chạy.
 */
export type CName = string;                      // chuỗi trong nháy đơn của expected, có thể là "'x' × n"
export type COracle = {
  kind: 'add' | 'edit' | 'del' | 'reject' | 'sv';
  noErr?: boolean;                               // "Không có thông báo lỗi"
  errShown?: boolean;                            // "Có thông báo lỗi" / "Báo lỗi"
  table: {
    addedRow?: { name?: CName; price?: number }; // "SAU_UI có thêm đúng 1 dòng 'Tên SP' = …, 'Giá' = …"
    mRow?: { name?: CName; price?: number };     // "dòng của M hiển thị 'Tên SP' = …, 'Giá' = …"
    othersSame?: boolean;                        // "mọi dòng khác SAU_UI = TRƯỚC_UI"
    countSame?: boolean;                         // "số dòng không đổi"
    unchanged?: boolean;                         // "SAU_UI = TRƯỚC_UI"
    gone?: CName;                                // "dòng 'X' không còn"
    countDelta?: number;                         // "số dòng SAU_UI = TRƯỚC_UI − 1"
  };
  data: {
    countDelta?: number;                         // "số bản ghi SAU = TRƯỚC + 1 | − 1" / "số bản ghi SAU = TRƯỚC" (0)
    newRec?: { name?: CName; price?: number; category_id?: number };
    m?: { name?: CName; price?: number; category_id?: number };
    keep?: ('price' | 'category_id' | 'name')[];  // "price, category_id = M_TRƯỚC"
    mSame?: boolean;                             // "M_SAU = M_TRƯỚC"
    listSame?: boolean;                          // "GET /api/products SAU = TRƯỚC"
    mGone?: boolean;                             // "GET /api/products SAU không còn id M"
  };
  noXssAlert?: boolean;                          // "không kích hoạt alert XSS"
  formBlocked?: boolean;                         // "Form chặn"
  unmapped: string[];
};

const q = String.raw`'((?:[^']|'(?= × ))*?)'(?: × (\d+))?`;   // 'chuỗi' hoặc 'x' × n
const nameFrom = (m: RegExpExecArray, i: number): CName => (m[i + 1] ? `'${m[i]}' × ${m[i + 1]}` : m[i]);
const numRe = String.raw`(-?\d+(?:\.\d+)?)`;

export function parseExpectedC(expected: string): COracle {
  const o: COracle = { kind: 'sv', table: {}, data: {}, unmapped: [] };
  let rest = expected;
  const strip = (t: string) => { rest = rest.replace(t, ' '); };
  const hit = (re: RegExp) => { const m = re.exec(expected); if (m) strip(m[0]); return m; };
  let m: RegExpExecArray | null;

  if (hit(/^Không có thông báo lỗi(?: \([^)]*\))?\./)) o.noErr = true;
  if (hit(/^Có thông báo lỗi(?: \([^)]*\))?(?: \([^)]*\))?\./)) o.errShown = true;
  if (hit(/^Báo lỗi;/)) o.errShown = true;
  hit(/^Không đánh giá thông báo\./);

  if ((m = hit(new RegExp(String.raw`SAU_UI có thêm đúng 1 dòng 'Tên SP' = ${q}(?:, 'Giá' = ${numRe} \(so giá trị số\))?\.`)))) {
    o.table.addedRow = { name: nameFrom(m, 1), ...(m[3] ? { price: +m[3] } : {}) };
  }
  if ((m = hit(new RegExp(String.raw`dòng của M hiển thị 'Tên SP' = ${q}(?:, 'Giá' = ${numRe} \(so giá trị số\))?[.;]`)))) {
    o.table.mRow = { name: nameFrom(m, 1), ...(m[3] ? { price: +m[3] } : {}) };
  }
  if (hit(/mọi dòng khác SAU_UI = TRƯỚC_UI;/)) o.table.othersSame = true;
  if (hit(/số dòng không đổi\./)) o.table.countSame = true;
  if (hit(/Bảng: SAU_UI = TRƯỚC_UI\./)) o.table.unchanged = true;
  if ((m = hit(new RegExp(String.raw`dòng ${q} không còn;`)))) o.table.gone = nameFrom(m, 1);
  if ((m = hit(/số dòng SAU_UI = TRƯỚC_UI ([+−-]) (\d+)\./))) o.table.countDelta = (m[1] === '+' ? 1 : -1) * +m[2];

  if ((m = hit(/số bản ghi SAU = TRƯỚC(?: ([+−-]) (\d+))?[.;]/))) o.data.countDelta = m[1] ? (m[1] === '+' ? 1 : -1) * +m[2] : 0;
  if ((m = hit(/bản ghi mới có (.*?)(?: \([^)]*\))?\.(?:\s|$)/))) {
    const seg = m[1]; const r: NonNullable<COracle['data']['newRec']> = {};
    let x: RegExpExecArray | null;
    if ((x = new RegExp(String.raw`name = ${q}`).exec(seg))) r.name = nameFrom(x, 1);
    if ((x = new RegExp(String.raw`price = ${numRe}`).exec(seg))) r.price = +x[1];
    if ((x = /category_id = (\d+)/.exec(seg))) r.category_id = +x[1];
    if (!Object.keys(r).length) throw new Error(`[c_fr15] "bản ghi mới có …" không đọc được trường: ${seg}`);
    o.data.newRec = r;
  }
  if ((m = hit(/M_SAU có (.*?)(?: \([^)]*\))?(?:;|\.(?:\s|$))/))) {
    const seg = m[1]; const r: NonNullable<COracle['data']['m']> = {};
    let x: RegExpExecArray | null;
    if ((x = new RegExp(String.raw`name = ${q}`).exec(seg))) r.name = nameFrom(x, 1);
    if ((x = new RegExp(String.raw`price = ${numRe}`).exec(seg))) r.price = +x[1];
    if ((x = /category_id = (\d+)/.exec(seg))) r.category_id = +x[1];
    if (!Object.keys(r).length) throw new Error(`[c_fr15] "M_SAU có …" không đọc được trường: ${seg}`);
    o.data.m = r;
  }
  if ((m = hit(/((?:price|category_id|name)(?:, (?:price|category_id|name))*) = M_TRƯỚC;/))) o.data.keep = m[1].split(', ') as COracle['data']['keep'];
  if (hit(/M_SAU = M_TRƯỚC;/)) o.data.mSame = true;
  if (hit(/GET \/api\/products SAU = TRƯỚC\./)) o.data.listSame = true;
  if (hit(/GET \/api\/products SAU không còn id M;/)) o.data.mGone = true;
  if (hit(/tuyệt đối không kích hoạt alert XSS(?: \([^)]*\))?\./)) o.noXssAlert = true;
  if (hit(/^Form chặn do type=number\./)) o.formBlocked = true;

  // loại kết quả
  if (o.data.listSame || o.table.unchanged) o.kind = 'reject';
  else if (o.data.newRec || o.table.addedRow) o.kind = 'add';
  else if (o.data.m || o.table.mRow) o.kind = 'edit';
  else if (o.data.mGone || o.table.gone) o.kind = 'del';
  else if (o.noXssAlert || o.formBlocked) o.kind = 'sv';
  else throw new Error(`[c_fr15] không xác định được loại kết quả từ expected: ${expected}`);

  // phần dư (bỏ nhãn "Bảng:", "Dữ liệu:", dấu câu)
  for (const c of rest.replace(/(Bảng|Dữ liệu):/g, ' ').split(/[.;](?:\s|$)/).map(s => s.trim()).filter(Boolean))
    o.unmapped.push(c);
  return o;
}
