---
name: gui-checklist-testing
description: Thiết kế và chạy checklist GUI theo bài giảng GUI & Usability (3 nguồn – điều khoản đặc tả UI, checklist theo control, heuristic Nielsen/Norman/Shneiderman), mỗi item có ngưỡng Pass/Fail quan sát được, chạy trên nhiều trình duyệt/nền tảng, gộp kết quả, xuất Excel + test summary và gom dữ kiện bug. Mỗi lần gọi một bước rồi dừng. Dùng khi người dùng nói "GUI checklist", "checklist giao diện", "kiểm thử giao diện", "cross-browser", "cross-platform", "IA-01…IA-04", hoặc gọi /gui-checklist-testing kèm thư mục checklist và số bước.
---

# GUI checklist theo từng bước

Skill dẫn AI qua kỹ thuật **checklist testing** của bài giảng (*Where checklists come from 1–3*, *From heuristics to a review checklist*, *Test every control*), **mỗi lần gọi làm một bước rồi dừng** để người dùng review và commit. Không gộp cả kỹ thuật vào một lượt: đề chấm việc dẫn AI qua từng bước, và người review cần thấy từng quyết định.

Dữ liệu của một phạm vi (một nhóm màn hình) nằm trong **một file** `checklist.json` (schema: `references/schema-checklist.md`). Bảng Markdown, Excel, test summary đều sinh từ file này.

## Quy tắc bắt buộc

1. **Đọc test basis thật trước khi viết:** đoạn đặc tả UI (vd SRS FR-21…24 + phần UI của các FR liên quan), mã UI (nhãn, `type`, `required`, thông báo thật, file:dòng). Không bịa control, nhãn, route.
2. **Đặc tả là oracle; mã chỉ để biết control nào tồn tại.** Expected lấy từ đặc tả hoặc heuristic/checklist bài giảng, **không** lấy từ hành vi hiện tại của mã. Không chạy SUT để chỉnh Expected theo cái quan sát được. Chỗ đặc tả im lặng → giả định trong `assumptions` (mã `GAx`), item ghi mã đó trong `gia_dinh`.
3. **Expected quan sát được, có ngưỡng:** nêu thao tác/điểm quan sát (DevTools, mắt thường, đo px/giây) và câu "Fail nếu …".
4. **Không trùng:** mỗi thuộc tính chung (vd màu nút, ký hiệu tiền) khẳng định ở **một** item; item khác không lặp lại.
5. **N/A phải có giả định:** nền tảng không áp dụng → bỏ khỏi `nen_tang` và ghi lý do trong `na` (mã `NAx` trong `assumptions`).
6. **Đóng băng output AI** sau mỗi bước AI (`scripts/freeze.py`) trước khi người dùng sửa; không sửa file đã đóng băng.
7. **Nguồn từng item:** `nguon` = `AI` / `SV` / `Both` (AI đề xuất, SV sửa đáng kể).
8. **Bước 2 (SV bổ sung) – AI không gợi ý** item hay khía cạnh nào. Chỉ trả lời "vì sao AI bỏ sót" sau khi SV đã commit item của mình; tách *đã nghĩ tới nhưng không đưa vào* / *không nghĩ tới* / *bị gỡ theo quyết định SV*; nêu nguyên nhân (prompt, giới hạn công cụ, đặc thù giao diện).
9. **Verdict chính thức = lượt chạy tay trên trình duyệt/thiết bị thật.** Lượt Playwright (chế độ auto, bước 3–4) chỉ ghi `auto_status`; item không có trong lượt tay thì lấy kết quả auto (ghi `nguon_kq = auto` + môi trường auto). Lệch auto ↔ tay → lấy lượt tay, ghi nguyên nhân lệch (V1). Ô auto Failed vì lỗi harness (Timeout, không assertion nào fail) → người dùng quyết **Blocked**, không lập bug. AI chỉ chạy test/`dom_probe.js` (đọc DOM, đo) và gộp; item chỉ quan sát bằng mắt (màu, bố cục, cảm nhận) do SV chấm. Bug report do SV viết; AI chỉ gom dữ kiện.
10. Quy định khoá học / `CLAUDE.md` hạn chế AI → quy định đó thắng skill này.

