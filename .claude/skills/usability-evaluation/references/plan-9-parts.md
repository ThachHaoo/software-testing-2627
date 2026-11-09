# Kế hoạch 9 phần (slide *The 9-part test plan*, Rubin & Chisnell)

"Plan before you recruit — the plan is the contract for the study." `check_kit.py --plan` kiểm 9 tiêu đề `## 1.` … `## 9.` đúng thứ tự và mỗi phần có nội dung.

| # | Phần (slide) | Tiêu đề gợi ý trong plan.md | Phải có |
|---|---|---|---|
| 1 | Purpose | Mục đích | Vì sao test, quyết định nào sẽ dựa vào kết quả |
| 2 | Problem statement (specific questions) | Câu hỏi cần trả lời | Câu hỏi cụ thể, trả lời được bằng dữ liệu thu (Q1…Qn) |
| 3 | Test objectives & tasks | Mục tiêu và nhiệm vụ | Nhiệm vụ dạng mục tiêu (không nêu bước), trạng thái đầu, thông tin phát cho người tham gia, tiêu chí thành công đo được, benchmark thời gian |
| 4 | User profile | Hồ sơ người dùng | Tiêu chí chọn người; không chứa dữ liệu cá nhân |
| 5 | Method & test design | Phương pháp và thiết kế | Moderated/unmoderated, think-aloud, số phiên (+ pilot), thứ tự trong phiên, thời lượng |
| 6 | Environment / equipment | Môi trường và thiết bị | Máy, trình duyệt, URL, reset dữ liệu trước mỗi phiên, công cụ quay, rủi ro môi trường đã biết |
| 7 | Test-monitor role | Vai trò người điều phối | Khi nào can thiệp, câu nhắc trung tính, ghi lại mỗi lần trợ giúp |
| 8 | Evaluation measures & data to collect | Đo lường và dữ liệu thu | Performance (thời gian, hoàn thành, lỗi, trợ giúp) + preference (SEQ, SUS, câu hỏi mở) và nơi ghi |
| 9 | Report contents | Nội dung báo cáo | Bảng số liệu, findings theo criticality, bug → issue, giới hạn nghiên cứu |

Nhiệm vụ "come from a user model, not the code".

Thống kê cần báo cáo (slide *Summarizing the results*):
- Performance: thời gian (mean, median, range, SD), % hoàn thành trong benchmark / bất kể thời gian / có trợ giúp, tỉ lệ lỗi trung bình.
- Preference: điểm Likert trung bình (SEQ, SUS), đếm và % từng lựa chọn, câu trả lời mở chia tích cực/tiêu cực và gom theo chủ đề (SV làm).

Phân tích (slide *Analysis*): bắt đầu từ nhiệm vụ thất bại, tìm từng lỗi và nguồn gốc; **criticality = severity × probability**; sửa mục criticality cao trước; kết thúc bằng khuyến nghị cụ thể, có ưu tiên.
