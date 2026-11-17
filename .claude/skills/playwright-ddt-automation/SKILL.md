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
4. **Đóng băng output AI** bằng `freeze.py` TRƯỚC khi người dùng sửa; không bao giờ sửa file đã đóng băng. Bản đóng băng **không được bị Playwright nạp**: `--out` phải nằm ngoài testDir (`--testdir`, mặc định `HW04/tests`; script từ chối nếu nằm trong), file mã đổi đuôi `*.ts.txt` (v2.1). Bản đóng băng v1 đã có (`HW04/appendix/ai-outputs/`, đuôi `.ts`) nằm ngoài testDir nên giữ nguyên.
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
- Từ `assets/ddt-fixture.template.ts` (v2): `loadData` (đọc data + kiểm sha1), `assumption()` (giả định SV ngoài expected; thiếu → ném lỗi), `resetDb` + `guardWorkers` (dừng nếu workers > 1), `blocked()`, `step()` (**chỉ** `TimeoutError` → Blocked, lỗi khác ném tiếp), `until()` (chờ điều kiện cụ thể có hạn), `settle()`, `netLog()`, `esc()`, fixture `api` có token admin + `dialogs` (ghi hộp thoại); page object của form/màn hình feature với selector lấy từ **mã UI thật** (nhãn, role, placeholder) — không bịa.
- Không chứa dữ liệu test. `freeze.py --step 2` → commit → dừng.

### 3 — Sinh spec (AI)
- Từ `assets/spec.template.ts` (v2, cấu trúc theo `C_FR15.spec.ts` @2e9e454): `for (const c of DATA.testcases)`, tiêu đề `"<tc_id> <title>"`, giá trị từ `c.inputs` (thay `{ts}`), oracle parse từ `c.expected` — **không đọc được loại kết quả → ném lỗi**; ý không tự động được → annotation `oracle không tự động`.
- Câu chữ/từ khoá/selector **không có trong expected** (vd từ khoá "giỏ trống", khối thông báo trên trang) → trường `assumptions` của file data (giả định, SV duyệt ở bước 1/3; không tính sha1), không gõ cứng trong spec.
- Thứ tự mỗi TC: API TRƯỚC → thao tác **đúng số lần procedure ghi** (gắn `netLog` trước khi bấm) → `until` **một trong các nhánh phản hồi** (request / URL đổi / thông báo hiện / hộp thoại; form hợp lệ HTML5 vẫn có thể không gửi request vì ứng dụng tự kiểm phía client) → nếu có request thì `await done` → `settle` → ghi quan sát → ảnh `<TC>_after-*` (chụp SAU khi đo xong) → API SAU → oracle.
- ≥ 3 kiểu assertion: **trạng thái UI** (`toBeVisible`/`toHaveURL`), **nội dung thông báo** (`toHaveText`/`toContainText`), **oracle dữ liệu qua API trước/sau** (`toEqual`), **đếm/giá trị** (`toHaveCount`/`toHaveValue`); dùng `expect.soft`.
- Điều kiện chặn đã biết (trường đặc tả có mà UI không có…) → `blocked('<lý do + case gốc>')`, không Fail giả.
- Cấm (lỗi đã gặp ở review A/B/C): `test.describe.configure({ mode: 'serial' })` (1 Fail chặn mọi TC sau); `catch {}` rỗng; `waitForTimeout`/chờ cứng; `Promise.race` nuốt lỗi; gọi API đọc dữ liệu trước khi request của thao tác có phản hồi; `new RegExp(chuỗi chưa esc)`; `^a|b` (chỉ neo nhánh đầu → viết `^(?:a|b)`); đếm hộp thoại bất kỳ (có thể là "thành công") là "thông báo lỗi" khi chưa có giả định SV phân loại → ghi annotation `oracle thông báo yếu`.
- `freeze.py --step 3` → commit → dừng.

### 4 — List + typecheck (AI chạy, SV chạy 3 trình duyệt)
- Claude Code **chỉ** chạy: `npx playwright test <X_FRnn> --list --reporter=list` (tránh sinh report rỗng) và `npx tsc --noEmit`. Báo số test = số TC trong data.
- SV chạy `npm run test:chrome`, `test:edge`, `test:firefox` trên máy mình → 3 report có "Run by" + ISO timestamp. AI không chạy lượt chính thức, không sửa report.
- Config: `trace: 'off'` (trace làm report vài chục MB, zip > 20 MB; với off ~1 MB/report), `screenshot: 'only-on-failure'`, `workers: 1`, `retries: 0`.
- Lỗi hạ tầng: worker crash (vd Windows `0xC0000409`, test dừng ở 0 ms, không assertion nào chạy) hoặc trình duyệt không khởi động (`spawn UNKNOWN`, chặn bởi chính sách hệ thống) → **chạy lại** TC/lượt, ghi "lỗi hạ tầng" trong RUN.md, không tính Fail, không lập bug. Lượt hỏng không dùng làm chính thức.

