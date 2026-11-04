# Prompt Log – HW03
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude Opus 5.5

> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script `tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.

---

## #1 | 17:15 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – kiểm chứng P3 (chỉ kiểm, chưa commit gì)
1. gh issue list -R tkob-team/eshop-sut --state all -L 500 --json number,title,author > $env:TEMP\issues.json; in số issue theo author.
2. adb version; nếu thiếu: hỏi tôi trước khi tải platform-tools (dl.google.com), giải nén vào D:\Tools\platform-tools.
3. adb devices (phải thấy 1 thiết bị "device").
4. Chạy ..\eshop-sut\backend: node server.js (nền); ..\eshop-sut\frontend-web: npx vite --host 127.0.0.1 --port 5173 (nền).
5. adb reverse tcp:5173 tcp:5173; adb reverse tcp:3000 tcp:3000; adb reverse --list.
6. Dừng, chờ tôi mở Chrome trên điện thoại vào http://localhost:5173 và đăng nhập test@eshop.com/Test1234!.
Báo cáo ≤ 10 dòng: kết quả từng bước + lỗi nguyên văn nếu có.
```

**Output:**
```
Đã chạy bước 1–4. Bước 3 và 5 chặn vì adb không thấy điện thoại.

- **1. Issues:** tổng 158 — henry-banana 64, ThachHaoo 57, nphoang-itus 37. JSON ở `$env:TEMP\issues.json`.
- **2. adb:** lúc đầu chưa có (`The term 'adb' is not recognized…`). Sau khi bạn đồng ý, em đã tải và giải nén vào `D:\Tools\platform-tools`, chạy được (`adb version 1.0.41`, `Version 37.0.1-15733141`). Em không sửa PATH, nên phải gọi bằng đường dẫn đầy đủ `D:\Tools\platform-tools\adb.exe`.
- **3. adb devices:** **Fail** — chỉ in `List of devices attached`, không có thiết bị nào, kiểm lại vẫn trống.
- **4. Server:** backend đang lắng nghe `:3000` (log: `Database initialized and seeded (Phase 2).`); web đang chạy ở `http://127.0.0.1:5173/` (`VITE v8.0.12 ready`). Cả hai chạy nền, CSDL vừa seed lại.
- **5. adb reverse:** **chưa chạy được** — `adb.exe: no devices/emulators found`.
- **6.** Chưa tới bước này.

Để adb thấy máy: trên điện thoại bật Developer options → USB debugging, cắm cáp dữ liệu, chọn chế độ USB là "File transfer", rồi bấm Allow ở hộp thoại hỏi khoá RSA. Xong báo em để chạy lại bước 3 và 5.
```

**Xử lý:** [...]

---

## #2 | 17:31 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – kiểm chứng P3, chạy lại bước 3, 5, 6 (backend + web vẫn chạy nền; nếu đã tắt thì chạy lại như bước 4).
- D:\Tools\platform-tools\adb.exe devices → phải là "<serial>  device". Nếu "unauthorized" → dừng, báo tôi.
- adb reverse tcp:5173 tcp:5173; adb reverse tcp:3000 tcp:3000; adb reverse --list.
- Dừng, chờ tôi mở Chrome trên điện thoại vào http://localhost:5173 và đăng nhập test@eshop.com / Test1234!.
Báo cáo ≤ 8 dòng.
```

**Output:**
```
Bước 3 và 5 qua. Em dừng ở bước 6, chờ bạn mở Chrome trên điện thoại.

- **Server:** backend `:3000` và web `127.0.0.1:5173` vẫn chạy nền, em không khởi động lại.
- **3. adb devices:** `da87b223  device` (model 23049PCD8G), không báo `unauthorized`.
- **5. adb reverse:** lệnh cho 5173 và 3000 trả về `5173` và `3000`. `--list` có `UsbFfs tcp:5173 tcp:5173` và `UsbFfs tcp:3000 tcp:3000`.
- **6.** Bạn vào `http://localhost:5173` trên Chrome điện thoại, đăng nhập `test@eshop.com` / `Test1234!`, rồi báo em kết quả.

Nếu rút cáp hoặc adb restart thì phải chạy lại 2 lệnh `adb reverse`.
```

**Xử lý:** [...]

---

## #3 | 17:34 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Kết quả bước 6, đã đăng nhập bình thường
```

