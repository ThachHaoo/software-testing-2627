# HW03 – GUI & Usability on EShop

**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Cấp độ AI:** Cấp 4 | **Bloom-AI:** G9.3 + G9.4 | **Công cụ AI:** Claude (Opus 5.5, Sonnet 4.6) qua claude.ai và Claude Code

## Tự đánh giá 🔒

| No. | Tiêu chí | Điểm | Tự đánh giá | Căn cứ |
|---|---|---|---|---|
| 1 | Task 1 – GUI Checklist (thiết kế + chạy + bug report) | 30 | 28 / 30 | Đã thiết kế 74 item (AI 48 · Both 20 · SV 6; bản v1 có 65 item), thực thi trên 3 nền tảng P1/P2/P3, đối chiếu 47 item Failed ra 14 trùng, 4 trùng một phần, 28 bug mới `BUG-58…85`, lập đủ 28 GitHub Issues (#247–#274). |
| 2 | Task 2 – Usability Evaluation (kịch bản + 7 phiên + phân tích) | 40 | 35 / 40 | Hoàn thành kế hoạch 9 phần (`plan.md`), điều phối 7 phiên chính thức S01–S07 (và 1 pilot S00), thu thập dữ liệu SEQ trung bình 6,3 và SUS trung bình 77,9, phân tích các pain point nhưng phần lập bug cho các pain point chưa có issue và mốc thời gian còn mang tính ước lượng. |
| 3 | Task 3 – Cross-Browser / Cross-Platform (≥ 3 nền tảng) | 20 | 19 / 20 | Kiểm thử toàn diện trên 3 nền tảng khác nhau gồm P1 (Cốc Cốc/Chromium trên Windows), P2 (Firefox trên Windows) và P3 (Chrome Android trên POCO F5 qua adb reverse), có đầy đủ ảnh chụp bằng chứng overlay thông tin sinh viên. |
| 4 | Agent Skills (+ video YouTube) | 10 | 9 / 10 | Đã đóng gói đầy đủ 2 Agent Skills (`gui-checklist-testing`, `usability-evaluation`) kèm theo cấu trúc script chuẩn và khai báo link video demo trong `skills/VideoLinks.md`. |
|  | **Tổng** (= 3 chữ số trong tên zip) | **100** | **91 / 100** | Tổng điểm tự đánh giá phản ánh mức độ hoàn thành toàn diện các task theo đúng yêu cầu chi tiết của đề bài HW03. |

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

- Bug: item Failed đối chiếu issue nhóm → **trùng 14**, **trùng một phần 4**, **MỚI 28** (`bugs/failed_list.md`, `bugs/dup_check.md`); MỚI + phần mới gom thành **28 bug** `BUG-58…85` (`bugs/bug_groups.md`); đã có link GitHub Issue: 28/28.
- Nguồn item checklist: AI 48 · AI + SV sửa 20 · SV bổ sung 6.
- Usability (Task 2, U1): 7 phiên chính S01–S07 + 1 pilot S00; hoàn thành 7/7; **SUS TB 77,9**, **SEQ TB 6,3** (report §5.6–5.7, `usability/sessions/`).
- Video Agent Skill: `skills/VideoLinks.md`.
- Sinh bằng `tools/summary_hw03.py` từ `checklist/checklist.json`, `bugs/`.
<!-- SUMMARY:END -->

## Video demo (YouTube)

| Nội dung | Link |
|---|---|
| Agent Skill `gui-checklist-testing`, `usability-evaluation` | [YouTube](https://youtu.be/2E0pcpoG7Mk) (`skills/VideoLinks.md`) |

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
| `appendix/commit_log.txt` | Git commit log |
| `skills/` | Agent Skill + `VideoLinks.md` |
