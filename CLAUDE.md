# CLAUDE.md — repo bài tập Software Testing (CS423 / CSC13003, AI-first)

Repo này chứa bài nộp của **Lê Tấn Hiệp – MSSV 23120255 – lớp Software Testing 23_3** (mỗi bài một thư mục `HWxx/`). Báo cáo viết **tiếng Việt**, sinh viên xưng **"em"**. Vai trò của Claude: **Software Testing Senior**, làm từng bước, góp ý ngắn gọn, thẳng thắn, không tâng bốc. Người dùng muốn **AI làm tối đa phần lặp lại/tính toán, người chỉ review, đánh giá, sửa** — nhưng luôn trong giới hạn ở mục 3.

## Vai trò của phiên Claude Code này: người thực hiện

Việc thảo luận, lên kế hoạch, review và hướng dẫn diễn ra ở **phiên claude.ai "Homework Testing Software"** (gọi tắt: *phiên thảo luận*). Phiên Claude Code này **thực hiện**: đọc mã SUT, chạy skill, chạy script/test, sửa file, commit.

- Nhiệm vụ thường đến dưới dạng khối **"Lệnh cho Claude Code"** dán từ phiên thảo luận. Làm đúng phạm vi khối lệnh; gặp chỗ mơ hồ hoặc quyết định không đảo ngược được thì hỏi lại, không tự mở rộng phạm vi.
- Quyết định mới từ phiên thảo luận được ghi vào mục "Quyết định đã chốt" bên dưới; đọc lại mục này đầu mỗi phiên.
- **Kết thúc mỗi nhiệm vụ** bằng một khối ngắn (≤ 25 dòng) để người dùng dán ngược
  về phiên thảo luận:

  ```
  ### Báo cáo cho phiên thảo luận
  - Nhiệm vụ: …
  - File đã tạo/sửa: …
  - Kết quả kiểm tra: check_domain …, lint …, test … (Pass/Fail/Not run)
  - Commit: <hash> <message>
  - Cần quyết định / câu hỏi: …
  ```

  Quy tắc cho khối báo cáo:
  - Nội dung dài (trích SRS, bảng biến/lớp/TC, khảo sát SUT, danh sách giả định)
    ghi vào file trong thư mục feature; báo cáo chỉ nêu đường dẫn. Kể cả khi lệnh
    yêu cầu "báo cáo X", hãy hiểu là ghi X vào file rồi trỏ tới.
  - "Cần quyết định" chỉ liệt kê điểm chặn bước kế tiếp, mỗi điểm 1 dòng:
    mã – câu hỏi – các phương án. Điểm không chặn thì ghi số lượng + đường dẫn file.
  - Bất thường mới phát hiện (SUT, harness): mỗi điểm 1 dòng, kèm file:dòng.
  - Không dùng bảng kẻ khung (┌─┐); dùng gạch đầu dòng hoặc bảng markdown.

## 0. Đọc gì trước khi làm

1. File này.
2. Skill khoá học **`cs423-ai-first-homework`** (đồng bộ từ tài khoản claude.ai) — luật AI-01, Homework Policies, biểu mẫu AI-02→AI-06. Nếu `/skills` không thấy skill này, báo người dùng ngay (có thể chưa đăng nhập bằng tài khoản claude.ai).
3. `context/HW01_lessons.md` — bài học rút ra từ HW01 (riêng quy tắc prompt log đã đổi, xem mục 4).
4. Đề bài hiện tại: `context/HW02_assignment.md`.
5. Bài giảng: `context/private/*.pdf` (slide Domain Testing; không commit).

Skill dùng trong repo:

| Skill | Nguồn | Dùng khi |
|---|---|---|
| `cs423-ai-first-homework` | đồng bộ từ claude.ai | mọi việc của môn |
| `test-design-istqb` | đồng bộ từ claude.ai | chọn kỹ thuật, oracle, rubric audit TC |
| `hw-submission-audit` | đồng bộ từ claude.ai | rà soát trước khi nộp |
| `qa-evidence-review` | đồng bộ từ claude.ai | trước khi kết luận Pass/Fail/bug |
| `domain-bva-testing` | `.claude/skills/` (bài nộp Agent Skill của HW02) | Domain + BVA từng bước |
| `test-case-writing` | `.claude/skills/` (của giảng viên, giữ nguyên) | schema JSON, linter, xuất Word/Excel nếu cần |

