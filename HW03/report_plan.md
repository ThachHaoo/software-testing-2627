# HW03 – GUI & Usability · Kế hoạch nộp bài (report_plan)

Lê Tấn Hiệp – 23120255 · Deadline **10:00 11/11/2026** · Cấp độ AI: **Cấp 4** · Bloom-AI: **G9.3 + G9.4** (theo đề §3, §8)

## a. Biểu mẫu AI

| Form | Bắt buộc | File | Ai làm |
|---|---|---|---|
| AI-02 Audit Report | Có | `ai-forms/AI-02_Audit_Report_23120255.md` + `.pdf` | AI điền dữ kiện, tỉ lệ; SV viết verdict + lý do, ký |
| AI-03 Disclosure | Có | `ai-forms/AI-03_Disclosure_23120255.md` + `.pdf` | AI điền công cụ, số lượt, dải #; SV xác nhận, ký |
| AI-04 Reflective | Không | — | HW thường, đề không yêu cầu |
| AI-05 Privacy | Có (làm cuối) | `ai-forms/AI-05_Privacy_Checklist_23120255.md` + `.pdf` | AI tick mục có bằng chứng; SV tick cam kết, ký. Bài có dữ liệu người tham gia → ghi rõ đã che gì |
| AI-06 | Đã nộp tuần 1 | — | — |

Câu tuyên bố nguyên văn: *"I use AI tools for the following tasks,"*. Mẫu định dạng form: `HW02/ai-forms/*.md` (không chép số liệu).

## b. Rubric (đề §15)

| # | Mục | Max | Tự chấm |
|---|---|---|---|
| 1 | Task 1 – GUI Checklist (thiết kế + chạy + bug) | 30 | `<SV>` |
| 2 | Task 2 – Usability (kịch bản + 7 phiên + phân tích) | 40 | `<SV>` |
| 3 | Task 3 – Cross-platform (≥ 3 nền tảng) | 20 | `<SV>` |
| 4 | Agent Skills (+ video YouTube) | 10 | `<SV>` |
| | Tổng = 3 số trong tên zip | 100 | `<SV>` |

## c. Danh sách nộp (đề §14) – trạng thái

| # | Mục | Đường dẫn dự kiến | Trạng thái | Nộp? |
|---|---|---|---|---|
| 1 | Report chính (.md + PDF): checklist report + usability report | `23120255_HW03_Report.md/.pdf` | THIẾU | Có |
| 2 | Bug report + ảnh trang GitHub Issues | `bugs/BUG-58…md`, `bugs/issues_page_HW03.png` | THIẾU | Có |
| 3 | AI Critique (200–300 từ) + Audit (.md + PDF) | report §Critique; `ai-forms/AI-02…` | THIẾU | Có |
| 4 | Commit log (text) | `commit_log.txt` | THIẾU | Có |
| 5 | Excel checklist (> 40 item) + test summary | `excel/23120255_HW03_Checklist.xlsx` | THIẾU | Có |
| 6 | Bằng chứng usability: kịch bản, ghi chú quan sát, SUS, findings xếp hạng, video (nếu có), bảng 7 người | `usability/…` | THIẾU | Có |
| 7 | Ảnh cross-platform (có overlay) | `checklist/evidence/P1_chrome`, `P2_firefox`, `P3_android` | THIẾU | Có |
| 8 | README.md: tự đánh giá + test summary (số màn/flow, item thiết kế/chạy/Pass/Fail, số bug, số người, link video) | `README.md` | THIẾU | Có |
| 9 | Skill + video demo (YouTube) | `skills/…`, `skills/VideoLinks.md` | THIẾU – **chép 2 skill → HW03/skills khi đóng gói** (`gui-checklist-testing`, `usability-evaluation` từ `.claude/skills/`; cập nhật theo cách làm thực tế 10/11) | Có |
| 10 | Prompt log | `appendix/A_prompt_log.md` | THIẾU (đổi `tools/hw.toml` sang HW03) | Có |
| — | Kế hoạch nộp bài (file này) | `report_plan.md` | — | Không (`HW03/.gitattributes`: export-ignore) |

