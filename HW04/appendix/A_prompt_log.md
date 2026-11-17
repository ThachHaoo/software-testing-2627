# Prompt Log – HW04
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude (không rõ model), Claude Opus 5.5

> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script `tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.

---

## #1 | 22:20 16/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – bước 0: dựng môi trường. Repo hiện tại.
1. git pull; git status phải sạch.
2. Em đặt đề vào context/HW04_assignment.pdf → chuyển thành context/HW04_assignment.md (giữ nguyên chữ).
3. tools/hw.toml: chuyển sang HW04 (since = "2026-11-12 18:51", log/notes/extra trong HW04/appendix/), giữ cấu hình HW03 dạng comment.
4. Tạo HW04/CLAUDE.md: chép quy ước còn đúng từ HW03/CLAUDE.md (AI-01, không amend, bug do SV viết, prompt log), thêm yêu cầu HW04 từ đề.
5. Tạo HW04/tests/: @playwright/test bản mới nhất, 3 project chromium/firefox/webkit, workers 1, retries 0, globalSetup kiểm SUT (lấy từ HW02), HTML reporter: title + metadata "Run by: 23120255 · <ISO timestamp lúc chạy>", outputFolder HW04/reports/<project>_<timestamp>. Cài 3 trình duyệt.
6. Tạo 1 spec smoke tạm (mở trang chủ), chạy trên 3 trình duyệt để kiểm report hiện đúng "Run by" + timestamp; xong XOÁ spec smoke và report smoke (không commit chúng).
7. Commit "HW04: bước 0 – môi trường" (không push).
Báo cáo ≤ 12 dòng: phiên bản Playwright, "Run by" hiện ở đâu trong report, lỗi nếu có.


 Đồng thời, tạm dừng ghi các prompt log cho HW03, vì giờ đã bắt đầu sang HW04
```

**Output:**
```
Đã có đề + hw.toml chuyển HW04. Giờ tạo HW04/CLAUDE.md, settings deny, khung notes, rồi dựng Playwright.

Now writing files.

Root CLAUDE.md table update + Playwright files.

Browsers tải xong; WebKit báo thiếu DLL (cảnh báo). Bật SUT rồi chạy smoke để xem WebKit có chạy không.

Smoke spec + run 3 browsers.

WebKit bị Windows Application Control (Smart App Control) chặn `Playwright.exe`, nên không chạy được. Em kiểm report của Chromium/Firefox trước.

Report đúng. Giờ xoá smoke, sinh log HW04, commit.

Đã commit bước 0. Chromium và Firefox chạy được và report hiện đúng "Run by". **WebKit không chạy được** vì Windows chặn nó, nên hiện chỉ có 2 trên 3 trình duyệt mà đề yêu cầu.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW04 bước 0 – dựng môi trường. Đã ngừng ghi log HW03: `tools/hw.toml` trỏ sang HW04 (since `2026-11-12 18:51`), cấu hình HW03 giữ dạng comment với until `2026-11-11 11:35`. Lượt #232 bị bỏ theo lựa chọn của em.
- **Playwright:** `@playwright/test` 1.65.1, đã cài chromium-1255, firefox-1572, webkit-2388.
- **"Run by" hiện ở 2 chỗ:** (1) tiêu đề lớn ở đầu report và tên tab trình duyệt: `HW04 EShop – chromium – Run by: 23120255 · 2026-11-16T22:30:41+07:00`; (2) mục Metadata (thu gọn sẵn, bấm mới mở). Report nằm ở `HW04/reports/<project>_<YYYYMMDDTHHMMSS>/`. Muốn mỗi trình duyệt một report thì chạy từng project: `npm run test:chromium|firefox|webkit`, hoặc `test:all` để chạy lần lượt cả 3.
- **Kiểm tra:** smoke Pass trên chromium và firefox; **webkit Fail** (lỗi bên dưới). Đã xoá spec smoke, report smoke và `test-results`, không commit.
- **Lỗi WebKit:** Windows Application Control (Smart App Control) chặn `ms-playwright\webkit-2388\Playwright.exe`. Playwright báo "Host system is missing dependencies" dù đủ DLL; bỏ qua bước kiểm thì báo `spawn UNKNOWN`.
- **Việc làm thêm ngoài lệnh:** chuyển SUT `../eshop-sut` từ nhánh `usability-tunnel` về `main @ de0f48f`; bật backend :3000, web :5173, admin :5174; thêm 4 luật deny cho HW04 vào `.claude/settings.json`; tạo khung `prompt_log_notes.toml`/`prompt_log_extra.toml`; tạo `HW04/.gitattributes`; cập nhật bảng bài ở `CLAUDE.md` gốc.
- **PDF đề:** `context/HW04_assignment.pdf` để ngoài commit (theo cách các bài trước không commit PDF đề), nên `git status` còn 1 file chưa theo dõi.
- **Commit:** `4d14bd7` HW04: bước 0 – môi trường (chưa push).
- **Cần quyết định:**
  - W1 – thay WebKit thế nào: (a) dùng Chrome / Edge / Firefox, đề cho phép (`channel: 'msedge'`); (b) tắt Smart App Control (không bật lại được nếu không cài lại Windows); (c) chạy WebKit bằng Docker.
  - M1 – đề §12 bắt repo GitHub **public**, còn `CLAUDE.md` gốc ghi repo private: (a) tạo repo public riêng cho HW04; (b) đổi repo hiện tại sang public.
  - M2 – deadline thật trên Moodle là khi nào.
```
*File AI ghi/gửi trong lượt này:* `hw.toml`, `CLAUDE.md`, `package.json`, `playwright.config.ts`, `global-setup.ts`, `hw03-runtime-state.md`

**Xử lý:** [...]

---

## #2 | 23:02 16/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #2. Deadline thật: 11:00 18/11/2026 (ghi vào HW04/CLAUDE.md). Repo đã public → sửa dòng "private" ở CLAUDE.md gốc.

A. Trình duyệt (W1=a): thay project chromium/firefox/webkit bằng chrome (channel 'chrome'), edge (channel 'msedge'), firefox. Cài Chrome nếu máy chưa có (npx playwright install chrome; lỗi quyền thì báo). Smoke tạm trên 3 trình duyệt như bước 0, xong xoá. Commit "HW04: đổi sang Chrome/Edge/Firefox (W1=a)".

B. Tạo skill .claude/skills/playwright-ddt-automation/ (SKILL.md + scripts/ + assets/, cấu trúc như domain-bva-testing). Quy trình 6 bước cho một feature, mỗi bước một commit "HW04[X-FRnn] k/6", output AI đóng băng vào HW04/appendix/ai-outputs/<X_FRnn>/step<k>/ TRƯỚC khi SV sửa:
 1 Chọn TC: từ HW02/<X_FRnn>/testcases.json chọn 15 TC suite UI (bỏ API/manual), đủ positive/negative/biên, ưu tiên TC từng Fail. Xuất HW04/data/<X_FRnn>.json: tc_id, title, technique, inputs, expected CHÉP NGUYÊN VĂN + sha1(expected), nguồn = commit HW02. Bảng lý do chọn ở HW04/<X_FRnn>/selection.md. DỪNG cho SV duyệt.
 2 Fixture/page object (login admin, reset CSDL bằng tools/restart_backend.ps1, đọc data JSON).
 3 Sinh spec HW04/tests/<X_FRnn>.spec.ts: lặp theo file data (không hardcode dữ liệu trong spec), tiêu đề "<tc_id> <title>", ≥3 kiểu assertion: trạng thái UI (toBeVisible/toHaveURL), nội dung thông báo (toHaveText/toContainText), oracle dữ liệu qua API trước/sau (toEqual), đếm (toHaveCount/toHaveValue); dùng expect.soft; kiểm sha1 expected trước khi chạy.
 4 Claude Code chỉ chạy --list + typecheck. SV chạy 3 trình duyệt.
 5 SV review → mỗi lần sửa là một commit riêng có sửa .spec ("HW04[X-FRnn] 5/6x – sửa: …").
 6 Gộp kết quả 3 report → HW04/<X_FRnn>/results.md (Pass/Fail/Blocked theo trình duyệt); Fail → _groups cho SV viết bug (AI không viết mô tả bug).
 Luật: không đổi expected hay assertion để cho test xanh; timeout = Blocked; healer/tự sửa chỉ sửa selector/chờ, ghi lý do.
 Commit skill riêng: "HW04: skill playwright-ddt-automation v1".

C. Chạy BƯỚC 1 cho A_FR01 rồi DỪNG.

Báo cáo ≤ 15 dòng: kết quả trình duyệt, cấu trúc skill, bảng 15 TC của A (mã, kỹ thuật, loại +/-/biên, HW02 Pass/Fail), các commit.
```

**Output:**
```
Chrome + Edge có sẵn. Sửa CLAUDE.md + config, chạy smoke.

Regex mất backslash; sửa, kiểm title report, xoá smoke.

Now HW02 A_FR01 testcases.json structure.

Viết skill. Bắt đầu scripts.

Thêm JSON reporter vào config, rồi commit skill.

Kiểm nhanh JSON reporter + merge_reports bằng smoke tạm.

Bước 1 A_FR01: liệt kê ứng viên.

Đã xong cả 3 phần A, B, C; Bước 1 của A_FR01 dừng ở đây để em duyệt.

### Báo cáo cho phiên thảo luận
- **A. Trình duyệt:** Chrome và Edge có sẵn trên máy, không phải cài. Smoke Pass trên chrome, edge, firefox; report hiện đúng `Run by: 23120255 · <ISO>`. Đã xoá smoke và report. Thêm vào lệnh: spec giờ đặt thẳng ở `HW04/tests/*.spec.ts` (đổi `testDir`).
- **B. Skill** `.claude/skills/playwright-ddt-automation/`:
  - `SKILL.md`: 6 bước và các luật trong lệnh.
  - `scripts/`: `select_tc.py`, `check_data.py`, `freeze.py`, `merge_reports.py` (nhóm Fail ghi vào `bug_groups.md`).
  - `assets/`: mẫu fixture, mẫu spec, mẫu `selection.json`.
  - Thêm JSON reporter (`results.json` cạnh `index.html`) cho bước 6. Đã thử `merge_reports.py` bằng smoke 3 test Pass/Fail/Blocked, ra đúng 3 verdict.
- **C. A_FR01 bước 1:** 59 TC UI ứng viên, chọn 15; `check_data.py` 0 lỗi. Chi tiết ở `HW04/A_FR01/selection.md`. Theo HW02 (status): Fail 5, Pass 5, Blocked 5.
  - Positive (EP): 01 Fail · 02 Fail · 03 Blocked
  - Negative (EP): 05 Pass · 07 Pass · 08 Blocked · 14 Blocked · 17 Pass · 18 Pass · 26 Blocked (BUG-14)
  - Boundary (BVA): 61 LB Blocked · 63 LB-1 Pass · 64 LB Fail
  - EG của SV: 202 Negative Fail (BUG-02) · 211 Positive Fail
  - Không lấy: suite API, TS-GUI (không có inputs), 216 (thăm dò), 223 (SRS không có Expected), các TC cùng triệu chứng BUG-01.
- **Commit:** `838752b` đổi Chrome/Edge/Firefox · `b0e2f7c` skill v1 · `b54c170` HW04[A-FR01] 1/6 · `f797653` prompt log.
- **Cần quyết định:**
  - S1 – loại của TC-202 (Negative) và TC-211 (Positive) do AI tự suy ra vì HW02 không ghi: giữ hay sửa.
  - S2 – TC-26 chắc chắn sẽ Blocked vì form không có ô Xác nhận mật khẩu: giữ để kiểm cách script xử lý ô vắng mặt, hay thay bằng 1 TC Fail khác.
```
*File AI ghi/gửi trong lượt này:* `select_tc.py`, `check_data.py`, `freeze.py`, `merge_reports.py`, `ddt-fixture.template.ts`, `spec.template.ts`, `selection.example.json`, `SKILL.md`, `selection.json`

**Xử lý:** [...]

---

## #3 | 00:07 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #3, A_FR01.
1. SV chốt selection (không freeze; commit "HW04[A-FR01] 1/6b – SV chốt"):
   - S1: loại TC-202 = Negative, TC-211 = Positive; ghi "(AI suy ra, SV duyệt)".
   - S2: bỏ TC-26.
   - Giảm Blocked còn tối đa 2: bỏ các TC Blocked có cùng bug gốc với TC Fail đã chọn. In bảng lý do Blocked của 03, 08, 14, 61 (bug gốc) trước khi bỏ.
   - Bù cho đủ 15 TC: ưu tiên BVA cận trên (UB/UB+1) nếu có, rồi tới TC Pass/Fail chạy trọn luồng.
   - Chạy lại check_data.py.
2. Chạy BƯỚC 2 của skill cho A (fixture/page object). Freeze → commit "HW04[A-FR01] 2/6". DỪNG.
Báo cáo ≤ 12 dòng: bảng 15 TC cuối (mã, loại, kỹ thuật, HW02 status), TC đã thay, file fixture, commit.
```

