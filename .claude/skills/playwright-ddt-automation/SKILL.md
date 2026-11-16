---
name: playwright-ddt-automation
description: Chuyển test case đã thiết kế (testcases.json của HW02) thành script Playwright data-driven chạy đa trình duyệt, theo 6 bước có điểm dừng cho người review — chọn TC → fixture/page object → sinh spec → list + typecheck → SV review/sửa → gộp kết quả 3 report và gom nhóm Fail. Dữ liệu và expected nằm ở file JSON riêng (chép nguyên văn + sha1), output AI đóng băng trước khi sửa. Dùng khi người dùng nói "automation", "tự động hoá test case", "data-driven", "Playwright đa trình duyệt", "HW04", hoặc gọi /playwright-ddt-automation kèm mã feature và số bước.
---

# Playwright data-driven automation theo từng bước

Mỗi lần gọi **làm một bước rồi dừng** để người dùng review và commit. Đề chấm việc "dẫn AI qua từng bước", và phần gap analysis cần diff được giữa bản AI và bản SV sửa.

Gọi: `/playwright-ddt-automation <X_FRnn> <bước>` — vd `A_FR01 1`. Thiếu số bước → xem commit `HW04[X-FRnn] k/6` gần nhất, hỏi lại.

Đường dẫn (HW04): nguồn `HW02/<X_FRnn>/testcases.json` · dữ liệu `HW04/data/<X_FRnn>.json` · tài liệu feature `HW04/<X_FRnn>/` · spec `HW04/tests/<X_FRnn>.spec.ts` · fixture `HW04/tests/fixtures/` · report `HW04/reports/<project>_<ts>/` · đóng băng `HW04/appendix/ai-outputs/<X_FRnn>/step<k>/`.

## Luật (vi phạm = dừng, báo người dùng)

1. **Không đổi expected hay assertion để test xanh.** expected chép nguyên văn từ HW02 tại commit nguồn, khoá bằng sha1; `check_data.py` và fixture đều kiểm. Muốn đổi oracle → hỏi người dùng, ghi lý do, đổi ở HW02 bằng commit riêng rồi chọn lại.
2. **Timeout = Blocked**, không Fail, không lập bug. Test fail chỉ vì `TimeoutError` (không assertion nào fail) là lỗi harness.
3. **Healer / tự sửa** chỉ được sửa **selector** và **chờ** (wait/locator), mỗi lần ghi lý do trong commit; không đụng dữ liệu, expected, assertion.
4. **Đóng băng output AI** bằng `freeze.py` TRƯỚC khi người dùng sửa; không bao giờ sửa file đã đóng băng.
5. **Không viết mô tả bug** (tiêu đề, steps, expected/actual, severity). Bước 6 chỉ gom dữ kiện.
6. Fail ≠ bug: cô lập nguyên nhân (chạy lại, restart backend, so UI với API) trước khi người dùng kết luận.
7. Quy định khoá học/repo (CLAUDE.md, skill khoá học) thắng skill này.

## Các bước — mỗi bước một commit `HW04[X-FRnn] k/6: …`

### 1 — Chọn TC (AI → SV duyệt)
- `select_tc.py <testcases.json> --candidates` → bảng ứng viên: tầng UI, suite `matrix` có `inputs`. Bỏ suite API, suite checklist/steps (không có dữ liệu vào), case quan sát tay/không có Expected theo SRS.
- Chọn **15 TC** (đề ≥ 12, dư 3 để bỏ case không tự động được): đủ Positive / Negative / Boundary; **ưu tiên TC từng Fail ở HW02**; mỗi nhóm triệu chứng (cùng bug) giữ 1–3 đại diện thay vì lấy hết; giữ vài TC Pass làm đối chứng.
- Viết `<feature-dir>/selection.json` (mẫu `assets/selection.example.json`: ids, reasons, excluded, criteria, type_override cho case HW02 không ghi `type` — đánh dấu "(suy ra)").
- `select_tc.py … --selection … --data … --md …` → `HW04/data/<X_FRnn>.json` (tc_id, title, suite, type, technique, bva_point, inputs, **expected nguyên văn**, expected_sha1, notes, hw02 status, nguồn = commit HW02) + `selection.md`.
- `check_data.py` phải 0 lỗi → `freeze.py --step 1` → commit → **DỪNG cho SV duyệt**.