## 1. HW02 – Domain Testing on EShop (đang làm)

**Đề:** với mỗi feature: (1) Domain Testing có AI hỗ trợ, giải thích từng bước; (2) BVA, giải thích từng bước; (3) AI gap analysis — case/bug AI bỏ sót và **vì sao** (prompt, giới hạn công cụ, độ phức tạp feature); (4) báo bug trong report **và** GitHub Issues của nhóm (có ảnh). Agent Skill + video YouTube demo end-to-end. Bloom-AI G9.2 + G9.3. Cấp độ AI: **Cấp 4**.

**Bảng điểm:** A 25 · B 25 · C 25 · D (Mobile) 15 · Agent Skills 10 = 100.

**Nộp** `23120255_HW02_AI_DomainTesting_<ggg>.zip` (ggg = tổng tự đánh giá, 3 chữ số), gồm: report chính .md + PDF (Domain + BVA); bug report + ảnh chụp trang GitHub Issues; AI Critique (200–300 từ) + AI Audit Report (.md + PDF); commit log (text); `README.md` có bảng tự đánh giá + test summary (số feature; số TC thiết kế/đã chạy/pass/fail/chưa chạy; số bug; link video); tài liệu khác. **Thiếu tài liệu bắt buộc = 0 điểm. Chép prompt giữa sinh viên = 0 điểm cả hai** → không chia sẻ skill/prompt với bạn cùng nhóm. Nộp trễ không nhận. Moodle ≤ 20 file, mỗi file ≤ 20 MB.

**Feature đã chọn** (không trùng trong nhóm; nhóm đã có FR-04, FR-09, FR-14):

| Pool | Feature | Thư mục | Ghi chú |
|---|---|---|---|
| A | FR-01 Đăng ký tài khoản | `HW02/A_FR01/` | web `frontend-web` + API `POST /api/register` |
| B | FR-07 Giỏ hàng | `HW02/B_FR07/` | SRS không nêu cận trên số lượng → phải ghi giả định |
| C | FR-15 Quản lý sản phẩm (CRUD, admin) | `HW02/C_FR15/` | `frontend-admin` + API `/api/products` |
| D | FR-20 – chức năng **Đăng ký trên Mobile** (áp dụng FR-01) | `HW02/D_FR20/` | kế thừa mô hình miền của A; chạy tay trên Expo Go; mã TC riêng `TC-FR20-xx`; thêm bảng so sánh web vs mobile |

**Test basis:** `../eshop-sut/README.md` (SRS v2.0 — mục FR-01, FR-07, FR-15, FR-20, FR-21…24 GUI, SEC-xx), `../eshop-sut/api_specification.md`, mã nguồn `../eshop-sut/{frontend-web,frontend-admin,frontend-mobile,backend}`. SRS là oracle; code chỉ để biết tên trường/nhãn/endpoint thật. Mở thư mục SUT bằng `/add-dir ../eshop-sut` nếu chưa truy cập được.

**SUT & môi trường** (ghi vào `HW02/env/environment.md`):
- SUT = fork nhóm `tkob-team/eshop-sut` @ **`de0f48f`** (= repo gốc `ttbhanh/eshop-sut` commit `85af3ba` + `.gitignore`, không đổi mã). GitHub Issues của nhóm ở fork này; Issues trên fork phải được bật trong Settings.
- Chạy trên **Windows (PowerShell), không chạy trong WSL2**. Backend :3000, web :5173, admin :5174.
- Tài khoản: admin `admin@eshop.com` / `Admin123!` (setup_guide ghi `admin123` — sai so với seed), user `test@eshop.com` / `Test1234!`.
- **Mỗi lần `node server.js` khởi động, CSDL bị xoá và seed lại**; giỏ hàng nằm trong RAM (`userCarts`). Restart backend = mất tài khoản/sản phẩm/giỏ đã tạo. Viết precondition và cleanup theo đặc điểm này.
- Mobile: Expo **SDK 54** (Expo Go bản SDK 54), sửa `frontend-mobile/App.js` dòng 16 `API_URL` thành IP LAN của máy; lưu thay đổi bằng `git diff > HW02/env/mobile_api_url.patch` (trong repo SUT). Điện thoại và máy cùng Wi-Fi (Wi-Fi trường có thể chặn → dùng hotspot).