**Output:**
```
Đã kiểm xong P3: cả 6 bước đều đạt. Em chưa commit gì và cũng chưa xác nhận lượt đăng nhập từ phía server.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – kiểm chứng P3, chỉ kiểm, không commit.
- **Kết quả:**
  - Issues trên `tkob-team/eshop-sut`: tổng 158 — henry-banana 64, ThachHaoo 57, nphoang-itus 37.
  - adb: lúc đầu máy chưa có, em đã tải về `D:\Tools\platform-tools` (bản 37.0.1, không sửa PATH).
  - `adb devices`: `da87b223  device`.
  - Backend `:3000` và web `:5173` đang chạy nền. Cổng 5173 và 3000 đã được chuyển tiếp từ điện thoại về máy (`adb reverse`).
  - Bước 6: bạn mở Chrome trên điện thoại vào `http://localhost:5173` và đăng nhập `test@eshop.com` bình thường.
- **Commit:** không có.
- **Lưu ý:** rút cáp hoặc restart adb thì phải chạy lại 2 lệnh `adb reverse`. Restart backend thì CSDL bị seed lại.
- **Cần quyết định:** không.
```

**Xử lý:** [...]

---

## #4 | 17:38 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – khung bài (commit "HW03: khung bài + report_plan")
1. tools/hw.toml: hw="HW03", since="2026-11-04", title="Prompt Log – HW03", log/notes/extra → HW03/appendix/… (giữ cấu hình HW02 dạng comment).
2. HW03/: giữ report_plan.md tôi đã đặt; tạo khung README.md và 23120255_HW03_Report.md theo mục c–d của report_plan (📝 = chỗ SV viết, 🔒 = phần cấm AI); thư mục checklist/evidence/{P1_chrome,P2_firefox,P3_android}, usability/sessions, bugs, excel, appendix/ai-outputs, ai-forms, skills (.gitkeep).
3. context/HW03_assignment.md = pdftotext đề D:\HK7\Testing\Exercise\HW\HW03\2026.HW03.GUI Usability_En.pdf; slide HW03 → context/private/ (không commit).
4. CLAUDE.md mục 0: đề hiện tại = HW03; thêm mục "Quyết định HW03" trỏ tới HW03/report_plan.md mục e (không chép dài).
5. on_stop.py --manual; commit. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đã trích đề, chép slide. Giờ sửa `hw.toml`, dựng khung README/Report.

Missing files OK (script returns {}). Write hw.toml + notes/extra headers.

Now dirs + CLAUDE.md.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – dựng khung bài. Đã làm đủ 5 bước; một chỗ khác yêu cầu ở bước 3, xem "Cần quyết định".
- **File đã tạo/sửa:**
  - `tools/hw.toml`: chuyển sang HW03, cấu hình HW02 giữ lại dạng comment.
  - `HW03/README.md` và `HW03/23120255_HW03_Report.md`: khung theo mục c–d, có 📝/🔒.
  - Các thư mục đã yêu cầu, mỗi thư mục có `.gitkeep`.
  - `HW03/appendix/prompt_log_notes.toml` và `prompt_log_extra.toml`: hai file trống, chỉ có phần hướng dẫn ở đầu. Lệnh không yêu cầu, em thêm để cấu hình trong `hw.toml` trỏ tới.
  - `context/HW03_assignment.md`: trích bằng pdftotext của Git, dạng text giữ bố cục, không phải markdown như đề HW02.
  - Thêm mục "Quyết định HW03" vào CLAUDE.md, trỏ tới report_plan mục e.
  - `HW03/report_plan.md`: giữ nguyên bản bạn đặt, chỉ commit.
- **Kết quả kiểm tra:** `on_stop.py --manual` chạy được, prompt log ghi 10 lượt (Claude Opus 5.5). Bài HW03 không có bước check_domain, lint hay test.
- **Commit:** `c409e1c HW03: khung bài + report_plan`
- **Cần quyết định:**
  - Slide – thư mục đề `D:\HK7\Testing\Exercise\HW\HW03` không có slide nào. Em đã chép `S13_GUI Testing & Usability Testing.pdf` và `EN.GUI + Usability + Compatibility Testing AI-First (Combined).pdf` từ `D:\HK7\Testing\Slides\` vào `context/private/` (không commit). Hai bản đúng chưa, hay cần thêm các file trong `Slides\Refs\` và `Templates\UI Checklist\`?
  - CLAUDE.md mục 1 vẫn ghi "HW02 … (đang làm)". Đổi thành "đã nộp" không?
```
*File AI ghi/gửi trong lượt này:* `hw.toml`, `prompt_log_notes.toml`, `prompt_log_extra.toml`, `README.md`, `23120255_HW03_Report.md`

