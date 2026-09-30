**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**
**CS423 / CSC15003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**
**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# Biểu mẫu Khai báo Sử dụng AI

*Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.*

## 1. Thông tin Môn học & Sinh viên

| Mục | Giá trị |
|---|---|
| Môn học: | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| Mã bài tập: | HW#01 |
| Tên bài tập: | QA/QC Jobs · 20 Defects · Test a Physical Product |
| Cấp độ AI (1–5): | Cấp 4 |
| Ngày: | 30/09/2026 |
| Họ tên sinh viên: | Lê Tấn Hiệp |
| MSSV: | 23120255 |

## 2. Câu hỏi Khai báo

### 1. Công cụ AI đã dùng:

- **Claude (Claude Opus 5.5, claude.ai)** – 24 lượt (#1–#16, #18–#25 trong prompt log), gồm 1 lượt dùng chế độ Research (#14).
- **Gemini Flash** – 1 lượt (#17), dùng làm đối chứng để kiểm tra hallucination khi giải thích defect D18.
- Không dùng GitHub Copilot, Cursor hay công cụ AI nào khác.

### 2. Giai đoạn nào của bài tập có dùng AI:

[x] brainstorm [x] outline [x] viết nháp [x] phản hồi [x] sửa chữa [ ] code [x] phân tích dữ liệu [x] thiết kế đồ hoạ [x] khác (ghi rõ)

- **Brainstorm:** gợi ý test case cho quạt (#4), tìm thêm tin tuyển dụng có yêu cầu AI (#6).
- **Outline:** dựng khung báo cáo, bảng biểu, placeholder (#1–#3).
- **Viết nháp:** điền bảng 1.1, 1.2, 1.4 (#7, #8, #13); bảng 20 defect (#15); nháp AI Audit Report (#19); bản tiếng Việt của Mandatory Disclosure (#21); Phụ lục (#22); nháp tự đánh giá (#23).
- **Phản hồi:** góp ý câu chữ mục 1.3 (#11, #12); góp ý AI Critique, không viết hộ (#20); phản hồi về 5 edge case tự tìm (#5).
- **Sửa chữa:** cập nhật mục 3.6 sau khi bỏ Mantis (#24).
- **Phân tích dữ liệu:** thống kê thị trường từ 10 tin (#13); file Excel Test Summary có công thức (#25).
- **Thiết kế đồ hoạ:** vẽ mindmap vai trò QA/QC bản gốc (#9, #10).
- **Khác:** research 20 software defect có nguồn (#14); giải thích D18 để làm đáp án đối chứng (#16, Claude) và để tìm hallucination (#17, Gemini); xác nhận hallucination (#18).

### 3. Prompt / nhiệm vụ chính cho AI:

*Nguyên văn đầy đủ của 25 lượt nằm ở Phụ lục A (`appendix/A_prompt_log.md`).*

1. **#4 – 18:48 29/09/2026 – Claude (R3):**
   > "Mình nghĩ là không cần bỏ bảng phân loại, cấu trúc hiện tại ổn rồi. Giờ mình sẽ làm bài 3, hiện tại mình chỉ có một cái quạt điện để test. Nó là Quạt Kakashi, Model: B300, chỉ có thể có các thao tác với chỗ làm cho quạt quay, hoặc đứng yên. Và các nút để mở quạt số 1, 2, 3 và tắt quạt số 0. Hãy giúp mình viết các test case để làm bài tập 3 nhé."

2. **#14 – 05:16 30/09/2026 – Claude Research (R2):**
   > "Giờ qua thực hiện requirement 2. Hãy giúp tôi research "software defects publicized between 2022 and 2026." Không bịa nguồn. Cứ research theo các tiêu chí: | ID | Tên defect | Năm công bố | Tổ chức / Sản phẩm | Nhóm | Loại lỗi | Severity | Nguồn | … | ID | Mô tả | Hậu quả | Giải pháp (thực tế) | Bài học kiểm thử | Sau khi research xong, tôi sẽ đưa format để bạn điền vào nhé"

3. **#17 – 08:08 30/09/2026 – Gemini Flash (R2):**
   > "Mình đang tìm hiểu về một sự cố phần mềm liên quan đến AI: chatbot MyCity của thành phố New York (NYC) đã đưa ra lời khuyên khiến doanh nghiệp làm trái luật. Hãy giải thích giúp mình tìm hiểu thêm về các thông tin sau về sự cố này (với mỗi ý, hãy ghi nguồn tham khảo): Sự cố được công bố vào ngày nào? Con số thiệt hại là bao nhiêu? Nguyên nhân gốc xảy ra defect này là gì? Có bao nhiêu người bị ảnh hưởng về vấn đề này? Ai đã chịu trách nhiệm cho vấn đề này? Ai phát triển chatbot và dựa trên nền tảng gì? Nêu 2–3 ví dụ cụ thể về câu trả lời sai của chatbot. Chính quyền đã phản ứng thế nào? Hiện nay chatbot đó còn hoạt động không?"

### 4. Phần cụ thể AI đóng góp:

- **R1:**
  - AI gợi ý 3 tin J08–J10 và điền bảng 1.1.
  - AI tóm tắt mô tả công việc và kỹ năng cho J02–J10 (1.2).
  - AI vẽ mindmap bản gốc (1.3).
  - AI soạn nháp bảng thống kê, bảng phân loại và đoạn nhận xét ở 1.4.
  - **AI KHÔNG đóng góp** nội dung J01, 10 ô AI Impact Analysis, và phần phân tích 3 lỗi E1–E3.
- **R2:**
  - AI research và điền bảng 2.0, 2.1 (20 defect, 8 AI/LLM).
  - AI giải thích D18 để làm đáp án đối chứng.
  - Gemini sinh câu trả lời chứa hallucination, được dùng làm minh chứng ở 2.2.
  - **AI KHÔNG đóng góp** việc phát hiện câu bịa và chụp minh chứng.
- **R3:**
  - AI sinh 15 test case ban đầu và 5 giả định G1–G5. Em giữ 10 TC (TC01–TC10) và lấy G1–G4 làm bảng chức năng F1–F4.
  - AI tạo file `23120255_TestCases.xlsx` từ dữ liệu bảng 3.3.
  - **AI KHÔNG đóng góp** 5 edge case TC11–TC15, việc thực thi test, 5 video, thông tin thiết bị (3.1) và kết luận (3.5).
- **Mục 4–7 và Phụ lục:**
  - AI soạn nháp AI Audit Report (mục 4 và AI-02), bản tiếng Việt của Mandatory Disclosure, bảng tóm tắt Phụ lục và nháp tự đánh giá.
  - **AI KHÔNG viết AI Critique** (mục 5), chỉ góp ý.
- **AI KHÔNG tạo** bất kỳ artifact nào thuộc danh mục cấm: ảnh thiết bị cùng thẻ sinh viên, giọng thuyết minh video, screenshot tin tuyển dụng, prompt log.

### 5. Cách tôi rà soát / chỉnh sửa / xác minh đầu ra AI:

- **Tin tuyển dụng (R1):**
  - Mở lại từng tin bằng tài khoản của mình và đối chiếu ngày đăng, cấp độ, địa điểm, lương.
  - Sửa lương J03–J10 theo trang hiển thị khi đăng nhập.
  - Tự chụp screenshot có username.
- **Mindmap (1.3):**
  - Đối chiếu từng nhánh với tài liệu ISTQB (v4.0.1) của môn học (§1.4.5, chương 2.2) và với 10 tin tuyển dụng ở R1.
  - Tìm và sửa 3 lỗi E1–E3.
  - Khi AI và tài liệu môn học trình bày khác nhau về "Kiểm thử sau thay đổi", em chọn theo tài liệu môn học và ghi rõ nguồn.
- **Defect (R2):**
  - Mở toàn bộ link nguồn, dùng Ctrl+F để đối chiếu từng con số và câu trích.
  - Phát hiện 1 link hết hạn (D16) và 1 thông tin đã cũ (D18), rồi cập nhật lại.
  - Với D18: hỏi cùng một bộ câu hỏi ở 2 công cụ (Claude, Gemini), đối chiếu với nguồn gốc (The Markup, AP), và phát hiện Gemini bịa phát ngôn của Microsoft.
- **Test case (R3):**
  - Kiểm tra 5 giả định của AI trên quạt thật; đánh giá từng TC là VALID / INVALID / INCOMPLETE.
  - Loại 5 TC trùng lặp hoặc tốn thời gian.
  - Chạy thật trên quạt để điền Actual / Verdict.
  - Tự tìm 5 edge case, rồi hỏi lại AI (#5) để xác nhận các edge case này không có trong output gốc.
- **Excel:** đối chiếu từng dòng với bảng 3.3; kiểm tra số liệu tổng hợp (13 Pass, 2 Fail) khớp với báo cáo.
- **Các phần AI soạn nháp (mục 4, 6, 7, Phụ lục):**
  - Đối chiếu với prompt log và nội dung thực tế.
  - Đổi xưng hô, sửa các điểm không đúng với thực tế.
  - Tự chốt điểm và checklist.

### 6. Trích dẫn (nếu môn yêu cầu):

[1] Anthropic. (2026). *Claude Opus 5.5* [Large language model]. https://claude.ai

[2] Google. (2026). *Gemini Flash* [Large language model]. https://gemini.google.com

## 3. Cam đoan Trung thực

*Bằng việc ký tên dưới đây, tôi cam đoan thông tin khai báo ở trên là chính xác và đầy đủ. Tôi hiểu rằng việc không khai báo hoặc khai báo sai lệch về việc dùng AI sẽ bị coi là vi phạm liêm chính học thuật và có thể dẫn đến điểm 0 cho bài tập cùng việc bị chuyển lên hội đồng kỷ luật.*

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