**Biểu mẫu AI cho HW02:** AI-02 Audit Report (bắt buộc, .md + PDF) · AI-03 Disclosure (bắt buộc) · AI-05 Privacy Checklist (bắt buộc, làm cuối) · AI-04 không cần · AI-06 đã nộp tuần 1 · Mantis **thay bằng GitHub Issues** theo đề · Excel **không yêu cầu** (test summary nằm trong README). File đặt ở `HW02/ai-forms/`.

**Quyết định đã chốt:**
- 2026-10-19: HW02 nằm trong repo này; SUT clone riêng ở thư mục cạnh repo, không chép vào repo.
- 2026-10-19: Prompt log **trích tự động bằng script** (mục 4); sinh viên tự ghi Section/Mục đích/Xử lý; khai trong Disclosure.
- 2026-10-19: BVA theo **mô hình 9 điểm của slide** (LB−1, LB, LB+1, NOM, UB−1, UB, UB+1, MIN_UI, MAX_UI); ghi rõ trong report.
- 2026-10-19: Test case lưu trong `testcases.json` theo schema `test-case-writing` + mở rộng `domain`; bảng .md sinh từ JSON.
- 2026-10-19 (A_FR01 review bước 1): email trùng so sánh **có phân biệt hoa/thường** và **cắt khoảng trắng đầu/cuối** (A3); expected của case tuân theo giả định này. Giữ A5 (tập ký tự đặc biệt đóng), A8 (xác nhận mật khẩu chỉ kiểm ở UI), A1/A4 (không có cận trên; MIN_UI/MAX_UI xét ở bước 4).
- 2026-10-19 (A_FR01 phạm vi): giữ FR-22.1–22.4, kiểm bằng suite GUI riêng, không phân lớp; bỏ FR-21 và SEC-01 khỏi phạm vi.
- 2026-10-19: SUT = `tkob-team/eshop-sut` @ `de0f48f` (= `ttbhanh/eshop-sut` `85af3ba` + `.gitignore`, không đổi mã); ghi ở `meta.sut_version` và `HW02/env/environment.md`.
- 2026-10-19: Dải mã TC mỗi feature — TS-DOM 01–59, TS-BVA 60–89 (tràn thì từ 100), TS-GUI 90–99, TS-SV (SV bổ sung) từ 200.
- Transcript ghi nhận các lượt #1–#3 của session cloud ngày 12/10 do Claude Sonnet 4.6 trả lời, các lượt sau Claude Opus 5.5 → AI-03 khai cả hai.
- 2026-10-20 (từ A_FR01) Verdict: lệch do biến mục tiêu → Fail; do biến khác chặn → Blocked, ghi case gốc trong notes (A20); `auto_status` giữ kết quả tự động gốc; "Pass hộp đen" (ghi notes) khi bị từ chối đúng nhưng lý do không chứng minh luật mục tiêu.
- A17: thiếu trường SRS yêu cầu → 1 case kiểm sự tồn tại (Fail), các case phụ thuộc trường đó Blocked.
- Case "UI+API" phải tách thành 2 case (mỗi tầng một case); expected của case API không chứa yếu tố UI.
- Chỉ đổi Expected sau khi có Actual khi điểm quan sát không tồn tại; ghi lý do vào notes.
- Evidence: tên `TC-xx_ui/_api/_req/_res/_failed/_manual_*`; bỏ trace .zip; evidence gốc không che đường dẫn (bản che để dán issue: `bugs/_issue_redacted/`).
- Bug: `BUG-xx` đánh số liên tục toàn HW02 (kế tiếp: xem dòng "BUG kế tiếp" ở cuối mục); Severity Critical/High/Medium/Low, Priority High/Medium/Low (`bugs/README.md`).
- Bước 7: AI gom dữ kiện → SV chốt danh sách bug → AI dựng khung (chỉ dữ kiện) → SV viết → AI sửa dữ kiện theo evidence, đánh dấu "(chưa kiểm chứng)" → kiểm trùng issue → `gh issue create` bằng tài khoản SV, tiêu đề `[FR-xx] <tiêu đề>`, `--label bug`.
- Tài khoản GitHub của SV: `ThachHaoo` (tên hiển thị TonKnight).
- 2026-10-20 (rút ra từ B_FR07):
  - Thiết kế TC:
    - Thuộc tính chung (nhãn, định dạng tiền, badge, phản hồi khi thêm) chỉ khẳng định ở **một** case.
    - `ec_target` ⊆ covers = lớp vào cần thử + lớp ra mà Expected khẳng định; truy vết sinh từ `ec_target`.
    - Phần không đổi ghi tương đối (SAU = TRƯỚC); giá trị tuyệt đối chỉ cho đầu ra case thực sự kiểm.
    - SRS im lặng và chưa có giả định → không đặt Expected/không tạo Fail; SV chốt giả định trước. Giả định quyết Expected mới → vào `assumptions` của case và truy vết.
  - BVA: không có cận trên → biến khai `no_upper_bound: "<mã giả định>"`, dùng điểm `LARGE` (case phải có mã đó trong `assumptions`).
  - Case SV: `technique` (EG…) + `approach: "gray-box"` khi chọn từ mã nguồn.
  - A20 mở rộng:
    - "Pass hộp đen" ghi case gốc khi đường thêm/nhập hỏng làm case từ chối đúng một cách ngẫu nhiên.
    - Case có thể có 2 case gốc, ghi cả hai.
  - Chạy test:
    - `merge_results.py` không ghi đè status SV đã chỉnh (`--force` mới ghi đè).
    - results mỗi lượt có timestamp.
    - evidence chỉ giữ lượt mới nhất.
    - Nhật ký lượt chạy ghi ở `RUN.md` + notes suite; lượt chính thức = lượt chạy toàn bộ sau restart backend.
  - Bug:
    - Format theo `bugs/BUG-14.md`.
    - Mục **Yêu cầu chỉ ghi yêu cầu/giả định bị vi phạm theo Actual**, kèm dòng "Đạt trong cùng case" / "Chưa đánh giá được" / "Không áp dụng"; yêu cầu ngầm định ghi "(ngầm định)".
    - Nhận định về tác động phải có dữ kiện (code/evidence).
    - SV commit bản viết (`7/7b`) trước khi AI sửa dữ kiện (`7/7c`).
    - File dữ kiện `bugs/_groups_<X_FRnn>.md`.
    - Tiền tố issue chỉ thêm trên GitHub = FR của feature đang kiểm (không ghi vào .md).
    - Ảnh trang Issues: `bugs/issues_page_<X_FRnn>.png`.
    - BUG kế tiếp: **BUG-51**; issue kế tiếp ≥ **#197**.
  - Checklist bước tái hiện (AI chạy thật trước khi tạo issue):
    - Web: giỏ là state React → điều hướng bằng link navbar, không gõ URL/tải lại; tiền điều kiện có bước dựng dữ liệu.
    - Windows PowerShell 5.1: tài khoản seed `test@eshop.com`; `-ContentType` ở tham số (không trong `-Headers`); `-Body ([Text.Encoding]::UTF8.GetBytes($body))`; `Invoke-WebRequest -UseBasicParsing`; lỗi 4xx/5xx đọc body bằng `try/catch` + `GetResponseStream()` (đặt `Position = 0`).
