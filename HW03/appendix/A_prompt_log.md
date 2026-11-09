# Prompt Log – HW03
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude (không rõ model), Claude Opus 5.5

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

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03 – vá CL-07 + chốt E2, kiểm `sv_items.md` (chỉ đọc), AI trả lời vì sao bỏ sót. Xong cả 3, gộp thành 2 commit theo lệnh. Không sửa `sv_items.md` và `ai-outputs/`.
- **A – vá CL-07:** thêm vế "Fail nếu chênh chiều cao > 2 px hoặc khác font-family/font-size", `nguon` đổi thành Both, `review_log` thêm mục S2. `report_plan` mục e thêm E2=b.
  - `check_checklist`: 0 lỗi, 0 cảnh báo. 68 item: AI 48, Both 20.
- **B – kiểm `sv_items.md`** (kết quả ở `HW03/checklist/sv_items_check.md`):
  - Không thiếu trường nào; `ia` hợp lệ; id không trùng.
  - Không item nào trích dòng SRS. 6 tên slide được trích đều có trong slide; riêng SV-01 gộp 2 slide thành một tên.
  - SV-05: P1/P2 ghi N/A nhưng không kèm mã giả định.
  - SV-06 trùng một phần với CL-53.
  - `luc_them` ghi "trong lúc chạy P1/P2/P3", nhưng repo chưa có lượt chạy nào.
  - 6 item SV chưa được đưa vào `checklist.json`.
- **C – vì sao bỏ sót** (`HW03/checklist/ai_gap_answer.md`):
  - Nhóm (1) đã nghĩ tới nhưng không đưa vào: SV-06, bằng chứng là CL-53 của v1.
  - Nhóm (2) không nghĩ tới: SV-01…SV-05, đều "không có dấu vết trong v1". Riêng SV-03: đoạn slide có Golden Rule nằm trong phần AI đã đọc ở lượt 1/6 mà v1 vẫn không có item nào.
  - Nhóm (3) bị gỡ theo quyết định SV: không có.
- **Commit:**
  - `9463442 HW03[T1] 2/6: vá CL-07`
  - `de4c69a HW03[T1] 2/6c: AI trả lời vì sao bỏ sót` (gồm cả B và prompt log 9 lượt)
- **Cần quyết định:** M1 – đưa 6 item SV vào `checklist.json` thế nào? (a) AI chép nguyên văn sang JSON với id SV-xx, `nguon` = SV; (b) SV tự chép.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `sv_items_check.md`, `ai_gap_answer.md`

**Xử lý:** [...]

---

## #10 | 19:47 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 2/6d – chốt checklist v2 (commit "HW03[T1] 2/6d: gộp item SV, chốt checklist v2"):
1. Kiểm lại sv_items.md (chỉ đọc) như 2/6b; còn lỗi cấu trúc → DỪNG, báo tôi.
2. M1=a: chép NGUYÊN VĂN SV-01…SV-06 vào checklist.json (id SV-xx, nguon="SV", thêm luc_them, ly_do_AI_bo_sot); giả định SV (nếu còn) vào assumptions. Không sửa chữ của tôi; trường trống → "(SV chưa ghi)".
3. check_checklist + render; meta.version = "v2 – chốt sau review SV". In số item theo IA và theo nguồn (AI/Both/SV).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

**Output:**
```
Em đã dừng ở bước 1: `sv_items.md` (bản `d173b63`) còn một lỗi cấu trúc, nên chưa gộp vào `checklist.json` và chưa commit.

- **Lỗi chặn – SV-05:** dòng 84 ghi `nen_tang: P3 (P1, P2 N/A)` nhưng không kèm mã giả định. Quy tắc ở đầu file yêu cầu N/A phải có mã, và `check_checklist.py` cũng đòi item có trường `na`. GA4 giờ đã ghi "không dùng" nên không còn mã nào để trỏ tới. Bạn chọn một trong ba cách:
  - (a) Thêm giả định mới, ví dụ GA5/NA2, vào bảng giả định, rồi ghi `P1, P2 N/A theo <mã>`.
  - (b) Dùng lại GA4 với nội dung mới.
  - (c) Cho SV-05 áp dụng cả P1 và P2.
- **Không chặn, ghi để bạn biết:**
  - SV-02 dòng 44: tiền điều kiện đang nằm trong `expected`, dạng `*Tiền điều kiện:* …<br>`. Nếu chép nguyên văn thì nó vẫn ở trong `expected`, không sang trường `tien_dieu_kien`.
  - Phần còn lại đạt: đủ trường, `ia` hợp lệ, id không trùng, mọi item có câu "Fail nếu", `luc_them` của cả 6 item đều ghi "trước khi chạy".

Sửa xong thì báo em chạy lại 2/6d.
```

**Xử lý:** [...]

---

## #11 | 19:53 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 2/6d – chốt checklist v2 (commit "HW03[T1] 2/6d: gộp item SV, chốt checklist v2"):
1. Kiểm lại sv_items.md (chỉ đọc) như 2/6b; còn lỗi cấu trúc → DỪNG, báo tôi.
2. M1=a: chép NGUYÊN VĂN SV-01…SV-06 vào checklist.json (id SV-xx, nguon="SV", thêm luc_them, ly_do_AI_bo_sot); giả định SV (nếu còn) vào assumptions. Không sửa chữ của tôi; trường trống → "(SV chưa ghi)".
3. check_checklist + render; meta.version = "v2 – chốt sau review SV". In số item theo IA và theo nguồn (AI/Both/SV).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

