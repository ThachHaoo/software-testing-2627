# Dữ kiện Fail — FR-15 Quản lý Sản phẩm (C_FR15)

> Dữ kiện do AI gom ở bước 7a, chưa phải bug report. Sửa ở 7a2: bỏ C8 (G3, G4, G9) và C17 (G16) khỏi yêu cầu bị vi phạm — giả định phạm vi/nới, không bị vi phạm; điền cột BUG theo mapping SV. **SV quyết G nào thành BUG nào** (gộp/tách), tiêu đề, severity, priority.
> Nhóm G chỉ gom các case có triệu chứng quan sát được giống nhau (tầng + quan sát). Không có tên bug, severity, priority hay kết luận nguyên nhân.
> Nguồn: `HW02/C_FR15/testcases.json` sau commit 6/7d (lượt chính thức = lượt 6, `results/C_FR15_20261020-185355.json`; manual TC-90…94). Đoạn code trích nguyên văn để SV đối chiếu (gray-box), không bình luận.
> BUG kế tiếp: **BUG-35**; issue mới trên tkob-team/eshop-sut sẽ từ **#181** trở đi.

## Ánh xạ nhóm → bug → issue (SV điền)

| Nhóm | BUG | Issue |
|---|---|---|
| G1 | BUG-35 | [#181](https://github.com/tkob-team/eshop-sut/issues/181) |
| G2 | BUG-36 | [#182](https://github.com/tkob-team/eshop-sut/issues/182) |
| G3 | BUG-37 | [#183](https://github.com/tkob-team/eshop-sut/issues/183) |
| G4 | BUG-38 | [#184](https://github.com/tkob-team/eshop-sut/issues/184) |
| G5 | BUG-45 | [#191](https://github.com/tkob-team/eshop-sut/issues/191) |
| G6 | BUG-39 | [#185](https://github.com/tkob-team/eshop-sut/issues/185) |
| G7 | BUG-40 | [#186](https://github.com/tkob-team/eshop-sut/issues/186) |
| G8 | BUG-41 | [#187](https://github.com/tkob-team/eshop-sut/issues/187) |
| G9 | BUG-42 | [#188](https://github.com/tkob-team/eshop-sut/issues/188) |
| G10 | BUG-46 | [#192](https://github.com/tkob-team/eshop-sut/issues/192) |
| G11 | BUG-47 | [#193](https://github.com/tkob-team/eshop-sut/issues/193) |
| G12 | BUG-48 | [#194](https://github.com/tkob-team/eshop-sut/issues/194) |
| G13 | BUG-43 | [#189](https://github.com/tkob-team/eshop-sut/issues/189) |
| G14 | BUG-44 | [#190](https://github.com/tkob-team/eshop-sut/issues/190) |
| G15 | BUG-49 | [#195](https://github.com/tkob-team/eshop-sut/issues/195) |
| G16 | BUG-50 | [#196](https://github.com/tkob-team/eshop-sut/issues/196) |

## Tổng hợp

| Nhóm | Số Fail | Blocked ghi case gốc | Yêu cầu / giả định bị vi phạm |
|---|---|---|---|
| G1 | 3 | 0 | FR-15.2 (TC-08, 66: 300/256 ký tự), C3 (TC-09: 3 dấu cách), C7 + C16 (không có thông báo lỗi) |
| G2 | 4 | 0 | FR-15.3 (TC-10: -1000; TC-67: 0; TC-11, 205: giá rỗng được lưu), C7 + C16 (không có thông báo lỗi) |
| G3 | 3 | 0 | FR-15.2 (TC-13: 300 ký tự; TC-78: 256 ký tự), C3 (TC-14), C7 + C16 (không có thông báo lỗi; hộp thoại duy nhất là 'Cập nhật thành công!') |
| G4 | 3 | 0 | FR-15.3 (TC-15: -1000; TC-79: 0; TC-16: rỗng), C7 + C16 |
| G5 | 1 | 5 | FR-15.5 (trên bảng UI: các sản phẩm khác hiển thị bị đổi tên), FR-15.1 – Xem (bảng không hiển thị giá mới của M; EC63) |
| G6 | 1 | 0 | C21 (SV chốt), C7 + C16 (không có thông báo lỗi) |
| G7 | 1 | 0 | C24 (SV chốt) |
| G8 | 17 | 0 | FR-15.2 (name: 23, 24, 25, 26, 27, 84, 100), FR-15.3 (price: 28, 29, 30, 31, 101, 208, 214), FR-15.4 (category_id: 32, 33, 34), C6, C9 (26, 27, 29, 30, 31, 33, 34), C3 (25), C11 (32), C23 (214) |
| G9 | 15 | 0 | FR-15.2 (35–39, 106, 112), FR-15.3 (40–43, 113), FR-15.4 (44–46), C6, C9 (38, 39, 41, 42, 43, 45, 46), C3 (37), C11 (44) |
| G10 | 3 | 0 | C10 |
| G11 | 9 | 0 | FR-12.2, SEC-02 (thiếu/sai token: 50, 51, 53, 54, 56, 57), SEC-03 (role user: 52, 55, 58) |
| G12 | 1 | 0 | C15; phần sập backend (7c, ngoài TC): ổn định tiến trình backend (ngầm định) — chưa đánh giá: FR-06 |
| G13 | 1 | 0 | C20 |
| G14 | 1 | 0 | C6 (không 5xx; SV ghi căn cứ C6, C9) |
| G15 | 1 | 0 | FR-22.1 |
| G16 | 1 | 0 | FR-21.3 |

Tổng Fail trong nhóm: 65; cộng TC-202 (loại riêng) = 66 — khớp 66 Fail của testcases.json. Blocked: TC-04, 80, 81, 82, 83 (case gốc TC-03, ghi ở G5).

### Loại riêng — không lập bug

- **TC-FR15-202:** lỗi thiết kế TC. Expected SV ghi 7000000, giá trị số của `00700000` là 700000; Actual 700000. Không phải lỗi SUT, không lập bug (notes 6c).

## Kiểm trùng issue

`gh api user` = ThachHaoo. `gh issue list -R tkob-team/eshop-sut --state all --limit 500`: 135 issue (mọi tác giả, gồm đã đóng; số lớn nhất #180; #31–48, #70–96 đã bị xoá — HTTP 410). Tìm theo: product/sản phẩm, /api/products, admin, giá/price, category/danh mục, token/auth/quyền, Infinity, text/plain, HTML, '*', ₫/phân cách, script/XSS, id không tồn tại.

**Không có issue nào về `/api/products` hoặc form/bảng sản phẩm của web admin.** Issue cùng dạng triệu chứng ở endpoint/màn hình khác (để SV so, không kết luận trùng):

| Nhóm | Issue | Tác giả | Tiêu đề (nguyên văn) |
|---|---|---|---|
| G8, G1, G2 | #51 | nphoang-itus | [BUG-FR16-03] Import không kiểm `price`: 0, âm, thập phân, chữ, rỗng đều được lưu |
| G8 | #52 | nphoang-itus | [BUG-FR16-04] Import không kiểm `category_id`: không tồn tại, chữ được lưu; giao diện đổi chữ và rỗng thành 1 mà không báo |
| G8, G1 | #66 | nphoang-itus | [BUG-FR16-09] Import chấp nhận `name` toàn khoảng trắng và dài hơn 255 ký tự |
| G8 | #178 | ThachHaoo | [FR-07] Endpoint POST /api/cart hoàn toàn thiếu validate payload, chấp nhận dữ liệu sai kiểu, id không tồn tại, quantity âm/thập phân/rỗng và lưu cả null khi gửi text/plain |
| G11 | #50 | nphoang-itus | [BUG-FR16-02] API import không kiểm `role = 'admin'`: user thường import được |
| G11 | #149, #150, #151 | henry-banana | [FR17-14] A regular user can create an administrator coupon · [FR17-15] A regular user can read the administrator coupon list · [FR17-16] A regular user can delete an administrator coupon |
| G13 | #180 | ThachHaoo | [FR-07] Endpoint POST /api/cart khi nhận JSON không hợp lệ (Infinity) trả về trang lỗi HTML 400 kèm stack trace văng ra ngoài thay vì JSON chuẩn chứa trường error |
| G14 | #26 | ThachHaoo | [FR-01] Gửi request POST /api/register với Content-Type: text/plain, văng lỗi HTTP 500 kèm trang HTML stack trace |
| G15 | #7, #28, #152 | nphoang-itus, ThachHaoo, henry-banana | [BUG-FR02-07] Trường bắt buộc của form đăng nhập không có ký hiệu `*` · [FR-01] Nhãn các trường bắt buộc trên form Đăng ký … không có ký hiệu dấu sao '*' · [FR17-17] Coupon form omits required-field markers |
| G6 | #16, #27, #122 | nphoang-itus, ThachHaoo, henry-banana | Stored XSS ở địa chỉ giao hàng (Web Admin), Họ Tên (đăng ký), tên hồ sơ — G6 khác ở chỗ script không chạy (SEC-04 đạt) |

Không thấy issue nào về: id không tồn tại trả 200 (G10), price trả dạng chuỗi (G12), bảng admin đổi tên mọi dòng sau Sửa (G5), định dạng tiền ở admin (G16), '1e5' (G7).

## Bước tái hiện — đã chạy thật (20/10/2026, sau lượt 6)

> Lệnh tái hiện do AI soạn để kiểm khả năng tái hiện; không dùng làm bước tái hiện trong BUG.

- API: Lệnh chung (Windows PowerShell 5.1, lưu file UTF-8 có BOM): `HW02/bugs/_repro_C_FR15/prelude.ps1` — đăng nhập admin@eshop.com / Admin123! lấy token; `$headers` chỉ có Authorization; `-ContentType` truyền riêng; body gửi dạng UTF-8 bytes; lỗi 4xx/5xx đọc body trong try/catch (`GetResponseStream()`, `Position = 0`). Mỗi script tự dựng dữ liệu (M) và tự xoá dữ liệu đã tạo.
- UI: Đã chạy kiểm bằng `HW02/bugs/_repro_C_FR15/ui_repro.js` (Playwright headless, đăng nhập admin, thao tác như các bước dưới), output dán bên dưới.
- Sau khi kiểm: **đã khởi động lại backend** (dừng tiến trình `node server.js` cũ, chạy lại trong `eshop-sut/backend`); GET /api/products còn đúng 5 sản phẩm seed id 1–5. Backend hiện chạy trong một cửa sổ thu nhỏ mới.
- Ghi chú khi viết lệnh (PowerShell 5.1): file .ps1 phải lưu UTF-8 có BOM (không BOM → chữ Việt trong body bị đọc sai); không đặt chuỗi JSON có `""` bên trong `"$(...)"` — PowerShell đổi `""` thành `"` làm hỏng body (lần chạy đầu của G9 bị lỗi này, đã sửa bằng cách gán biến trước khi in; output dưới đây là lần chạy sau khi sửa).


## G1 — UI · form Thêm: Tên vi phạm (dài hơn 255 ký tự, chỉ gồm khoảng trắng) → bản ghi được tạo, không có thông báo

- **TC Fail (3):** 08, 09, 66
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-15.2 (TC-08, 66: 300/256 ký tự), C3 (TC-09: 3 dấu cách), C7 + C16 (không có thông báo lỗi)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** FR-22.4 (không có thông báo nên chưa xét vị trí)
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-08 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 11, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx…
  - TC-FR15-09 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 12, name "   ", price 1500000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dò…
  - TC-FR15-66 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 63, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx…
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-08_ui.png`, `HW02/C_FR15/evidence/TC-FR15-09_ui.png`, `HW02/C_FR15/evidence/TC-FR15-66_ui.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 491–499:

```js
 491                  <input
 492                    placeholder="Tên sản phẩm"
 493                    className="border p-2 rounded"
 494                    value={productForm.name}
 495                    onChange={(e) =>
 496                      setProductForm({ ...productForm, name: e.target.value })
 497                    }
 498                    required
 499                  />
```

`backend/server.js` dòng 167–177:

```js
 167  app.post("/api/products", (req, res) => {
 168    const { name, price, description, imageUrl, category_id } = req.body;
 169    db.run(
 170      "INSERT INTO products (name, price, description, imageUrl, category_id) VALUES (?, ?, ?, ?, ?)",
 171      [name, price, description, imageUrl, category_id],
 172      function (err) {
 173        if (err) return res.status(500).json({ error: err.message });
 174        res.json({ message: "Product created", id: this.lastID });
 175      },
 176    );
 177  });
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Đăng nhập http://localhost:5174 bằng admin@eshop.com / Admin123!, bấm mục 'Sản phẩm'.
2. Ô 'Tên sản phẩm' dán chuỗi 256 ký tự 'x' (lần 2: gõ 3 dấu cách); ô 'Giá tiền' gõ 1500000; chọn danh mục 'Laptop'.
3. Bấm 'Lưu sản phẩm' một lần; quan sát thông báo và bảng; mở http://localhost:3000/api/products xem bản ghi mới.

Output (`ui_repro.js`):

```text
G1 Thêm, tên 256 ký tự: hộp thoại=[]; bản ghi 6 → 7; bản ghi mới={"id":128,"name":"<256 ký tự>","price":1500000,"description":"","imageUrl":"","category_id":2}
G1 Thêm, tên 3 dấu cách: hộp thoại=[]; bản ghi 7 → 8; bản ghi mới={"id":129,"name":"   ","price":1500000,"description":"","imageUrl":"","category_id":2}
```


## G2 — UI · form Thêm: Giá vi phạm (≤ 0, để trống; chữ số full-width dán vào ô thành rỗng) → bản ghi được tạo, không có thông báo

- **TC Fail (4):** 10, 11, 67, 205
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-15.3 (TC-10: -1000; TC-67: 0; TC-11, 205: giá rỗng được lưu), C7 + C16 (không có thông báo lỗi)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** FR-22.4
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-10 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "-1000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 13, name "Tai nghe UI10 1792497264050", price -1000, category_id 2}; bảng T…
  - TC-FR15-11 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 14, name "Tai nghe UI11 1792497267834", price "", category_id 2}; bảng TRƯỚC → S…
  - TC-FR15-67 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "0"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 64, name "Tai nghe BVA 67 1792497343940", price 0, category_id 2}; bảng TRƯỚC →…
  - TC-FR15-205 (Fail) — Expected: Form chặn không cho nhập/dán, hoặc báo lỗi Giá tiền bắt buộc/không hợp lệ; không lưu rác vào CSDL. · Actual: giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 108, name "SP FullWidth Price 1792497416268", price "", category_id 2}; bảng TRƯ…
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-10_ui.png`, `HW02/C_FR15/evidence/TC-FR15-11_ui.png`, `HW02/C_FR15/evidence/TC-FR15-67_ui.png`, `HW02/C_FR15/evidence/TC-FR15-205_ui.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 500–507:

```js
 500                  <input
 501                    placeholder="Giá tiền"
 502                    type="number"
 503                    className="border p-2 rounded"
 504                    value={productForm.price}
 505                    onChange={(e) =>
 506                      setProductForm({ ...productForm, price: e.target.value })
 507                    }
```

`backend/server.js` dòng 167–177:

```js
 167  app.post("/api/products", (req, res) => {
 168    const { name, price, description, imageUrl, category_id } = req.body;
 169    db.run(
 170      "INSERT INTO products (name, price, description, imageUrl, category_id) VALUES (?, ?, ?, ?, ?)",
 171      [name, price, description, imageUrl, category_id],
 172      function (err) {
 173        if (err) return res.status(500).json({ error: err.message });
 174        res.json({ message: "Product created", id: this.lastID });
 175      },
 176    );
 177  });
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Đăng nhập admin, mục 'Sản phẩm'.
2. Ô 'Tên sản phẩm' gõ 'repro G2'; ô 'Giá tiền' gõ -1000 (lần 2: để trống); danh mục 'Laptop'.
3. Bấm 'Lưu sản phẩm' một lần; quan sát thông báo, bảng và GET /api/products.

Output (`ui_repro.js`):

```text
G2 Thêm, giá -1000: hộp thoại=[]; bản ghi 8 → 9; bản ghi mới={"id":130,"name":"repro G2 1792498104231","price":-1000,"description":"","imageUrl":"","category_id":2}
G2 Thêm, giá để trống: hộp thoại=[]; bản ghi 9 → 10; bản ghi mới={"id":131,"name":"repro G2b 1792498104231","price":"","description":"","imageUrl":"","category_id":2}
```


## G3 — UI · form Sửa: Tên vi phạm → sản phẩm M bị ghi đè; hộp thoại 'Cập nhật thành công!'

- **TC Fail (3):** 13, 14, 78
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-15.2 (TC-13: 300 ký tự; TC-78: 256 ký tự), C3 (TC-14), C7 + C16 (không có thông báo lỗi; hộp thoại duy nhất là 'Cập nhật thành công!')
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** FR-22.4
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-13 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 16, name "Muc tieu 13 1792497274144", price "1000000", category_…
  - TC-FR15-14 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 17, name "Muc tieu 14 1792497277406", price 1000000, category_id…
  - TC-FR15-78 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "1000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 75, name "Muc tieu 78 1792497375297", price 1000000, category_id…
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-13_ui.png`, `HW02/C_FR15/evidence/TC-FR15-13_failed.png`, `HW02/C_FR15/evidence/TC-FR15-14_ui.png`, `HW02/C_FR15/evidence/TC-FR15-14_failed.png`, `HW02/C_FR15/evidence/TC-FR15-78_ui.png`, `HW02/C_FR15/evidence/TC-FR15-78_failed.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 105–116:

```js
 105    const handleProductSubmit = async (e) => {
 106      e.preventDefault();
 107      try {
 108        if (productForm.id) {
 109          await axios.put(`${API_URL}/products/${productForm.id}`, productForm);
 110          const fakeMassUpdatedProducts = products.map((p) => ({
 111            ...p,
 112            name: productForm.name,
 113          }));
 114          setProducts(fakeMassUpdatedProducts);
 115          alert("Cập nhật thành công!");
 116        } else {
```

`backend/server.js` dòng 179–189:

```js
 179  app.put("/api/products/:id", (req, res) => {
 180    const { name, price, description, imageUrl, category_id } = req.body;
 181    db.run(
 182      "UPDATE products SET name = ?, price = ?, description = ?, imageUrl = ?, category_id = ? WHERE id = ?",
 183      [name, price, description, imageUrl, category_id, req.params.id],
 184      function (err) {
 185        if (err) return res.status(500).json({ error: err.message });
 186        res.json({ message: "Product updated" });
 187      },
 188    );
 189  });
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Dựng M: POST /api/products (token admin) {name: 'repro G3 M', price: 1000000, category_id: 1, …}.
2. Đăng nhập admin, mục 'Sản phẩm', bấm 'Sửa' trên dòng 'repro G3 M'.
3. Xoá trắng ô 'Tên sản phẩm', gõ 3 dấu cách; bấm 'Lưu sản phẩm' một lần; quan sát hộp thoại và GET /api/products/<id M>.

Output (`ui_repro.js`):

```text
G3: hộp thoại=["Cập nhật thành công!"]; M TRƯỚC={"name":"repro G3 M 1792498104231","price":1000000}; M SAU={"name":"   ","price":"1000000","category_id":1}
```


## G4 — UI · form Sửa: Giá vi phạm (≤ 0, để trống) → sản phẩm M bị ghi đè; hộp thoại 'Cập nhật thành công!'

- **TC Fail (3):** 15, 16, 79
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-15.3 (TC-15: -1000; TC-79: 0; TC-16: rỗng), C7 + C16
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** FR-22.4
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-15 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "-1000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 18, name "Muc tieu 15 1792497280777", price "1000000", category_id…
  - TC-FR15-16 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: ""; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 19, name "Muc tieu 16 1792497284060", price 1000000, category_id 1} → M…
  - TC-FR15-79 (Fail) — Expected: Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệ… · Actual: giá trị ô Giá tiền trước khi lưu: "0"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 76, name "Muc tieu 79 1792497378516", price "1000000", category_id 1} …
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-15_ui.png`, `HW02/C_FR15/evidence/TC-FR15-15_failed.png`, `HW02/C_FR15/evidence/TC-FR15-16_ui.png`, `HW02/C_FR15/evidence/TC-FR15-16_failed.png`, `HW02/C_FR15/evidence/TC-FR15-79_ui.png`, `HW02/C_FR15/evidence/TC-FR15-79_failed.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 500–507:

```js
 500                  <input
 501                    placeholder="Giá tiền"
 502                    type="number"
 503                    className="border p-2 rounded"
 504                    value={productForm.price}
 505                    onChange={(e) =>
 506                      setProductForm({ ...productForm, price: e.target.value })
 507                    }
```

`backend/server.js` dòng 179–189:

```js
 179  app.put("/api/products/:id", (req, res) => {
 180    const { name, price, description, imageUrl, category_id } = req.body;
 181    db.run(
 182      "UPDATE products SET name = ?, price = ?, description = ?, imageUrl = ?, category_id = ? WHERE id = ?",
 183      [name, price, description, imageUrl, category_id, req.params.id],
 184      function (err) {
 185        if (err) return res.status(500).json({ error: err.message });
 186        res.json({ message: "Product updated" });
 187      },
 188    );
 189  });
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Dựng M như G3.
2. Đăng nhập admin, mục 'Sản phẩm', bấm 'Sửa' trên dòng M.
3. Xoá trắng ô 'Giá tiền', gõ 0; bấm 'Lưu sản phẩm' một lần; quan sát hộp thoại và GET /api/products/<id M>.

Output (`ui_repro.js`):

```text
G4: hộp thoại=["Cập nhật thành công!"]; M TRƯỚC={"name":"repro G4 M 1792498104231","price":1000000}; M SAU={"name":"repro G4 M 1792498104231","price":0,"category_id":1}
```


## G5 — UI · form Sửa hợp lệ: sau khi lưu, mọi dòng của bảng hiển thị 'Tên SP' = tên mới; ô 'Giá' của dòng M vẫn là giá cũ

- **TC Fail (1):** 03
- **Blocked ghi case gốc (5):** 04, 80, 81, 82, 83 — case gốc TC-FR15-03
- **Yêu cầu / giả định bị vi phạm:** FR-15.5 (trên bảng UI: các sản phẩm khác hiển thị bị đổi tên), FR-15.1 – Xem (bảng không hiển thị giá mới của M; EC63)
- **Đạt trong cùng case:** Dữ liệu: M_SAU có name/price/category_id mới (TC-03); FR-15.5 ở tầng dữ liệu đạt ở TC-FR15-19 (API, Pass)
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-03 (Fail) — Expected: Không đánh giá thông báo. Bảng: dòng của M hiển thị 'Tên SP' = 'Sửa UI03 {ts}', 'Giá' = 2500000 (so giá trị số); mọi dòng khác SAU_UI = TRƯỚC_UI; số dòng không … · Actual: giá trị ô Giá tiền trước khi lưu: "2500000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 8, name "Muc tieu 03 1792497243367", price "1000000", category_i…
  - TC-FR15-04 (Blocked) — Expected: Bảng: dòng của M hiển thị 'Giá' = 2500000.5 (so giá trị số). Dữ liệu: M_SAU có price = 2500000.5 (so giá trị số); name, category_id = M_TRƯỚC. · Actual: giá trị ô Giá tiền trước khi lưu: "2500000.5"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 9, name "Muc tieu 04 1792497246840", price 1000000, category_i…
  - TC-FR15-80 (Blocked) — Expected: Bảng: dòng của M hiển thị 'Giá' = 0.1 (so giá trị số). Dữ liệu: M_SAU có price = 0.1 (so giá trị số); name, category_id = M_TRƯỚC; số bản ghi SAU = TRƯỚC. · Actual: giá trị ô Giá tiền trước khi lưu: "0.1"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 77, name "Muc tieu 80 1792497381784", price 1000000, category_id 1} …
  - TC-FR15-81 (Blocked) — Expected: Bảng: dòng của M hiển thị 'Giá' = 0.2 (so giá trị số). Dữ liệu: M_SAU có price = 0.2 (so giá trị số); name, category_id = M_TRƯỚC; số bản ghi SAU = TRƯỚC. · Actual: giá trị ô Giá tiền trước khi lưu: "0.2"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 78, name "Muc tieu 81 1792497385011", price "1000000", category_id 1…
  - TC-FR15-82 (Blocked) — Expected: Bảng: dòng của M hiển thị 'Giá' = 1500000 (so giá trị số). Dữ liệu: M_SAU có price = 1500000 (so giá trị số); name, category_id = M_TRƯỚC; số bản ghi SAU = TRƯỚ… · Actual: giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 79, name "Muc tieu 82 1792497388349", price 1000000, category_id…
  - TC-FR15-83 (Blocked) — Expected: Bảng: dòng của M hiển thị 'Giá' = 1000000000000 (so giá trị số). Dữ liệu: M_SAU có price = 1000000000000 (so giá trị số); name, category_id = M_TRƯỚC; số bản gh… · Actual: giá trị ô Giá tiền trước khi lưu: "1000000000000"; hộp thoại: "Cập nhật thành công!"; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 80, name "Muc tieu 83 1792497391707", price "1000000", cat…
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-03_ui.png`, `HW02/C_FR15/evidence/TC-FR15-04_ui.png`, `HW02/C_FR15/evidence/TC-FR15-04_failed.png`, `HW02/C_FR15/evidence/TC-FR15-80_ui.png`, `HW02/C_FR15/evidence/TC-FR15-80_failed.png`, `HW02/C_FR15/evidence/TC-FR15-81_ui.png`, `HW02/C_FR15/evidence/TC-FR15-81_failed.png`, `HW02/C_FR15/evidence/TC-FR15-82_ui.png`, `HW02/C_FR15/evidence/TC-FR15-82_failed.png`, `HW02/C_FR15/evidence/TC-FR15-83_ui.png`, `HW02/C_FR15/evidence/TC-FR15-83_failed.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 105–116:

```js
 105    const handleProductSubmit = async (e) => {
 106      e.preventDefault();
 107      try {
 108        if (productForm.id) {
 109          await axios.put(`${API_URL}/products/${productForm.id}`, productForm);
 110          const fakeMassUpdatedProducts = products.map((p) => ({
 111            ...p,
 112            name: productForm.name,
 113          }));
 114          setProducts(fakeMassUpdatedProducts);
 115          alert("Cập nhật thành công!");
 116        } else {
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Dựng M như G3.
2. Đăng nhập admin, mục 'Sản phẩm'; ghi lại bảng.
3. Bấm 'Sửa' trên dòng M; ô 'Tên sản phẩm' gõ 'Sửa repro G5', ô 'Giá tiền' gõ 2500000; bấm 'Lưu sản phẩm'; đóng hộp thoại; so bảng với trước (không tải lại trang) và GET /api/products.

Output (`ui_repro.js`):

```text
G5: hộp thoại=["Cập nhật thành công!"]; M TRƯỚC={"name":"repro G5 M 1792498104231","price":1000000}; M SAU={"name":"Sửa repro G5 1792498104231","price":"2500000","category_id":1}
   bảng TRƯỚC (rút gọn): ["iPhone 15 Pro Max | 30000000 ₫", "Samsung Galaxy S24 Ultra | 28000000 ₫", …, "repro G5 M 1792498104231 | 1000000 ₫"]
   bảng SAU (rút gọn):   ["Sửa repro G5 1792498104231 | 30000000 ₫", "Sửa repro G5 1792498104231 | 28000000 ₫", …, "Sửa repro G5 1792498104231 | 1000000 ₫"]
```


## G6 — UI · form Thêm: Tên '<script>alert(1)</script>' → bản ghi được tạo, không có thông báo

- **TC Fail (1):** 200
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** C21 (SV chốt), C7 + C16 (không có thông báo lỗi)
- **Đạt trong cùng case:** SEC-04 trong cùng case: không có hộp thoại '1'; bảng hiển thị chữ nguyên văn
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-200 (Fail) — Expected: Báo lỗi; tuyệt đối không kích hoạt alert XSS (SEC-04, C21). · Actual: giá trị ô Giá tiền trước khi lưu: "1500000"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 105, name "<script>alert(1)</script>", price 1500000, category_id 2}; bản…
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-200_ui.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 491–499:

```js
 491                  <input
 492                    placeholder="Tên sản phẩm"
 493                    className="border p-2 rounded"
 494                    value={productForm.name}
 495                    onChange={(e) =>
 496                      setProductForm({ ...productForm, name: e.target.value })
 497                    }
 498                    required
 499                  />
```

`backend/server.js` dòng 167–177:

```js
 167  app.post("/api/products", (req, res) => {
 168    const { name, price, description, imageUrl, category_id } = req.body;
 169    db.run(
 170      "INSERT INTO products (name, price, description, imageUrl, category_id) VALUES (?, ?, ?, ?, ?)",
 171      [name, price, description, imageUrl, category_id],
 172      function (err) {
 173        if (err) return res.status(500).json({ error: err.message });
 174        res.json({ message: "Product created", id: this.lastID });
 175      },
 176    );
 177  });
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Đăng nhập admin, mục 'Sản phẩm'.
2. Ô 'Tên sản phẩm' gõ <script>alert(1)</script>; ô 'Giá tiền' 1500000; danh mục 'Laptop'.
3. Bấm 'Lưu sản phẩm' một lần; quan sát thông báo, bảng, GET /api/products.

Output (`ui_repro.js`):

```text
G6 Thêm, tên <script>: hộp thoại=[]; bản ghi 13 → 14; bản ghi mới={"id":135,"name":"<script>alert(1)</script>","price":1500000,"description":"","imageUrl":"","category_id":2}
```


## G7 — UI · form Thêm: Giá gõ dạng ký hiệu khoa học '1e5' → bản ghi được tạo với price 100000

- **TC Fail (1):** 201
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** C24 (SV chốt)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-201 (Fail) — Expected: Form chặn do type=number. · Actual: giá trị ô Giá tiền trước khi lưu: "1e5"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 106, name "Sản phẩm E-Notation 1792497408679", price 100000, category_id 2}; …
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-201_ui.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 500–507:

```js
 500                  <input
 501                    placeholder="Giá tiền"
 502                    type="number"
 503                    className="border p-2 rounded"
 504                    value={productForm.price}
 505                    onChange={(e) =>
 506                      setProductForm({ ...productForm, price: e.target.value })
 507                    }
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Đăng nhập admin, mục 'Sản phẩm'.
2. Ô 'Tên sản phẩm' gõ 'repro G7'; ô 'Giá tiền' gõ 1e5; danh mục 'Laptop'.
3. Bấm 'Lưu sản phẩm' một lần; quan sát bảng và GET /api/products.

Output (`ui_repro.js`):

```text
G7 Thêm, giá 1e5: hộp thoại=[]; bản ghi 14 → 15; bản ghi mới={"id":136,"name":"repro G7 1792498104231","price":100000,"description":"","imageUrl":"","category_id":2}
```


## G8 — API · POST /api/products với dữ liệu vi phạm FR-15.2–15.4 / sai kiểu / thiếu trường → HTTP 200 'Product created', bản ghi được tạo

- **TC Fail (17):** 23, 24, 25, 26, 27, 84, 100, 28, 29, 30, 31, 101, 208, 214, 32, 33, 34
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-15.2 (name: 23, 24, 25, 26, 27, 84, 100), FR-15.3 (price: 28, 29, 30, 31, 101, 208, 214), FR-15.4 (category_id: 32, 33, 34), C6, C9 (26, 27, 29, 30, 31, 33, 34), C3 (25), C11 (32), C23 (214)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-23 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":22}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 22, name "", price 1500000, category_id 2}
  - TC-FR15-24 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":23}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 23, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx…
  - TC-FR15-25 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":24}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 24, name "   ", price 1500000, category_id 2}
  - TC-FR15-26 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":25}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 25, name null, price 1500000, category_id 2}
  - TC-FR15-27 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":26}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 26, name "123", price 1500000, category_id 2}
  - TC-FR15-84 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":81}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 81, name "", price 1500000, category_id 2}
  - TC-FR15-100 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":87}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 87, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx…
  - TC-FR15-28 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":27}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 27, name "SP API28 1792497292506", price -1000, category_id 2}
  - TC-FR15-29 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":28}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 28, name "SP API29 1792497293415", price null, category_id 2}
  - TC-FR15-30 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":29}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 29, name "SP API30 1792497294325", price "abc", category_id 2}
  - TC-FR15-31 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":30}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 30, name "SP API31 1792497295222", price 100000, category_id 2}
  - TC-FR15-101 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":88}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 88, name "SP BVA 101 1792497398040", price 0, category_id 2}
  - TC-FR15-208 (Fail) — Expected: HTTP 4xx kèm trường error; CSDL không tạo sản phẩm mới. · Actual: HTTP 200 {"message":"Product created","id":112}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 112, name "SP Giá Âm Cực Đại 1792497423262", price -999999999999, category_id 2}
  - TC-FR15-214 (Fail) — Expected: HTTP 4xx kèm trường error (do JS parse `1e-324` ngầm thành `0`, vi phạm giá > 0); CSDL không đổi. · Actual: HTTP 200 {"message":"Product created","id":114}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 114, name "SP Underflow Price 1792497426240", price 0, category_id 2}
  - TC-FR15-32 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":31}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 31, name "SP API32 1792497296103", price 1500000, category_id 999}
  - TC-FR15-33 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":32}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 32, name "SP API33 1792497297046", price 1500000, category_id null}
  - TC-FR15-34 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":33}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 33, name "SP API34 1792497297969", price 1500000, category_id "abc"}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-23_req.json`, `HW02/C_FR15/evidence/TC-FR15-23_res.json`, `HW02/C_FR15/evidence/TC-FR15-23_api.png`, `HW02/C_FR15/evidence/TC-FR15-24_req.json`, `HW02/C_FR15/evidence/TC-FR15-24_res.json`, `HW02/C_FR15/evidence/TC-FR15-24_api.png`, `HW02/C_FR15/evidence/TC-FR15-24_failed.png`, `HW02/C_FR15/evidence/TC-FR15-25_req.json`, `HW02/C_FR15/evidence/TC-FR15-25_res.json`, `HW02/C_FR15/evidence/TC-FR15-25_api.png`, `HW02/C_FR15/evidence/TC-FR15-26_req.json`, `HW02/C_FR15/evidence/TC-FR15-26_res.json`, `HW02/C_FR15/evidence/TC-FR15-26_api.png`, `HW02/C_FR15/evidence/TC-FR15-27_req.json`, `HW02/C_FR15/evidence/TC-FR15-27_res.json`, `HW02/C_FR15/evidence/TC-FR15-27_api.png`, `HW02/C_FR15/evidence/TC-FR15-84_req.json`, `HW02/C_FR15/evidence/TC-FR15-84_res.json`, `HW02/C_FR15/evidence/TC-FR15-84_api.png`, `HW02/C_FR15/evidence/TC-FR15-100_req.json`, `HW02/C_FR15/evidence/TC-FR15-100_res.json`, `HW02/C_FR15/evidence/TC-FR15-100_api.png`, `HW02/C_FR15/evidence/TC-FR15-100_failed.png`, `HW02/C_FR15/evidence/TC-FR15-28_req.json`, `HW02/C_FR15/evidence/TC-FR15-28_res.json`, `HW02/C_FR15/evidence/TC-FR15-28_api.png`, `HW02/C_FR15/evidence/TC-FR15-29_req.json`, `HW02/C_FR15/evidence/TC-FR15-29_res.json`, `HW02/C_FR15/evidence/TC-FR15-29_api.png`, `HW02/C_FR15/evidence/TC-FR15-30_req.json`, `HW02/C_FR15/evidence/TC-FR15-30_res.json`, `HW02/C_FR15/evidence/TC-FR15-30_api.png`, `HW02/C_FR15/evidence/TC-FR15-31_req.json`, `HW02/C_FR15/evidence/TC-FR15-31_res.json`, `HW02/C_FR15/evidence/TC-FR15-31_api.png`, `HW02/C_FR15/evidence/TC-FR15-101_req.json`, `HW02/C_FR15/evidence/TC-FR15-101_res.json`, `HW02/C_FR15/evidence/TC-FR15-101_api.png`, `HW02/C_FR15/evidence/TC-FR15-208_req.json`, `HW02/C_FR15/evidence/TC-FR15-208_res.json`, `HW02/C_FR15/evidence/TC-FR15-208_api.png`, `HW02/C_FR15/evidence/TC-FR15-214_req.json`, `HW02/C_FR15/evidence/TC-FR15-214_res.json`, `HW02/C_FR15/evidence/TC-FR15-214_api.png`, `HW02/C_FR15/evidence/TC-FR15-32_req.json`, `HW02/C_FR15/evidence/TC-FR15-32_res.json`, `HW02/C_FR15/evidence/TC-FR15-32_api.png`, `HW02/C_FR15/evidence/TC-FR15-33_req.json`, `HW02/C_FR15/evidence/TC-FR15-33_res.json`, `HW02/C_FR15/evidence/TC-FR15-33_api.png`, `HW02/C_FR15/evidence/TC-FR15-34_req.json`, `HW02/C_FR15/evidence/TC-FR15-34_res.json`, `HW02/C_FR15/evidence/TC-FR15-34_api.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`backend/server.js` dòng 167–177:

```js
 167  app.post("/api/products", (req, res) => {
 168    const { name, price, description, imageUrl, category_id } = req.body;
 169    db.run(
 170      "INSERT INTO products (name, price, description, imageUrl, category_id) VALUES (?, ?, ?, ?, ?)",
 171      [name, price, description, imageUrl, category_id],
 172      function (err) {
 173        if (err) return res.status(500).json({ error: err.message });
 174        res.json({ message: "Product created", id: this.lastID });
 175      },
 176    );
 177  });
```

**Bước tái hiện (nháp) + output đã chạy:**

Lệnh (`HW02/bugs/_repro_C_FR15/G8.ps1`, chạy: `powershell -ExecutionPolicy Bypass -File HW02/bugs/_repro_C_FR15/G8.ps1`):

```powershell
. "$PSScriptRoot\prelude.ps1"
# POST /api/products với dữ liệu vi phạm FR-15.2 / FR-15.3 / FR-15.4 (token admin)
$r1 = Send 'POST' "$base/api/products" '{"name": "", "price": 1500000, "category_id": 2, "description": "repro G8", "imageUrl": "https://placehold.co/300"}' $headers; "1) name rỗng      -> $r1"
$r2 = Send 'POST' "$base/api/products" '{"name": "repro G8 gia am", "price": -1000, "category_id": 2, "description": "repro G8", "imageUrl": "https://placehold.co/300"}' $headers; "2) price -1000    -> $r2"
$r3 = Send 'POST' "$base/api/products" '{"name": "repro G8 dm 999", "price": 1500000, "category_id": 999, "description": "repro G8", "imageUrl": "https://placehold.co/300"}' $headers; "3) category 999   -> $r3"
foreach ($r in @($r1, $r2, $r3)) { $id = ([regex]'"id":(\d+)').Match($r).Groups[1].Value; if ($id) { "   GET /api/products/$id -> $(Send 'GET' "$base/api/products/$id" $null @{})"; $null = Send 'DELETE' "$base/api/products/$id" $null $headers } }
```

Output:

```text
1) name rỗng      -> HTTP 200 {"message":"Product created","id":122}
2) price -1000    -> HTTP 200 {"message":"Product created","id":123}
3) category 999   -> HTTP 200 {"message":"Product created","id":124}
   GET /api/products/122 -> HTTP 200 {"id":122,"name":"","price":"1500000","description":"repro G8","imageUrl":"https://placehold.co/300","category_id":2}
   GET /api/products/123 -> HTTP 200 {"id":123,"name":"repro G8 gia am","price":-1000,"description":"repro G8","imageUrl":"https://placehold.co/300","category_id":2}
   GET /api/products/124 -> HTTP 200 {"id":124,"name":"repro G8 dm 999","price":"1500000","description":"repro G8","imageUrl":"https://placehold.co/300","category_id":999}
```


## G9 — API · PUT /api/products/:id với dữ liệu vi phạm → HTTP 200 'Product updated', sản phẩm M bị ghi đè

- **TC Fail (15):** 35, 36, 37, 38, 39, 106, 112, 40, 41, 42, 43, 113, 44, 45, 46
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-15.2 (35–39, 106, 112), FR-15.3 (40–43, 113), FR-15.4 (44–46), C6, C9 (38, 39, 41, 42, 43, 45, 46), C3 (37), C11 (44)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-35 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 39, name "Muc tieu 35 1792497302093", price 1000000, category_id 1} → M_SAU {id 39, name "", price 2500000, category_id 3}
  - TC-FR15-36 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 40, name "Muc tieu 36 1792497303069", price "1000000", category_id 1} → M_SAU {id 40, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx…
  - TC-FR15-37 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 41, name "Muc tieu 37 1792497304008", price 1000000, category_id 1} → M_SAU {id 41, name "   ", price 2500000, category_id 3}
  - TC-FR15-38 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 42, name "Muc tieu 38 1792497304945", price "1000000", category_id 1} → M_SAU {id 42, name null, price "2500000", category_id 3}
  - TC-FR15-39 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 43, name "Muc tieu 39 1792497305863", price 1000000, category_id 1} → M_SAU {id 43, name "123", price 2500000, category_id 3}
  - TC-FR15-106 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 93, name "Muc tieu 106 1792497399830", price 1000000, category_id 1} → M_SAU {id 93, name "", price 2500000, category_id 3}
  - TC-FR15-112 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 99, name "Muc tieu 112 1792497402085", price 1000000, category_id 1} → M_SAU {id 99, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx…
  - TC-FR15-40 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 44, name "Muc tieu 40 1792497306783", price "1000000", category_id 1} → M_SAU {id 44, name "Sua API40 1792497306783", price "-1000", category_id 3}
  - TC-FR15-41 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 45, name "Muc tieu 41 1792497307693", price 1000000, category_id 1} → M_SAU {id 45, name "Sua API41 1792497307693", price null, category_id 3}
  - TC-FR15-42 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 46, name "Muc tieu 42 1792497308626", price "1000000", category_id 1} → M_SAU {id 46, name "Sua API42 1792497308626", price "abc", category_id 3}
  - TC-FR15-43 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 47, name "Muc tieu 43 1792497309603", price 1000000, category_id 1} → M_SAU {id 47, name "Sua API43 1792497309603", price 100000, category_id 3}
  - TC-FR15-113 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 100, name "Muc tieu 113 1792497402983", price "1000000", category_id 1} → M_SAU {id 100, name "Sua BVA 113 1792497402983", price "0", category_id 3}
  - TC-FR15-44 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 48, name "Muc tieu 44 1792497310540", price "1000000", category_id 1} → M_SAU {id 48, name "Sua API44 1792497310540", price "2500000", category_id 999}
  - TC-FR15-45 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 49, name "Muc tieu 45 1792497311464", price 1000000, category_id 1} → M_SAU {id 49, name "Sua API45 1792497311464", price 2500000, category_id null}
  - TC-FR15-46 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 50, name "Muc tieu 46 1792497312379", price "1000000", category_id 1} → M_SAU {id 50, name "Sua API46 1792497312379", price "2500000", category_id "abc"}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-35_req.json`, `HW02/C_FR15/evidence/TC-FR15-35_res.json`, `HW02/C_FR15/evidence/TC-FR15-35_api.png`, `HW02/C_FR15/evidence/TC-FR15-36_req.json`, `HW02/C_FR15/evidence/TC-FR15-36_res.json`, `HW02/C_FR15/evidence/TC-FR15-36_api.png`, `HW02/C_FR15/evidence/TC-FR15-36_failed.png`, `HW02/C_FR15/evidence/TC-FR15-37_req.json`, `HW02/C_FR15/evidence/TC-FR15-37_res.json`, `HW02/C_FR15/evidence/TC-FR15-37_api.png`, `HW02/C_FR15/evidence/TC-FR15-38_req.json`, `HW02/C_FR15/evidence/TC-FR15-38_res.json`, `HW02/C_FR15/evidence/TC-FR15-38_api.png`, `HW02/C_FR15/evidence/TC-FR15-39_req.json`, `HW02/C_FR15/evidence/TC-FR15-39_res.json`, `HW02/C_FR15/evidence/TC-FR15-39_api.png`, `HW02/C_FR15/evidence/TC-FR15-106_req.json`, `HW02/C_FR15/evidence/TC-FR15-106_res.json`, `HW02/C_FR15/evidence/TC-FR15-106_api.png`, `HW02/C_FR15/evidence/TC-FR15-112_req.json`, `HW02/C_FR15/evidence/TC-FR15-112_res.json`, `HW02/C_FR15/evidence/TC-FR15-112_api.png`, `HW02/C_FR15/evidence/TC-FR15-112_failed.png`, `HW02/C_FR15/evidence/TC-FR15-40_req.json`, `HW02/C_FR15/evidence/TC-FR15-40_res.json`, `HW02/C_FR15/evidence/TC-FR15-40_api.png`, `HW02/C_FR15/evidence/TC-FR15-41_req.json`, `HW02/C_FR15/evidence/TC-FR15-41_res.json`, `HW02/C_FR15/evidence/TC-FR15-41_api.png`, `HW02/C_FR15/evidence/TC-FR15-42_req.json`, `HW02/C_FR15/evidence/TC-FR15-42_res.json`, `HW02/C_FR15/evidence/TC-FR15-42_api.png`, `HW02/C_FR15/evidence/TC-FR15-43_req.json`, `HW02/C_FR15/evidence/TC-FR15-43_res.json`, `HW02/C_FR15/evidence/TC-FR15-43_api.png`, `HW02/C_FR15/evidence/TC-FR15-113_req.json`, `HW02/C_FR15/evidence/TC-FR15-113_res.json`, `HW02/C_FR15/evidence/TC-FR15-113_api.png`, `HW02/C_FR15/evidence/TC-FR15-44_req.json`, `HW02/C_FR15/evidence/TC-FR15-44_res.json`, `HW02/C_FR15/evidence/TC-FR15-44_api.png`, `HW02/C_FR15/evidence/TC-FR15-45_req.json`, `HW02/C_FR15/evidence/TC-FR15-45_res.json`, `HW02/C_FR15/evidence/TC-FR15-45_api.png`, `HW02/C_FR15/evidence/TC-FR15-46_req.json`, `HW02/C_FR15/evidence/TC-FR15-46_res.json`, `HW02/C_FR15/evidence/TC-FR15-46_api.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`backend/server.js` dòng 179–189:

```js
 179  app.put("/api/products/:id", (req, res) => {
 180    const { name, price, description, imageUrl, category_id } = req.body;
 181    db.run(
 182      "UPDATE products SET name = ?, price = ?, description = ?, imageUrl = ?, category_id = ? WHERE id = ?",
 183      [name, price, description, imageUrl, category_id, req.params.id],
 184      function (err) {
 185        if (err) return res.status(500).json({ error: err.message });
 186        res.json({ message: "Product updated" });
 187      },
 188    );
 189  });
```

**Bước tái hiện (nháp) + output đã chạy:**

Lệnh (`HW02/bugs/_repro_C_FR15/G9.ps1`, chạy: `powershell -ExecutionPolicy Bypass -File HW02/bugs/_repro_C_FR15/G9.ps1`):

```powershell
. "$PSScriptRoot\prelude.ps1"
# Dựng M
$m = Send 'POST' "$base/api/products" '{"name": "repro G9 M", "price": 1000000, "category_id": 1, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers
$M = ([regex]'"id":(\d+)').Match($m).Groups[1].Value
"Dựng M -> $m"
"M TRƯỚC -> $(Send 'GET' "$base/api/products/$M" $null @{})"
$r = Send 'PUT' "$base/api/products/$M" '{"name": "", "price": 2500000, "category_id": 3, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers
"PUT name rỗng -> $r"
"M SAU -> $(Send 'GET' "$base/api/products/$M" $null @{})"
$null = Send 'DELETE' "$base/api/products/$M" $null $headers
```

Output:

```text
Dựng M -> 125
M TRƯỚC -> HTTP 200 {"id":125,"name":"repro G9 M","price":1000000,"description":"repro","imageUrl":"https://placehold.co/300","category_id":1}
PUT name rỗng -> HTTP 200 {"message":"Product updated"}
M SAU -> HTTP 200 {"id":125,"name":"","price":2500000,"description":"repro","imageUrl":"https://placehold.co/300","category_id":3}
```


## G10 — API · id không tồn tại → HTTP 200 (GET trả {}, PUT 'Product updated', DELETE 'Product deleted')

- **TC Fail (3):** 47, 48, 49
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** C10
- **Đạt trong cùng case:** Dữ liệu không đổi (SAU = TRƯỚC) ở cả 3 case
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-47 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (C10). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {}; bản ghi TRƯỚC → SAU: 5 → 5
  - TC-FR15-48 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (C10). Dữ liệu: GET /api/products SAU = TRƯỚC (không có bản ghi mới, không bản ghi nào đổi). · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 5 → 5
  - TC-FR15-49 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (C10). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-47_req.json`, `HW02/C_FR15/evidence/TC-FR15-47_res.json`, `HW02/C_FR15/evidence/TC-FR15-47_api.png`, `HW02/C_FR15/evidence/TC-FR15-48_req.json`, `HW02/C_FR15/evidence/TC-FR15-48_res.json`, `HW02/C_FR15/evidence/TC-FR15-48_api.png`, `HW02/C_FR15/evidence/TC-FR15-49_req.json`, `HW02/C_FR15/evidence/TC-FR15-49_res.json`, `HW02/C_FR15/evidence/TC-FR15-49_api.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`backend/server.js` dòng 159–165:

```js
 159  app.get("/api/products/:id", (req, res) => {
 160    db.get("SELECT * FROM products WHERE id = ?", [req.params.id], (err, row) => {
 161      if (!row) return res.status(200).json({});
 162      if (row.id % 2 === 0) row.price = row.price.toString();
 163      res.json(row);
 164    });
 165  });
```

`backend/server.js` dòng 179–196:

```js
 179  app.put("/api/products/:id", (req, res) => {
 180    const { name, price, description, imageUrl, category_id } = req.body;
 181    db.run(
 182      "UPDATE products SET name = ?, price = ?, description = ?, imageUrl = ?, category_id = ? WHERE id = ?",
 183      [name, price, description, imageUrl, category_id, req.params.id],
 184      function (err) {
 185        if (err) return res.status(500).json({ error: err.message });
 186        res.json({ message: "Product updated" });
 187      },
 188    );
 189  });
 190  
 191  app.delete("/api/products/:id", (req, res) => {
 192    db.run("DELETE FROM products WHERE id = ?", [req.params.id], function (err) {
 193      if (err) return res.status(500).json({ error: err.message });
 194      res.json({ message: "Product deleted" });
 195    });
 196  });
```

**Bước tái hiện (nháp) + output đã chạy:**

Lệnh (`HW02/bugs/_repro_C_FR15/G10.ps1`, chạy: `powershell -ExecutionPolicy Bypass -File HW02/bugs/_repro_C_FR15/G10.ps1`):

```powershell
. "$PSScriptRoot\prelude.ps1"
"Số bản ghi TRƯỚC: $(((Invoke-WebRequest -UseBasicParsing "$base/api/products").Content | ConvertFrom-Json).Count)"
"GET    /api/products/999999 -> $(Send 'GET' "$base/api/products/999999" $null @{})"
"PUT    /api/products/999999 -> $(Send 'PUT' "$base/api/products/999999" '{"name": "repro G10", "price": 2500000, "category_id": 3, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers)"
"DELETE /api/products/999999 -> $(Send 'DELETE' "$base/api/products/999999" $null $headers)"
"Số bản ghi SAU: $(((Invoke-WebRequest -UseBasicParsing "$base/api/products").Content | ConvertFrom-Json).Count)"
```

Output:

```text
Số bản ghi TRƯỚC: 6
GET    /api/products/999999 -> HTTP 200 {}
PUT    /api/products/999999 -> HTTP 200 {"message":"Product updated"}
DELETE /api/products/999999 -> HTTP 200 {"message":"Product deleted"}
Số bản ghi SAU: 6
```


## G11 — API · POST/PUT/DELETE /api/products không có token, token không hợp lệ hoặc token role user → HTTP 200, thao tác được thực hiện

- **TC Fail (9):** 50, 51, 52, 53, 54, 55, 56, 57, 58
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-12.2, SEC-02 (thiếu/sai token: 50, 51, 53, 54, 56, 57), SEC-03 (role user: 52, 55, 58)
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-50 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":34}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 34, name "SP API50 1792497298877", price 1500000, category_id 2}
  - TC-FR15-51 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":35}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 35, name "SP API51 1792497299774", price 1500000, category_id 2}
  - TC-FR15-52 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product created","id":36}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 36, name "SP API52 1792497300678", price 1500000, category_id 2}
  - TC-FR15-53 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 51, name "Muc tieu 53 1792497314256", price 1000000, category_id 1} → M_SAU {id 51, name "Sua API53 1792497314256", price 2500000, category_id 3}
  - TC-FR15-54 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 52, name "Muc tieu 54 1792497315170", price "1000000", category_id 1} → M_SAU {id 52, name "Sua API54 1792497315170", price "2500000", category_id 3}
  - TC-FR15-55 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 53, name "Muc tieu 55 1792497316069", price 1000000, category_id 1} → M_SAU {id 53, name "Sua API55 1792497316069", price 2500000, category_id 3}
  - TC-FR15-56 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU vẫn có id M; SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 55, name "Muc tieu 56 1792497320087", price 1000000, category_id 1} → M_SAU HTTP 200 {}
  - TC-FR15-57 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU vẫn có id M; SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 56, name "Muc tieu 57 1792497320980", price "1000000", category_id 1} → M_SAU HTTP 200 {}
  - TC-FR15-58 (Fail) — Expected: HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU vẫn có id M; SAU = TRƯỚC. · Actual: HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 57, name "Muc tieu 58 1792497321894", price 1000000, category_id 1} → M_SAU HTTP 200 {}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-50_req.json`, `HW02/C_FR15/evidence/TC-FR15-50_res.json`, `HW02/C_FR15/evidence/TC-FR15-50_api.png`, `HW02/C_FR15/evidence/TC-FR15-51_req.json`, `HW02/C_FR15/evidence/TC-FR15-51_res.json`, `HW02/C_FR15/evidence/TC-FR15-51_api.png`, `HW02/C_FR15/evidence/TC-FR15-52_req.json`, `HW02/C_FR15/evidence/TC-FR15-52_res.json`, `HW02/C_FR15/evidence/TC-FR15-52_api.png`, `HW02/C_FR15/evidence/TC-FR15-53_req.json`, `HW02/C_FR15/evidence/TC-FR15-53_res.json`, `HW02/C_FR15/evidence/TC-FR15-53_api.png`, `HW02/C_FR15/evidence/TC-FR15-54_req.json`, `HW02/C_FR15/evidence/TC-FR15-54_res.json`, `HW02/C_FR15/evidence/TC-FR15-54_api.png`, `HW02/C_FR15/evidence/TC-FR15-55_req.json`, `HW02/C_FR15/evidence/TC-FR15-55_res.json`, `HW02/C_FR15/evidence/TC-FR15-55_api.png`, `HW02/C_FR15/evidence/TC-FR15-56_req.json`, `HW02/C_FR15/evidence/TC-FR15-56_res.json`, `HW02/C_FR15/evidence/TC-FR15-56_api.png`, `HW02/C_FR15/evidence/TC-FR15-57_req.json`, `HW02/C_FR15/evidence/TC-FR15-57_res.json`, `HW02/C_FR15/evidence/TC-FR15-57_api.png`, `HW02/C_FR15/evidence/TC-FR15-58_req.json`, `HW02/C_FR15/evidence/TC-FR15-58_res.json`, `HW02/C_FR15/evidence/TC-FR15-58_api.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`backend/server.js` dòng 100–110:

```js
 100  const authenticateToken = (req, res, next) => {
 101    const authHeader = req.headers["authorization"];
 102    const token = authHeader && authHeader.split(" ")[1];
 103    if (token == null) return res.status(401).json({ error: "Unauthorized" });
 104  
 105    jwt.verify(token, SECRET_KEY, (err, user) => {
 106      if (err) return res.status(403).json({ error: "Forbidden" });
 107      req.user = user;
 108      next();
 109    });
 110  };
```

`backend/server.js` dòng 167–167:

```js
 167  app.post("/api/products", (req, res) => {
```

`backend/server.js` dòng 179–179:

```js
 179  app.put("/api/products/:id", (req, res) => {
```

`backend/server.js` dòng 191–191:

```js
 191  app.delete("/api/products/:id", (req, res) => {
```

**Bước tái hiện (nháp) + output đã chạy:**

Lệnh (`HW02/bugs/_repro_C_FR15/G11.ps1`, chạy: `powershell -ExecutionPolicy Bypass -File HW02/bugs/_repro_C_FR15/G11.ps1`):

```powershell
. "$PSScriptRoot\prelude.ps1"
$lu = Invoke-WebRequest -UseBasicParsing -Method Post -Uri "$base/api/login" -ContentType 'application/json' -Body ([Text.Encoding]::UTF8.GetBytes('{"email":"test@eshop.com","password":"Test1234!"}'))
$TU = ($lu.Content | ConvertFrom-Json).token
# 1) POST không có header Authorization
$p = Send 'POST' "$base/api/products" '{"name": "repro G11 no token", "price": 1500000, "category_id": 2, "description": "repro", "imageUrl": "https://placehold.co/300"}' @{}
"1) POST không token -> $p"
$P = ([regex]'"id":(\d+)').Match($p).Groups[1].Value
# Dựng M bằng token admin
$m = Send 'POST' "$base/api/products" '{"name": "repro G11 M", "price": 1000000, "category_id": 1, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers
$M = ([regex]'"id":(\d+)').Match($m).Groups[1].Value
# 2) PUT với token không hợp lệ
"2) PUT token sai -> $(Send 'PUT' "$base/api/products/$M" '{"name": "repro G11 sua bang token sai", "price": 2500000, "category_id": 3, "description": "repro", "imageUrl": "https://placehold.co/300"}' @{ Authorization = 'Bearer abc.def.ghi' })"
"   M SAU -> $(Send 'GET' "$base/api/products/$M" $null @{})"
# 3) DELETE với token role user (test@eshop.com)
"3) DELETE token user -> $(Send 'DELETE' "$base/api/products/$M" $null @{ Authorization = "Bearer $TU" })"
"   M SAU -> $(Send 'GET' "$base/api/products/$M" $null @{})"
if ($P) { $null = Send 'DELETE' "$base/api/products/$P" $null $headers }
```

Output:

```text
1) POST không token -> HTTP 200 {"message":"Product created","id":126}
2) PUT token sai -> HTTP 200 {"message":"Product updated"}
   M SAU -> HTTP 200 {"id":127,"name":"repro G11 sua bang token sai","price":2500000,"description":"repro","imageUrl":"https://placehold.co/300","category_id":3}
3) DELETE token user -> HTTP 200 {"message":"Product deleted"}
   M SAU -> HTTP 200 {}
```


## G12 — API · GET /api/products/:id với id chẵn → price là chuỗi JSON ("28000000")

- **TC Fail (1):** 22
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** C15; phần sập backend (7c, ngoài TC — AI đề xuất ở 7e, chờ SV duyệt): ổn định tiến trình backend (ngầm định — SRS không có điều khoản; lỗi một request không được dừng tiến trình). Chưa đánh giá được: FR-06 (web `ProductDetail.jsx` dòng 16, mobile `App.js` dòng 120 gọi endpoint này; chưa kiểm qua UI)
- **Đạt trong cùng case:** name, category_id đúng giá trị seed
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-22 (Fail) — Expected: HTTP 2xx; body là bản ghi id 2 với name = 'Samsung Galaxy S24 Ultra', category_id = 1 và price = 28000000 là số JSON (không phải chuỗi) (C15). Nơi duy nhất khẳn… · Actual: HTTP 200 {"id":2,"name":"Samsung Galaxy S24 Ultra","price":"28000000","description":"Màn hình hiển thị xuất sắc, camera siêu zoom","imageUrl":"https://placehold.co/300x300/png?text=Samsung+S24","category_id":1; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-22_req.json`, `HW02/C_FR15/evidence/TC-FR15-22_res.json`, `HW02/C_FR15/evidence/TC-FR15-22_api.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`backend/server.js` dòng 159–165:

```js
 159  app.get("/api/products/:id", (req, res) => {
 160    db.get("SELECT * FROM products WHERE id = ?", [req.params.id], (err, row) => {
 161      if (!row) return res.status(200).json({});
 162      if (row.id % 2 === 0) row.price = row.price.toString();
 163      res.json(row);
 164    });
 165  });
```

**Bước tái hiện (nháp) + output đã chạy:**

Lệnh (`HW02/bugs/_repro_C_FR15/G12.ps1`, chạy: `powershell -ExecutionPolicy Bypass -File HW02/bugs/_repro_C_FR15/G12.ps1`):

```powershell
. "$PSScriptRoot\prelude.ps1"
"GET /api/products/2 -> $(Send 'GET' "$base/api/products/2" $null @{})"
"GET /api/products/1 -> $(Send 'GET' "$base/api/products/1" $null @{})"
```

Output:

```text
GET /api/products/2 -> HTTP 200 {"id":2,"name":"Samsung Galaxy S24 Ultra","price":"28000000","description":"Màn hình hiển thị xuất sắc, camera siêu zoom","imageUrl":"https://placehold.co/300x300/png?text=Samsung+S24","category_id":1}
GET /api/products/1 -> HTTP 200 {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"description":"Điện thoại cao cấp của Apple","imageUrl":"https://placehold.co/300x300/png?text=iPhone+15","category_id":1}
```


## G13 — API · POST /api/products body không phải JSON hợp lệ (price: Infinity) → HTTP 400, body là trang HTML

- **TC Fail (1):** 209
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** C20
- **Đạt trong cùng case:** Dữ liệu không đổi
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-209 (Fail) — Expected: HTTP 4xx kèm trường error (không trả về HTML 500 lộ stack trace); CSDL không đổi. · Actual: HTTP 400 <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot; &quot;price&quot;: Infinity, &quot;... is n; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-209_req.json`, `HW02/C_FR15/evidence/TC-FR15-209_res.json`, `HW02/C_FR15/evidence/TC-FR15-209_api.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`backend/server.js` dòng 11–12:

```js
  11  app.use(cors());
  12  app.use(bodyParser.json());
```

**Bước tái hiện (nháp) + output đã chạy:**

Lệnh (`HW02/bugs/_repro_C_FR15/G13.ps1`, chạy: `powershell -ExecutionPolicy Bypass -File HW02/bugs/_repro_C_FR15/G13.ps1`):

```powershell
. "$PSScriptRoot\prelude.ps1"
"POST price Infinity -> $(Send 'POST' "$base/api/products" '{"name": "repro G13", "price": Infinity, "category_id": 2, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers)"
```

Output:

```text
POST price Infinity -> HTTP 400 <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot; &quot;price&quot;: Infinity, &quot;... is not valid JSON<br> … (stack trace, rút gọn)
```


## G14 — API · POST /api/products với Content-Type: text/plain → HTTP 500, body là trang HTML

- **TC Fail (1):** 211
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** C6 (không 5xx; SV ghi căn cứ C6, C9)
- **Đạt trong cùng case:** Không tạo sản phẩm
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-211 (Fail) — Expected: HTTP 4xx (400 hoặc 415); CSDL không tạo sản phẩm. · Actual: HTTP 500 <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-211_req.json`, `HW02/C_FR15/evidence/TC-FR15-211_res.json`, `HW02/C_FR15/evidence/TC-FR15-211_api.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`backend/server.js` dòng 11–12:

```js
  11  app.use(cors());
  12  app.use(bodyParser.json());
```

`backend/server.js` dòng 167–168:

```js
 167  app.post("/api/products", (req, res) => {
 168    const { name, price, description, imageUrl, category_id } = req.body;
```

**Bước tái hiện (nháp) + output đã chạy:**

Lệnh (`HW02/bugs/_repro_C_FR15/G14.ps1`, chạy: `powershell -ExecutionPolicy Bypass -File HW02/bugs/_repro_C_FR15/G14.ps1`):

```powershell
. "$PSScriptRoot\prelude.ps1"
"POST text/plain -> $(Send 'POST' "$base/api/products" '{"name": "repro G14", "price": 1500000, "category_id": 2, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers 'text/plain')"
```

Output:

```text
POST text/plain -> HTTP 500 <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<br> &nbsp; &nbsp;at D:\HK7\…\backend\server.js:168:11<br> … (stack trace, rút gọn)
```


## G15 — GUI · form 'Thêm sản phẩm mới' không có nhãn, không có ký hiệu '*' cho Tên, Giá, Danh mục

- **TC Fail (1):** 90
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-22.1
- **Đạt trong cùng case:** —
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-90 (Fail) — Expected: 3 nhãn Tên sản phẩm, Giá, Danh mục đều có ký hiệu '*' (FR-22.1). · Actual: Manual – 20/10/2026 18:33. Form 'Thêm sản phẩm mới' chỉ có placeholder 'Tên sản phẩm', 'Giá tiền', 'URL Ảnh', 'Mô tả' và ô chọn danh mục; không có nhãn, không có ký hiệu '*'.
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-90_manual.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 490–507:

```js
 490                <div className="grid grid-cols-2 gap-4">
 491                  <input
 492                    placeholder="Tên sản phẩm"
 493                    className="border p-2 rounded"
 494                    value={productForm.name}
 495                    onChange={(e) =>
 496                      setProductForm({ ...productForm, name: e.target.value })
 497                    }
 498                    required
 499                  />
 500                  <input
 501                    placeholder="Giá tiền"
 502                    type="number"
 503                    className="border p-2 rounded"
 504                    value={productForm.price}
 505                    onChange={(e) =>
 506                      setProductForm({ ...productForm, price: e.target.value })
 507                    }
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Đăng nhập admin, mục 'Sản phẩm'.
2. Quan sát form 'Thêm sản phẩm mới': tìm nhãn và ký hiệu '*' của Tên, Giá, Danh mục.

Output (`ui_repro.js`):

```text
G15: số <label> trong form=0; có '*' trong form=false; placeholder=["Tên sản phẩm","Giá tiền","URL Ảnh","Mô tả"]
```


## G16 — GUI · cột 'Giá' của bảng sản phẩm không có ký tự phân cách hàng nghìn ('30000000 ₫')

- **TC Fail (1):** 92
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định bị vi phạm:** FR-21.3
- **Đạt trong cùng case:** Có ký hiệu ₫
- **Chưa đánh giá được trong cùng case:** —
- **Actual (lượt 6 / manual, rút gọn 260 ký tự):**
  - TC-FR15-92 (Fail) — Expected: Ô 'Giá' hiển thị ký hiệu '₫' và phân cách hàng nghìn '.' hoặc ',' (vd 30.000.000 ₫ hoặc 30,000,000 ₫) (FR-21.3, C17). Nơi duy nhất kiểm định dạng tiền. · Actual: Manual – 20/10/2026 18:36. Ô 'Giá' dòng 'iPhone 15 Pro Max' hiển thị '30000000 ₫' — có ₫, không có ký tự phân cách hàng nghìn.
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-92_manual.png`

**Đoạn code liên quan (gray-box, trích nguyên văn):**

`frontend-admin/src/App.jsx` dòng 590–590:

```js
 590                      <td className="p-3">{p.price} ₫</td>
```

**Bước tái hiện (nháp) + output đã chạy:**

1. Đăng nhập admin, mục 'Sản phẩm'.
2. Đọc ô 'Giá' của dòng 'iPhone 15 Pro Max' (locale trình duyệt en-US).

Output (`ui_repro.js`):

```text
G16: ô Giá dòng 'iPhone 15 Pro Max' = "30000000 ₫"
```




## Kiểm 7c — chạy thật bước tái hiện SV viết (20/10/2026, sau commit 7/7b `b06a775`)

Script: `HW02/bugs/_repro_C_FR15/7c/` — `restart_backend.ps1` (dừng `node server.js`, khởi động lại, chờ đủ 5 sản phẩm seed), `api_7c.ps1` (Windows PowerShell 5.1), `ui_7c.js` (Playwright 1.48.2, Chromium). Lệnh tái hiện do AI soạn để kiểm khả năng tái hiện; không dùng làm bước tái hiện trong BUG.

- Restart backend: API — trước mỗi BUG và sau BUG cuối; UI — trước mỗi thao tác (A/B/C…) và sau thao tác cuối.
- API: payload theo bước SV; trường SV không ghi lấy giá trị hợp lệ như TC (`price` 1500000/2500000, `category_id` 2/3, `description`, `imageUrl`). SV không ghi token ở BUG-41…44, 46, 48 → không gửi `Authorization`. BUG-42 dùng sản phẩm seed id 1. BUG-47 chạy cả "token hết hạn" (SV ghi trong bước; không có TC) bằng JWT ký với `SECRET_KEY` ở `backend/server.js` dòng 9, `exp` = 1 giờ trước.
- UI: SV không ghi bước đăng nhập; script đăng nhập `admin@eshop.com` / `Admin123!` rồi đi theo bước SV. "Sản phẩm bất kỳ" ở BUG-37/38 = dòng "iPhone 15 Pro Max" (id 1). Danh mục "bất kỳ" = Laptop.

```powershell
powershell -ExecutionPolicy Bypass -File HW02\bugs\_repro_C_FR15\7c\api_7c.ps1
$env:NODE_PATH = (Resolve-Path 'HW02\tests\node_modules').Path; node HW02\bugs\_repro_C_FR15\7c\ui_7c.js
```

### Kết quả

| BUG | Tái hiện theo bước SV? | Ghi chú |
|---|---|---|
| BUG-35 | Có (thêm bước đăng nhập) | A/B/C: không thông báo, 5 → 6 |
| BUG-36 | Có (thêm bước đăng nhập) | -1000 / 0 / rỗng: không thông báo, 5 → 6; TC-205 thực tế dán chữ số full-width (ô thành rỗng), không phải "để trống" |
| BUG-37 | Có (thêm bước đăng nhập) | nút ở chế độ sửa chỉ có "Lưu sản phẩm"; không có nút "Cập nhật sản phẩm" |
| BUG-38 | Có (thêm bước đăng nhập) | như BUG-37 |
| BUG-39 | Có (thêm bước đăng nhập) | không có hộp thoại "1" |
| BUG-40 | Có (thêm bước đăng nhập) | price lưu 100000 |
| BUG-41 | Có | 16/16 payload → HTTP 200 "Product created" |
| BUG-42 | Có | 14/14 payload → HTTP 200 "Product updated" |
| BUG-43 | Có | HTTP 400, `Content-Type: text/html` |
| BUG-44 | Có | không `-ContentType` và `text/plain` đều HTTP 500, body HTML |
| BUG-45 | Không theo đúng ví dụ (id 8 không có sau seed); có với sản phẩm seed | tên mới đè mọi dòng; ô 'Giá' dòng M giữ giá cũ |
| BUG-46 | Có | GET `{}`, PUT/DELETE 200 |
| BUG-47 | Có | 4 kiểu danh tính × POST/PUT/DELETE → HTTP 200, dữ liệu đổi |
| BUG-48 | Có | price kiểu String |
| BUG-49 | Có (thêm bước đăng nhập) | 0 `<label>`, không có '*' |
| BUG-50 | Có (thêm bước đăng nhập) | "30000000 ₫" |

Bất thường mới (ngoài bước SV, phát sinh khi AI gọi thêm `GET /api/products/:id` ở lần chạy đầu): `POST` với `price: null` tạo bản ghi id chẵn, sau đó `GET /api/products/<id chẵn>` làm tiến trình `node server.js` dừng (`row.price.toString()` trên `null` — `backend/server.js` dòng 162). Chạy lại riêng: POST → `{"message":"Product created","id":6}`; GET /api/products/6 → "An error occurred while sending the request."; GET /api/products → "No connection could be made because the target machine actively refused it. (localhost:3000)"; tiến trình server.js còn chạy: False. Chưa có TC/bug — SV quyết. Script đã đổi sang đọc bản ghi qua `GET /api/products` (đúng bước SV) và chạy lại; output dưới đây là lần chạy lại.

Output `api_7c.ps1` (chuỗi "x" lặp rút gọn thành 20 ký tự + "…"):

```text
===== BUG-41 (POST /api/products, các payload vi phạm; không gửi token)
   [backend restart xong: 5 sản phẩm]
name ""          (TC-23/84) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":6}; bản ghi 5 → 6; bản ghi id 6 trong GET /api/products: {"id":6,"name":"","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
name 256×x       (TC-100) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":7}; bản ghi 6 → 7; bản ghi id 7 trong GET /api/products: {"id":7,"name":"xxxxxxxxxxxxxxxxxxxx…","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
name 300×x       (TC-24) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":8}; bản ghi 7 → 8; bản ghi id 8 trong GET /api/products: {"id":8,"name":"xxxxxxxxxxxxxxxxxxxx…","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
name "   "       (TC-25) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":9}; bản ghi 8 → 9; bản ghi id 9 trong GET /api/products: {"id":9,"name":"   ","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
name null        (TC-26) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":10}; bản ghi 9 → 10; bản ghi id 10 trong GET /api/products: {"id":10,"name":null,"price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
name 123         (TC-27) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":11}; bản ghi 10 → 11; bản ghi id 11 trong GET /api/products: {"id":11,"name":"123","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
price -1000      (TC-28) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":12}; bản ghi 11 → 12; bản ghi id 12 trong GET /api/products: {"id":12,"name":"SP 7c 28","price":-1000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
price -999999999999 (TC-208) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":13}; bản ghi 12 → 13; bản ghi id 13 trong GET /api/products: {"id":13,"name":"SP 7c 208","price":-999999999999,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
price 0          (TC-101) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":14}; bản ghi 13 → 14; bản ghi id 14 trong GET /api/products: {"id":14,"name":"SP 7c 101","price":0,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
price 1e-324     (TC-214) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":15}; bản ghi 14 → 15; bản ghi id 15 trong GET /api/products: {"id":15,"name":"SP 7c 214","price":0,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
price null       (TC-29) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":16}; bản ghi 15 → 16; bản ghi id 16 trong GET /api/products: {"id":16,"name":"SP 7c 29","price":null,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
price "abc"      (TC-30) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":17}; bản ghi 16 → 17; bản ghi id 17 trong GET /api/products: {"id":17,"name":"SP 7c 30","price":"abc","description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
price "100000"   (TC-31) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":18}; bản ghi 17 → 18; bản ghi id 18 trong GET /api/products: {"id":18,"name":"SP 7c 31","price":100000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
category 999     (TC-32) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":19}; bản ghi 18 → 19; bản ghi id 19 trong GET /api/products: {"id":19,"name":"SP 7c 32","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":999}
category null    (TC-33) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":20}; bản ghi 19 → 20; bản ghi id 20 trong GET /api/products: {"id":20,"name":"SP 7c 33","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":null}
category "abc"   (TC-34) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":21}; bản ghi 20 → 21; bản ghi id 21 trong GET /api/products: {"id":21,"name":"SP 7c 34","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":"abc"}
===== BUG-42 (PUT /api/products/1 — sản phẩm seed đang tồn tại; không gửi token)
   [backend restart xong: 5 sản phẩm]
name ""          (TC-35/106) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"description":"Điện thoại cao cấp của Apple","imageUrl":"https://placehold.co/300x300/png?text=iPhone+15","category_id":1}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
name 256×x       (TC-112) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"xxxxxxxxxxxxxxxxxxxx…","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
name 300×x       (TC-36) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"xxxxxxxxxxxxxxxxxxxx…","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"xxxxxxxxxxxxxxxxxxxx…","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
name "   "       (TC-37) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"xxxxxxxxxxxxxxxxxxxx…","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"   ","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
name null        (TC-38) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"   ","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":null,"price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
name 123         (TC-39) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":null,"price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"123","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
price -1000      (TC-40) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"123","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 40","price":-1000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
price 0          (TC-113) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 40","price":-1000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 113","price":0,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
price null       (TC-41) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 113","price":0,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 41","price":null,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
price "abc"      (TC-42) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 41","price":null,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 42","price":"abc","description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
price "100000"   (TC-43) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 42","price":"abc","description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 43","price":100000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
category 999     (TC-44) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 43","price":100000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 44","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":999}
category null    (TC-45) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 44","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":999}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 45","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":null}
category "abc"   (TC-46) -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 45","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":null}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 46","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":"abc"}
===== BUG-43 (POST, price: Infinity thô, Content-Type application/json)
   [backend restart xong: 5 sản phẩm]
price Infinity   (TC-209) -> HTTP 400 [text/html; charset=utf-8] <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot; &quot;price&quot;: Infinity, &quot;... is not valid JSON<br> &nbsp;…; bản ghi 5 → 5; bản ghi id  trong GET /api/products: —
===== BUG-44 (POST không có Content-Type: application/json)
   [backend restart xong: 5 sản phẩm]
a) không truyền -ContentType (PS 5.1 tự gửi application/x-www-form-urlencoded) -> HTTP 500 [text/html; charset=utf-8] <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<br> &nbsp; &nbsp;at D:\H…; bản ghi 5 → 5
b) Content-Type: text/plain (như TC-211) -> HTTP 500 [text/html; charset=utf-8] <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<br> &nbsp; &nbsp;at D:\H…; bản ghi 5 → 5
===== BUG-46 (id 999 không tồn tại)
   [backend restart xong: 5 sản phẩm]
GET    /api/products/999 -> HTTP 200 [application/json; charset=utf-8] {}; bản ghi 5 → 5
PUT    /api/products/999 -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 5 → 5
DELETE /api/products/999 -> HTTP 200 [application/json; charset=utf-8] {"message":"Product deleted"}; bản ghi 5 → 5
   GET /api/products (danh sách sau 3 request): 1,2,3,4,5
===== BUG-47 (không token / token sai / token hết hạn / token user)
   [backend restart xong: 5 sản phẩm]
   token user: role trong phản hồi login = user
POST   [không token] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":6}; bản ghi 5 → 6; bản ghi id 6 trong GET /api/products: {"id":6,"name":"SP 7c 47 không token","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
PUT    /1 [không token] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 6 → 6
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"description":"Điện thoại cao cấp của Apple","imageUrl":"https://placehold.co/300x300/png?text=iPhone+15","category_id":1}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 47 không token","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
DELETE /2 [không token] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product deleted"}; bản ghi 6 → 5; GET /api/products/2 -> HTTP 200 [application/json; charset=utf-8] {}
POST   [token sai abc.def.ghi] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":7}; bản ghi 5 → 6; bản ghi id 7 trong GET /api/products: {"id":7,"name":"SP 7c 47 token sai abc.def.ghi","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
PUT    /1 [token sai abc.def.ghi] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 6 → 6
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 47 không token","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 47 token sai abc.def.ghi","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
DELETE /3 [token sai abc.def.ghi] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product deleted"}; bản ghi 6 → 5; GET /api/products/3 -> HTTP 200 [application/json; charset=utf-8] {}
POST   [token hết hạn (exp = 1 giờ trước)] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":8}; bản ghi 5 → 6; bản ghi id 8 trong GET /api/products: {"id":8,"name":"SP 7c 47 token hết hạn (exp = 1 giờ trước)","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
PUT    /1 [token hết hạn (exp = 1 giờ trước)] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 6 → 6
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 47 token sai abc.def.ghi","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 47 token hết hạn (exp = 1 giờ trước)","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
DELETE /4 [token hết hạn (exp = 1 giờ trước)] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product deleted"}; bản ghi 6 → 5; GET /api/products/4 -> HTTP 200 [application/json; charset=utf-8] {}
POST   [token user test@eshop.com] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product created","id":9}; bản ghi 5 → 6; bản ghi id 9 trong GET /api/products: {"id":9,"name":"SP 7c 47 token user test@eshop.com","price":1500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":2}
PUT    /1 [token user test@eshop.com] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product updated"}; bản ghi 6 → 6
      M TRƯỚC: HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 47 token hết hạn (exp = 1 giờ trước)","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
      M SAU:   HTTP 200 [application/json; charset=utf-8] {"id":1,"name":"Sua 7c 47 token user test@eshop.com","price":2500000,"description":"Mô tả 7c","imageUrl":"https://placehold.co/300","category_id":3}
DELETE /5 [token user test@eshop.com] -> HTTP 200 [application/json; charset=utf-8] {"message":"Product deleted"}; bản ghi 6 → 5; GET /api/products/5 -> HTTP 200 [application/json; charset=utf-8] {}
===== BUG-48 (GET /api/products/2)
   [backend restart xong: 5 sản phẩm]
GET /api/products/2 -> HTTP 200 {"id":2,"name":"Samsung Galaxy S24 Ultra","price":"28000000","description":"Màn hình hiển thị xuất sắc, camera siêu zoom","imageUrl":"https://placehold.co/300x300/png?text=Samsung+S24","category_id":1}
   kiểu price trong JSON: String
===== kết thúc
   [backend restart xong: 5 sản phẩm]
```

Output `ui_7c.js` (chuỗi "x" lặp ghi `"x"×N`):

```text
===== BUG-35 (Thêm — Tên vi phạm; Giá 1500000; Danh mục Laptop)
   [backend restart xong: 5 sản phẩm]
A 300×x  (TC-08): giá trị ô Giá tiền lúc bấm="1500000"; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"\"x\"×300","price":1500000,"category_id":2}]; bảng 5 → 6 dòng; dòng mới=["\"x\"×300 | 1500000 ₫"]
   [backend restart xong: 5 sản phẩm]
B "   "  (TC-09): giá trị ô Giá tiền lúc bấm="1500000"; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"   ","price":1500000,"category_id":2}]; bảng 5 → 6 dòng; dòng mới=["    | 1500000 ₫"]
   [backend restart xong: 5 sản phẩm]
C 256×x  (TC-66): giá trị ô Giá tiền lúc bấm="1500000"; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"\"x\"×256","price":1500000,"category_id":2}]; bảng 5 → 6 dòng; dòng mới=["\"x\"×256 | 1500000 ₫"]
===== BUG-36 (Thêm — Tên "Tai nghe UI10"; Giá vi phạm; Danh mục Laptop)
   [backend restart xong: 5 sản phẩm]
-1000            (TC-10): giá trị ô Giá tiền lúc bấm="-1000"; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"Tai nghe UI10","price":-1000,"category_id":2}]; bảng 5 → 6 dòng; dòng mới=["Tai nghe UI10 | -1000 ₫"]
   [backend restart xong: 5 sản phẩm]
0                (TC-67): giá trị ô Giá tiền lúc bấm="0"; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"Tai nghe UI10","price":0,"category_id":2}]; bảng 5 → 6 dòng; dòng mới=["Tai nghe UI10 | 0 ₫"]
   [backend restart xong: 5 sản phẩm]