- 2026-10-20 (rút ra từ C_FR15):
  - Khung bug = mẫu B (`d0d0e05:HW02/bugs/BUG-22.md`): chỗ SV viết ghi `` `<SV viết>` `` (trong backtick); Môi trường gạch đầu dòng giá trị thật; Yêu cầu do AI điền từ `_groups`; Dữ kiện chỉ gồm Actual nguyên văn + dòng "Lặp lại" + code trích; không chép Expected.
  - 7a không soạn bước tái hiện thay SV; AI chỉ chạy bước SV viết ở 7c. Gặp bất thường ngoài bước SV → báo, ghi "AI phát hiện".
  - Giả định phạm vi (vd C8) và giả định nới (vd C17) không bao giờ vào "yêu cầu bị vi phạm".
  - Harness UI: đọc validity HTML5 ngay khi bấm (bài học H1); ghi mọi kênh thông báo (hộp thoại, bong bóng, chữ trên trang); không phân loại thông báo theo chữ của SUT.
  - Vá harness → chạy lại toàn bộ thành **một** lượt chính thức; `merge --force` chỉ khi không có status SV đặt.
  - Lệnh có chỗ `<...>` chưa điền → DỪNG, hỏi.

**Việc còn mở:** repo bài nộp đang public và chưa chuyển private được → **commit cục bộ, chỉ `git push` sau hạn nộp** (commit vẫn giữ giờ gốc, commit log xuất từ máy); không push `.transcripts/`; hỏi thầy có skill `domain-testing-design` đi kèm `test-case-writing` không; deadline trên Moodle.

