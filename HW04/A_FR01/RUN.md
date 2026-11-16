# A_FR01 – nhật ký lượt chạy

| Lượt | Thời điểm (Run by) | Spec @ commit | Report | Kết quả |
|---|---|---|---|---|
| Lượt thử 1 – chrome | 2026-11-17T00:25:37+07:00 | `9a5e558` (bản AI bước 3) | `HW04/reports/chrome_20261117T002537/` | 1 Fail (TC-FR01-01) + 14 did not run |
| Lượt thử 1 – edge | 2026-11-17T00:26:42+07:00 | `9a5e558` | `HW04/reports/edge_20261117T002642/` | 1 Fail (TC-FR01-01) + 14 did not run |
| Lượt thử 1 – firefox | 2026-11-17T00:27:39+07:00 | `9a5e558` | `HW04/reports/firefox_20261117T002739/` | 1 Fail (TC-FR01-01) + 14 did not run |

## Lượt thử 1 – ghi chú

- SV chạy trên máy mình, mỗi trình duyệt một lượt (`npx playwright test A_FR01 --project=<chrome|edge|firefox>`).
- 14 TC "did not run": spec bản AI đặt `test.describe.configure({ mode: 'serial' })` → TC đầu Fail thì Playwright bỏ qua mọi TC còn lại (annotation `serial`). Đây là lỗi của script, không phải kết quả của 14 TC.
- Sửa ở commit `HW04[A-FR01] 5/6a – sửa: bỏ mode serial (1 Fail chặn 14 TC)`. Lượt thử 1 không dùng làm lượt chính thức.