Moodle: ≤ 20 file, mỗi file ≤ 20 MB. Zip: `23120255_HW03_AI_GUIUsability_<ggg>.zip`, đóng gói bằng `git archive` (như HW02 R2).

## d. Mâu thuẫn / dễ sót trong đề

| Mã | Nội dung | Cách xử lý |
|---|---|---|
| M1 | Overlay ảnh: §6 "username dạng email SV" ↔ §11 "MSSV + họ tên" | Overlay đủ email SV + MSSV + họ tên |
| M2 | "Perform Task 1 across ≥ 3 platforms" | **SV chốt: chạy TOÀN BỘ checklist trên mỗi nền tảng** |
| M3 | Đề chỉ có Passed/Failed | **SV chốt: thêm N/A, ghi giả định** (căn cứ slide: checklist chấm Yes/No/N/A) |
| M4 | Không trùng màn chính/flow với thành viên nhóm | Chia C1/C2/C3, U1–U4 (tin nhắn nhóm 04/11) |
| M5 | Bảng đầu "G9.1→G9.6" ↔ §3/§8 "G9.3 + G9.4"; Skill thuộc G9.5 | Ghi G9.3 + G9.4 |
| M6 | Excel bắt buộc ↔ Homework Policies (bảng tổng hợp phải có trong .md) | Excel + chép bảng sang report |
| M7 | Video phiên usability chứa giọng/màn hình người tham gia; 20 MB/file | Xin đồng ý; không đăng công khai; link Drive giới hạn quyền (`[...]` SV chốt) |
| M8 | Commit cho mỗi bước, kể cả **mỗi phiên usability** | ≥ 9 commit Task 2 (plan, pilot, 7 phiên, phân tích) |
| M9 | Flow U1 đi qua chỗ có bug HW02 đã biết (BUG-15…29 giỏ hàng) | Findings ghi "đã biết – BUG-xx", không tạo issue trùng |
| M10 | Đề nói "spec không gán FR cho UI" ↔ SRS `README.md` §8 có **FR-21…FR-24** khớp IA-01…IA-04 | Report nêu ánh xạ IA ↔ FR một lần; dùng FR-21…24 (+ FR-02/03/04/11 phần UI) làm căn cứ Expected |
| M11 | Đề nhắc BrowserStack/LambdaTest "strongly preferred" | Không dùng: trial 30 phút Live, 1 phút/thiết bị (BrowserStack), phiên 2 phút (LambdaTest/TestMu AI) → không đủ chạy toàn bộ checklist (M2). Đề cho phép thiết bị thật |

## e. Quyết định đã chốt