**Output:**
```
Cấu trúc đã sạch (SV-05 → P1–P3, SV-02 tách tiền điều kiện). Gộp vào JSON.

Chỉnh check (id SV-xx) + render (ly_do dạng dict).

Đã gộp 6 item SV vào checklist và commit, nhưng `check_checklist` còn báo 12 lỗi vì 6 item SV chưa có trường `loai_nguon`.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03[T1] 2/6d – gộp item SV, chốt checklist v2.
- **Kiểm `sv_items.md` @ `0600998`:** hết lỗi cấu trúc (SV-05 áp dụng cả P1–P3, tiền điều kiện của SV-02 đã tách thành trường riêng).
- **File:** `HW03/checklist/checklist.json` và `checklist.md`.
  - SV-01…SV-06 chép nguyên văn, `nguon` = SV, có `luc_them` và `ly_do_ai_bo_sot` (loại + giải thích). SV-01 ghi P3 N/A theo NA1.
  - GA4 bạn ghi "không dùng" nên không đưa vào `assumptions`.
  - Phiên bản: "v2 – chốt sau review SV".
  - Hai script của skill sửa theo: `check_checklist` nhận id dạng SV-xx và báo trường "(SV chưa ghi)"; `render_checklist` hiện lý do và lúc thêm của item SV.
- **Số item: 74.** Theo IA: IA-01 19 · IA-02 26 · IA-03 13 · IA-04 16. Theo nguồn: AI 48 · Both 20 · SV 6.
- **Kết quả kiểm tra:** `check_checklist` **Fail – 12 lỗi**, tất cả là `loai_nguon = (SV chưa ghi)` ở SV-01…SV-06, mỗi item 2 lỗi.
- **Commit:** `3f2328f HW03[T1] 2/6d: gộp item SV, chốt checklist v2`
- **Cần quyết định:** L2 – `loai_nguon` của SV-01…SV-06 phải là SRS, Control hoặc Heuristic; mẫu `sv_items.md` không có trường này nên em để "(SV chưa ghi)". Phương án: (a) bạn ghi vào `sv_items.md`, em gộp lại; (b) bạn đọc giá trị cho từng item, em điền vào JSON.
- **Nhắc:** bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `merge_sv.py`

**Xử lý:** [...]

---

## #12 | 19:55 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 2/6d2 (commit "HW03[T1] 2/6d2: SV chốt loai_nguon item SV"): L2=b — điền loai_nguon vào checklist.json: SV-01 Heuristic, SV-02 Heuristic, SV-03 Control, SV-04 Heuristic, SV-05 Heuristic, SV-06 Heuristic (SV chốt theo quy tắc "nguồn đứng đầu can_cu", giống v1). Thêm trường loai_nguon vào khung mẫu RUN/sv_items của skill để lần sau không thiếu. check_checklist phải 0 lỗi; render. on_stop.py --manual. Báo cáo ≤ 5 dòng.
```

**Output:**
```
- `checklist.json`: đã điền `loai_nguon` cho SV-01…06 đúng như bạn chốt (5 Heuristic, SV-03 Control), ghi thêm mục L2 vào `review_log`. `check_checklist` giờ **0 lỗi, 0 cảnh báo**; tổng 74 item (SRS 43, Control 9, Heuristic 22); đã render lại `checklist.md`.
- Skill: thêm khung `assets/sv_items_template.md`, có trường `loai_nguon` và `tien_dieu_kien`. `SKILL.md` bước 2 ghi rõ AI chỉ dựng khung trống. Mẫu RUN không sửa vì RUN không có trường này.
- Commit: `17f747d HW03[T1] 2/6d2: SV chốt loai_nguon item SV` (gồm prompt log, 12 lượt).
- Bạn tự push (`git push`).
```
*File AI ghi/gửi trong lượt này:* `sv_items_template.md`

**Xử lý:** [...]

---

## #13 | 19:57 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 3/6 – theo skill gui-checklist-testing bước 3 (commit "HW03[T1] 3/6: Playwright P1/P2 + RUN.md"). Không sửa expected trong checklist.json.
1. Phân loại 74 item vào trường che_do: auto (đo được bằng DOM/bàn phím/Network trên Playwright) / manual (cần mắt, thiết bị thật, đợi thời gian, tắt backend…) / mixed. In bảng đếm.
2. Playwright (HW03/tests/): chỉ item auto + phần auto của mixed. P1 = channel "chrome" (Chrome đã cài), P2 = firefox của Playwright (ghi rõ đây là bản build Playwright, không phải Firefox đã cài). expect.soft; oracle lấy từ expected của checklist.json (khoá sha1 như HW02). Dựng dữ liệu bằng API trước khi chạy (đơn 5 trạng thái qua admin, tài khoản seed). Ghi kết quả theo lượt có timestamp vào HW03/checklist/runs/<P>_auto_<ts>.json (auto_status) + ảnh phần tử vào evidence/auto/. Item nào Firefox Playwright không làm được (vd throttling) → để manual cho P2.
3. HW03/checklist/RUN.md cho phần chạy tay, theo thứ tự màn hình (không theo số item): mỗi nền tảng 1 lượt, đầu lượt restart backend + dựng dữ liệu; P3 nhắc adb reverse 2 cổng + chrome://inspect để dán dom_probe.js; mỗi item ghi cần nhìn gì, ảnh nào bắt buộc (item Failed + 1 ảnh/màn/nền tảng cho Task 3, có overlay Sticky Notes "23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn", thấy tên trình duyệt + URL), tên ảnh P<n>_<id>_<k>.png. Kèm file trống HW03/checklist/runs/<P>_manual_TEMPLATE.md để tôi ghi kết quả.
4. Chỉ chạy `npx playwright test --list`; KHÔNG chạy lượt thật (tôi chạy). In lệnh tôi cần chạy cho P1, P2.
on_stop.py --manual. Báo cáo ≤ 12 dòng. Nhắc tôi push.
```

**Output:**
````
Đang dựng harness Playwright; đọc API đổi trạng thái đơn để dựng dữ liệu.

Còn chặn: máy không có Chrome/Firefox cài sẵn (chỉ Cốc Cốc) — ghi vào báo cáo, vẫn dựng harness. Viết cấu hình Playwright.

Giờ `lib.ts` (helper đo DOM, API dựng dữ liệu, oracle khoá sha1).

Viết `oracle.ts` (tham số đo theo từng item) — hash điền bằng script.

Viết spec (một test cho mỗi item auto/mixed).

PowerShell nuốt `${}` — sửa bằng Edit.

Gán `che_do` vào checklist.json + vá merge_platform cho file lượt `kind: auto`.

Generate oracle, npm install, `--list`.

Harness Playwright list OK (142 = 71×2). Giờ RUN.md + mẫu ghi kết quả + script dựng đơn cho lượt tay.

Đã dựng xong phần chạy tự động (Playwright cho P1/P2) và RUN.md cho phần chạy tay. Mới chạy `--list`, chưa chạy lượt thật. Có một chỗ chặn: máy chưa cài Google Chrome và Firefox, chỉ thấy Cốc Cốc.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** HW03[T1] 3/6 – Playwright P1/P2 + RUN.md. Không sửa `expected`; `check_checklist` 0 lỗi, 0 cảnh báo.
- **Phân loại `che_do` (74 item):**

  | Chế độ | Số item |
  |---|---|
  | auto | 59 |
  | mixed | 12 |
  | manual | 3 (CL-01, CL-52, CL-64) |

  - Firefox của Playwright không giả lập được mạng chậm và không cấp quyền clipboard, nên CL-53, CL-63, SV-02 chỉ chạy tự động trên P1; trên P2 chạy tay.
- **Playwright – `HW03/tests/`:**
  - Một test cho mỗi item auto/mixed: 71 test × 2 nền tảng = 142.
  - Ngưỡng đo nằm ở `oracle.src.json`; `oracle.ts` sinh từ đó, khoá bằng sha1 của `expected` như HW02. Hai ngưỡng màu không có số trong Expected (CL-04 xanh dương, CL-05 đỏ) em tự đặt theo dải hue và ghi lý do — bạn duyệt.
  - Dữ liệu: CL-62 chạy đầu khi tài khoản chưa có đơn; ngay sau đó dựng 7 đơn qua API (đủ 5 trạng thái + 2 đơn chờ để thử huỷ).
  - Kết quả mỗi lượt ghi vào `checklist/runs/<P>_auto_<ts>.json` (`auto_status`), ảnh vào `evidence/auto/`. `merge_platform.py` đã sửa để file lượt tự động chỉ ghi `auto_status`, không đụng `ket_qua`.
- **RUN.md** (sinh bằng `gen_run.py`): xếp theo màn hình — Bước A (CL-62) → dựng đơn → M1…M6 → cuối lượt (CL-52, CL-64).
  - Số item chạy tay: P1 15, P2 15, P3 70.
  - Có lệnh adb + `chrome://inspect` cho P3, quy tắc ảnh/overlay, cảnh báo khoá tài khoản.
  - Kèm `dom_probe.js`, `seed_orders.py` (dựng đơn, đặt lại mật khẩu) và 3 mẫu `runs/P{1,2,3}_manual_TEMPLATE.md`.
