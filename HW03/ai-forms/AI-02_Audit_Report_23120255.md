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
| Mã bài tập: | HW03-AI – GUI & Usability on EShop |
| Ngày làm bài: | 04/11/2026 – [...] |
| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — Claude Sonnet 4.6 2 lượt; Claude Opus 5.5 91 lượt; Claude (không rõ model) 6 lượt (tổng 99 lượt theo dòng Tổng của `appendix/A_prompt_log.md`, bản trích 19:03 10/11/2026) |
| Có sử dụng AI: | [x] Có [ ] Không |

**Tuyên bố sử dụng AI (đề):** xem report chính §11 Mandatory Disclosure.

## 2. Hướng dẫn

- Mỗi artifact do AI tạo là 1 hàng. Mục (1) Prompt + công cụ + thời gian + mã `#n`, (2) Output, (5) Bản SV sửa ở bảng 3.1; mục (3) Verdict và (4) Lý do ở bảng 3.2 (em viết).
- Prompt và output nguyên văn: `appendix/A_prompt_log.md` theo mã `#n`; output dạng file đóng băng: `appendix/ai-outputs/`.
- Cột #n để "[chờ chốt transcript]" tới lần trích prompt log cuối (gồm transcript phiên claude.ai).

## 3. Bảng Audit — 1 hàng / artifact

### 3.1 Mục (1), (2), (5)

| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |
|---|---|---|---|---|
| H1 | Harness HW03: `HW03/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp), khung report/README | Claude Code · 04/11/2026 18:12 · `24f1345` (HW03: tách CLAUDE.md theo bài – thêm HW02/HW03 CLAUDE.md (bỏ chặn của gitignore toàn cục)) · [chờ chốt transcript] | khung bài, quyết định, khai Audit · `HW03/CLAUDE.md`, `HW03/report_plan.md` | `d7dc423` HW03: X1, X2 – ghi quyết định vào report_plan mục e; `9463442` HW03[T1] 2/6: vá CL-07; `1172c20` HW03[T1] 3/6b: C1, H1, P3A; `99a64dc` HW03: deadline thật 11/11 10:00; … (+15) |
| T1 | Khảo sát control C2 (`c2_inventory.md`) | Claude Code · 04/11/2026 17:49 · `39f685c` (HW03[T1] 1/6: AI nháp checklist C2) · [chờ chốt transcript] | inventory màn Đăng nhập, Quên MK, Hồ sơ, Lịch sử đơn, navbar · `HW03/checklist/c2_inventory.md` | không có |
| T2 | Checklist nháp 3 nguồn – bản đóng băng v1 (bước 1) | Claude Code · 04/11/2026 17:49 · `39f685c` (HW03[T1] 1/6: AI nháp checklist C2) · [chờ chốt transcript] | 65 item · `HW03/appendix/ai-outputs/T1_checklist_ai_v1.json` | không có |
| T3 | Khung trống `sv_items.md` + kiểm cấu trúc item SV (`sv_items_check.md`) | Claude Code · 04/11/2026 19:29 · `de4c69a` (HW03[T1] 2/6c: AI trả lời vì sao bỏ sót) · [chờ chốt transcript] | khung trống; nội dung item SV do SV viết · `HW03/checklist/sv_items_check.md` | không có |
| T4 | Câu trả lời "vì sao AI bỏ sót" (sau khi SV commit item) | Claude Code · 04/11/2026 19:29 · `de4c69a` (HW03[T1] 2/6c: AI trả lời vì sao bỏ sót) · [chờ chốt transcript] | SV-01…SV-06 · `HW03/checklist/ai_gap_answer.md` | không có |
| T5 | Playwright C2 + oracle khoá sha1 + reporter + seed đơn | Claude Code · 04/11/2026 20:09 · `07982fc` (HW03[T1] 3/6: Playwright P1/P2 + RUN.md) · [chờ chốt transcript] | 59 item auto, 3 project P1/P2/P3 · `HW03/tests/C2.spec.ts`, `HW03/tests/lib.ts`, `HW03/tests/oracle.src.json` … | `1172c20` HW03[T1] 3/6b: C1, H1, P3A |
| T6 | `RUN.md` (phần chạy tay) + mẫu file lượt + `dom_probe.js` | Claude Code · 04/11/2026 20:09 · `07982fc` (HW03[T1] 3/6: Playwright P1/P2 + RUN.md) · [chờ chốt transcript] | 15/15/13 item chạy tay · `HW03/checklist/RUN.md`, `HW03/tests/gen_run.py`, `HW03/checklist/dom_probe.js` … | `1172c20` HW03[T1] 3/6b: C1, H1, P3A; `9dfb111` HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59; `107b67f` HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt; `61858d4` HW03[T1] 4/6a2: sửa nhãn ảnh B3/B4, M5 dùng ảnh M3/M4; … (+1) |
| T7 | Kiểm ảnh/kết quả chạy tay (`run_check.md`), nén + đổi tên ảnh | Claude Code · 10/11/2026 02:45 · `107b67f` (HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt) · [chờ chốt transcript] | R1–R12, L1–L8 · `HW03/checklist/run_check.md`, `tools/compress_hw03.py` | `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `4b4c64c` HW03[T1] 4/6d: R4; `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64 |
| T8 | Gộp lượt auto + tay vào `checklist.json` (V1, override theo quyết định SV) + `checklist.md` | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · [chờ chốt transcript] | kết quả P1/P2/P3 · `tools/merge_hw03.py` | `0679e25` HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện); `d811ea2` HW03: cập nhật skill theo cách làm thực tế; `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2; … (+1) |
| T9 | Excel 3 sheet | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · [chờ chốt transcript] | Test Cases / Checklist / Test Summary Report · `HW03/excel/23120255_HW03_Checklist.xlsx` | `0679e25` HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện); `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2 |
| T10 | Danh sách Failed + đối chiếu trùng issue (`failed_list.md`, `dup_check.md`, `issues.json`, `issue_dup_FR02.md`) | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · [chờ chốt transcript] | trùng 14 / một phần 4 / MỚI 28 · `HW03/bugs/failed_list.md`, `HW03/bugs/dup_check.md`, `HW03/bugs/issues.json` … | `0679e25` HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện); `3ab505e` HW03[T1] 5/6b: SV chốt nhóm bug; `d811ea2` HW03: cập nhật skill theo cách làm thực tế; `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; … (+1) |
| T11 | Nhóm dữ kiện bug + khung BUG-58…85 (chỉ dữ kiện) | Claude Code · 10/11/2026 03:07 · `0679e25` (HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện)) · [chờ chốt transcript] | 28 nhóm (SV chốt), 28 khung · `HW03/bugs/bug_groups.md`, `tools/bug_groups_hw03.py`, `tools/bug_skeleton_hw03.py` | `3ab505e` HW03[T1] 5/6b: SV chốt nhóm bug; `d811ea2` HW03: cập nhật skill theo cách làm thực tế; `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2; … (+1) |
| T12 | Danh sách ảnh thiếu (`missing_photos.md`) | Claude Code · 10/11/2026 18:51 · `9ede85b` (HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02) · [chờ chốt transcript] | đối chiếu RUN.md/report · `HW03/checklist/missing_photos.md` | `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64; `6069790` HW03[T1] 4/6f: ảnh tổng quan P3 |
| U1 | Gói usability nháp – bản đóng băng (plan 9 phần, participant kit, phiếu quan sát) | Claude Code · 04/11/2026 17:51 · `c081f96` (HW03[T2] 1/10: AI nháp gói usability) · [chờ chốt transcript] | chưa dùng trong phiên thật · `HW03/appendix/ai-outputs/T2_plan_v1.md`, `HW03/appendix/ai-outputs/T2_participant_kit_v1.md`, `HW03/appendix/ai-outputs/T2_observation_sheet_v1.md` | không có |
| U2 | Môi trường usability từ xa (script phiên, tunnel, đưa SUT về main) + sửa plan mục 5–6 | Claude Code · 10/11/2026 03:22 · `4199810` (HW03[T2] 2b/10: môi trường usability từ xa (tunnel)) · [chờ chốt transcript] | nhánh local `usability-tunnel` trong eshop-sut (không nộp) · `tools/usability_session.ps1`, `tools/sut_main.ps1`, `tools/restart_backend.ps1` … | không có |
| S1 | Agent Skill `gui-checklist-testing` (SKILL.md, reference, asset, 8 script) | Claude Code · 10/11/2026 18:25 · `fcab9e1` (HW03[Skill] 1/3: chép skill + VideoLinks) · [chờ chốt transcript] | chép từ `.claude/skills/` · `HW03/skills/gui-checklist-testing` | `0d8fd34` HW03[Skill] 1/3b: D1; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2 |
| S2 | Agent Skill `usability-evaluation` (SKILL.md, reference, asset, 6 script) | Claude Code · 10/11/2026 18:25 · `fcab9e1` (HW03[Skill] 1/3: chép skill + VideoLinks) · [chờ chốt transcript] | chưa dùng trên phiên thật · `HW03/skills/usability-evaluation` | không có |
| S3 | `skills/VideoLinks.md` + đề xuất demo (`demo_plan.md`, không nộp) | Claude Code · 10/11/2026 18:25 · `fcab9e1` (HW03[Skill] 1/3: chép skill + VideoLinks) · [chờ chốt transcript] | link `<SV điền>` · `HW03/skills/VideoLinks.md`, `HW03/skills/demo_plan.md` | không có |
| R1 | Bảng report T1/T3 (§3.3, §3.5, §3.6, §4.1, §4.3) + nháp §3.2, §4.2 (📝 AI nháp) | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · [chờ chốt transcript] | khối giữa marker REPORT:T1 · `tools/report_t1_hw03.py` | `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2; `4b4c64c` HW03[T1] 4/6d: R4; `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64 |
| R2 | Test summary README + report §8 | Claude Code · 10/11/2026 19:05 · `70aa585` (HW03: README test summary (script) + chỗ tự chấm) · [chờ chốt transcript] | khối SUMMARY · `tools/summary_hw03.py` | không có |
| R3 | Khung AI-02, AI-03, khối Mandatory Disclosure §11 | Claude Code · 10/11/2026 19:07 · `c2aa7ae` (HW03: khung AI-02, AI-03 + Mandatory Disclosure §11 (script)) · [chờ chốt transcript] | file này · `tools/forms_hw03.py` | không có |
| E1 | Mô tả môi trường (`env/environment.md`) | Claude Code · 05/11/2026 02:26 · `1172c20` (HW03[T1] 3/6b: C1, H1, P3A) · [chờ chốt transcript] | phiên bản trình duyệt/OS/thiết bị · `HW03/env/environment.md` | `107b67f` HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt |

