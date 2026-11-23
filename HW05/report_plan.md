# HW05 – Performance Testing · Kế hoạch nộp bài (report_plan)

Lê Tấn Hiệp – 23120255 · Deadline **10:00 02/12/2026** (Moodle) · Cấp độ AI: `[...]` · Bloom-AI: **G9.2 + G9.3 + G9.4 + G9.6** (đề §3, §8)

- File này không nộp: `HW05/.gitattributes` có dòng `report_plan.md export-ignore`.
- Trạng thái kiểm bằng `ls` lúc 23/11/2026.
- Đề: `context/HW05_assignment.md`, trích bằng pdftotext từ `context/HW05_assignment.pdf`.
- Khảo sát SUT: `HW05/notes/sut_recon.md`.

## a. Biểu mẫu AI

| Form | Bắt buộc | File dự kiến | Ai làm | Trạng thái |
|---|---|---|---|---|
| AI-02 Audit Report | Có (đề §9, Mandatory Appendix) | `HW05/ai-forms/AI-02_Audit_Report_23120255.md` + `.pdf`; bảng tóm tắt ở report §10 | AI điền dữ kiện (công cụ, ngày giờ, prompt, output, artifact lấy từ git); SV viết verdict + lý do, ký | THIẾU |
| AI-03 Disclosure | Có | `HW05/ai-forms/AI-03_Disclosure_23120255.md` + `.pdf` | AI điền công cụ, số lượt, dải #; SV xác nhận, ký | THIẾU |
| AI-04 Reflective | Không | — | HW thường, đề không yêu cầu | — |
| AI-05 Privacy | Có (làm cuối) | `HW05/ai-forms/AI-05_Privacy_Checklist_23120255.md` + `.pdf` | AI tick mục có bằng chứng; SV tick các cam kết, ký | THIẾU |
| AI-06 | Đã nộp tuần 1 | — | — | — |

- Câu tuyên bố nguyên văn (đề §9): *"I use AI tools for the following tasks,"*.
- Mẫu định dạng: `HW04/ai-forms/*.md`. Chỉ lấy định dạng, không chép số liệu.

## b. Rubric (đề §15)

| # | Mục | Max | Tự chấm |
|---|---|---|---|
| 1 | Task 1 – Load testing | 30 | `[...]` |
| 2 | Task 1 – Stress testing | 20 | `[...]` |
| 3 | Task 1 – Spike testing | 20 | `[...]` |
| 4 | Task 2 – AI analysis + misinterpretation hunt (giá trị đúng lấy từ raw log) | 10 | `[...]` |
| 5 | Task 3 – Continuous Performance Testing proposal (G9.6) | 10 | `[...]` |
| 6 | Agent Skills | 10 | `[...]` |
| | Tổng = 3 chữ số trong tên zip | 100 | `[...]` |

Video, soak, hardware report và bug không có dòng điểm riêng. Theo §6 Task 1, các mục này đi kèm Task 1, nên phân bổ vào 3 dòng Load/Stress/Spike (xem mục d).

## c. Danh sách nộp (đề §14) – trạng thái