**Xử lý:** [...]

---

## #5 | 17:44 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 3 việc, mỗi việc 1 commit. Đọc HW03/report_plan.md trước.

A. report_plan mục e (commit "HW03: chốt E1, O1, T"):
- E1=a: Excel mới HW03/excel/23120255_HW03_Checklist.xlsx, 3 sheet như HW01.
- O1: overlay "23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn"; PC = Sticky Notes + chụp toàn màn hình (thấy tên trình duyệt + URL); điện thoại = thêm chữ bằng trình sửa ảnh ngay sau khi chụp.
- T=SUS (10 câu tiếng Việt) + SEQ (1 câu sau nhiệm vụ); bộ câu hỏi tối giản vì có người non-IT.
- Xoá 3 mục này khỏi "Còn chờ SV chốt".

B. AI nháp checklist C2 (commit "HW03[T1] 1/6: AI nháp checklist C2"):
1. Khảo sát ..\eshop-sut\frontend-web: Login, ForgotPassword, Profile, navbar App.jsx (khi đã đăng nhập) → liệt kê control từng màn kèm file:dòng → HW03/checklist/c2_inventory.md.
2. Cùng file: trích yêu cầu UI từ SRS README.md (FR-21…24 + phần UI của FR-02, FR-03, FR-04, FR-11), ghi số dòng.
3. Sinh ≥ 45 item vào HW03/checklist/checklist.json theo 3 nguồn trong slide (context/private): (a) điều khoản SRS, (b) checklist theo control (text box, button, link, validation), (c) heuristic Nielsen/Norman/Shneiderman. Mỗi item: id CL-xx, ia (IA-01…04), man_hinh, muc_kiem_tra, can_cu, expected (quan sát được, có ngưỡng Pass/Fail), uu_tien (Mandatory/Optional), nen_tang (P1/P2/P3; N/A phải kèm giả định), nguon="AI". Đủ 4 IA, không trùng nhau.
4. Render checklist.md; chép nguyên bản JSON vào HW03/appendix/ai-outputs/T1_checklist_ai_v1.json (đóng băng). Không chạy SUT để chỉnh Expected theo hành vi quan sát.

C. AI nháp gói usability U1 (commit "HW03[T2] 1/10: AI nháp gói usability"):
HW03/usability/:
- plan.md: kế hoạch 9 phần theo slide, ngắn.
- participant_kit.md: 1 trang phát người tham gia — lời mở đầu (kiểm sản phẩm, không kiểm bạn; xin đồng ý quay màn hình + ghi âm; TA có thể gọi xác nhận), nhiệm vụ U1 dạng mục tiêu (không chỉ bước), SEQ, SUS 10 câu, 4 câu hỏi mở (rõ ràng / khôi phục lỗi / tốc độ / tin cậy).
- observation_sheet.md: phiếu trống cho SV (thời gian, lỗi, do dự, câu nói, lần cần trợ giúp).
Kiểm nhiệm vụ làm được trên dữ liệu seed (tài khoản test@eshop.com, mã giảm giá đủ ngưỡng). KHÔNG tạo bảng người tham gia (SV tự làm). Chép bản đầu vào appendix/ai-outputs/T2_*_v1.md (đóng băng).

Cuối: on_stop.py --manual. Báo cáo ≤ 15 dòng: đường dẫn, số item theo từng IA, các commit.
```

**Output:**
```
Đang khảo sát SUT (đọc xong 4 màn), giờ đọc SRS.

Khảo sát xong. Viết `c2_inventory.md`.

Viết checklist JSON (dùng script tạm để đánh số tự động).

Checklist xong (65 item, commit `39f685c`). Giờ kiểm luồng U1 trên mã để viết gói usability.

Đã thử luồng U1 qua API: SAVE10 tính sai, VIP100/BIGBUY đúng. Restart backend để xoá đơn thử, rồi viết gói usability.

