# Đề xuất demo video – `gui-checklist-testing` (không nộp, export-ignore)

Mục tiêu: cho thấy skill dẫn AI **từng bước rồi dừng** (khảo sát → nháp 3 nguồn → freeze → check → chạy → gộp → Excel), trong ≤ 10 phút quay.

## Phạm vi đề xuất

- Màn: **Đăng ký** (`/register`, frontend-web :5173) – 1 màn form nhỏ, **ngoài phạm vi C2** (C2 bỏ Đăng ký vì đã kiểm domain ở HW02) nên không lẫn với kết quả T1 đã nộp.
- 1 nền tảng: P1 Chrome Windows, chạy tay. Không Playwright (tốn thời gian dựng project).
- `--min` hạ xuống (vd 8) cho demo; nói rõ trong video đây là demo, bài chính dùng ngưỡng > 40.
- Thư mục demo: `HW03/demo/register/` trên **nhánh tạm `demo-video`**. Freeze vào `HW03/demo/ai-outputs/` (KHÔNG vào `HW03/appendix/ai-outputs/`). Nhánh không merge vào main.

## Chuẩn bị (ngoài video)

```powershell
git switch -c demo-video
powershell -ExecutionPolicy Bypass -File tools\restart_backend.ps1
cd ..\eshop-sut\frontend-web; npx vite --host 127.0.0.1 --port 5173   # cửa sổ riêng
```

- SUT đang ở nhánh `usability-tunnel` (proxy `/api`, chạy local vẫn được). Không cần `tools\sut_main.ps1`; nếu chuyển về main thì nhớ chuyển lại trước phiên T2.
- Mở sẵn: terminal Claude Code, Chrome tab `http://127.0.0.1:5173/register`, VS Code thư mục `HW03/demo/`.

## Kịch bản (ước lượng thời gian)

| # | Bước skill | Lệnh / thao tác | ~phút |
|---|---|---|---|
| 1 | Giới thiệu | Mở `HW03/skills/gui-checklist-testing/SKILL.md`: quy tắc, 7 bước, "mỗi lần một bước rồi dừng" | 1 |
| 2 | Bước 0 – khảo sát | `/gui-checklist-testing HW03/demo/register 0` → xem `register_inventory.md` + `checklist.json` (meta) | 1.5 |
| 3 | Bước 1 – nháp 3 nguồn | `/gui-checklist-testing HW03/demo/register 1` (dặn: ~8–10 item, freeze ra `HW03/demo/ai-outputs`) → AI chạy `render_checklist.py`, `freeze.py --step 1 --out HW03/demo/ai-outputs --prefix demo_checklist`, `check_checklist.py --min 8` | 2.5 |
| 4 | Bước 2 – SV | Bỏ qua trên video (nói: bước 🔒 SV tự thêm item, AI không gợi ý); có thể thêm 1 item SV đã chuẩn bị sẵn | 0.5 |
| 5 | Bước 3 – RUN + dom_probe | `/gui-checklist-testing HW03/demo/register 3` → dán `dom_probe.js` vào DevTools Console trang register, xem JSON | 1.5 |
| 6 | Bước 4 – chạy + gộp | SV ghi nhanh `HW03/demo/register/runs/P1_manual_<ts>.csv` (`id,status,notes,evidence`) cho vài item → `python HW03/skills/gui-checklist-testing/scripts/merge_platform.py HW03/demo/register/checklist.json <csv> --platform P1` → `check_checklist.py` | 2 |
| 7 | Bước 5 – Excel | `python HW03/skills/gui-checklist-testing/scripts/build_excel.py HW03/demo/register/checklist.json -o HW03/demo/register/demo.xlsx` → mở Excel, 3 sheet | 1 |

Tổng ≈ 10 phút. Bước 6 (gom bug) chỉ nhắc bằng lời: AI không viết bug.

## Sau khi quay

```powershell
git switch main
# giữ hoặc xoá nhánh tạm: git branch -D demo-video  (SV quyết)
```

- Lượt Claude Code khi quay sẽ vào `.transcripts/` → prompt log HW03 sẽ có các lượt này; SV quyết khai (mục đích "demo skill") hoặc thêm `exclude` trong `tools/hw.toml`.
- Video: không lộ email/tài khoản đã lưu trong Chrome, username/hostname trong terminal nếu repo public.
