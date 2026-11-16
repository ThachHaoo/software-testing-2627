# B_FR07 – nhật ký lượt chạy

Lệnh (PowerShell, `HW04\tests`): `npx playwright test B_FR07 --project=<chrome|edge|firefox>`. Spec @ `7e75536` (bước 3), config trace off @ `597bda7`. Backend/web/admin chạy sẵn; `beforeAll` restart backend (CSDL seed sạch).

| Lượt | Bắt đầu (Run by) | Spec | Report | Kết quả |
|---|---|---|---|---|
| Lượt thử 1 – chrome | 2026-11-17T01:43:50+07:00 | `7e75536` | `HW04/reports/chrome_20261117T014350/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 1 – edge | 2026-11-17T01:45:49+07:00 | `7e75536` | `HW04/reports/edge_20261117T014549/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 1 – firefox | 2026-11-17T01:47:56+07:00 | `7e75536` | `HW04/reports/firefox_20261117T014756/` | 6 Pass, 9 Fail, 0 Blocked |

Metadata `Run by` trong `results.json` của cả 3: `23120255 · <ISO +07:00>` (khớp cột Bắt đầu). Mỗi report ≈ 1.2 MB.

## Lượt thử 1 – dữ kiện (AI tổng hợp từ results.json, chưa kết luận)

### 15 TC × 3 trình duyệt so với HW02

| TC | HW02 | chrome | edge | firefox | Assertion fail (giống nhau ở 3 trình duyệt) |
|---|---|---|---|---|---|
| TC-FR07-01 | Fail | Fail | Fail | Fail | giỏ trống: có img/svg minh hoạ |
| TC-FR07-02 | Fail | Fail | Fail | Fail | B21 phản hồi ≤ 2 s; các dòng giỏ SAU; số dòng SAU; Tổng SAU |
| TC-FR07-04 | Fail | Fail | Fail | Fail | các dòng giỏ SAU; Tổng SAU; badge SAU |
| TC-FR07-08 | Fail | Fail | Fail | Fail | hiện dialog xác nhận sau khi bấm xoá |
| TC-FR07-10 | Pass | Pass | Pass | Pass | – |
| TC-FR07-11 | Pass | Pass | Pass | Pass | – |
| TC-FR07-13 | Pass | Pass | Pass | Pass | – |
| TC-FR07-60 | Pass | Pass | Pass | Pass | – |
| TC-FR07-61 | Fail | Fail | Fail | Fail | các dòng giỏ SAU; số dòng SAU; Tổng SAU |
| TC-FR07-62 | Fail | Fail | Fail | Fail | các dòng giỏ SAU; số dòng SAU; Tổng SAU |
| TC-FR07-63 | Fail | Fail | Fail | Fail | các dòng giỏ SAU; số dòng SAU; Tổng SAU |
| TC-FR07-64 | Fail | Fail | Fail | Fail | các dòng giỏ SAU; số dòng SAU; Tổng SAU |
| TC-FR07-66 | Pass | Pass | Pass | Pass | – |
| TC-FR07-200 | Pass | Pass | Pass | Pass | – |
| TC-FR07-205 | Fail | Fail | Fail | Fail | B21 phản hồi ≤ 2 s; lần 1: có dòng id 5, Số lượng id 5; lần 2: có dòng id 5, Số lượng id 5, số dòng |

- Verdict khác HW02: **không có** (15/15 trùng).
- Verdict khác giữa các trình duyệt: **không có**.
- Blocked / timeout: 0.

### TC Pass – annotation để SV xét pass giả

- Annotation `oracle không tự động` / `oracle thông báo yếu` trên TC Pass: **không có** (2 annotation này chỉ xuất hiện ở TC-08 và TC-01, đều Fail).
- Annotation dữ kiện của TC Pass (giống nhau ở 3 trình duyệt):

| TC | Ô Số lượng (gõ → value) | Phản hồi sau khi bấm thêm | Dialog sau khi bấm xoá | TRƯỚC → SAU (dòng: tên × SL; Tổng) |
|---|---|---|---|---|
| TC-FR07-10 | `-3` → `-3` | không có thay đổi nhìn thấy trong 2000 ms | – | iPhone 15 Pro Max × 1; 30000000 → giống TRƯỚC |
| TC-FR07-11 | `1.5` → `1.5` | không có thay đổi nhìn thấy trong 2000 ms | – | iPhone 15 Pro Max × 1; 30000000 → giống TRƯỚC |
| TC-FR07-13 | `abc` → `""` | không có thay đổi nhìn thấy trong 2000 ms | – | iPhone 15 Pro Max × 1; 30000000 → giống TRƯỚC |
| TC-FR07-60 | `0` → `0` | không có thay đổi nhìn thấy trong 2000 ms | – | iPhone 15 Pro Max × 1; 30000000 → giống TRƯỚC |
| TC-FR07-66 | – | – | `[]` (không có dialog) | Tai nghe AirPods Pro 2 × 1; 6000000 → giỏ trống |
| TC-FR07-200 | `<script>alert(1)</script>` → `""` | không có thay đổi nhìn thấy trong 2000 ms | – | giỏ trống → giỏ trống |

### Ghi chú harness

- `results.json` ghi mỗi annotation 2 lần (mức test và mức result); script tổng hợp đã khử trùng lặp. Không ảnh hưởng verdict.
