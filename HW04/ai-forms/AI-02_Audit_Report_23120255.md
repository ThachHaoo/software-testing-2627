**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**
**CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**
**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# AI Audit Report — Mẫu 5 mục cho mỗi Artifact

*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW#01–HW#06, Seminar).*

## 1. Thông tin Sinh viên

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |
| MSSV: | 23120255 |
| Lớp / Khoá: | Software Testing - 23_3 |
| Mã bài tập: | HW04-AI – Automation Testing on EShop |
| Ngày làm bài: | 16/11/2026 – 18/11/2026 |
| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — Claude (không rõ model) 37 lượt; Claude Opus 5.5 47 lượt (tổng 84 lượt theo dòng Tổng của `appendix/A_prompt_log.md`, bản trích 01:49 18/11/2026) |
| Có sử dụng AI: | [x] Có [ ] Không |

**Tuyên bố sử dụng AI (đề):** xem report chính §10 Mandatory Disclosure.

## 2. Hướng dẫn

- Mỗi artifact do AI tạo là 1 hàng. Mục (1) Prompt + công cụ + thời gian + mã `#n`, (2) Output, (5) Bản SV sửa ở bảng 3.1; mục (3) Verdict và (4) Lý do ở bảng 3.2 (em viết).
- Prompt và output nguyên văn: `appendix/A_prompt_log.md` theo mã `#n`; output dạng file đóng băng: `appendix/ai-outputs/` (`INDEX.md`).
- Bảng theo từng commit HW04: report §9.
- Cột #n để "–" tới lần trích prompt log cuối.

## 3. Bảng Audit — 1 hàng / artifact

### 3.1 Mục (1), (2), (5)

| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |
|---|---|---|---|---|
| H1 | Harness HW04: `HW04/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp) | Claude Code · 16/11/2026 22:34 · `4d14bd7` (HW04: bước 0 – môi trường) · – | đề tóm tắt, quyết định, khai Audit · `HW04/CLAUDE.md`, `HW04/report_plan.md` | `838752b` HW04: đổi sang Chrome/Edge/Firefox (W1=a); `ac813b0` HW04: report_plan + dàn ý report (khối REPORT sinh bằng tools/hw04_report.py) + prompt log 28 lượt; `60bec96` HW04: report_plan ghi S1/T1–T4, khai bộ đọc claude.ai; notes ghi chú model lượt claude.ai (nguon_luot); `eb40646` HW04[A-FR01]: ghi 3 lượt không chính thức 17/11 tối (Firefox bị Code Integrity chặn) + log môi trường |
| H2 | Bộ chạy Playwright: config 3 trình duyệt + "Run by" + JSON reporter, global-setup, package/tsconfig | Claude Code · 16/11/2026 22:34 · `4d14bd7` (HW04: bước 0 – môi trường) · – | project chrome/edge/firefox, workers 1, retries 0 · `HW04/tests/playwright.config.ts`, `HW04/tests/global-setup.ts`, `HW04/tests/package.json` … | `838752b` HW04: đổi sang Chrome/Edge/Firefox (W1=a); `b0e2f7c` HW04: skill playwright-ddt-automation v1; `161074b` HW04[A-FR01] 2/6: fixture + page object (Register, Login), tsconfig; `597bda7` HW04: tắt trace để report < 20 MB (Z1=d) |
| S1 | Agent Skill `playwright-ddt-automation` v1 (SKILL.md, 4 script, 3 asset) | Claude Code · 16/11/2026 23:07 · `b0e2f7c` (HW04: skill playwright-ddt-automation v1) · – | quy trình 6 bước có điểm dừng · `.claude/skills/playwright-ddt-automation/SKILL.md`, `.claude/skills/playwright-ddt-automation/scripts/select_tc.py`, `.claude/skills/playwright-ddt-automation/scripts/merge_reports.py` | `0990ac0` HW04[A-FR01] 1/6b – SV chốt; `9905eca` HW04[A-FR01] 6/6: gộp 3 report → results.md, bug_groups.md (3 nhóm), 24 ảnh lỗi; `656962c` HW04[B-FR07] 1/6: chọn 15 TC UI + data JSON (oracle giỏ = trạng thái UI); `14ac598` HW04[B-FR07] 5/6a – sửa: từ khoá giỏ trống chuyển vào data (assumptions, giả định SV chốt), expected giữ nguyên (R1=a); … (+3) |
| S2 | Skill v2 – bài học review A/B/C (template fixture/spec, checklist review bước 5) | Claude Code · 18/11/2026 00:54 · `5bb31d1` (HW04: skill playwright-ddt-automation v2 (bài học review A/B/C)) · – | bỏ serial, step/until/esc/assumption · `.claude/skills/playwright-ddt-automation/assets/spec.template.ts`, `.claude/skills/playwright-ddt-automation/assets/ddt-fixture.template.ts`, `.claude/skills/playwright-ddt-automation/SKILL.md` | `99080b2` HW04: skill v2.1 – freeze ngoài testDir, chế độ demo, chạy thử E2E sạch |
| S3 | Skill v2.1 – freeze ngoài testDir, chế độ demo (`demo.py`), chạy thử E2E | Claude Code · 18/11/2026 01:26 · `99080b2` (HW04: skill v2.1 – freeze ngoài testDir, chế độ demo, chạy thử E2E sạch) · – | 4 TC × 3 trình duyệt khớp HW02 · `.claude/skills/playwright-ddt-automation/scripts/demo.py`, `.claude/skills/playwright-ddt-automation/scripts/freeze.py` | không có |
| S4 | Bản chép skill nộp `HW04/skills/` + `VideoLinks.md` | chưa commit | bản v2.1 @99080b2; link 2 video · `HW04/skills/playwright-ddt-automation/SKILL.md`, `HW04/skills/VideoLinks.md` | – |
| A1 | A_FR01 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng | Claude Code · 16/11/2026 23:08 · `b54c170` (HW04[A-FR01] 1/6: chọn 15 TC UI + data JSON (expected nguyên văn + sha1)) · – | selection + data · `HW04/appendix/ai-outputs/A_FR01/step1/selection.json`, `HW04/appendix/ai-outputs/A_FR01/step1/A_FR01.json`, `HW04/appendix/ai-outputs/A_FR01/step1/selection.md` | không có |
| A2 | A_FR01 bước 2: fixture + page object – bản đóng băng | Claude Code · 17/11/2026 00:10 · `161074b` (HW04[A-FR01] 2/6: fixture + page object (Register, Login), tsconfig) · – | selector theo mã UI thật · `HW04/appendix/ai-outputs/A_FR01/step2/a_fr01.ts`, `HW04/appendix/ai-outputs/A_FR01/step2/ddt.ts`, `HW04/appendix/ai-outputs/A_FR01/step2/register.page.ts` … | không có |
| A3 | A_FR01 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng | Claude Code · 17/11/2026 00:23 · `9a5e558` (HW04[A-FR01] 3/6: sinh spec data-driven + bảng assertion) · – | 45 test (15 TC × 3) · `HW04/appendix/ai-outputs/A_FR01/step3/A_FR01.spec.ts`, `HW04/appendix/ai-outputs/A_FR01/step3/assertions.md` | không có |
| A4 | A_FR01 `RUN.md` – dữ kiện lượt thử/chính thức | Claude Code · 17/11/2026 00:30 · `6fc76b5` (HW04[A-FR01] 5/6a – sửa: bỏ mode serial (1 Fail chặn 14 TC)) · – | bảng lượt chạy, ghi chú lỗi hạ tầng · `HW04/A_FR01/RUN.md` | `b321098` HW04[A-FR01]: RUN.md lượt thử 2 + 4 report; `74dd2c6` HW04[A-FR01]: lượt chính thức (3 report) + RUN.md; `9905eca` HW04[A-FR01] 6/6: gộp 3 report → results.md, bug_groups.md (3 nhóm), 24 ảnh lỗi; `597bda7` HW04: tắt trace để report < 20 MB (Z1=d); … (+5) |
| A6 | A_FR01 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng | Claude Code · 17/11/2026 01:14 · `9905eca` (HW04[A-FR01] 6/6: gộp 3 report → results.md, bug_groups.md (3 nhóm), 24 ảnh lỗi) · – | Pass/Fail/Blocked theo trình duyệt, nhóm Fail (dữ kiện) · `HW04/appendix/ai-outputs/A_FR01/step6/results.md`, `HW04/appendix/ai-outputs/A_FR01/step6/bug_groups.md` | không có |
| A7 | A_FR01 `not_automated.md` – TC/phần expected không tự động | chưa commit | từ selection.json + annotation report · `HW04/A_FR01/not_automated.md` | – |
| B1 | B_FR07 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng | Claude Code · 17/11/2026 01:18 · `656962c` (HW04[B-FR07] 1/6: chọn 15 TC UI + data JSON (oracle giỏ = trạng thái UI)) · – | selection + data · `HW04/appendix/ai-outputs/B_FR07/step1/selection.json`, `HW04/appendix/ai-outputs/B_FR07/step1/B_FR07.json`, `HW04/appendix/ai-outputs/B_FR07/step1/selection.md` | không có |
| B2 | B_FR07 bước 2: fixture + page object – bản đóng băng | Claude Code · 17/11/2026 01:33 · `8b77124` (HW04[B-FR07] 2/6: fixture + page object (trang chủ, chi tiết, giỏ qua navbar; oracle giỏ từ UI)) · – | selector theo mã UI thật · `HW04/appendix/ai-outputs/B_FR07/step2/b_fr07.ts`, `HW04/appendix/ai-outputs/B_FR07/step2/shop.pages.ts` | không có |
| B3 | B_FR07 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng | Claude Code · 17/11/2026 01:43 · `7e75536` (HW04[B-FR07] 3/6: spec data-driven + parser oracle + bảng assertion (45 test)) · – | 45 test (15 TC × 3) · `HW04/appendix/ai-outputs/B_FR07/step3/B_FR07.spec.ts`, `HW04/appendix/ai-outputs/B_FR07/step3/b_fr07.oracle.ts`, `HW04/appendix/ai-outputs/B_FR07/step3/assertions.md` | không có |
| B4 | B_FR07 `RUN.md` – dữ kiện lượt thử/chính thức | Claude Code · 17/11/2026 01:52 · `6d9f402` (HW04[B-FR07] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md) · – | bảng lượt chạy, ghi chú lỗi hạ tầng · `HW04/B_FR07/RUN.md` | `ef419f2` HW04[B-FR07] 5/6: lượt thử 2 (3 trình duyệt) + RUN.md (TC-60 firefox: worker crash); `d676bf9` HW04[B-FR07] 5/6: RUN.md – TC-60 firefox lỗi hạ tầng (3/3 Pass khi chạy riêng), xoá 3 report rỗng; `072e47f` HW04[B-FR07] 6/6 – lượt chính thức |
| B6 | B_FR07 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng | Claude Code · 17/11/2026 14:18 · `072e47f` (HW04[B-FR07] 6/6 – lượt chính thức) · – | Pass/Fail/Blocked theo trình duyệt, nhóm Fail (dữ kiện) · `HW04/appendix/ai-outputs/B_FR07/step6/results.md`, `HW04/appendix/ai-outputs/B_FR07/step6/bug_groups.md` | không có |
| B7 | B_FR07 `not_automated.md` – TC/phần expected không tự động | Claude Code · 17/11/2026 13:42 · `841c7e2` (HW04[B-FR07] 5/6: ghi phần không tự động (TC-08 dialog đang mở)) · – | từ selection.json + annotation report · `HW04/B_FR07/not_automated.md` | không có |
| C1 | C_FR15 bước 1: chọn 15 TC + data JSON (expected nguyên văn + sha1) – bản đóng băng | Claude Code · 17/11/2026 14:14 · `25f6e6e` (HW04[C-FR15] 1/6: chọn 15 TC UI (Thêm/Sửa/Xóa) + data JSON + rủi ro sập backend (chưa quyết)) · – | selection + data · `HW04/appendix/ai-outputs/C_FR15/step1/selection.json`, `HW04/appendix/ai-outputs/C_FR15/step1/C_FR15.json`, `HW04/appendix/ai-outputs/C_FR15/step1/selection.md` | không có |
| C2 | C_FR15 bước 2: fixture + page object – bản đóng băng | Claude Code · 17/11/2026 14:20 · `16d791d` (HW04[C-FR15] 2/6: fixture + page object admin (login, form theo placeholder, bảng, dialog, API trước/sau, health-check backend)) · – | selector theo mã UI thật · `HW04/appendix/ai-outputs/C_FR15/step2/c_fr15.ts`, `HW04/appendix/ai-outputs/C_FR15/step2/admin.pages.ts` | không có |
| C3 | C_FR15 bước 3: spec data-driven + parser oracle + bảng assertion – bản đóng băng | Claude Code · 17/11/2026 14:28 · `370c9cd` (HW04[C-FR15] 3/6: spec data-driven + parser oracle + bảng assertion (45 test); giả định ngoài expected vào data) · – | 45 test (15 TC × 3) · `HW04/appendix/ai-outputs/C_FR15/step3/C_FR15.spec.ts`, `HW04/appendix/ai-outputs/C_FR15/step3/c_fr15.oracle.ts`, `HW04/appendix/ai-outputs/C_FR15/step3/assertions.md` | không có |
| C4 | C_FR15 `RUN.md` – dữ kiện lượt thử/chính thức | Claude Code · 17/11/2026 14:47 · `0631be5` (HW04[C-FR15] 4/6: lượt thử 1 (3 trình duyệt) + RUN.md) · – | bảng lượt chạy, ghi chú lỗi hạ tầng · `HW04/C_FR15/RUN.md` | `2c54f76` HW04[C-FR15] 6/6 – lượt chính thức |
| C6 | C_FR15 bước 6: `results.md` + `bug_groups.md` (merge_reports) – bản đóng băng | Claude Code · 17/11/2026 15:17 · `2c54f76` (HW04[C-FR15] 6/6 – lượt chính thức) · – | Pass/Fail/Blocked theo trình duyệt, nhóm Fail (dữ kiện) · `HW04/appendix/ai-outputs/C_FR15/step6/results.md`, `HW04/appendix/ai-outputs/C_FR15/step6/bug_groups.md` | không có |
| C7 | C_FR15 `not_automated.md` – TC/phần expected không tự động | chưa commit | từ selection.json + annotation report · `HW04/C_FR15/not_automated.md` | – |
| B1 | Dữ kiện nhóm Fail A+B, C (`_groups_AB.md`, `_groups_C.md`) | Claude Code · 17/11/2026 14:48 · `961d61d` (HW04: dữ kiện nhóm Fail A + B để SV quyết G → BUG) · – | triệu chứng, vị trí mã SUT, issue HW02 · `HW04/bugs/_groups_AB.md`, `HW04/bugs/_groups_C.md` | `f497ee8` HW04: dữ kiện nhóm Fail C + README nháp (test summary sinh bằng tools/hw04_summary.py) |
| B2 | Khung 18 bug (Cách 2, chỉ dữ kiện) + `bugs/README.md` | Claude Code · 17/11/2026 15:34 · `2667147` (HW04: khung 18 bug (Cách 2)) · – | nội dung bug do SV viết · `HW04/bugs/README.md`, `HW04/bugs/BUG-86.md` | `2775914` HW04: SV viết 18 bug; `8f47846` HW04: SV sửa bug theo kiểm dữ kiện; `1881c16` HW04: SV sửa bug theo kiểm dữ kiện; `78873e0` HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug |
| B3 | Kiểm tái hiện 18 bug bằng Playwright (`repro_check.md`) | Claude Code · 17/11/2026 20:59 · `9e9f88f` (HW04: kiểm tái hiện 18 bug (dữ kiện, chờ SV sửa)) · – | lần 1 lệch, lần 2 không lệch · `HW04/bugs/repro_check.md` | `78873e0` HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug |
| B4 | Tạo 18 GitHub Issue `gh issue create --body-file` (file SV viết) + ảnh trang Issues | Claude Code · 17/11/2026 21:22 · `78873e0` (HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug) · – | #298–#315 trên tkob-team/eshop-sut · `HW04/bugs/issues_page_1.png` | không có |
| R1 | README test summary (`tools/hw04_summary.py`) | Claude Code · 17/11/2026 15:18 · `f497ee8` (HW04: dữ kiện nhóm Fail C + README nháp (test summary sinh bằng tools/hw04_summary.py)) · – | khối SUMMARY · `tools/hw04_summary.py`, `HW04/README.md` | `78873e0` HW04: tạo 18 issue [HW04] (#298–#315), điền số issue, ảnh trang Issues, README số bug; `2d3660b` HW04: link video Task 2 (README, report §7, skills/VideoLinks.md); RUN.md A ghi 3 lượt quay video |
| R2 | Dàn ý report + khối REPORT (`tools/hw04_report.py`) | Claude Code · 17/11/2026 21:36 · `ac813b0` (HW04: report_plan + dàn ý report (khối REPORT sinh bằng tools/hw04_report.py) + prompt log 28 lượt) · – | bảng chọn TC/kết quả/review/bug/audit · `tools/hw04_report.py`, `HW04/23120255_HW04_Report.md` | `2d3660b` HW04: link video Task 2 (README, report §7, skills/VideoLinks.md); RUN.md A ghi 3 lượt quay video |
| R3 | Khung AI-02 + khối Mandatory Disclosure §10 (`tools/forms_hw04.py`) | chưa commit | file này · `tools/forms_hw04.py`, `HW04/ai-forms/AI-02_Audit_Report_23120255.md` | – |
| P1 | Bộ đọc bản xuất dữ liệu claude.ai cho prompt log | Claude Code · 17/11/2026 22:12 · `86d4d78` (tools: đọc hội thoại claude.ai từ bản xuất dữ liệu (claude-ai_*.json); HW04 prompt log 65 lượt) · – | 36 lượt claude.ai vào log · `tools/extract_prompt_log.py` | `60bec96` HW04: report_plan ghi S1/T1–T4, khai bộ đọc claude.ai; notes ghi chú model lượt claude.ai (nguon_luot) |
| D1 | Chạy thử skill E2E ở chế độ demo (nhánh `skill-dryrun`, đã xoá, không commit) | Claude Code · 18/11/2026 01:26 · `99080b2` (HW04: skill v2.1 – freeze ngoài testDir, chế độ demo, chạy thử E2E sạch) · – | lỗi phát hiện → S3 · `.claude/skills/playwright-ddt-automation/scripts/demo.py` | không có |

*33 artifact. Sinh bằng `tools/forms_hw04.py` từ danh mục trong script + `git log` (commit tạo = commit đầu tiên thêm file chính – đường dẫn đầu ở cột (2) – hoặc commit chỉ định cho skill v1/v2/v2.1, khung bug, bộ đọc claude.ai). Cột (5) chỉ liệt kê commit, không diễn giải.*

### 3.2 Mục (3), (4) – em điền

*Verdict: VALID / INVALID / INCOMPLETE. Lý do: 1–2 câu, dẫn ISTQB/slide. #n để mở `appendix/A_prompt_log.md`.*

| Mã | #n | (3) Verdict | (4) Lý do |
|---|---|---|---|
| H1 | – | `<SV viết>` | `<SV viết>` |
| H2 | – | `<SV viết>` | `<SV viết>` |
| S1 | – | `<SV viết>` | `<SV viết>` |
| S2 | – | `<SV viết>` | `<SV viết>` |
| S3 | – | `<SV viết>` | `<SV viết>` |
| S4 | – | `<SV viết>` | `<SV viết>` |
| A1 | – | `<SV viết>` | `<SV viết>` |
| A2 | – | `<SV viết>` | `<SV viết>` |
| A3 | – | `<SV viết>` | `<SV viết>` |
| A4 | – | `<SV viết>` | `<SV viết>` |
| A6 | – | `<SV viết>` | `<SV viết>` |
| A7 | – | `<SV viết>` | `<SV viết>` |
| B1 | – | `<SV viết>` | `<SV viết>` |
| B2 | – | `<SV viết>` | `<SV viết>` |
| B3 | – | `<SV viết>` | `<SV viết>` |
| B4 | – | `<SV viết>` | `<SV viết>` |
| B6 | – | `<SV viết>` | `<SV viết>` |
| B7 | – | `<SV viết>` | `<SV viết>` |
| C1 | – | `<SV viết>` | `<SV viết>` |
| C2 | – | `<SV viết>` | `<SV viết>` |
| C3 | – | `<SV viết>` | `<SV viết>` |
| C4 | – | `<SV viết>` | `<SV viết>` |
| C6 | – | `<SV viết>` | `<SV viết>` |
| C7 | – | `<SV viết>` | `<SV viết>` |
| B1 | – | `<SV viết>` | `<SV viết>` |
| B2 | – | `<SV viết>` | `<SV viết>` |
| B3 | – | `<SV viết>` | `<SV viết>` |
| B4 | – | `<SV viết>` | `<SV viết>` |
| R1 | – | `<SV viết>` | `<SV viết>` |
| R2 | – | `<SV viết>` | `<SV viết>` |
| R3 | – | `<SV viết>` | `<SV viết>` |
| P1 | – | `<SV viết>` | `<SV viết>` |
| D1 | – | `<SV viết>` | `<SV viết>` |

### 3.3 Khai cho Audit (chép nguyên văn `report_plan.md` mục f)

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
  - `users.list` – `[...]` (SV/phiên thảo luận ghi rõ commit/bài).
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

## 4. Kết luận chung

`<SV viết>`

## 5. AI Critique

Xem report chính `23120255_HW04_Report.md` §8.

## Chữ ký

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |
| MSSV: | 23120255 |
| Lớp / Khoá: | Software Testing - 23_3 |
| Môn học: | CSC13003 – Kiểm chứng Phần mềm |
| Giảng viên: | Thầy Lâm Quang Vũ, Thầy Trần Duy Hoàng, Cô Trần Thị Bích Hạnh, Thầy Trương Phước Lộc, Thầy Hồ Tuấn Thanh |
| Ngày: | [...] |
| Chữ ký: | [...] |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Hardman, P. (2025). A Post-AI Learning Taxonomy.
- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.