Empty → seed reset OK. Run prompt log.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – chốt E1/O1/T, AI nháp checklist C2, AI nháp gói usability U1. Cả 3 việc xong, mỗi việc một commit.
- **File:**
  - `HW03/report_plan.md` (mục e)
  - `HW03/checklist/c2_inventory.md`, `checklist.json`, `checklist.md`
  - `tools/render_checklist.py`: script render mới, cần khai trong Audit
  - `HW03/usability/plan.md`, `participant_kit.md`, `observation_sheet.md`
  - Bản đóng băng: `HW03/appendix/ai-outputs/T1_checklist_ai_v1.json` và `T2_{plan,participant_kit,observation_sheet}_v1.md`
- **Checklist: 65 item** — IA-01: 16 · IA-02: 23 · IA-03: 11 · IA-04: 15.
  - Theo căn cứ: SRS 40, heuristic 17, checklist theo control 8. Mandatory 48, Optional 17.
  - Có 3 giả định: NA1 (thứ tự Tab trên P3 ghi N/A), GA1 (định dạng ngày), GA2 (badge giỏ hàng).
- **Kiểm luồng U1:** chạy qua API trên dữ liệu seed, đi trọn từ đăng nhập → tìm "tai nghe" → áp mã → đặt hàng → đơn hiện trong lịch sử. Sau đó em restart backend, lịch sử đơn trả `[]`. Prompt log ghi 11 lượt; file `A_prompt_log.md` đã cập nhật nhưng chưa commit vì lệnh không yêu cầu.
- **Commit:**
  - `4ab90da HW03: chốt E1, O1, T`
  - `39f685c HW03[T1] 1/6: AI nháp checklist C2`
  - `c081f96 HW03[T2] 1/10: AI nháp gói usability`
- **Cần quyết định:**
  - **K1 – mã giảm giá trong nhiệm vụ.** `SAVE10` tính sai: đơn 6.000.000 ₫ ra `final_amount` 60.000.000, `discount_amount` −54.000.000 (`backend/server.js`, handler từ dòng 363). Gói usability đang dùng `VIP100` (tính đúng, giảm 100.000 ₫). Phương án: (a) giữ `VIP100`; (b) dùng `SAVE10` để người tham gia gặp lỗi này. Riêng việc có lập bug cho SAVE10 hay không, em chưa đưa vào đây, bạn quyết sau.
- **Bất thường (AI phát hiện):**
  - Quy tắc chặn sửa `ai-outputs/` và `A_prompt_log.md` trong `.claude/settings.json` mới chỉ áp cho HW02, HW03 chưa được bảo vệ. Có nên thêm quy tắc tương tự cho HW03 không?
