# HW04 – Automation Testing · Kế hoạch nộp bài (report_plan)

Lê Tấn Hiệp – 23120255 · Deadline **11:00 18/11/2026** (Moodle) · Cấp độ AI: **Cấp 4** · Bloom-AI: **G9.2 + G9.3 + G9.4** (đề §3, §8)

File này không nộp (`HW04/.gitattributes`: `report_plan.md export-ignore`). Trạng thái kiểm bằng `ls` lúc 17/11/2026 (lệnh #23).

## a. Biểu mẫu AI

| Form | Bắt buộc | File dự kiến | Ai làm | Trạng thái |
|---|---|---|---|---|
| AI-02 Audit Report | Có (đề §9, Mandatory Appendix) | `ai-forms/AI-02_Audit_Report_23120255.md` + `.pdf`; bảng tóm tắt ở report §9 | AI điền dữ kiện (công cụ, ngày giờ, prompt, output, artifact từ git); SV viết verdict + lý do, ký | THIẾU |
| AI-03 Disclosure | Có | `ai-forms/AI-03_Disclosure_23120255.md` + `.pdf` | AI điền công cụ, số lượt, dải #; SV xác nhận, ký | THIẾU |
| AI-04 Reflective | Không | — | HW thường, đề không yêu cầu | — |
| AI-05 Privacy | Có (làm cuối) | `ai-forms/AI-05_Privacy_Checklist_23120255.md` + `.pdf` | AI tick mục có bằng chứng; SV tick cam kết, ký | THIẾU |
| AI-06 | Đã nộp tuần 1 | — | — | — |

Câu tuyên bố nguyên văn (đề §9): *"I use AI tools for the following tasks,"*. Mẫu định dạng: `HW03/ai-forms/*.md` (không chép số liệu).

## b. Rubric (đề §15)

| # | Mục | Max | Tự chấm |
|---|---|---|---|
| 1 | Task 1 – Feature A (FR-01 Đăng ký) | 25 | `<SV>` |
| 1 | Task 1 – Feature B (FR-07 Giỏ hàng) | 25 | `<SV>` |
| 1 | Task 1 – Feature C (FR-15 Quản lý sản phẩm) | 25 | `<SV>` |
| 2 | Task 2 – Demo video | 15 | `<SV>` |
| 3 | Agent Skills (+ video YouTube) | 10 | `<SV>` |
| | Tổng = 3 số trong tên zip | 100 | `<SV>` |

## c. Danh sách nộp (đề §14) – trạng thái

| # | Mục (đề §14) | Đường dẫn | Trạng thái | Ghi chú |
|---|---|---|---|---|
| 1 | Main report (.md + PDF) gồm automation report + review/gap analysis script AI | `HW04/23120255_HW04_Report.md` / `.pdf` | .md: ĐÃ CÓ (dàn ý, lệnh #23) · PDF: THIẾU | 🔒 §3.6/4.6/5.6 "vì sao AI sai", §8 Critique, §11 tự đánh giá do SV viết |
| 2 | Link repo GitHub public (scripts, data, HTML reports) | README + report §1 | THIẾU (ô `[...]`) | `https://github.com/ThachHaoo/software-testing-2627` – SV điền |
| 3 | HTML report đa trình duyệt | `HW04/reports/` | ĐÃ CÓ: 9 lượt chính thức (A 134709/134950/135230, B 141103/141230/141359, C 151143/151225/151306) + 23 lượt thử | Z2: lượt thử export-ignore (chưa áp vào `.gitattributes`) |
| 4 | Link video demo YouTube unlisted (≥ 5 phút, tiếng Việt, whoami/hostname hoặc face-cam) | README, report §7 | THIẾU | SV đang quay |
| 5 | AI Critique + AI Audit Report (.md + PDF) | report §8, §9; `ai-forms/AI-02…` | THIẾU | Critique 🔒 200–300 từ |
| 6 | Git commit log (text) | `HW04/commit_log.txt` (`tools/export_commit_log.ps1 HW04`) | THIẾU | Chạy sau commit cuối |
| 7 | Bug report + ảnh trang GitHub Issues | `HW04/bugs/BUG-86…103.md`, `HW04/bugs/issues_page_1.png` | ĐÃ CÓ | 18 issue #298–#315 |
| 8 | README.md: bảng tự chấm + test summary (feature, TC automated/executed/pass/fail, số lượt chạy, số bug, link video) | `HW04/README.md` | ĐÃ CÓ một phần: summary sinh bằng `tools/hw04_summary.py` · THIẾU: bảng tự chấm, link video, link repo | |
| 9a | Supporting – Agent Skill + video dùng skill | `HW04/skills/playwright-ddt-automation/`, `HW04/skills/VideoLinks.md` | THIẾU | Chép từ `.claude/skills/playwright-ddt-automation/` khi đóng gói |
| 9b | Supporting – prompt log | `HW04/appendix/A_prompt_log.md` | ĐÃ CÓ (28 lượt, 17/11 lệnh #23) | Thiếu transcript claude.ai (phiên thảo luận) – SV tải về `.transcripts/` |
| 9c | Supporting – output AI đông lạnh | `HW04/appendix/ai-outputs/` (INDEX.md) | ĐÃ CÓ | A/B/C step1, 3, 6 |
| 9d | Supporting – data, spec, page object, fixture | `HW04/data/`, `HW04/tests/` | ĐÃ CÓ | |
| 9e | Supporting – evidence ảnh | `HW04/*/evidence/` | ĐÃ CÓ (A 48, B 54, C 54 ảnh) | AI chỉ xem mẫu (A 3, B 3, C 2) → SV xem hết trước khi nộp |
| — | Kế hoạch nộp bài (file này) | `HW04/report_plan.md` | — | Không nộp (export-ignore) |

Moodle: ≤ 20 file, mỗi file ≤ 20 MB. Zip: `23120255_HW04_AI_Automation_<ggg>.zip` bằng `git archive` (CLAUDE.md gốc mục 2). `HW04/reports/` hiện 106 MB (9 lượt chính thức ≈ 19 MB chưa nén; 23 lượt thử ≈ 87 MB, gồm lượt có trace) → Z2.

## d. Mâu thuẫn / dễ sót trong đề

| Mã | Nội dung | Cách xử lý |
|---|---|---|
| G9 | Bảng đầu đề "G9.1 → G9.6, depending on the homework" ↔ §3, §8 "G9.2 (Apply), G9.3 (Analyse), G9.4 (Collaborate)"; Agent Skill (§7) thuộc G9.5 | Ghi G9.2 + G9.3 + G9.4 (§3/§8 là quy định riêng của HW04) |
| M1 | Đề §12 bắt buộc repo public ↔ CLAUDE.md gốc cũ ghi private | Đã chốt: repo public từ 16/11 |
| M2 | Deadline "refer to Moodle" | 11:00 18/11/2026 |
| WK | §6 gợi ý Chromium/Firefox/WebKit; WebKit bị Smart App Control chặn | W1=a: Chrome/Edge/Firefox (đề cho phép bộ này) |
| C8 | §12 chỉ commit chạm `.spec.*` mới tính 8 commit | Hiện 12 commit sửa `HW04/tests/*.spec.ts` (`tools/hw04_summary.py`) |
| RB | §11 "Run by" + ISO timestamp không được AI sinh/bịa | Report HTML chỉ từ lượt SV chạy; AI không sửa nội dung report |

## e. Quyết định đã chốt

| Mã | Quyết định | Nguồn |
|---|---|---|
| S1 = a | Tự viết skill `playwright-ddt-automation` | phiên thảo luận 23:01 16/11 |
| T1 = a | 15 TC UI mỗi feature | phiên thảo luận 23:01 16/11 |
| T2 = a | Dữ liệu JSON (expected nguyên văn HW02 + sha1) | phiên thảo luận 23:01 16/11 |
| T3 = a | Chromium/Firefox/WebKit → thay bằng W1 = a | phiên thảo luận 23:01 16/11 |
| T4 = a | Playwright HTML reporter, "Run by" ở title + metadata | phiên thảo luận 23:01 16/11 |
| W1 = a | WebKit bị Smart App Control chặn → Chrome (channel chrome) / Edge (msedge) / Firefox | `HW04/CLAUDE.md` §5 |
| A-S1 | A: loại TC-202 = Negative, TC-211 = Positive (AI suy ra, SV duyệt) – mã S1 trong `A_FR01/selection.json`, khác S1 ở trên | `HW04/A_FR01/selection.json` decisions |
| B1 = b | Tạo issue MỚI cho mọi bug (không comment issue HW02); tiêu đề `[HW04][FR-xx] …`; mục "Liên quan" trỏ issue HW02 | `HW04/bugs/README.md` |
| Z1 = d | Tắt trace trong `playwright.config.ts` (3 report có trace ≈ 30 MB); A chạy lại | `HW04/A_FR01/RUN.md` |
| Z2 | Lượt thử export-ignore khi đóng gói; chỉ nộp 9 lượt chính thức | phiên thảo luận (chưa áp vào `HW04/.gitattributes`) |
| R1 = a | B: từ khoá giỏ trống vào data (`assumptions`), expected giữ nguyên | B 5/6a |
| R2 | B: minh hoạ giỏ trống phải nằm trong khối chứa dòng chữ, bỏ `.first()` | B 5/6b |
| R3 = a | C: giữ `errShown` theo H4 (HW02), ghi là điểm yếu | `HW04/C_FR15/review_sv.md` |
| P1 = a | Ảnh `<TC>_after-*` ngay sau thao tác chính (A after-submit, B after-action, C after-save) | B 5/6c, A 5/6e |
| C1 | C: chọn TC theo `HW04/C_FR15/selection.json` | C 1/6b |
| C2 = a | C: sau mỗi case kiểm backend sống; sập → annotation `backend sập`, resetDb, case Fail | C 1/6b, fixture `c_fr15.ts` |
| C3 | C: 3 giả định ngoài expected (selector thông báo, alert XSS '1', "Form chặn" = SAU = TRƯỚC) – kế thừa HW02 H3/C21/C24, SV chốt | C selection.json |
| Cách 2 | Mỗi nhóm Fail (G) = 1 bug → 18 bug BUG-86…103 | `HW04/bugs/README.md` |

**Còn chờ SV chốt:** áp Z2 vào `.gitattributes`.

## f. Khai cho Audit (ghi dần)

Nguồn: `HW04/*/RUN.md`, `HW04/*/review_sv.md`, khối báo cáo các lệnh, git log.

- Harness HW04 (AI hỗ trợ tạo): skill `playwright-ddt-automation` (SKILL.md, 4 script, 3 asset), `HW04/tests/` (config, global-setup, fixture, page object), `tools/hw04_summary.py`, `tools/restart_backend.ps1`, cấu hình prompt log `tools/hw.toml`.
- Việc AI làm ngoài phạm vi lệnh / sự cố:
  - `rm -rf ../reports/chrome_*` (khi probe) xoá nhầm report đã commit → khôi phục ngay bằng `git checkout -- HW04/reports`; từ đó probe dùng `--reporter=line`, chỉ xoá thư mục mới.
  - 3 report rỗng 13:46 (global-setup không thấy backend) → xoá theo lệnh #14.
  - Tiến trình nền web/admin bị Claude Code dừng do máy thiếu bộ nhớ (17/11); AI không tự bật lại.
  - TC-60 firefox lượt thử 2 B: worker crash `0xC0000409` → SV chạy lại 3/3 Pass → lỗi hạ tầng (B RUN.md).
  - 17/11 tối, A (không chính thức): Windows Code Integrity chặn `firefox-1572\firefox.exe` (sự kiện 3077/3033, 23:05) → lượt gộp 22:56 (firefox 0/15, `spawn UNKNOWN`) và firefox riêng 23:05 (0/15); sau khi khởi động lại máy firefox 23:22 = 7P/8F, khớp chính thức. Chính thức giữ 13:47–13:52; report 3 lượt này không commit. Log: `HW04/env/firefox_blocked_20261117.txt` (A RUN.md).
- Lỗi do AI, phát hiện sau:
  - **C3 chép nhầm** vào "Yêu cầu bị vi phạm" của BUG-101, BUG-103 (generator lấy mọi dòng Yêu cầu của HW02 BUG-35/37) → sửa `d6cd474`.
  - C TC-07: ô không hợp lệ ghi 2 lần (`checkValidity()` cũng bắn `invalid`) – AI phát hiện ở lệnh #17 → sửa 5/6a `2e9e454`.
- Lỗi script AI do **phiên thảo luận** phát hiện (khi đối chiếu code):
  - A: `mode: 'serial'` (1 Fail chặn 14 TC) → 5/6a `6fc76b5`.
  - A: nhóm regex `^(…|…)` trong `oracleOf`, thiếu escape trước `new RegExp` → 5/6c `740934b`.
  - A: `users.list()` gọi ngay sau khi race kết thúc, không chờ phản hồi `POST /api/register` (A_FR01/review_sv.md "Phiên thảo luận bổ sung") → 5/6b `5a378f1`.
  - C: `errShown` đếm mọi hộp thoại (kể cả "Cập nhật thành công!") là "có thông báo lỗi" → R3=a giữ, ghi điểm yếu.
- Lỗi skill lộ ra khi chạy demo / chạy thử (18/11, lệnh #26–#28):
  - Template spec v1 còn `test.describe.configure({ mode: 'serial' })` – lỗi đã sửa ở A 5/6a nhưng chưa đưa ngược vào skill → sửa ở v2 `5bb31d1`.
  - Bản đóng băng nằm trong thư mục Playwright quét (demo đóng băng vào thư mục demo) → có thể bị nạp như spec → v2.1 `99080b2`: `freeze.py` từ chối `--out` trong testDir, đổi đuôi `*.ts.txt`.
  - Template v2 chờ riêng `POST` sau khi bấm → TC-01, TC-63 (ứng dụng tự kiểm phía client, không gửi POST) bị Blocked giả "chờ POST quá 10000 ms" → v2.1: chờ một trong các nhánh phản hồi (request / URL đổi / thông báo / hộp thoại).
  - Config chính thức (testMatch `*.spec.ts`) nạp luôn spec demo (`--list` 4 file, thừa 45 test) → v2.1: spec demo đuôi `*.demo.ts`.
  - Phiên thảo luận không ra lệnh cập nhật skill sau review A (bài học A chỉ sửa trong spec A) → B, C và template vẫn mang bản v1 tới lệnh #27.
- Script tạm AI viết, **không commit**: sinh 18 khung bug (`gen_bugs.py`), Playwright tái hiện 18 bug (`repro.spec.ts`), tạo issue (`mk_issues.py`), chụp trang Issues (`shot.cjs`), đọc phiên bản trình duyệt.
- AI chạy `gh issue create` 18 lần (#298–#315) với file SV viết; chụp `issues_page_1.png` (chưa đăng nhập GitHub).
- AI chỉ xem mẫu ảnh evidence (A 3/48, B 3/54, C 2/54) – SV xem phần còn lại.
- Prompt log: AI thêm bộ đọc bản xuất dữ liệu claude.ai (`conversations.json`) vào `tools/extract_prompt_log.py` (`86d4d78`); hội thoại chép nguyên văn vào `.transcripts/claude-ai_session_HW04_p1.json` (không nộp). 36 lượt claude.ai ghi "Claude (không rõ model)" vì bản xuất không ghi model; SV xác nhận dùng Opus 5.5 (ghi ở `prompt_log_notes.toml`, trường `ghi_chu_model`, chỉ áp cho lượt claude.ai qua `nguon_luot`).

## g. Danh sách cho Mandatory Disclosure (ghi dần)

- AI tạo bản đầu: chọn TC (`selection.json/.md`), file data JSON (expected chép nguyên văn + sha1), page object + fixture, 3 spec + 3 parser oracle, `assertions.md`, `RUN.md` (dữ kiện), `results.md` + `bug_groups.md` (merge_reports), `_groups_AB.md`, `_groups_C.md`, khung 18 bug (chỉ dữ kiện), `repro_check.md`, README test summary, dàn ý report, `report_plan.md`, skill `playwright-ddt-automation`.
- SV xem xét và sửa: 5/6 các feature (A 5/6a–e, B 5/6a–c, C 5/6a), giả định trong data, `[...]`.
- SV tự làm hoàn toàn: ý review spec (`review_sv.md` Bản 1), 18 bug report (tiêu đề, severity, priority, bước, expected, actual, nhận định), chạy lượt chính thức trên máy, video + giọng thuyết minh, Critique, phần "vì sao AI sai/bỏ sót", verdict Audit, điểm tự chấm.
- Prompt log: trích tự động bằng `tools/extract_prompt_log.py` (hook `on_stop.py`); Section/Mục đích/Xử lý do SV ghi trong `prompt_log_notes.toml`. 3 lượt "Claude (không rõ model)" – lý do SV ghi trong notes.
