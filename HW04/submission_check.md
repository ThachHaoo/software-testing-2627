# HW04 – rà soát trước khi nộp (skill hw-submission-audit, 18/11/2026 ~09:00)

Kiểm trên bản `git archive HEAD HW04` (HEAD `f9a7d67`). Không nộp file này (`export-ignore`).

| Mức | File / vị trí | Hiện tại | Sửa thành |
|---|---|---|---|
| HIGH | zip | `git archive HEAD HW04` = **54,1 MB** (1307 file; 23 lượt thử ≈ 37 MB nén) | Áp Z2 (23 lượt thử `export-ignore` trong `HW04/.gitattributes`) → **16,4 MB** (đo thử, chưa áp); hoặc split-and-zip. SV chốt |
| HIGH | tên zip | chưa tạo | `23120255_HW04_AI_Automation_093.zip` (tổng tự đánh giá report §11 = 93) |
| MED | `appendix/A_prompt_log.md` | 86/86 lượt còn `[...]` ở Mục đích/Xử lý | SV ghi Section/Mục đích/Xử lý trong `prompt_log_notes.toml` rồi `python tools/hooks/on_stop.py --manual` |
| MED | `appendix/A_prompt_log.md` | phiên claude.ai chỉ tới 21:40 17/11 (bản xuất cũ) | Xuất lại dữ liệu claude.ai → thay `.transcripts/claude-ai_session_HW04_p1.json` → trích lại log → cập nhật số lượt ở AI-02/03/05 |
| MED | report §10 dòng ~855 | khối "📝 AI nháp – SV xác nhận" + 2 ô `<SV viết>` | SV xác nhận, xoá dòng 📝, viết 2 ô |
| MED | AI-02 §4, AI-03 mục 2/3/4/5, chữ ký AI-02/03/05 | `<SV viết>` / `<SV điền>` / `[...]` | SV viết, ký, xuất lại PDF |
| MED | report §9 | `a99d6ee` (commit AI) chưa có verdict | SV ghi verdict |
| MED | report §7 | "Chỗ sửa script AI được kể trong video" `<SV viết>` | SV ghi |
| MED | `appendix/commit_log.txt` | xuất ở `f9a7d67`, sẽ lệch sau các commit kế | Xuất lại sau commit cuối (`tools/export_commit_log.ps1 HW04`) |
| LOW | report | script đếm "135 lượt" ≠ 86 lượt log | Không sửa: 135 = lượt test thực thi (TC × trình duyệt), không phải lượt AI |
| LOW | report mục lục | 11 anchor `#…` script báo "không tồn tại" | Không sửa: anchor nội bộ, không phải file |
| LOW | AI-05 | 7 mục cam kết `[ ]` "(em tự xác nhận)" | SV tick khi đúng thật |

Đã khớp:
- Form bắt buộc AI-02, AI-03, AI-05 có .md + .pdf (chưa ký); AI-04 không bắt buộc (HW); AI-06 nộp tuần 1.
- Cấp độ AI: report dòng đầu "Cấp 4" = AI-03.
- Số lượt: log 86 = AI-02 = AI-03 = AI-05 (Claude Opus 5.5 49, không rõ model 37: 36 claude.ai + #52).
- AI Critique: 292 từ (đếm theo khoảng trắng, bỏ dòng `>`), trong khoảng 200–300.
- Verdict khớp Khai cho Audit: các commit có lỗi AI đã nêu (b0e2f7c serial, 9a5e558/7e75536/370c9cd spec bước 3, 2667147 chép nhầm C3, 5bb31d1 v2 chưa chạy E2E) đều INCOMPLETE; không có artifact lỗi mà ghi VALID.
- Tỉ lệ verdict (report §9 = AI-02 §3.2): VALID 45 (80%), INVALID 0, INCOMPLETE 11 (20%); không tính 11 commit SV làm, 1 commit AI chưa có verdict.
- Bug report: 18 bug do SV viết (commit `2775914`, `8f47846`, `1881c16`, `b264556`); bảng §6 ghi "(AI chép)".
- Không có file > 20 MB trong HW04; file nội bộ (`CLAUDE.md`, `report_plan.md`, `placeholders_left.md`) đã `export-ignore`.
