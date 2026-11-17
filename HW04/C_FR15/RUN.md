# C_FR15 – nhật ký lượt chạy

Lệnh (PowerShell, `HW04\tests`): `npx playwright test C_FR15 --project=<chrome|edge|firefox>`. Spec @ `370c9cd` (bước 3), config trace off @ `597bda7`. Backend/web/admin chạy sẵn; `beforeAll` restart backend (CSDL seed sạch).

| Lượt | Bắt đầu (Run by) | Spec | Report | Kết quả |
|---|---|---|---|---|
| Lượt thử 1 – chrome | 2026-11-17T14:42:30+07:00 | `370c9cd` | `HW04/reports/chrome_20261117T144230/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 1 – edge | 2026-11-17T14:43:14+07:00 | `370c9cd` | `HW04/reports/edge_20261117T144314/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 1 – firefox | 2026-11-17T14:43:59+07:00 | `370c9cd` | `HW04/reports/firefox_20261117T144359/` | 6 Pass, 9 Fail, 0 Blocked |

Metadata `Run by` trong `results.json` cả 3: `23120255 · <ISO +07:00>`. Mỗi report ≈ 2.1 MB.

## Lượt thử 1 – dữ kiện (AI tổng hợp từ results.json, chưa kết luận)

### 15 TC × 3 trình duyệt so với HW02

| TC | Thao tác | HW02 | chrome | edge | firefox | Assertion fail (giống nhau ở 3 trình duyệt) |
|---|---|---|---|---|---|---|
| TC-FR15-01 | Thêm | Pass | Pass | Pass | Pass | – |
| TC-FR15-03 | Sửa | Fail | Fail | Fail | Fail | dòng của M: 'Giá' (so giá trị số); mọi dòng khác SAU_UI = TRƯỚC_UI |
| TC-FR15-05 | Xóa | Pass | Pass | Pass | Pass | – |
| TC-FR15-07 | Thêm | Pass | Pass | Pass | Pass | – |
| TC-FR15-10 | Thêm | Fail | Fail | Fail | Fail | có thông báo lỗi; bảng SAU_UI = TRƯỚC_UI; GET /api/products SAU = TRƯỚC |
| TC-FR15-11 | Thêm | Fail | Fail | Fail | Fail | có thông báo lỗi; bảng SAU_UI = TRƯỚC_UI; GET /api/products SAU = TRƯỚC |
| TC-FR15-15 | Sửa | Fail | Fail | Fail | Fail | bảng SAU_UI = TRƯỚC_UI; GET /api/products SAU = TRƯỚC; M_SAU = M_TRƯỚC |
| TC-FR15-65 | Thêm | Pass | Pass | Pass | Pass | – |
| TC-FR15-66 | Thêm | Fail | Fail | Fail | Fail | có thông báo lỗi; bảng SAU_UI = TRƯỚC_UI; GET /api/products SAU = TRƯỚC |
| TC-FR15-67 | Thêm | Fail | Fail | Fail | Fail | có thông báo lỗi; bảng SAU_UI = TRƯỚC_UI; GET /api/products SAU = TRƯỚC |
| TC-FR15-68 | Thêm | Pass | Pass | Pass | Pass | – |
| TC-FR15-77 | Sửa | Pass | Pass | Pass | Pass | – |
| TC-FR15-78 | Sửa | Fail | Fail | Fail | Fail | bảng SAU_UI = TRƯỚC_UI; GET /api/products SAU = TRƯỚC; M_SAU = M_TRƯỚC |
| TC-FR15-200 | Thêm | Fail | Fail | Fail | Fail | có thông báo lỗi |
| TC-FR15-201 | Thêm | Fail | Fail | Fail | Fail | form chặn: GET /api/products SAU = TRƯỚC |

- Verdict khác HW02: **không có** (15/15 trùng). Khác giữa trình duyệt: **không có**. Blocked / timeout / `backend sập`: 0.

### TC Pass – annotation để SV xét pass giả

| TC | `oracle thông báo yếu` | `oracle không tự động` | `price dạng chuỗi (BUG-48)` | Quan sát (chrome; edge/firefox giống) |
|---|---|---|---|---|
| TC-FR15-01 | – | – | – | không ô lỗi, không hộp thoại, không thông báo; POST → 200, GET → 200 |
| TC-FR15-05 | – | – | **có** (3 trình duyệt): M_TRƯỚC price = "1000000" (M id 6) | DELETE /api/products/6 → 200, GET → 200 |
| TC-FR15-07 | – | – | – | ô không hợp lệ: "Tên sản phẩm: Please fill out this field." (ghi 2 lần, xem ghi chú harness); không request |
| TC-FR15-65 | – | – | – | POST → 200, GET → 200 |
| TC-FR15-68 | – | – | – | ô Giá `0.1` → `0.1`; POST → 200, GET → 200 |
| TC-FR15-77 | – | – | – | hộp thoại "Cập nhật thành công!"; PUT /api/products/7 → 200 |

- Annotation `oracle thông báo yếu` chỉ xuất hiện ở TC Fail: TC-15, TC-78 (chỉ có hộp thoại "Cập nhật thành công!"). `price dạng chuỗi (BUG-48)` ở TC Fail: TC-15 (M_SAU "-1000"), TC-78 (M_SAU "1000000").

### Ghi chú harness

- Ô không hợp lệ ở TC-07 được ghi 2 lần: spec gọi `form.checkValidity()` trước khi bấm (để biết có gửi request không) — lệnh này cũng bắn sự kiện `invalid` mà hook đang nghe. Chỉ xảy ra khi form thật sự không hợp lệ (cùng điều kiện trình duyệt hiện bong bóng), không đổi verdict; chưa sửa.
- `results.json` ghi mỗi annotation 2 lần (mức test và mức result) như A/B.

## Lượt chính thức

| Lượt | Bắt đầu (Run by) | Spec | Report | Kết quả |
|---|---|---|---|---|
| Chính thức – chrome | 2026-11-17T15:11:43+07:00 | `2e9e454` | `HW04/reports/chrome_20261117T151143/` | 6 Pass, 9 Fail, 0 Blocked |
| Chính thức – edge | 2026-11-17T15:12:25+07:00 | `2e9e454` | `HW04/reports/edge_20261117T151225/` | 6 Pass, 9 Fail, 0 Blocked |
| Chính thức – firefox | 2026-11-17T15:13:06+07:00 | `2e9e454` | `HW04/reports/firefox_20261117T151306/` | 6 Pass, 9 Fail, 0 Blocked |

- `Run by` (metadata `results.json`) cả 3: `23120255 · <ISO +07:00>`, khớp tên thư mục.
- Verdict trùng HW02 15/15, trùng lượt thử 1, không lệch giữa trình duyệt. Gộp + nhóm Fail: `results.md`, `bug_groups.md` (9 nhóm), `evidence/` (27 ảnh lúc kết thúc + 27 ảnh `_after-save`).
