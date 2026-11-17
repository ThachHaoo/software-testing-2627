# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: C_FR15.spec.ts >> TC-FR15-201 Kiểm tra nhập giá tiền dạng E-notation `1e5` vào ô 'Giá tiền'
- Location: C_FR15.spec.ts:70:3

# Error details

```
Error: form chặn: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 8

@@ -37,6 +37,14 @@
      "id": 5,
      "imageUrl": "https://placehold.co/300x300/png?text=Keychron+Q1",
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
    },
+   Object {
+     "category_id": 2,
+     "description": "Mô tả SV201 1794903183526",
+     "id": 6,
+     "imageUrl": "https://placehold.co/300",
+     "name": "Sản phẩm E-Notation 1794903183526",
+     "price": 100000,
+   },
  ]
```

# Page snapshot

```yaml
- generic [ref=e3]:
  - generic [ref=e4]:
    - heading "EShop Admin" [level=1] [ref=e5]
    - list [ref=e6]:
      - listitem [ref=e7] [cursor=pointer]: Dashboard
      - listitem [ref=e8] [cursor=pointer]: Danh mục
      - listitem [ref=e9] [cursor=pointer]: Sản phẩm
      - listitem [ref=e10] [cursor=pointer]: Mã Giảm Giá
      - listitem [ref=e11] [cursor=pointer]: Đơn hàng
      - listitem [ref=e12] [cursor=pointer]: Người dùng
      - listitem [ref=e13] [cursor=pointer]: Đăng xuất
  - generic [ref=e15]:
    - heading "Quản lý Sản phẩm" [level=2] [ref=e16]
    - generic [ref=e17]:
      - generic [ref=e18]:
        - heading "📂 Import sản phẩm từ CSV" [level=3] [ref=e19]
        - link "Tải file mẫu (template.csv)" [ref=e20] [cursor=pointer]:
          - /url: data:text/csv;charset=utf-8,…
      - generic [ref=e21]:
        - button "Choose File" [ref=e22]
        - button "Import 0 sản phẩm" [disabled] [ref=e23]
    - generic [ref=e24]:
      - heading "Thêm sản phẩm mới" [level=3] [ref=e25]
      - generic [ref=e26]:
        - textbox "Tên sản phẩm" [ref=e27]
        - spinbutton "Giá tiền" [ref=e28]
        - textbox "URL Ảnh" [ref=e29]
        - textbox "Mô tả" [ref=e30]
        - combobox [ref=e31]:
          - option "Điện thoại" [selected]
          - option "Laptop"
          - option "Phụ kiện"
      - button "Lưu sản phẩm" [active] [ref=e32] [cursor=pointer]
    - table [ref=e33]:
      - rowgroup [ref=e34]:
        - row [ref=e35]:
          - columnheader "Ảnh" [ref=e36]
          - columnheader "Tên SP" [ref=e37]
          - columnheader "Giá" [ref=e38]
          - columnheader "Hành động" [ref=e39]
      - rowgroup [ref=e40]:
        - row [ref=e41]:
          - cell [ref=e42]:
            - img "iPhone 15 Pro Max" [ref=e43]
          - cell "iPhone 15 Pro Max" [ref=e44]
          - cell "30000000 ₫" [ref=e45]
          - cell [ref=e46]:
            - button "Sửa" [ref=e47] [cursor=pointer]
            - button "Xóa" [ref=e48] [cursor=pointer]
        - row [ref=e49]:
          - cell [ref=e50]:
            - img "Samsung Galaxy S24 Ultra" [ref=e51]
          - cell "Samsung Galaxy S24 Ultra" [ref=e52]
          - cell "28000000 ₫" [ref=e53]
          - cell [ref=e54]:
            - button "Sửa" [ref=e55] [cursor=pointer]
            - button "Xóa" [ref=e56] [cursor=pointer]
        - row [ref=e57]:
          - cell [ref=e58]:
            - img "MacBook Pro M3" [ref=e59]
          - cell "MacBook Pro M3" [ref=e60]
          - cell "45000000 ₫" [ref=e61]
          - cell [ref=e62]:
            - button "Sửa" [ref=e63] [cursor=pointer]
            - button "Xóa" [ref=e64] [cursor=pointer]
        - row [ref=e65]:
          - cell [ref=e66]:
            - img "Tai nghe AirPods Pro 2" [ref=e67]
          - cell "Tai nghe AirPods Pro 2" [ref=e68]
          - cell "6000000 ₫" [ref=e69]
          - cell [ref=e70]:
            - button "Sửa" [ref=e71] [cursor=pointer]
            - button "Xóa" [ref=e72] [cursor=pointer]
        - row [ref=e73]:
          - cell [ref=e74]:
            - img "Bàn phím cơ Keychron Q1" [ref=e75]
          - cell "Bàn phím cơ Keychron Q1" [ref=e76]
          - cell "4000000 ₫" [ref=e77]
          - cell [ref=e78]:
            - button "Sửa" [ref=e79] [cursor=pointer]
            - button "Xóa" [ref=e80] [cursor=pointer]
        - row [ref=e81]:
          - cell [ref=e82]:
            - img "Sản phẩm E-Notation 1794903183526" [ref=e83]
          - cell "Sản phẩm E-Notation 1794903183526" [ref=e84]
          - cell "100000 ₫" [ref=e85]
          - cell [ref=e86]:
            - button "Sửa" [ref=e87] [cursor=pointer]
            - button "Xóa" [ref=e88] [cursor=pointer]
```