### 2 — Fixture / page object (AI)
- Từ `assets/ddt-fixture.template.ts`: `loadCases` (đọc data + kiểm sha1), `resetDb` (`tools/restart_backend.ps1`), fixture `api` có token admin, `blocked()`; page object của form/màn hình feature với selector lấy từ **mã UI thật** (nhãn, role, placeholder) — không bịa.
- Không chứa dữ liệu test. `freeze.py --step 2` → commit → dừng.

### 3 — Sinh spec (AI)
- Từ `assets/spec.template.ts`: `for (const c of loadCases(...))`, tiêu đề `"<tc_id> <title>"`, giá trị từ `c.inputs` (thay `{ts}`), oracle từ `c.expected`.
- ≥ 3 kiểu assertion: **trạng thái UI** (`toBeVisible`/`toHaveURL`), **nội dung thông báo** (`toHaveText`/`toContainText`), **oracle dữ liệu qua API trước/sau** (`toEqual`), **đếm/giá trị** (`toHaveCount`/`toHaveValue`); dùng `expect.soft`.
- Điều kiện chặn đã biết (trường đặc tả có mà UI không có…) → `blocked('<lý do + case gốc>')`, không Fail giả.
- `freeze.py --step 3` → commit → dừng.

### 4 — List + typecheck (AI chạy, SV chạy 3 trình duyệt)
- Claude Code **chỉ** chạy: `npx playwright test <X_FRnn> --list --reporter=list` (tránh sinh report rỗng) và `npx tsc --noEmit`. Báo số test = số TC trong data.
- SV chạy `npm run test:chrome`, `test:edge`, `test:firefox` trên máy mình → 3 report có "Run by" + ISO timestamp. AI không chạy lượt chính thức, không sửa report.

### 5 — SV review và sửa
- SV đọc spec, so với bản đóng băng step3, sửa. **Mỗi lần sửa một commit riêng có sửa `.spec.ts`**: `HW04[X-FRnn] 5/6x – sửa: <tóm tắt>` (x = a, b, c…).
- AI không gợi ý edge case/assertion còn thiếu trong lúc SV review. Chỉ khi SV hỏi "vì sao AI bỏ sót" sau khi đã commit phần của SV mới trả lời — trung thực, tách *đã nghĩ tới nhưng không đưa vào* với *không nghĩ tới*.

### 6 — Gộp kết quả (AI gộp, SV viết bug)
- `merge_reports.py <data> <feature-dir> <report chrome> <report edge> <report firefox>` → `results.md` (Pass/Fail/Blocked theo trình duyệt, cột HW02) + `bug_groups.md` (TC Fail gom theo lỗi đầu tiên, chỉ dữ kiện).
- SV cô lập nguyên nhân, viết bug + GitHub Issue (ảnh). AI chỉ kiểm trường thiếu, chạy `gh issue create --body-file` với file SV viết.

## Lệnh

```bash
S=.claude/skills/playwright-ddt-automation/scripts
python $S/select_tc.py HW02/A_FR01/testcases.json --candidates
python $S/select_tc.py HW02/A_FR01/testcases.json --selection HW04/A_FR01/selection.json --data HW04/data/A_FR01.json --md HW04/A_FR01/selection.md
python $S/check_data.py HW04/data/A_FR01.json
python $S/freeze.py --feature A_FR01 --step 1 --out HW04/appendix/ai-outputs HW04/A_FR01/selection.json HW04/data/A_FR01.json HW04/A_FR01/selection.md
python $S/merge_reports.py HW04/data/A_FR01.json HW04/A_FR01 HW04/reports/chrome_<ts> HW04/reports/edge_<ts> HW04/reports/firefox_<ts>
```

Cấu hình Playwright cần: project `chrome`/`edge`/`firefox`, `workers: 1`, `retries: 0`, HTML reporter (title + metadata `Run by: <MSSV> · <ISO>`) và JSON reporter `results.json` cùng thư mục report (cho `merge_reports.py`).

## Tài nguyên

- `scripts/select_tc.py` — liệt kê ứng viên; xuất data JSON + selection.md
- `scripts/check_data.py` — đủ trường, ≥ 12 TC, sha1, expected trùng nguyên văn nguồn HW02
- `scripts/freeze.py` — đóng băng output AI theo `<X_FRnn>/step<k>/`, không ghi đè
- `scripts/merge_reports.py` — gộp 3 report → results.md + bug_groups.md
- `assets/ddt-fixture.template.ts`, `assets/spec.template.ts`, `assets/selection.example.json`
