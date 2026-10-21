# Rà soát trước khi nộp HW02 (bản nháp)

> AI sinh ngày 21/10/2026 bằng skill `hw-submission-audit` (script `audit_hw.py`, chạy `python -I -X utf8`) + grep placeholder. Chỉ dữ kiện; chạy lại sau khi em điền xong.

## 1. Thiếu / cần làm

| Mục | Trạng thái | Ghi chú |
|---|---|---|
| Report .md + PDF | ĐÃ CÓ (PDF bản nháp) | xuất lại PDF sau khi điền xong (`node tools/md2pdf.js …`) |
| AI-02, AI-03, AI-05 .md + PDF | ĐÃ CÓ bản nháp, CHƯA KÝ | ô Ngày/Chữ ký `[...]`; AI-05 các mục cam kết em tự tick |
| AI-06 | Không có trong repo | em xác nhận đã nộp tuần 1 (report §14) |
| Commit log | ĐÃ CÓ `appendix/commit_log.txt` | xuất lại sau commit cuối |
| Agent Skill | ĐÃ CÓ `skills/domain-bva-testing/` | video: `skills/VideoLinks.md` còn `[...]` |
| Video demo (YouTube) | THIẾU | link ở `skills/VideoLinks.md`, README, report §7, §13 |
| Tên zip | chưa tạo | `23120255_HW02_AI_DomainTesting_<ggg>.zip`, ggg = tổng tự đánh giá |
| Prompt log | 398 lượt lúc kiểm; 2 lượt chưa có Mục đích/Xử lý (#138, #171) | trích lại lần cuối, rồi chạy lại `build_forms.py`, `audit_tables.py` để số lượt ở form/report khớp |

## 2. Dung lượng

- Không có file nào > 20 MB trong `HW02/` (trừ `tests/node_modules`, không vào zip).
- `git archive HEAD HW02`: xem báo cáo cho phiên thảo luận (đo ở bước 8).

## 3. Kết quả script `audit_hw.py` (rút gọn)

- HIGH `prompt log: Mã #138 xuất hiện 2 lần` — dòng thứ hai (`A_prompt_log.md`, khoảng dòng 10726) nằm trong khối output của một lượt (văn bản được trích lại), không phải tiêu đề lượt; script đếm cả dòng trong output.
- HIGH `report:2089 Có thể AI đã viết phần bị cấm` — dòng "Danh mục cấm (AI không làm)" ở §12, nội dung là liệt kê việc AI KHÔNG làm; script bắt theo từ khoá.
- MED: 65 dòng report còn placeholder/📝 (chi tiết mục 4); 2 lượt prompt log còn `[...]` ở Mục đích/Xử lý (#138, #171).
- LOW: 8 mục AI-05 chưa tick (đều là mục em tự xác nhận).
- Script không tìm thấy mục AI Critique vì tiêu đề có 🔒; đếm bằng `build_forms.py`: ≈ 287 từ (trong 200–300).
- Số liệu: report/AI-02/AI-03/AI-05 ghi 397 lượt, log lúc kiểm có 398 → trích lại lần cuối rồi sinh lại form.

## 4. Placeholder còn lại (file:dòng)

| File | Loại | Số dòng |
|---|---|---|
| `23120255_HW02_Report.md` | `<SV viết>` | 1 |
| `23120255_HW02_Report.md` | `[#n:` | 1 |
| `23120255_HW02_Report.md` | `[...]` | 11 |
| `23120255_HW02_Report.md` | `[chấm sau khi làm form]` | 1 |
| `23120255_HW02_Report.md` | `📝` | 54 |
| `README.md` | `[...]` | 1 |
| `ai-forms/AI-02_Audit_Report_23120255.md` | `[#n:` | 1 |
| `ai-forms/AI-02_Audit_Report_23120255.md` | `[...]` | 4 |
| `ai-forms/AI-02_Audit_Report_23120255.md` | `[chấm sau khi làm form]` | 1 |
| `ai-forms/AI-02_Audit_Report_23120255.md` | `📝` | 3 |
| `ai-forms/AI-03_Disclosure_Form_23120255.md` | `[...]` | 3 |
| `ai-forms/AI-03_Disclosure_Form_23120255.md` | `📝` | 2 |
| `ai-forms/AI-05_Privacy_Checklist_23120255.md` | `[...]` | 2 |
| `env/environment.md` | `[...]` | 7 |
| `report_plan.md` | `[...]` | 4 |
| `skills/VideoLinks.md` | `[...]` | 1 |

<details><summary>Chi tiết từng dòng</summary>

| File:dòng | Loại | Nội dung (trích) |
|---|---|---|
| `23120255_HW02_Report.md:3` | `📝` | > 📝 **Khung report.** Đề không quy định tên report chính → dùng `23120255_HW02_Report.md` theo CLAUDE.md §6 và |
| `23120255_HW02_Report.md:4` | `📝` | > 📝 Ký hiệu: `[...]` = ô cần điền · `<SV viết>` = em tự viết · 🔒 = em tự viết, AI không viết/nháp · bảng giữa  |
| `23120255_HW02_Report.md:4` | `[...]` | > 📝 Ký hiệu: `[...]` = ô cần điền · `<SV viết>` = em tự viết · 🔒 = em tự viết, AI không viết/nháp · bảng giữa  |
| `23120255_HW02_Report.md:4` | `<SV viết>` | > 📝 Ký hiệu: `[...]` = ô cần điền · `<SV viết>` = em tự viết · 🔒 = em tự viết, AI không viết/nháp · bảng giữa  |
| `23120255_HW02_Report.md:14` | `[...]` | \| Ngày nộp \| [...] \| |
| `23120255_HW02_Report.md:16` | `📝` | > 📝 AI nháp – SV xác nhận (câu tuyên bố phải khớp mục 12) |
| `23120255_HW02_Report.md:25` | `📝` | 6. Dựng khung report, sinh bảng dữ kiện, nháp các khối giải thích từng bước (đánh dấu 📝 AI nháp) và các mục ch |
| `23120255_HW02_Report.md:45` | `📝` | > 📝 Thứ tự mục 3–7 theo rubric đề §15 (A 25 · B 25 · C 25 · D 15 · Agent Skills 10). Mỗi feature có 7 mục con  |
| `23120255_HW02_Report.md:49` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong. Giá trị lấy từ `env/environment.md`, `env/mobile_api_url.pa |
| `23120255_HW02_Report.md:56` | `[...]` | \| Node.js \| [...] \| |
| `23120255_HW02_Report.md:67` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong. Nguồn duy nhất của mục này: `.claude/skills/domain-bva-test |
| `23120255_HW02_Report.md:136` | `📝` | > 📝 em quyết có ghi việc đổi căn cứ api_specification.md từ C (C9) ở đây hay không |
| `23120255_HW02_Report.md:156` | `📝` | > 📝 Bảng giữa các marker `<!-- REPORT:A_FR01:… -->` sinh bằng `python tools/report_tables.py HW02 A_FR01 --rep |
| `23120255_HW02_Report.md:227` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:251` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:318` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:350` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:519` | `📝` | > 📝 Dữ kiện: `A_FR01/sv_cases.md`, `A_FR01/ai_gap_answer.md`. |
| `23120255_HW02_Report.md:523` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:545` | `📝` | > 📝 Bảng "Kết quả thực thi" đầy đủ (Expected, Actual, Verdict, bằng chứng, bug) ở `A_FR01/testcases.md`. |
| `23120255_HW02_Report.md:572` | `📝` | > 📝 Dữ kiện: `bugs/_groups_A_FR01.md`, `bugs/BUG-xx.md`. |
| `23120255_HW02_Report.md:578` | `📝` | > 📝 Bảng giữa các marker `<!-- REPORT:B_FR07:… -->` sinh bằng `python tools/report_tables.py HW02 B_FR07 --rep |
| `23120255_HW02_Report.md:655` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:691` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:761` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:793` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:906` | `📝` | > 📝 Dữ kiện: `B_FR07/sv_cases.md`, `B_FR07/sv_questions.md`, `B_FR07/ai_gap_answer.md`. |
| `23120255_HW02_Report.md:910` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:933` | `📝` | > 📝 Bảng "Kết quả thực thi" đầy đủ ở `B_FR07/testcases.md`. |
| `23120255_HW02_Report.md:966` | `📝` | > 📝 Dữ kiện: `bugs/_groups_B_FR07.md`, `bugs/BUG-xx.md`. |
| `23120255_HW02_Report.md:972` | `📝` | > 📝 Bảng giữa các marker `<!-- REPORT:C_FR15:… -->` sinh bằng `python tools/report_tables.py HW02 C_FR15 --rep |
| `23120255_HW02_Report.md:1040` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1069` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1157` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1205` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1342` | `📝` | > 📝 Dữ kiện: `C_FR15/sv_cases.md`, `C_FR15/sv_questions.md`, `C_FR15/ai_gap_answer.md`. |
| `23120255_HW02_Report.md:1346` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1374` | `📝` | > 📝 Bảng "Kết quả thực thi" đầy đủ ở `C_FR15/testcases.md`. |
| `23120255_HW02_Report.md:1403` | `📝` | > 📝 Dữ kiện: `bugs/_groups_C_FR15.md`, `bugs/BUG-xx.md`, `bugs/_repro_C_FR15/`. |
| `23120255_HW02_Report.md:1409` | `📝` | > 📝 Bảng giữa các marker `<!-- REPORT:D_FR20:… -->` sinh bằng `python tools/report_tables.py HW02 D_FR20 --rep |
| `23120255_HW02_Report.md:1472` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1496` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1543` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1567` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1644` | `📝` | > 📝 Dữ kiện: `D_FR20/sv_cases.md`, `D_FR20/ai_gap_answer.md`, `D_FR20/compare_web_mobile.md`. |
| `23120255_HW02_Report.md:1648` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong |
| `23120255_HW02_Report.md:1670` | `📝` | > 📝 Bảng "Kết quả thực thi" đầy đủ ở `D_FR20/testcases.md`. Nhật ký ảnh (bắt buộc / khi khác Expected / ngoài  |
| `23120255_HW02_Report.md:1690` | `📝` | > 📝 Dữ kiện: `bugs/_groups_D_FR20.md`, `bugs/BUG-xx.md`. |
| `23120255_HW02_Report.md:1740` | `📝` | > 📝 Dữ kiện: [`D_FR20/compare_web_mobile.md`](D_FR20/compare_web_mobile.md), `D_FR20/RUN.md`. |
| `23120255_HW02_Report.md:1744` | `📝` | > 📝 AI nháp – SV duyệt/sửa, xoá dòng này khi xong. Nguồn: `.claude/skills/domain-bva-testing/SKILL.md`, `refer |
| `23120255_HW02_Report.md:1757` | `[...]` | \| Feature demo trong video \| [...] \| |
| `23120255_HW02_Report.md:1758` | `[...]` | \| Video YouTube \| [...] \| |
| `23120255_HW02_Report.md:1794` | `📝` | > 📝 Khối này trùng khối `SUMMARY` trong `README.md` (cùng lệnh `summary.py`). |
| `23120255_HW02_Report.md:1862` | `📝` | > 📝 Bug report đầy đủ: `bugs/BUG-xx.md`; thang đo: `bugs/README.md`. Ảnh trang Issues ở mục x.7 của từng featu |
| `23120255_HW02_Report.md:1866` | `📝` | > 📝 Bản đầy đủ: `ai-forms/AI-02_Audit_Report_23120255.md` / `.pdf`. Cột Verdict, Lý do và Kết luận em tự viết. |
| `23120255_HW02_Report.md:1912` | `[...]` | \| G5 \| Khung trống `sv_cases.md` (AI tạo khung, nội dung SV viết; commit chung với nội dung SV) \| (commit khôn |
| `23120255_HW02_Report.md:1928` | `[#n:` | \| F1 \| Biểu mẫu AI-02/03/05 (.md) \| — · [#n: form chưa làm] \| chưa làm \| — \| |
| `23120255_HW02_Report.md:1990` | `[chấm sau khi làm form]` | \| F1 \| Biểu mẫu AI-02/03/05 (.md) \| [chấm sau khi làm form] \| Các biểu mẫu khai báo minh bạch quá trình sử dụn |
| `23120255_HW02_Report.md:2070` | `[...]` | - Lượt AI chỉ rà soát, không tạo artifact: [...] |
| `23120255_HW02_Report.md:2080` | `📝` | > 📝 AI nháp – SV xác nhận. Dán nguyên văn giống nhau ở đây và trong AI-02. |
| `23120255_HW02_Report.md:2084` | `📝` | \| Phần AI tạo bản đầu \| Harness: `CLAUDE.md`, Agent Skill `domain-bva-testing` (SKILL.md, references, `freeze. |
| `23120255_HW02_Report.md:2085` | `📝` | \| Phần em xem xét và sửa \| Review từng bước 1–4 của mỗi feature và chốt giả định (commit `x/7b`, `x/7c`…, "SV  |
| `23120255_HW02_Report.md:2099` | `[...]` | \| 5 \| Agent Skills \| 10 \| 10 \| mục 7; `skills/domain-bva-testing/` (chép trước khi nộp); video: [...] \| |
| `23120255_HW02_Report.md:2102` | `📝` | > 📝 Phải khớp bảng trong `README.md` và số `ggg` trong tên zip. Cột "Căn cứ" là dữ kiện do script sinh từ `sum |
| `23120255_HW02_Report.md:2122` | `[...]` | \| AI-06 \| Nộp tuần 1: [...] (em xác nhận) \| |
| `23120255_HW02_Report.md:2124` | `📝` | > 📝 Thứ tự làm: AI-02 → AI-03 → AI-05. AI-03 có 1 câu giải thích các lượt 'Claude (không rõ model)' theo P3 (s |
| `23120255_HW02_Report.md:2130` | `[...]` | [`appendix/A_prompt_log.md`](appendix/A_prompt_log.md) — trích tự động; số lượt và dải mã: [...] (trích lại lầ |
| `23120255_HW02_Report.md:2138` | `[...]` | `appendix/commit_log.txt` — [...] (xuất bằng `tools/export_commit_log.ps1 HW02` sau commit cuối). |
| `README.md:34` | `[...]` | \| Agent Skill `domain-bva-testing` chạy end-to-end trên một feature \| [...] \| [...] \| |
| `skills/VideoLinks.md:5` | `[...]` | \| Agent Skill `domain-bva-testing` chạy end-to-end trên một feature (bước 1 → 7) \| [...] \| [...] \| |
| `ai-forms/AI-02_Audit_Report_23120255.md:28` | `📝` | 6. Dựng khung report, sinh bảng dữ kiện, nháp các khối giải thích từng bước (đánh dấu 📝 AI nháp) và các mục ch |
| `ai-forms/AI-02_Audit_Report_23120255.md:81` | `[...]` | \| G5 \| Khung trống `sv_cases.md` (AI tạo khung, nội dung SV viết; commit chung với nội dung SV) \| (commit khôn |
| `ai-forms/AI-02_Audit_Report_23120255.md:97` | `[#n:` | \| F1 \| Biểu mẫu AI-02/03/05 (.md) \| — · [#n: form chưa làm] \| chưa làm \| — \| |
| `ai-forms/AI-02_Audit_Report_23120255.md:158` | `[chấm sau khi làm form]` | \| F1 \| Biểu mẫu AI-02/03/05 (.md) \| [chấm sau khi làm form] \| Các biểu mẫu khai báo minh bạch quá trình sử dụn |
| `ai-forms/AI-02_Audit_Report_23120255.md:216` | `[...]` | - Lượt AI chỉ rà soát, không tạo artifact: [...] |
| `ai-forms/AI-02_Audit_Report_23120255.md:230` | `📝` | \| Phần AI tạo bản đầu \| Harness: `CLAUDE.md`, Agent Skill `domain-bva-testing` (SKILL.md, references, `freeze. |
| `ai-forms/AI-02_Audit_Report_23120255.md:231` | `📝` | \| Phần em xem xét và sửa \| Review từng bước 1–4 của mỗi feature và chốt giả định (commit `x/7b`, `x/7c`…, "SV  |
| `ai-forms/AI-02_Audit_Report_23120255.md:246` | `[...]` | \| Ngày: \| [...] \| |
| `ai-forms/AI-02_Audit_Report_23120255.md:247` | `[...]` | \| Chữ ký: \| [...] \| |
| `ai-forms/AI-03_Disclosure_Form_23120255.md:17` | `[...]` | \| Ngày: \| [...] \| |
| `ai-forms/AI-03_Disclosure_Form_23120255.md:136` | `📝` | Harness: `CLAUDE.md`, Agent Skill `domain-bva-testing` (SKILL.md, references, `freeze.py`, `check_domain.py`,  |
| `ai-forms/AI-03_Disclosure_Form_23120255.md:144` | `📝` | - Review từng bước 1–4 của mỗi feature và chốt giả định (commit `x/7b`, `x/7c`…, "SV chốt …"); sửa Expected/qu |
| `ai-forms/AI-03_Disclosure_Form_23120255.md:172` | `[...]` | \| Ngày: \| [...] \| |
| `ai-forms/AI-03_Disclosure_Form_23120255.md:173` | `[...]` | \| Chữ ký: \| [...] \| |
| `ai-forms/AI-05_Privacy_Checklist_23120255.md:49` | `[...]` | \| Ngày: \| [...] \| |
| `ai-forms/AI-05_Privacy_Checklist_23120255.md:50` | `[...]` | \| Chữ ký: \| [...] \| |
| `env/environment.md:6` | `[...]` | \| Máy \| [...] (OS, CPU/RAM) \| |
| `env/environment.md:7` | `[...]` | \| Node.js \| [...] (`node -v`) \| |
| `env/environment.md:8` | `[...]` | \| Trình duyệt \| [...] (tên + phiên bản) \| |
| `env/environment.md:10` | `[...]` | \| Điện thoại \| [...] (model, Android/iOS + phiên bản) \| |
| `env/environment.md:11` | `[...]` | \| Expo Go \| [...] (bản cho SDK 54) \| |
| `env/environment.md:12` | `[...]` | \| Thay đổi SUT \| `frontend-mobile/App.js` dòng 16 `API_URL` → IP LAN `[...]` (xem `mobile_api_url.patch`) \| |
| `env/environment.md:13` | `[...]` | \| Playwright \| [...] (`npx playwright --version`) \| |
| `report_plan.md:69` | `[...]` | \| 15 \| Prompt log \| đề §9; AI-01 \| `HW02/appendix/A_prompt_log.md` (363 lượt `## #`) \| **CẦN CẬP NHẬT**: `prom |
| `report_plan.md:72` | `[...]` | \| 18 \| Tự đánh giá \| đề §14, §15 \| `HW02/README.md` bảng "Tự đánh giá" \| **CẦN CẬP NHẬT** (ô `[...]`) \| |
| `report_plan.md:74` | `[...]` | \| 20 \| Video demo skill (YouTube link) \| đề §7, §14 \| `HW02/README.md` mục Video (`[...]`); `HW02/skills/Video |
| `report_plan.md:76` | `[...]` | \| 22 \| README.md \| đề §14 \| `HW02/README.md` \| ĐÃ CÓ – **CẦN CẬP NHẬT** (dòng "Công cụ AI: [...]", tên file re |

</details>