- **Bất thường:**
  - Backend: mỗi lần sai mật khẩu bộ đếm tăng 2 (`server.js:54`) và khoá 180 giây (`server.js:57`), trong khi SRS ghi tăng 1 và khoá 30 giây. Hệ quả: sai 2 lần là bị khoá; script tự đăng nhập đúng ngay sau mỗi lần sai để tránh.
  - Môi trường: không thấy Google Chrome và Firefox (đã tìm đường dẫn cài đặt, registry, Start Menu). Playwright mới có sẵn chromium-1140, chưa có bản Firefox.
- **Kết quả kiểm tra:** `npx playwright test --list` → 142 test, chưa chạy lượt thật.
- **Commit:** `07982fc HW03[T1] 3/6: Playwright P1/P2 + RUN.md` (gồm prompt log 13 lượt).
- **Cần quyết định:** C1 – P1 cần Google Chrome thật. (a) Bạn tự cài Chrome; (b) dùng `npx playwright install chrome` (cài Chrome chính thức, cần quyền admin). Firefox: cài bản thật cho lượt chạy tay P2, còn lượt tự động dùng `npx playwright install firefox`.

Lệnh chạy, mỗi nền tảng một lượt, restart backend trước mỗi lượt:

```powershell
cd HW03\tests
npx playwright install firefox          # một lần, bản build Firefox của Playwright
# P1: restart backend (CSDL seed) rồi:
npx playwright test --project=P1
python ..\..\.claude\skills\gui-checklist-testing\scripts\merge_platform.py ..\checklist\checklist.json (Get-ChildItem ..\checklist\runs\P1_auto_*.json | Sort LastWriteTime | Select -Last 1).FullName --platform P1 --dry-run
# P2: restart backend lần nữa rồi:
npx playwright test --project=P2
```

Bạn tự push (`git push`).
````
*File AI ghi/gửi trong lượt này:* `package.json`, `playwright.config.ts`, `global-setup.ts`, `lib.ts`, `oracle.src.json`, `gen_oracle.py`, `C2.spec.ts`, `reporter.ts`, `seed_orders.py`, `gen_run.py`

**Xử lý:** [...]

---

## #14 | 20:27 04/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Ghi nhớ những cái đang chạy. Tắt giúp mình để mình chạy về phòng. Rồi mình sẽ bảo bạn bật lại nhé
```

**Output:**
```
Em đã tắt hết, không còn tiến trình `node` hay `adb` nào chạy; bạn mang máy đi được.

Lúc tắt có:
- backend `:3000`;
- web vite `:5173`;
- adb server, với 2 cổng 5173 và 3000 đang nối sang POCO F5 (`da87b223`).

Em đã gỡ 2 cổng đó trước khi tắt adb.

Em đã ghi vào bộ nhớ danh sách này, cách bật lại, và việc HW03 đang chờ: bạn cài Chrome/Firefox (C1) rồi chạy Playwright cho P1/P2. Khi bạn nói "bật lại", em chạy lại backend và vite, rồi `adb devices` và 2 lệnh `adb reverse`. Lúc đó cắm cáp điện thoại và để USB debugging bật.

Backend khởi động lại sẽ seed lại CSDL, nên dữ liệu thử cũ sẽ mất (vốn không cần giữ). Mọi thay đổi đã commit (`07982fc`); nhớ `git push`.
```
*File AI ghi/gửi trong lượt này:* `hw03-runtime-state.md`

**Xử lý:** [...]

---

## #15 | 02:03 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
bật lại nhé
```

**Output:**
```
Bật lại xong, đủ như lúc tắt:
- **Backend** đang chạy ở `:3000`. CSDL vừa seed lại, nên đúng là trạng thái cần có trước lượt Playwright.
- **Web** đang chạy ở `127.0.0.1:5173`.
- **Điện thoại**: adb thấy `da87b223 device`, hai cổng `5173` và `3000` đã nối sang máy.

Việc tiếp theo bên bạn vẫn là C1: cài Chrome và Firefox, rồi chạy `npx playwright test --project=P1` trong `HW03\tests`. Restart backend trước mỗi lượt.
```

**Xử lý:** [...]