| Mã | Quyết định |
|---|---|
| S1 | Checklist **C2 – Tài khoản (web :5173)**: Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ + Lịch sử đơn/huỷ đơn, navbar khi đã đăng nhập. **Không lấy Đăng ký** (đã kiểm ở HW02 A/D) |
| U | Usability **U1**: đăng nhập (tài khoản cho sẵn) → tìm SP → thêm giỏ → thanh toán có mã giảm giá → xem đơn trong Hồ sơ. Moderated, trực tiếp trên PC của SV. Restart backend trước mỗi phiên |
| M2 | Toàn bộ checklist × 3 nền tảng |
| M3 | Có N/A + giả định |
| P1 | ~~Chrome trên Windows~~ → **Cốc Cốc 160 trên Windows 11** (Q1, 10/11) (localhost:5173) |
| P2 | Firefox trên Windows (cài mới) |
| P3 | Chrome Android trên POCO F5 qua `adb reverse tcp:5173` + `tcp:3000` — **đã kiểm chứng 04/11 17:35** (adb 37.0.1 ở `D:\Tools\platform-tools`, web chạy `--host 127.0.0.1`) |
| BS | Không dùng BrowserStack/LambdaTest (M11) |
| R | Người tham gia: 1 pilot + 7 chính, đã tuyển 04/11 (ngoài lớp; một phần IT, một phần non-IT) |
| E1 | Excel **mới** `excel/23120255_HW03_Checklist.xlsx`, 3 sheet như HW01 (Test Cases / Checklist / Test Summary Report) |
| O1 | Overlay: `23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn`. PC = cửa sổ Sticky Notes + chụp toàn màn hình (thấy tên trình duyệt + URL); điện thoại = thêm chữ bằng trình sửa ảnh của máy ngay sau khi chụp |
| T | Thang: **SUS** (10 câu tiếng Việt) + **SEQ** (1 câu sau nhiệm vụ); bộ câu hỏi tối giản vì có người non-IT |
| K1 | Mã giảm giá trong nhiệm vụ U1 = **VIP100** (a). Lý do: usability đo thiết kế, không để bug tính tiền đã biết (SAVE10) làm nhiễu SUS |
| X1 | (a) Cài `openpyxl` cho Python các script dùng (`C:\msys64\ucrt64\bin\python.exe` 3.14; Python này không có pip → `pacman -S mingw-w64-ucrt-x86_64-python-openpyxl`) → `build_excel.py` chạy được |
| X2 | (a) `HW03/CLAUDE.md` không nộp: `export-ignore` trong `HW03/.gitattributes` |
| E2 | (b) Playwright tự chạy các item kiểm được qua DOM/bàn phím trên P1 (Chrome channel) + P2 (Firefox của Playwright) → `auto_status`; SV chạy tay phần còn lại + toàn bộ P3. **Verdict chính thức = lượt trên trình duyệt thật** |
| H1 | Ngưỡng màu cho auto: CL-04 xanh dương = hue 190–250°, CL-05 đỏ = hue 340–20°, độ bão hoà ≥ 0,3 (SV: "nhìn thấy đúng xanh dương/đỏ là được"); expected không đổi |
| Q1 | P1 chính thức = **Cốc Cốc 160.0.106 / Windows 11** (nhân Chromium; SV không dùng Chrome hằng ngày). Lượt auto P1 = Chrome 157 qua Playwright `channel: "chrome"`: chỉ để tham chiếu. Ghi vào mục "lệch so với kế hoạch" của report |
| Q2 | (a) CL-64 = **Blocked** trên P1/P2/P3: form Hồ sơ chặn bởi validation SĐT (issue nhóm #111) trước khi kiểm được trường hợp tắt backend |
| V1 | Lệch auto ↔ tay: **verdict lấy lượt trên trình duyệt thật** (tay), ghi nguyên nhân lệch (vd auto giả lập locale vi-VN, còn Firefox/Chrome Android thật của SV dùng locale máy → khác định dạng tiền/ngày) |
| O2 | Overlay thực tế = `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn` (dấu "-" thay "·" của O1). P1/P2: cửa sổ Sticky Notes; P3: thêm chữ bằng trình sửa ảnh của máy |
| B5 | Ảnh `P1_SV-02_3/4` lộ email cá nhân và tài khoản đã lưu → SV che bằng ô đen (khai trong AI-05) |
| T-P3 | CL-30, CL-48 trên P3 = **Blocked**: lượt auto Playwright `TimeoutError` (locator.click 30 s), không có assertion fail → không lập bug (5/6a, 10/11) |
| CL34 | CL-34 P2: giữ kết quả auto (Failed), ghi "chỉ Firefox Playwright, chưa xác nhận trên trình duyệt thật"; **loại khỏi danh sách lập bug** (5/6a) |
| Q1-auto | 59 item auto của P1 lấy kết quả lượt Chrome 157 (Playwright), không chạy lại trên Cốc Cốc; khai trong mục "lệch so với kế hoạch" của report (5/6a) |
| CL52-P3 | CL-52 P3: notes ghi "thiếu ảnh" (ảnh `P3_CL-52_1` chỉ thấy "Đăng nhập thất bại", không thấy trạng thái khoá) (5/6a) |
| G-SV | SV chốt nhóm bug (5/6b): tách G-02 cũ (CL-13, CL-14) và G-23 cũ (CL-08, CL-09); G-13 giữ gộp; CL-04, CL-08, CL-40, CL-60, CL-62 trùng #160, #170, #169, #165, #167 → bỏ khung. Còn 28 nhóm → BUG-58…85 |
| U-R | T2 chạy **remote synchronous moderated** qua Google Meet (người tham gia dùng máy tính của mình, chia sẻ màn hình, think-aloud; quay Game Bar/OBS khi đồng ý). SUT công khai tạm thời qua Cloudflare quick tunnel, nhánh local `usability-tunnel` của eshop-sut (chỉ đổi URL API sang `/api` + Vite proxy), không push (10/11) |
| R9 | CL-08 P1 = **Failed** (4/6c, 10/11): Expected "cùng một kiểu phân cách trên cả 3 nền tảng" áp cho cả P1 ("30.000.000 ₫" ≠ "6,000,000 ₫" P2/P3); lý do lấy từ khuyến nghị run_check R9, SV có thể sửa. Áp bằng override `tools/merge_hw03.py`, không sửa file lượt tay. CL-08 trùng #170 → không khung bug |
| R11 | CL-09 P1 = **Failed** (4/6c, 10/11): Expected "dd/mm/yyyy và giống nhau trên P1, P2, P3" áp cho cả P1 ("9/11/2026" ≠ "11/9/2026" P2/P3); L1 đóng. Hệ quả: G-23/`BUG-80` thêm nền tảng P1 (khung BUG-80 chưa sửa – chờ SV) |
| D1 | Skill tự đủ (Skill 1/3b, 10/11): `gen_oracle.py`, `gen_run.py` gắn cứng HW03 (đường dẫn `HW03/checklist`, màn C2, overlay, adb) → **không chép** vào `scripts/`; SKILL.md ghi "chỉ có ở repo ví dụ". Sửa chữ nguồn trong `render_checklist.py` (không còn trỏ `tools/`). `.claude/skills` ↔ `HW03/skills` diff = 0 |
| D2 | Lượt Claude Code khi quay demo skill **vào prompt log** (khai mục đích "demo skill"), không thêm `exclude` vào `tools/hw.toml` |
| R4 | Giờ lượt tay P1 (4/6d, 10/11): SV giải thích ".jpg là ảnh lấy từ điện thoại, .png là ảnh chụp màn hình máy tính"; ảnh P1 đều .png → giờ lấy từ mtime ảnh gốc `evidence_raw/P1_chrome/`: kết thúc 00:10 10/11 (P1_CL-64_1), restart 22:56 09/11 (trước ảnh đầu 23:24). Kiểm chéo bằng P2 (mtime 00:13–00:36 khớp file lượt 00:10–00:38) |
| PFX | Tiền tố tiêu đề GitHub Issue = **`[HW03-C2-<số BUG>]`** (vd `[HW03-C2-58]`), theo cách bạn nhóm đặt `[HW03-C3-xx]`; chỉ dùng trên GitHub, không đưa vào tiêu đề trong file BUG (5/6c, 10/11) |
| DUP | Giữ nguyên mức trùng của cả 28 nhóm theo `bugs/dup_check.md` (21 issue mới #204–#224 đều là admin C3); G-16 ↔ #123 = liên quan (5/6c, 10/11) |
| M6 | Bỏ ảnh `P*_M6_1`: M6 "Chung – tất cả màn C2" là nhóm item, không phải một màn; ảnh tổng quan chỉ M1…M5 (RUN.md mục 2). Sửa tiêu đề nhóm M6 trong `RUN.md` + `tests/gen_run.py` (4/6e, 10/11) |
| CL64-P3 | CL-64 P3: bỏ tham chiếu `P3_CL-64_1.jpg` (không tồn tại ở đâu), giữ `_2`; notes "ảnh _1 không có; chỉ _2" (4/6e) |
| M4-P3 | Giữ `P3_M4_1` dù Lịch sử đơn trống; report §4.3 ghi "lịch sử đơn trống lúc chụp" (4/6e) |

| PILOT | S00 = pilot (P00), không tính thống kê; sau pilot giữ nguyên kịch bản, từ S01 bổ sung "hỏi lại ngay khi nhận xét mơ hồ"; S01–S07 = 7 phiên chính. Mã "SO1" (chữ O) trong form = S01. Nghề nghiệp S00…S07 do SV cung cấp (không lấy cột "Bạn là" của form) (11/11) |
**Còn chờ SV chốt:** (không còn)

## f. Khai cho Audit (ghi dần)

- 04/11 phiên thảo luận: đọc đề + slide, lập bảng form, đề xuất chia C1/C2/C3 + U1–U4 cho nhóm, tin nhắn mời người tham gia (AI nháp), hướng dẫn bật Gỡ lỗi USB, lệnh kiểm chứng P3.
- 04/11 Claude Code: tải platform-tools (SV đồng ý), chạy backend/web, `adb reverse`, liệt kê issue nhóm (158).
- AI phát hiện khi kiểm luồng U1: SAVE10 tính sai (server.js:400), ngưỡng dùng > thay vì >= (server.js:379) – chưa quyết lập bug.
- AI phát hiện khi đọc code: login_attempts +2 (server.js:54), khoá 180 s (server.js:57) ≠ FR-02 – chờ CL-52 chạy tay. Kiểm trùng: đã có #1, #2, #3 (`checklist/issue_dup_FR02.md`).
- 05/11 Claude Code: cài Firefox của Playwright (131.0), thêm project P3 (Playwright `_android`) vào harness; sửa lỗi reporter.ts ghi 0 item (`TestResult.annotations` chưa có ở 1.48) – phát hiện khi smoke CL-03.
- 10/11 Claude Code: tạo skill `usability-evaluation` (SKILL.md, 2 reference, 3 asset, 6 script); kiểm plan/kit HW03 bằng `check_kit.py` (0 lỗi, không sửa); thử `sus_score.py` trên 2 phiếu giả ở thư mục tạm (không commit).
- 10/11 Claude Code: kiểm ảnh/kết quả chạy tay (`checklist/run_check.md`), nén + đổi tên ảnh đạt (`tools/compress_hw03.py`, gốc ở `evidence_raw/` không nộp), chuẩn hoá giá trị Pass/Fail → Passed/Failed, CL-64 → Blocked (Q2) và metadata (tiêu đề P2, Android 14) trong `runs/*_manual_*` theo yêu cầu SV; không sửa notes.
- 10/11 Claude Code (4/6a2–4/6b): đổi tên/nén ảnh B3/B4 theo bảng SV duyệt, M5 dùng lại ảnh M3/M4; gộp auto + tay vào `checklist.json` (`tools/merge_hw03.py`: CSV từ file tay, ánh xạ tên ảnh, V1, ghi `nguon_kq` + `lech_auto_tay`); Excel (`build_excel.py`, thêm fullCalcOnLoad; kiểm bằng Excel: 21 công thức, 0 lỗi); `bugs/issues.json` (gh issue list) + `bugs/failed_list.md` (`tools/failed_list_hw03.py`, AI đối chiếu trùng theo tiêu đề issue, SV xác nhận); chèn marker REPORT:T1/U1 vào report và điền 2 bảng T1 (`tools/report_t1_hw03.py`).
- 10/11 Claude Code (5/6a): ghi quyết định T-P3/CL-34/Q1-auto/CL-52 P3 vào `merge_hw03.py` (OVERRIDE, nối notes, không sửa chữ SV); CL-01 đổi thành trùng #9 theo notes; `bugs/bug_groups.md` (30 nhóm dữ kiện, AI đề xuất, SV xác nhận) + khung `bugs/BUG-58…87.md` chỉ chép dữ kiện (`tools/bug_groups_hw03.py`); Tiêu đề/Mô tả/Steps/Severity/Priority/Nhận định để trống cho SV.
- 10/11 Claude Code (T2 2b): nhánh local `usability-tunnel` trong eshop-sut (commit `e33212d`: 7 file frontend-web đổi `http://localhost:3000/api` → `/api`, `vite.config.js` proxy + allowedHosts); tải cloudflared 2026.10.7 vào `D:\Tools\cloudflared` (SV đồng ý, chữ ký Cloudflare hợp lệ); `tools/usability_session.ps1`, `tools/sut_main.ps1`; sửa plan.md mục 5–6 và thêm 1 dòng vào participant_kit.md theo lệnh SV; check_kit 0 lỗi. SV tự thử luồng qua 4G.
- 10/11 Claude Code (skill): cập nhật `gui-checklist-testing` (chế độ Playwright, gộp V1, quy tắc ảnh, đọc slide trước bước 1, quy tắc 9; chuyển `merge_hw03.py`/`failed_list_hw03.py`/`bug_groups_hw03.py` thành `scripts/merge_runs.py`/`failed_list.py`/`bug_groups.py` tổng quát, `tools/` giữ wrapper dữ liệu HW03; schema thêm trường auto) và `usability-evaluation` (bước 0: lựa chọn remote synchronous + tunnel). Chạy lại trên dữ liệu HW03: checklist.json, CSV, checklist.md, failed_list, bug_groups, BUG-58…85, report giống hệt; Excel 2144 ô, 0 ô khác.
- 10/11 Claude Code (4/6c, Skill 1/3, 1/3b, report): R9/R11 áp bằng override `merge_hw03.py`; `merge_runs.py` bỏ `lech_auto_tay` khi quyết định làm tay = auto (nguyên nhân chuyển vào notes); chép skill sang `HW03/skills/` + `VideoLinks.md` + `demo_plan.md` (đề xuất demo); D1 sửa SKILL.md/`render_checklist.py`; `bugs/dup_check.md` (kiểm trùng 179 issue, AI đề xuất mức, SV quyết); `report_t1_hw03.py` thêm khối §3.3, §3.5 (thực thi), §3.6, §4.3; **AI nháp §3.2 và §4.2 của report** (dòng "📝 AI nháp – SV duyệt/sửa", chỉ dùng dữ kiện trong repo).
- **Lỗi RUN.md do AI** (phát hiện 10/11 khi lập `missing_photos.md`): `gen_run.py` (AI viết, 3/6) ghi "ảnh tổng quan bắt buộc: `P<n>_M6_1.png`" cho nhóm M6, mâu thuẫn mục 2 của chính RUN.md (M1…M5) → sửa 4/6e.
- 10/11 Claude Code (4/6e): sửa tiêu đề M6 (`RUN.md`, `gen_run.py`), bỏ tham chiếu `P3_CL-64_1.jpg` theo SV, ghi chú `P3_M4_1`; xem 5 ảnh P3_M* – chưa có overlay → dừng, chưa nén.
- 10/11 Claude Code (4/6f): xem từng ảnh P3_M1_1…P3_M4_1 sau khi SV overlay (đủ overlay, URL localhost, không lộ thông tin riêng), nén bằng `tools/compress_hw03.py`, chạy lại report §4.3.
- 10/11 phiên thảo luận 19:23: AI dựng Google Form (Apps Script) cho SEQ + SUS + 4 câu hỏi mở từ `participant_kit.md`; CSV form có họ tên/SĐT không vào repo.
- 10/11 phiên thảo luận 19:29–19:31: AI nháp kịch bản điều phối `usability/moderator_script.md` (phiên ~10 phút); Claude Code commit nguyên văn (2c/10), sửa plan mục 3, 5 theo SV chốt (2d/10).
- 10/11 Claude Code (5/6e): **AI viết `tests/repro_bugs.spec.ts` + `tests/repro.config.ts`** (Playwright chạy lại Steps SV của BUG-58…85 trên P1/P2, số đo `bugs/repro/repro_P*.json`) và `bugs/bug_check.md` (kiểm dữ kiện, chỉ liệt kê, không đề xuất câu chữ).
- 11/11 Claude Code (T2 2/10–9/10): **AI dựng 8 phiếu `usability/sessions/S00…S07.json`** từ notes SV ghi tay (`sessions/notes/`) + CSV Google Form (chỉ cột mã phiên, đồng ý, SEQ, SUS, 4 câu mở) bằng `tools/usability_fill_hw03.py` (AI viết); nhãn "AI chép, SV duyệt"; thời gian / hoàn thành / trợ giúp để SV điền. Thêm `HW03/usability/evidence_raw/` vào `.gitignore`.
- 10/11 Claude Code (5/6c): `bugs/dup_check.md` (kiểm trùng 179 issue, AI đề xuất mức, SV quyết); khung `BUG-58…85` theo mẫu HW02 bằng `tools/bug_skeleton_hw03.py` (chỉ dữ kiện); `checklist/missing_photos.md`.
- 11/11 Claude Code (6/6): tạo 28 issue #247–#274 bằng `gh issue create --body-file` với file BUG SV viết (SV xác nhận bảng trước khi tạo); ghi link vào BUG-xx, README, report.
- 11/11 Claude Code (5/6g): `bugs/bug_check2.md` (kiểm lại 14 bug SV sửa; chỉ liệt kê, không đề xuất câu chữ).
- 11/11 Claude Code: khôi phục dòng Dữ kiện BUG-72 về đúng `checklist.json`, `gh issue edit #266` + comment theo lệnh SV, nhật ký `bugs/issue_edits.md`; ảnh trang Issues `[HW03-C2]` (Playwright chụp, `bugs/issues_page_HW03-C2_*.png`) chèn report §6.
- 11/11 Claude Code (T2 10/10): `sus_score.py --check/--report` → REPORT:U1; `tools/summary_hw03.py` thêm dòng U1; đối chiếu 7 pain point §5.8 ↔ issue nhóm (chỉ đọc, trả lời trong phiên – SV tự ghi cột liên quan).
- 11/11 Claude Code: prompt log thêm transcript claude.ai p2; `prompt_log_turns.txt`; `tools/forms_hw03.py` thêm artifact B1–B7, U3–U6, R4, cột #n theo dải lượt trước commit, lý do lượt không rõ model chờ SV; §11 thêm mục 8–12.
- Lỗi phiên thảo luận: `[...]`.

## g. Danh sách cho Mandatory Disclosure (ghi dần)

- AI tạo bản đầu (danh mục đủ: AI-02 mục 3.1, report §11 mục 1–12): checklist nháp 65 item, gói usability nháp, Playwright + RUN.md, Excel, bảng report, khung BUG (chỉ dữ kiện), kiểm trùng issue, bug_check/bug_check2 + repro, Google Form + moderator_script (phiên thảo luận), phiếu phiên S00…S07 AI chép, khung AI-02/AI-03, script/harness.
- SV xem xét và sửa: `[...]`.
- Item SV bổ sung (🔒, kèm lý do AI bỏ sót): `[...]`.
- SV tự làm hoàn toàn: tuyển + danh sách 7 người, điều phối phiên, ghi chú quan sát, câu trả lời SUS, ảnh cross-platform có overlay, bug report, Critique, verdict Audit, điểm tự chấm, giọng video.
- Dữ liệu người tham gia (cho AI-05): SV đã gửi CSV có họ tên/SĐT người tham gia cho phiên thảo luận claude.ai lúc 00:43 11/11; AI chỉ dùng cột SEQ/SUS. CSV (`usability/evidence_raw/responses.csv`) không commit; Claude Code chỉ đọc cột mã phiên, đồng ý, SEQ, SUS, câu hỏi mở.
- Prompt log: trích tự động bằng `tools/extract_prompt_log.py` (hook `on_stop.py`); Section/Mục đích/Xử lý do em ghi.

## h. Lịch (deadline 10:00 thứ Tư 11/11/2026)

| Khi | Việc |
|---|---|
| T2 09/11 tối | Chạy tay checklist (P1, P2, P3) theo RUN.md |
| T3 10/11 ngày | T1 bước 4/6 (gộp kết quả P1–P3) + form AI-02/03/05 |
| T3 10/11 tối | Pilot + 7 phiên usability (S1–S7) |
| Đêm T3 → sáng T4 11/11 | Phân tích usability + report + zip; nộp trước 10:00 |
