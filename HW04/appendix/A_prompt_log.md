# Prompt Log – HW04
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude Opus 5.5

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
```
*File AI ghi/gửi trong lượt này:* `select_tc.py`, `check_data.py`, `freeze.py`, `merge_reports.py`, `ddt-fixture.template.ts`, `spec.template.ts`, `selection.example.json`, `SKILL.md`, `selection.json`

**Xử lý:** [...]

---

**Tổng:** 2 lượt; Claude Opus 5.5 2 lượt (#1, #2).