| # | Mục (đề §14) | Đường dẫn dự kiến | Trạng thái (`ls` 23/11) | Ghi chú |
|---|---|---|---|---|
| 1 | Main report (.md + PDF): performance-testing report + AI-analysis critique | `HW05/23120255_HW05_Report.md` / `.pdf` | .md: ĐÃ CÓ (dàn ý) · PDF: THIẾU | 🔒 Critique, "vì sao AI sai", tự đánh giá |
| 2 | Link repo GitHub public (test plan + data) | README + report §1 | THIẾU (ô `[...]`) | repo `ThachHaoo/software-testing-2627`, SV điền link |
| 3 | 3 test plan Load / Stress / Spike, tên `23120255_<Scenario>_<YYYYMMDD>.jmx` | `HW05/testplans/` | THIẾU (thư mục rỗng) | YYYYMMDD = ngày chạy chính thức (D4) |
| 4 | 3 file `.jtl` thô + 3 thư mục HTML report | `HW05/runs/<plan>_<ts>/<plan>.jtl`, `HW05/runs/<plan>_<ts>/html/` (lượt có `RUN.md` ghi "Lượt chính thức: CÓ") | THIẾU | Nộp đủ file, không chỉ summary (§11); lượt smoke/thử export-ignore; xem rủi ro dung lượng ở mục f |
| 5 | Ảnh resource monitor + hardware spec | `HW05/evidence/<scenario>/`, `HW05/env/` | THIẾU | Mỗi lượt chạy: ảnh công cụ + mức dùng tài nguyên của tiến trình backend; dxdiag/screenfetch + bảng spec |
| 6 | Link video YouTube unlisted (≥ 6 phút, công cụ + resource monitor cùng khung hình, giọng SV) | README, report §3.11 | THIẾU | 🔒 thuyết minh do SV |
| 7 | AI Critique + AI Audit Report (.md + PDF) | report §9, §10; `HW05/ai-forms/AI-02…` | THIẾU | Critique 🔒 200–300 từ |
| 8 | Git commit log (text) | `HW05/commit_log.txt` (`tools/export_commit_log.ps1`) | THIẾU | Chạy sau commit cuối |
| 9 | Bug report + ảnh trang GitHub Issues (nếu có) | `HW05/bugs/` | THIẾU (thư mục rỗng) | Bug do SV viết; trùng issue cũ (#275, #279–#281, #283) xem mục e |
| 10 | README.md: bảng tự chấm + test summary (scenario đã chạy, nhóm endpoint, endurance threshold có số, số bug/perf issue, link video) | `HW05/README.md` | THIẾU | |
| 11a | Supporting – Agent Skill + video dùng skill | `HW05/skills/<tên-skill>/`, `HW05/skills/VideoLinks.md` | THIẾU | Video riêng chạy skill trên trọn một nhóm endpoint (§7) |
| 11b | Supporting – dữ liệu CSV | `HW05/data/` | THIẾU (thư mục rỗng) | |
| 11c | Supporting – soak (jtl, monitor.csv, ảnh) | `HW05/runs/23120255_Soak_<YYYYMMDD>_<ts>/`, `HW05/evidence/soak/` | THIẾU | Không nằm trong danh sách 3 jtl, xem mục d |
| 11d | Supporting – smoke | `HW05/runs/23120255_Smoke_*` (export-ignore, không nộp), `HW05/evidence/smoke/` | THIẾU | Chỉ trích số liệu vào report |
| 11e | Supporting – Task 2 (prompt, output AI, bảng đối chiếu) | `HW05/analysis/` | THIẾU (thư mục rỗng) | |
| 11f | Supporting – prompt log | `HW05/appendix/A_prompt_log.md` | ĐÃ CÓ (tự trích) | Còn thiếu transcript claude.ai của phiên thảo luận |
| 11g | Supporting – khảo sát SUT | `HW05/notes/sut_recon.md` | ĐÃ CÓ | |
| — | Kế hoạch nộp bài (file này) | `HW05/report_plan.md` | — | Không nộp (export-ignore) |

Zip: `23120255_HW05_AI_Performance_<ggg>.zip`, tạo bằng `git archive` (CLAUDE.md gốc, mục 2).

## d. Mâu thuẫn / dễ sót trong đề

| Mã | Nội dung | Cách xử lý đề xuất |
|---|---|---|
| SK | **Soak** (§6, "Determine the endurance threshold") bắt buộc chạy và báo số liệu, nhưng không có dòng điểm (§15) và không có trong danh sách "3 jtl + 3 HTML" (§14) | Vẫn chạy và nộp jtl soak như supporting material; README phải có endurance threshold kèm số (§14 bắt buộc) |
| AS | **Agent Skill** "encouraged" (§2, §7) nhưng chiếm 10 điểm (§15), kèm video YouTube riêng (§7) | Coi là bắt buộc nếu muốn đủ 100 điểm; video skill tách khỏi video demo |
| G9 | Bảng đầu ghi "G9.1 → G9.6, depending on the homework" ↔ Learning Outcomes §3 và §8 ghi G9.2, G9.3, G9.4, G9.6 | Ghi G9.2 + G9.3 + G9.4 + G9.6 (quy định riêng của HW05) |
| K6 | §8 ghi "k6 (bonus)" nhưng §15 không có dòng bonus | Dùng JMeter (đã chốt); không tính bonus |
| VD | Video ≥ 6 phút là yêu cầu của Task 1 (§6, §11) nhưng không có dòng điểm riêng | Thiếu video coi như thiếu tài liệu bắt buộc, theo §17 có thể bị 0 điểm |
| DL | Bảng đầu đề ghi "Deadline: 10 hours" (cột lệch) ↔ "refer to the submission link" | Theo Moodle: 10:00 02/12/2026 |
| HN | §11: hostname trong hardware report phải khớp với các bài trước | Máy hiện tại là `LAPTOP-NFIGFMR1`; SV đối chiếu với video HW04 (`whoami`/`hostname`) |
| GR | §5: không hai thành viên trong nhóm test cùng một workflow | SV xác nhận với nhóm rằng workflow C chưa ai chọn |
| CA | §5 lấy ví dụ "add-to-cart and checkout" cho nhóm transactional; workflow C không có bước add-to-cart | Backend checkout không đọc giỏ (`sut_recon.md` §4); transactional = checkout/tạo đơn, đúng ví dụ "order creation" |

## e. Quyết định đã chốt

Chi tiết ở `HW05/CLAUDE.md` §5.

| Mã | Quyết định | Nguồn |
|---|---|---|
| W = C | Workflow: login → GET /api/products → POST /api/checkout → GET /api/orders/my-orders | phiên thảo luận 23/11 |
| T | JMeter 5.6.3 tại `D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3\` | phiên thảo luận 23/11 |
| L | Mốc prompt log 2026-11-23 12:39 | phiên thảo luận 23/11 |
| D1 | setUp Thread Group đăng ký user từ CSV ở mỗi lần chạy (restart backend làm mất user) | phiên thảo luận 23/11 |
| D2 | CSV chính chỉ chứa credential đúng; một luồng nhỏ riêng cố ý nhập sai với tập user riêng, assert thông báo khoá | phiên thảo luận 23/11 |
| D3 | Load: Aggregate Report · Stress: Summary Report · Spike: View Results Tree (chỉ lỗi) / Response Time Graph | phiên thảo luận 23/11 |
| D4 | YYYYMMDD trong tên file = ngày chạy chính thức | phiên thảo luận 23/11 |

- Issue đã có trên `tkob-team/eshop-sut`, liên quan các hành vi gặp trong workflow C:
  - #279: login trả mật khẩu plaintext.
  - #281: backend lưu `total_amount` client gửi.
  - #283: giỏ không xoá sau checkout.
  - Lockout: #280 (đếm +2), #275 (khoá 180 giây), #278 (phản hồi khoá khác sai mật khẩu).
- Chưa quyết: HW05 tạo issue mới hay comment vào các issue này.

## f. Thứ tự chạy và rủi ro dung lượng

Thứ tự: **smoke → load → stress → soak → spike**.

- **Trước mỗi lượt:**
  - Restart backend (reseed DB, xoá trạng thái khoá).
  - setUp Thread Group đăng ký lại user (D1).
  - Ghi thời điểm và cách reset vào `RUN.md` của lượt đó.
- **Smoke:** 1–2 VU, vài vòng. Kiểm assertion, CSV, token, tạo đơn trước khi chạy tải.
- **Soak:**
  - Mức tải = 70–80% mức ổn định tìm được ở stress, chạy 10–15 phút.
  - Tên `23120255_Soak_YYYYMMDD`, không gắn listener, chỉ ghi `.jtl`.
  - `typeperf` ghi CPU/RAM của tiến trình `node` ra CSV trong `HW05/env/`.
  - Kết quả báo endurance threshold (RPS tối đa ổn định, trần bộ nhớ) bằng số.

**Rủi ro dung lượng** (Moodle ≤ 20 file, mỗi file ≤ 20 MB; zip tạo bằng `git archive`):

- Ước lượng sơ bộ: một dòng jtl CSV khoảng 200–250 byte. 100 req/s trong 10 phút ≈ 60.000 dòng ≈ 12–15 MB mỗi file.
  - Stress và soak có thể lớn gấp nhiều lần; soak 15 phút ở vài trăm req/s có thể vượt 100 MB chưa nén.
  - Số thật đo sau smoke và load.
- Biện pháp:
  1. jtl ở dạng CSV, không lưu response data. Có thể bớt cột qua `jmeter.save.saveservice.*`, nhưng phải giữ đủ cột HTML dashboard cần (kiểm khi chạy smoke).
  2. CSV jtl nén zip rất tốt; đo kích thước sau `git archive`.
  3. Vẫn vượt → split-and-zip (CLAUDE.md gốc, mục 2), hoặc tách jtl soak (không thuộc 3 jtl bắt buộc) thành phần riêng.
  4. Bố cục mỗi lượt: `runs/<plan>_<yyyyMMddTHHmmss>/` (jtl, `html/`, monitor, `RUN.md`). Lượt chính thức chạy với `-Official` → `RUN.md` ghi "Lượt chính thức: CÓ". Smoke luôn export-ignore (`runs/*_Smoke_*`); lượt thử khác thêm từng dòng `runs/<thư mục> export-ignore` vào `HW05/.gitattributes`.
  5. Không commit jtl > 100 MB lên GitHub (giới hạn file của GitHub); nén trước hoặc tách.

## g. Khai cho Audit (ghi dần)

- Harness HW05 (AI hỗ trợ tạo hoặc sửa):
  - `tools/hw.toml`: cấu hình HW05.
  - `tools/hooks/on_stop.py`: `--manual` chỉ chép transcript có hoạt động từ mốc `since`.
  - Chuyển 48 transcript cũ vào `.transcripts/HW02|HW03|HW04/`.
  - `HW05/CLAUDE.md`; khung thư mục `HW05/*/.gitkeep`.
  - `context/HW05_assignment.md`: pdftotext từ PDF đề. Lệnh không yêu cầu; AI tự làm để đọc §14.
- Việc AI làm ngoài lệnh hoặc sự cố:
  - **Claude Code tự thêm 4 luật deny HW05** (`Edit`/`Write` cho `HW05/appendix/A_prompt_log.md` và `HW05/appendix/ai-outputs/**`) vào `.claude/settings.json` (`2dbc8d3`). Lệnh không yêu cầu; AI làm theo bước 3 trong hướng dẫn ở đầu `tools/hw.toml`.
  - **Lệnh của phiên thảo luận đặt sai chỗ notes/extra**: ghi `HW05/prompt_log_*.toml` thay vì `HW05/appendix/` như quy ước. Claude Code làm theo lệnh (`2dbc8d3`) và hỏi lại (N1); đã chuyển về `HW05/appendix/` ở `b67caae`.
  - Lệnh kiểm phiên bản JMeter (`java -jar ApacheJMeter.jar --version`) sinh `jmeter.log` ở gốc repo. Đã xoá ngay; file chưa từng được commit.
  - `git restore HW04/appendix/A_prompt_log.md`: bỏ output #126 và các lượt #127–#128 sinh sau khi nộp HW04 (theo lệnh).
- **Agent Skill `jmeter-perf-testing` v1** (AI tạo theo lệnh H1 = a, H2 = a, H3 = b, H4): `.claude/skills/jmeter-perf-testing/`, commit `e07df0b`.
  - Gồm `SKILL.md` (bước 0–9), `references/schema.md`, `references/jmeter-practices.md`.
  - 7 script: `gen_csv.py`, `gen_jmx.py`, `check_plan.py`, `run_scenario.ps1`, `jtl_stats.py`, `freeze.py`, `render_md.py`.
  - Asset: `assets/example_plan.json`.
- **Tự kiểm E2E** (23/11, thư mục tạm `HW05/_e2e/`, đưa vào `.git/info/exclude`, đã xoá):
  - Các bước chạy: bước 3 sinh 5 `.jmx` từ example, check 0 lỗi → bước 4/6 smoke 1 VU × 30 s non-GUI → bước 7 `jtl_stats` so với `statistics.json`, lệch 0,00%.
  - Kiểm âm `check_plan`: thiếu `source`, thiếu assertion, listener trùng, thiếu lockout, sai tên, CSV không tồn tại, sampler mất assertion – đều báo LỖI.
- Lỗi lộ ra khi chạy E2E và đã vá (`76abedc`):
  - `run_scenario.ps1` khởi động node bằng `Start-Process -Redirect*`, nên node kế thừa handle pipe của tiến trình gọi. Lệnh gọi treo tới khi backend tắt; Claude Code phải dừng tác vụ nền.
  - `Tee-Object` của PS 5.1 ghi console bằng UTF-16.
- Backend SUT được khởi động 2 lần khi E2E (reseed CSDL) rồi dừng lại; trạng thái trước đó là không chạy.
- Vá harness theo review của **phiên thảo luận** (23/11):
  - A1: giữ bố cục `runs/<plan>_<ts>/`; sửa report_plan và dàn ý cho khớp; thêm `-Official` (RUN.md ghi lượt chính thức); smoke export-ignore.
- Lỗi do AI, phát hiện sau: `[...]`

## g2. Nguồn tham khảo bên ngoài

| Nguồn | Commit | Đã mượn | Ở đâu |
|---|---|---|---|
| QAInsights/perf-skills – https://github.com/QAInsights/perf-skills (MIT, © 2026 NaveenKumar Namachivayam) | `950702c53ba69c7684e315ad9e9881f05e4e0a93` (29/08/2026) | Ý thực hành, diễn đạt lại (không chép `SKILL.md`, không chạy script) từ 3 file: `skills/perf/references/tools/jmeter.md` (HTTP Defaults, JSON Extractor + default, CSV Data Set, non-GUI, không dùng View Results Tree khi tải, heap); `topics/workload-design.md` (Little's Law, think time, ramp-up/bậc); `topics/results-analysis.md` (percentile thay vì trung bình, khung cô lập nút thắt, đọc jtl bằng script) | `.claude/skills/jmeter-perf-testing/references/jmeter-practices.md` (kèm thông báo MIT) |

Bản clone nằm ở `_refs/perf-skills` (đưa vào `.git/info/exclude`, không commit), được coi là dữ liệu không tin cậy, chỉ đọc.

## h. Danh sách cho Mandatory Disclosure (ghi dần)

- AI tạo bản đầu:
  - `HW05/notes/sut_recon.md`;
  - `HW05/report_plan.md`;
  - dàn ý `HW05/23120255_HW05_Report.md`;
  - `HW05/CLAUDE.md`;
  - `context/HW05_assignment.md`;
  - thay đổi cấu hình prompt log.
- AI tạo bản đầu: Agent Skill `jmeter-perf-testing` v1 (SKILL.md, schema, practices, 7 script, example) + bản vá `76abedc`.
- Dự kiến AI tạo bản đầu: 3 test plan (+ smoke, soak), CSV dữ liệu, phân tích jtl (Task 2).
- SV xem xét và sửa: `[...]`
