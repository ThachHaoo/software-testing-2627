# HW03 – GUI & Usability on EShop

**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Cấp độ AI:** Cấp 4 | **Bloom-AI:** G9.3 + G9.4 | **Công cụ AI:** 📝

> Quy ước: 📝 = chỗ em viết · 🔒 = phần AI không được viết hộ.

## Tự đánh giá 🔒

| No. | Tiêu chí | Điểm | Tự đánh giá | Căn cứ |
|---|---|---|---|---|
| 1 | Task 1 – GUI Checklist (thiết kế + chạy + bug report) | 30 | `<SV điền>` | `<SV điền>` |
| 2 | Task 2 – Usability Evaluation (kịch bản + 7 phiên + phân tích) | 40 | `<SV điền>` | `<SV điền>` |
| 3 | Task 3 – Cross-Browser / Cross-Platform (≥ 3 nền tảng) | 20 | `<SV điền>` | `<SV điền>` |
| 4 | Agent Skills (+ video YouTube) | 10 | `<SV điền>` | `<SV điền>` |
|  | **Tổng** (= 3 chữ số trong tên zip) | **100** | `<SV điền>` | |

## Test summary

<!-- SUMMARY:START -->
| Chỉ số | P1 – Cốc Cốc (Chromium) trên Windows | P2 – Firefox trên Windows | P3 – Chrome Android (POCO F5, adb reverse) | Tổng |
|---|---|---|---|---|
| Màn hình kiểm (M1–M5) | 5 | 5 | 5 | 5 |
| Item checklist thiết kế | 74 | 74 | 74 | 74 |
| Item đã chạy (trừ N/A) | 74 | 74 | 70 | 218 ô |
| Passed | 25 | 24 | 22 | 71 ô |
| Failed | 46 | 47 | 44 | 137 ô |
| N/A | 0 | 0 | 4 | 4 ô |
| Blocked | 3 | 3 | 4 | 10 ô |

- Bug: item Failed đối chiếu issue nhóm → **trùng 14**, **trùng một phần 4**, **MỚI 28** (`bugs/failed_list.md`, `bugs/dup_check.md`); MỚI + phần mới gom thành **28 bug** `BUG-58…85` (`bugs/bug_groups.md`); đã có link GitHub Issue: 0/28.
- Nguồn item checklist: AI 48 · AI + SV sửa 20 · SV bổ sung 6.
- Usability (Task 2): không thực hiện phiên usability nào (report §5.4–5.9); kế hoạch, phiếu người tham gia, phiếu quan sát ở `usability/`.
- Video Agent Skill: `skills/VideoLinks.md`.
- Sinh bằng `tools/summary_hw03.py` từ `checklist/checklist.json`, `bugs/`.
<!-- SUMMARY:END -->

## Video demo (YouTube)

| Nội dung | Link |
|---|---|
| Agent Skill `gui-checklist-testing`, `usability-evaluation` | xem `skills/VideoLinks.md` |

## Tài liệu trong bài nộp

| File | Nội dung |
|---|---|
| `23120255_HW03_Report.md` / `.pdf` | Report chính: checklist report + usability report + AI Critique |
| `excel/23120255_HW03_Checklist.xlsx` | Checklist (> 40 item) + test summary |
| `checklist/evidence/P1_chrome`, `P2_firefox`, `P3_android` | Ảnh cross-platform có overlay (email SV + MSSV + họ tên) |
| `usability/` | Kịch bản, ghi chú quan sát, SUS, findings xếp hạng, bảng 7 người, `sessions/` |
| `bugs/` | Bug report + `issues_page_HW03.png` |
| `ai-forms/` | AI-02 Audit Report, AI-03 Disclosure, AI-05 Privacy Checklist (.md + PDF) |
| `appendix/A_prompt_log.md` | Prompt log (trích tự động) |
| `appendix/ai-outputs/` | Output AI gốc (đóng băng) |
| `commit_log.txt` | Git commit log |
| `skills/` | Agent Skill + `VideoLinks.md` |