để trống         (TC-11, TC-205 theo bước SV): giá trị ô Giá tiền lúc bấm=""; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"Tai nghe UI10","price":"","category_id":2}]; bảng 5 → 6 dòng; dòng mới=["Tai nghe UI10 |  ₫"]
   [backend restart xong: 5 sản phẩm]
gõ "１５０００００" (input thật của TC-205, kiểm thêm): giá trị ô Giá tiền lúc bấm=""; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"Tai nghe UI10","price":"","category_id":2}]; bảng 5 → 6 dòng; dòng mới=["Tai nghe UI10 |  ₫"]
===== BUG-37 (Sửa — chọn dòng 'iPhone 15 Pro Max'; Tên vi phạm)
   [backend restart xong: 5 sản phẩm]
300×x  (TC-13): tiêu đề form sau khi bấm 'Sửa'=["📂 Import sản phẩm từ CSV","Sửa sản phẩm"]; hộp thoại=["Cập nhật thành công!"]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=["Thêm sản phẩm mới","Lưu sản phẩm"]; bản ghi 5 → 5
      M TRƯỚC (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"category_id":1}
      M SAU   (GET /api/products): {"id":1,"name":"\"x\"×300","price":30000000,"category_id":1}
      bảng TRƯỚC: ["iPhone 15 Pro Max | 30000000 ₫","Samsung Galaxy S24 Ultra | 28000000 ₫","MacBook Pro M3 | 45000000 ₫","Tai nghe AirPods Pro 2 | 6000000 ₫","Bàn phím cơ Keychron Q1 | 4000000 ₫"]
      bảng SAU:   ["\"x\"×300 | 30000000 ₫","\"x\"×300 | 28000000 ₫","\"x\"×300 | 45000000 ₫","\"x\"×300 | 6000000 ₫","\"x\"×300 | 4000000 ₫"]
   [backend restart xong: 5 sản phẩm]
