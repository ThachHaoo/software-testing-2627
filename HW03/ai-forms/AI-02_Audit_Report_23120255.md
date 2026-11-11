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
| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — Claude Sonnet 4.6 3 lượt; Claude Opus 5.5 193 lượt; Claude (không rõ model) 8 lượt (tổng 204 lượt theo dòng Tổng của `appendix/A_prompt_log.md`, bản trích 11:05 11/11/2026) |
| Có sử dụng AI: | [x] Có [ ] Không |

**Tuyên bố sử dụng AI (đề):** xem report chính §11 Mandatory Disclosure.

## 2. Hướng dẫn

- Mỗi artifact do AI tạo là 1 hàng. Mục (1) Prompt + công cụ + thời gian + mã `#n`, (2) Output, (5) Bản SV sửa ở bảng 3.1; mục (3) Verdict và (4) Lý do ở bảng 3.2 (em viết).
- Prompt và output nguyên văn: `appendix/A_prompt_log.md` theo mã `#n`; output dạng file đóng băng: `appendix/ai-outputs/`.
- Cột #n để "–" tới lần trích prompt log cuối (gồm transcript phiên claude.ai).

## 3. Bảng Audit — 1 hàng / artifact

### 3.1 Mục (1), (2), (5)

| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |
|---|---|---|---|---|
| H1 | Harness HW03: `HW03/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp), khung report/README | Claude Code · 04/11/2026 18:12 · `24f1345` (HW03: tách CLAUDE.md theo bài – thêm HW02/HW03 CLAUDE.md (bỏ chặn của gitignore toàn cục)) · #21–#23 | khung bài, quyết định, khai Audit · `HW03/CLAUDE.md`, `HW03/report_plan.md` | `d7dc423` HW03: X1, X2 – ghi quyết định vào report_plan mục e; `9463442` HW03[T1] 2/6: vá CL-07; `1172c20` HW03[T1] 3/6b: C1, H1, P3A; `99a64dc` HW03: deadline thật 11/11 10:00; … (+19) |
| T1 | Khảo sát control C2 (`c2_inventory.md`) | Claude Code · 04/11/2026 17:49 · `39f685c` (HW03[T1] 1/6: AI nháp checklist C2) · #17 | inventory màn Đăng nhập, Quên MK, Hồ sơ, Lịch sử đơn, navbar · `HW03/checklist/c2_inventory.md` | không có |
| T2 | Checklist nháp 3 nguồn – bản đóng băng v1 (bước 1) | Claude Code · 04/11/2026 17:49 · `39f685c` (HW03[T1] 1/6: AI nháp checklist C2) · #17 | 65 item · `HW03/appendix/ai-outputs/T1_checklist_ai_v1.json` | không có |
| T3 | Khung trống `sv_items.md` + kiểm cấu trúc item SV (`sv_items_check.md`) | Claude Code · 04/11/2026 19:29 · `de4c69a` (HW03[T1] 2/6c: AI trả lời vì sao bỏ sót) · #33 | khung trống; nội dung item SV do SV viết · `HW03/checklist/sv_items_check.md` | không có |
| T4 | Câu trả lời "vì sao AI bỏ sót" (sau khi SV commit item) | Claude Code · 04/11/2026 19:29 · `de4c69a` (HW03[T1] 2/6c: AI trả lời vì sao bỏ sót) · #33 | SV-01…SV-06 · `HW03/checklist/ai_gap_answer.md` | không có |
| T5 | Playwright C2 + oracle khoá sha1 + reporter + seed đơn | Claude Code · 04/11/2026 20:09 · `07982fc` (HW03[T1] 3/6: Playwright P1/P2 + RUN.md) · #42 | 59 item auto, 3 project P1/P2/P3 · `HW03/tests/C2.spec.ts`, `HW03/tests/lib.ts`, `HW03/tests/oracle.src.json` … | `1172c20` HW03[T1] 3/6b: C1, H1, P3A |
| T6 | `RUN.md` (phần chạy tay) + mẫu file lượt + `dom_probe.js` | Claude Code · 04/11/2026 20:09 · `07982fc` (HW03[T1] 3/6: Playwright P1/P2 + RUN.md) · #42 | 15/15/13 item chạy tay · `HW03/checklist/RUN.md`, `HW03/tests/gen_run.py`, `HW03/checklist/dom_probe.js` … | `1172c20` HW03[T1] 3/6b: C1, H1, P3A; `9dfb111` HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59; `107b67f` HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt; `61858d4` HW03[T1] 4/6a2: sửa nhãn ảnh B3/B4, M5 dùng ảnh M3/M4; … (+1) |
| T7 | Kiểm ảnh/kết quả chạy tay (`run_check.md`), nén + đổi tên ảnh | Claude Code · 10/11/2026 02:45 · `107b67f` (HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt) · #66–#73 | R1–R12, L1–L8 · `HW03/checklist/run_check.md`, `tools/compress_hw03.py` | `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `4b4c64c` HW03[T1] 4/6d: R4; `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64 |
| T8 | Gộp lượt auto + tay vào `checklist.json` (V1, override theo quyết định SV) + `checklist.md` | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · #75 | kết quả P1/P2/P3 · `tools/merge_hw03.py` | `0679e25` HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện); `d811ea2` HW03: cập nhật skill theo cách làm thực tế; `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2; … (+1) |
| T9 | Excel 3 sheet | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · #75 | Test Cases / Checklist / Test Summary Report · `HW03/excel/23120255_HW03_Checklist.xlsx` | `0679e25` HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện); `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2 |
| T10 | Danh sách Failed + đối chiếu trùng issue theo tiêu đề (`failed_list.md`, `issues.json`, `issue_dup_FR02.md`) | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · #75 | trùng 14 / một phần 4 / MỚI 28 · `HW03/bugs/failed_list.md`, `HW03/bugs/issues.json`, `HW03/checklist/issue_dup_FR02.md` … | `0679e25` HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện); `3ab505e` HW03[T1] 5/6b: SV chốt nhóm bug; `d811ea2` HW03: cập nhật skill theo cách làm thực tế; `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; … (+1) |
| T11 | Nhóm dữ kiện bug + khung BUG-58…85 (chỉ dữ kiện) | Claude Code · 10/11/2026 03:07 · `0679e25` (HW03[T1] 5/6a: quyết định treo + khung bug (dữ kiện)) · #76–#77 | 28 nhóm (SV chốt), 28 khung · `HW03/bugs/bug_groups.md`, `tools/bug_groups_hw03.py` | `3ab505e` HW03[T1] 5/6b: SV chốt nhóm bug; `d811ea2` HW03: cập nhật skill theo cách làm thực tế; `090cabb` HW03[T1] 4/6c: SV chốt R9, R11; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2 |
| T12 | Danh sách ảnh thiếu (`missing_photos.md`) | Claude Code · 10/11/2026 18:51 · `9ede85b` (HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02) · #105 | đối chiếu RUN.md/report · `HW03/checklist/missing_photos.md` | `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64; `6069790` HW03[T1] 4/6f: ảnh tổng quan P3 |
| B1 | Kiểm trùng 179 issue nhóm (`dup_check.md`; AI đề xuất mức, SV quyết) | Claude Code · 10/11/2026 18:37 · `e9a2c85` (HW03[T1] 5/6c: kiểm trùng issue (khung bug chờ chốt tiền tố)) · #100–#102 | trùng / một phần / mới theo item Failed · `HW03/bugs/dup_check.md` | không có |
| B2 | Khung BUG-58…85 theo mẫu HW02 (chỉ dữ kiện) + script `bug_skeleton_hw03.py` | Claude Code · 10/11/2026 18:51 · `9ede85b` (HW03[T1] 5/6c: kiểm trùng issue + khung bug theo mẫu HW02) · #105 | 28 file khung; Tiêu đề/Steps/Severity… để SV viết · `tools/bug_skeleton_hw03.py` | không có |
| B3 | Kiểm dữ kiện 28 bug + tái hiện Steps SV bằng Playwright (`bug_check.md`, `repro_bugs.spec.ts`) | Claude Code · 10/11/2026 20:33 · `715c4eb` (HW03[T1] 5/6e: kiểm dữ kiện + tái hiện bug (AI)) · #130 | sạch 14 / còn điểm 14; P1, P2 · `HW03/bugs/bug_check.md`, `HW03/tests/repro_bugs.spec.ts`, `HW03/tests/repro.config.ts` … | không có |
| B4 | Kiểm lại 14 bug SV sửa (`bug_check2.md`) | Claude Code · 11/11/2026 07:51 · `de6882e` (HW03[T1] 5/6g: kiểm lại 14 bug SV sửa (AI)) · #177 | đã xử lý 6 / còn điểm 8 · `HW03/bugs/bug_check2.md` | không có |
| B5 | Tạo 28 GitHub Issue bằng `gh issue create --body-file` (file SV viết) + ghi link vào BUG-xx, README, report | Claude Code · 11/11/2026 05:18 · `bf715c0` (HW03[T1] 6/6: link GitHub Issue #247–#260 cho 14 bug) · #167–#169 | #247–#274 trên tkob-team/eshop-sut · `HW03/README.md` | `77a351f` HW03[T1] 6/6: link GitHub Issue #261–#274 cho 14 bug còn lại; `0185a48` HW03: SV tự chấm; `066cf3c` HW03: SV sửa căn cứ tự chấm |
| B6 | Sửa body issue #266 + comment theo lệnh SV (`issue_edits.md`) | Claude Code · 11/11/2026 08:11 · `99a9e27` (HW03[T1]: khôi phục dữ kiện BUG-72 (#266)) · #181 | nhật ký lệnh `gh issue edit`/comment · `HW03/bugs/issue_edits.md` | không có |
| B7 | Ảnh trang Issues `[HW03-C2]` (Playwright chụp) chèn report §6 | Claude Code · 11/11/2026 08:13 · `08fe5ab` (HW03[T1]: ảnh trang Issues) · #181 | 25 + 3 issue · `HW03/bugs/issues_page_HW03-C2_1.png`, `HW03/bugs/issues_page_HW03-C2_2.png` | không có |
| U1 | Gói usability nháp – bản đóng băng (plan 9 phần, participant kit, phiếu quan sát) | Claude Code · 04/11/2026 17:51 · `c081f96` (HW03[T2] 1/10: AI nháp gói usability) · #17 | chưa dùng trong phiên thật · `HW03/appendix/ai-outputs/T2_plan_v1.md`, `HW03/appendix/ai-outputs/T2_participant_kit_v1.md`, `HW03/appendix/ai-outputs/T2_observation_sheet_v1.md` | không có |
| U2 | Môi trường usability từ xa (script phiên, tunnel, đưa SUT về main) + sửa plan mục 5–6 | Claude Code · 10/11/2026 03:22 · `4199810` (HW03[T2] 2b/10: môi trường usability từ xa (tunnel)) · #82–#85 | nhánh local `usability-tunnel` trong eshop-sut (không nộp) · `tools/usability_session.ps1`, `tools/sut_main.ps1`, `tools/restart_backend.ps1` … | `2485116` HW03[T2] 2d/10: plan theo phiên 10 phút + Google Form |
| U3 | Google Form SEQ + SUS + 4 câu hỏi mở (Apps Script – phiên thảo luận claude.ai) | Claude Code · 10/11/2026 19:36 · `2485116` (HW03[T2] 2d/10: plan theo phiên 10 phút + Google Form) · #118–#128 | form trên Google, không có file trong repo; CSV trả lời không commit · `HW03/usability/plan.md` | không có |
| U4 | Kịch bản điều phối `moderator_script.md` (phiên thảo luận nháp, Claude Code commit nguyên văn) | Claude Code · 10/11/2026 19:36 · `70f26ef` (HW03[T2] 2c/10: kịch bản điều phối (AI nháp)) · #118–#128 | phiên ~10 phút · `HW03/usability/moderator_script.md` | không có |
| U5 | Phiếu phiên S00…S07.json AI chép từ notes SV + CSV (`usability_fill_hw03.py`) | Claude Code · 11/11/2026 00:49 · `750cfdd` (HW03[T2] 2/10: pilot S00) · #158 | nhãn "AI chép, SV duyệt"; thời gian/hoàn thành/trợ giúp SV điền · `tools/usability_fill_hw03.py`, `HW03/usability/sessions/S00.json` | `d9919c9` HW03[T2] 10/10: số liệu U1 |
| U6 | Đối chiếu 7 pain point §5.8 ↔ issue nhóm (chỉ đọc, trả lời trong phiên) | Claude Code · 11/11/2026 08:39 · `afc81da` (HW03[T2]: SV ghi issue liên quan vào findings) · #184 | bảng trùng / liên quan / chưa có; SV tự ghi vào report · `HW03/23120255_HW03_Report.md` | `f96dfb2` HW03[T2]: Thêm quy định Severity; `cf4e6b7` HW03[T1]: SV viết §3.4 – item bổ sung + vì sao AI bỏ sót; `557c0fe` HW03[T1]: SV sửa §3.4 theo kiểm dữ kiện; `1d0683b` HW03[T1]: SV sửa câu từ 3.4; … (+14) |
| S1 | Agent Skill `gui-checklist-testing` (SKILL.md, reference, asset, 8 script) | Claude Code · 10/11/2026 18:25 · `fcab9e1` (HW03[Skill] 1/3: chép skill + VideoLinks) · #92–#97 | chép từ `.claude/skills/` · `HW03/skills/gui-checklist-testing` | `0d8fd34` HW03[Skill] 1/3b: D1; `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2 |
| S2 | Agent Skill `usability-evaluation` (SKILL.md, reference, asset, 6 script) | Claude Code · 10/11/2026 18:25 · `fcab9e1` (HW03[Skill] 1/3: chép skill + VideoLinks) · #92–#97 | chưa dùng trên phiên thật · `HW03/skills/usability-evaluation` | không có |
| S3 | `skills/VideoLinks.md` + đề xuất demo (`demo_plan.md`, không nộp) | Claude Code · 10/11/2026 18:25 · `fcab9e1` (HW03[Skill] 1/3: chép skill + VideoLinks) · #92–#97 | link `<SV điền>` · `HW03/skills/VideoLinks.md`, `HW03/skills/demo_plan.md` | `5cd2ebb` HW03[Skill] 3/3: link video demo |
| R1 | Bảng report T1/T3 (§3.3, §3.5, §3.6, §4.1, §4.3) | Claude Code · 10/11/2026 02:55 · `3ee3158` (HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed) · #75 | khối giữa marker REPORT:T1 · `tools/report_t1_hw03.py` | `ad992bc` HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2; `4b4c64c` HW03[T1] 4/6d: R4; `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64 |
| R4 | AI nháp report §3.2, §4.2 (📝 AI nháp – SV duyệt/sửa) | Claude Code · 10/11/2026 18:42 · `ad992bc` (HW03: report T1/T3 – bảng + AI nháp 3.2, 4.2) · #102 | chỉ dùng dữ kiện trong repo · `HW03/23120255_HW03_Report.md` | `4b4c64c` HW03[T1] 4/6d: R4; `f6e85c3` HW03[T1] 4/6e: M6 + tham chiếu CL-64; `6069790` HW03[T1] 4/6f: ảnh tổng quan P3; `c51665d` HW03: report §5 – không có phiên usability; … (+30) |
| R2 | Test summary README + report §8 (11/11 thêm dòng U1 từ phiếu phiên) | Claude Code · 10/11/2026 19:05 · `70aa585` (HW03: README test summary (script) + chỗ tự chấm) · #114 | khối SUMMARY · `tools/summary_hw03.py` | `d9919c9` HW03[T2] 10/10: số liệu U1 |
| R3 | Khung AI-02, AI-03, khối Mandatory Disclosure §11 | Claude Code · 10/11/2026 19:07 · `c2aa7ae` (HW03: khung AI-02, AI-03 + Mandatory Disclosure §11 (script)) · #114 | file này · `tools/forms_hw03.py` | `d4fa9e4` HW03: AI-02 – thêm artifact AI từ tối 10/11, cột #n theo prompt log; `47b96b1` HW03: AI-03 – số lượt theo dòng Tổng, lượt không rõ model chờ lý do; `f33f7d5` HW03: §11 Mandatory Disclosure + report_plan f/g – việc AI từ tối 10/11, dòng CSV (AI-05) |
| E1 | Mô tả môi trường (`env/environment.md`) | Claude Code · 05/11/2026 02:26 · `1172c20` (HW03[T1] 3/6b: C1, H1, P3A) · #43–#48 | phiên bản trình duyệt/OS/thiết bị · `HW03/env/environment.md` | `107b67f` HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt |

*34 artifact. Sinh bằng `tools/forms_hw03.py` từ danh mục trong script + `git log` (commit tạo = commit đầu tiên thêm file chính – đường dẫn đầu ở cột (2)). Cột (5) chỉ liệt kê commit, không diễn giải.*

### 3.2 Mục (3), (4) – em điền

*Verdict: VALID / INVALID / INCOMPLETE. Lý do: 1–2 câu, dẫn ISTQB/slide. #n để mở `appendix/A_prompt_log.md`.*

| Mã | #n | (3) Verdict | (4) Lý do |
|---|---|---|---|
| H1 | #21–#23 | VALID | Khung bài và kế hoạch tuân thủ đúng yêu cầu đề bài; SV đã chủ động bổ sung các quyết định X1, X2 và điều chỉnh mốc thời gian hoàn thành. |
| T1 | #17 | VALID | Bảng khảo sát control liệt kê chính xác các phần tử JSX thực tế trong mã nguồn C2; làm cơ sở dữ liệu đầu vào chuẩn xác để đối chiếu checklist. |
| T2 | #17 | INCOMPLETE | Bản nháp v1 có 20 item thuộc nhóm "Both" (AI + SV sửa) và 6 item SV bổ sung; đồng thời có sự thiên lệch về SRS như đã nêu trong Critique. |
| T3 | #33 | INCOMPLETE | Khung `sv_items.md` dựng đúng cấu trúc nhưng thiếu trường `loai_nguon` (L2) và báo 12 lỗi khi chạy script kiểm tra, đúng như điểm hạn chế đã nêu trong Critique. |
| T4 | #33 | VALID | AI phân tích và tự nhận diện chính xác các nhóm nguyên nhân bỏ sót dựa trên 3 nguồn prompt; cung cấp dữ kiện đối chiếu minh bạch cho §3.4. |
| T5 | #42 | INCOMPLETE | Mã tự động hóa sinh ra hữu ích nhưng có sai sót làm lệch kết quả (ép locale `vi-VN` làm sai CL-08, so tọa độ sai CL-11 và ghi nhầm TimeoutError của harness vào SV-06 trên P3 như Critique đã nêu). |
| T6 | #42 | INCOMPLETE | Kế hoạch `RUN.md` giúp định hướng chạy tay nhưng phần M6 mâu thuẫn chính nó và đã được SV sửa lại trong quá trình thực thi. |
| T7 | #66–#73 | VALID | Script kiểm tra và nén ảnh tự động vận hành chính xác; đảm bảo toàn bộ ảnh chứng minh kết quả chạy tay P1/P2/P3 khớp đúng với nhật ký kiểm thử. |
| T8 | #75 | VALID | Script gộp kết quả `merge_hw03.py` xử lý chính xác quy tắc ghi đè (override) từ lượt chạy tay của SV, đảm bảo tính toàn vẹn dữ liệu kết quả kiểm thử. |
| T9 | #75 | VALID | File Excel 3 sheet xuất ra đầy đủ, đúng cấu trúc mẫu báo cáo kiểm thử chuẩn; các công thức tổng hợp số liệu chính xác theo kết quả gộp. |
| T10 | #75 | VALID | Danh sách lỗi Failed và kết quả gom nhóm trùng issue khớp với SRS và các lỗi đã biết trên repository gốc. |
| T11 | #76–#77 | INCOMPLETE | Khung bug do AI dựng cần phải được tái cấu trúc lại theo đúng mẫu quy định của HW02 (B2) và bổ sung thiếu sót trường hợp P1 ở BUG-80. |
| T12 | #105 | VALID | Danh sách rà soát ảnh minh họa phản ánh đúng các vị trí còn thiếu, giúp SV nhanh chóng bổ sung ảnh thực tế trên P3. |
| B1 | #100–#102 | VALID | Kết quả đối chiếu 179 issue có sẵn hỗ trợ SV đánh giá chính xác các lỗi trùng lặp và lỗi mới phát sinh. |
| B2 | #105 | VALID | Script sinh khung bug hoạt động chính xác theo mẫu HW02, đảm bảo tính nhất quán trong hồ sơ báo cáo lỗi. |
| B3 | #130 | VALID | Kịch bản tự động tái hiện bug (`repro_bugs.spec.ts`) xác nhận chính xác trạng thái lỗi trên P1/P2. |
| B4 | #177 | INCOMPLETE | Bản kiểm tra này chỉ rà soát câu chữ sửa đổi của SV trong file bug chứ không phải lỗi SUT được sửa, vì mã nguồn SUT không thay đổi. |
| B5 | #167–#169 | VALID | Tự động hóa tạo 28 GitHub Issue (#247–#274) thành công; các liên kết tham chiếu được chèn chính xác vào tài liệu báo cáo. |
| B6 | #181 | VALID | Nhật ký cập nhật issue ghi chép đầy đủ các thao tác chỉnh sửa body và comment; đảm bảo tính truy vết của hồ sơ quản lý lỗi. |
| B7 | #181 | VALID | Ảnh chụp danh sách GitHub Issue minh chứng đầy đủ số lượng lỗi đã được đăng tải công khai trên repository dự án. |
| U1 | #17 | INCOMPLETE | Gói tài liệu nháp không bị bỏ hoàn toàn mà vẫn được tận dụng: form và kịch bản dùng lại từ kit, plan chỉ cần chỉnh sửa mục 3 và 5 cho phiên 10 phút. |
| U2 | #82–#85 | VALID | Môi trường test từ xa và các script điều khiển backend vận hành ổn định, tạo điều kiện thuận lợi cho người tham gia thử nghiệm thực tế. |
| U3 | #118–#128 | VALID | Mẫu biểu khảo sát Google Form (SEQ + SUS + câu hỏi mở) thu thập chính xác cả định lượng lẫn định tính theo phương pháp của Rubin & Chisnell. |
| U4 | #118–#128 | VALID | Kịch bản điều phối `moderator_script.md` thiết kế hợp lý, giữ thời lượng phiên trong mức 10 phút và không dẫn dắt người tham gia. |
| U5 | #158 | VALID | Script tổng hợp dữ liệu từ phiếu ghi chép và CSV hoạt động chính xác; bảo đảm dữ liệu khảo sát người dùng được ghi nhận trung thực. |
| U6 | #184 | VALID | Bảng đối chiếu 7 pain point trải nghiệm người dùng với các issue nhóm phản ánh đúng mối liên hệ giữa lỗi giao diện và cảm nhận người dùng. |
| S1 | #92–#97 | VALID | Agent Skill `gui-checklist-testing` chứa đầy đủ các kịch bản kiểm thử GUI per-control và tài liệu tham khảo theo đúng chuẩn cấu trúc skill. |
| S2 | #92–#97 | INCOMPLETE | Skill này áp dụng cấu trúc kế hoạch 9 phần theo tài liệu của Rubin & Chisnell và slide môn học. |
| S3 | #92–#97 | VALID | File tham chiếu video được cấu trúc đúng quy định, sẵn sàng chứa link minh chứng sau khi hoàn tất quay video demo. |
| R1 | #75 | VALID | Bảng tổng hợp báo cáo T1/T3 xuất chính xác số liệu từ kết quả gộp; đảm bảo các con số thống kê nhất quán toàn bộ báo cáo. |
| R4 | #102 | VALID | SV đã duyệt và giữ nguyên bản nháp do commit duyệt eb9c78a chỉ thực hiện xoá 2 dòng 📝 mà không thay đổi câu chữ nào. |
| R2 | #114 | VALID | Script cập nhật file README và §8 báo cáo tự động tính toán chính xác các chỉ số bao phủ và tỷ lệ đạt/nối của bài kiểm thử. |
| R3 | #114 | VALID | Khung báo cáo minh bạch AI (AI-02, AI-03) sinh ra đúng cấu trúc mẫu quy định; hỗ trợ kê khai chi tiết các lượt tương tác AI. |
| E1 | #43–#48 | VALID | Tài liệu mô tả môi trường kiểm thử `environment.md` ghi nhận đầy đủ chi tiết phiên bản OS, trình duyệt và thông số thiết bị thật P1/P2/P3. |

## 4. Kết luận chung

Quá trình ứng dụng AI (Claude Code và Claude.ai) trong bài tập HW03 đã mang lại cho em hiệu quả cao trong việc tự động hóa các công việc lặp đi lặp lại như: dựng khung tài liệu, viết script Playwright tự động hóa kiểm thử GUI, tổng hợp báo cáo Excel 3 sheet, và tự động tạo 28 GitHub Issues trên repository SUT. Việc em lưu trữ lịch sử tương tác và đóng băng các bản nháp (v1) giúp duy trì tính minh bạch và khả năng truy vết dữ liệu toàn diện theo đúng chính sách sử dụng AI của môn học.

Tuy nhiên, kết quả audit cho em thấy AI không thể thay thế vai trò chủ đạo của sinh viên trong quá trình kiểm thử chất lượng phần mềm. AI bộc lộ rõ những hạn chế như: thiên lệch quá mức vào tài liệu SRS mà bỏ sót các quy tắc thiết kế trong slide (Golden Rule), thiếu các tiêu chí WCAG về tương phản, focus, kích thước vùng bấm (WCAG/Accessibility), ghi nhận sai trạng thái lỗi do thiết lập môi trường Playwright (locale vi-VN), và hoàn toàn không thể dự đoán được các hành vi thực tế trên thiết bị di động thật (bàn phím ảo, hiển thị focus ring, dán dữ liệu). Đặc biệt ở Task 2 (Usability Testing), AI không thể thay thế em trong vai trò người quan sát thực tế vì toàn bộ các điểm nghẽn trải nghiệm (pain point) cốt lõi em thu được đều xuất phát từ cảm nhận của người dùng thật. Em đã giữ vai trò quyết định trong việc kiểm soát dữ liệu, điều chỉnh các câu lệnh script, trực tiếp thực thi kiểm thử trên thiết bị thật, tự tay viết 6 item bổ sung SV-01…SV-06, và trực tiếp điều phối các phiên thử nghiệm usability để hoàn thành bài tập.

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