## Các bước

Gọi: `/gui-checklist-testing <thư-mục-checklist> <bước>` — vd `HW03/checklist 1`. Thiếu số bước → đọc `checklist.json` (`meta.step`) để biết bước kế và hỏi lại.

### Bước 0 — Khảo sát
- Liệt kê control từng màn hình trong phạm vi (loại, nhãn, thuộc tính, file:dòng) và trích yêu cầu UI của đặc tả (mã + số dòng) vào `<dir>/<scope>_inventory.md`.
- Tạo `checklist.json` với `meta` (scope, sut_version, test_basis, platforms, result_values, inventory), `assumptions` rỗng, `items` rỗng. Dừng.

### Bước 1 — Nháp checklist theo 3 nguồn
- **Đọc toàn bộ phần nguồn checklist trong slide** (*Where checklists come from 1–3*, *From heuristics to a review checklist*, *Test every control*, các slide checklist theo control) **trước khi sinh item**; không sinh từ trí nhớ về heuristic.
- Sinh item từ: (a) **điều khoản đặc tả** (mỗi điều khoản áp dụng cho màn trong phạm vi), (b) **checklist theo control** (text box, button, link, validation… – chỉ control có trong inventory), (c) **heuristic** Nielsen 10 / Norman 6 / Shneiderman 8 / WCAG khi đặc tả im lặng. Ghi `loai_nguon` = `SRS` / `Control` / `Heuristic`.
- Mỗi item: `id` CL-xx, `ia` (IA-01…IA-04), `man_hinh`, `muc_kiem_tra`, `can_cu` (mã + dòng), `expected` có ngưỡng, `uu_tien` Mandatory/Optional, `nen_tang`, `nguon: "AI"`; tuỳ chọn `tien_dieu_kien`, `gia_dinh`, `na`.
- Đủ 4 IA; số item ≥ ngưỡng đề (vd > 40).
- `render_checklist.py` → `freeze.py --step 1` → `check_checklist.py`. Dừng.

### Bước 2 — SV bổ sung 🔒 + gap analysis
- SV sửa item AI (đổi `nguon` → `Both`), thêm item `nguon: "SV"` với `ly_do_ai_bo_sot` (SV viết). **AI không gợi ý.**
- AI chỉ được dựng khung trống `<dir>/sv_items.md` từ `assets/sv_items_template.md` (có đủ trường, gồm `loai_nguon`). Sau khi SV commit: AI kiểm cấu trúc (chỉ đọc), rồi chép nguyên văn vào JSON (id `SV-xx`); trường trống → "(SV chưa ghi)" và `check_checklist.py` báo lỗi cho tới khi SV điền.
- Sau khi SV commit, nếu SV hỏi: trả lời vì sao AI bỏ sót theo quy tắc 8; SV tự viết phần phân tích trong report.
- `render_checklist.py` + `check_checklist.py`. Dừng.

