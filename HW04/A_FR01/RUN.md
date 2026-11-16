# A_FR01 – nhật ký lượt chạy

| Lượt | Thời điểm (Run by) | Spec @ commit | Report | Kết quả |
|---|---|---|---|---|
| Lượt thử 1 – chrome | 2026-11-17T00:25:37+07:00 | `9a5e558` (bản AI bước 3) | `HW04/reports/chrome_20261117T002537/` | 1 Fail (TC-FR01-01) + 14 did not run |
| Lượt thử 1 – edge | 2026-11-17T00:26:42+07:00 | `9a5e558` | `HW04/reports/edge_20261117T002642/` | 1 Fail (TC-FR01-01) + 14 did not run |
| Lượt thử 1 – firefox | 2026-11-17T00:27:39+07:00 | `9a5e558` | `HW04/reports/firefox_20261117T002739/` | 1 Fail (TC-FR01-01) + 14 did not run |

| Lượt thử 2 – chrome | 2026-11-17T00:31:49+07:00 | `6fc76b5` (5/6a) | `HW04/reports/chrome_20261117T003149/` | 8 Fail, 7 Pass |
| Lượt thử 2 – edge | 2026-11-17T00:34:25+07:00 | `6fc76b5` | `HW04/reports/edge_20261117T003425/` | 8 Fail, 7 Pass |
| Lượt thử 2 – firefox | 2026-11-17T00:37:11+07:00 | `6fc76b5` | `HW04/reports/firefox_20261117T003711/` | 8 Fail, 7 Pass |
| Lượt thử 2 – chrome (chạy lại) | 2026-11-17T00:45:04+07:00 | `6fc76b5` | `HW04/reports/chrome_20261117T004504/` | 8 Fail, 7 Pass |
| **Chính thức – chrome** | 2026-11-17T01:01:15+07:00 | `3d19917` (5/6d) | `HW04/reports/chrome_20261117T010115/` | 8 Fail, 7 Pass |
| **Chính thức – edge** | 2026-11-17T01:04:19+07:00 | `3d19917` | `HW04/reports/edge_20261117T010419/` | 8 Fail, 7 Pass |
| **Chính thức – firefox** | 2026-11-17T01:07:08+07:00 | `3d19917` | `HW04/reports/firefox_20261117T010708/` | 8 Fail, 7 Pass |

## Lượt thử 1 – ghi chú

- SV chạy trên máy mình, mỗi trình duyệt một lượt (`npx playwright test A_FR01 --project=<chrome|edge|firefox>`).
- 14 TC "did not run": spec bản AI đặt `test.describe.configure({ mode: 'serial' })` → TC đầu Fail thì Playwright bỏ qua mọi TC còn lại (annotation `serial`). Đây là lỗi của script, không phải kết quả của 14 TC.
- Sửa ở commit `HW04[A-FR01] 5/6a – sửa: bỏ mode serial (1 Fail chặn 14 TC)`. Lượt thử 1 không dùng làm lượt chính thức.

## Lượt thử 2 – ghi chú

- Spec sau 5/6a (bỏ serial), trước các sửa 5/6b–5/6d theo review của SV (`review_sv.md`).
- Cả 4 report: Fail = TC-FR01-01, 02, 64, 68, 74, 77, 202, 211; Pass = 05, 07, 17, 18, 22, 23, 63 (trùng nhau giữa các trình duyệt).
- Không dùng làm lượt chính thức: spec còn đồng bộ submit bằng `Promise.race` + `catch` rỗng và gọi oracle API không chờ POST.

## Lượt chính thức – ghi chú

- Spec @ `3d19917` (sau 5/6b–5/6d). Lượt chạy bắt đầu sau commit này (00:58); mọi TC có annotation `phản hồi` (chỉ có từ 5/6b).
- Kiểm "Run by" (17/11, AI mở `index.html` bằng Chrome): tiêu đề report và tên tab đều là `HW04 EShop – <trình duyệt> – Run by: 23120255 · <ISO>`, metadata `Run by` khớp; ISO có múi giờ +07:00.
- Fail = TC-FR01-01, 02, 64, 68, 74, 77, 202, 211; Pass = 05, 07, 17, 18, 22, 23, 63 — trùng nhau ở 3 trình duyệt. Gộp: `results.md`, `bug_groups.md`.