---

## #16 | 02:17 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – bật lại + chuẩn bị chạy (commit "HW03[T1] 3/6b: C1, H1, P3A"):
1. Bật lại backend + vite (--host 127.0.0.1) + adb devices + adb reverse 2 cổng.
2. C1: Chrome 157 đã cài lại ở C:\Program Files\Google\Chrome\Application\chrome.exe (dùng channel "chrome"); Firefox thật đã cài cho chạy tay P2; npx playwright install firefox cho lượt auto. Chạy --list lại. Ghi phiên bản Chrome/Firefox/Firefox-Playwright vào HW03/env/environment.md (không ghi đường dẫn có tên người dùng Windows).
3. H1: CL-04 hue 190–250, CL-05 hue 340–20, sat ≥ 0,3 — SV chốt ("nhìn thấy đúng xanh dương/đỏ là được"); ghi review_log + report_plan mục e.
4. report_plan mục f: "AI phát hiện khi đọc code: login_attempts +2 (server.js:54), khoá 180 s (server.js:57) ≠ FR-02 – chờ CL-52 chạy tay"; kiểm trùng issue FR-02 trong issues.json → in kết quả.
5. P3A (giới hạn 15 phút): thử Playwright _android với POCO (flag "Enable command line on non-rooted devices" đã bật); được → thêm project P3 chạy item auto, cập nhật RUN.md (P3 chỉ còn manual/mixed); không được → báo lỗi nguyên văn, giữ P3 chạy tay.
on_stop.py --manual. Báo cáo ≤ 10 dòng.
```

**Output:**
```
Đã có version. Giờ ghi environment.md, rồi H1, mục f, kiểm issue, thử P3A.

Ngưỡng H1 đã khớp oracle.src.json. Chỉ ghi review_log + report_plan.

Kiểm trùng FR-02: tải lại issue kèm body để quét đủ.

Trùng nhiều: #1, #2, #3 khớp đúng finding. Ghi vào file, rồi thử P3A.

Giờ thử P3A (Playwright `_android`, giới hạn 15 phút).

P3A chạy được. Xem config/fixture để thêm project P3.

P3A chạy được (kết nối 5,7 s). Thêm project P3 vào harness.

Giờ sửa lib.ts (fixture P3), global-setup, reporter, config.

Giờ gen_run.py: P3 chỉ còn manual/mixed.

213 test (71 × 3). Smoke 1 test đọc-only (CL-03) trên P3 để kiểm fixture, xong xoá file kết quả.

Fixture chạy được trên máy thật. Nhưng reporter ghi 0 item và lượt chạy mất 1,1 phút. Đang xem log đầy đủ.

P1 cũng ghi 0 item. Đây là lỗi có sẵn của reporter, không riêng P3. Đang debug.

Reporter đã sửa xong: nguyên nhân là `r.annotations` chưa có ở Playwright 1.48. Còn lỗi ảnh phần tử trên P3: chụp không ra file và không báo lỗi. Đang kiểm.

Script lẻ chạy nhanh, ảnh phần tử chụp được. Nghi do fixture `page` mặc định mở tab mới trên Android. Sửa để P3 dùng tab sẵn có.

Đã sửa: smoke P3 chạy 4 s, ảnh và reporter đều đúng. Kiểm thêm cổng N/A (CL-10 trên P3) rồi dọn file smoke.

Thêm 1 dòng log P3A rồi commit.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** 3/6b xong, commit `1172c20 HW03[T1] 3/6b: C1, H1, P3A`. Backend :3000 và vite :5173 đang chạy, CSDL sạch (test@eshop.com chưa có đơn). adb thấy `da87b223 device`, đã reverse 2 cổng.
- **C1:** `HW03/env/environment.md` có Chrome 157.0.8103.39, Firefox thật 159.0.1, Firefox của Playwright 131.0, Chrome Android 156.0.8078.79. `--list` ra 213 test (71 × P1/P2/P3).
- **H1:** ngưỡng trong `oracle.src.json` vốn đã đúng H1, không phải đổi. Đã ghi review_log và thêm dòng H1 vào report_plan mục e.
- **Mục f:** đã ghi. Kiểm 158 issue: lỗi đếm +2 và khoá 180 s **đã có #1, #2, #3**. Các issue FR-02 khác (#4–#9, #62–#64) liệt kê ở `HW03/checklist/issue_dup_FR02.md`.
- **P3A:** chạy được. Đã thêm project P3; P3 chạy tay giờ còn 13 item (RUN.md và template đã sinh lại). Item N/A theo NA1 tự bỏ qua, không ghi vào kết quả. Chrome trên máy bị đóng/mở lại và xoá storage của localhost:5173/3000 trước mỗi test.
- **Bất thường harness (đã sửa):**
  - `tests/reporter.ts:24` ghi 0 item trên cả P1 lẫn P2 vì Playwright 1.48 chưa có `TestResult.annotations`. Không sửa thì lượt auto chạy thật sẽ ra JSON rỗng.
  - P3: fixture page mặc định mở tab mới trên điện thoại, làm ảnh phần tử chụp hỏng mà không báo lỗi. Đã đổi sang dùng tab sẵn có.
- **Kiểm tra:** check_checklist 0 lỗi. Chạy thử CL-03 (chỉ đọc) trên P3 và P1 để kiểm fixture/reporter, đã xoá file kết quả và ảnh của lượt thử. Lượt thật: Not run (SV chạy).
- **Cần quyết định:** không. Bước kế tiếp của SV: restart backend rồi chạy `npx playwright test --project=P1`, lặp lại cho P2 và P3, sau đó push.
```

**Xử lý:** [...]

---

## #17 | 02:31 05/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
──
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #18 | 02:31 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – R1, R2 (commit "HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59"):
1. Chép HW02/bugs/_repro_C_FR15/7c/restart_backend.ps1 → tools/restart_backend.ps1 (giữ nguyên bản HW02). Tắt backend nền của phiên này.
2. HW03/tests/package.json thêm script: "p1"/"p2"/"p3" = restart_backend.ps1 rồi playwright test --project=Px (powershell -ExecutionPolicy Bypass -File ../../tools/restart_backend.ps1 && …).
3. RUN.md (sửa gen_run.py rồi sinh lại): bước restart = `powershell -ExecutionPolicy Bypass -File tools\restart_backend.ps1`; sau restart chạy seed_orders.py khi lượt cần đơn.
4. R2: tiền điều kiện CL-58, CL-59 trong checklist.json → "Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái" (expected không đổi); review_log ghi R2 "SV chốt".
5. Chạy thử restart_backend.ps1 một lần, in kết quả. on_stop.py --manual. Báo cáo ≤ 6 dòng.
```