*22 artifact. Sinh bằng `tools/forms_hw03.py` từ danh mục trong script + `git log` (commit tạo = commit đầu tiên thêm file chính – đường dẫn đầu ở cột (2)). Cột (5) chỉ liệt kê commit, không diễn giải.*

### 3.2 Mục (3), (4)

| Mã | Artifact | (3) Verdict (VALID / INVALID / INCOMPLETE) | (4) Lý do (dẫn ISTQB/slide) |
|---|---|---|---|
| H1 | Harness HW03: `HW03/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp), khung report/README | `<SV viết>` | `<SV viết>` |
| T1 | Khảo sát control C2 (`c2_inventory.md`) | `<SV viết>` | `<SV viết>` |
| T2 | Checklist nháp 3 nguồn – bản đóng băng v1 (bước 1) | `<SV viết>` | `<SV viết>` |
| T3 | Khung trống `sv_items.md` + kiểm cấu trúc item SV (`sv_items_check.md`) | `<SV viết>` | `<SV viết>` |
| T4 | Câu trả lời "vì sao AI bỏ sót" (sau khi SV commit item) | `<SV viết>` | `<SV viết>` |
| T5 | Playwright C2 + oracle khoá sha1 + reporter + seed đơn | `<SV viết>` | `<SV viết>` |
| T6 | `RUN.md` (phần chạy tay) + mẫu file lượt + `dom_probe.js` | `<SV viết>` | `<SV viết>` |
| T7 | Kiểm ảnh/kết quả chạy tay (`run_check.md`), nén + đổi tên ảnh | `<SV viết>` | `<SV viết>` |
| T8 | Gộp lượt auto + tay vào `checklist.json` (V1, override theo quyết định SV) + `checklist.md` | `<SV viết>` | `<SV viết>` |
| T9 | Excel 3 sheet | `<SV viết>` | `<SV viết>` |
| T10 | Danh sách Failed + đối chiếu trùng issue (`failed_list.md`, `dup_check.md`, `issues.json`, `issue_dup_FR02.md`) | `<SV viết>` | `<SV viết>` |
| T11 | Nhóm dữ kiện bug + khung BUG-58…85 (chỉ dữ kiện) | `<SV viết>` | `<SV viết>` |
| T12 | Danh sách ảnh thiếu (`missing_photos.md`) | `<SV viết>` | `<SV viết>` |
| U1 | Gói usability nháp – bản đóng băng (plan 9 phần, participant kit, phiếu quan sát) | `<SV viết>` | `<SV viết>` |
| U2 | Môi trường usability từ xa (script phiên, tunnel, đưa SUT về main) + sửa plan mục 5–6 | `<SV viết>` | `<SV viết>` |
| S1 | Agent Skill `gui-checklist-testing` (SKILL.md, reference, asset, 8 script) | `<SV viết>` | `<SV viết>` |
| S2 | Agent Skill `usability-evaluation` (SKILL.md, reference, asset, 6 script) | `<SV viết>` | `<SV viết>` |
| S3 | `skills/VideoLinks.md` + đề xuất demo (`demo_plan.md`, không nộp) | `<SV viết>` | `<SV viết>` |
| R1 | Bảng report T1/T3 (§3.3, §3.5, §3.6, §4.1, §4.3) + nháp §3.2, §4.2 (📝 AI nháp) | `<SV viết>` | `<SV viết>` |
| R2 | Test summary README + report §8 | `<SV viết>` | `<SV viết>` |
| R3 | Khung AI-02, AI-03, khối Mandatory Disclosure §11 | `<SV viết>` | `<SV viết>` |
| E1 | Mô tả môi trường (`env/environment.md`) | `<SV viết>` | `<SV viết>` |

## 4. Kết luận chung

`<SV viết>`

## 5. AI Critique

Xem report chính `23120255_HW03_Report.md` §10.

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