## 2. Quy trình mỗi feature — 7 bước, mỗi bước một commit

Đề yêu cầu dẫn AI qua **từng bước** của kỹ thuật (không một prompt "sinh test case và tìm bug") và **mỗi bước của mỗi feature một commit**. Dùng skill `domain-bva-testing`, mỗi lần gọi một bước, xong thì **dừng** chờ người dùng review.

| Bước | Ai làm | Việc | Commit message |
|---|---|---|---|
| 1 | AI → SV review | Biến vào/ra (+ khởi tạo `testcases.json`) | `HW02[A-FR01] 1/7: Phân tích biến vào/ra` |
| 2 | AI → SV review | Lớp tương đương (Complete Set of Partitions) | `HW02[A-FR01] 2/7: Phân lớp tương đương` |
| 3 | AI → SV review | TC Domain (coverage + minimum set) | `HW02[A-FR01] 3/7: Test case Domain` |
| 4 | AI → SV review | TC BVA | `HW02[A-FR01] 4/7: Test case BVA` |
| 5 | **SV** 🔒 rồi hỏi AI | SV tự thêm case còn thiếu (`TS-SV`, `origin: Human`) **trước**, sau đó mới hỏi AI vì sao bỏ sót | `HW02[A-FR01] 5/7: SV bổ sung TC + gap analysis` |
| 6 | AI viết script, **SV chạy** | Playwright/API trên máy SV → `merge_results.py`; mobile chạy tay | `HW02[A-FR01] 6/7: Chạy test, cập nhật Actual/Verdict` |
| 7 | **SV** 🔒 | Bug report (`HW02/bugs/BUG-xx.md`) + GitHub Issue có ảnh | `HW02[A-FR01] 7/7: Bug report + GitHub Issues` |

Sau mỗi bước AI (1–4): chạy `freeze.py` để đóng băng bản nháp vào `HW02/appendix/ai-outputs/` **trước** khi SV sửa; chạy `check_domain.py`, linter của giảng viên, `render_md.py`. Commit chung khác: `HW02: …` (dàn ý, audit, form, README, nộp).

## 3. Giới hạn của AI (vi phạm = rủi ro 0 điểm)

- **Không** gợi ý edge case/boundary/security case trong lúc SV đang tự tìm (bước 5). Khi được hỏi "vì sao bỏ sót": trung thực, tách *đã nghĩ tới nhưng không đưa vào output* với *không nghĩ tới*.
- **Không** viết hoặc nháp mô tả bug (tóm tắt, steps, expected/actual) — kể cả bảng bug trong report và nội dung GitHub Issue. Chỉ kiểm tra trường thiếu, severity/priority. Được chạy `gh issue create --body-file` với file **SV đã viết**.
- **Không** viết hộ: AI Critique, phần phân tích "vì sao AI bỏ sót" trong report, verdict cuối của Audit. Chỉ góp ý chỗ khẳng định quá mức, đếm từ.
- **Không** tạo: giọng thuyết minh video, screenshot có username/hostname thay SV, chữ ký, tick các mục cam kết cá nhân trong AI-05.
- **Không** sửa file trong `HW02/appendix/ai-outputs/` và **không** sửa tay `A_prompt_log.md` (đã chặn trong `.claude/settings.json`).
- **Không** bịa nguồn, số liệu, tên trường/nút/endpoint; Expected suy ra từ SRS; chỗ SRS im lặng → ghi giả định.
- **Không** tự đổi Expected sau khi có Actual. Không kết luận bug trước khi cô lập nguyên nhân (chạy lại, reset dữ liệu, so UI với API).
- Mọi lượt AI làm "việc phụ" (dàn ý, script, form, README, sửa nhất quán) đều là artifact phải khai trong Audit/Disclosure. Bản thân harness này (CLAUDE.md, skill, script) cũng do AI hỗ trợ tạo → khai trong Audit.