"   "  (TC-14): tiêu đề form sau khi bấm 'Sửa'=["📂 Import sản phẩm từ CSV","Sửa sản phẩm"]; hộp thoại=["Cập nhật thành công!"]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=["Thêm sản phẩm mới","Lưu sản phẩm"]; bản ghi 5 → 5
      M TRƯỚC (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"category_id":1}
      M SAU   (GET /api/products): {"id":1,"name":"   ","price":30000000,"category_id":1}
      bảng TRƯỚC: ["iPhone 15 Pro Max | 30000000 ₫","Samsung Galaxy S24 Ultra | 28000000 ₫","MacBook Pro M3 | 45000000 ₫","Tai nghe AirPods Pro 2 | 6000000 ₫","Bàn phím cơ Keychron Q1 | 4000000 ₫"]
      bảng SAU:   ["    | 30000000 ₫","    | 28000000 ₫","    | 45000000 ₫","    | 6000000 ₫","    | 4000000 ₫"]
   [backend restart xong: 5 sản phẩm]
256×x  (TC-78): tiêu đề form sau khi bấm 'Sửa'=["📂 Import sản phẩm từ CSV","Sửa sản phẩm"]; hộp thoại=["Cập nhật thành công!"]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=["Thêm sản phẩm mới","Lưu sản phẩm"]; bản ghi 5 → 5
      M TRƯỚC (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"category_id":1}
      M SAU   (GET /api/products): {"id":1,"name":"\"x\"×256","price":30000000,"category_id":1}
      bảng TRƯỚC: ["iPhone 15 Pro Max | 30000000 ₫","Samsung Galaxy S24 Ultra | 28000000 ₫","MacBook Pro M3 | 45000000 ₫","Tai nghe AirPods Pro 2 | 6000000 ₫","Bàn phím cơ Keychron Q1 | 4000000 ₫"]
      bảng SAU:   ["\"x\"×256 | 30000000 ₫","\"x\"×256 | 28000000 ₫","\"x\"×256 | 45000000 ₫","\"x\"×256 | 6000000 ₫","\"x\"×256 | 4000000 ₫"]