### Bước 3 — RUN.md + dom_probe.js (+ chế độ Playwright)
- **Phân loại cách chạy từng item** (`che_do`): `auto` (kiểm được hoàn toàn qua DOM/bàn phím/mạng – Playwright), `manual` (cần mắt người: màu, bố cục, cảm nhận, autofill…), `mixed` (một phần auto, phần còn lại tay – mô tả phần tay trong `che_do_ghi_chu`); nền tảng chạy auto được ghi `auto_nen_tang` nếu không phải mọi nền tảng.
- **Chế độ Playwright** (tuỳ chọn, khi có nhiều item `auto`): mỗi test đọc ngưỡng/đầu vào từ oracle **khoá theo `sha1(expected)[0:8]`** – `oracle.src.json` → `gen_oracle.py` → `oracle.ts`; Expected đổi thì test dừng với "oracle cũ" thay vì chạy theo bản cũ (không sinh lại oracle chỉ để hết lỗi). Mỗi project = một nền tảng (vd Chrome channel, Firefox của Playwright, Chrome Android thật qua `_android`); reporter ghi file lượt JSON `kind: "auto"` + ảnh phần tử vào `evidence/auto/`. Ví dụ: `HW03/tests/` (`C2.spec.ts`, `lib.ts`, `gen_oracle.py`, `gen_run.py`) – **chỉ có ở repo ví dụ (bài HW03), không kèm trong `scripts/` của skill** vì gắn cứng đường dẫn, màn hình, overlay của bài đó; bài khác viết lại theo cùng cách (oracle khoá sha1, sinh RUN.md từ `checklist.json`). Locale/viewport giả lập của Playwright có thể khác trình duyệt thật → ghi vào RUN.md để giải thích lệch ở bước 4.
- `RUN.md` (mẫu `assets/RUN_template.md`; chế độ Playwright: sinh bằng script kiểu `gen_run.py` (chỉ có ở repo ví dụ), chỉ còn item `manual`/`mixed`): thứ tự nhóm item (gom theo tiền điều kiện để ít restart), lệnh khởi động SUT, tài khoản, quy tắc ảnh (dưới), cách ghi kết quả vào file lượt `runs/<Px>_manual_<YYYYMMDD-HHMM>.md|.csv`.
- **Quy tắc ảnh:** (a) mỗi item **Failed** trên mỗi nền tảng: `P<n>_<id>_<k>.png`; (b) cross-platform: **1 ảnh tổng quan mỗi màn hình / nền tảng** `P<n>_M<k>_1.png` (ảnh màn khác thấy đủ vùng đó thì dùng lại, ghi tham chiếu, không chép trùng); không chụp item Passed/N/A. **Overlay theo đề** trên mọi ảnh (thấy tên trình duyệt + URL); AI không tạo/ghép overlay, chỉ kiểm, đổi tên, nén (bản gốc để thư mục `evidence_raw/` gitignore).
- `dom_probe.js` (từ `assets/dom_probe.js`): dán vào DevTools Console từng trang; in JSON số `<h1>`, `type` các ô, nhãn có `*`, `lang`, `title`, thứ tự focus, vị trí thông báo so với nút submit. Chỉ là dữ kiện cho SV chấm.
- Procedure phải khớp cách chạy thật trước khi chạy; sửa thì freeze lại, Expected không đổi. Dừng.

### Bước 4 — Chạy từng nền tảng + gộp
- Chế độ Playwright: chạy lượt auto từng nền tảng trước (restart/seed dữ liệu trong lệnh) → file `runs/<Px>_auto_<ts>.json` → `auto_status`.
- SV chạy tay phần còn lại trên trình duyệt/thiết bị thật, ghi file lượt (bảng Markdown `| ID | status | notes | ảnh |` hoặc CSV `id,status,notes,evidence`). Mỗi nền tảng một commit. AI kiểm ảnh/kết quả (chỉ đọc, ghi `run_check.md`), chỉ chuẩn hoá giá trị (Pass→Passed…) khi người dùng yêu cầu, không sửa notes.
- Gộp: `merge_runs.py --config <cfg>` (một lệnh cho mọi lượt; gọi `merge_platform.py` bên trong): lượt auto → `auto_status`; lượt tay → `ket_qua`; item chỉ có auto → `ket_qua` = auto (`nguon_kq`); lệch auto ↔ tay → giữ tay + `lech_auto_tay` (nguyên nhân trong `cause`); quyết định người dùng (lỗi harness → Blocked, loại khỏi lập bug `lap_bug: false`, nối câu vào notes) trong `override`, áp sau cùng nên chạy lại vẫn giữ. Gộp một lượt lẻ: `merge_platform.py <json> <file-lượt> --platform Px [--dry-run]`.
- `check_checklist.py`: mọi item Failed có notes + ảnh. Dừng.

### Bước 5 — Excel + test summary
- `build_excel.py <json> -o <xlsx>`: 3 sheet (Test Cases / Checklist / Test Summary Report) như mẫu HW01, có cột theo từng nền tảng, dropdown kết quả, công thức đếm.
- Bảng tổng (thiết kế / đã chạy / Passed / Failed / N/A / Blocked theo nền tảng; theo IA; theo nguồn) chép sang README + report. Dừng.