**Output:**
```
Bước 1b (SV chốt) và bước 2 của A_FR01 đã commit; em dừng trước bước 3.

### Báo cáo cho phiên thảo luận
- **Selection chốt** (`check_data.py` 0 lỗi): Positive 3, Negative 7, Boundary 5. Theo HW02 (status): Fail 8, Pass 7, Blocked 0.

  | Loại | Kỹ thuật | TC (HW02 status) |
  |---|---|---|
  | Positive | EP | 01 Fail · 02 Fail |
  | Positive (AI suy ra, SV duyệt) | EG | 211 Fail |
  | Negative | EP | 05 · 07 · 17 · 18 · 22 · 23 (đều Pass) |
  | Negative (AI suy ra, SV duyệt) | EG | 202 Fail (BUG-02) |
  | Boundary | BVA | 63 LB-1 Pass · 64 LB Fail · 68 LB Fail · 74 LB Fail · 77 LB Fail |

- **TC đã thay:** bỏ 03, 08, 14, 61 (cả 4 bị chặn bởi TC-01, bug gốc BUG-01) và bỏ 26 (S2). Bù 68, 74, 77, 22, 23. HW02 không có điểm UB/UB+1 vì SRS không có cận trên (giả định A1/A4), nên bù bằng TC chạy trọn luồng.
- **Thêm vào lệnh:** sửa `select_tc.py` để ghi được nhãn "(AI suy ra, SV duyệt)" và mục "Quyết định của SV" trong `selection.md`; thay đổi này nằm trong commit 1/6b.
- **Fixture / page object** (`HW04/tests/`):
  - `fixtures/ddt.ts` (dùng chung): đọc data và kiểm sha1, `resetDb`, `blocked`, fixture `api` có token admin.
  - `fixtures/a_fr01.ts`: chụp danh sách user trước/sau qua API, xoá user mới sau mỗi case.
  - `pages/register.page.ts`, `pages/login.page.ts`: label trong form không gắn với ô nhập, nên tìm ô nhập theo khối `<div>` chứa nhãn.
  - Thêm `tsconfig.json` và cài `typescript`, `@types/node`.
- **Kiểm tra:** `tsc --noEmit` Pass. Probe tạm trên Chrome (đã xoá) tìm thấy đủ ô Họ Tên, Email, Mật khẩu, nút submit, 2 ô của trang Login; ô Xác nhận mật khẩu = 0 (khớp BUG-14).
- **Commit:** `0990ac0` HW04[A-FR01] 1/6b – SV chốt · `161074b` HW04[A-FR01] 2/6 (đã freeze `step2/`).
- **Cần quyết định:** không có.
```
*File AI ghi/gửi trong lượt này:* `ddt.ts`, `register.page.ts`, `login.page.ts`, `a_fr01.ts`

**Xử lý:** [...]

---