===== BUG-38 (Sửa — chọn dòng 'iPhone 15 Pro Max'; Giá vi phạm)
   [backend restart xong: 5 sản phẩm]
-1000    (TC-15): tiêu đề form sau khi bấm 'Sửa'=["📂 Import sản phẩm từ CSV","Sửa sản phẩm"]; hộp thoại=["Cập nhật thành công!"]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=["Thêm sản phẩm mới","Lưu sản phẩm"]; bản ghi 5 → 5
      M TRƯỚC (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"category_id":1}
      M SAU   (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":-1000,"category_id":1}
      bảng TRƯỚC: ["iPhone 15 Pro Max | 30000000 ₫","Samsung Galaxy S24 Ultra | 28000000 ₫","MacBook Pro M3 | 45000000 ₫","Tai nghe AirPods Pro 2 | 6000000 ₫","Bàn phím cơ Keychron Q1 | 4000000 ₫"]
      bảng SAU:   ["iPhone 15 Pro Max | 30000000 ₫","iPhone 15 Pro Max | 28000000 ₫","iPhone 15 Pro Max | 45000000 ₫","iPhone 15 Pro Max | 6000000 ₫","iPhone 15 Pro Max | 4000000 ₫"]
   [backend restart xong: 5 sản phẩm]
0        (TC-79): tiêu đề form sau khi bấm 'Sửa'=["📂 Import sản phẩm từ CSV","Sửa sản phẩm"]; hộp thoại=["Cập nhật thành công!"]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=["Thêm sản phẩm mới","Lưu sản phẩm"]; bản ghi 5 → 5
      M TRƯỚC (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"category_id":1}
      M SAU   (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":0,"category_id":1}
      bảng TRƯỚC: ["iPhone 15 Pro Max | 30000000 ₫","Samsung Galaxy S24 Ultra | 28000000 ₫","MacBook Pro M3 | 45000000 ₫","Tai nghe AirPods Pro 2 | 6000000 ₫","Bàn phím cơ Keychron Q1 | 4000000 ₫"]
      bảng SAU:   ["iPhone 15 Pro Max | 30000000 ₫","iPhone 15 Pro Max | 28000000 ₫","iPhone 15 Pro Max | 45000000 ₫","iPhone 15 Pro Max | 6000000 ₫","iPhone 15 Pro Max | 4000000 ₫"]
   [backend restart xong: 5 sản phẩm]
để trống (TC-16): tiêu đề form sau khi bấm 'Sửa'=["📂 Import sản phẩm từ CSV","Sửa sản phẩm"]; hộp thoại=["Cập nhật thành công!"]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=["Thêm sản phẩm mới","Lưu sản phẩm"]; bản ghi 5 → 5
      M TRƯỚC (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"category_id":1}
      M SAU   (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":"","category_id":1}
      bảng TRƯỚC: ["iPhone 15 Pro Max | 30000000 ₫","Samsung Galaxy S24 Ultra | 28000000 ₫","MacBook Pro M3 | 45000000 ₫","Tai nghe AirPods Pro 2 | 6000000 ₫","Bàn phím cơ Keychron Q1 | 4000000 ₫"]
      bảng SAU:   ["iPhone 15 Pro Max | 30000000 ₫","iPhone 15 Pro Max | 28000000 ₫","iPhone 15 Pro Max | 45000000 ₫","iPhone 15 Pro Max | 6000000 ₫","iPhone 15 Pro Max | 4000000 ₫"]
===== BUG-39 (Thêm — Tên <script>alert(1)</script>)
   [backend restart xong: 5 sản phẩm]
TC-200: giá trị ô Giá tiền lúc bấm="1500000"; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"<script>alert(1)</script>","price":1500000,"category_id":2}]; bảng 5 → 6 dòng; dòng mới=["<script>alert(1)</script> | 1500000 ₫"]
===== BUG-40 (Thêm — Tên "Sản phẩm E-Notation"; Giá 1e5)
   [backend restart xong: 5 sản phẩm]
TC-201: giá trị ô Giá tiền lúc bấm="1e5"; hộp thoại=[]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=[]; bản ghi (GET /api/products) 5 → 6; bản ghi mới=[{"id":6,"name":"Sản phẩm E-Notation","price":100000,"category_id":2}]; bảng 5 → 6 dòng; dòng mới=["Sản phẩm E-Notation | 100000 ₫"]
===== BUG-45 (Sửa — Tên "Sửa UI03", Giá 2500000)
   [backend restart xong: 5 sản phẩm]
   bước 2 SV ghi "ví dụ sản phẩm id = 8": GET /api/products/8 sau seed -> {}; id trong CSDL: [1,2,3,4,5]; bảng UI không có cột id
   [backend restart xong: 5 sản phẩm]
thay bằng dòng seed 'iPhone 15 Pro Max' (id 1): tiêu đề form sau khi bấm 'Sửa'=["📂 Import sản phẩm từ CSV","Sửa sản phẩm"]; hộp thoại=["Cập nhật thành công!"]; ô HTML5 invalid=[]; chữ mới trên trang (ngoài bảng)=["Thêm sản phẩm mới","Lưu sản phẩm"]; bản ghi 5 → 5
      M TRƯỚC (GET /api/products): {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"category_id":1}
      M SAU   (GET /api/products): {"id":1,"name":"Sửa UI03","price":2500000,"category_id":1}
      bảng TRƯỚC: ["iPhone 15 Pro Max | 30000000 ₫","Samsung Galaxy S24 Ultra | 28000000 ₫","MacBook Pro M3 | 45000000 ₫","Tai nghe AirPods Pro 2 | 6000000 ₫","Bàn phím cơ Keychron Q1 | 4000000 ₫"]
      bảng SAU:   ["Sửa UI03 | 30000000 ₫","Sửa UI03 | 28000000 ₫","Sửa UI03 | 45000000 ₫","Sửa UI03 | 6000000 ₫","Sửa UI03 | 4000000 ₫"]
===== BUG-49 + BUG-50 (quan sát form 'Thêm sản phẩm mới' và cột 'Giá')
   [backend restart xong: 5 sản phẩm]
BUG-49: tiêu đề form=["📂 Import sản phẩm từ CSV","Thêm sản phẩm mới"]; số <label> trong form=0; có '*' trong form=false; placeholder=["Tên sản phẩm","Giá tiền","URL Ảnh","Mô tả"]; số <select>=1
BUG-50: ô Giá dòng 'iPhone 15 Pro Max' = "30000000 ₫"
===== kết thúc   [backend restart xong: 5 sản phẩm]
```

### Log sửa dữ kiện 7c (trước → sau)

| BUG | Mục | Trước | Sau | Căn cứ |
|---|---|---|---|---|
| 35, 36, 37, 38, 39, 40, 45, 49, 50 | Tiền điều kiện | (không có bước đăng nhập) | thêm dòng "- Đã đăng nhập trang Admin bằng tài khoản `admin@eshop.com` / `Admin123!`." | bước thiếu: `frontend-admin/src/App.jsx` dòng 188 (`if (!token)` → chỉ hiện form "Admin Login") |
| 36 | Bước 3 | `+ Để trống ô giá tiền: "" (TC-FR15-11, TC-FR15-205)` | `+ Để trống ô giá tiền: "" (TC-FR15-11)` + dòng mới `+ Dán chuỗi chữ số toàn chiều rộng "１５０００００" — ô Giá tiền nhận giá trị rỗng "" (TC-FR15-205)` | inputs TC-FR15-205 (`Giá: "１５０００００"`); Actual TC-205 `giá trị ô Giá tiền trước khi lưu: ""`; 7c: gõ chuỗi này → ô "" |
| 36 | Nhận định | `…hoặc không có giá.` | `…hoặc không có giá (chưa kiểm chứng).` | không có case/evidence về luồng bán (giỏ hàng, đặt hàng) với sản phẩm này |
| 37, 38, 45 | Bước 4 | `Bấm nút "Lưu sản phẩm" (hoặc "Cập nhật sản phẩm").` | `Bấm nút "Lưu sản phẩm".` | `App.jsx` dòng 546: nút duy nhất "Lưu sản phẩm" cho cả Thêm và Sửa |
| 45 | Bước 2 | `(ví dụ sản phẩm id = 8)` | `(ví dụ dòng "iPhone 15 Pro Max", id = 1)` | sau seed chỉ có id 1–5 (`GET /api/products/8` → `{}`); id 8 là sản phẩm harness dựng ở lượt 6; bảng UI không có cột id |
| 45 | Actual | `…giá cũ trên bảng UI (1000000 ₫).` | `…giá cũ trên bảng UI (TC-FR15-03: 1000000 ₫; tái hiện 7c với "iPhone 15 Pro Max": 30000000 ₫).` | 1000000 là giá của M ở TC-03; theo bước đã sửa, giá cũ là 30000000 (output 7c) |
| 44 | Bước 1 | `…Content-Type: application/json (TC-FR15-211).` | `…Content-Type: application/json (TC-FR15-211 gửi Content-Type: text/plain).` | `TC-FR15-211_req.json`: `"Content-Type": "text/plain"` |
| 41 | Nhận định | `…gây sai lệch toàn bộ hệ thống.` | `…gây sai lệch toàn bộ hệ thống (chưa kiểm chứng).` | evidence chỉ cho thấy bản ghi products bị tạo; không có dữ kiện về phần khác |
| 43 | Nhận định | `…kỳ vọng nhận JSON response).` | `…kỳ vọng nhận JSON response) (chưa kiểm chứng).` | không có case cho client (web/admin/mobile) nhận phản hồi này |
| 47 | Nhận định | `Bất kỳ ai trên Internet cũng…` | `Bất kỳ ai trên Internet (chưa kiểm chứng) cũng…` | chỉ kiểm trên localhost; phần "không cần đăng nhập/quyền Admin" có dữ kiện (lượt 6 + 7c) |
| 47 | Bước 1, Trường hợp 2 | `…Token không hợp lệ / sai Chữ ký / Token hết hạn` | `…Token không hợp lệ / sai Chữ ký` | SV quyết bỏ, không có TC |
| 48 | TC liên quan | (không có) | thêm dòng "Ngoài TC: GET /api/products/:id (id chẵn, price null) làm dừng tiến trình backend — AI phát hiện khi kiểm 7c" | SV quyết gộp lỗi sập backend vào BUG-48 (7c2) |
| 48 | Dữ kiện (AI chép) | (không có) | thêm mục "Sập backend (AI phát hiện ở 7c, ngoài bước của SV)": request, phản hồi, stderr nguyên văn, code `server.js` 159–165 | output `crash_48.ps1` (mục "Kiểm 7c2") |
| 48 | Các bước tái hiện, Actual, Yêu cầu, Nhận định | (không có) | thêm chỗ trống `<SV viết: phần sập backend>` cuối mỗi mục | SV viết |

### Điểm SV tự sửa (chữ của SV — AI không sửa)

- Severity/Priority ngoài thang (`bugs/README.md`: Severity Critical/High/Medium/Low, Priority High/Medium/Low): BUG-36 Severity "Major", Priority "Major"; BUG-39 Severity "Major"; BUG-45 Severity "Major".
- BUG-46 tiêu đề: "44xx" (thang mã HTTP là 4xx).
- BUG-46 Expected: "kèm thông báo lỗi cụ thể dạng JSON" — C10 chỉ nêu 4xx (không 2xx, không 5xx), không nêu body.
- BUG-47 Expected: "401 Unauthorized" / "403 Forbidden" — FR-12.2, SEC-02, SEC-03, C5 không nêu mã; C6: "không cố định mã cụ thể".
- BUG-49 Expected: "dấu sao màu đỏ hoặc ký hiệu *" — FR-22.1 chỉ nêu "ký hiệu *" (vế "hoặc" vẫn đúng; SV xem lại).
- Mục "Yêu cầu": không thấy yêu cầu nào được liệt kê mà Actual không vi phạm.

## Kiểm 7c2 — sập backend (gộp vào BUG-48 theo quyết định SV)

Script `HW02/bugs/_repro_C_FR15/7c/crash_48.ps1` (Windows PowerShell 5.1): dừng backend, chạy lại `node server.js` với stderr ghi ra file, POST `price: null`, GET bản ghi vừa tạo, in stderr, restart backend bình thường.

```powershell
powershell -ExecutionPolicy Bypass -File HW02\bugs\_repro_C_FR15\7c\crash_48.ps1
```

Output (20/10/2026):

```text
POST /api/products body: {"name": "SP 7c null", "price": null, "category_id": 2, "description": "Mô tả 7c", "imageUrl": "https://placehold.co/300"}
-> HTTP 200 {"message":"Product created","id":6}
GET /api/products/6 -> lỗi: An error occurred while sending the request.
tiến trình đã dừng: True; mã thoát: 1
--- stderr ---
D:\HK7\Testing\Exercise\HW\eshop-sut\backend\server.js:162
    if (row.id % 2 === 0) row.price = row.price.toString();
                                                ^