### Bước 6 — Gom dữ kiện bug
- `gh issue list --state all --limit 500 --json number,title,state,labels,author > bugs/issues.json`; `failed_list.py --config <cfg>` → `bugs/failed_list.md` (item × nền tảng Failed, cột trùng/MỚI; AI đối chiếu theo tiêu đề issue + màn + notes, người dùng xác nhận).
- `bug_groups.py --config <cfg> [--skeleton]`: gom item MỚI theo **dữ kiện quan sát giống nhau** (cùng phần tử / cùng hành vi, khác màn/nền tảng) → `bugs/bug_groups.md`; người dùng tách/gộp, chốt; rồi `--skeleton` sinh khung `BUG-<n>.md` (số nối tiếp bug cũ) **chỉ chứa dữ kiện chép lại** (item, nền tảng, môi trường, nguồn bước nguyên văn, Expected, Actual, ảnh); Tiêu đề / Mô tả / Steps / Severity / Priority để trống.
- **Không** viết mô tả bug. SV chốt danh sách, viết bug; AI chạy bước tái hiện SV viết, sửa dữ kiện theo evidence, tạo issue bằng `--body-file` của SV.

## Script

| Script | Việc |
|---|---|
| `scripts/check_checklist.py <json> [--min 41]` | Kiểm schema, id, 4 IA, 3 nguồn, N/A có giả định, mã giả định tồn tại, trùng mục, ngưỡng "Fail nếu", Failed có notes/ảnh. Mã thoát ≠ 0 khi có lỗi |
| `scripts/freeze.py <json> --step k --out <hw>/appendix/ai-outputs [--note "#n"]` | Đóng băng json + md, có timestamp, không ghi đè, ghi `INDEX.md` |
| `scripts/render_checklist.py <json> -o <md>` | Bảng theo IA, thống kê, giả định, cột kết quả từng nền tảng |
| `scripts/merge_platform.py <json> <lượt.csv\|json> --platform Px [--dry-run] [--force]` | Gộp kết quả một lượt chạy |
| `scripts/build_excel.py <json> -o <xlsx> [--tester …]` | Excel 3 sheet (cần `openpyxl`; đặt fullCalcOnLoad – mở Excel là tính lại) |
| `scripts/merge_runs.py --config <cfg> [--dry-run]` | Gộp mọi lượt auto + tay theo V1 (md → CSV, ánh xạ tên ảnh, `nguon_kq`, `lech_auto_tay`, `override`) |
| `scripts/failed_list.py --config <cfg>` | `failed_list.md`: Failed × nền tảng, đối chiếu trùng issue, loại `lap_bug: false`, cảnh báo lỗi harness |
| `scripts/bug_groups.py --config <cfg> [--skeleton]` | `bug_groups.md` + khung `BUG-<n>.md` chỉ dữ kiện; dừng nếu nhóm không phủ đúng tập item MỚI |

`merge_runs.py`, `failed_list.py`, `bug_groups.py` nhận config JSON (khoá mô tả trong docstring) hoặc được import và gọi `run(cfg)` từ wrapper của bài – ví dụ `tools/merge_hw03.py`, `tools/failed_list_hw03.py`, `tools/bug_groups_hw03.py` chỉ giữ dữ liệu riêng HW03 (tên file lượt, nguyên nhân lệch, quyết định, bảng trùng, nhóm).

## Quy ước verdict

- Lệch Expected → **Failed** (notes ghi Actual nguyên văn + lý do). Bị lỗi khác chặn (vd thiếu control mà item phụ thuộc) → **Blocked** + item gốc trong notes.
- Lượt auto lỗi harness (Timeout, không assertion fail) → người dùng quyết **Blocked**, ghi lý do, không lập bug. Kết quả chỉ có trên trình duyệt của Playwright, chưa xác nhận trên trình duyệt thật → giữ, ghi rõ, loại khỏi lập bug (`lap_bug: false`).
- Nền tảng không áp dụng (theo `na`) → **N/A**; N/A không có giả định = lỗi check.
- Expected sai phát hiện sau khi có Actual → không sửa Expected; ghi "Failed do lỗi thiết kế item, không lập bug".
- Lượt chính thức = chạy toàn bộ trên một nền tảng sau khi reset dữ liệu; ghi nhật ký trong `RUN.md`.
