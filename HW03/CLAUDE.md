# HW03/CLAUDE.md — GUI & Usability on EShop (đang làm)

Phần chung (vai trò, khối báo cáo, giới hạn AI, prompt log, git, zip, SUT) ở `CLAUDE.md` gốc. File này chỉ giữ phần riêng HW03.

## 1. Đề và rubric

- Đề: `context/HW03_assignment.md` (pdftotext từ `2026.HW03.GUI Usability_En.pdf`). Slide: `context/private/S13_GUI Testing & Usability Testing.pdf`, `context/private/EN.GUI + Usability + Compatibility Testing AI-First (Combined).pdf`.
- Cấp độ AI **Cấp 4**, Bloom-AI **G9.3 + G9.4**. Deadline 07/11/2026 (giờ xem Moodle).
- Kế hoạch nộp, mâu thuẫn trong đề (M1–M11), quyết định, khai Audit/Disclosure: **`HW03/report_plan.md`** (không nộp – `export-ignore`).

| # | Mục | Điểm |
|---|---|---|
| 1 | Task 1 – GUI Checklist (thiết kế + chạy + bug) | 30 |
| 2 | Task 2 – Usability (kịch bản + 7 phiên + phân tích) | 40 |
| 3 | Task 3 – Cross-browser / cross-platform (≥ 3 nền tảng) | 20 |
| 4 | Agent Skills (+ video YouTube) | 10 |

Zip: `23120255_HW03_AI_GUIUsability_<ggg>.zip`. Biểu mẫu: AI-02 + AI-03 + AI-05 (.md + PDF) ở `HW03/ai-forms/`; AI-04 không cần; AI-06 đã nộp. Excel bắt buộc (`excel/23120255_HW03_Checklist.xlsx`, 3 sheet như HW01) và bảng tổng hợp chép sang report.

## 2. Phạm vi

- **T1 – checklist C2 – Tài khoản** (web :5173): Đăng nhập, Quên mật khẩu (2 bước), Hồ sơ + Lịch sử đơn/huỷ đơn, navbar khi đã đăng nhập. Không lấy Đăng ký (đã kiểm ở HW02). Khảo sát control: `HW03/checklist/c2_inventory.md`.
- **T2 – usability U1**: đăng nhập (tài khoản cho sẵn) → tìm SP → thêm giỏ → thanh toán có mã giảm giá (**VIP100**, K1) → xem đơn trong Hồ sơ. Moderated, trực tiếp trên PC của SV (P1). 1 pilot + 7 phiên. Thang SUS + SEQ.
- **T3**: chạy **toàn bộ** checklist trên mỗi nền tảng (M2). Kết quả: Passed / Failed / N/A (kèm giả định) / Blocked.
- IA-01…IA-04 của đề ↔ FR-21…FR-24 của SRS (M10); thêm phần UI của FR-02, FR-03, FR-04, FR-10, FR-11, SEC-04.

## 3. Nền tảng

| Mã | Nền tảng | Cách chạy |
|---|---|---|
| P1 | Chrome trên Windows | `http://localhost:5173` |
| P2 | Firefox trên Windows | `http://localhost:5173` |
| P3 | Chrome Android (POCO F5) | USB debugging + `adb reverse` (dưới) |

```powershell
# backend + web (nền)
cd ..\eshop-sut\backend; node server.js
cd ..\eshop-sut\frontend-web; npx vite --host 127.0.0.1 --port 5173
# P3: adb ở D:\Tools\platform-tools (platform-tools 37.0.1, không có trong PATH)
D:\Tools\platform-tools\adb.exe devices          # phải là "<serial>  device"; "unauthorized" → dừng, báo SV
D:\Tools\platform-tools\adb.exe reverse tcp:5173 tcp:5173
D:\Tools\platform-tools\adb.exe reverse tcp:3000 tcp:3000
D:\Tools\platform-tools\adb.exe reverse --list
```

Rút cáp / restart adb → chạy lại 2 lệnh `reverse`. DevTools trên P3: `chrome://inspect` trên PC.

Không dùng BrowserStack/LambdaTest (M11: trial quá ngắn). Overlay ảnh (O1): `23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn`; PC = Sticky Notes + chụp toàn màn hình (thấy tên trình duyệt + URL); điện thoại = thêm chữ bằng trình sửa ảnh ngay sau khi chụp.

## 4. Quyết định

Toàn bộ quyết định đã chốt ở **`HW03/report_plan.md` mục e** (S1, U, M2, M3, P1–P3, BS, R, E1, O1, T, K1). Quyết định mới ghi vào đó, không chép sang đây. Mục f (khai Audit) và g (Disclosure) ghi dần.