TypeError: Cannot read properties of null (reading 'toString')
    at Statement.<anonymous> (D:\HK7\Testing\Exercise\HW\eshop-sut\backend\server.js:162:49)
    at Statement.replacement (D:\HK7\Testing\Exercise\HW\eshop-sut\backend\node_modules\sqlite3\lib\trace.js:25:27)
    at Statement.replacement (D:\HK7\Testing\Exercise\HW\eshop-sut\backend\node_modules\sqlite3\lib\trace.js:25:27)

Node.js v24.15.0
backend restart xong: 5 sản phẩm
```

## Kiểm 7e — chạy lại bước 4a–4c (phần sập backend) SV viết ở BUG-48 (20/10/2026)

Restart backend trước (`restart_backend.ps1`) và sau (cuối `crash_48.ps1`). Bước 4a SV chỉ ghi `"price": null`; các trường khác lấy giá trị hợp lệ như TC. Sau seed, bản ghi mới có id 6 (chẵn) như ví dụ của SV.

```powershell
powershell -ExecutionPolicy Bypass -File HW02\bugs\_repro_C_FR15\7c\restart_backend.ps1
powershell -ExecutionPolicy Bypass -File HW02\bugs\_repro_C_FR15\7c\crash_48.ps1
```

Output:

```text
backend restart xong: 5 sản phẩm
POST /api/products body: {"name": "SP 7c null", "price": null, "category_id": 2, "description": "Mô tả 7c", "imageUrl": "https://placehold.co/300"}
-> HTTP 200 {"message":"Product created","id":6}
GET /api/products/6 -> lỗi: Unable to connect to the remote server
tiến trình đã dừng: True; mã thoát: 
--- stderr ---
D:\HK7\Testing\Exercise\HW\eshop-sut\backend\server.js:162
    if (row.id % 2 === 0) row.price = row.price.toString();
                                                ^

