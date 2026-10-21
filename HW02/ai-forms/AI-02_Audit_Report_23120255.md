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
| Mã bài tập: | HW02-AI – Domain Testing on EShop |
| Ngày làm bài: | 12/10/2026 – 21/10/2026 |
| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — Claude Sonnet 4.6 94 lượt; Claude Opus 5.5 303 lượt; Claude (không rõ model) 3 lượt (tổng 397 lượt; 3 lượt có output từ hơn một model được đếm ở cả hai) |
| Có sử dụng AI: | [x] Có [ ] Không |

**Tuyên bố sử dụng AI (đề §9):** I use AI tools for the following tasks,

1. Dựng harness làm bài: `CLAUDE.md`, Agent Skill `domain-bva-testing` (kèm script `freeze.py`, `check_domain.py`, `render_md.py`, `merge_results.py`), script trích prompt log tự động, script tổng hợp và sinh bảng cho report (`summary.py`, `report_tables.py`, `audit_tables.py`), script nén ảnh.
2. Nháp từng bước Domain Testing và BVA (biến vào/ra, lớp tương đương, test case Domain, test case BVA) cho 4 feature; mỗi bản nháp được đóng băng ở `appendix/ai-outputs/` trước khi em review và sửa.
3. Trả lời "vì sao bản AI bỏ sót" sau khi em đã tự bổ sung case (`<feature>/ai_gap_answer.md`).
4. Viết script Playwright (A, B, C), hướng dẫn chạy `RUN.md` (B, C, D), gộp kết quả chạy vào JSON, chép kết quả chạy tay của em sang file lượt (D).
5. Gom dữ kiện bug (`bugs/_groups_*.md`), dựng khung bug trống chỉ có dữ kiện, sửa dữ kiện theo evidence, chạy `gh issue create` với nội dung em viết.
6. Dựng khung report, sinh bảng dữ kiện, nháp các khối giải thích từng bước (đánh dấu 📝 AI nháp) và các mục chung (1, 2, 7, 12) để em duyệt/sửa.

## 2. Hướng dẫn

- Mỗi artifact do AI tạo là 1 hàng. Mục (1) Prompt + công cụ + thời gian + mã `#n`, (2) Output, (5) Bản SV sửa ở bảng 3.1; mục (3) Verdict và (4) Lý do ở bảng 3.2 (em viết).
- Prompt và output nguyên văn đầy đủ: `appendix/A_prompt_log.md` theo mã `#n`; output dạng file: `appendix/ai-outputs/`.
- Bảng chép nguyên văn từ report chính §10 (sinh bằng `tools/audit_tables.py`, `tools/build_forms.py`).

## 3. Bảng Audit — 1 hàng / artifact

### 3.1 Mục (1), (2), (5)

*#n theo bản trích 09:21 21/10/2026 (397 lượt trong `appendix/A_prompt_log.md`); số có thể đổi ở lần trích cuối trước khi nộp. Cách khớp: khối lượt liên tiếp cùng section trong `prompt_log_notes.toml`, giờ ≤ giờ commit tạo artifact; riêng bản đóng băng bước k và artifact nhiều commit khớp theo git (ghi "khớp theo: git"): lượt sau commit cuối của bước k−1 (hoặc commit trước đó) tới commit bước k — không có lượt nào trong khoảng đó (một lượt tạo nhiều commit) thì lấy lượt đang chạy lúc commit; section hiện nhãn đang có trong notes.*

| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |
|---|---|---|---|---|
| A1 | A_FR01 – bước 1 (biến vào/ra) | Claude Opus 5.5 (1M context) · 19/10/2026 16:33 · `4e30b25` · #17–#19 (16:10 19/10 – 16:31 19/10; Claude Opus 5.5; section trong notes: “3.1 A_FR01 Bước 1 – Phân tích biến vào/ra”; khớp theo: git) | 9 biến · `appendix/ai-outputs/A_FR01_step1_*` (1 lần đóng băng) | Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 4 đổi, 0 bỏ, 0 thêm. |
| A2 | A_FR01 – bước 2 (lớp tương đương) | Claude Opus 5.5 (1M context) · 19/10/2026 16:48 · `d799b74` · #21–#23 (16:39 19/10 – 16:47 19/10; Claude Opus 5.5; section trong notes: “3.2 A_FR01 Bước 2 – Phân lớp tương đương”; khớp theo: git) | 9 biến, 50 lớp · `appendix/ai-outputs/A_FR01_step2_*` (1 lần đóng băng) | Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 1 đổi, 0 bỏ, 2 thêm. |
| A3 | A_FR01 – bước 3 (TC Domain) | Claude Opus 5.5 (1M context) · 19/10/2026 17:11 · `448b10d` · #24–#28 (16:51 19/10 – 17:09 19/10; Claude Opus 5.5; section trong notes: “3.3 A_FR01 Bước 3 – Sinh test case Domain”; khớp theo: git) | 9 biến, 50 lớp, TS-DOM 53, TS-GUI 5 · `appendix/ai-outputs/A_FR01_step3_*` (1 lần đóng băng) | Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 1 đổi, 0 bỏ, 2 thêm; TC (trường thiết kế): 55 đổi, 0 bỏ. |
| A4 | A_FR01 – bước 4 (TC BVA) | Claude Opus 5.5 (1M context) · 19/10/2026 17:25 · `b567dc2` · #31–#32 (17:22 19/10 – 17:25 19/10; Claude Opus 5.5; section trong notes: “3.4 A_FR01 Bước 4 – Sinh test case BVA”; khớp theo: git) | 9 biến, 50 lớp, TS-DOM-UI 27, TS-DOM-API 30, TS-BVA-UI 19, TS-BVA-API 19, TS-GUI 5 · `appendix/ai-outputs/A_FR01_step4_*` (1 lần đóng băng) | Commit cùng bước sau commit đầu: `6a5a17e` HW02[A-FR01] 4/7b: SV sửa TC-90, TC-92 cô lập nguyên nhân thiếu ô Xác nhận mật khẩu. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 1 đổi, 0 bỏ, 2 thêm; TC (trường thiết kế): 2 đổi, 0 bỏ. |
| B1 | B_FR07 – bước 1 (biến vào/ra) | Claude Opus 5.5 (1M context) · 20/10/2026 10:18 · `b48929e` · #116–#119 (10:13 20/10 – 10:14 20/10; Claude (không rõ model), Claude Opus 5.5, Claude Sonnet 4.6; section trong notes: “4.1 B_FR07 Bước 1 – Phân tích biến vào/ra & Giả định” / “4.1 B_FR07 Bước 1”; khớp theo: git) | 21 biến · `appendix/ai-outputs/B_FR07_step1_*` (1 lần đóng băng) | Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 3 đổi, 1 bỏ, 1 thêm. |
| B2 | B_FR07 – bước 2 (lớp tương đương) | Claude Opus 5.5 (1M context) · 20/10/2026 10:31 · `5badc45` · #126–#126 (10:29 20/10 – 10:29 20/10; Claude Opus 5.5; section trong notes: “4.1 B_FR07 Bước 1 – Phân tích biến vào/ra & Giả định [lượt Claude Code đang chạy lúc commit; prompt: “Nhiệm vụ 1 – Lưu notes bước 1 (commit riêng)”; bước nhắc trong prompt: bước 1, 1/7b, bước 3, Bước 2, 2/7, bước 2]”; khớp theo: git) | 21 biến, 52 lớp · `appendix/ai-outputs/B_FR07_step2_*` (1 lần đóng băng) | Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 3 đổi, 1 bỏ, 1 thêm; lớp: 50 đổi, 2 bỏ, 5 thêm. |
| B3 | B_FR07 – bước 3 (TC Domain) | Claude Opus 5.5 (1M context) · 20/10/2026 10:37 · `4c69716` · #127–#129 (10:32 20/10 – 10:33 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section trong notes: “4.1 B_FR07 Bước 1 – Phân tích biến vào/ra & Giả định”; khớp theo: git) | 20 biến, 53 lớp, TS-DOM-UI 13, TS-DOM-API 14, TS-GUI 10 · `appendix/ai-outputs/B_FR07_step3_*` (4 lần đóng băng) | Commit cùng bước sau commit đầu: `444474a` HW02[B-FR07] 3/7b: sửa TC domain theo review; `3013c2f` HW02[B-FR07] 3/7c: ec_target, tách nhãn, B21; `8c72dcc` HW02[B-FR07] 3/7d: làm sạch truy vết. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 1 đổi, 0 bỏ, 1 thêm; lớp: 0 đổi, 0 bỏ, 2 thêm; TC (trường thiết kế): 21 đổi, 0 bỏ. |
| B4 | B_FR07 – bước 4 (TC BVA) | Claude Opus 5.5 (1M context) · 20/10/2026 11:03 · `7dcb0a7` · #138–#138 (11:00 20/10 – 11:00 20/10; Claude Opus 5.5; section trong notes: “4.3 B_FR07 Bước 3 – Sinh test case Domain [lượt Claude Code đang chạy lúc commit; prompt: “Nhiệm vụ 1 – B_FR07 sửa bước 3 lần 3 (commit "HW02[B-FR07] 3/7d: làm sạch …”; bước nhắc trong prompt: bước 3, 3/7d, Bước 4, 4/7]”; khớp theo: git) | 20 biến, 53 lớp, TS-DOM-UI 13, TS-DOM-API 14, TS-BVA-UI 7, TS-BVA-API 5, TS-GUI 10 · `appendix/ai-outputs/B_FR07_step4_*` (3 lần đóng băng) | Commit cùng bước sau commit đầu: `2572dc9` HW02[B-FR07] 4/7b: sửa TC BVA theo review; `1519b82` HW02[B-FR07] 4/7c: oracle tương đối cho phần không đổi. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 1 thêm; lớp: 0 đổi, 0 bỏ, 2 thêm; TC (trường thiết kế): 0 đổi, 0 bỏ. |
| C1 | C_FR15 – bước 1 (biến vào/ra) | Claude Opus 5.5 (1M context) · 20/10/2026 16:26 · `224f147` · #214–#215 (16:19 20/10 – 16:21 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section trong notes: “5.1 C_FR15 Bước 1 – Phân tích biến vào/ra & Giả định”; khớp theo: git) | 15 biến · `appendix/ai-outputs/C_FR15_step1_*` (1 lần đóng băng) | Commit cùng bước sau commit đầu: `1012f71` HW02[C-FR15] 1/7b: SV chốt giả định C0–C14. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 1 đổi, 1 bỏ, 0 thêm. |
| C2 | C_FR15 – bước 2 (lớp tương đương) | Claude Opus 5.5 (1M context) · 20/10/2026 16:39 · `d1e228a` · #219–#219 (16:35 20/10 – 16:35 20/10; Claude Opus 5.5; section trong notes: “5.1 C_FR15 Bước 1 – Phân tích biến vào/ra & Giả định [lượt Claude Code đang chạy lúc commit; prompt: “1) Áp quyết định của SV cho giả định C_FR15 (commit riêng, trước bước 2):”; bước nhắc trong prompt: bước 2, 1/7b, bước 1, 2/7, bước 3]”; khớp theo: git) | 14 biến, 73 lớp · `appendix/ai-outputs/C_FR15_step2_*` (2 lần đóng băng) | Commit cùng bước sau commit đầu: `f982e3b` HW02[C-FR15] 2/7b: sửa lý do C9 và lớp số thập phân V3; `b889942` HW02[C-FR15] 2/7c: SV chốt C9, C15. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 4 đổi, 0 bỏ, 0 thêm. |
| C3 | C_FR15 – bước 3 (TC Domain) | Claude Opus 5.5 (1M context) · 20/10/2026 16:52 · `c3e971f` · #226–#226 (16:52 20/10 – 16:52 20/10; Claude Sonnet 4.6; section trong notes: “5.3 C_FR15 Bước 3 – Sinh test case Domain”; khớp theo: git) | 14 biến, 73 lớp, TS-DOM-UI 16, TS-DOM-API-POST 17, TS-DOM-API-PUT 18, TS-DOM-API-OTHER 7, TS-GUI 5 · `appendix/ai-outputs/C_FR15_step3_*` (2 lần đóng băng) | Commit cùng bước sau commit đầu: `65c4bf2` HW02[C-FR15] 3/7b: tách suite API theo linter; `af3946f` HW02[C-FR15] 3/7c: SV chốt C16–C18. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 1 đổi, 0 bỏ, 0 thêm; TC (trường thiết kế): 10 đổi, 0 bỏ. |
| C4 | C_FR15 – bước 4 (TC BVA) | Claude Opus 5.5 (1M context) · 20/10/2026 16:58 · `1593b82` · #228–#228 (16:56 20/10 – 16:56 20/10; Claude Opus 5.5; section trong notes: “5.3 C_FR15 Bước 3 – Sinh test case Domain [lượt Claude Code đang chạy lúc commit; prompt: “1) Sửa bước 3 theo review SV (output AI → có freeze):”; bước nhắc trong prompt: bước 3, 3/7b, 3/7c, 4/7, bước 5]”; khớp theo: git) | 14 biến, 73 lớp, TS-DOM-UI 16, TS-DOM-API-POST 17, TS-DOM-API-PUT 18, TS-DOM-API-OTHER 7, TS-BVA-UI-THEM 12, TS-BVA-UI-SUA 12, TS-BVA-API-POST 12, TS-BVA-API-PUT 12, TS-GUI 5 · `appendix/ai-outputs/C_FR15_step4_*` (1 lần đóng băng) | Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 0 đổi, 0 bỏ, 0 thêm; TC (trường thiết kế): 0 đổi, 0 bỏ. |
| D1 | D_FR20 – bước 1 (biến vào/ra) | Claude Opus 5.5 (1M context) · 20/10/2026 22:28 · `c266570` · #293–#295 (22:16 20/10 – 22:23 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section trong notes: “6.1 D_FR20 Bước 1 – Phân tích biến vào/ra & Giả định”; khớp theo: git) | 9 biến · `appendix/ai-outputs/D_FR20_step1_*` (1 lần đóng băng) | Commit cùng bước sau commit đầu: `f420033` HW02[D-FR20] 1/7b: SV chốt giả định. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 2 đổi, 0 bỏ, 0 thêm. |
| D2 | D_FR20 – bước 2 (lớp tương đương) | Claude Opus 5.5 (1M context) · 20/10/2026 22:42 · `8a85ee1` · #299–#299 (22:39 20/10 – 22:39 20/10; Claude Opus 5.5; section trong notes: “6.1 D_FR20 Bước 1 – Phân tích biến vào/ra & Giả định [lượt Claude Code đang chạy lúc commit; prompt: “Đính chính lệnh trước: A_FR01 không có commit 1/7b (SV chốt giả định ngay trong …”; bước nhắc trong prompt: 1/7b, 1/7, bước 5, bước 2]”; khớp theo: git) | 9 biến, 32 lớp · `appendix/ai-outputs/D_FR20_step2_*` (2 lần đóng băng) | Commit cùng bước sau commit đầu: `af52010` HW02[D-FR20] 2/7b: sửa phân lớp theo review. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 0 đổi, 0 bỏ, 0 thêm. |
| D3 | D_FR20 – bước 3 (TC Domain) | Claude Opus 5.5 (1M context) · 20/10/2026 22:48 · `61b7e8c` · #301–#301 (22:44 20/10 – 22:44 20/10; Claude Opus 5.5; section trong notes: “6.2 D_FR20 Bước 2 – Phân lớp tương đương [lượt Claude Code đang chạy lúc commit; prompt: “## Lệnh cho Claude Code — D_FR20: sửa bước 2 (2/7b) → SV chốt (2/7c) …”; bước nhắc trong prompt: bước 2, 2/7b, 2/7c, bước 3, Bước 3, 3/7, bước 4]”; khớp theo: git) | 9 biến, 32 lớp, TS-DOM 17, TS-GUI 5 · `appendix/ai-outputs/D_FR20_step3_*` (2 lần đóng băng) | Commit cùng bước sau commit đầu: `de46981` HW02[D-FR20] 3/7b: sửa theo review. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 0 đổi, 0 bỏ, 0 thêm; TC (trường thiết kế): 5 đổi, 0 bỏ. |
| D4 | D_FR20 – bước 4 (TC BVA) | Claude Opus 5.5 (1M context) · 20/10/2026 22:52 · `c19c666` · #303–#303 (22:50 20/10 – 22:50 20/10; Claude Opus 5.5; section trong notes: “6.3 D_FR20 Bước 3 – Sinh test case Domain [lượt Claude Code đang chạy lúc commit; prompt: “## Lệnh cho Claude Code — D_FR20: rà bước 3 → bước 4 → khung …”; bước nhắc trong prompt: bước 3, bước 4, bước 5, 2/7c, 3/7b, Bước 4, 4/7]”; khớp theo: git) | 9 biến, 32 lớp, TS-DOM 17, TS-BVA 5, TS-GUI 5 · `appendix/ai-outputs/D_FR20_step4_*` (1 lần đóng băng) | Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 0 đổi, 0 bỏ, 0 thêm; TC (trường thiết kế): 5 đổi, 0 bỏ. |
| D6 | D_FR20 – bước 6 (thủ tục chạy) | Claude Opus 5.5 (1M context) · 20/10/2026 23:53 · `fdbef12` · #317–#319 (23:47 20/10 – 23:53 20/10; Claude Opus 5.5; section trong notes: “6.6 D_FR20 Bước 6 – Thực thi kịch bản kiểm thử”; khớp theo: git) | 9 biến, 32 lớp, TS-DOM 17, TS-BVA 5, TS-GUI 5, TS-SV 6 · `appendix/ai-outputs/D_FR20_step6_*` (3 lần đóng băng) | Commit cùng bước sau commit đầu: `21b4a24` HW02[D-FR20] 6/7a3: procedure theo D0 mới; `644d982` HW02[D-FR20] 6/7a4: ảnh theo RUN.md + cách đọc TRƯỚC/SAU; `690e797` HW02[D-FR20] 6/7a5: quy trình TS-GUI theo RUN.md; `74ecbb3` HW02[D-FR20] 6/7b: kết quả lượt chính thức; `f644140` HW02[D-FR20] 6/7b2: verdict SV chốt + ảnh đăng nhập thử; `f5c893e` HW02[D-FR20] 6/7b3: đồng bộ file lượt + Actual đăng nhập thử. Bản cuối (HEAD) so với bản đóng băng cuối của bước — biến: 0 đổi, 0 bỏ, 0 thêm; lớp: 0 đổi, 0 bỏ, 0 thêm; TC (trường thiết kế): 0 đổi, 0 bỏ. |
| H1 | Harness: CLAUDE.md | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `CLAUDE.md` — “CLAUDE.md — repo bài tập Software Testing (CS423 / CSC13003, AI-first)” | 19 commit sau; có chữ "SV": `3b8131c` HW02[D-FR20] 7/7a3: SV quyết mapping + khung BUG-51–57; `1a5137f` HW02: dữ kiện đối chiếu gap analysis SV |
| H2 | Agent Skill `domain-bva-testing` (SKILL.md, references, scripts freeze/check_domain/render_md/merge_results…) | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `.claude/skills/domain-bva-testing` — “9 file: SKILL.md, example-sum.json, automation.md, schema-domain.md, merge_results.cpython-314.pyc, check_domain.py …” | 20 commit sau; có chữ "SV": không |
| H3 | Hook Stop + script trích prompt log | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `.claude/settings.json` — “JSON 0 KB”; `tools/hooks/on_stop.py` — “1) chép transcript của phiên vào <repo>/.transcripts/ (bản sao dự phòng, gitignore),”; `tools/extract_prompt_log.py` — “Trích prompt log từ transcript Claude Code (.jsonl) sang Markdown theo format HW01.”; `tools/hw.toml` — “Cấu hình bài đang làm — hook on_stop.py và các script đọc file này.” | 7 commit sau; có chữ "SV": không |
| H4 | Script tổng hợp số liệu `summary.py` | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `tools/summary.py` — “Đọc <HW>/*/testcases.json và <HW>/bugs/BUG-*.md, in bảng Markdown.” | 4 commit sau; có chữ "SV": không |
| H5 | Script xuất commit log | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `tools/export_commit_log.ps1` — “Xuất commit log UTF-8 cho một bài (chạy ở gốc repo, SAU commit cuối cùng).” | không có commit sau |
| H6 | Script nén ảnh chạy tay | Claude Opus 5.5 (1M context) · 20/10/2026 23:53 · `ead7314` · #317–#319 (23:47 20/10 – 23:53 20/10; Claude Opus 5.5; section "6.6 D_FR20 Bước 6 – Thực thi kịch bản kiểm thử") | `tools/compress_manual.py` — “1. Ảnh gốc ở --raw (mặc định HW02/D_FR20/manual_raw; .png/.jpg/.jpeg, không bao giờ bị sửa…” | 1 commit sau; có chữ "SV": không |
| H7 | Script sinh bảng report `report_tables.py`, `audit_tables.py` | Claude Opus 5.5 (1M context) · 21/10/2026 07:10 · `8cf76b0` · #361–#374 (06:36 21/10 – 07:06 21/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Báo cáo HW02 – Điền dữ kiện") | `tools/report_tables.py` — “Sinh bảng dữ kiện cho report chính HW02 từ <feature>/testcases.json, bugs/BUG-xx.md, ai-ou…”; `tools/audit_tables.py` — “Sinh bảng dữ kiện cấp bài (không theo feature) cho report chính HW02. Không dùng AI, không…” | 9 commit sau; có chữ "SV": không |
| T1 | Playwright: cấu hình chung, global-setup, README | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `HW02/tests/playwright.config.ts` — “export default defineConfig({”; `HW02/tests/global-setup.ts` — “/**”; `HW02/tests/README.md` — “Test tự động HW02 (Playwright)” | 4 commit sau; có chữ "SV": không |
| T2 | Playwright A_FR01 | Claude Opus 5.5 (1M context) · 19/10/2026 22:40 · `d840b73` · #44–#45 (22:38 19/10 – 22:39 19/10; Claude Opus 5.5; section "3.6 A_FR01 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/tests/A_FR01` — “2 file: A_FR01.spec.ts, lib.ts” | không có commit sau |
| T3 | Playwright B_FR07 | Claude Opus 5.5 (1M context) · 20/10/2026 12:54 · `1abe0a1` · #151–#153 (12:43 20/10 – 12:54 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "4.6 B_FR07 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/tests/B_FR07` — “2 file: B_FR07.spec.ts, lib.ts” | 1 commit sau; có chữ "SV": không |
| T4 | Playwright C_FR15 | Claude Opus 5.5 (1M context) · 20/10/2026 18:12 · `ab466c8` · #245–#245 (18:06 20/10 – 18:06 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "5.6 C_FR15 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/tests/C_FR15` — “3 file: C_FR15.spec.ts, lib.ts, oracle.ts” | 1 commit sau; có chữ "SV": không |
| R1 | RUN.md B_FR07 | Claude Opus 5.5 (1M context) · 20/10/2026 12:54 · `1abe0a1` · #151–#153 (12:43 20/10 – 12:54 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "4.6 B_FR07 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/B_FR07/RUN.md` — “B_FR07 – Lệnh chạy test (SV chạy trên máy mình, PowerShell)” | 1 commit sau; có chữ "SV": không |
| R2 | RUN.md C_FR15 | Claude Opus 5.5 (1M context) · 20/10/2026 18:12 · `ab466c8` · #245–#245 (18:06 20/10 – 18:06 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "5.6 C_FR15 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/C_FR15/RUN.md` — “C_FR15 – Lệnh chạy test (SV chạy trên máy mình, PowerShell)” | 4 commit sau; có chữ "SV": không |
| R3 | RUN.md D_FR20 (chạy tay) + mẫu file lượt | Claude Opus 5.5 (1M context) · 20/10/2026 23:41 · `06f4d14` · #304–#315 (22:53 20/10 – 23:41 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "6.5 D_FR20 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/D_FR20/RUN.md` — “D_FR20 – Hướng dẫn chạy tay (Android thật, Expo Go)”; `HW02/D_FR20/results/D_FR20_manual_TEMPLATE.json` — “JSON 31 KB” | 6 commit sau; có chữ "SV": `f644140` HW02[D-FR20] 6/7b2: verdict SV chốt + ảnh đăng nhập thử |
| N1 | Ghi chú bước 1 B_FR07 | Claude Opus 5.5 (1M context) · 20/10/2026 10:30 · `e9ca12c` · #116–#126 (10:13 20/10 – 10:29 20/10; Claude (không rõ model), Claude Opus 5.5, Claude Sonnet 4.6; section "4.1 B_FR07 Bước 1 – Phân tích biến vào/ra & Giả định") | `HW02/B_FR07/notes_step1.md` — “B_FR07 – Notes bước 1 (trích SRS, khảo sát SUT)” | không có commit sau |
| N2 | Ghi chú bước 1 D_FR20 | Claude Opus 5.5 (1M context) · 20/10/2026 22:28 · `c266570` · #293–#295 (22:16 20/10 – 22:23 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "6.1 D_FR20 Bước 1 – Phân tích biến vào/ra & Giả định") | `HW02/D_FR20/step1_notes.md` — “D_FR20 – Ghi chú bước 0–1 (AI, chờ SV review)” | 9 commit sau; có chữ "SV": `f420033` HW02[D-FR20] 1/7b: SV chốt giả định; `b975f90` HW02[D-FR20] 5/7b: đưa case SV vào TS-SV + gap answer; `c32baff` HW02[D-FR20] 5/7f: đồng bộ case SV |
| G1 | Câu trả lời gap analysis của AI – A_FR01 | Claude Opus 5.5 (1M context) · 19/10/2026 19:20 · `8d837f1` · #35–#35 (19:14 19/10 – 19:14 19/10; Claude Opus 5.5; section "3.5 A_FR01 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/A_FR01/ai_gap_answer.md` — “Câu trả lời gap analysis của AI — FR-01 (bước 5)” | không có commit sau |
| G2 | Câu trả lời gap analysis của AI – B_FR07 | Claude Opus 5.5 (1M context) · 20/10/2026 12:14 · `897a7c8` · #143–#144 (11:11 20/10 – 12:10 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "4.5 B_FR07 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/B_FR07/ai_gap_answer.md` — “B_FR07 – AI trả lời "vì sao bản AI không có case này" (bước 5)” | không có commit sau |
| G3 | Câu trả lời gap analysis của AI – C_FR15 | Claude Opus 5.5 (1M context) · 20/10/2026 17:20 · `d1c71d8` · #229–#232 (16:59 20/10 – 17:16 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "5.5 C_FR15 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/C_FR15/ai_gap_answer.md` — “C_FR15 – AI trả lời "vì sao bản AI không có case này" (bước 5)” | 2 commit sau; có chữ "SV": `078c5b0` HW02[C-FR15] 5/7c: áp trả lời SV Q1–Q5; `7561a75` HW02[C-FR15] 5/7d: áp tiếp trả lời SV |
| G4 | Câu trả lời gap analysis của AI – D_FR20 | Claude Opus 5.5 (1M context) · 20/10/2026 23:15 · `b975f90` · #304–#306 (22:53 20/10 – 23:13 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "6.5 D_FR20 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/D_FR20/ai_gap_answer.md` — “D_FR20 – AI trả lời "vì sao bản AI không có case này" (bước 5)” | 4 commit sau; có chữ "SV": `57191a7` HW02[D-FR20] 5/7d: đồng bộ case SV; `c32baff` HW02[D-FR20] 5/7f: đồng bộ case SV; `12b9cda` HW02[D-FR20] 5/7h: đồng bộ case SV; `cc61c0b` HW02[D-FR20] 5/7j: đồng bộ case SV |
| G5 | Khung trống `sv_cases.md` (AI tạo khung, nội dung SV viết; commit chung với nội dung SV) | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 20/10/2026 17:16 · `c22e3da` · #229–#232 (16:59 20/10 – 17:16 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "5.5 C_FR15 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/C_FR15/sv_cases.md` — “C_FR15 – Test case sinh viên bổ sung (bước 5)” · Feature khác: [...] | không có commit sau |
| Q1 | Câu hỏi/trả lời bước 5 (`sv_questions.md`) B_FR07 | Claude Opus 5.5 (1M context) · 20/10/2026 12:14 · `897a7c8` · #143–#144 (11:11 20/10 – 12:10 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "4.5 B_FR07 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/B_FR07/sv_questions.md` — “B_FR07 – Câu hỏi khi chuẩn hoá case SV (bước 5b)” | 1 commit sau; có chữ "SV": `21a989a` HW02[B-FR07] 5/7c: áp trả lời SV |
| Q2 | Câu hỏi/trả lời bước 5 (`sv_questions.md`) C_FR15 | Claude Opus 5.5 (1M context) · 20/10/2026 17:20 · `d1c71d8` · #229–#232 (16:59 20/10 – 17:16 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "5.5 C_FR15 Bước 5 – SV bổ sung TC & AI gap analysis") | `HW02/C_FR15/sv_questions.md` — “C_FR15 – Câu hỏi khi chuẩn hoá case SV (bước 5b)” | 2 commit sau; có chữ "SV": `078c5b0` HW02[C-FR15] 5/7c: áp trả lời SV Q1–Q5; `7561a75` HW02[C-FR15] 5/7d: áp tiếp trả lời SV |
| BG1 | Dữ kiện bug `_groups` A_FR01 | Claude Opus 5.5 (1M context) · 19/10/2026 23:36 · `e899e06` · #58–#60 (23:31 19/10 – 23:34 19/10; Claude Opus 5.5; section "3.7 A_FR01 Bước 7 – Báo cáo lỗi (Bug report)") | `HW02/bugs/_groups_A_FR01.md` — “Dữ kiện Fail — FR-01 (A_FR01)” | 3 commit sau; có chữ "SV": không |
| BG2 | Dữ kiện bug `_groups` B_FR07 | Claude Opus 5.5 (1M context) · 20/10/2026 13:45 · `d8d60ff` · #162–#168 (13:29 20/10 – 13:45 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "4.7 B_FR07 Bước 7 – Báo cáo lỗi (Bug report)") | `HW02/bugs/_groups_B_FR07.md` — “Dữ kiện Fail — FR-07 Giỏ hàng (B_FR07)” | 1 commit sau; có chữ "SV": không |
| BG3 | Dữ kiện bug `_groups` C_FR15 + script tái hiện | Claude Opus 5.5 (1M context) · 20/10/2026 19:11 · `ea4cfd6` · #245–#254 (18:06 20/10 – 19:05 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section "5.6 C_FR15 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/bugs/_groups_C_FR15.md` — “Dữ kiện Fail — FR-15 Quản lý Sản phẩm (C_FR15)”; `HW02/bugs/_repro_C_FR15` — “14 file: api_7c.ps1, crash_48.ps1, redact_7f.js, restart_backend.ps1, ui_7c.js, G10.ps1 …” | 8 commit sau; có chữ "SV": `4800a3c` HW02[C-FR15] 7/7f0: BUG-48 bỏ căn cứ API spec theo SV |
| BG4 | Dữ kiện bug `_groups` D_FR20 + bảng web ↔ mobile | Claude Opus 5.5 (1M context) · 21/10/2026 02:16 · `3db7ddb` · #317–#337 (23:47 20/10 – 02:09 21/10; Claude Opus 5.5; section "6.6 D_FR20 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/bugs/_groups_D_FR20.md` — “Dữ kiện Fail — FR-20 Đăng ký trên Mobile (D_FR20)”; `HW02/D_FR20/compare_web_mobile.md` — “D_FR20 – So sánh web (A_FR01) ↔ mobile (D_FR20)” | 6 commit sau; có chữ "SV": `3b8131c` HW02[D-FR20] 7/7a3: SV quyết mapping + khung BUG-51–57 |
| BG5 | Quy ước bug (`bugs/README.md`), nhật ký đính chính A | Claude Opus 5.5 (1M context) · 19/10/2026 23:36 · `e899e06` · #58–#60 (23:31 19/10 – 23:34 19/10; Claude Opus 5.5; section "3.7 A_FR01 Bước 7 – Báo cáo lỗi (Bug report)") | `HW02/bugs/README.md` — “Bug report HW02 — quy ước”; `HW02/bugs/_edit_log_A.md` — “Nhật ký sửa issue A_FR01 (7/7e)” | 3 commit sau; có chữ "SV": không |
| BG6 | Khung BUG-xx (trống, chỉ dữ kiện) và sửa dữ kiện theo evidence (7/7a, 7/7c) | Claude Opus 5.5 (1M context) · 19/10/2026 23:36 · `e899e06` · A_FR01: #58–#92 (23:31 19/10 – 07:29 20/10; Claude Opus 5.5; section trong notes: “3.7 A_FR01 Bước 7 – Báo cáo lỗi (Bug report)” / “3.7 A_FR01 Bước 7 – Báo cáo lỗi (Bug report) [lượt Claude Code đang chạy lúc commit; prompt: “Bước 7 HW02/A_FR01 — lượt 1: chuẩn bị dữ kiện cho SV (theo AI-01 §11: …”; bước nhắc trong prompt: Bước 7, 7/7a]”; khớp theo: git) · B_FR07: #161–#194 (13:23 20/10 – 15:31 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section trong notes: “4.6 B_FR07 Bước 6 – Thực thi kịch bản kiểm thử” / “4.7 B_FR07 Bước 7 – Báo cáo lỗi (Bug report)” / “4.7 B_FR07 Bước 7 – Báo cáo lỗi (Bug report) [lượt Claude Code đang chạy lúc commit; prompt: “Sửa dữ kiện BUG-15, BUG-17 theo evidence. Chạy SAU commit "7/7b: SV viết BUG-15–17"”; bước nhắc trong prompt: 7/7b, 7/7c]”; khớp theo: git) · C_FR15: #254–#275 (19:05 20/10 – 21:20 20/10; Claude (không rõ model), Claude Opus 5.5; section trong notes: “5.6 C_FR15 Bước 6 – Thực thi kịch bản kiểm thử” / “5.7 C_FR15 Bước 7 – Báo cáo lỗi (Bug report)” / “5.7 C_FR15 Bước 7”; khớp theo: git) · D_FR20: #337–#356 (02:09 21/10 – 03:28 21/10; Claude Opus 5.5; section trong notes: “6.6 D_FR20 Bước 6 – Thực thi kịch bản kiểm thử [lượt Claude Code đang chạy lúc commit; prompt: “## Lệnh cho Claude Code — D_FR20: dọn 6/7b3 → 7/7a”; bước nhắc trong prompt: 6/7b3, 7/7a, 6/7b4]” / “6.7 D_FR20 Bước 7 – Báo cáo lỗi (Bug report) [lượt Claude Code đang chạy lúc commit; prompt: “- RUN.md bước 4: đổi IP kiểm thành 192.168.2.12. Giữ câu cũ + "(đã thay: …”; bước nhắc trong prompt: bước 4, 7/7a2]” / “6.7 D_FR20 Bước 7 – Báo cáo lỗi (Bug report)”; khớp theo: git) | 30 commit: `e899e06`, `11eaa75`, `7b9c972`, `7f5b524`, `103c8ec`, `d72d863`, `d8d60ff`, `d0d0e05` … | — |
| BG7 | Bản che ảnh để đăng issue | Claude Opus 5.5 (1M context) · 20/10/2026 07:29 · `7b9c972` · #58–#92 (23:31 19/10 – 07:29 20/10; Claude Opus 5.5; section "3.7 A_FR01 Bước 7 – Báo cáo lỗi (Bug report)") | `HW02/bugs/_issue_redacted` — “8 file: BUG-09.txt, BUG-10.txt, BUG-34.txt, BUG-43.txt, BUG-44.txt, BUG-48.txt …” | 2 commit sau; có chữ "SV": không |
| BG8 | Tạo GitHub Issues bằng `gh issue create` (nội dung SV viết) + ảnh trang Issues | Claude Opus 5.5 (1M context) · 20/10/2026 09:19 · `27da576` · A_FR01: #93–#100 (07:30 20/10 – 09:18 20/10; Claude Opus 5.5; section trong notes: “3.7 A_FR01 Bước 7 – Báo cáo lỗi (Bug report)”; khớp theo: git) · B_FR07: #195–#206 (15:34 20/10 – 15:59 20/10; Claude Opus 5.5, Claude Sonnet 4.6; section trong notes: “4.7 B_FR07 Bước 7 – Báo cáo lỗi (Bug report)”; khớp theo: git) · C_FR15: #282–#284 (21:40 20/10 – 21:55 20/10; Claude Opus 5.5; section trong notes: “5.7 C_FR15 Bước 7 – Báo cáo lỗi (Bug report)”; khớp theo: git) · D_FR20: #359–#359 (03:40 21/10 – 03:40 21/10; Claude Opus 5.5; section trong notes: “6.7 D_FR20 Bước 7 – Báo cáo lỗi (Bug report) [lượt Claude Code đang chạy lúc commit; prompt: “đã kéo xong ảnh”; bước nhắc trong prompt: không có]”; khớp theo: git) | 5 commit: `27da576`, `352a34d`, `9e34128`, `4d816d8`, `ec4175d` | — |
| E1 | Môi trường + patch API_URL mobile | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `HW02/env/environment.md` — “Môi trường kiểm thử”; `HW02/env/mobile_api_url.patch` — “diff --git a/frontend-mobile/App.js b/frontend-mobile/App.js” | 3 commit sau; có chữ "SV": không |
| P1 | Kế hoạch nộp bài `report_plan.md` | Claude Opus 5.5 (1M context) · 21/10/2026 06:48 · `d8627c7` · #361–#366 (06:36 21/10 – 06:43 21/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Báo cáo HW02 – Điền dữ kiện") | `HW02/report_plan.md` — “HW02 – Kế hoạch nộp bài” | 6 commit sau; có chữ "SV": `1a5137f` HW02: dữ kiện đối chiếu gap analysis SV |
| P2 | Khung report + bảng dữ kiện + 21 khối giải thích từng bước do AI nháp (§2, x.1–x.4, x.6) + các mục chung | Claude Opus 5.5 (1M context) · 21/10/2026 06:49 · `6f3b791` · #361–#367 (06:36 21/10 – 06:49 21/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Báo cáo HW02 – Điền dữ kiện") | `HW02/23120255_HW02_Report.md` — “HW02 – Domain Testing on EShop” | 19 commit sau; có chữ "SV": `db3c193` HW02 - report: SV viết AI Critique, AI review; `23c61d6` HW02: report – chép gap analysis SV A–D; `1dd750a` HW02: SV viết verdict Audit; `658694a` HW02: SV sửa verdict Audit |
| P3 | README HW02 (bảng tự đánh giá trống, khối SUMMARY) | (commit không ghi Co-Authored-By; harness do AI hỗ trợ tạo – CLAUDE.md §3) · 19/10/2026 16:08 · `d81747d` · #1–#16 (21:20 12/10 – 16:07 19/10; Claude Opus 5.5, Claude Sonnet 4.6; section "Khởi tạo môi trường & Harness") | `HW02/README.md` — “HW02 – Domain Testing on EShop” | 6 commit sau; có chữ "SV": không |
| P4 | File lượt chạy tay D (AI chép nguyên văn từ `Check.md` của SV) | Claude Opus 5.5 (1M context) · 21/10/2026 01:43 · `74ecbb3` · #317–#331 (23:47 20/10 – 01:37 21/10; Claude Opus 5.5; section "6.6 D_FR20 Bước 6 – Thực thi kịch bản kiểm thử") | `HW02/D_FR20/results/D_FR20_manual_20261021-001500.json` — “JSON 40 KB” | 2 commit sau; có chữ "SV": `f644140` HW02[D-FR20] 6/7b2: verdict SV chốt + ảnh đăng nhập thử |
| F1 | Biểu mẫu AI-02/03/05 (.md) | — · [#n: form chưa làm] | chưa làm | — |

*54 artifact. Sinh bằng `tools/audit_tables.py` từ `appendix/ai-outputs/`, `git log` (trailer Co-Authored-By cho tool), danh mục ở đầu script. Cột (5) chỉ liệt kê commit, không diễn giải lý do. Cột (3) Verdict, (4) Lý do ở bảng ngay dưới (em viết).*

### 3.2 Mục (3), (4)

| Mã | Artifact | (3) Verdict (VALID / INVALID / INCOMPLETE) | (4) Lý do (dẫn ISTQB/slide) |
|---|---|---|---|
| A1 | A_FR01 – bước 1 (biến vào/ra) | INCOMPLETE | AI phân tích dư 4 biến không có trên giao diện SUT; SV đã sửa và điều chỉnh lại 4 biến để đảm bảo tính chính xác của dữ liệu đầu vào (Equivalent Partitioning). |
| A2 | A_FR01 – bước 2 (lớp tương đương) | INCOMPLETE | AI phân lớp cơ bản ổn; SV đã bổ sung 2 lớp ký tự đặc biệt (EC51/EC52 cho email domain và ngoài ASCII) ở bước 5 để phủ trọn vẹn tập giá trị (Equivalent Partitioning). |
| A3 | A_FR01 – bước 3 (TC Domain) | INCOMPLETE | AI sinh bộ test case bị tối ưu quá mức khiến thiếu biến thể dữ liệu; SV hiệu chỉnh 55 trường để phủ đúng miền giá trị (Slide Domain Testing). |
| A4 | A_FR01 – bước 4 (TC BVA) | INCOMPLETE | AI bỏ sót việc cô lập nguyên nhân khi form thiếu ô Xác nhận mật khẩu; SV sửa TC-90 và TC-92 theo quy tắc BVA điểm biên (Boundary Value Analysis). |
| B1 | B_FR07 – bước 1 (biến vào/ra) | INCOMPLETE | AI nhận diện thiếu biến giỏ hàng trong CSDL và thừa biến rác; SV điều chỉnh 3 biến, bỏ 1 và thêm 1 biến khớp thực tế SRS FR-07. |
| B2 | B_FR07 – bước 2 (lớp tương đương) | INCOMPLETE | Prompt gộp chung với bước 1; AI phân lớp sơ sài cho trường số lượng và giá tiền, SV phải chỉnh sửa lý do 50 lớp và thêm 5 lớp mới (Equivalent Partitioning). |
| B3 | B_FR07 – bước 3 (TC Domain) | INCOMPLETE | AI gán sai mã EC vào điều kiện kiểm thử làm gãy truy vết RTM; SV trải qua 4 lượt đóng băng để làm sạch truy vết và sửa 21 test case (Traceability). |
| B4 | B_FR07 – bước 4 (TC BVA) | INCOMPLETE | Prompt gộp chung với bước 3; AI gán Oracle tuyệt đối cho trường không đổi gây fail vô lý, SV đã chỉnh thành Oracle tương đối (Test Oracle). |
| C1 | C_FR15 – bước 1 (biến vào/ra) | INCOMPLETE | AI nhận diện thừa biến môi trường server; SV gọt bỏ 1 biến rác và chốt lại 14 biến chuẩn cho tính năng Admin CRUD (SRS FR-15). |
| C2 | C_FR15 – bước 2 (lớp tương đương) | INCOMPLETE | Prompt gộp chung với bước 1; AI hiểu sai logic chấp nhận chuỗi số của V8, SV đã sửa lý do C9 và bổ sung lớp số thập phân V3 (Equivalent Partitioning). |
| C3 | C_FR15 – bước 3 (TC Domain) | INCOMPLETE | Suite API AI sinh bị vướng lỗi linter cú pháp và trùng dữ liệu; SV tách suite API và hiệu chỉnh 10 test case để đảm bảo tính thực thi (Slide Domain Testing). |
| C4 | C_FR15 – bước 4 (TC BVA) | VALID | Prompt gộp chung với bước 3; AI xác định chính xác các điểm biên cận dưới/không âm cho trường giá sản phẩm Admin theo chuẩn BVA (Boundary Value Analysis). |
| D1 | D_FR20 – bước 1 (biến vào/ra) | INCOMPLETE | AI chưa bao phủ đầy đủ ngữ cảnh di động; SV đã điều chỉnh 2 biến và cập nhật hệ thống giả định D0–D16 cho phù hợp với app di động. |
| D2 | D_FR20 – bước 2 (lớp tương đương) | INCOMPLETE | Prompt gộp chung với bước 1; AI chưa tính tới bộ gõ di động, SV bổ sung kịch bản CJK/Emoji (0 lớp đổi, 0 lớp thêm ở cột 5 do chỉnh ở các bước sau; Equivalent Partitioning). |
| D3 | D_FR20 – bước 3 (TC Domain) | INCOMPLETE | Prompt gộp chung với bước 2; AI sinh các bước thao tác chưa khớp với luồng Expo Go trên Android, SV đã sửa 5 test case cho đúng các bước bấm tay (Slide Domain Testing). |
| D4 | D_FR20 – bước 4 (TC BVA) | INCOMPLETE | Prompt gộp chung với bước 3; AI đưa ra Expected sai cho kịch bản BVA độ dài mật khẩu trên Mobile, SV đã chỉnh sửa 5 kịch bản BVA cho đúng thực tế (Boundary Value Analysis). |
| D6 | D_FR20 – bước 6 (thủ tục chạy) | INCOMPLETE | AI đề xuất quy trình chụp ảnh bằng chứng bị thừa; SV điều chỉnh quy trình TS-GUI theo đúng RUN.md (chỉ chụp 2 ảnh TRƯỚC/SAU) để tối ưu thời gian. |
| H1 | Harness: CLAUDE.md | INCOMPLETE | AI dựng quy ước ban đầu còn chung chung, SV đã cập nhật và tinh chỉnh qua 18 commit sau khi rút kinh nghiệm từ các feature trước (Test Environment). |
| H2 | Agent Skill `domain-bva-testing` (SKILL.md, references, scripts freeze/check_domain/render_md/merge_results…) | VALID | Đóng gói đầy đủ các script kiểm tra schema, render Markdown và merge kết quả tự động; script chạy đúng, đã kiểm hồi quy. |
| H3 | Hook Stop + script trích prompt log | VALID | Hook tự động sao lưu transcript và script trích log hoạt động chính xác, đảm bảo tính minh bạch và truy vết (Traceability); script chạy đúng, đã kiểm hồi quy. |
| H4 | Script tổng hợp số liệu `summary.py` | VALID | Thống kê chính xác, tự động và khách quan số lượng kịch bản kiểm thử và bug report cho từng feature; script chạy đúng, đã kiểm hồi quy. |
| H5 | Script xuất commit log | VALID | Tool PowerShell xuất log UTF-8 chuẩn xác, phục vụ trích xuất lịch sử git cuối bài; script chạy đúng, đã kiểm hồi quy. |
| H6 | Script nén ảnh chạy tay | VALID | Tự động tối ưu dung lượng ảnh chụp màn hình Mobile mà không làm giảm độ phân giải chứng minh lỗi; script chạy đúng, đã kiểm hồi quy. |
| H7 | Script sinh bảng report `report_tables.py`, `audit_tables.py` | VALID | Tự động hóa trích xuất dữ liệu báo cáo từ các artifact gốc sang Markdown chuẩn xác; script chạy đúng, đã kiểm hồi quy. |
| T1 | Playwright: cấu hình chung, global-setup, README | VALID | Thiết lập cấu hình Playwright và global-setup chuẩn xác, chạy ổn định trên môi trường Node.js; đã kiểm hồi quy (Test Environment). |
| T2 | Playwright A_FR01 | VALID | Mã tự động hóa định vị chính xác các selector UI và kiểm tra API đăng ký hoạt động tốt. |
| T3 | Playwright B_FR07 | INCOMPLETE | AI viết mã tự động thiếu cơ chế chờ bất đồng bộ gây Flaky Test khi click dồn dập; mã do AI sinh đã được hỗ trợ thêm hàm xử lý chờ trong `lib.ts` (Test Automation). |
| T4 | Playwright C_FR15 | INCOMPLETE | AI thiếu hàm sinh dữ liệu ngẫu nhiên làm các lượt chạy bị trùng tên sản phẩm; mã do AI sinh đã được bổ sung file `oracle.ts` để tạo chuỗi ngẫu nhiên. |
| R1 | RUN.md B_FR07 | VALID | Tài liệu hướng dẫn chi tiết các lệnh thực thi kiểm thử Giỏ hàng viết rõ ràng, chạy đúng thực tế. |
| R2 | RUN.md C_FR15 | INCOMPLETE | Bỏ sót bước dọn dẹp CSDL Admin trước khi chạy test; tài liệu đã được bổ sung lệnh dọn dẹp CSDL để đảm bảo tính độc lập giữa các lượt chạy. |
| R3 | RUN.md D_FR20 (chạy tay) + mẫu file lượt | INCOMPLETE | Mẫu template chạy tay ban đầu do AI sinh thiếu các trường ghi nhận thông tin thiết bị thật; SV đã bổ sung thông tin POCO F5. |
| N1 | Ghi chú bước 1 B_FR07 | VALID | Trích dẫn đầy đủ yêu cầu SRS FR-07 và kết quả khảo sát SUT thực tế, thông tin chuẩn xác. |
| N2 | Ghi chú bước 1 D_FR20 | INCOMPLETE | Thông tin IP endpoint API trong file ghi chú cần đính chính lại do SV chuyển địa chỉ mạng từ quán cafe về ký túc xá (commit `3ad5c8f`). |
| G1 | Câu trả lời gap analysis của AI – A_FR01 | VALID | AI giải thích nguyên nhân bỏ sót kịch bản hợp lý dựa trên quy tắc Minimum Set và việc không chạy SUT thật. |
| G2 | Câu trả lời gap analysis của AI – B_FR07 | VALID | Phân tích đúng lý do AI bỏ qua các lỗi tương tranh (Race Condition) do giới hạn quan sát của LLM. |
| G3 | Câu trả lời gap analysis của AI – C_FR15 | INCOMPLETE | Bộ câu trả lời gap analysis gốc được cập nhật thêm các phản hồi và quyết định làm rõ từ SV (áp câu trả lời SV vào bộ case). |
| G4 | Câu trả lời gap analysis của AI – D_FR20 | INCOMPLETE | Bộ câu trả lời gap analysis gốc được cập nhật thêm các phản hồi đính chính và làm rõ từ SV cho kịch bản di động. |
| G5 | Khung trống `sv_cases.md` (AI tạo khung, nội dung SV viết; commit chung với nội dung SV) | VALID | Khung mẫu Markdown được tạo chuẩn cấu trúc giúp SV tự điền kịch bản bổ sung ở bước 5 dễ dàng; đã kiểm tra đồng bộ. |
| Q1 | Câu hỏi/trả lời bước 5 (`sv_questions.md`) B_FR07 | VALID | Ghi lại đầy đủ và minh bạch các trao đổi chuẩn hóa kịch bản kiểm thử Giỏ hàng giữa SV và AI (Traceability). |
| Q2 | Câu hỏi/trả lời bước 5 (`sv_questions.md`) C_FR15 | VALID | Lưu trữ chính xác các quyết định của SV về việc giữ/bỏ các test case dị dạng ở tầng API (Traceability). |
| BG1 | Dữ kiện bug `_groups` A_FR01 | VALID | Dữ liệu tổng hợp các test case Fail của feature A đầy đủ, hỗ trợ tốt cho việc lập báo cáo lỗi (Defect Management). |
| BG2 | Dữ kiện bug `_groups` B_FR07 | VALID | Gom nhóm dữ kiện lỗi Giỏ hàng chính xác theo từng phân vùng UI/API, phục vụ phân tích nguyên nhân gốc (Defect Management). |
| BG3 | Dữ kiện bug `_groups` C_FR15 + script tái hiện | VALID | Cung cấp đầy đủ các script PowerShell/JS tái hiện lỗi Admin và log crash backend BUG-48 chuẩn xác (Defect Management). |
| BG4 | Dữ kiện bug `_groups` D_FR20 + bảng web ↔ mobile | VALID | Bảng đối chiếu giao diện Web-Mobile hỗ trợ phát hiện chính xác các lỗi bất đồng bộ trải nghiệm trên các nền tảng khác nhau. |
| BG5 | Quy ước bug (`bugs/README.md`), nhật ký đính chính A | VALID | Thiết lập quy trình đánh giá mức độ nghiêm trọng và nhật ký đính chính minh bạch; tài liệu phụ chạy đúng quy ước (Defect Management). |
| BG6 | Khung BUG-xx (trống, chỉ dữ kiện) và sửa dữ kiện theo evidence (7/7a, 7/7c) | INCOMPLETE | Khung báo cáo lỗi do AI sinh ban đầu bị thiếu thông tin môi trường và bằng chứng; SV đã tự tay hoàn thiện mô tả chi tiết cho 57 bug (Defect Management). |
| BG7 | Bản che ảnh để đăng issue | VALID | Script và bản che ảnh nhạy cảm/token hoạt động chuẩn xác, đảm bảo an toàn thông tin khi công khai Issue. |
| BG8 | Tạo GitHub Issues bằng `gh issue create` (nội dung SV viết) + ảnh trang Issues | VALID | Tự động hóa việc đẩy 57 báo cáo lỗi do SV biên soạn lên GitHub Issues thành công; script chạy đúng, đã kiểm hồi quy. |
| E1 | Môi trường + patch API_URL mobile | VALID | Ghi nhận chính xác thông tin môi trường thử nghiệm và file patch cấu hình IP cho app Mobile (Test Environment). |
| P1 | Kế hoạch nộp bài `report_plan.md` | VALID | Liệt kê đầy đủ danh mục sản phẩm bàn giao và lộ trình hoàn thiện báo cáo chi tiết; tài liệu phụ đúng định dạng. |
| P2 | Khung report + bảng dữ kiện + 21 khối giải thích từng bước do AI nháp (§2, x.1–x.4, x.6) + các mục chung | INCOMPLETE | AI nháp ban đầu chứa một số câu khẳng định quá mức; SV đã rà soát gọt dũa văn phong và tự viết phần AI Critique/Audit. |
| P3 | README HW02 (bảng tự đánh giá trống, khối SUMMARY) | VALID | File README tổng quan của bài tập được tạo đầy đủ các mục tóm tắt số liệu (SUMMARY) đúng quy ước bài tập. |
| P4 | File lượt chạy tay D (AI chép nguyên văn từ `Check.md` của SV) | VALID | AI chuyển đổi chính xác nguyên văn dữ liệu kết quả kiểm thử thủ công từ file `Check.md` của SV sang JSON mà không làm biến đổi nội dung gốc. |
| F1 | Biểu mẫu AI-02/03/05 (.md) | VALID | Đã làm tốt rồi, không cần sửa |

### 3.3 Đánh giá từng TC do AI sinh

**Bảng A – TC giữ nguyên bản AI (gộp theo suite)**

| Feature | Suite | Số TC giữ nguyên bản AI | Verdict | Lý do |
|---|---|---|---|---|
| A_FR01 | TS-DOM-UI | 27 | VALID | đã đủ tốt ở các case AI tìm ra |
| A_FR01 | TS-DOM-API | 30 | VALID | đã đủ tốt ở các case AI tìm ra |
| A_FR01 | TS-BVA-UI | 19 | VALID | đã đủ tốt ở các case AI tìm ra |
| A_FR01 | TS-BVA-API | 19 | VALID | đã đủ tốt ở các case AI tìm ra |
| A_FR01 | TS-GUI | 3 | VALID | đã đủ tốt ở các case AI tìm ra |
| B_FR07 | TS-DOM-UI | 13 | VALID | đã đủ tốt ở các case AI tìm ra |
| B_FR07 | TS-DOM-API | 14 | VALID | đã đủ tốt ở các case AI tìm ra |
| B_FR07 | TS-BVA-UI | 7 | VALID | đã đủ tốt ở các case AI tìm ra |
| B_FR07 | TS-BVA-API | 5 | VALID | đã đủ tốt ở các case AI tìm ra |
| B_FR07 | TS-GUI | 10 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-DOM-UI | 16 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-DOM-API-POST | 17 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-DOM-API-PUT | 18 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-DOM-API-OTHER | 7 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-BVA-UI-THEM | 12 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-BVA-UI-SUA | 12 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-BVA-API-POST | 12 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-BVA-API-PUT | 12 | VALID | đã đủ tốt ở các case AI tìm ra |
| C_FR15 | TS-GUI | 5 | VALID | đã đủ tốt ở các case AI tìm ra |
| D_FR20 | TS-DOM | 17 | VALID | đã đủ tốt ở các case AI tìm ra |
| D_FR20 | TS-BVA | 5 | VALID | đã đủ tốt ở các case AI tìm ra |
| D_FR20 | TS-GUI | 5 | VALID | đã đủ tốt ở các case AI tìm ra |

**Bảng B – TC khác bản AI hoặc không có trong bản đóng băng**

| TC | Thay đổi (git) | Verdict | Lý do |
|---|---|---|---|
| TC-FR01-90 | khác bản AI `A_FR01_step4_20261019-1719.json` ở expected_result, rationale, steps; commit đầu tiên khác: `6a5a17e` | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-92 | khác bản AI `A_FR01_step4_20261019-1719.json` ở title, expected_result, rationale, steps; commit đầu tiên khác: `6a5a17e` | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-219 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-223 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-224 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-225 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-226 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-227 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-228 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |
| TC-FR01-231 | không có trong bản AI đóng băng | INCOMPLETE | hiểu nhầm context nên phải chỉnh sửa |

*295 TC có `origin` AI/Both: 285 giữ nguyên, 10 khác/không có trong bản đóng băng. Verdict và lý do theo quyết định của em (V1, V2, 21/10), áp theo trạng thái sửa trong git. Bản đánh giá từng TC trước đó: `appendix/audit_103_sv_old.md`.*

## 4. Tổng kết Độ chính xác AI

|  | VALID | INVALID | INCOMPLETE | Tổng |
|---|---|---|---|---|
| Artifact (cột (3) ở 10.2, không tính F1) | 20 (44.4%) | 0 (0.0%) | 25 (55.6%) | 45 |
| TC do AI sinh (theo số TC ở 10.3) | 285 (96.6%) | 0 (0.0%) | 10 (3.4%) | 295 |

*Tỉ lệ = số verdict loại đó / tổng hàng (hoặc tổng TC). Đếm bằng script từ cột Verdict ở 10.2 và trạng thái TC ở 10.3.*

- Phiên thảo luận đưa sai hash `8d837f1` cho A3 bản 2 (đúng `1cfa163`); D5 trích hash sai (`D_FR20/step1_notes.md:121`, giả định D5 trong `D_FR20/testcases.json`), nội dung giống hệt (`report_plan.md` mục g).
- Lượt AI chỉ rà soát, không tạo artifact: [...]

## 5. Kết luận — Khi nào nên / không nên dùng AI?

Xem report chính `23120255_HW02_Report.md` mục 10.5.

## 6. AI Critique

Xem report chính `23120255_HW02_Report.md` mục 11 (R4: Critique chỉ nằm trong report).

## 7. Mandatory Disclosure (dán nguyên văn report §12)

| Mục | Nội dung |
|---|---|
| Phần AI tạo bản đầu | Harness: `CLAUDE.md`, Agent Skill `domain-bva-testing` (SKILL.md, references, `freeze.py`, `check_domain.py`, `render_md.py`, `merge_results.py`), hook Stop + `tools/extract_prompt_log.py`, `tools/summary.py`, `tools/compress_manual.py`, `tools/export_commit_log.ps1`, `tools/report_tables.py`, `tools/audit_tables.py`. Bản nháp bước 1–4 (biến, lớp, TC Domain, TC BVA) của A_FR01, B_FR07, C_FR15, D_FR20 — đóng băng ở `appendix/ai-outputs/`. Ghi chú bước 1 (`B_FR07/notes_step1.md`, `D_FR20/step1_notes.md`). Câu trả lời gap analysis (`*/ai_gap_answer.md`) và câu hỏi chuẩn hoá case SV (`sv_questions.md`). Khung trống `sv_cases.md`. Script Playwright A/B/C, `RUN.md` B/C/D. Dữ kiện bug `bugs/_groups_*.md`, `D_FR20/compare_web_mobile.md`, khung BUG-xx trống (chỉ dữ kiện), bản che ảnh `bugs/_issue_redacted/`. `report_plan.md`, khung report, khung `README.md`, bảng dữ kiện của report (sinh bằng script), 21 khối 📝 AI nháp giải thích từng bước (§2, x.1–x.4, x.6) và các mục chung 1, 7, 12 |
| Phần em xem xét và sửa | Review từng bước 1–4 của mỗi feature và chốt giả định (commit `x/7b`, `x/7c`…, "SV chốt …"); sửa Expected/quy trình trước khi chạy; chạy toàn bộ test trên máy em (Playwright A/B/C, chạy tay D trên Android); chốt verdict cuối theo quy tắc mục 2.6; duyệt dữ kiện bug AI sửa (7/7c); duyệt các khối 📝 AI nháp; Section/Mục đích/Xử lý của prompt log |
| Edge case em bổ sung | Suite `TS-SV*` của 4 feature (`origin: Human`; số lượng ở cột "TC SV thêm" mục 8), viết trước khi hỏi AI (`*/sv_cases.md`, commit `HW02[X-FRnn] 5/7`) |
| Phần em tự viết hoàn toàn | Case TS-SV; mô tả mọi bug (`bugs/BUG-xx.md`, danh sách ở mục 9) và nội dung GitHub Issues; phân tích "vì sao AI bỏ sót" (x.5); AI Critique (mục 11); verdict và lý do Audit (10.2, 10.3, 10.5); điểm tự đánh giá; thuyết minh video demo skill |
| Cách tạo prompt log | Trích tự động bằng `tools/extract_prompt_log.py` (chạy qua hook Stop `tools/hooks/on_stop.py` sau mỗi lượt), chép nguyên văn prompt/output từ transcript Claude Code và bản tải về của phiên claude.ai, giờ Asia/Saigon, ghi model từng lượt; em tự ghi Section/Mục đích/Xử lý trong `appendix/prompt_log_notes.toml`. Các lượt 'Claude (không rõ model)' theo P3 (số liệu lấy ở lần trích cuối) — giữ nguyên, không vá script; lý do từng lượt em ghi trong `appendix/prompt_log_notes.toml` |
| Danh mục cấm (AI không làm) | Không viết/nháp mô tả bug (tóm tắt, bước, expected/actual) và nội dung issue; không gợi ý edge case/boundary/security khi em đang tự tìm (bước 5); không viết AI Critique, phân tích gap, verdict Audit, điểm tự chấm; không tạo giọng thuyết minh video, ảnh có username/hostname, chữ ký; không tick mục cam kết cá nhân AI-05; không sửa `appendix/ai-outputs/`; không sửa tay prompt log |

## Chữ ký

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |
| MSSV: | 23120255 |
| Lớp / Khoá: | Software Testing - 23_3 |
| Môn học: | CSC13003 – Kiểm chứng Phần mềm |
| Giảng viên: | Thầy Lâm Quang Vũ, Thầy Trần Duy Hoàng, Cô Trần Thị Bích Hạnh, Thầy Trương Phước Lộc, Thầy Hồ Tuấn Thanh |
| Ngày: | 21/10/2026 |
| Chữ ký: | ![Chữ ký](signature.png) |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Hardman, P. (2025). A Post-AI Learning Taxonomy.
- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.
- Anthropic (2025). Building reliable AI test agents — engineering blog.
