# Kiểm `sv_items.md` (AI, chỉ đọc)

Bản kiểm: `sv_items.md` @ `823f7b9` (6 item SV-01…SV-06, 1 giả định GA4). AI chỉ liệt kê điểm cần xem; không đề xuất câu chữ, không sửa file của SV.

## 1. Trường thiếu / "(SV chưa ghi)"

Không có. Cả 6 item có đủ `ia`, `man_hinh`, `muc_kiem_tra`, `can_cu`, `expected` (có "Fail nếu …"), `nen_tang`, `uu_tien`, `luc_them`, `ly_do_AI_bo_sot.loai`, `ly_do_AI_bo_sot.giai_thich`.

## 2. `ia`, id

- `ia`: cả 6 thuộc IA-01…IA-04 (IA-01: SV-01, SV-04, SV-05 · IA-02: SV-02, SV-03 · IA-04: SV-06). Không có item IA-03.
- id: SV-01…SV-06, không trùng.

## 3. `can_cu`

- Không item nào trích điều khoản SRS `FR-xx (README.md:dòng)` → không có số dòng SRS cần đối chiếu.
- Tên slide được trích, đối chiếu với `context/private/EN.GUI + Usability + Compatibility Testing AI-First (Combined).pdf` (bản trích text):

| Item | Slide được trích | Có trong slide |
|---|---|---|
| SV-01 | "Checklist - Text Box & Button" | Có, nhưng là **2 slide riêng**: "Checklist — Text Box", "Checklist — Button" |
| SV-02 | "Checklist - Text Box" | Có |
| SV-03 | "Checklist - input-field validation" (Golden Rule) | Có — "G O L D E N R U L E On error, return focus to the offending field…" |
| SV-04 | "Accessibility & colour-blindness checks" | Có |
| SV-05 | "Why GUI testing is hard - Unsolicited events / Window management" | Có |
| SV-06 | "Double-submit on double-click" | Có |

- WCAG 2.2 SC 2.4.7, SC 1.4.3, Nielsen #5/#7, Norman Visibility, Shneiderman #5/#8: tên chuẩn/heuristic, không cần số dòng.

## 4. `nen_tang` / N/A

- SV-01: P3 N/A theo NA1 — NA1 nói về phím Tab; item điều hướng bằng Tab → mã giả định có tồn tại (`checklist.json` assumptions).
- SV-05: chỉ P3; **P1, P2 không ghi mã giả định N/A** (quy tắc đầu file: "Nền tảng nào N/A thì ghi kèm mã giả định"). GA4 nói về phạm vi P3, không nêu lý do P1/P2 N/A.
- Các item còn lại: P1, P2, P3.

## 5. Trùng / gần trùng với CL-01…CL-68 (bản `9463442`)

| Item SV | CL liên quan | Mức |
|---|---|---|
| SV-06 (chống gửi trùng khi bấm nhanh, 3 form, mạng thường) | CL-53 (chỉ báo đang xử lý + chống gửi trùng, chỉ Đăng nhập, Slow 3G, "bấm thêm 2 lần chỉ phát sinh 1 request") | Trùng một phần: cùng điểm quan sát "chỉ 1 request"; khác điều kiện mạng và số form |
| SV-01 (focus nhìn thấy được) | CL-10/11/12 (thứ tự Tab), CL-38 (bấm nhãn → focus) | Liên quan, không trùng: CL không kiểm việc focus có hiển thị |
| SV-05 (bàn phím ảo che form) | CL-15 (bố cục không vỡ ở màn hẹp) | Liên quan, không trùng: CL-15 không có điều kiện bàn phím ảo |
| SV-02, SV-03, SV-04 | — | Không thấy CL tương ứng |

## 6. Khác

- `luc_them`: SV-01, SV-06 "trong lúc chạy P1"; SV-02, SV-05 "trong lúc chạy P3"; SV-04 "trong lúc chạy P2". Tại thời điểm kiểm, repo **chưa có file lượt chạy nào** (`HW03/checklist/runs/` không tồn tại, `checklist.json` chưa có `ket_qua`).
- `ly_do_AI_bo_sot.loai` của SV-03 ghi "chất lượng input prompt" — đầu file liệt kê giá trị "prompt (chất lượng input của em)".
- Item SV chưa nằm trong `checklist.json` (chưa có `nguon: "SV"`) → chưa được `check_checklist.py` kiểm và chưa vào `checklist.md`.