**Output:**
```
Backend nền đã tắt. Giờ sửa package.json, gen_run.py, CL-58/59.

package.json và checklist.json đã ghi. gen_run.py sửa bằng Edit.

Chạy thử restart_backend.ps1.

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** R1 + R2 xong. Commit `9dfb111 HW03[T1] 3/6c: restart_backend dùng chung, sửa tiền điều kiện CL-58/59`.
- **R1:** `tools/restart_backend.ps1` chép nguyên bản từ HW02 (so `cmp`: giống hệt). Backend nền của phiên đã tắt. `HW03/tests/package.json` có `npm run p1`, `p2`, `p3` (restart rồi mới chạy `--project=Px`).
- **RUN.md:** sinh lại từ `gen_run.py`. Bước 1 dùng `restart_backend.ps1`. Bước B ghi rõ: chạy `seed_orders.py` ngay sau restart và Bước A, khi lượt đó cần đơn.
- **R2:** tiền điều kiện CL-58 và CL-59 giờ là "Sau restart backend, chạy seed_orders.py để có đủ đơn 5 trạng thái". Expected không đổi. review_log có R2 "SV chốt".
- **Kiểm tra:**
  - check_checklist: 0 lỗi.
  - Chạy thử `restart_backend.ps1`: in "backend restart xong: 5 sản phẩm", exit 0. Cổng 3000 đang listen (backend mới); vite :5173 vẫn chạy.
  - Đã chạy on_stop.py --manual: prompt log có 18 lượt.
- **Cần quyết định:** không. Lưu ý: backend giờ do script bật trong một cửa sổ riêng (thu nhỏ), không còn là tiến trình nền của phiên này.
```

**Xử lý:** [...]

---

## #19 | 02:49 05/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Lưu lại những gì đang chạy hiện tại, để lần sau mình yêu cầu bật lại thì mở lại hết như vậy nhé. Giờ tắt tất cả những gì đang chạy giúp mình
```

**Output:**
```
Đã ghi lại những gì đang chạy và tắt hết. Các cổng 3000, 5173, 5037 giờ không còn gì nghe, không còn tiến trình `node` hay `adb` nào.

Lúc tắt có 3 thứ chạy, lần sau bạn bảo "bật lại" mình sẽ mở lại đúng như vậy:
- **Backend `:3000`**: bật lại bằng `tools\restart_backend.ps1`. Mỗi lần bật, CSDL tự seed lại.
- **Web `:5173`**: vite chạy ở `127.0.0.1`.
- **adb**: điện thoại POCO `da87b223`, nối cổng `5173` và `3000` sang máy. Mình đã gỡ hai cổng này rồi tắt adb.

Admin `:5174` lúc đó không chạy nên sẽ không bật.

Khi bật lại, điện thoại cần cắm cáp và bật gỡ lỗi USB. Nếu adb báo `unauthorized`, mình sẽ dừng và báo bạn.

Việc tiếp theo bên bạn: chạy `npm run p1`, `npm run p2`, `npm run p3` trong `HW03/tests` (mỗi lệnh đã tự restart backend), rồi chạy tay theo RUN.md.
```
*File AI ghi/gửi trong lượt này:* `hw03-runtime-state.md`

**Xử lý:** [...]

---

## #20 | 22:31 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
mở lại nhé
```

**Output:**
```
Đã bật lại đủ như lúc tắt:
- **Backend** đang chạy ở `:3000` (bật bằng `restart_backend.ps1`), CSDL vừa seed lại.
- **Web** đang chạy ở `127.0.0.1:5173`.
- **Điện thoại**: adb thấy `da87b223 device`, hai cổng `5173` và `3000` đã nối sang máy.

Việc tiếp theo bên bạn: chạy `npm run p1`, `npm run p2`, `npm run p3` trong `HW03\tests` (mỗi lệnh tự restart backend), rồi chạy tay theo RUN.md.
```

**Xử lý:** [...]

---

## #21 | 22:34 09/11/2026 | Claude (không rõ model) | [...]
**Mục đích:** [...]

**Prompt:**
```
chạy npm run p1, npm run p2, npm run p3 trong HW03/tests (mỗi lệnh đã tự restart backend)
Để làm gì nhỉ
```

**Output:**
```
(không có output dạng văn bản)
```

**Xử lý:** [...]

---

## #22 | 23:30 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
khi chạy tay theo RUN.md có cần đọc thêm file khác không vậy?
```

**Output:**
```
Gần như không cần. RUN.md đã đủ thứ tự chạy, tiền điều kiện, ngưỡng Pass/Fail ("Cần nhìn" chép nguyên văn Expected), quy tắc chụp ảnh và lệnh cần chạy. Chỉ có 3 file đi kèm:

| File | Khi nào | Dùng để |
|---|---|---|
| `checklist/runs/Px_manual_TEMPLATE.md` | Đầu mỗi lượt | Chép thành `Px_manual_<YYYYMMDD-HHMM>.md`, ghi status, notes và tên ảnh từng item |
| `checklist/runs/Px_auto_*.json` | Item **mixed** | Cột "Cần nhìn" của item mixed ghi "Phần tự động: xem `runs/Px_auto_*.json`". Mở file, tìm mã item, đọc `notes` (số đo, chuỗi Tab, mã màu…) rồi bạn chấm phần còn lại bằng mắt. Vì vậy phải chạy `npm run px` **trước** lượt tay của nền tảng đó |
| `checklist/dom_probe.js` | Chỉ trên P3, khi cần đo DOM | Dán vào Console của `chrome://inspect`, chép JSON vào file kết quả. Giờ P3 đã có lượt auto nên ít khi cần |

Không cần đọc thêm:
- `checklist.md`/`checklist.json`: chỉ mở nếu muốn xem căn cứ SRS hoặc giả định của một item. Item N/A không có trong bảng RUN.md.
- `seed_orders.py`: chỉ chạy (Bước B) rồi chép bảng mã đơn mà nó in ra vào file kết quả.
- `issue_dup_FR02.md`: để dành cho bước viết bug (6/6), khi kiểm trùng issue.