## 4. Prompt log (tự động)

- Hook **Stop** (`.claude/settings.json` → `tools/hooks/on_stop.py`) chạy sau mỗi lượt: chép transcript vào `.transcripts/` (gitignore, không nộp) rồi tái tạo `HW02/appendix/A_prompt_log.md` bằng `tools/extract_prompt_log.py`. Script chỉ chép nguyên văn, lọc khối hệ thống, giờ Asia/Saigon, ghi model của từng lượt.
- SV tự ghi **Section / Mục đích / Xử lý** trong `HW02/appendix/prompt_log_notes.toml`; lượt dùng công cụ khác (Gemini, ChatGPT…) chép nguyên văn vào `prompt_log_extra.toml`.
- Transcript session cloud (claude.ai) do người dùng tải về, đặt vào `.transcripts/`.
- Chạy tay: `python tools/hooks/on_stop.py --manual`. Xem số lượt: `python tools/extract_prompt_log.py .transcripts/*.jsonl --since 2026-10-12 --list`.
- Log sai → sửa script/ghi chú rồi trích lại; không sửa tay output. Trước khi nộp: trích lại lần cuối, đếm lượt, cập nhật số liệu ở report, Audit, AI-03, AI-05.

## 5. Lệnh hay dùng

```powershell
python .claude/skills/domain-bva-testing/scripts/freeze.py HW02/A_FR01/testcases.json --step 3 --out HW02/appendix/ai-outputs --note "#15"
python .claude/skills/domain-bva-testing/scripts/check_domain.py HW02/A_FR01/testcases.json
python .claude/skills/test-case-writing/scripts/lint_testcases.py HW02/A_FR01/testcases.json
python .claude/skills/domain-bva-testing/scripts/render_md.py HW02/A_FR01/testcases.json -o HW02/A_FR01/testcases.md
cd HW02/tests; $env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/A_FR01.json"; npx playwright test A_FR01 --reporter=list,json; cd ../..
python .claude/skills/domain-bva-testing/scripts/merge_results.py HW02/A_FR01/testcases.json HW02/tests/results/A_FR01.json
python tools/summary.py HW02 --write HW02/README.md
powershell -ExecutionPolicy Bypass -File tools/export_commit_log.ps1 HW02
```

## 6. Cấu trúc HW02

```
HW02/
├── README.md                    # tự đánh giá + test summary (SUMMARY tự sinh) + link video
├── 23120255_HW02_Report.md/.pdf # report chính: mỗi feature 4 bảng theo slide + giải thích từng bước + gap analysis
├── A_FR01/ B_FR07/ C_FR15/ D_FR20/
│   ├── testcases.json           # nguồn dữ liệu duy nhất
│   ├── testcases.md             # sinh từ JSON
│   └── evidence/                # ảnh chạy test
├── bugs/BUG-xx.md + issues_page_<feature>.png   # SV viết 🔒
├── tests/                       # Playwright (SV chạy trên máy mình)
├── env/environment.md, mobile_api_url.patch
├── skills/domain-bva-testing/   # chép từ .claude/skills/ khi nộp + VideoLinks.md
├── ai-forms/AI-02…, AI-03…, AI-05… (.md + .pdf đã ký)
└── appendix/A_prompt_log.md, prompt_log_notes.toml, ai-outputs/, commit_log.txt
```

Trước khi nộp: chạy skill `hw-submission-audit`; chép `.claude/skills/domain-bva-testing` sang `HW02/skills/`; zip **chỉ** thư mục `HW02` (không `.git`, không `.transcripts`).
