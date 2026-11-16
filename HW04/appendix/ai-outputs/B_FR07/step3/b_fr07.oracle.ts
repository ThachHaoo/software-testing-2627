/**
 * B_FR07 – đọc cột 'Thao tác' và 'expected' (nguyên văn HW02) thành thao tác + oracle. Không phụ thuộc Playwright
 * (chạy được bằng `node` để kiểm offline). Không nhận dạng được → ném lỗi (thao tác) hoặc ghi vào `unmapped`
 * (phần expected không ánh xạ được assertion — spec ghi annotation, không tự bịa).
 */

export type Op =
  | { k: 'detail'; id: number; qty: string; snapshot?: number }          // trang chi tiết: gõ Số lượng, bấm thêm ĐÚNG 1 lần
  | { k: 'home-link' }                                                    // ở trang giỏ: bấm link về trang chủ (vùng main)
  | { k: 'delete'; id: number; dialog: 'accept' | 'dismiss'; optional: boolean };

export type RowSpec = { name: string; price?: number; qty: number; subtotal: number };
export type Oracle = {
  before: { noTable?: boolean; illustration?: boolean; emptyText?: boolean; badgeZeroOrHidden?: boolean };
  feedback?: 'present' | 'absent';
  dialogConfirm?: boolean;
  countBefore?: number;
  countAfter?: number;
  unchanged?: boolean;                 // "giỏ không đổi"
  add: RowSpec[];                      // "0 → 1 dòng 'X', …"
  modify: { name: string; qty: number; qtyBefore: number; subtotal: number }[];
  remove: string[];                    // "không còn 'X'"
  keep: string[];                      // "dòng 'Y' không đổi" / "Số lượng dòng 'Y' không đổi"
  absent: string[];                    // "không xuất hiện dòng 'X'"
  clear?: boolean;                     // "1 → 0 dòng" + trạng thái giỏ trống
  emptyAfter?: boolean;
  total?: number | 'unchanged';
  totalIsSum?: boolean;                // "(= Thành tiền dòng còn lại)"
  badge?: number;
  urlAfterHome?: string;
  noAlert?: boolean;
  phases: Record<number, { rows: { id: number; qty: number }[]; count?: number; feedback?: boolean }>;
  unmapped: string[];
};

const unquote = (s: string) => {
  const m = /^'(.*)'(?: \(.*\))?$/.exec(s.trim());
  return m ? m[1] : s.trim();
};

export function parseActions(text: string): Op[] {
  const t = text.trim();
  let m = /^CT: id (\d+), nhập (\S+), bấm 'Thêm' \*\*1 lần\*\*, mở \/cart \(ghi giỏ\); quay lại, nhập (\S+), bấm 'Thêm' \*\*1 lần\*\*, mở \/cart$/.exec(t);
  if (m) return [{ k: 'detail', id: +m[1], qty: m[2], snapshot: 1 }, { k: 'detail', id: +m[1], qty: m[3], snapshot: 2 }];
  const ops: Op[] = [];
  for (const part of t.split(', rồi ')) {
    if (/^(Ở|ở) trang giỏ:? bấm link về trang chủ$/.test(part)) { ops.push({ k: 'home-link' }); continue; }
    if ((m = /^CT: id (\d+) × (.*)$/.exec(part))) { ops.push({ k: 'detail', id: +m[1], qty: unquote(m[2]) }); continue; }
    if ((m = /^Bấm nút xoá trên dòng id (\d+) → dialog( \(nếu có\))?: chọn (xác nhận|huỷ|hủy)$/.exec(part))) {
      ops.push({ k: 'delete', id: +m[1], optional: !!m[2], dialog: m[3] === 'xác nhận' ? 'accept' : 'dismiss' });
      continue;
    }
    throw new Error(`[b_fr07] không hiểu cột 'Thao tác': "${part}"`);
  }
  return ops;
}

/** Cụm đã được ánh xạ assertion hoặc chỉ là nối câu / tham chiếu giả định (không cần assertion riêng). */
const CONNECTORS = [
  /^TRƯỚC → SAU$/, /^Sau khi xác nhận$/, /^Sau khi bấm nút xoá$/, /^Ngay sau khi bấm thêm$/, /^Bấm thêm$/,
  /^Trong ≤ 2 giây sau khi bấm 'Thêm vào giỏ hàng'$/, /^ghi loại phản hồi vào Actual$/, /^Bước 3$/, /^Sau thao tác$/,
  /^Sau khi bấm link về trang chủ(?: \(giỏ có hàng\))?$/, /^và$/, /^Ngay khi gõ\/paste$/,
];