Thứ tự mỗi nền tảng: `npm run px`, rồi mình gộp file auto, rồi bạn chạy tay theo RUN.md, ghi vào bản sao template.
```

**Xử lý:** [...]

---

## #23 | 23:31 09/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Màn hình này là sao: "Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ" là bao nhiêu màn hình
```

**Output:**
```
Chuỗi đó là **3 trang (URL) nhưng 4 màn hình cần xem**:

| # | Màn hình | URL | Nhận biết |
|---|---|---|---|
| 1 | Đăng nhập | `/login` | Form email + mật khẩu |
| 2 | Quên mật khẩu **B1** | `/forgot-password` | Ô "Nhập Email của bạn" + nút "Lấy mã OTP" |
| 3 | Quên mật khẩu **B2** | `/forgot-password` (cùng URL) | Bấm "Lấy mã OTP" xong thì hiện hộp xanh "Mã OTP của bạn là: …", ô OTP, ô mật khẩu mới, nút "← Quay lại" |
| 4 | Hồ sơ | `/profile` (phải đăng nhập) | Phần form hồ sơ. Lịch sử đơn cũng nằm ở trang này nhưng tính là màn M4 riêng |

B1 và B2 là hai bước trên cùng một trang, đổi bằng state (`setStep`), URL không đổi (`c2_inventory.md:38–53`).

Gặp item có màn hình như vậy, bạn kiểm cả 4 màn. Item **Failed** nếu **ít nhất 1 màn** vi phạm ngưỡng; notes ghi rõ màn nào, ví dụ "B2: …".

Ảnh tổng quan cho Task 3 vẫn theo M1–M5 (B1 và B2 chung M2), không phải mỗi item chụp riêng 4 màn.
```

**Xử lý:** [...]

---

## #24 | 00:53 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<task-notification>
<task-id>bnddydt0w</task-id>
<tool-use-id>toolu_019QpNyDpQYTeKpbzaPss5Pg</tool-use-id>
<output-file>C:\Users\tanhi\AppData\Local\Temp\claude\3d1ee2708df72d7d\e3928b55-32bd-47d5-a8e1-a4900f6a6dea\tasks\bnddydt0w.output</output-file>
<status>killed</status>
<summary>Background command "Start web frontend dev server" was stopped because the system is running low on memory</summary>
<note>This is not a failure of the command. Claude Code stopped it because the system was critically low on memory while the session was idle, which says nothing about the command or its own memory use, so there is nothing in it to debug. Do not start it again on your own, even if the work seems to need it: memory may still be short. Report what was stopped and why, and start it again only when asked. The user can turn this behavior off by starting Claude Code with CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1 in its environment; setting it from a shell command has no effect.</note>
</task-notification>
```

**Output:**
````
Web `:5173` (vite) vừa bị Claude Code tự dừng vì máy gần hết RAM lúc phiên đang rảnh. Không phải lỗi của vite. Mình chưa bật lại.

Backend `:3000` và adb (2 cổng) vẫn chạy: hai cái này không do phiên quản lý nên không bị dừng.

Cần web thì bảo mình bật lại, hoặc bạn tự chạy:

```powershell
cd ..\eshop-sut\frontend-web; npx vite --host 127.0.0.1 --port 5173
```

Bạn tự chạy trong cửa sổ riêng thì vite không bị Claude Code dừng theo kiểu này nữa. Trước lượt Playwright nên đóng bớt ứng dụng nặng.
````

**Xử lý:** [...]

---

## #25 | 02:00 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03 – 2 việc (mỗi việc 1 commit):
A. "HW03: deadline thật 11/11 10:00": report_plan + HW03/CLAUDE.md: deadline = 10:00 11/11/2026; lịch mục h theo bảng: T2 tối chạy tay; T3 ngày 4/6 + form; T3 tối pilot + 7 phiên; đêm T3–sáng T4 phân tích + report + zip.
B. "HW03[T2] 2/10: skill usability-evaluation": .claude/skills/usability-evaluation/ theo mẫu domain-bva-testing/gui-checklist-testing, mỗi lần gọi 1 bước rồi dừng:
  0 plan 9 phần (Rubin, slide) · 1 participant kit 1 trang (nhiệm vụ dạng mục tiêu, SEQ, SUS 10 câu tiếng Việt, 4 câu hỏi mở) + freeze · 2 pilot → sửa kit (diff + lý do SV) · 3 phiếu quan sát/phiên (sessions/S0x.json: thời gian, hoàn thành, lỗi, do dự, trích lời, SEQ, 10 câu SUS) · 4 scripts/sus_score.py (SUS chuẩn: lẻ −1, chẵn 5−x, ×2,5; trung bình, SD, min/max; SEQ; tỉ lệ hoàn thành; thời gian) → bảng giữa marker REPORT · 5 khung findings (SV viết: điểm đau, tách bug lẻ / vấn đề thiết kế, severity × probability) · 6 gom dữ kiện bug (SV viết mô tả).
  Giới hạn trong SKILL.md: AI không tạo danh sách người tham gia, ghi chú quan sát, câu trả lời SUS, phần tổng hợp/findings; không đưa dữ liệu cá nhân người tham gia cho AI (che 4 số giữa SĐT).
  Áp bước 0–1 cho HW03 bằng file đã có (usability/plan.md, participant_kit.md: chỉ kiểm khớp skill, không viết lại); thử sus_score.py trên 2 phiếu GIẢ trong thư mục tạm (không commit dữ liệu giả).
on_stop.py --manual. Báo cáo ≤ 10 dòng. Nhắc tôi push.
```

