# B_FR07 – nhật ký lượt chạy

Lệnh (PowerShell, `HW04\tests`): `npx playwright test B_FR07 --project=<chrome|edge|firefox>`. Spec @ `7e75536` (bước 3), config trace off @ `597bda7`. Backend/web/admin chạy sẵn; `beforeAll` restart backend (CSDL seed sạch).

| Lượt | Bắt đầu (Run by) | Spec | Report | Kết quả |
|---|---|---|---|---|
| Lượt thử 1 – chrome | 2026-11-17T01:43:50+07:00 | `7e75536` | `HW04/reports/chrome_20261117T014350/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 1 – edge | 2026-11-17T01:45:49+07:00 | `7e75536` | `HW04/reports/edge_20261117T014549/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 1 – firefox | 2026-11-17T01:47:56+07:00 | `7e75536` | `HW04/reports/firefox_20261117T014756/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 2 – chrome | 2026-11-17T13:55:45+07:00 | `c8a2ce9` (5/6a–c) | `HW04/reports/chrome_20261117T135545/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 2 – edge | 2026-11-17T13:57:10+07:00 | `c8a2ce9` | `HW04/reports/edge_20261117T135710/` | 6 Pass, 9 Fail, 0 Blocked |
| Lượt thử 2 – firefox | 2026-11-17T13:58:36+07:00 | `c8a2ce9` | `HW04/reports/firefox_20261117T135836/` | 5 Pass, 10 Fail, 0 Blocked |
| Chạy riêng TC-60 – firefox (`--grep "TC-FR07-60 " --repeat-each=3`) | 2026-11-17T14:08:40+07:00 | `c8a2ce9` | `HW04/reports/firefox_20261117T140840/` | 3/3 Pass |
| **Chính thức – chrome** | 2026-11-17T14:11:03+07:00 | `c8a2ce9` | `HW04/reports/chrome_20261117T141103/` | 6 Pass, 9 Fail, 0 Blocked |
| **Chính thức – edge** | 2026-11-17T14:12:30+07:00 | `c8a2ce9` | `HW04/reports/edge_20261117T141230/` | 6 Pass, 9 Fail, 0 Blocked |
| **Chính thức – firefox** | 2026-11-17T14:13:59+07:00 | `c8a2ce9` | `HW04/reports/firefox_20261117T141359/` | 6 Pass, 9 Fail, 0 Blocked |

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

## Lượt thử 2 – dữ kiện (AI tổng hợp từ results.json, chưa kết luận, chưa sửa)

- Spec @ `c8a2ce9` (sau 5/6a từ khoá giỏ trống vào data, 5/6b minh hoạ trong khối giỏ trống, 5/6c ảnh `<TC>_after-action`). `Run by` cả 3: `23120255 · <ISO +07:00>`. Mỗi report ≈ 2.1–2.2 MB.
- Verdict trùng lượt thử 1 ở chrome/edge (15/15) và ở firefox 14/15. Khác duy nhất: **TC-FR07-60 trên firefox** (Fail; lượt thử 1 firefox Pass; lượt thử 2 chrome/edge Pass).

### TC-FR07-60 – firefox, lượt thử 2

| Mục | Giá trị |
|---|---|
| Lỗi (nguyên văn) | `Error: worker process exited unexpectedly (code=3221226505, signal=null)` — 3221226505 = `0xC0000409` |
| Assertion fail | **không có** (không có lỗi `expect`) |
| Thời lượng | 0 ms; bắt đầu 06:59:23.214Z (UTC) ngay sau TC-13 (Pass, 3885 ms) cùng worker 4 |
| Annotation | không có (kể cả `expected`, `hw02`, `TRƯỚC`, `phản hồi sau khi bấm thêm`) → thân test chưa chạy |
| Ảnh `TC-FR07-60_after-action` / ảnh lỗi | không có attachment |
| Worker | worker 4 chạy TC-10, 11, 13 (Pass) rồi thoát khi vào TC-60; TC-61 chạy ở worker 5 (beforeAll restart backend lại: "backend restart xong: 5 sản phẩm") |
| Lượt thử 1 firefox (`7e75536`) | Pass; annotation: ô Số lượng `0` → `0`; phản hồi "không có thay đổi nhìn thấy trong 2000 ms"; TRƯỚC = SAU (iPhone 15 Pro Max × 1; 30000000) |
| Lượt thử 2 chrome/edge | Pass; annotation giống lượt thử 1 firefox; có ảnh `TC-FR07-60_after-action` |

Đối chiếu code (5/6b, 5/6c):
- 5/6b (minh hoạ giỏ trống): chỉ chạy khi expected có "img hoặc svg" (oracle `before.illustration`) = chỉ TC-01. TC-60 không đi qua đoạn này; ngoài ra thân TC-60 chưa chạy.
- 5/6c (ảnh song song cửa sổ 2 s): đoạn này nằm sau bấm "Thêm vào giỏ hàng" trong thân test; TC-60 chưa tới đó (0 ms, không annotation). Cùng worker 4 đã chạy đoạn 5/6c ở TC-10, 11, 13 (đều Pass, có ảnh) trước khi worker thoát — dữ kiện này không đủ để loại hẳn hay khẳng định liên quan.
- Theo quy ước HW04 (CLAUDE.md §6, lỗi không có assertion fail = lỗi harness → Blocked, không lập bug): ô này là ứng viên Blocked; `merge_reports.py` hiện đếm `failed` không có annotation `blocked` là Fail.

### Lượt 13:46:05–07 (không thuộc A/B)

- 13:46:05–07: global-setup báo backend chưa chạy, 0 test → 3 report rỗng đã xoá (lệnh #14), không commit.

### TC-FR07-60 / firefox – kết luận lượt thử 2 (lệnh #14)

- Lượt thử 2: worker crash `0xC0000409`, thân test chưa chạy (0 ms, không annotation, không assertion).
- SV chạy riêng `npx playwright test B_FR07 --project=firefox --grep "TC-FR07-60 " --repeat-each=3`: **3/3 Pass** → lỗi hạ tầng (worker Firefox crash), không lập bug.

## Lượt chính thức – ghi chú

- Spec + page object + fixture @ `c8a2ce9` (commit spec mới nhất), config @ `597bda7` (trace off). Mỗi report ≈ 2.1 MB.
- Kiểm "Run by" (17/11, AI mở `index.html` bằng Chrome): tiêu đề `HW04 EShop – <trình duyệt> – Run by: 23120255 · <ISO +07:00>` ở cả 3 report (và report chạy riêng TC-60).
- Fail = TC-FR07-01, 02, 04, 08, 61, 62, 63, 64, 205; Pass = 10, 11, 13, 60, 66, 200 — trùng ở 3 trình duyệt, trùng HW02 và lượt thử 1.
- Gộp (bước 6): `results.md`, `bug_groups.md` (6 nhóm G1–G6), `evidence/` 54 ảnh = 27 ảnh lúc kết thúc + 27 ảnh `<TC>_after-action[-k]_<trình duyệt>` (chỉ TC Fail; TC-01 không có thao tác chính nên không có ảnh after-action; TC-205 có 2).