```
*File AI ghi/gửi trong lượt này:* `c2_inventory.md`, `gen_checklist.py`, `render_checklist.py`, `plan.md`, `participant_kit.md`, `observation_sheet.md`

**Xử lý:** [...]

---

## #6 | 17:57 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – cấu hình + K1 (commit "HW03: bật hook Stop, bảo vệ ai-outputs/prompt log, K1")
1. Hook: <a: thêm lại Stop on_stop.py như trước be8996e | b: giữ tắt>. Deny Edit/Write HW03/appendix/ai-outputs/** và HW03/appendix/A_prompt_log.md.
1b. extract_prompt_log.py: --since/--until nhận thêm "YYYY-MM-DD HH:MM" (vẫn nhận ngày như cũ); hw.toml since = "2026-11-04 12:26". Chạy --list cho ngày 04/11, in giờ + 60 ký tự đầu prompt từng lượt để tôi kiểm còn lượt HW02 nào lọt vào không. Vá harness → commit riêng "HW03: vá harness – since theo giờ".
2. report_plan mục e: K1=a (VIP100; lý do: usability đo thiết kế, không để bug tính tiền đã biết làm nhiễu SUS). Mục f: "AI phát hiện khi kiểm luồng U1: SAVE10 tính sai (server.js:400), ngưỡng dùng > thay vì >= (server.js:379) – chưa quyết lập bug".
3. Kiểm trùng trong $env:TEMP\issues.json: issue nhắc SAVE10 / percent / mã giảm giá / apply-coupon → in số, tiêu đề, author.
4. HW03/.gitattributes: report_plan.md export-ignore. report_plan mục c thêm cột "Nộp?".
5. on_stop.py --manual (gồm A_prompt_log.md chưa commit); commit; nhắc tôi push. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đang vá `--since` theo giờ; kiểm chỗ khác dùng `since`.

epl module loaded → reuse parse_bound.

Đang sửa report_plan mục e/f, rồi `.gitattributes` và commit.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – bật lại hook Stop, chặn sửa file AI/prompt log, vá `since` theo giờ, chốt K1. Đã làm đủ, 2 commit.
- **File:**
  - `.claude/settings.json`: bật lại hook Stop, chép nguyên khối như trước `be8996e`; chặn Edit/Write `HW03/appendix/ai-outputs/**` và `HW03/appendix/A_prompt_log.md`.
  - `tools/extract_prompt_log.py`: `--since`/`--until` nhận thêm `YYYY-MM-DD HH:MM`.
  - `tools/audit_tables.py`: sửa theo, vì script này cũng đọc `since` — để nguyên sẽ báo lỗi với giá trị có giờ.
  - `tools/hw.toml`: `since = "2026-11-04 12:26"`.
  - `HW03/report_plan.md`: thêm K1 ở mục e, dòng "AI phát hiện" ở mục f, cột "Nộp?" ở mục c.
  - `HW03/.gitattributes`: `report_plan.md` không vào zip. Đã thử `git archive`: zip không có `report_plan.md`, nhưng có chính file `.gitattributes`.
- **Kiểm tra:**
  - Lọc theo ngày như cũ cho HW02 vẫn ra 407 lượt (cũ: 407).
  - Prompt log HW03 hiện có 12 lượt.
  - Danh sách lượt 04/11 (giờ | đầu prompt):
    - #1 17:15 | HW03 – kiểm chứng P3
    - **#2 17:24 | `d:\…\HW02\append…`**
    - **#3 17:27 | Mình chỉ cần giữ lại tất cả lệnh của hôm nay…**
    - **#4 17:28 | À thôi bỏ hết đi, vì log hiện tại không phải của HW02…**
    - **#5 17:29 | commit đi kiểu end HW02**
    - **#6 17:30 | Ủa khoan, Undo lại nhé…**
    - **#7 17:31 | Rồi commit nhé**
    - #8 17:31 | HW03 – kiểm chứng P3, chạy lại bước 3, 5, 6
    - #9 17:34 | Kết quả bước 6
    - #10 17:38 | HW03 – khung bài
    - #11 17:44 | HW03 – 3 việc
- **Issue trùng:** mã giảm giá thuộc nhóm FR09 của henry-banana.
  - SAVE10 tính sai: trùng **#126** "[FR09-03] A 10 percent coupon returns a negative discount and increases total".
  - Ngưỡng dùng `>` thay vì `>=`: trùng **#124** (fixed) và **#125** (percent) "…rejected at its exact minimum total".
  - Liên quan: #134 (mã 100% cho discount âm).
- **Commit:**
  - `eced5dd HW03: vá harness – since theo giờ`
  - `e4dcd91 HW03: bật hook Stop, bảo vệ ai-outputs/prompt log, K1`
- **Nhắc:** bạn tự push (`git push`).
- **Cần quyết định:**
  - **L1** – Lượt #2–#7 (17:24–17:31) là việc kết thúc HW02 nhưng nằm sau mốc 12:26 nên vẫn vào log HW03. Phương án: (a) dời `since` sang 17:32 (cũng loại luôn #1, vì #1 lúc 17:15); (b) giữ, ghi lý do trong `prompt_log_notes.toml`.
```
*File AI ghi/gửi trong lượt này:* `.gitattributes`

**Xử lý:** [...]

---

## #7 | 18:10 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – harness, mỗi mục 1 commit. Phần skill dùng skill testing-technique-skill-template.
1. "HW03: tách CLAUDE.md theo bài": CLAUDE.md gốc chỉ giữ phần chung (vai trò, khối báo cáo, giới hạn AI, prompt log, git/push/amend, zip git archive + export-ignore, mẹo PowerShell, SUT chung), ≤ 200 dòng. Chuyển §1 + quyết định HW02 NGUYÊN VĂN sang HW02/CLAUDE.md. Tạo HW03/CLAUDE.md ≤ 120 dòng: đề, rubric, phạm vi C2/U1, P1–P3 + adb reverse (D:\Tools\platform-tools, vite --host 127.0.0.1), quyết định (trỏ report_plan mục e), giới hạn riêng (🔒 item SV thêm, dữ liệu người tham gia, ảnh overlay, SUS do người tham gia điền), quy trình T1/T2/T3 + mẫu commit. Kiểm không mất dòng: in số dòng trước/sau từng file.
2. "HW03: HARNESS_SETUP – bắt đầu bài mới": thêm mục checklist bắt đầu bài (hw.toml since theo giờ + exclude, deny ai-outputs/prompt log, HWxx/CLAUDE.md, slide → context/private, .gitattributes export-ignore, transcript claude-ai_session_<HW>_p1).
3. L1=c: (như lệnh trước — exclude trong hw.toml, dry-run HW02 vẫn 407).
4. "HW03: skill gui-checklist-testing (khung)": .claude/skills/gui-checklist-testing/ theo mẫu domain-bva-testing — SKILL.md 7 bước (0 khảo sát · 1 nháp theo 3 nguồn + freeze · 2 SV thêm 🔒 + gap · 3 RUN.md + dom_probe.js · 4 chạy từng nền tảng + merge · 5 Excel + test summary · 6 gom dữ kiện bug), references/schema-checklist.md, scripts check_checklist.py, freeze, render (từ tools/render_checklist.py), merge_platform.py, build_excel.py. Chạy check_checklist.py trên HW03/checklist/checklist.json để thử; chưa đổi dữ liệu HW03.
on_stop.py --manual. Báo cáo ≤ 15 dòng. Nhắc tôi push.
```

**Output:**
```
Item 1: tách CLAUDE.md. Dựng HW02/CLAUDE.md bằng script (chép nguyên văn dòng 55–248).

Giờ viết CLAUDE.md gốc (phần chung).

Global gitignore chặn `CLAUDE.md` → thêm ngoại lệ trong `.gitignore` của repo, commit tiếp (không amend).

Item 2: HARNESS_SETUP mục 6.

Implement `--exclude` + wire into on_stop and audit_tables.

Item 4: load skill template.

Đang dựng skill `gui-checklist-testing`; đọc cấu trúc Excel HW01 (qua zipfile, máy chưa có openpyxl).

Viết SKILL.md + schema.

Scripts: check, freeze, render, merge, excel.

Update render to include per-platform notes; then build_excel + assets.

Kiểm thử script (không đổi dữ liệu HW03; merge/freeze chạy trên bản sao trong tmp).

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – 4 việc harness. Xong cả 4, tổng 5 commit: mục 1 tốn 2 commit vì một chỗ chặn của gitignore toàn cục. Chưa đổi dữ liệu HW03.
- **1. Tách CLAUDE.md:**
  - Số dòng trước: `CLAUDE.md` 248. Sau: `CLAUDE.md` gốc 112, `HW02/CLAUDE.md` 205 (§1, §2, §5, §6 và các dòng HW02 của §3–§4, chép nguyên văn), `HW03/CLAUDE.md` 91.
  - Script so từng dòng: chỉ 6 dòng gốc không còn nguyên văn — các dòng 10, 34, 37, 38, 40, 42 (quy tắc ghi quyết định, danh sách "đọc gì trước", mục Quyết định HW03). Nội dung vẫn còn, chỉ viết lại cho chung.
- **2. HARNESS_SETUP:** thêm mục 6, checklist bắt đầu bài mới gồm 7 bước.
- **3. L1=c:**
  - `extract_prompt_log.py` thêm `--exclude` (lặp được); `on_stop.py` và `audit_tables.py` đọc `exclude` từ `hw.toml`.
  - `exclude` bỏ 17:24–17:30 và lượt 17:31 đầu tiên; lượt 17:31#2 là của HW03 nên giữ.
  - Prompt log HW03 còn 7 lượt. Lọc lại HW02 vẫn ra 407 lượt.
- **4. Skill `.claude/skills/gui-checklist-testing/`:**
  - `SKILL.md` 7 bước, `references/schema-checklist.md`, `assets/dom_probe.js`, `assets/RUN_template.md`.
  - Scripts: `check_checklist`, `freeze`, `render_checklist` (chuyển từ `tools/`, ở `tools/` để lại script chuyển tiếp), `merge_platform`, `build_excel`.
- **Kết quả kiểm tra:**
  - `check_checklist` trên `HW03/checklist/checklist.json`: 0 lỗi, 1 cảnh báo (CL-07 chưa có câu "Fail nếu").
  - `render_checklist` chạy lại cho ra `checklist.md` giống hệt bản đã commit.
  - Thử `merge_platform` và `freeze` trên bản sao trong thư mục tạm: chặn kết quả mâu thuẫn khi không có `--force`, từ chối N/A trên nền tảng đang áp dụng.
  - `build_excel`: **chưa chạy được** vì máy chưa cài `openpyxl`; mới chỉ kiểm cú pháp.
- **Commit:**
  - `e781197`, `24f1345` – tách CLAUDE.md (2 commit)
  - `2d16283` – HARNESS_SETUP
  - `b2e7ef8` – exclude
  - `a1df52c` – skill (khung)
- **Bất thường:** `~/.gitignore_global` dòng 5 chặn mọi file `CLAUDE.md` nên lần commit đầu thiếu `HW02/` và `HW03/CLAUDE.md`. Em thêm `!CLAUDE.md` vào `.gitignore` của repo và commit bổ sung, không amend.
- **Cần quyết định:**
  - X1 – cài `openpyxl` để chạy được `build_excel` (bước 5)? (a) `python -m pip install openpyxl`; (b) để tới bước 5.
  - X2 – `HW03/CLAUDE.md` có nộp trong zip không? (a) thêm `export-ignore`; (b) nộp như tài liệu harness.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `CLAUDE.md`, `CLAUDE.md`, `xl.py`, `SKILL.md`, `schema-checklist.md`, `check_checklist.py`, `freeze.py`, `merge_platform.py`, `build_excel.py`, `dom_probe.js`, `RUN_template.md`

**Xử lý:** [...]

---

## #8 | 18:41 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 2 commit. Không sửa ai-outputs/.

A. "HW03: X1, X2": cài openpyxl đúng trình Python các script đang dùng, chạy thử build_excel.py ra thư mục tạm (không commit xlsx). HW03/.gitattributes thêm CLAUDE.md export-ignore; report_plan mục e: X1=a, X2=a. Tạo khung trống HW03/checklist/sv_items.md (chỉ tiêu đề cột: id SV-xx, ia, man_hinh, muc_kiem_tra, can_cu, expected, nen_tang, ly_do_AI_bo_sot; không ví dụ, không danh mục).

B. "HW03[T1] 2/6: SV review checklist AI": item sửa → nguon="Both"; ghi meta.review_log (ngày, mã quyết định, "SV chốt").
- G1=a: heuristic/WCAG/checklist theo control là căn cứ hợp lệ (slide GUI "Where checklists come from"); severity bug từ các item này do SV quyết.
- G2: NA1 giữ; GA1 giữ; GA2 bỏ → CL-41 chỉ kiểm có badge hiển thị số > 0 sau khi thêm 1 SP (FR-23.2); GA3 mới "Thông báo lỗi chỉ ở hộp thoại alert không thoả FR-22.4" (AI đề xuất, SV chấp nhận).
- G3: CL-44, CL-55 ngưỡng ≤ 1 s, can_cu thêm "Nielsen – response time limits (1 s)".
- G4=a: giữ CL-31/32/34/37, notes "kiểm trùng issue FR-04 trước khi lập bug".
- Sửa: CL-10/11/12 Expected = thứ tự theo vị trí hiển thị (trên→dưới, trái→phải), bỏ chuỗi lấy từ code · CL-13 bỏ vế tên kỹ thuật · CL-45 thành "link tới đúng /forgot-password" (bỏ vế tải lại trang) · CL-28 chỉ giữ "mã hiển thị 6 chữ số" · CL-33 bỏ vế nhãn · CL-17 tách type=email / chặn sai định dạng · CL-43 tách 3 vế · CL-23 căn cứ thêm GA3 · CL-40 bỏ /cart · CL-59 bỏ FR-20 · CL-58 thêm tiền điều kiện dựng đơn 5 trạng thái một lần qua admin, dùng chung 3 nền tảng.
- Item tách: id mới từ CL-66, ghi "tách từ CL-xx"; không đánh số lại.
check_checklist + render; in số item theo IA và theo nguồn (AI/Both). on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

**Output:**
```
Excel chạy được (openpyxl qua pacman MSYS2). Giờ commit A.

Part B: áp review SV vào checklist.json.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – chốt X1, X2 và áp bản review của SV vào checklist (T1 2/6). Xong cả hai. Lệnh yêu cầu 2 commit, thực tế là 3: lần commit A, lệnh sửa `report_plan.md` bị lỗi mà em không thấy, nên phải thêm 1 commit ghi X1/X2 (không amend).
- **X1:** `python` của các script là MSYS2 (`C:\msys64\ucrt64\bin\python.exe` 3.14) và không có pip, nên em cài bằng `pacman -S mingw-w64-ucrt-x86_64-python-openpyxl`. Lệnh này kéo thêm `python-pillow` và vài thư viện ảnh. `openpyxl` 3.1.5 đã chạy được.
  - `build_excel.py` ra thư mục tạm: đủ 3 sheet, có công thức COUNTIF; file xlsx không commit.
- **X2:** `HW03/.gitattributes` thêm `CLAUDE.md export-ignore`. Thử `git archive`: zip không còn `report_plan.md` lẫn `CLAUDE.md`. Đã tạo khung `HW03/checklist/sv_items.md` (chỉ tiêu đề cột).
- **Review:** `checklist.json` và `.md` cập nhật đủ G1–G4 và các sửa.
  - Item tách: CL-66 (từ CL-17); CL-67, CL-68 (từ CL-43).
  - `assumptions`: bỏ GA2, thêm GA3.
  - `meta.review_log` có 5 mục (G1–G4, S), mỗi mục ghi "SV chốt".
  - `ai-outputs/` không sửa.
- **Số item: 68.** Theo IA: IA-01 16 · IA-02 24 · IA-03 13 · IA-04 15. Theo nguồn: AI 49 · Both 19.
  - CL-31/32/34/37 chỉ thêm notes nên em giữ `nguon` = AI. Nếu bạn muốn tính là "sửa" thì đổi thành Both.
- **Kết quả kiểm tra:** `check_checklist` 0 lỗi, 1 cảnh báo (CL-07 chưa có câu "Fail nếu"). Prompt log 8 lượt.
- **Commit:**
  - `b8a86e9 HW03: X1, X2`
  - `d7dc423 HW03: X1, X2 – ghi quyết định vào report_plan mục e`
  - `a8b8560 HW03[T1] 2/6: SV review checklist AI`
- **Cần quyết định:** không có điểm chặn. Lưu ý: commit 2/6 hiện mới là phần review; item SV tự thêm (`sv_items.md`) chưa có, và `HW03/CLAUDE.md` đang định nghĩa bước 2 gồm cả phần đó.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `review_b.py`

**Xử lý:** [...]

---

## #9 | 19:27 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 3 commit. Không sửa sv_items.md, không sửa ai-outputs/.
A. "HW03[T1] 2/6: vá CL-07": thêm vế "Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size". report_plan mục e: E2=b (Playwright tự chạy item DOM/bàn phím trên P1 Chrome channel + P2 Firefox Playwright → auto_status; SV chạy tay phần còn lại + toàn bộ P3; verdict chính thức = lượt trên trình duyệt thật).
B. Kiểm sv_items.md (CHỈ ĐỌC): trường thiếu/"(SV chưa ghi)", ia hợp lệ, id trùng, can_cu trỏ tới dòng SRS có thật, item trùng nội dung CL-xx → ghi HW03/checklist/sv_items_check.md (chỉ liệt kê, không đề xuất câu chữ). Commit chung với C.
C. "HW03[T1] 2/6c: AI trả lời vì sao bỏ sót": HW03/checklist/ai_gap_answer.md — mỗi SV-xx xếp đúng 1 nhóm: (1) đã nghĩ tới nhưng không đưa vào, (2) không nghĩ tới, (3) đã có nhưng bị gỡ theo quyết định SV. Bằng chứng phải lấy từ bản v1 (T1_checklist_ai_v1.json, c2_inventory.md, prompt của lệnh 1/6): nhóm (1) chỉ khi inventory/v1 có nhắc tới; không có bằng chứng → nhóm (2) và ghi "không có dấu vết trong v1". Nêu nguyên nhân khả dĩ (prompt / giới hạn model / đặc điểm giao diện), ghi rõ là nhận định của AI. Không viết thay cột ly_do_AI_bo_sot của SV.
on_stop.py --manual (commit cả A_prompt_log.md). Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

**Output:**
```
Đang kiểm `sv_items.md` (chỉ đọc): đối chiếu tên slide được trích.

Viết `sv_items_check.md` và `ai_gap_answer.md`.
```
*File AI ghi/gửi trong lượt này:* `sv_items_check.md`, `ai_gap_answer.md`

**Xử lý:** [...]

---

**Tổng:** 9 lượt; Claude Opus 5.5 9 lượt (#1, #2, #3, #4, #5, #6, #7, #8, #9).