TypeError: Cannot read properties of null (reading 'toString')
    at Statement.<anonymous> (D:\HK7\Testing\Exercise\HW\eshop-sut\backend\server.js:162:49)
    at Statement.replacement (D:\HK7\Testing\Exercise\HW\eshop-sut\backend\node_modules\sqlite3\lib\trace.js:25:27)
    at Statement.replacement (D:\HK7\Testing\Exercise\HW\eshop-sut\backend\node_modules\sqlite3\lib\trace.js:25:27)

Node.js v24.15.0
backend restart xong: 5 sản phẩm
```

Kết quả: tái hiện được — POST trả `HTTP 200 {"message":"Product created","id":6}`; GET /api/products/6 không có phản hồi; tiến trình `node server.js` dừng; stderr giống 7c2. Khác 7c2 ở chi tiết không thuộc chữ SV: thông báo PowerShell lần này là "Unable to connect to the remote server" (7c2: "An error occurred while sending the request."), và `ExitCode` không đọc được (trống) — 7c2 đọc được 1.

Log sửa dữ kiện 7e (trước → sau): không sửa chữ SV. Đối chiếu: "id = 6" khớp; "mã thoát 1" khớp 7c2; "TypeError: Cannot read properties of null (reading 'toString') tại dòng 162" khớp stderr; "Connection refused" khớp 7c; "không có khối try-catch" khớp `backend/server.js` (không có `try {`, không có `process.on('uncaughtException')`).

| BUG | Mục | Trước | Sau | Căn cứ |
|---|---|---|---|---|
| 48 | Yêu cầu | `<SV viết: phần sập backend>` | 2 dòng yêu cầu bị vi phạm (ổn định tiến trình backend — ngầm định; API spec §3.2) + 1 dòng "Chưa đánh giá được: FR-06" | lệnh 7e mục 1 — AI đề xuất, chờ SV duyệt |

Kiểm trùng 7e (`gh issue list -R tkob-team/eshop-sut --state all --limit 1000`, mọi tác giả): 135 issue (lớn nhất #180); issue mới từ sau 7a (20/10/2026 19:11): 0. Từ khoá crash/sập/dừng/server dừng/tiến trình/toString/DoS/unhandled/uncaught/connection refused/"Cannot read properties of null" trên tiêu đề + nội dung: khớp #25, #26, #28 — cả ba của FR-01 (#25: HTTP 413, "tiến trình backend không dừng"; #26: POST /api/register text/plain → HTTP 500, "tiến trình backend không dừng"; #28: nhãn '*', "không gây sập app"). Không trùng.

### Log sửa 7f0 (trước → sau)

| BUG / nhóm | Mục | Trước | Sau | Căn cứ |
|---|---|---|---|---|
| BUG-48 | Yêu cầu | có dòng "- **API spec §3.2:** (`api_specification.md` dòng 84–85) `GET /api/products/:id` — Xem chi tiết một sản phẩm. — (sập backend: request không nhận được phản hồi nào)" | bỏ dòng này; giữ dòng "Ổn định tiến trình backend (ngầm định)" và "Chưa đánh giá được: FR-06" | SV quyết: dòng "ngầm định" đã đủ căn cứ cho phần sập backend |
| G12 | Tổng hợp + "Yêu cầu / giả định bị vi phạm" | "…ổn định tiến trình backend (ngầm định), API spec §3.2…" | bỏ "API spec §3.2" | như trên |

## 7f — tạo issue (20/10/2026)

- Tài khoản `gh api user` = ThachHaoo; tạo tuần tự BUG-35 → 50 trên `tkob-team/eshop-sut`, label `bug`, tiêu đề = "[FR-15] " + tiêu đề trong .md → #181–#196 (bảng ánh xạ ở đầu file).
- Body = nội dung .md, bỏ mục "Link GitHub Issue"; dưới "Ảnh tiêu biểu" thêm dòng `[SV kéo ảnh … vào đây — alt = …]` để SV kéo ảnh.
- Bản che (gốc giữ nguyên), sinh bằng `_repro_C_FR15/7c/redact_7f.js`: `_issue_redacted/TC-FR15-209_api_redacted.png`, `BUG-43.txt` (TC-209); `_issue_redacted/TC-FR15-211_api_redacted.png`, `BUG-44.txt` (TC-211); `_issue_redacted/BUG-48.txt` (stderr). Body issue BUG-48: đường dẫn máy trong stderr thay bằng `<SUT_DIR>` (file .md giữ nguyên văn). BUG-43, 44, 48 .md: thêm dòng "Bản che dùng cho issue" trong mục Bằng chứng.
- Ảnh còn lại (UI, API JSON, ảnh chạy tay TC-90/92) không chứa đường dẫn máy/tên người dùng (đã xem).