## 5. Giới hạn riêng HW03 (bổ sung mục 3 của `CLAUDE.md` gốc)

- **Item SV bổ sung 🔒** (T1 bước 2): AI không gợi ý item, không gợi ý khía cạnh (accessibility, RTL, dark mode…) trong lúc SV tìm. Hỏi "vì sao AI bỏ sót" chỉ sau khi SV đã commit item của mình.
- **Dữ liệu người tham gia 🔒**: AI không tạo, không điền, không sửa bảng 7 người (tên, Zalo/SĐT che 4 số giữa), không bịa tên/hồ sơ. Không đọc/không chép số điện thoại đầy đủ vào file nào. Ghi chú quan sát, thời gian, câu nói nguyên văn do SV ghi.
- **SUS/SEQ do người tham gia điền 🔒**: AI chỉ tính điểm từ câu trả lời SV nhập; không ước lượng, không điền thay câu trả lời thiếu.
- **Ảnh cross-platform có overlay 🔒**: AI không chụp/tạo/ghép ảnh overlay thay SV; chỉ đổi tên, nén, kiểm ảnh có đủ overlay + tên trình duyệt + URL.
- **Video phiên usability**: chứa giọng/màn hình người tham gia → không đăng công khai; AI không xử lý nội dung video.
- Kết quả checklist: SV quan sát và chấm; AI chỉ chạy `dom_probe.js` (đọc DOM, đo) và gộp kết quả. AI không chấm item chỉ quan sát được bằng mắt.
- Finding usability trùng bug đã biết (HW02 BUG-xx, issue nhóm như #124–#126 mã giảm giá) → ghi "đã biết – #xx", không tạo issue trùng.

## 6. Quy trình và mẫu commit

Skill: `gui-checklist-testing` (`.claude/skills/`), mỗi lần gọi một bước rồi dừng chờ SV review. Sau mỗi bước AI nháp: freeze vào `HW03/appendix/ai-outputs/` trước khi SV sửa.

**T1 – GUI checklist** (`HW03/checklist/checklist.json` là nguồn duy nhất; `.md` sinh từ JSON)

| Bước | Ai | Việc | Commit |
|---|---|---|---|
| 1 | AI → SV | Khảo sát + nháp checklist theo 3 nguồn (SRS, control, heuristic) + freeze | `HW03[T1] 1/6: AI nháp checklist C2` |
| 2 | **SV** 🔒 rồi hỏi AI | SV review, sửa, thêm item (`nguon: "SV"`); sau đó gap analysis | `HW03[T1] 2/6: SV bổ sung item + gap analysis` |
| 3 | AI → SV | `RUN.md` (thứ tự, tiền điều kiện, ảnh) + `dom_probe.js` | `HW03[T1] 3/6: RUN.md + dom_probe` |
| 4 | SV chạy, AI gộp | Chạy từng nền tảng (T3 bên dưới) → `merge_platform.py` | `HW03[T1] 4/6: Gộp kết quả P1–P3` |
| 5 | AI → SV | Excel + test summary (README, report) | `HW03[T1] 5/6: Excel + test summary` |
| 6 | **SV** 🔒 | Bug report `HW03/bugs/BUG-58…` + GitHub Issues có ảnh | `HW03[T1] 6/6: Bug report + GitHub Issues` |

**T3 – mỗi nền tảng một commit** (ảnh Failed + overlay ở `checklist/evidence/Px_*`):
`HW03[T3] P1: Chạy checklist trên Chrome Windows` · `HW03[T3] P2: … Firefox Windows` · `HW03[T3] P3: … Chrome Android`.

**T2 – usability U1** (`HW03/usability/`)

| Bước | Ai | Việc | Commit |
|---|---|---|---|
| 1 | AI → SV | Nháp plan 9 phần, participant kit, phiếu quan sát + freeze | `HW03[T2] 1/10: AI nháp gói usability` |
| 2 | **SV** | Pilot + chỉnh kịch bản/kit | `HW03[T2] 2/10: Pilot + chỉnh kịch bản` |
| 3–9 | **SV** 🔒 | Phiên S1…S7 (restart backend trước mỗi phiên); phiếu quan sát + SUS/SEQ | `HW03[T2] 3/10: Phiên S1` … `HW03[T2] 9/10: Phiên S7` |
| 10 | AI tính, **SV** phân tích 🔒 | Điểm SUS/SEQ, gom pain point, findings theo severity | `HW03[T2] 10/10: Phân tích + findings` |

Commit chung khác: `HW03: …` (harness, report, form, README, nộp). Bug kế tiếp: **BUG-58**; issue nhóm tiếp theo ≥ #204 (kiểm lại bằng `gh issue list` trước khi tạo).