**Output:**
```
Task A trước: sửa deadline + lịch mục h.

Xong A (`99a64dc`). Sang B: đọc mẫu skill + file usability hiện có.

Slide khớp plan.md (9 phần, criticality = severity × probability, thống kê thời gian mean/median/range/SD). Viết skill.

Giờ assets.

Assets xong. Giờ viết scripts (sus_score trước, quan trọng nhất).

Còn 5 script nhỏ: freeze, check_kit, kit_diff, new_session, bug_facts.

Scripts xong. Áp bước 0–1 cho HW03 (chỉ kiểm) + thử sus_score trên 2 phiếu giả ở scratchpad.

Lỗi ở script (regex bắt nhầm "Lời mở đầu"), không phải kit. Sửa.

HW03 plan + kit: 0 lỗi, trùng bản đóng băng v1. Sửa placeholder template cho khỏi cảnh báo, rồi thử sus_score.

Số tay khớp: S01 = 82,5, S02 = 57,5, SD = 17,7. Lỗi nhỏ: dòng chú thích dính ngay sau bảng (GFM sẽ coi là hàng bảng). Sửa.

Skill chạy đúng. Ghi khai Audit, chạy on_stop, commit chỉ skill + prompt log (không đụng file chạy tay của SV).

### Báo cáo cho phiên thảo luận
- **Nhiệm vụ:** A + B xong, 2 commit: `99a64dc HW03: deadline thật 11/11 10:00` và `78c13d8 HW03[T2] 2/10: skill usability-evaluation`.
- **A:** đã sửa deadline thành 10:00 11/11/2026 ở `HW03/CLAUDE.md:8` và report_plan dòng 3. Mục h thay bằng bảng lịch 4 mốc (T2 tối → sáng T4).
- **B:** skill ở `.claude/skills/usability-evaluation/`, gồm SKILL.md (bước 0–6 và giới hạn AI), 2 reference, 3 asset, 6 script. `sus_score.py` báo lỗi thay vì điền thay khi phiếu thiếu SUS/SEQ, và từ chối phiếu có chuỗi số giống SĐT hoặc có email.
- **Áp bước 0–1 cho HW03:** `check_kit.py` trên plan.md + participant_kit.md ra 0 lỗi; hai file trùng bản đóng băng v1, không sửa.
- **Thử 2 phiếu giả (thư mục tạm, không commit):** SUS 82,5 và 57,5, khớp tính tay; SD 17,7; thời gian, hoàn thành, benchmark tính đúng; ghi bảng giữa marker được. kit_diff, bug_facts, new_session cũng chạy đúng.
- **Lỗi script, đã sửa:** check_kit bắt nhầm mục "Lời mở đầu"; sus_score để dòng chú thích dính vào bảng.
- **Kiểm tra:** check_kit 0 lỗi; sus_score đã chạy thử; on_stop.py --manual: prompt log 25 lượt. Không có lint/test tự động cho skill (Not run).
- **Cần quyết định:**
  - D1 – Report chưa có marker `<!-- REPORT:U1:usability_sessions/usability_summary:START/END -->`. Phương án: (a) AI chèn khung marker vào report, (b) SV tự chèn.
  - D2 – Có nhiều file chạy tay của bạn chưa commit: ảnh `evidence/P1–P3`, `runs/*_manual_*`, `runs/*_auto_*.json`, ảnh auto bị ghi đè, xoá 3 `.gitkeep`. Mình không động vào. Phương án: (a) bạn tự commit, (b) bảo mình commit cùng bước 4/6 gộp kết quả.
- **Nhắc push:** bạn tự push 2 commit mới (`99a64dc`, `78c13d8`); `7ba0785` cũng chưa push nếu bạn chưa push trước đó.
```
*File AI ghi/gửi trong lượt này:* `SKILL.md`, `plan-9-parts.md`, `schema-session.md`, `session_template.json`, `participant_kit_template.md`, `findings_template.md`, `sus_score.py`, `freeze.py`, `check_kit.py`, `kit_diff.py`, `new_session.py`, `bug_facts.py`

**Xử lý:** [...]

---

## #26 | 02:11 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 4/6 – kiểm + gộp. KHÔNG sửa chữ tôi viết trong runs/*_manual_*; chỉ liệt kê.
1. Kiểm (chỉ đọc) → HW03/checklist/run_check.md:
   a. Ảnh evidence/P1–P3 (xem từng ảnh): có overlay "23120255 · Lê Tấn Hiệp · email"; thấy tên trình duyệt/thiết bị + URL localhost; không lộ đường dẫn C:\Users\…, token, chrome://version; ảnh nhoè/cắt mất vùng lỗi. Đủ: mỗi item manual Failed ≥ 1 ảnh; mỗi màn × nền tảng 1 ảnh Task 3 (Z1: item auto Failed dùng ảnh phần tử).
   b. runs/*_manual_*: item nào chưa có kết quả; giá trị ngoài Passed/Failed/N/A; Failed thiếu Notes; N/A thiếu mã giả định; Notes mâu thuẫn với expected (vd ghi số liệu đạt ngưỡng mà chấm Failed).
   c. So auto ↔ manual cùng item/nền tảng: lệch → bảng để tôi quyết verdict.
   Dừng, báo cáo phần a–c nếu có lỗi chặn (thiếu kết quả/ảnh); không chặn thì làm tiếp.
2. Nén + đổi tên ảnh như HW02D (compress_manual.py; bản gốc → thư mục gitignore), tên P<n>_<id>_<k>.png. Commit "HW03[T1] 4/6a: SV chạy tay P1/P2/P3" (runs/, evidence/ đã nén, khôi phục .gitkeep nếu cần).
3. merge_platform.py: gộp auto + manual vào checklist.json (ket_qua theo nền tảng; item lệch để "CHỜ SV" trong bảng 1c, không tự chọn). build_excel.py → excel/23120255_HW03_Checklist.xlsx (recalc, 0 lỗi công thức). Danh sách Failed (item × nền tảng) + kiểm trùng issues.json (trùng → số issue; HW02 BUG-xx của tôi) → HW03/bugs/failed_list.md. Commit "HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed".
4. D1=a: chèn khung marker REPORT:U1 (sessions, summary) và REPORT:T1 (checklist summary, cross-platform) vào report; chạy script điền bảng T1.
on_stop.py --manual. Báo cáo ≤ 15 dòng: số item Passed/Failed/N/A theo nền tảng, số Failed mới (chưa có issue) / trùng, các điểm cần tôi quyết.
```

**Output:**
```
Bắt đầu bước 1: đọc file kết quả chạy tay.

Ảnh nhỏ sẵn (≤ 225 KB). Xem 1 ảnh mẫu để biết bố cục trước.

Đang xem ảnh: P1 + P2 xong (phát hiện nhãn M lệch, ảnh hoán đổi, lộ tài khoản đã lưu). Còn P3.

P3 không có overlay. Xem nốt các ảnh P3 còn lại để xác nhận.

Ảnh xem xong. Giờ so auto ↔ manual (1c).

Đủ dữ kiện. Có lỗi chặn (thiếu ảnh M5, 26 ảnh P3 không overlay, ảnh đặt nhầm tên) → ghi `run_check.md` rồi dừng theo lệnh.
```
*File AI ghi/gửi trong lượt này:* `run_check.md`

**Xử lý:** [...]

---

## #27 | 02:40 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 4/6 – xử lý run_check (chưa gộp):
1. Kiểm lại ảnh evidence/P1–P3 (xem từng ảnh, chỉ đọc): B1 – mọi ảnh P3 có overlay "23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn"; B5 – P1_SV-02-3/4 không còn lộ Gmail/tài khoản khác. Liệt kê ảnh còn lỗi cùng B2 (thiếu M5), B3 (nhãn ảnh sai), B4 (CL-52/CL-64 tráo; P3_CL-52_1 sai màn).
2. Ảnh đạt → nén + đổi tên P<n>_<id>_<k> như HW02D (bản gốc → evidence_raw/, thêm .gitignore). Ảnh còn lỗi hoặc còn lộ thông tin → để evidence_raw/, KHÔNG commit.
3. runs/*_manual_*: chỉ chuẩn hoá giá trị (Pass→Passed, Fail→Failed) và metadata theo R-list (tiêu đề file P2, Android 14); không sửa Notes.
4. report_plan mục e: Q1 – P1 chính thức = Cốc Cốc 160/Windows 11 (Chromium; SV không dùng Chrome), lượt auto P1 = Chrome 157 Playwright chỉ tham chiếu, ghi vào "lệch so với kế hoạch"; Q2=a – CL-64 Blocked bởi #111; V1 – lệch auto↔tay lấy trình duyệt thật, ghi nguyên nhân; overlay = "23120255 - Lê Tấn Hiệp - email" (P1/P2 Sticky Notes; P3 thêm chữ bằng trình sửa ảnh); B5 che bằng ô đen (khai AI-05). Sửa environment.md + gen_run.py theo P1 = Cốc Cốc.
5. Commit "HW03[T1] 4/6a1: SV chạy tay P1/P2/P3 – kết quả + ảnh đạt" (message ghi "AI chuẩn hoá giá trị/metadata, nén/đổi tên ảnh theo yêu cầu SV").
6. HW03/checklist/RUN_retake.md: chỉ những ảnh/item còn phải làm (liệt kê tên đích).
on_stop.py --manual. Báo cáo ≤ 8 dòng. Nhắc tôi push.
```

**Output:**
```
Ảnh P3 (trừ M1–M4) và P1_SV-02-3/4 vừa được sửa. Xem lại.

Kết quả kiểm lại: P3 CL/SV có overlay, nhưng 5 ảnh P3 M1–M4 vẫn chưa có. B5 đã che. B2/B3/B4 chưa sửa. Xem `compress_manual.py`.

Kiểm overlay còn đọc được sau nén.

Ảnh nén vẫn đọc rõ chữ. Bước 3: chuẩn hoá runs (chỉ cột status + metadata).

Bước 4: report_plan, environment.md, gen_run.py.

Bước 6: viết `RUN_retake.md`.
```
*File AI ghi/gửi trong lượt này:* `RUN_retake.md`

**Xử lý:** [...]

---

## #28 | 02:47 10/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW03[T1] 4/6b:
1. R-M5: dùng lại ảnh M3/M4 nếu thấy đủ navbar đã đăng nhập (tên, Đăng xuất, Giỏ hàng) → ghi tham chiếu trong RUN_retake/report, không chép file trùng; ảnh nào không đủ → báo. B3, B4 (phần tráo tên): đổi tên theo tên đích trong RUN_retake.md (SV đồng ý), nén, commit "HW03[T1] 4/6a2: sửa nhãn ảnh B3/B4, M5 dùng ảnh M3/M4".
2. merge_platform.py: gộp auto + manual vào checklist.json theo V1 (lệch → kết quả trình duyệt thật + ghi nguyên nhân lệch). build_excel.py → excel/23120255_HW03_Checklist.xlsx (recalc, 0 lỗi công thức). HW03/bugs/failed_list.md: Failed (item × nền tảng), kiểm trùng issues.json + HW02 BUG-xx của tôi → cột "issue trùng"/"MỚI".
3. D1=a: chèn khung marker REPORT:U1 (sessions, summary) và REPORT:T1 (checklist summary, cross-platform) vào report; điền bảng T1 từ checklist.json.
Commit "HW03[T1] 4/6b: gộp kết quả, Excel, danh sách Failed". on_stop.py --manual. Báo cáo ≤ 12 dòng: Passed/Failed/N/A/Blocked theo nền tảng; số Failed MỚI / trùng. Nhắc tôi push.
```

**Output:**
```
Step 1 first: check navbar in M3/M4 images.

Ảnh khớp. Cập nhật RUN_retake.md.

Step 2: merge. Read merge_platform.py.

Gộp kết quả: thấy đúng 8 chỗ lệch L1–L8 và auto Blocked CL-27/CL-48. Giờ viết script gộp.

Excel COM có sẵn → recalc + đếm lỗi công thức qua Excel.

Viết script PowerShell recalc có retry khi Excel báo bận.

Excel: 21 công thức, 0 lỗi, khớp JSON. Giờ làm failed_list — tìm issues.json và BUG HW02.

Step 3: report markers. Xem cấu trúc report.

Chèn marker vào report (giữ dòng 📝 của SV).

Phát hiện: P3 CL-30/CL-48 Failed do `TimeoutError` của harness, không phải do SUT. Rà toàn bộ ô auto Failed vì lỗi kỹ thuật.
```
*File AI ghi/gửi trong lượt này:* `RUN_retake.md`, `merge_hw03.py`, `recalc_xlsx.ps1`, `failed_list_hw03.py`, `report_t1_hw03.py`

**Xử lý:** [...]

---

**Tổng:** 28 lượt; Claude Opus 5.5 26 lượt (#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #18, #19, #20, #22, #23, #24, #25, #26, #27, #28); Claude (không rõ model) 2 lượt (#17, #21).