### 5 — SV review và sửa
- SV đọc spec, so với bản đóng băng step3, sửa. **Mỗi lần sửa một commit riêng có sửa `.spec.ts`**: `HW04[X-FRnn] 5/6x – sửa: <tóm tắt>` (x = a, b, c…).
- AI không gợi ý edge case/assertion còn thiếu trong lúc SV review. Chỉ khi SV hỏi "vì sao AI bỏ sót" sau khi đã commit phần của SV mới trả lời — trung thực, tách *đã nghĩ tới nhưng không đưa vào* với *không nghĩ tới*.
- Trước khi review, SV có thể dùng mục **Checklist review bước 5** bên dưới (lỗi đã gặp ở A/B/C).

### 6 — Gộp kết quả (AI gộp, SV viết bug)
- `merge_reports.py <data> <feature-dir> <report chrome> <report edge> <report firefox>` → `results.md` (Pass/Fail/Blocked theo trình duyệt, cột HW02) + `bug_groups.md` (TC Fail gom theo lỗi đầu tiên, chỉ dữ kiện).
- SV cô lập nguyên nhân, viết bug + GitHub Issue (ảnh). AI chỉ kiểm trường thiếu, chạy `gh issue create --body-file` với file SV viết.

## Chế độ demo (v2.1) – quay video / chạy thử skill

Chạy trọn 6 bước trên **một feature, ít TC** (vd 4: 2 Fail + 2 Pass theo HW02) mà không chạm `HW04/data`, spec, report hay `appendix/ai-outputs` chính thức.

- Dựng: `python $S/demo.py --feature <X_FRnn> [--dir HW04/tests/_demo] [--min 4]` → in đủ lệnh từng bước.
- Bố cục `<dir>` (phải nằm dưới `HW04/tests` để Node thấy `node_modules`): `playwright.config.ts` (testDir `./tests`, testMatch `*.demo.ts`, testIgnore `**/ai-outputs/**`, report → `<dir>/reports/<project>_<ts>/`, metadata "Chế độ: demo"), `tests/fixtures/ddt.ts` (đọc data qua `DDT_DATA_DIR` = `<dir>/data`), `tests/<X_FRnn>.demo.ts`, `data/`, `<X_FRnn>/` (selection, results, bug_groups), `ai-outputs/` (ngoài testDir demo, đuôi `.txt`).
- Spec demo đuôi **`.demo.ts`** (không phải `.spec.ts`) để config chính thức (testDir `HW04/tests`, testMatch `*.spec.ts`) không nạp nhầm; chạy demo luôn kèm `--config ./_demo/playwright.config.ts` (từ `HW04/tests`).
- Đường dẫn: fixture tìm gốc repo bằng cách đi lên tới `tools/restart_backend.ps1` (không phụ thuộc độ sâu); page object chính thức import từ spec demo bằng `../../pages/<file>`; globalSetup dùng `HW04/tests/global-setup.ts`.
- Script chạy từ **gốc repo** (`select_tc.py`/`check_data.py` gọi `git show` theo đường dẫn tương đối).
- Điểm dừng giữ nguyên: sau bước 1 (SV duyệt TC), bước 4 (SV tự chạy 3 trình duyệt), bước 5 (SV review). Không commit gì của demo; xong thì xoá `<dir>`.

## Checklist review bước 5 (lỗi spec AI đã gặp ở HW04 A/B/C)

Danh sách lỗi đã thấy trong bản AI ở `HW04/<X_FRnn>/review_sv.md` — SV soi từng dòng; danh sách này không thay việc SV tự đọc spec.

- [ ] Không có `mode: 'serial'`; `beforeAll` dừng khi `workers > 1` (resetDb).
- [ ] Không `catch` rỗng; chỉ `TimeoutError` → Blocked; lỗi khác ném tiếp.
- [ ] Không `waitForTimeout`/chờ cứng; không `Promise.race` nuốt lỗi; chờ phản hồi mạng hoặc điều kiện cụ thể.
- [ ] API đọc dữ liệu "sau" chỉ gọi khi request của thao tác đã có phản hồi (hoặc đã xác nhận không có request).
- [ ] Chuỗi dựng `RegExp` đã escape; nhiều nhánh nhóm đúng `^(?:a|b)`.
- [ ] Expected không đọc được → ném lỗi; oracle yếu/không tự động → annotation (không im lặng Pass).
- [ ] Câu chữ/từ khoá/selector không có trong expected nằm ở `assumptions` của file data, không gõ cứng.
- [ ] Hộp thoại "thành công" không bị đếm là "thông báo lỗi" khi chưa có giả định SV.
- [ ] Bấm đúng số lần procedure ghi; không có bước phụ sinh sự kiện trùng (vd `checkValidity()` bắn `invalid`).
- [ ] Ảnh `<TC>_after-*` chụp sau khi đo xong, không chụp song song lúc đang chờ.
- [ ] Selector bám mã UI thật, không `.first()` chung chung bắt nhầm phần tử.
- [ ] Config: `trace: 'off'`, `retries: 0`, `workers: 1`.

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
- `scripts/freeze.py` — đóng băng output AI theo `<X_FRnn>/step<k>/`, không ghi đè; từ chối `--out` trong testDir; file mã → `*.ts.txt`
- `scripts/demo.py` — dựng chế độ demo (config/fixture/spec `.demo.ts`/data/reports riêng trong `<dir>`)
- `scripts/merge_reports.py` — gộp 3 report → results.md + bug_groups.md
- `assets/ddt-fixture.template.ts`, `assets/spec.template.ts`, `assets/selection.example.json`
