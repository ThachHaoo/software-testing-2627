**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**
**CS423 / CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**
**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# Bảng Kiểm Quyền Riêng tư & Sử dụng AI Có Trách nhiệm

*Thực hiện bảng kiểm này TRƯỚC KHI nộp bất kỳ bài tập có dùng AI.*

**Bài tập:** HW#01 – QA/QC Jobs · 20 Defects · Test a Physical Product
**Công cụ AI:** Claude Opus 5.5 (24 lượt), Gemini Flash (1 lượt) – chi tiết ở AI-03 và Phụ lục A

## 1. Trước khi dùng AI

- [ ] Đã xác nhận Cấp độ AI cho bài tập này.
  *Báo cáo và AI-03 ghi Cấp 4 – cần đối chiếu với thang cấp độ trong slide môn học.*
- [ ] Dùng tài khoản Claude Pro tự chọn (không phải tài khoản cá nhân).
  *Tự xác nhận loại tài khoản đã dùng.*
- [ ] Đã đọc Thoả thuận AI của môn học.
- [x] Hiểu rõ artifact nào KHÔNG được sinh bằng AI.
  *Ảnh thiết bị + thẻ SV, giọng thuyết minh video, screenshot tin tuyển dụng có username, prompt log có timestamp – đã liệt kê trong mục 6 báo cáo và AI-03.*

## 2. Trong khi dùng AI

- [ ] Không nhập dữ liệu cá nhân của bạn, khách hàng, bệnh nhân.
  *Không nhập dữ liệu của người khác. Tuy nhiên file báo cáo gửi cho AI có họ tên, MSSV, lớp và link GitHub của chính SV – tự quyết định có tick hay không và ghi chú nếu cần.*
- [ ] Không paste nguyên si tài liệu có bản quyền lên AI.
  *Đã gửi: file đề bài HW01 (tài liệu môn học), 1 ảnh chụp tài liệu ISTQB của môn (#12), 1 ảnh mindmap tham khảo của Learning Fundamentals (#10, chỉ để tham khảo phong cách, không sao chép nội dung). Tự đánh giá mức độ phù hợp trước khi tick.*
- [x] Không paste code công ty / code open-source giới hạn license.
  *Không gửi bất kỳ đoạn code nào cho AI.*
- [ ] Đã ghi mọi prompt + phản hồi AI vào prompt_log.md có timestamp.
  *Chỉ tick sau khi: xóa các entry mẫu "#1 | 14:32"; dán output thật của Gemini vào #17; sửa ô "Xử lý" của #19; sửa timestamp #8, #9, #16.*

## 3. Trước khi nộp bài

- [x] Mọi artifact AI sinh đã được gắn tag trong AI Audit Report.
  *19 artifact (A01–A19) có verdict VALID / INVALID / INCOMPLETE trong AI-02; mục 4 báo cáo cần đồng bộ số lượng.*
- [x] Mọi trích dẫn AI đã được xác minh (nguồn thực sự tồn tại).
  *Đã mở toàn bộ link tin tuyển dụng (R1) và nguồn defect (R2); ghi nhận 1 link hết hạn (D16) và phát ngôn bịa của Gemini (D18, mục 2.2).*
- [x] Mọi code AI sinh đã được thực thi và test.
  *Không nộp code do AI sinh. File Excel có 53 công thức, đã tính lại: 0 lỗi, số liệu khớp bảng 3.3 (13 Pass, 2 Fail).*
- [ ] AI Critique 200–300 chữ đã có trong báo cáo.
  *Bản hiện tại 337 chữ – cần cắt xuống ≤ 300 rồi mới tick.*
- [x] Đoạn Mandatory Disclosure ở cuối báo cáo.
  *Mục 6 báo cáo, có họ tên, MSSV, lớp, ngày.*
- [x] Đính kèm AI Use Disclosure Form.
  *`ai-templates/AI-03_Disclosure_Form_23120255` – cần ký trước khi nộp.*
- [ ] Sẵn sàng cho vấn đáp ngẫu nhiên 5–7 phút tuần kế nộp bài.
  *Ôn: lý do chọn input của TC11–TC15; 1 lỗi AI đã sửa (E1–E3 hoặc Gemini/D18); chạy lại 1 TC trên quạt.*

## 4. Cam đoan Cuối cùng

*Trách nhiệm cuối cùng về độ chính xác, tính nguyên bản, và liêm chính của bài nộp này thuộc về tôi. Mọi việc dùng AI không khai báo đều bị coi là vi phạm liêm chính học thuật.*

## Chữ ký

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |
| MSSV: | 23120255 |
| Lớp / Khoá: | Software Testing - 23_3 |
| Môn học: | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| Giảng viên: | |
| Ngày: | 30/09/2026 |
| Chữ ký: | |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Hardman, P. (2025). A Post-AI Learning Taxonomy.
- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.
- Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.
- Anthropic (2025). Building reliable AI test agents — engineering blog.
- DeepEval & Promptfoo documentation — testing frameworks for LLM systems.
