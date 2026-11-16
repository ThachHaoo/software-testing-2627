# HW04/CLAUDE.md — Automation Testing on EShop (đang làm)

Phần chung (vai trò, khối báo cáo, giới hạn AI, prompt log, git, zip, SUT) ở `CLAUDE.md` gốc. File này chỉ giữ phần riêng HW04.

## 1. Đề và rubric

- Đề: `context/HW04_assignment.md` (pdftotext từ `2026.HW04.Automation Testing_En.pdf`, bản PDF: `context/HW04_assignment.pdf`).
- Bloom-AI **G9.2 (Apply) + G9.3 (Analyse) + G9.4 (Collaborate)**. Deadline **11:00 18/11/2026** (Moodle).
- Không nộp trễ; thiếu tài liệu bắt buộc = 0 điểm; chép giữa SV (kể cả prompt) = 0. 30% SV có thể bị gọi vấn đáp 5–7 phút tuần sau deadline.

| # | Mục | Điểm |
|---|---|---|
| 1 | Task 1 – Feature A (FR-01) | 25 |
| 1 | Task 1 – Feature B (FR-07) | 25 |
| 1 | Task 1 – Feature C (FR-15) | 25 |
| 2 | Task 2 – Demo video | 15 |
| 3 | Agent Skills | 10 |

Zip: `23120255_HW04_AI_Automation_<ggg>.zip` (ggg ∈ [000, 100]). Biểu mẫu AI-02→AI-06: xác định theo skill `cs423-ai-first-homework` (chưa chốt).

## 2. Yêu cầu của đề (tóm tắt, đối chiếu đề khi viết report)

**Feature**: đúng 3 feature web đã chọn ở HW02 — A **FR-01** (Đăng ký, web :5173), B **FR-07** (Giỏ hàng, web :5173), C **FR-15** (Quản lý sản phẩm, admin :5174). Không dùng Pool D.

**Task 1 – script tự động do AI sinh**
- Mỗi feature ≥ **12 TC** chuyển thành script, AI dẫn **từng bước** (không một prompt chung chung). Positive/negative/edge đều tính.
- **Data-driven**: dữ liệu test ở file `.csv`/`.json` riêng — mảng/đối tượng inline trong script **không được chấp nhận**. Dùng ≥ **3 kiểu assertion khác nhau**.
- Chạy ≥ **3 trình duyệt** (Chromium/Firefox/WebKit); mỗi feature chạy đủ 3 → ≥ **9 lượt chạy**. Mỗi lượt có **HTML report** hiện rõ **"Run by: 23120255"** kèm **ISO timestamp** (🔒 không AI sinh/bịa report).
- **Review + sửa**: báo AI sai/sót gì (selector mong manh, assertion yếu/thiếu, thiếu edge case, wait flaky) và **vì sao** (prompt, giới hạn model, đặc điểm feature).
- Chạy end-to-end; assertion fail lộ **defect thật** → bug report trong report Markdown **và** GitHub Issues, mỗi issue có ảnh. Liệt kê TC không tự động được + lý do.

**Task 2 – video demo**: YouTube unlisted ≥ **5 phút**, thuyết minh **tiếng Việt** (giọng SV 🔒), chạy một script end-to-end gồm lượt đa trình duyệt + HTML report; kể ≥ 1 chỗ đã sửa script AI; có face-cam **hoặc** terminal chạy `whoami` và `hostname`.

**Agent Skill** (khuyến khích, 10 đ): skill áp dụng quy trình này (sinh + bảo trì script data-driven, đa trình duyệt) + video YouTube dùng skill trên một feature trọn vẹn.

**Audit/Critique**: AI Audit Report (tên công cụ, ngày giờ, prompt, output); AI Critique 200–300 từ (🔒 SV viết).

**Git**: repo GitHub **public**, ≥ **8 commit có sửa file test script** (`.spec.ts`…); commit chỉ README/PDF/tài liệu không tính. Commit log dạng text.

**Zip gồm**: report chính (.md + PDF, có automation report + review/gap analysis script AI); link repo public; HTML report đa trình duyệt; link video; AI Critique + Audit (.md + PDF); commit log; bug report + ảnh trang Issues; `README.md` có bảng tự chấm + test summary (số feature; số TC automated/executed/passed/failed; số lượt chạy; số bug; link video).

## 3. Môi trường

- SUT `../eshop-sut` nhánh **main @ de0f48f** (đã chuyển từ `usability-tunnel` 16/11). Backend :3000, web :5173, admin :5174.
- Bộ test: `HW04/tests/` — `@playwright/test` **1.65.1**, project `chromium`/`firefox`/`webkit`, `workers: 1`, `retries: 0`, `globalSetup` kiểm SUT.
- Report: `HW04/reports/<project>_<YYYYMMDDTHHMMSS>/` (Playwright HTML; tiêu đề + metadata `Run by: 23120255 · <ISO>`). Mỗi lượt một trình duyệt: `npm run test:chrome` (…`edge`, `firefox`), `npm run test:all` chạy lần lượt cả 3.

## 4. Mâu thuẫn / điểm cần quyết định

- **M1** – Đề §12 yêu cầu repo **public** ↔ CLAUDE.md gốc ghi private → đã chốt: repo đã public (16/11), sửa CLAUDE.md gốc.
- **M2** – Deadline thật: 11:00 18/11/2026 (Moodle).

## 5. Quyết định

- **W1 = a** (16/11): WebKit bị Windows Smart App Control chặn → dùng **Chrome / Edge / Firefox** (đề §6 cho phép). Project `chrome` (channel `chrome`), `edge` (channel `msedge`), `firefox`.
- **Quy trình**: skill `playwright-ddt-automation` (`.claude/skills/`), 6 bước/feature, commit `HW04[X-FRnn] k/6: …`; output AI freeze vào `HW04/appendix/ai-outputs/<X_FRnn>/step<k>/` trước khi SV sửa.

## 6. Giới hạn riêng HW04 (bổ sung mục 3 của `CLAUDE.md` gốc)

- Quy tắc chung giữ nguyên: AI-01; **không amend**; **bug report + nội dung Issue do SV viết** (AI chỉ kiểm trường thiếu, chạy `gh issue create --body-file` với file SV viết); prompt log trích tự động (`tools/hw.toml` → `HW04/appendix/`), không sửa tay `A_prompt_log.md`, không sửa `appendix/ai-outputs/`.
- **HTML report** 🔒: chỉ sinh từ lượt chạy thật trên máy SV; AI không sửa nội dung report, không sửa `Run by`/timestamp sau khi chạy.
- **Bước SV review/sửa script** 🔒: AI không gợi ý edge case/selector/assertion còn thiếu trong lúc SV review; phần "AI sai/sót gì, vì sao" do SV viết.
- Script AI nháp → freeze vào `HW04/appendix/ai-outputs/` **trước** khi SV sửa (để diff được trong gap analysis).
- Video: AI không viết lời thuyết minh.
- Assertion fail ≠ bug: cô lập nguyên nhân (chạy lại, reset CSDL bằng restart backend, so UI với API); fail vì timeout/harness → Blocked, không lập bug.

## 7. Quy trình và mẫu commit

Commit chung: `HW04: …`. Bước theo feature: `HW04[A-FR01] k/6: …`, `HW04[B-FR07] k/6: …`, `HW04[C-FR15] k/6: …`; sửa ở bước 5: `HW04[X-FRnn] 5/6x – sửa: …` (mỗi lần sửa một commit có sửa `.spec.ts`). Chi tiết: SKILL.md của skill. Nhớ: ≥ 8 commit phải chạm file `.spec.ts`.