# Test source

```ts
  158 |         await until(`chờ ${method} /api/products`, () => !!sent(method));
  159 |         const s = sent(method)!;
  160 |         if (s.status !== 200) await until('chờ hộp thoại lỗi lưu', () => dialogs.length > n0);
  161 |         else if (op === 'Thêm') { const i = net.indexOf(s); await until('chờ GET /api/products sau khi thêm', () => !!listAfter(i)); await listAfter(i)!.done; }
  162 |         else await until("chờ hộp thoại sau khi lưu (Sửa)", () => dialogs.length > n0);
  163 |       }
  164 |     }
  165 |     await settle(page);
  166 |     const invalid: string[] = await page.evaluate(() => [...(window as unknown as { __inv: string[] }).__inv]);
  167 |     const newDialogs = dialogs.slice(n0);
  168 |     const pageMsgs = (await pageMessages()).filter(m => !msgBefore.includes(m));
  169 |     const errShown = invalid.length > 0 || newDialogs.length > 0 || pageMsgs.length > 0;
  170 |     ann('quan sát sau thao tác', JSON.stringify({
  171 |       'ô không hợp lệ HTML5': invalid, 'hộp thoại': newDialogs.map(d => d.message), 'thông báo mới trên trang': pageMsgs,
  172 |       'request': net.map(x => `${x.method} ${x.url.replace(API, '')} → ${x.status}`),
  173 |     }));
  174 |     // ảnh ngay sau thao tác chính, chụp SAU khi đo xong (không song song với việc chờ/đo)
  175 |     await info.attach(`${c.tc_id}_after-save`, { body: await page.screenshot(), contentType: 'image/png' });
  176 | 
  177 |     // Bước 7: SAU_UI, GET SAU (+ M_SAU)
  178 |     const tAfter = await table.read();
  179 |     const after = await catalog.list();
  180 |     const mAfter = M ? await catalog.get(M.id) : null;
  181 |     priceIsString('M_SAU', mAfter);
  182 |     const added = after.filter(p => !before.some(b => b.id === p.id));
  183 |     const tAdded = tAfter.filter(x => !tBefore.some(y => y.name === x.name && y.priceRaw === x.priceRaw));
  184 |     ann('SAU', JSON.stringify({
  185 |       'bản ghi': `${before.length} → ${after.length}`, 'bản ghi mới': added.map(p => ({ ...p, name: short(p.name) })),
  186 |       'bảng': `${tBefore.length} → ${tAfter.length} dòng`, 'dòng mới/đổi': tAdded.map(r => `${short(r.name)} | ${r.priceRaw}`),
  187 |       ...(M ? { M_SAU: mAfter } : {}),
  188 |     }));
  189 | 
  190 |     // ---- Oracle: thông báo ----
  191 |     if (o.noErr) expect.soft(errShown, 'không có thông báo lỗi (EC73)').toBe(false);
  192 |     if (o.errShown) {
  193 |       expect.soft(errShown, 'có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)').toBe(true);
  194 |       if (errShown && !invalid.length && !pageMsgs.length)
  195 |         ann('oracle thông báo yếu', `chỉ có hộp thoại ${JSON.stringify(newDialogs.map(d => d.message))} — đếm là "có thông báo" như HW02 (H4: không phân loại nội dung), SV xét`);
  196 |     }
  197 | 
  198 |     // ---- Oracle: bảng (UI) ----
  199 |     if (o.table.unchanged) expect.soft(tAfter, 'bảng SAU_UI = TRƯỚC_UI').toEqual(tBefore);
  200 |     if (o.table.addedRow) {
  201 |       expect.soft(tAfter.length, 'bảng có thêm đúng 1 dòng').toBe(tBefore.length + 1);
  202 |       const want = o.table.addedRow.name !== undefined ? nameOf(o.table.addedRow.name, ts) : undefined;
  203 |       const row: TableRow | undefined = want !== undefined ? tAdded.find(r => r.name === want) : tAdded[0];
  204 |       if (want !== undefined) {
  205 |         await expect.soft(table.row(want), `bảng có đúng 1 dòng 'Tên SP' = '${short(want)}'`).toHaveCount(1);
  206 |         await expect.soft(table.row(want).first(), `dòng mới '${short(want)}' hiển thị`).toBeVisible();
  207 |       }
  208 |       if (o.table.addedRow.price !== undefined) expect.soft(row?.price, "dòng mới: 'Giá' (so giá trị số)").toBe(o.table.addedRow.price);
  209 |     }
  210 |     if (o.table.mRow) {
  211 |       const cell = table.rows.nth(mRowIdx).locator('td').nth(1);
  212 |       if (o.table.mRow.name !== undefined) await expect.soft(cell, "dòng của M: 'Tên SP'").toHaveText(nameOf(o.table.mRow.name, ts));
  213 |       if (o.table.mRow.price !== undefined) expect.soft(tAfter[mRowIdx]?.price, "dòng của M: 'Giá' (so giá trị số)").toBe(o.table.mRow.price);
  214 |     }
  215 |     if (o.table.othersSame)
  216 |       expect.soft(tAfter.filter((_, i) => i !== mRowIdx), 'mọi dòng khác SAU_UI = TRƯỚC_UI').toEqual(tBefore.filter((_, i) => i !== mRowIdx));
  217 |     if (o.table.countSame) await expect.soft(table.rows, 'số dòng không đổi').toHaveCount(tBefore.length);
  218 |     if (o.table.gone !== undefined) await expect.soft(table.row(nameOf(o.table.gone, ts)), `bảng không còn dòng '${nameOf(o.table.gone, ts)}'`).toHaveCount(0);
  219 |     if (o.table.countDelta !== undefined) await expect.soft(table.rows, 'số dòng SAU_UI').toHaveCount(tBefore.length + o.table.countDelta);
  220 | 
  221 |     // ---- Oracle: dữ liệu (API GET trước/sau) ----
  222 |     if (o.data.listSame) expect.soft(byId(after), 'GET /api/products SAU = TRƯỚC').toEqual(byId(before));
  223 |     if (o.data.mSame) expect.soft(mAfter, 'M_SAU = M_TRƯỚC').toEqual(mBefore);
  224 |     if (o.data.countDelta !== undefined) expect.soft(after.length, 'số bản ghi SAU').toBe(before.length + o.data.countDelta);
  225 |     if (o.data.newRec) {
  226 |       const n = added[0];
  227 |       const want: Record<string, unknown> = {}, got: Record<string, unknown> = {};
  228 |       if (o.data.newRec.name !== undefined) { want.name = nameOf(o.data.newRec.name, ts); got.name = n?.name; }
  229 |       if (o.data.newRec.price !== undefined) { want.price = o.data.newRec.price; got.price = numish(n?.price); }
  230 |       if (o.data.newRec.category_id !== undefined) { want.category_id = o.data.newRec.category_id; got.category_id = numish(n?.category_id); }
  231 |       expect.soft(got, `bản ghi mới (so giá trị số), thấy ${n ? JSON.stringify({ ...n, name: short(n.name) }) : 'không có'}`).toEqual(want);
  232 |       if (o.data.newRec.price !== undefined) expect.soft(sameNumber(n?.price, o.data.newRec.price), 'price bản ghi mới (sameNumber như HW02)').toBe(true);
  233 |     }
  234 |     if (o.data.m) {
  235 |       const m = mAfter as Product | null;
  236 |       const want: Record<string, unknown> = {}, got: Record<string, unknown> = {};
  237 |       if (o.data.m.name !== undefined) { want.name = nameOf(o.data.m.name, ts); got.name = m?.name; }
  238 |       if (o.data.m.price !== undefined) { want.price = o.data.m.price; got.price = numish(m?.price); }
  239 |       if (o.data.m.category_id !== undefined) { want.category_id = o.data.m.category_id; got.category_id = numish(m?.category_id); }
  240 |       expect.soft(got, 'M_SAU (so giá trị số)').toEqual(want);
  241 |     }
  242 |     if (o.data.keep) {
  243 |       const k = o.data.keep;
  244 |       expect.soft(k.map(x => String((mAfter as Record<string, unknown> | null)?.[x])), `M_SAU ${k.join(', ')} = M_TRƯỚC`)
  245 |         .toEqual(k.map(x => String((mBefore as Record<string, unknown> | null)?.[x])));
  246 |     }
  247 |     if (o.data.mGone) expect.soft(after.map(p => p.id), 'GET /api/products SAU không còn id M').not.toContain(M!.id);
  248 | 
  249 |     // ---- Oracle: case SV ----
  250 |     if (o.noXssAlert) {
  251 |       const xss = assumption('xss_alert_text');
  252 |       const re = new RegExp(`^\\s*${esc(xss.value)}\\s*$`);
  253 |       expect.soft(newDialogs.filter(d => re.test(d.message)), `không kích hoạt alert XSS (không có hộp thoại '${xss.value}' — ${xss.note})`).toEqual([]);
  254 |     }
  255 |     if (o.formBlocked) {
  256 |       const fb = assumption('form_blocked_means');
  257 |       ann('oracle Form chặn', `${fb.value} (${fb.note})`);
> 258 |       expect.soft(byId(after), `form chặn: ${fb.value}`).toEqual(byId(before));
      |                                                          ^ Error: form chặn: GET /api/products SAU = TRƯỚC
  259 |     }
  260 |   });
  261 | }
  262 | 
```