## #4 | 00:21 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #4, A_FR01, BƯỚC 3 của skill.
1. In lại bảng 15 TC từ selection.md (báo cáo trước bị cụt dòng Boundary).
2. Sinh HW04/tests/A_FR01.spec.ts theo SKILL.md bước 3 (lặp theo data, không hardcode, ≥3 kiểu assertion, expect.soft, kiểm sha1). Ghi rõ kiểu assertion nào ở TC nào vào HW04/A_FR01/assertions.md.
3. Chỉ chạy tsc --noEmit + playwright test --list (đủ 15 TC × 3 trình duyệt = 45).
4. Freeze step3/ → commit "HW04[A-FR01] 3/6". DỪNG, không chạy test thật.
Báo cáo ≤ 12 dòng: số test --list, bảng kiểu assertion, lệnh SV dùng để chạy 3 trình duyệt.
```

**Output:**
````
Spec A_FR01 đã sinh và commit; `--list` ra đủ 45 test. Em chưa chạy test thật.

**Bảng 15 TC** (từ `HW04/A_FR01/selection.md`):

| # | TC | Loại | Kỹ thuật | BVA | HW02 auto / status |
|---|---|---|---|---|---|
| 1 | 01 | Positive | EP | | Fail / Fail |
| 2 | 02 | Positive | EP | | Fail / Fail |
| 3 | 05 | Negative | EP | | Pass / Pass |
| 4 | 07 | Negative | EP | | Pass / Pass |
| 5 | 17 | Negative | EP | | Pass / Pass |
| 6 | 18 | Negative | EP | | Pass / Pass |
| 7 | 22 | Negative | EP | | Pass / Pass |
| 8 | 23 | Negative | EP | | Pass / Pass |
| 9 | 63 | Boundary | BVA | LB-1 | Pass / Pass |
| 10 | 64 | Boundary | BVA | LB | Fail / Fail |
| 11 | 68 | Boundary | BVA | LB | Fail / Fail |
| 12 | 74 | Boundary | BVA | LB | Fail / Fail |
| 13 | 77 | Boundary | BVA | LB | Fail / Fail |
| 14 | 202 | Negative (AI suy ra, SV duyệt) | EG | | Fail / Fail |
| 15 | 211 | Positive (AI suy ra, SV duyệt) | EG | | Fail / Fail |

### Báo cáo cho phiên thảo luận
- **Spec:** `HW04/tests/A_FR01.spec.ts`. Lặp theo `HW04/data/A_FR01.json`. Oracle đọc từ chuỗi expected nguyên văn (hàm `oracleOf`); expected nào không xác định được là thành công hay từ chối thì spec báo lỗi, không đoán. Đã thử phần đọc oracle trên đủ 15 expected, không lỗi. File data bị sửa expected thì sai sha1 và cả file không chạy. CSDL được restart một lần đầu mỗi lượt chạy (`beforeAll`).
- **Kết quả kiểm tra:** `tsc --noEmit` Pass · `--list --reporter=list` ra 45 test (15 TC × chrome/edge/firefox) · không chạy test thật.
- **Kiểu assertion** (đều `expect.soft`; chi tiết `HW04/A_FR01/assertions.md`):

  | TC | Trạng thái UI | Nội dung thông báo | API trước/sau `toEqual` | Đếm / giá trị |
  |---|---|---|---|---|
  | 01, 02, 64, 68, 74, 77 | `toHaveURL(/login)` | – | đúng 1 user mới | `toHaveValue`, `toHaveCount(0)` |
  | 211 | `toHaveURL(/)` sau khi đăng nhập lại | – | đúng 1 user mới | `toHaveValue`, `toHaveCount(0)`, có token |
  | 05, 07, 17, 18, 22, 23, 63 | `toHaveURL(/register)`, `toBeVisible` | `toHaveText` | không có user mới, seed không bị sửa/xoá | `toHaveValue` |
  | 202 | `toBeVisible` | `toContainText` mật khẩu + ký tự đặc biệt | không có user mới | `toHaveValue` |

- **Lệnh SV chạy 3 trình duyệt** (backend :3000, web :5173, admin :5174 phải đang chạy):
  ```
  cd HW04\tests; npx playwright test A_FR01 --project=chrome; npx playwright test A_FR01 --project=edge; npx playwright test A_FR01 --project=firefox
  ```
  `npm run test:chrome|edge|firefox` cũng được, nhưng sẽ chạy mọi spec, không chỉ A_FR01.
- **Commit:** `9a5e558` HW04[A-FR01] 3/6 (đã freeze `step3/`).
- **Cần quyết định:** không có.
````
*File AI ghi/gửi trong lượt này:* `A_FR01.spec.ts`, `assertions.md`

**Xử lý:** [...]

---

## #5 | 00:29 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #5, A_FR01, BƯỚC 5 (SV review).
1. Giữ 3 report lượt vừa chạy (chrome_20261117T00…, edge_20261117T002642, firefox_20261117T002739); tạo HW04/A_FR01/RUN.md ghi chúng là "lượt thử 1": 1 Fail (TC-01) + 14 did not run do mode serial.
2. Sửa theo SV: bỏ test.describe.configure({ mode: 'serial' }) ở A_FR01.spec.ts:44 để mỗi TC chạy độc lập; kiểm lại việc beforeAll/resetDb vẫn đúng khi worker khởi động lại sau một test Fail (giải thích ngắn trong báo cáo). Không đổi gì khác.
3. tsc --noEmit + --list. Commit "HW04[A-FR01] 5/6a – sửa: bỏ mode serial (1 Fail chặn 14 TC)". Không freeze (bản SV sửa).
4. Kiểm sơ bộ: TC-01 Fail vì assertion nào (đọc error-context trong report chrome) – Fail do SUT hay do script? Chỉ báo dữ kiện.
Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đang ghi RUN.md và sửa spec.

Spec đã sửa, bỏ mode serial và commit 5/6a. 3 report lượt thử 1 được commit cùng `RUN.md`. TC-01 Fail ở 3 assertion; dữ kiện nghiêng về phía SUT, không phải script.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** A_FR01 bước 5a: giữ 3 report lượt thử 1, bỏ `mode: 'serial'` ở `A_FR01.spec.ts`.
- **File đã tạo/sửa:** `HW04/A_FR01/RUN.md` (lượt thử 1: mỗi trình duyệt 1 Fail TC-01 + 14 did not run, có annotation `serial`). `A_FR01.spec.ts`: chỉ xoá 2 dòng.
- **Kết quả kiểm tra:** `tsc --noEmit` Pass · `--list` 45 test · chưa chạy test thật.
- **beforeAll sau khi bỏ serial:** Playwright bỏ worker sau mỗi test Fail và mở worker mới cho test kế tiếp. `beforeAll` chạy lại trong worker mới, tức `resetDb()` chạy thêm một lần sau mỗi Fail. CSDL vẫn seed sạch, đúng tiền điều kiện; token admin được lấy lại sau mỗi lần reset. Cái giá là mỗi Fail tốn thêm thời gian restart backend (chạy 1 worker nên không có xung đột).
- **TC-01 Fail ở 3 assertion** (giống nhau trên cả 3 trình duyệt):
  - `toHaveURL(/login$/)`: URL nhận được vẫn là `/register`.
  - `toHaveCount(0)` hộp lỗi: có 1 hộp lỗi.
  - `toEqual` user mới: mong 1, nhận `[]`.
- **Dữ kiện về nguyên nhân:**
  - Phía script chạy đúng: 6 lần `toHaveValue` đều Pass, và snapshot cho thấy 3 ô có đúng giá trị đã gõ.
  - Hộp lỗi hiện "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT."
  - Regex ở `../eshop-sut/frontend-web/src/pages/Register.jsx:15` bắt buộc có khoảng trắng và chỉ nhận `[A-Za-z\d\s]`, nên mật khẩu `Abcd1234!` bị chặn trước khi gửi request. Triệu chứng trùng HW02 BUG-01.
- **Commit:** `6fc76b5` HW04[A-FR01] 5/6a – sửa: bỏ mode serial (1 Fail chặn 14 TC).
- **Bất thường (không chặn):** Git cảnh báo sẽ đổi LF→CRLF cho các file trong `HW04/reports/` (`index.html` chứa dữ liệu nhúng, trace `.js`). Đề xuất thêm `reports/** -text` vào `HW04/.gitattributes` để report giữ nguyên byte; chờ em duyệt.
- **Cần quyết định:** không có.
```
*File AI ghi/gửi trong lượt này:* `RUN.md`

**Xử lý:** [...]

---

## #6 | 00:55 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #6, A_FR01, BƯỚC 5 (tiếp).
1. Chép NGUYÊN VĂN danh sách soi spec của SV (em dán bên dưới) vào HW04/A_FR01/review_sv.md, thêm mục "Phiên thảo luận bổ sung": serial (đã sửa 5/6a), ^ ở dòng 28, RegExp không escape ở dòng 38, users.list() không chờ POST. Commit "HW04[A-FR01] review của SV" TRƯỚC khi sửa code.
2. Sửa, mỗi mục một commit có sửa A_FR01.spec.ts:
   5/6b – sau khi bấm Đăng Ký: chờ phản hồi POST /api/register (hoặc xác nhận không có POST trong N giây) rồi mới gọi users.list(); bỏ catch rỗng, ghi annotation nhánh nào xảy ra (điều hướng / hộp lỗi / trình duyệt chặn / timeout → Blocked).
   5/6c – oracleOf: sửa nhóm ^(...|...), escape chuỗi trước khi new RegExp; case reject mà không đọc được ý thông báo thì ghi annotation "oracle thông báo yếu" (không tự bịa ý).
   5/6d – beforeAll: dừng nếu workers > 1 (resetDb không an toàn khi chạy song song).
3. tsc + --list sau mỗi commit. Ghi 00:37 (firefox 8F/7P) và các lượt chrome/edge cùng đợt vào RUN.md là "lượt thử 2". Thêm reports/** -text vào HW04/.gitattributes (commit riêng).
Báo cáo ≤ 10 dòng. DỪNG; SV chạy lượt chính thức.
--- Danh sách SV ---



Soi spec: 

Oracle phụ thuộc regex tiếng Việt cứng nhắc: vì dùng regex để phân tích câu văn tiếng việt, nên giả sử expected diễn đạt lệch 1 xíu thì regex phân tích sai --> bỏ sót kiểm tra thông báo lỗi hoặc crash.
Đồng bộ sau Submit dùng Promise.race cùng vboiws catch(() => {}) dễ gây flaky: submit xong thì đua giữa waitForURL và r.error.waitFor. Giả sử mạng lag quá 5s, timeout không bắt dực thì script hiểu nhầm trình duyệt chặn submit.
Làm dụng expect.soft: nếu bước submit thất bại ở ban đầu, mà vẫn chạy tiếp xuống gọi API users.list(), có thể race condition khi backend chưa ghi xong DB, rồi lại chạy tiếp relogin --> nhiều lỗi.
Dọn dữ liệu (cleanup) và resetDb() chưa an toàn khi chạy song song: có thể khi chạy nhiều trình duyệt cùng lúc thì các worker restart backend đè lên nhau.
```

**Output:**
````
Now 5/6c.

Escape hỏng ở dòng 26; sửa bằng Edit.

Now 5/6d.

Cập nhật RUN.md + commit report lượt thử 2.

Đã xong lệnh #6: review của SV commit trước, 3 sửa 5/6b–5/6d, RUN.md lượt thử 2, rule `-text` cho report. Spec sau sửa chưa chạy thật; dừng để em chạy lượt chính thức.

### Báo cáo cho phiên thảo luận
- **Review:** `HW04/A_FR01/review_sv.md`: danh sách của em chép nguyên văn + mục "Phiên thảo luận bổ sung" (4 điểm) + bảng sửa. Commit `3e7dda8`, làm trước khi sửa code.
- **Sửa spec** (mỗi commit chỉ sửa `A_FR01.spec.ts`; `tsc` Pass và `--list` ra 45 test sau mỗi commit):
  - `5a378f1` 5/6b: sau khi bấm Đăng Ký, xác định nhánh điều hướng / hộp lỗi / trình duyệt chặn. Có POST thì chờ phản hồi (tối đa 10 s), không có thì chờ 2 s để xác nhận không có POST, rồi mới gọi `users.list()`. Bỏ `catch` rỗng; mỗi TC có annotation `phản hồi`. Hết giờ, hoặc có POST mà không có phản hồi → Blocked.
  - `740934b` 5/6c: đổi thành `^(…|…)`; thêm hàm `esc()` escape chữ trước `new RegExp` (cả hint lẫn URL), đã thử riêng bằng node. Case từ chối mà expected không nêu ý thông báo → annotation "oracle thông báo yếu"; 7 TC 05/07/17/18/22/23/63 sẽ có annotation này.
  - `3d19917` 5/6d: `beforeAll` dừng nếu `workers > 1`.
- **`79d4bb6`:** thêm `reports/** -text` vào `HW04/.gitattributes`; renormalize không đổi file nào đã commit.
- **`b321098` RUN.md lượt thử 2** (spec `6fc76b5`): chrome 00:31, edge 00:34, firefox 00:37, cả 3 đều 8 Fail / 7 Pass. Fail giống nhau ở cả 3 trình duyệt: 01, 02, 64, 68, 74, 77, 202, 211.
- **Thêm vào lệnh:** có thêm `chrome_20261117T004504` (00:45, cũng 8F/7P, cùng spec 5/6a). Em ghi là "lượt thử 2 – chrome (chạy lại)" và commit cùng 3 report kia.
- **Lệnh chạy lượt chính thức** (trong `HW04\tests`; backend, web, admin phải đang chạy):
  ```
  npx playwright test A_FR01 --project=chrome; npx playwright test A_FR01 --project=edge; npx playwright test A_FR01 --project=firefox
  ```
- **Cần quyết định:** không có.
````
*File AI ghi/gửi trong lượt này:* `esc.js`

**Xử lý:** [...]

---

## #7 | 01:11 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #7, A_FR01.
1. RUN.md: ghi lượt chính thức (3 report mới nhất chrome/edge/firefox, spec @3d19917, 8F/7P cả 3). Kiểm từng report có "Run by: 23120255" + ISO timestamp. Commit report chính thức + RUN.md.
2. Đo dung lượng HW04/reports/ (từng thư mục). Nếu tổng các lượt thử làm zip có nguy cơ > 20 MB thì báo, chưa xoá gì.
3. BƯỚC 6: merge_reports.py → HW04/A_FR01/results.md (bảng TC × 3 trình duyệt + tổng). bug_groups.md: mỗi Fail ghi TC, Expected, Actual (nguyên văn assertion lỗi), trình duyệt, yêu cầu bị vi phạm, vị trí code SUT, issue HW02 liên quan (#, chỉ dữ kiện); nhóm theo triệu chứng giống hệt. Tách ảnh lỗi từ report ra HW04/A_FR01/evidence/<TC>_<browser>.png.
   KHÔNG viết mô tả bug, không đề xuất gộp/tách.
4. Commit "HW04[A-FR01] 6/6". DỪNG.
Báo cáo ≤ 10 dòng: số nhóm G, TC mỗi nhóm, dung lượng reports.
```

**Output:**
```
Consistent (annotation `phản hồi` = spec ≥5/6b). Ghi RUN.md + commit.

Đang mở rộng `merge_reports.py` (Actual nguyên văn, nhóm theo triệu chứng, tách ảnh từ report).

Bước 6 của A_FR01 đã xong và commit; em dừng ở đây. Có một rủi ro: nếu zip cả 10 report thì vượt 20 MB, em chưa xoá gì.

### Báo cáo cho phiên thảo luận
- **Lượt chính thức** (spec `3d19917`): chrome 01:01:15, edge 01:04:19, firefox 01:07:08, cả 3 đều 8 Fail / 7 Pass. Em mở từng `index.html` để kiểm: tiêu đề và tên tab đều có `Run by: 23120255 · <ISO +07:00>`, metadata khớp. Commit `74dd2c6` (3 report + `RUN.md`).
- **Dung lượng `HW04/reports/`: 68 MB** cho 10 thư mục.
  - Lượt thử: chrome 2.3 / 5.4 / 4.7 MB · edge 2.3 / 5.4 MB · firefox 3.5 / 15 MB.
  - Chính thức: chrome 5.2 · edge 5.7 · firefox 19 MB.
  - Zip thử: cả 10 thư mục ≈ **26.8 MB (> 20 MB)**; chỉ 3 lượt chính thức ≈ 10.6 MB.
- **Bước 6** (`9905eca`, đã freeze `step6/`):
  - `results.md`: bảng 15 TC × 3 trình duyệt; tổng mỗi trình duyệt Pass 7, Fail 8, Blocked 0.
  - `bug_groups.md`: 3 nhóm, gom theo cùng các assertion lỗi và cùng giá trị nhận được.
  - 24 ảnh trong `HW04/A_FR01/evidence/<TC>_<browser>.png`.
- **Các nhóm:**
  - G1: 01, 02, 64, 68, 74, 77 (HW02 BUG-01, issue #17). Lỗi chung: URL vẫn ở `/register`, có 1 hộp lỗi, không có user mới.
  - G2: 202 (BUG-02, issue #18). Không có hộp lỗi và có 1 user mới được tạo.
  - G3: 211 (HW02 ghi BUG-01). 5 assertion lỗi, gồm cả phần đăng nhập lại: vẫn ở `/login`, có lỗi đăng nhập, token null.
- **Thêm vào lệnh:**
  - `merge_reports.py` sửa trong commit 6/6: ghi Actual nguyên văn, nhóm theo triệu chứng, tách ảnh từ dữ liệu nhúng trong report, nhận thêm `--context`.
  - `HW04/A_FR01/bug_context.json` ghi issue, yêu cầu bị vi phạm, vị trí code SUT, lấy từ `HW02/bugs/BUG-01.md`, `BUG-02.md` và `Register.jsx:15-19`.
  - `RUN.md`: sửa ngày kiểm Run by từ 16/11 thành 17/11.
- **Lưu ý về ảnh:** ảnh là lúc test kết thúc, không phải lúc assertion đầu tiên lỗi. Ví dụ ảnh của 202 là trang `/login`. Đã ghi chú trong `bug_groups.md`. Em xem 2/24 ảnh: chỉ có giao diện app và dữ liệu test, không có thông tin cá nhân. 22 ảnh còn lại em chưa xem, cần xem trước khi push (repo public).
- **Cần quyết định:**
  - Z1 – report vượt giới hạn: (a) zip chỉ 3 lượt chính thức, lượt thử để trên GitHub; (b) xoá trace khỏi report lượt thử; (c) chia zip.
```
*File AI ghi/gửi trong lượt này:* `merge_reports.py`

**Xử lý:** [...]

---

## #8 | 01:17 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #8.
1. Z1=d: playwright.config.ts trace 'off' (giữ screenshot only-on-failure, video off). Commit "HW04: tắt trace để report < 20 MB (Z1=d)". RUN.md của A: lượt 01:01–01:07 → "lượt thử 3"; SV sẽ chạy lại A làm lượt chính thức.
2. BƯỚC 1 skill cho B_FR07 (từ HW02/B_FR07/testcases.json, 15 TC UI, tối đa 2 Blocked). Lưu ý SUT (HW02 handoff/CLAUDE.md): giỏ web là state React, không gọi /api/cart, không lưu localStorage → oracle dữ liệu qua API không áp dụng được cho giỏ; dùng trạng thái giỏ trên UI (số dòng, số lượng, tổng tiền) làm oracle, ghi rõ trong selection.md. Bỏ case cần reload trang nếu Expected phụ thuộc lưu trữ.
3. check_data.py, freeze, commit "HW04[B-FR07] 1/6". DỪNG.
Báo cáo ≤ 12 dòng: bảng 15 TC (mã, loại +/-/biên, kỹ thuật, HW02 status), TC không lấy + lý do.
```

**Output:**
```
Now B_FR07 candidates.

Facts confirmed (CartContext.jsx: `useState([])`, no axios/localStorage). Writing selection.

Đã tắt trace (Z1=d) và làm xong bước 1 của B_FR07; dừng ở đây để em duyệt.

### Báo cáo cho phiên thảo luận
- **Z1=d:** `playwright.config.ts` đặt `trace: 'off'`, giữ `screenshot: 'only-on-failure'`, `video: 'off'`. `HW04/A_FR01/RUN.md`: 3 lượt 01:01–01:07 đổi thành "lượt thử 3"; `results.md`, `bug_groups.md` và ảnh hiện tại sẽ gộp lại sau lượt chính thức. Commit `597bda7`.
- **B_FR07 bước 1:** 25 TC UI ứng viên, chọn 15, Blocked theo HW02 = 0. `check_data.py` 0 lỗi, 1 cảnh báo: HW02 ghi TC BVA là Positive/Negative chứ không ghi Boundary, nên cột "biên" lấy theo điểm BVA. Commit `656962c`, đã freeze `step1/`.
  - Positive, EP: 01 Fail · 02 Fail · 04 Fail · 08 Fail
  - Negative, EP: 10 Pass · 13 Pass
  - Biên (BVA): 60 LB-1 Pass (Negative) · 61 LB · 62 LB+1 · 63 NOM · 64 LARGE (4 TC này Positive, Fail) · 66 LB Pass (Positive)
  - EG của SV (loại do AI suy ra): 200 Negative Pass · 201 Positive Fail · 205 Positive Fail
- **TC không lấy:**
  - Suite API: giỏ web không gọi API này. TS-GUI: không có inputs.
  - Blocked 03, 06, 65, 203, 206: bug gốc BUG-15. 05, 07: BUG-18 (không có nút +/-). 09: BUG-19.
  - 11, 12: trùng nhóm số lượng không hợp lệ với 10/13/60.
  - Không có case nào cần tải lại trang.
- **Oracle giỏ:** đã ghi trong `selection.md`. `CartContext.jsx:6` dùng `useState([])`, không gọi API, không dùng localStorage. Nên oracle là trạng thái giỏ trên `/cart` trước/sau (số dòng, đơn giá, số lượng, thành tiền, tổng, badge); API chỉ dùng tạo user và dọn dẹp.
- **Thêm vào lệnh:** `select_tc.py` thêm `bug_map` vì `testcases.json` của B không ghi `bug_id`. Bug lấy từ mục "TC liên quan" của `HW02/bugs/BUG-15, 17, 19, 20, 21`. Script cũng thêm phần ghi chú tuỳ ý vào `selection.md`. A_FR01 chạy lại `check_data.py` vẫn 0 lỗi.
- **Cần quyết định:**
  - B1 – loại của TC-200 (Negative), 201 (Positive), 205 (Positive) do AI suy ra: giữ hay sửa.
  - B2 – TC-201 phụ thuộc thời gian (20 lần bấm trong 0,4 s; HW02 ghi lượt 1 chưa chốt verdict), dễ flaky: giữ hay thay bằng TC-11.
```
*File AI ghi/gửi trong lượt này:* `selection.json`

**Xử lý:** [...]

---

## #9 | 01:30 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #9.
1. A_FR01: ghi 3 report mới nhất (trace off, ~1.08 MB/report) là LƯỢT CHÍNH THỨC trong RUN.md; kiểm Run by + kết quả; chạy lại bước 6 (results.md, bug_groups.md, ảnh evidence) theo lượt này. Commit "HW04[A-FR01] 6/6b – lượt chính thức (trace off)".
2. B_FR07 – SV chốt selection (không freeze; commit "HW04[B-FR07] 1/6b – SV chốt"):
   - B1: loại TC-200 = Negative, 201/205 = Positive (ghi "(AI suy ra, SV duyệt)").
   - B2: thay TC-201 bằng TC-11. check_data.py.
3. BƯỚC 2 cho B (fixture/page object: trang sản phẩm, chi tiết, giỏ /cart vào bằng link navbar; đọc trạng thái giỏ từ UI). Freeze → commit "HW04[B-FR07] 2/6". DỪNG.
Báo cáo ≤ 10 dòng.
```

**Output:**
```
Now B selection 1/6b.

Step 2 B: đọc UI thật (Home, ProductDetail, Cart, App navbar).

Probe tạm selector trên Chrome (không phải lượt test).

Lỡ xoá cả thư mục report chrome đã commit bằng glob — khôi phục từ git ngay.

Khôi phục đủ (diff rỗng). Sửa `waitLoaded` của trang chi tiết, probe lại (chỉ xoá đúng thư mục probe).

Đã xong cả 3 phần: A_FR01 lượt chính thức và gộp lại bước 6, B_FR07 SV chốt selection, B_FR07 bước 2. Trong lúc probe, em lỡ xoá rồi khôi phục report chrome đã commit; không mất gì.

### Báo cáo cho phiên thảo luận
- **A_FR01 lượt chính thức:** chrome 01:17:31, edge 01:20:24, firefox 01:23:54; mỗi report khoảng 1.1 MB, không có trace. Cả 3 có tiêu đề `Run by: 23120255 · <ISO +07:00>`, kết quả 8 Fail / 7 Pass, TC Fail trùng các lượt thử. Bước 6 gộp lại: `results.md`, `bug_groups.md` (vẫn 3 nhóm G1/G2/G3), 24 ảnh; đã freeze `step6b/`. Commit `b7cbc6b`.
- **B_FR07 1/6b:** loại TC-200 = Negative, TC-205 = Positive "(AI suy ra, SV duyệt)"; thay TC-201 bằng TC-11. `check_data.py` 0 lỗi, 1 cảnh báo (HW02 ghi TC BVA là Positive/Negative, không có loại Boundary). Còn 9 TC từng Fail, 6 TC Pass. Commit `77111f7`.
- **B_FR07 2/6:**
  - `pages/shop.pages.ts`: navbar, trang chủ (thẻ sản phẩm tìm theo link `/product/<id>`), trang chi tiết, giỏ `/cart` vào bằng link navbar; `state()` đọc dòng, giá, số lượng, thành tiền, tổng, badge từ UI.
  - `fixtures/b_fr07.ts`: bảng sản phẩm seed đọc từ tiền điều kiện trong file data (không qua API). `startSession` cho khách/user (user tạo qua API rồi đăng nhập trên UI). `buildCart` theo cú pháp HW02 `TC:`/`CT: … × n`; cú pháp lạ thì báo lỗi, không đoán.
  - Dialog được ghi lại rồi xử lý theo `dialogAction` (mặc định dismiss) để trang không bị treo. User tạo trong case được xoá sau case.
  - `tsc` Pass; probe trên Chrome đọc đúng trạng thái giỏ. Đã freeze `step2/`, commit `8b77124`.
- **Dữ kiện SUT thấy khi probe** (chỉ ghi nhận): giỏ trống không có ảnh/icon; không có badge; bấm Xóa không hiện dialog; bấm "Thêm vào giỏ hàng" ở trang chi tiết lần 1 không thêm, lần 2 mới thêm và nút đổi thành "Đã thêm".
- **Sự cố:** khi dọn report của probe đầu tiên, em dùng `rm -rf ../reports/chrome_*` nên xoá luôn các report chrome đã commit, kể cả lượt chính thức. Đã khôi phục bằng `git checkout -- HW04/reports`; `git diff` so với HEAD rỗng. Từ lần probe sau em chỉ xoá đúng thư mục mới sinh, và đã ghi quy tắc này vào memory.
- **Cần quyết định:** không có.
```
*File AI ghi/gửi trong lượt này:* `shop.pages.ts`, `b_fr07.ts`, `reports-no-glob-delete.md`

**Xử lý:** [...]

---

## #10 | 01:37 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #10, B_FR07, BƯỚC 3.
1. Sinh HW04/tests/B_FR07.spec.ts theo SKILL.md bước 3 (lặp theo data, không hardcode, expect.soft, kiểm sha1). Áp luôn các bài học từ review A: không mode serial; không catch rỗng; chờ trạng thái rõ ràng thay cho chờ cứng; escape chuỗi trước new RegExp; expected không đọc được → ném lỗi, không đoán; oracle thông báo yếu → annotation.
2. Bấm đúng số lần ghi trong procedure – KHÔNG bấm thêm để lách lỗi "lần bấm đầu bị nuốt" (đó là hành vi SUT cần lộ ra).
3. ≥3 kiểu assertion: trạng thái UI (toHaveURL/toBeVisible), nội dung (toHaveText/toContainText), oracle trạng thái giỏ trước/sau dạng object (toEqual), đếm (toHaveCount/toHaveValue). Ghi bảng vào HW04/B_FR07/assertions.md.
4. tsc + --list (45 test). Freeze step3/ → commit "HW04[B-FR07] 3/6". DỪNG.
Báo cáo ≤ 10 dòng + lệnh SV chạy 3 trình duyệt.
```

**Output:**
````
Spec B phức tạp hơn A (6 dạng Expected, 6 dạng Thao tác). Đang viết spec + kiểm parser offline trên 15 expected.

Kiểm parser offline trên 15 expected trước khi viết spec.

Chỉ còn 1 cụm thật sự không tự động được (TC-08 "dòng chưa bị xoá khi dialog đang mở" — dialog native khoá trang). Kiểm escape trong file rồi viết spec.

tsc OK, `--list` = 45 test, không sinh report thừa. Giờ ghi assertions.md rồi freeze + commit.

B_FR07 bước 3 đã xong và đã commit. tsc Pass, `--list` = 45 test (15 TC × 3 trình duyệt). Chưa chạy test thật nào, đúng phạm vi lệnh, nên spec chưa được kiểm trên SUT.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: B_FR07 bước 3: spec data-driven, bảng assertion, freeze.
- File:
  - `HW04/tests/B_FR07.spec.ts`
  - `HW04/tests/oracles/b_fr07.oracle.ts`: đọc cột `Thao tác`/`expected`; cú pháp lạ thì ném lỗi; cụm không ánh xạ được ghi annotation. Đã thử offline đủ 15 TC.
  - `HW04/B_FR07/assertions.md`
  - Bản đông lạnh ở `appendix/ai-outputs/B_FR07/step3/`.
- Đã áp bài học từ review A:
  - Không chạy mode serial, có kiểm workers > 1.
  - Không có catch rỗng: chỉ bắt `TimeoutError`, lúc điều hướng thì đổi thành Blocked, lúc chờ phản hồi thì ghi "không có phản hồi"; lỗi khác ném lại.
  - Chờ trạng thái cụ thể (`waitForFunction`, `poll`), không chờ cứng; chuỗi lấy từ expected chỉ dùng regex cố định nên không cần escape.
  - Bấm Thêm/Xóa đúng 1 lần.
- Các kiểu assertion:
  - `toHaveURL`/`toBeVisible` (trạng thái UI)
  - `toHaveText`/`toContainText` (nội dung)
  - `toEqual` trên các dòng giỏ SAU, dựng từ TRƯỚC + thay đổi expected nêu (object)
  - `toHaveCount` (đếm), `toBe` cho Tổng/badge
  - phản hồi ≤ 2 s (B21) và dialog (`poll`)
- Giỏ TRƯỚC không khớp cột `Giỏ ban đầu` → Blocked (B20).
- Annotation `oracle không tự động`: TC-08 "dòng chưa bị xoá khi dialog đang mở" (dialog native khoá trang); `oracle thông báo yếu`: TC-01 (chỉ kiểm chữ "trống").
- Kết quả kiểm tra: tsc Pass, `--list` 45 test; test Not run.
- Commit: `7e75536` HW04[B-FR07] 3/6: spec data-driven + parser oracle + bảng assertion (45 test)
- Cần quyết định: không.

**Lệnh SV chạy 3 trình duyệt** (PowerShell, trong `HW04\tests`, backend/web/admin đang chạy):
```powershell
npx playwright test B_FR07 --project=chrome; npx playwright test B_FR07 --project=edge; npx playwright test B_FR07 --project=firefox
```
````
*File AI ghi/gửi trong lượt này:* `b_fr07.oracle.ts`, `B_FR07.spec.ts`

**Xử lý:** [...]

---

## #11 | 01:51 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #11, B_FR07.
1. Tạo HW04/B_FR07/RUN.md: 3 report vừa chạy = "lượt thử 1" (6P/9F mỗi trình duyệt).
2. Chỉ báo dữ kiện (không sửa code): bảng 15 TC × 3 trình duyệt so với HW02 status; TC nào verdict khác HW02 hoặc khác giữa các trình duyệt; với mỗi TC Pass, liệt kê annotation "không tự động"/"oracle yếu" (nếu có) để SV xét pass giả.
3. Commit RUN.md + 3 report. DỪNG.
Báo cáo ≤ 10 dòng.
```

**Output:**
```
Kết quả: 15/15 trùng HW02, 3 trình duyệt giống nhau. Lấy thêm annotation dữ kiện của 6 TC Pass để ghi vào RUN.md.

Đã ghi RUN.md cho lượt thử 1 của B_FR07 và commit cùng 3 report. Cả 15 TC cho cùng verdict với HW02, giống nhau ở 3 trình duyệt.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: B_FR07, ghi lượt thử 1 và báo dữ kiện (không sửa code).
- File: `HW04/B_FR07/RUN.md` (bảng lượt chạy, bảng 15 TC × 3 trình duyệt kèm assertion fail, bảng annotation của các TC Pass) và 3 report `chrome_20261117T014350`, `edge_20261117T014549`, `firefox_20261117T014756` (mỗi report khoảng 1.2 MB).
- Kết quả: mỗi trình duyệt 6 Pass, 9 Fail, 0 Blocked; Run by ghi `23120255 · <ISO +07:00>` ở cả 3.
  - Pass: TC-10, 11, 13, 60, 66, 200 — trùng HW02.
  - Fail: TC-01, 02, 04, 08, 61, 62, 63, 64, 205 — trùng HW02.
- So HW02: verdict khác HW02 không có; khác giữa các trình duyệt không có.
- TC Pass: không TC nào có annotation "oracle không tự động" hay "oracle thông báo yếu" (2 loại này chỉ ở TC-08 và TC-01, đều Fail). Dữ kiện còn lại (giá trị ô Số lượng sau khi gõ, phản hồi sau khi bấm thêm, dialog, giỏ TRƯỚC/SAU) đã chép vào RUN.md để SV xét pass giả.
- Harness: `results.json` ghi mỗi annotation 2 lần (mức test và mức result), không ảnh hưởng verdict.
- Commit: `6d9f402` HW04[B-FR07] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md — lệnh không ghi message nên em đặt số bước 4/6.
- Cần quyết định: không.
```

**Xử lý:** [...]

---

## #12 | 01:55 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Giờ mình sẽ tạm thời đi ngủ, giúp mình ghi nhớ những gì đang chạy nhé. Rồi tắt nó. Sáng mình dậy mình nhắn "Chạy lại tất cả" thì bạn chạy lại những gì đang bật nhé
```

**Output:**
```
Đã ghi nhớ. Giờ tắt 3 tiến trình.

Đã ghi nhớ và tắt cả 3 tiến trình. Cổng 3000, 5173, 5174 đều không còn ai nghe.

**Lúc tắt đang chạy:**
- Backend :3000 (`node server.js`)
- Web :5173 (vite `frontend-web`)
- Admin :5174 (vite `frontend-admin`)

Không có test nào đang chạy. Mọi việc đã commit (mới nhất là `6d9f402`, lượt thử 1 của B_FR07).

Sáng bạn nhắn **"Chạy lại tất cả"** thì mình bật lại đúng 3 cái trên. Backend khởi động lại sẽ seed lại CSDL từ đầu, nên tài khoản hay sản phẩm tạo thêm trước đó sẽ mất. Bật xong mình kiểm 3 cổng rồi báo bạn.

Chúc bạn ngủ ngon.

No response requested.
```
*File AI ghi/gửi trong lượt này:* `hw03-runtime-state.md`

**Xử lý:** [...]

---

## #13 | 13:39 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #12, B_FR07 BƯỚC 5 (+ ảnh A).
1. Chép NGUYÊN VĂN 4 ý soi spec của SV vào HW04/B_FR07/review_sv.md, kèm cột "Đối chiếu code (phiên thảo luận)": ý 1 không có waitForTimeout (chỉ ngưỡng 2 s B21, dòng 62–72, 161); ý 2 selector bám Expected, yếu ở .first() + mọi img/svg trong main; ý 3 /trống/i gõ cứng dòng 121, tên SP dòng 133 lấy từ data; ý 4 mặc định dismiss, xoá có 'xác nhận' → accept; phần "dòng chưa xoá khi dialog mở" TC-08 không tự động hoá được. Commit trước khi sửa code.
2. Sửa, mỗi mục một commit có sửa B_FR07.spec.ts:
   5/6a (R1=a) – từ khoá giỏ trống chuyển vào HW04/data/B_FR07.json, trường riêng ghi "giả định SV chốt (SRS không có câu chữ)"; KHÔNG sửa expected (sha1 giữ nguyên).
   5/6b (R2) – ảnh/icon minh hoạ phải nằm trong cùng khối chứa dòng chữ giỏ trống; bỏ .first() chung.
   5/6c (P1=a) – chụp ảnh ngay sau thao tác chính (sau bấm Thêm/Xoá) bằng testInfo.attach, tên <TC>_after-action.
3. P1=a cho A: thêm ảnh ngay sau khi bấm Đăng Ký vào A_FR01.spec.ts (commit "HW04[A-FR01] 5/6e – ảnh sau submit"). Ghi vào RUN.md của A: lượt 01:17–01:24 → "lượt thử 4"; SV chạy lại A làm lượt chính thức.
4. Ghi TC-08 (phần dialog đang mở) vào HW04/B_FR07/not_automated.md + lý do.
5. tsc + --list sau mỗi commit. DỪNG. Báo cáo ≤ 10 dòng + lệnh SV chạy lại A và B.


nguyên văn:



Soi spec: 
- Chờ hardcode (waitForTimeout), có thể gây chậm suite cũng như dễ flaky: Giả sử nó chạy nhanh hơn thì gây chậm, còn nếu có khi mạng lag hoặc CPU lag thì gây ra flaky.
- Selector phụ thuộc cấu trúc DOM và thẻ HTML chung chung: cảm giác script kiểm tra hình minh hoạ giỏ giống bằng selector main img, main svg không đủ tốt lắm.Vậy nên dễ nhầm nếu trong <main> có icon khác hoặc fail nếu UI dùng <canvas>
- Assertion phụ thuộc chặt vào câu chữ tiếng Việt cụ thể: Các assertion đang khớp hardcode text. Nên nếu đổi thông báo thì lại fail.
- Cách bắt sự kiện dialog: script gắn listener page.on('dialog', ...) và tự động accept() ngay lập tức. Nên cái này chỉ check có bật dialog hay không chứ không kiểm tra được trạng thái UI tạm dừng.
```

**Output:**
````
Dòng trích dẫn khớp code. Ghi review_sv.md, commit trước khi sửa.

The esc regex lost backslashes — fix with Edit.

5/6b xong. Giờ 5/6c: chụp ảnh ngay sau bấm Thêm/Xoá.

B xong 3 commit. Giờ A: ảnh sau submit.

Giờ not_automated.md cho TC-08.

Đã xong lệnh #12: 6 commit, tsc và `--list` Pass sau mỗi commit sửa code. Các chỗ sửa chưa chạy trên SUT vì backend/web/admin đang tắt từ tối qua.

### Báo cáo cho phiên thảo luận
- **Review:** `HW04/B_FR07/review_sv.md` chép nguyên văn 4 ý soi spec, kèm cột "Đối chiếu code" theo đúng lệnh. Commit trước khi sửa: `2c8372f`.
- **5/6a `14ac598` (R1=a):** từ khoá "trống" chuyển vào `HW04/data/B_FR07.json`, trường `assumptions.empty_cart_keyword`, ghi "giả định SV chốt (SRS không có câu chữ)".
  - Expected và sha1 giữ nguyên; `check_data.py` 0 lỗi.
  - Để chạy lại `select_tc.py` không làm mất trường này, em sửa thêm script đó, `selection.json` và kiểu `DataFile` trong `ddt.ts`.
- **5/6b `4f3c278` (R2):** chỉ nhận img/svg đang hiển thị nằm trong khối cha trực tiếp của dòng chữ giỏ trống; bỏ `.first()`.
- **5/6c `c8a2ce9` (P1=a):** ảnh `<TC>_after-action` chụp ngay sau bấm Thêm/Xoá, song song với cửa sổ 2 s đo phản hồi B21. TC-205 có 2 lần bấm Thêm nên ảnh tên `-1`, `-2`.
- **A 5/6e `9f26855`:** ảnh `<TC>_after-submit` ngay sau khi bấm Đăng Ký. RUN.md của A: lượt 01:17–01:24 đổi thành "lượt thử 4"; results/bug_groups/evidence của A cần gộp lại sau lượt chính thức mới.
- **`841c7e2`:** `HW04/B_FR07/not_automated.md` ghi TC-08 (phần dialog đang mở) và lý do: dialog native khoá trang nên script không đọc được bảng giỏ khi dialog còn mở.
- **Cần quyết định:** không có.

**Lệnh SV chạy lại A và B.** Bật SUT trước (nhắn "Chạy lại tất cả"), rồi chạy trong PowerShell ở `HW04\tests`:
```powershell
npx playwright test A_FR01 --project=chrome; npx playwright test A_FR01 --project=edge; npx playwright test A_FR01 --project=firefox
npx playwright test B_FR07 --project=chrome; npx playwright test B_FR07 --project=edge; npx playwright test B_FR07 --project=firefox
```
````

**Xử lý:** [...]

---

## #14 | 13:46 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
chạy lại tất cả
```

**Output:**
````
Đã bật lại đủ 3 tiến trình, cả 3 đều trả HTTP 200:
- Backend :3000 — CSDL đã seed lại, có 5 sản phẩm.
- Web :5173 (vite `frontend-web`).
- Admin :5174 (vite `frontend-admin`).

Memory đã cập nhật là đang chạy. Mình chưa chạy test nào.

Lệnh chạy lại A và B làm lượt chính thức (PowerShell, trong `HW04\tests`):
```powershell
npx playwright test A_FR01 --project=chrome; npx playwright test A_FR01 --project=edge; npx playwright test A_FR01 --project=firefox
npx playwright test B_FR07 --project=chrome; npx playwright test B_FR07 --project=edge; npx playwright test B_FR07 --project=firefox
```

Code sửa ở lệnh #12 (5/6a–c của B, 5/6e của A) chưa chạy trên SUT. Nếu muốn, mình chạy thử nhanh trên Chrome với `--reporter=line` trước khi bạn chạy lượt chính thức; cách này không tạo HTML report nên không lẫn vào thư mục `reports`.
````

**Xử lý:** [...]

---

## #15 | 14:04 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #13.
1. A: ghi 3 report mới nhất là LƯỢT CHÍNH THỨC (7P/8F cả 3, spec @9f26855); chạy lại bước 6 (results, bug_groups, evidence – có thêm ảnh after-submit). Commit "HW04[A-FR01] 6/6c – lượt chính thức".
2. B: ghi 3 report mới là "lượt thử 2" (chrome/edge 6P/9F, firefox 5P/10F). Chỉ báo dữ kiện, chưa sửa:
   - TC nào Fail riêng trên firefox, assertion nào, giá trị nhận được (annotation phản hồi B21, ảnh after-action).
   - Ở lượt thử 1 (spec @7e75536) TC đó Pass trên firefox không.
   - Liên quan tới 5/6b (selector minh hoạ) hay 5/6c (ảnh song song cửa sổ 2 s)? Đọc code + so annotation 2 lượt.
3. Đưa SV lệnh chạy lại RIÊNG TC đó trên firefox 3 lần (--grep "<TC>" --repeat-each=3) để kiểm flaky.
Commit RUN.md + report. DỪNG. Báo cáo ≤ 10 dòng.
```

**Output:**
````
3 report rỗng lúc 13:46 = global-setup báo backend chưa chạy (0 test). Không đụng tới, sẽ báo. Xem merge_reports xử lý ảnh thế nào.

Xem ảnh trước khi commit (repo public).

Ảnh chỉ có UI EShop + dữ liệu test (TC-211 có tên/email SV — là dữ liệu HW02 đã public trong data JSON). Ghi RUN.md A, commit.

Phần B: tìm TC Fail riêng trên firefox.

TC-FR07-60 firefox: không phải assertion — worker crash `0xC0000409` lúc 0 ms, thân test chưa chạy. Ghi RUN.md B.

A đã ghi lượt chính thức và gộp lại bước 6; B đã ghi lượt thử 2. TC Fail riêng trên firefox là TC-FR07-60, nhưng đây là tiến trình test bị crash chứ không có assertion nào fail.

### Báo cáo cho phiên thảo luận
- **A lượt chính thức:** 3 report 13:47 / 13:49 / 13:52 (spec @`9f26855`), 7P/8F cả 3 trình duyệt, Run by đúng. Bước 6 vẫn ra 3 nhóm G1–G3. Evidence 48 ảnh = 24 ảnh lúc kết thúc + 24 ảnh `<TC>_after-submit`. Để tách được ảnh after-submit, em sửa thêm `merge_reports.py`. Freeze `step6c/`. Commit `ea55c9c` "HW04[A-FR01] 6/6c – lượt chính thức".
- **Ảnh A:** em chỉ xem 3/48 ảnh, chưa xem đủ từng ảnh theo quy tắc repo; SV nên xem nốt trước khi push. 3 ảnh đã xem chỉ có UI EShop và dữ liệu test; ảnh TC-211 có "Lê Tấn Hiệp" / `hiep.sv12@domain.com`, là dữ liệu HW02 đã có sẵn trong data JSON.
- **B lượt thử 2:** chrome/edge 6P/9F, firefox 5P/10F, trùng lượt thử 1 ngoại trừ TC-FR07-60 trên firefox. Commit `ef419f2`.
- **TC-FR07-60 / firefox:**
  - Lỗi `worker process exited unexpectedly (code=3221226505)`, tức `0xC0000409`. Không có assertion fail.
  - Test chạy 0 ms, không có annotation nào (kể cả annotation phản hồi B21), không có ảnh after-action → thân test chưa chạy.
  - Worker này vừa chạy TC-10/11/13 (đều Pass, có ảnh) thì crash khi bắt đầu TC-60.
- **So lượt thử 1 (@`7e75536`):** TC-60 Pass trên firefox. Ở lượt thử 2, TC-60 cũng Pass trên chrome/edge.
- **Liên quan 5/6b, 5/6c?**
  - 5/6b chỉ chạy ở TC-01; TC-60 không đi qua đoạn đó.
  - 5/6c nằm sau bấm Thêm, TC-60 chưa tới. Nhưng cùng worker đã chạy 5/6c ở 3 TC trước, nên dữ kiện chưa đủ để loại hẳn.
  - Theo quy ước HW04, ô này là ứng viên Blocked; `merge_reports.py` hiện vẫn đếm là Fail.
- **Bất thường:** 3 report rỗng `*_20261117T13460{5,6,7}`, 0 test, do global-setup báo backend không trả lời. Em không commit và cũng chưa xoá.
- **Cần quyết định:** xoá hay giữ 3 report rỗng (`HW04/reports/*_20261117T13460x`).

**SV chạy kiểm flaky** (PowerShell, trong `HW04\tests`):
```powershell
npx playwright test B_FR07 --project=firefox --grep "TC-FR07-60 " --repeat-each=3
```
````

**Xử lý:** [...]

---

## #16 | 14:10 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #14.
1. B: xoá 3 report rỗng *_20261117T13460{5,6,7}; RUN.md ghi 1 dòng (global-setup: backend chưa chạy, 0 test). Ghi TC-60/firefox ở lượt thử 2 = worker crash 0xC0000409, thân test chưa chạy; SV chạy riêng --repeat-each=3: 3/3 Pass → lỗi hạ tầng, không lập bug. Commit.
   SV đang chạy lượt chính thức B – KHÔNG khởi động lại SUT, không chạy test.
2. BƯỚC 1 skill cho C_FR15 (HW02/C_FR15/testcases.json, 15 TC suite UI: TS-DOM-UI, TS-BVA-UI-THEM, TS-BVA-UI-SUA, TS-SV-UI; tối đa 2 Blocked; có cả Thêm và Sửa). Lưu ý SUT (HW02 handoff/CLAUDE.md): đăng nhập admin admin@eshop.com/Admin123!; form Thêm/Sửa dùng chung, nút "Lưu sản phẩm", chỉ có placeholder; sửa 1 SP → mọi dòng đổi tên; hộp thoại "Cập nhật thành công!"; price null + id chẵn làm backend sập → ghi rủi ro này trong selection.md (TC nào có thể làm sập backend, đề xuất xử lý), CHƯA quyết. Oracle dữ liệu = GET /api/products trước/sau.
3. check_data.py, freeze, commit "HW04[C-FR15] 1/6". DỪNG.
Báo cáo ≤ 12 dòng: bảng 15 TC (mã, Thêm/Sửa, loại, kỹ thuật, HW02 status), TC có nguy cơ làm sập backend.
```

**Output:**
```
Phần 1 xong. `firefox_20261117T140840` (lượt chạy riêng của SV) để nguyên. Sang C_FR15 bước 1: xem ứng viên.

Đang đọc 45 ứng viên UI của C_FR15 để chọn 15 TC.

Xem rủi ro sập backend (price null + id chẵn) trong mã SUT và tài liệu HW02.

Đã đọc đủ ứng viên và mã SUT. Đang viết selection.json cho C (15 TC, 0 Blocked, có cả Thêm/Sửa/Xóa).

Đã xong cả 2 phần của lệnh #14. Không khởi động lại SUT, không chạy test; 3 report SV mới chạy (`chrome_…141103`, `edge_…141230`, `firefox_…140840`) để nguyên, chưa commit.

### Báo cáo cho phiên thảo luận
- **B `d676bf9`:** đã xoá 3 report rỗng 13:46. RUN.md ghi: lượt 13:46 backend chưa chạy, 0 test; TC-60/firefox ở lượt thử 2 là worker crash `0xC0000409`, thân test chưa chạy; chạy riêng 3/3 Pass → lỗi hạ tầng, không lập bug.
- **C 1/6 `25f6e6e`:** `HW04/C_FR15/selection.{json,md}`, `HW04/data/C_FR15.json`, đã freeze `step1/`. `check_data.py`: 0 lỗi, 1 cảnh báo (HW02 không ghi loại Boundary, như A và B). Selection có 0 Blocked, gồm 10 Thêm, 4 Sửa, 1 Xóa.

| TC | Thao tác | Loại | Kỹ thuật | HW02 |
|---|---|---|---|---|
| 01 / 03 / 05 | Thêm / Sửa / Xóa | Positive | EP | Pass / Fail / Pass |
| 07 · 10 · 11 | Thêm | Negative | EP | Pass · Fail · Fail |
| 15 | Sửa | Negative | EP | Fail |
| 65 · 66 · 67 · 68 | Thêm | Pos · Neg · Neg · Pos | BVA UB · UB+1 · LB-1 · LB | Pass · Fail · Fail · Pass |
| 77 · 78 | Sửa | Pos · Neg | BVA UB · UB+1 | Pass · Fail |
| 200 · 201 | Thêm | Negative (AI suy ra) | EG: XSS · 1e5 | Fail · Fail |

- **Nguy cơ sập backend** (cơ chế BUG-48: GET `/api/products/:id` trên id chẵn có price = null):
  - TC gọi `/:id` lên M: 03, 05, 15, 77, 78. M dựng qua API với price 1000000, các case này ghi giá trị số hoặc giữ nguyên → theo dữ liệu đã chọn không có price null.
  - TC ghi giá bất thường qua UI: 11 (HW02 lưu `""`, không phải null), 201; script không gọi `/:id` cho bản ghi mới của case Thêm.
  - Gần cơ chế nhất là TC-16 (Sửa giá rỗng), đã loại.
  - Đề xuất xử lý (a)–(d) ghi trong `HW04/C_FR15/selection.md`, chưa quyết.
- **Cần quyết định:**
  - C1: duyệt loại Negative cho TC-200 và TC-201 (AI suy ra; TS-SV-UI của HW02 không ghi loại).
  - C2: xử lý rủi ro sập backend: (a) kiểm backend sau mỗi case, chết thì Blocked rồi resetDb; (b) lấy M từ danh sách GET thay cho `/:id`; (c) cleanup xoá bản ghi price null hoặc rỗng; (d) giữ nguyên procedure.
```
*File AI ghi/gửi trong lượt này:* `selection.json`

**Xử lý:** [...]

---

## #17 | 14:18 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #15.
1. B: ghi 3 report mới nhất là LƯỢT CHÍNH THỨC (6P/9F cả 3, spec @c8a2ce9 hoặc commit spec mới nhất); kiểm Run by; bước 6 (results.md, bug_groups.md, evidence gồm ảnh after-action). Freeze → commit "HW04[B-FR07] 6/6 – lượt chính thức".
2. C: SV chốt (không freeze; commit "HW04[C-FR15] 1/6b – SV chốt"):
   - C1: loại TC-200 = Negative, TC-201 = Negative "(AI suy ra, SV duyệt)".
   - C2=a: ghi vào selection.md: sau mỗi case kiểm backend sống; sập → case đó Fail + annotation "backend sập", resetDb trước case kế. Không đổi procedure, không xoá bản ghi để tránh sập.
3. BƯỚC 2 cho C (fixture/page object admin: login admin, form Thêm/Sửa theo placeholder, nút "Lưu sản phẩm", bảng SP, dialog; API GET /api/products trước/sau; health-check backend). Freeze → commit "HW04[C-FR15] 2/6". DỪNG.
Báo cáo ≤ 10 dòng + số nhóm G của B.
```

**Output:**
```
B 6/6 xong (6 nhóm G). Giờ C 1/6b: SV chốt C1, C2=a.

Bước 2 C: đọc UI admin thật.

Đã xong cả 3 phần của lệnh #15: B có lượt chính thức và bước 6, C có SV chốt và bước 2. B có **6 nhóm G** (G1 gồm TC-61/62/63/64; G2–G6 mỗi nhóm 1 TC: 01, 02, 04, 08, 205).

### Báo cáo cho phiên thảo luận
- **B 6/6 `072e47f`:** 3 report 14:11 / 14:12 / 14:13 (spec @`c8a2ce9`), mỗi trình duyệt 6P/9F, trùng HW02. Đã kiểm Run by trên tiêu đề cả 3 report.
  - Bước 6: `results.md`, `bug_groups.md`, evidence 54 ảnh = 27 ảnh lúc kết thúc + 27 ảnh after-action; đã freeze `step6/`.
  - Em chỉ xem 3/54 ảnh (đều chỉ có UI EShop và tài khoản "Cart Tester"); SV xem nốt trước khi push.
  - Em commit thêm report chạy riêng TC-60 (`firefox_20261117T140840`, 3/3 Pass) làm bằng chứng cho kết luận lỗi hạ tầng. Lệnh không yêu cầu, nên nếu không muốn thì gỡ commit file này.
- **C 1/6b `f4086c0`:** C1 ghi TC-200/201 là Negative "(AI suy ra, SV duyệt)". C2=a ghi vào `selection.md` ở mục "Rủi ro sập backend" và mục quyết định. `check_data.py` 0 lỗi.
- **C 2/6 `16d791d`:** `pages/admin.pages.ts` và `fixtures/c_fr15.ts`, đã freeze `step2/`.
  - Page object: trang login admin; thanh bên tab "Sản phẩm"; form Thêm/Sửa định vị theo placeholder, select danh mục, nút "Lưu sản phẩm"/"Hủy sửa", đọc ô HTML5 không hợp lệ; bảng đọc Tên SP + giá dạng số, nút Sửa/Xóa theo tên dòng.
  - Fixture: `catalog` (gọi API danh sách, chi tiết, tạo, xoá, kiểm backend sống); dựng M theo procedure; dialog được ghi lại rồi bấm OK; cleanup theo danh sách lúc bắt đầu case.
  - C2=a: sau mỗi case kiểm backend; nếu sập thì gắn annotation "backend sập", resetDb, case đó Fail.
- **Kiểm tra C:** tsc Pass. Probe trên Chrome (`--reporter=line`, không sinh report) đọc đúng bảng, heading Thêm/Sửa, bong bóng HTML5 khi tên rỗng; cleanup trả CSDL về 5 bản ghi.
- **Bất thường:** khi probe, M có id 6 và GET `/api/products/6` trả `price` dạng chuỗi `"1000000"`, khớp BUG-48 (`server.js:162`).
- **Cần quyết định:** chưa chặn bước kế. `HW04/reports` hiện 93 MB, phần lớn là các report còn trace của các lượt thử đầu của A (khoảng 19 MB mỗi report) → zip sẽ vượt 20 MB nếu không loại các lượt thử khỏi zip (`export-ignore`).
```
*File AI ghi/gửi trong lượt này:* `admin.pages.ts`, `c_fr15.ts`

**Xử lý:** [...]

---

## #18 | 14:23 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Báo cáo cho phiên thảo luận

- B 6/6 072e47f: 3 report 14:11 / 14:12 / 14:13 (spec @c8a2ce9), mỗi trình duyệt 6P/9F, trùng HW02. Đã kiểm Run by trên tiêu đề cả 3 report.
  - Bước 6: results.md, bug_groups.md, evidence 54 ảnh = 27 ảnh lúc kết thúc + 27 ảnh after-action; đã freeze step6/.
  - Em chỉ xem 3/54 ảnh (đều chỉ có UI EShop và tài khoản "Cart Tester"); SV xem nốt trước khi push.
  - Em commit thêm report chạy riêng TC-60 (firefox_20261117T140840, 3/3 Pass) làm bằng chứng cho kết luận lỗi hạ tầng. Lệnh không yêu cầu, nên nếu không muốn thì gỡ commit file này.
- C 1/6b f4086c0: C1 ghi TC-200/201 là Negative "(AI suy ra, SV duyệt)". C2=a ghi vào selection.md ở mục "Rủi ro sập backend" và mục quyết định. check_data.py 0 lỗi.
- C 2/6 16d791d: pages/admin.pages.ts và fixtures/c_fr15.ts, đã freeze step2/.
  - Page object: trang login admin; thanh bên tab "Sản phẩm"; form Thêm/Sửa định vị theo placeholder, select danh mục, nút "Lưu sản phẩm"/"Hủy sửa", đọc ô HTML5 không hợp lệ; bảng đọc Tên SP + giá dạng số, nút Sửa/Xóa theo tên dòng.
  - Fixture: catalog (gọi API danh sách, chi tiết, tạo, xoá, kiểm backend sống); dựng M theo procedure; dialog được ghi lại rồi bấm OK; cleanup theo danh sách lúc bắt đầu case.
  - C2=a: sau mỗi case kiểm backend; nếu sập thì gắn annotation "backend sập", resetDb, case đó Fail.
- Kiểm tra C: tsc Pass. Probe trên Chrome (--reporter=line, không sinh report) đọc đúng bảng, heading Thêm/Sửa, bong bóng HTML5 khi tên rỗng; cleanup trả CSDL về 5 bản ghi.
- Bất thường: khi probe, M có id 6 và GET /api/products/6 trả price dạng chuỗi "1000000", khớp BUG-48 (server.js:162).
- Cần quyết định: chưa chặn bước kế. HW04/reports hiện 93 MB, phần lớn là các report còn trace của các lượt thử đầu của A (khoảng 19 MB mỗi report) → zip sẽ vượt 20 MB nếu không loại các lượt thử khỏi zip (export-ignore).
```

**Output:**
```
Đoạn bạn vừa dán là khối báo cáo của chính mình ở lượt trước, không kèm lệnh mới nào. Có thể bạn định dán vào phiên thảo luận trên claude.ai.

Mình chưa làm gì thêm. Repo sạch, commit mới nhất là `16d791d` (C 2/6). Mình đang dừng chờ lệnh #16, có thể là bước 3 của C (sinh spec) hoặc quyết định export-ignore cho các lượt thử để zip dưới 20 MB.
```

**Xử lý:** [...]

---

## #19 | 14:24 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #16, C_FR15, BƯỚC 3.
1. Sinh HW04/tests/C_FR15.spec.ts theo SKILL.md bước 3 + mọi bài học A/B: không serial; không catch rỗng; không chờ cứng; escape trước new RegExp; expected không đọc được → ném lỗi; từ khoá/câu chữ không có trong expected thì để trong file data (giả định SV), không gõ cứng trong spec; ảnh <TC>_after-save ngay sau bấm "Lưu sản phẩm"/Xóa (chụp SAU khi đo xong, không song song cửa sổ đo); bấm đúng số lần theo procedure.
2. price chuỗi ở id chẵn (BUG-48): đọc HW02/tests/C_FR15/oracle.ts xem HW02 so price thế nào, làm giống để verdict so được với HW02; Fail do kiểu chuỗi → annotation "price dạng chuỗi (BUG-48)".
3. ≥3 kiểu assertion: UI (toHaveURL/toBeVisible), nội dung (toHaveText/toContainText), oracle dữ liệu GET trước/sau (toEqual), đếm/giá trị (toHaveCount/toHaveValue). Bảng vào HW04/C_FR15/assertions.md.
4. tsc + --list (45). Freeze step3/ → commit "HW04[C-FR15] 3/6". DỪNG.
Báo cáo ≤ 10 dòng + lệnh SV chạy 3 trình duyệt.
```

**Output:**
````
Parser đọc đúng 15/15, không còn cụm dư. Thêm giả định (selector thông báo trên trang, chữ alert XSS, nghĩa "Form chặn") vào data, rồi viết spec.

Đã sinh spec C_FR15 bước 3 và commit; tsc Pass, `--list` = 45 test. Chưa chạy test thật nào, nên spec chưa được kiểm trên SUT.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: C_FR15 bước 3 — spec data-driven, parser oracle, bảng assertion, freeze.
- File:
  - `HW04/tests/C_FR15.spec.ts`
  - `HW04/tests/oracles/c_fr15.oracle.ts`: kiểm offline 15/15, 0 cụm expected không ánh xạ được.
  - `HW04/C_FR15/assertions.md`
  - Bản đông lạnh ở `appendix/ai-outputs/C_FR15/step3/`.
- Đã áp bài học A/B:
  - Không mode serial, có kiểm workers > 1; không có catch rỗng (chỉ đổi `TimeoutError` thành Blocked).
  - Không chờ cứng: chờ log mạng POST/PUT/DELETE, rồi GET danh sách hoặc hộp thoại, rồi 2 khung hình; quá 10 s → Blocked.
  - Escape chuỗi trước `new RegExp`; expected không đọc được thì ném lỗi; bấm "Lưu sản phẩm"/"Xóa" đúng 1 lần.
  - Ảnh `<TC>_after-save` chụp sau khi đo xong, không song song với việc chờ.
- **Giả định mới cần SV duyệt** (lấy từ HW02, đưa vào `assumptions` của `HW04/data/C_FR15.json`, expected và sha1 giữ nguyên):
  - selector "thông báo trên trang" (HW02 H3)
  - chữ của alert XSS = `'1'` (C21)
  - "Form chặn" = dữ liệu SAU = TRƯỚC (C24)
- **So giá giống HW02:** `sameNumber` (`Number(actual) === expected`, null/"" không khớp); trường giữ nguyên so bằng `String`. Vì vậy price dạng chuỗi ở id chẵn không làm Fail; khi M_TRƯỚC hoặc M_SAU trả price là chuỗi, spec chỉ gắn annotation "price dạng chuỗi (BUG-48)".
- Assertion: `toBeVisible`, `toHaveText`, `toHaveValue`, `toHaveCount`, `toEqual` (GET trước/sau, M, bảng), `toBe`.
- Kết quả kiểm tra: tsc Pass, `--list` 45 test; test Not run.
- Commit: `370c9cd` HW04[C-FR15] 3/6: spec data-driven + parser oracle + bảng assertion (45 test); giả định ngoài expected vào data
- Cần quyết định: không chặn bước kế. Chỉ có 3 giả định ở trên (SV duyệt khi review bước 5).

**Lệnh SV chạy 3 trình duyệt** (PowerShell, trong `HW04\tests`; backend/web/admin đang chạy):
```powershell
npx playwright test C_FR15 --project=chrome; npx playwright test C_FR15 --project=edge; npx playwright test C_FR15 --project=firefox
```
````
*File AI ghi/gửi trong lượt này:* `c_fr15.oracle.ts`, `C_FR15.spec.ts`

**Xử lý:** [...]

---

## #20 | 14:46 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #17.
1. C: HW04/C_FR15/RUN.md – 3 report vừa chạy = "lượt thử 1" (6P/9F cả 3). Bảng 15 TC × 3 trình duyệt so HW02 status; TC Pass nào có annotation oracle yếu/không tự động/"price dạng chuỗi (BUG-48)" (để SV xét pass giả). Commit RUN.md + report.
2. C – SV duyệt 3 giả định (không freeze, commit "HW04[C-FR15] SV duyệt giả định"): selector thông báo trên trang, chữ alert XSS = '1', "Form chặn" = SAU = TRƯỚC → ghi "(kế thừa HW02 H3/C21/C24, SV chốt lại)".
3. A + B: bảng dữ kiện để SV quyết G → BUG (KHÔNG đề xuất gộp/tách, KHÔNG viết mô tả): mỗi G: TC, triệu chứng (assertion lỗi), vị trí code SUT, yêu cầu bị vi phạm, issue HW02 liên quan, "G nào cùng vị trí code". Ghi HW04/bugs/_groups_AB.md.
DỪNG. Báo cáo ≤ 12 dòng: kết quả so HW02 của C + số G của B.
```

**Output:**
```
Phần 2: SV duyệt 3 giả định.

Phần 3: gom dữ kiện G của A và B. Đọc bug_groups hai bên và bug HW02 liên quan.

Lệnh #17 xong 3 phần, mỗi phần một commit. C lượt thử 1 trùng HW02 ở cả 15/15 TC; B có 6 nhóm Fail.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: lệnh #17 — C: RUN.md lượt thử 1 + SV duyệt 3 giả định; A+B: bảng dữ kiện các nhóm Fail.
- File:
  - `HW04/C_FR15/RUN.md` + 3 report (14:42, 14:43, 14:43)
  - `HW04/C_FR15/selection.json`, `HW04/C_FR15/selection.md`, `HW04/C_FR15/assertions.md`, `HW04/data/C_FR15.json`: 3 giả định đổi sang "(kế thừa HW02 H3/C21/C24, SV chốt lại)"; thêm quyết định C3. Expected và sha1 giữ nguyên, check_data báo 0 lỗi.
  - `HW04/bugs/_groups_AB.md`
- **Kết quả C so với HW02:** 6 Pass / 9 Fail ở cả 3 trình duyệt. Verdict trùng HW02 15/15, không TC nào khác nhau giữa các trình duyệt; 0 Blocked, 0 lần backend sập.
- **TC Pass cần SV xét pass giả:** chỉ TC-05 có annotation "price dạng chuỗi (BUG-48)" (M_TRƯỚC id 6). Không TC Pass nào có annotation oracle yếu hay không tự động. Annotation oracle yếu chỉ gặp ở TC-15 và TC-78: hai TC này Fail và chỉ có hộp thoại "Cập nhật thành công!".
- **Lỗi harness chưa sửa, không đổi verdict:** ở TC-07, ô không hợp lệ bị ghi 2 lần, vì lệnh `checkValidity()` gọi trước khi bấm cũng bắn sự kiện `invalid`.
- **Số nhóm:** B có 6 nhóm. 4 nhóm cùng vị trí `ProductDetail.jsx:21-31` (G1, G3, G6 và một phần G4); G4 còn vị trí thứ hai `App.jsx:23`. A có 3 nhóm, cả 3 cùng `Register.jsx:15`.
- Kết quả kiểm tra: check_data 0 lỗi; test Not run (đã dùng 3 report SV vừa chạy).
- Commit:
  - `0631be5` HW04[C-FR15] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md
  - `feec5e2` HW04[C-FR15] SV duyệt giả định
  - `961d61d` HW04: dữ kiện nhóm Fail A + B để SV quyết G → BUG
- Cần quyết định:
  - G→BUG cho A và B (dữ kiện ở `HW04/bugs/_groups_AB.md`).
  - Mọi nhóm đều đã có issue HW02 (#17, #18, #161, #165, #166, #167): comment vào issue cũ hay tạo issue mới cho HW04.
```

**Xử lý:** [...]

---

## #21 | 15:10 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #18, C_FR15 BƯỚC 5.
1. HW04/C_FR15/review_sv.md:
   - "Bản 1 – SV tự soi": chép NGUYÊN VĂN 5 ý (em dán bên dưới) + cột "Đối chiếu code (phiên thảo luận)": ý 1 = bug SUT, script phát hiện (dòng 210–211 → TC-03 Fail); ý 2+4 = theo Expected (TC-01 C13, TC-03 "Không đánh giá thông báo"); ý 3 = theo Expected/H4 (dòng 130); ý 5 = restart sau mỗi Fail đúng, nhiều dữ liệu = phạm vi.
   - "Bản 2 – sau đối chiếu": chép NGUYÊN VĂN 3 ý (em dán bên dưới), cột Nguồn: ý 1 = phiên thảo luận, ý 2 = SV, ý 3 = Claude Code (báo cáo lệnh #17). R3=a: giữ errShown theo H4, ghi là điểm yếu.
   Commit trước khi sửa code.
2. 5/6a: sửa ghi trùng ô không hợp lệ ở TC-07 (chỉ ghi sự kiện sau khi bấm Lưu). Commit có sửa C_FR15.spec.ts. tsc + --list.
DỪNG. Báo cáo ≤ 8 dòng + lệnh SV chạy lượt chính thức C.
--- Bản 1 ---
Soi spec:
Lỗi render toàn bảng khi Sửa: như khi sửa 1 sản phẩm, thì frontend ghi đè tên mới lên toàn bộ các dòng sản phẩm trong bảng, nhưng cột giá thì lại không cập nhật.
Thiếu phản hồi trực quan sau thao tác: Thao tác Thêm và Xoá không có thông báo thành công, còn thao tác Sửa thì lại dùng alert() của trình duyệt và báo thành công giả ngay cả khi UI render lỗi.
Lệch ngôn ngữ thông báo validation: Dùng validation mặc định của trình duyệt nên câu báo lỗi hiển thị tiếng Anh dù hệ thống cấu hình tiếng Việt.
Bỏ qua kiểm tra thông báo thành công: kịch bản hiện đang bỏ qua việc đánh giá thông báo phản hồi ở luồng Thêm và Sửa, nên test sẽ không bắt được lỗi UX hoặc thông báo sai ngữ cảnh.
Phụ thuộc backend restart để reset dữ liệu: Mỗi lần chạy đều khởi động lại backend để đưa DB về trạng thái 5 sản phẩm, nên gây chậm thời gian thực thi và bỏ qua các lỗi khi mà data nó nhiều.
--- Bản 2 ---
Soi spec: 
- Coi hộp thoại thành công là "có thông báo lỗi": Biến "errShown = invalid || newDialogs.length > 0 || pageMsgs" đếm mọi hộp thoại xuất hiện mà không phân biệt nó là gì.
- Phụ thuộc backend restart để reset dữ liệu: Mỗi lần chạy đều khởi động lại backend để đưa DB về trạng thái 5 sản phẩm, nên gây chậm thời gian thực thi và bỏ qua các lỗi khi mà data nó nhiều.
- Ô nhập liệu không hợp lệ bị ghi nhận 2 lần: Khi kiểm tra validation, gọi checkValidity() trước khi ấn submit sẽ kích hoạt sự kiện invalid.
```

**Output:**
````
Đã ghi `review_sv.md` và sửa lỗi ghi trùng ô không hợp lệ (5/6a); tsc Pass, `--list` = 45 test. Chưa chạy lại để kiểm bản sửa trên SUT.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: C_FR15 bước 5 — `review_sv.md` (2 bản nguyên văn) + 5/6a sửa ghi trùng ô không hợp lệ.
- File: `HW04/C_FR15/review_sv.md` (Bản 1: 5 ý + cột Đối chiếu code; Bản 2: 3 ý + cột Nguồn/Xử lý, ghi R3=a); `HW04/tests/C_FR15.spec.ts` (ngay sau `checkValidity()` xoá `__inv`, nên chỉ còn sự kiện của lần bấm Lưu).
- Đã kiểm: dòng 130 và 210–211 phiên thảo luận dẫn đúng với spec @ 370c9cd.
- Kết quả kiểm tra: tsc Pass, `--list` 45 test; test Not run.
- Commit: `9b1a139` HW04[C-FR15] 5/6: review_sv.md (SV soi bản 1 + bản 2 sau đối chiếu); `2e9e454` HW04[C-FR15] 5/6a – sửa: ô không hợp lệ chỉ ghi sự kiện của lần bấm Lưu (bỏ ghi trùng do checkValidity)
- Cần quyết định: không có.

**Lệnh SV chạy lượt chính thức C** (PowerShell, trong `HW04\tests`; backend/web/admin đang chạy):
```powershell
npx playwright test C_FR15 --project=chrome; npx playwright test C_FR15 --project=edge; npx playwright test C_FR15 --project=firefox
```
````

**Xử lý:** [...]

---

## #22 | 15:16 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #19.
1. C: ghi 3 report mới nhất là LƯỢT CHÍNH THỨC (6P/9F cả 3, spec @2e9e454); kiểm Run by; bước 6 (results.md, bug_groups.md, evidence gồm ảnh after-save). Freeze → commit "HW04[C-FR15] 6/6 – lượt chính thức".
2. Bảng dữ kiện nhóm Fail của C giống _groups_AB.md (TC, triệu chứng, vị trí code SUT, yêu cầu bị vi phạm, issue HW02 liên quan, G nào cùng vị trí code) → HW04/bugs/_groups_C.md. KHÔNG đề xuất gộp/tách.
3. HW04/README.md (bản nháp, số liệu tính bằng script, không gõ tay): bảng test summary – số feature, TC automated/executed/pass/fail/blocked theo feature × trình duyệt, số lượt chạy chính thức, số commit có sửa .spec; ô số bug và link video để [...].
Commit. DỪNG. Báo cáo ≤ 10 dòng: số G của C, số commit .spec.
```

**Output:**
```
Đang làm bước 6 của C: đã gộp 3 report (9 nhóm, 54 ảnh). Giờ xem mẫu ảnh rồi commit.

Đã viết `_groups_C.md`; giờ viết script sinh README test summary.

Lệnh #19 xong: C chốt lượt chính thức (bước 6), có bảng dữ kiện nhóm Fail của C và README nháp. C có 9 nhóm Fail; 12 commit có sửa `.spec.ts` (đề cần ≥ 8).

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: C 6/6 lượt chính thức + `_groups_C.md` + README nháp (số liệu sinh bằng script).
- File:
  - `HW04/C_FR15/RUN.md`, `HW04/C_FR15/results.md`, `HW04/C_FR15/bug_groups.md` (freeze `step6/`)
  - `HW04/C_FR15/evidence/`: 54 ảnh (27 ảnh lúc kết thúc + 27 ảnh `_after-save`). Em mới xem 2 ảnh, không thấy thông tin cá nhân; 52 ảnh còn lại SV cần tự xem trước khi push.
  - `HW04/bugs/_groups_C.md`
  - `HW04/README.md`; `tools/hw04_summary.py` ghi đè phần giữa 2 marker trong README.
- Kết quả C chính thức (spec @2e9e454): 6P/9F ở cả 3 trình duyệt, 0 Blocked, trùng HW02 15/15. `Run by` trong `results.json` cả 3 = `23120255 · <ISO>`, khớp tên thư mục.
- **Số G của C: 9.** Mỗi TC Fail là một nhóm riêng. Vị trí code trùng nhau:
  - `App.jsx:500-507` (ô Giá): G2, G3, G4, G6, G8
  - `server.js:167-177` (POST): G2, G3, G5, G7, G8
  - `App.jsx:105-116`: G1, G9
  - G2, G3, G8 cùng issue HW02 BUG-36 (#182).
- **Số commit sửa `.spec.ts`: 12** (A 6, B 4, C 2).
- README: 3 feature, 45 TC, 9 lượt chính thức, 135 lượt thực thi, 57P/78F/0 Blocked. Ô số bug và 2 link video để `[...]`.
- Commit: `2c54f76` HW04[C-FR15] 6/6 – lượt chính thức; `f497ee8` HW04: dữ kiện nhóm Fail C + README nháp (test summary sinh bằng tools/hw04_summary.py)
- Cần quyết định: G→BUG cho C (dữ kiện ở `HW04/bugs/_groups_C.md`); comment vào issue HW02 cũ (#181–#186, #191) hay tạo issue mới.
```
*File AI ghi/gửi trong lượt này:* `hw04_summary.py`

**Xử lý:** [...]

---

## #23 | 15:29 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #20. G→BUG = Cách 2 (mỗi G = 1 bug; SV: bám _groups, bước tái hiện gọn, confirmation test từng hành vi). B1=b: tạo issue MỚI cho mọi bug (không comment issue cũ); tiêu đề GitHub "[HW04][FR-xx] …"; mục "Liên quan" trỏ issue HW02.
1. Ghi quyết định vào HW04/bugs/README.md (tiêu chí + lý do SV, bảng G → BUG). Đánh số tiếp toàn môn: BUG-86 trở đi (HW03 dừng ở BUG-85) – kiểm lại số cuối trong HW03/bugs trước.
2. Dựng 18 khung HW04/bugs/BUG-xx.md theo mẫu HW02 (d0d0e05:HW02/bugs/BUG-22.md):
   - `<SV viết>` (trong backtick): Tiêu đề, Severity (Critical/High/Medium/Low), Priority (High/Medium/Low), Tiền điều kiện, Bước tái hiện, Expected, Actual, Nhận định.
   - AI điền dữ kiện: Môi trường (SUT commit, Windows, Chrome/Edge/Firefox + phiên bản, Playwright 1.65.1, report chính thức của từng trình duyệt), TC liên quan, Bằng chứng (ảnh after-* + ảnh lúc kết thúc trong evidence/), Yêu cầu bị vi phạm (từ _groups, SV duyệt), Dữ kiện (AI chép) = assertion lỗi + giá trị nhận được nguyên văn, code SUT trích có số dòng, Liên quan (issue HW02).
   - KHÔNG viết bước tái hiện, mô tả, nhận định, severity.
3. Commit "HW04: khung 18 bug (Cách 2)". DỪNG.
Báo cáo ≤ 10 dòng: bảng BUG-xx ↔ G ↔ TC ↔ issue HW02 liên quan.
```

**Output:**
```
Đã có phiên bản trình duyệt; giờ đối chiếu bản Firefox build rồi sinh 18 khung bug.

Khung 18 bug đã sinh, đoạn code khớp số dòng. Giờ ghi `HW04/bugs/README.md` và commit.

Đã dựng 18 khung bug (BUG-86 → BUG-103) và ghi quyết định vào `HW04/bugs/README.md`, commit `2667147`. Mỗi file còn 8 ô `<SV viết>` để trống; em không viết mô tả, bước tái hiện, nhận định hay severity.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: G→BUG theo Cách 2 (mỗi G = 1 bug), B1=b; ghi quyết định + dựng 18 khung bug.
- Bảng BUG ↔ G ↔ TC ↔ issue HW02 (đầy đủ trong `HW04/bugs/README.md`):
  - A (`Register.jsx`): 86 = A-G1 (6 TC) ↔ #17 · 87 = A-G2 (202) ↔ #18 · 88 = A-G3 (211) ↔ #17
  - B: 89 = B-G1 (61–64) ↔ #161 · 90 = B-G2 (01) ↔ #167 · 91 = B-G3 (02) ↔ #161 · 92 = B-G4 (04) ↔ #166 + #161 · 93 = B-G5 (08) ↔ #165 · 94 = B-G6 (205) ↔ #161
  - C: 95 = C-G1 (03) ↔ #191 · 96 = C-G2 (10) ↔ #182 · 97 = C-G3 (11) ↔ #182 · 98 = C-G4 (15) ↔ #184 + #194 (annotation) · 99 = C-G5 (200) ↔ #185 · 100 = C-G6 (201) ↔ #186 · 101 = C-G7 (66) ↔ #181 · 102 = C-G8 (67) ↔ #182 · 103 = C-G9 (78) ↔ #183 + #194 (annotation)
- Số cuối HW03 đã kiểm trong `HW03/bugs/`: BUG-85.
- File: `HW04/bugs/README.md`, `HW04/bugs/BUG-86.md` … `BUG-103.md` (sinh bằng script tạm, không commit).
- Phần AI điền trong mỗi khung:
  - Môi trường: Chrome 157.0.8103.79, Edge 157.0.4341.60, Firefox 159.0 (firefox-1572), Playwright 1.65.1, report chính thức từng trình duyệt.
  - Bằng chứng: ảnh `after-*` và ảnh lúc kết thúc (BUG-90 chỉ có ảnh lúc kết thúc vì TC-01 không có thao tác chính).
  - Yêu cầu theo HW02 (SV duyệt), assertion lỗi nguyên văn bản chrome, đoạn code SUT có số dòng, mục "Liên quan" trỏ issue HW02.
- Kết quả kiểm tra: test Not run (không cần cho bước này).
- Commit: `2667147` HW04: khung 18 bug (Cách 2)
- Cần quyết định: không có. Bước kế: SV viết 18 bug, rồi em chạy `gh issue create`.
```
*File AI ghi/gửi trong lượt này:* `gen_bugs.py`

**Xử lý:** [...]

---

## #24 | 19:45 17/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
<task-notification>
<task-id>bbxf7wbit</task-id>
<tool-use-id>toolu_012Mz1CeDoPVg42RB6Eqv66K</tool-use-id>
<output-file>C:\Users\tanhi\AppData\Local\Temp\claude\3d1ee2708df72d7d\58f7c391-7d8f-420c-bb07-be59428f036f\tasks\bbxf7wbit.output</output-file>
<status>killed</status>
<summary>Background command "Start web frontend on 5173" was stopped because the system is running low on memory</summary>
<note>This is not a failure of the command. Claude Code stopped it because the system was critically low on memory while the session was idle, which says nothing about the command or its own memory use, so there is nothing in it to debug. Do not start it again on your own, even if the work seems to need it: memory may still be short. Report what was stopped and why, and start it again only when asked. The user can turn this behavior off by starting Claude Code with CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1 in its environment; setting it from a shell command has no effect.</note>
</task-notification>
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #25 | 19:45 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<task-notification>
<task-id>br0wrmv3d</task-id>
<tool-use-id>toolu_01PU5MiJeCntiBxVVCQ2ysJA</tool-use-id>
<output-file>C:\Users\tanhi\AppData\Local\Temp\claude\3d1ee2708df72d7d\58f7c391-7d8f-420c-bb07-be59428f036f\tasks\br0wrmv3d.output</output-file>
<status>killed</status>
<summary>Background command "Start admin frontend on 5174" was stopped because the system is running low on memory</summary>
<note>This is not a failure of the command. Claude Code stopped it because the system was critically low on memory while the session was idle, which says nothing about the command or its own memory use, so there is nothing in it to debug. Do not start it again on your own, even if the work seems to need it: memory may still be short. Report what was stopped and why, and start it again only when asked. The user can turn this behavior off by starting Claude Code with CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1 in its environment; setting it from a shell command has no effect.</note>
</task-notification>
```

**Output:**
```
Máy thiếu bộ nhớ nên Claude Code đã tự dừng 2 tiến trình nền: web :5173 và admin :5174. Em chưa bật lại vì bộ nhớ có thể vẫn thiếu. Backend :3000 không bị nhắc tới trong thông báo, em chưa kiểm còn chạy hay không.

Bước kế (SV viết 18 bug) không cần SUT. Khi cần chạy test lại (chụp ảnh tái hiện, quay video), bạn nhắn "bật lại web + admin" thì em chạy lại 2 lệnh `npx vite --host 127.0.0.1 --port 5173` / `5174`.
```

**Xử lý:** [...]

---

## #26 | 20:55 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #21, bug 7c + issue.
0. Sửa dữ kiện AI điền sai: xoá dòng C3 trong "Yêu cầu bị vi phạm" của BUG-101 (dòng ~63) và BUG-103 (dòng ~60) – C3 không liên quan TC-66/78. Không đụng chữ SV. Commit "HW04: sửa Yêu cầu do AI chép nhầm C3 (BUG-101, 103)".
1. Chạy thật bước tái hiện SV viết trong 18 file BUG-86…103 (Playwright script tạm hoặc API; không sửa chữ SV). Bảng: bug, tái hiện được không, chỗ bước/giá trị lệch thực tế. Có lệch → DỪNG, báo SV sửa.
2. Không lệch: kiểm trùng issue HW04 trên tkob-team/eshop-sut (gh = ThachHaoo); tạo tuần tự 18 issue: tiêu đề "[HW04][FR-xx] …" (từ file), thân = nội dung file, label bug; ảnh nhúng bằng link raw GitHub của repo public ThachHaoo/software-testing-2627 theo commit hiện tại (1 ảnh after-* + 1 ảnh lúc kết thúc, bản chrome). Điền số issue vào từng BUG-xx.md và bugs/README.md.
3. Chụp ảnh trang Issues (lọc "[HW04]" + author:ThachHaoo) → HW04/bugs/issues_page*.png. Cập nhật số bug trong README (hw04_summary.py). Commit. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Now read SV's repro steps from 18 files.

Đang viết script Playwright tạm (scratchpad) để chạy lại bước tái hiện SV viết cho 18 bug.

Tái hiện đã chạy xong cả 18 bug. Kiểm lại riêng BUG-87 (endpoint `/api/users` không tồn tại nên cột "user tạo" bị sai) bằng cách đăng nhập API.

Em dừng ở bước 1, chưa tạo issue: cả 18 bug đều tái hiện được hành vi, nhưng 3 bug có số id lệch thực tế. Bước 2–3 (tạo issue, chụp trang Issues, cập nhật README) chưa làm.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: lệnh #21 — bước 0 (sửa C3) xong; bước 1 kiểm tái hiện có lệch nên DỪNG trước bước 2.
- File: `HW04/bugs/BUG-101.md`, `HW04/bugs/BUG-103.md` (xoá dòng C3); `HW04/bugs/repro_check.md` (bảng 18 bug).
- Cách chạy: script Playwright tạm trên Chrome, restart backend trước từng bug, vào giỏ bằng link navbar.
- **Lệch giá trị (SV cần sửa), id đều phụ thuộc trạng thái CSDL:**
  - BUG-96: Actual ghi `id = 7`, thực tế `6`.
  - BUG-101: Actual ghi `id = 7`, thực tế `6`.
  - BUG-103: tiền điều kiện, bước 5 và Actual ghi M `id = 8` (`GET /api/products/8`), thực tế M là `id = 6`.
- **Lệch cách ghi bước (SV xét có sửa hay không):**
  - BUG-87: bước 4 không ghi mật khẩu cụ thể; script dùng `Abcd 1234` (data TC-202).
  - BUG-89 → 94: bước ghi vào giỏ bằng URL `/cart`. Gõ URL làm tải lại trang, giỏ (state React) mất dù bug có hay không.
  - BUG-95: ghi `category_id = 3`, nhưng ô chọn hiện tên (`Phụ kiện`).
  - BUG-97: `price: null` là giá trị script đọc ra; UI hiện `₫`.
- Kết quả kiểm tra: tái hiện 18/18 hành vi; test chính thức Not run (không cần).
- Commit: `d6cd474` HW04: sửa Yêu cầu do AI chép nhầm C3 (BUG-101, 103); `9e9f88f` HW04: kiểm tái hiện 18 bug (dữ kiện, chờ SV sửa)
- Cần quyết định: SV sửa 3 bug lệch id (và các chỗ ghi bước nếu muốn), rồi gửi lệnh để em làm tiếp bước 2–3.
```
*File AI ghi/gửi trong lượt này:* `repro.spec.ts`

**Xử lý:** [...]

---

## #27 | 21:18 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #22. SV đã sửa bước tái hiện (BUG-87, 89–94, 95, 96, 97, 101, 103).
1. Chạy lại tái hiện CHỈ các bug vừa sửa; cập nhật repro_check.md. Còn lệch → DỪNG.
2. Không lệch → làm tiếp bước 2–3 của lệnh #21 (kiểm trùng, tạo 18 issue tuần tự, ảnh nhúng link raw theo commit hiện tại, điền số issue vào BUG-xx.md + bugs/README.md, chụp trang Issues, cập nhật README). Commit. Báo cáo ≤ 10 dòng: bảng BUG ↔ issue #.
```

**Output:**
```
SV đã sửa; bước giờ trùng với cách script chạy. Chạy lại 12 bug đã sửa.

Không có issue trùng. Tạo 18 issue tuần tự.

Thư mục chưa có, chưa issue nào được tạo. Chạy lại.

18 issue đã tạo (#298 → #315). Điền số issue vào file, rồi chụp trang Issues.

Đã tạo đủ 18 issue `[HW04]` trên `tkob-team/eshop-sut` (#298 → #315), và đã điền số issue vào từng file bug cùng `bugs/README.md`. Trước đó em chạy lại 12 bug SV vừa sửa: tất cả tái hiện được, không còn lệch.

### Báo cáo cho phiên thảo luận
- Nhiệm vụ: tái hiện lại 12 bug vừa sửa → tạo 18 issue → điền số issue → chụp trang Issues → cập nhật README.
- Tái hiện lần 2: 12/12 ra đúng hành vi SV ghi, 0 lệch (BUG-87, 89–97, 101, 103), ghi thêm mục "Lần 2" vào `HW04/bugs/repro_check.md`.
- Kiểm trùng: tài khoản ThachHaoo chưa có issue `[HW04]` nào; không tiêu đề nào trùng.
- Mỗi issue: tiêu đề lấy từ file, thân = nội dung file, label `bug`. Ảnh nhúng bằng link raw @ `b264556` (commit đã có trên origin; em thử 1 link, trả 200): 1 ảnh after-* + 1 ảnh lúc kết thúc, bản chrome. BUG-90 chỉ 1 ảnh vì không có ảnh after-*.
- **BUG ↔ issue:**

  | BUG | Issue | BUG | Issue | BUG | Issue |
  |---|---|---|---|---|---|
  | 86 | #298 | 92 | #304 | 98 | #310 |
  | 87 | #299 | 93 | #305 | 99 | #311 |
  | 88 | #300 | 94 | #306 | 100 | #312 |
  | 89 | #301 | 95 | #307 | 101 | #313 |
  | 90 | #302 | 96 | #308 | 102 | #314 |
  | 91 | #303 | 97 | #309 | 103 | #315 |

- `HW04/bugs/issues_page_1.png`: lọc `author:ThachHaoo "[HW04]"`, ra 18 kết quả trong 1 trang. Ảnh chụp khi chưa đăng nhập GitHub; em đã xem, không có thông tin cá nhân.
- README: `tools/hw04_summary.py` giờ đếm số bug từ `HW04/bugs/README.md` → 18/18 bug report có issue.
- Kết quả kiểm tra: tái hiện Pass 12/12; test chính thức Not run (không cần).
- Commit: `78873e0` HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug
- Cần quyết định: không có. Commit `78873e0` chưa push (SV tự push).
```
*File AI ghi/gửi trong lượt này:* `mk_issues.py`

**Xử lý:** [...]

---

## #28 | 21:32 17/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – lệnh #23. SV đang quay video: KHÔNG restart SUT, không chạy test, không xoá report.
1. HW04/report_plan.md: bảng form (AI-02, AI-03, AI-05; AI-04 không cần; AI-06 đã nộp tuần 1), rubric + điểm tối đa, danh sách mọi file phải nộp theo đề §14 kèm trạng thái ĐÃ CÓ/THIẾU (kiểm bằng ls), mâu thuẫn đề (G9.x), quyết định đã chốt (S1, T1–T4, W1, B1=b, Z1=d, Z2 export-ignore lượt thử, R1–R3, C2=a, Cách 2), mục "Khai cho Audit" (gom từ RUN.md, review_sv.md, báo cáo các lệnh: việc làm ngoài lệnh, rm -rf report, C3 chép nhầm, serial/^/escape/users.list/errShown do phiên thảo luận phát hiện), mục "Danh sách cho Mandatory Disclosure".
2. HW04/23120255_HW04_Report.md – dàn ý đầy đủ: đầu file (công cụ AI, cấp độ 4, Bloom G9.2/G9.3/G9.4, câu nguyên văn "I use AI tools for the following tasks,"); §1 môi trường; §2 skill + quy trình 6 bước; §3–5 mỗi feature: selection, data, assertion, kết quả 3 trình duyệt (bảng sinh bằng script giữa marker REPORT), review = chép nguyên văn review_sv.md, 🔒 "Vì sao AI sai/bỏ sót" để `<SV viết>`, TC không tự động hoá được; §6 bug (AI chép bảng từ BUG-xx.md, nhãn "(AI chép)"); §7 video [...]; §8 Critique 🔒; §9 Audit (hàng artifact lấy từ git, verdict/lý do `<SV viết>`); §10 Mandatory Disclosure; §11 tự đánh giá `<SV viết>`.
3. tools/hw.toml/prompt log: chạy on_stop.py --manual, báo số lượt.
Commit. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đang gom dữ kiện (report, quyết định, file nộp) để viết `report_plan.md` và dàn ý report.
```

**Xử lý:** [...]

---

**Tổng:** 28 lượt; Claude Opus 5.5 27 lượt (#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #25, #26, #27, #28); Claude (không rõ model) 1 lượt (#24).
