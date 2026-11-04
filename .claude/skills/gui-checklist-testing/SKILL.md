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
9. **Kết quả do người chạy quan sát.** AI chỉ chạy `dom_probe.js` (đọc DOM, đo) và gộp. Item chỉ quan sát bằng mắt (màu, bố cục, cảm nhận) do SV chấm. Bug report do SV viết; AI chỉ gom dữ kiện.
10. Quy định khoá học / `CLAUDE.md` hạn chế AI → quy định đó thắng skill này.

## Các bước

Gọi: `/gui-checklist-testing <thư-mục-checklist> <bước>` — vd `HW03/checklist 1`. Thiếu số bước → đọc `checklist.json` (`meta.step`) để biết bước kế và hỏi lại.

### Bước 0 — Khảo sát
- Liệt kê control từng màn hình trong phạm vi (loại, nhãn, thuộc tính, file:dòng) và trích yêu cầu UI của đặc tả (mã + số dòng) vào `<dir>/<scope>_inventory.md`.
- Tạo `checklist.json` với `meta` (scope, sut_version, test_basis, platforms, result_values, inventory), `assumptions` rỗng, `items` rỗng. Dừng.

### Bước 1 — Nháp checklist theo 3 nguồn
- Sinh item từ: (a) **điều khoản đặc tả** (mỗi điều khoản áp dụng cho màn trong phạm vi), (b) **checklist theo control** (text box, button, link, validation… – chỉ control có trong inventory), (c) **heuristic** Nielsen 10 / Norman 6 / Shneiderman 8 / WCAG khi đặc tả im lặng. Ghi `loai_nguon` = `SRS` / `Control` / `Heuristic`.
- Mỗi item: `id` CL-xx, `ia` (IA-01…IA-04), `man_hinh`, `muc_kiem_tra`, `can_cu` (mã + dòng), `expected` có ngưỡng, `uu_tien` Mandatory/Optional, `nen_tang`, `nguon: "AI"`; tuỳ chọn `tien_dieu_kien`, `gia_dinh`, `na`.
- Đủ 4 IA; số item ≥ ngưỡng đề (vd > 40).
- `render_checklist.py` → `freeze.py --step 1` → `check_checklist.py`. Dừng.

### Bước 2 — SV bổ sung 🔒 + gap analysis
- SV sửa item AI (đổi `nguon` → `Both`), thêm item `nguon: "SV"` với `ly_do_ai_bo_sot` (SV viết). **AI không gợi ý.**
- AI chỉ được dựng khung trống `<dir>/sv_items.md` từ `assets/sv_items_template.md` (có đủ trường, gồm `loai_nguon`). Sau khi SV commit: AI kiểm cấu trúc (chỉ đọc), rồi chép nguyên văn vào JSON (id `SV-xx`); trường trống → "(SV chưa ghi)" và `check_checklist.py` báo lỗi cho tới khi SV điền.
- Sau khi SV commit, nếu SV hỏi: trả lời vì sao AI bỏ sót theo quy tắc 8; SV tự viết phần phân tích trong report.
- `render_checklist.py` + `check_checklist.py`. Dừng.

### Bước 3 — RUN.md + dom_probe.js
- `RUN.md` (mẫu `assets/RUN_template.md`): thứ tự nhóm item (gom theo tiền điều kiện để ít restart), lệnh khởi động SUT, tài khoản, bảng ảnh (chỉ chụp item Failed + overlay theo đề), cách ghi kết quả vào file lượt `runs/<Px>_<YYYYMMDD-HHMM>.csv`.
- `dom_probe.js` (từ `assets/dom_probe.js`): dán vào DevTools Console từng trang; in JSON số `<h1>`, `type` các ô, nhãn có `*`, `lang`, `title`, thứ tự focus, vị trí thông báo so với nút submit. Chỉ là dữ kiện cho SV chấm.
- Procedure phải khớp cách chạy thật trước khi chạy; sửa thì freeze lại, Expected không đổi. Dừng.

### Bước 4 — Chạy từng nền tảng + gộp
- SV chạy toàn bộ checklist trên từng nền tảng, ghi file lượt (CSV: `id,status,notes,evidence`). Mỗi nền tảng một commit.
- `merge_platform.py <json> <file-lượt> --platform Px` (thử `--dry-run` trước): ghi `ket_qua[Px]`, `notes_nt[Px]`, `evidence[Px]`; không ghi đè kết quả khác đã có trừ `--force`.
- `check_checklist.py`: mọi item Failed có notes + ảnh. Dừng.

### Bước 5 — Excel + test summary
- `build_excel.py <json> -o <xlsx>`: 3 sheet (Test Cases / Checklist / Test Summary Report) như mẫu HW01, có cột theo từng nền tảng, dropdown kết quả, công thức đếm.
- Bảng tổng (thiết kế / đã chạy / Passed / Failed / N/A / Blocked theo nền tảng; theo IA; theo nguồn) chép sang README + report. Dừng.

### Bước 6 — Gom dữ kiện bug
- Từ item Failed: gom nhóm theo nguyên nhân chung (một chỗ sửa), mỗi nhóm: item, nền tảng, notes nguyên văn, ảnh, code trích (file:dòng), yêu cầu bị vi phạm → `bugs/_groups_<scope>.md`. Kiểm trùng issue nhóm (`gh issue list`).
- **Không** viết mô tả bug. SV chốt danh sách, viết bug; AI chạy bước tái hiện SV viết, sửa dữ kiện theo evidence, tạo issue bằng `--body-file` của SV.

## Script

| Script | Việc |
|---|---|
| `scripts/check_checklist.py <json> [--min 41]` | Kiểm schema, id, 4 IA, 3 nguồn, N/A có giả định, mã giả định tồn tại, trùng mục, ngưỡng "Fail nếu", Failed có notes/ảnh. Mã thoát ≠ 0 khi có lỗi |
| `scripts/freeze.py <json> --step k --out <hw>/appendix/ai-outputs [--note "#n"]` | Đóng băng json + md, có timestamp, không ghi đè, ghi `INDEX.md` |
| `scripts/render_checklist.py <json> -o <md>` | Bảng theo IA, thống kê, giả định, cột kết quả từng nền tảng |
| `scripts/merge_platform.py <json> <lượt.csv\|json> --platform Px [--dry-run] [--force]` | Gộp kết quả một lượt chạy |
| `scripts/build_excel.py <json> -o <xlsx>` | Excel 3 sheet (cần `openpyxl`) |

## Quy ước verdict

- Lệch Expected → **Failed** (notes ghi Actual nguyên văn + lý do). Bị lỗi khác chặn (vd thiếu control mà item phụ thuộc) → **Blocked** + item gốc trong notes.
- Nền tảng không áp dụng (theo `na`) → **N/A**; N/A không có giả định = lỗi check.
- Expected sai phát hiện sau khi có Actual → không sửa Expected; ghi "Failed do lỗi thiết kế item, không lập bug".
- Lượt chính thức = chạy toàn bộ trên một nền tảng sau khi reset dữ liệu; ghi nhật ký trong `RUN.md`.