export function parseExpected(expected: string, seed: { id: number; name: string; price: number }[]): Oracle {
  const o: Oracle = { before: {}, add: [], modify: [], remove: [], keep: [], absent: [], phases: {}, unmapped: [] };
  let e = expected;
  let rest = expected;                   // phần expected chưa ánh xạ — mỗi lần khớp thì xoá đoạn đã khớp
  const strip = (t: string) => { rest = rest.replace(t, ' '); };
  const hit = (re: RegExp, s = e) => { const m = re.exec(s); if (m) strip(m[0]); return m; };
  const all = (re: RegExp, s = e) => { const ms = [...s.matchAll(re)]; ms.forEach(x => strip(x[0])); return ms; };

  // "Sau lần k: …" (case nhiều lần thêm) — xử lý riêng rồi bỏ khỏi chuỗi
  for (const m of [...e.matchAll(/Sau lần (\d+): (.*?)(?=Sau lần \d+:|$)/g)]) {
    const seg = m[2];
    const ph: Oracle['phases'][number] = { rows: [] };
    for (const r of seg.matchAll(/id (\d+) × (\d+)/g)) ph.rows.push({ id: +r[1], qty: +r[2] });
    const c = /(\d+) dòng/.exec(seg); if (c) ph.count = +c[1];
    if (/có phản hồi/.test(seg)) ph.feedback = true;
    if (!ph.rows.length) throw new Error(`[b_fr07] "Sau lần ${m[1]}" không có "id N × Q": ${seg}`);
    o.phases[+m[1]] = ph;
    e = e.replace(m[0], ''); strip(m[0]);
  }

  const b3 = /Bước 3: ([^.]*)\./.exec(e)?.[1] ?? '';
  if (b3) e = e.replace(b3, '');
  if (b3) {
    if (hit(/không có bảng sản phẩm/, b3)) o.before.noTable = true;
    if (hit(/có hình minh hoạ\/icon \(img hoặc svg\)/, b3)) o.before.illustration = true;
    if (hit(/dòng chữ báo giỏ trống/, b3)) o.before.emptyText = true;
    if (hit(/badge ẩn hoặc 0/, b3)) o.before.badgeZeroOrHidden = true;
  }
  let m: RegExpExecArray | null;
  if ((m = hit(/URL = (\S+?)\.?(?=\s|$)/))) o.urlAfterHome = m[1];
  if (hit(/có ít nhất một phản hồi nhìn thấy được gắn với lần thêm(?: \([^)]*\))?/)) o.feedback = 'present';
  if (hit(/không có phản hồi báo đã thêm/)) o.feedback = 'absent';
  if (hit(/hiện dialog xác nhận/)) o.dialogConfirm = true;
  for (const r of all(/(\d+) → (\d+) dòng '([^']+)', (?:Đơn giá (\d+), )?Số lượng (\d+), Thành tiền (\d+)/g)) {
    o.countBefore = +r[1]; o.countAfter = +r[2];
    o.add.push({ name: r[3], ...(r[4] ? { price: +r[4] } : {}), qty: +r[5], subtotal: +r[6] });
  }
  if ((m = hit(/(?:^|[^'\d])(\d+) → (\d+) dòng(?! ')/))) { o.countBefore = +m[1]; o.countAfter = +m[2]; if (+m[2] === 0) o.clear = true; }
  if ((m = hit(/vẫn (\d+) dòng/))) { o.countBefore = o.countAfter = +m[1]; }
  for (const r of all(/'([^']+)' Số lượng (\d+) → (\d+), Thành tiền SAU (\d+)/g)) o.modify.push({ name: r[1], qtyBefore: +r[2], qty: +r[3], subtotal: +r[4] });
  for (const r of all(/(?:Số lượng )?dòng '([^']+)' không đổi(?: \(Số lượng, Thành tiền SAU = TRƯỚC\))?/g)) o.keep.push(r[1]);
  for (const r of all(/không còn '([^']+)'/g)) o.remove.push(r[1]);
  for (const r of all(/không xuất hiện dòng '([^']+)'/g)) o.absent.push(r[1]);
  if (hit(/giỏ không đổi/)) o.unchanged = true;
  if (hit(/số dòng SAU = TRƯỚC/)) o.unchanged = true;
  if (hit(/Tổng SAU = Tổng TRƯỚC/)) o.total = 'unchanged';
  if ((m = hit(/Tổng(?: SAU)? (\d+)/))) o.total = +m[1];
  if (hit(/\(= Thành tiền dòng còn lại\)/)) o.totalIsSum = true;
  if ((m = hit(/badge SAU (\d+)/))) o.badge = +m[1];
  if (hit(/(?:trang giỏ )?không còn bảng sản phẩm(?: và)?/)) o.emptyAfter = true;
  if (hit(/chuyển sang trạng thái giỏ trống/)) o.emptyAfter = true;
  if (hit(/không bật alert(?: XSS)?/)) o.noAlert = true;
  if (hit(/ô input chặn hoặc không thực thi script/)) o.noAlert = true;

  // Phần còn lại không ánh xạ được → unmapped (spec ghi annotation, không tự bịa assertion)
  const leftovers = rest.replace(/\([^)]*\bB\d+[^)]*\)/g, ' ')                    // tham chiếu giả định HW02 (B2, B9, B21…)
    .split(/[.;:—,]\s*/).map(x => x.trim()).filter(Boolean);
  for (const c of leftovers) if (!CONNECTORS.some(re => re.test(c))) o.unmapped.push(c);

  const any = o.feedback || o.dialogConfirm || o.countAfter !== undefined || o.unchanged || o.add.length || o.modify.length
    || o.remove.length || o.absent.length || o.total !== undefined || o.urlAfterHome || o.noAlert || Object.keys(o.phases).length
    || Object.keys(o.before).length;
  if (!any) throw new Error(`[b_fr07] không đọc được oracle nào từ expected: ${expected}`);
  for (const ph of Object.values(o.phases)) for (const r of ph.rows)
    if (!seed.some(p => p.id === r.id)) throw new Error(`[b_fr07] id ${r.id} không có trong sản phẩm seed`);
  return o;
}
