## 4. AI Audit Report

**Công cụ AI đã dùng:** Claude (claude-opus-5-5) – 17 lượt; Gemini Flash – 1 lượt (dùng làm "đối chứng" để tìm hallucination).
**Quy ước:** nguyên văn prompt và output của mọi lượt nằm ở **Phụ lục A – Prompt log** (mã `#n`). Output dạng file được lưu nguyên bản trong `appendix/ai-outputs/`. Dưới đây, output ngắn được trích nguyên văn; output dài được trích đoạn chính và dẫn chiếu tới file gốc.

**Danh sách artifact có dùng AI:**

| Mã | Artifact | Section | Prompt | Verdict |
|---|---|---|---|---|
| A01 | Khung báo cáo (dàn ý đầy đủ, bảng, placeholder) | Toàn bài | #1, #2, #3 | VALID |
| A02 | Tìm thêm tin tuyển dụng có yêu cầu AI | 1.1 (J08–J10) | #6 | VALID |
| A03 | Điền bảng 10 tin tuyển dụng | 1.1 | #7 | INCOMPLETE |
| A04 | Tóm tắt JD (mô tả, kỹ năng) cho 10 tin | 1.2 | #8 | INCOMPLETE |
| A05 | Mindmap vai trò QA/QC | 1.3 | #9, #10 | INCOMPLETE |
| A06 | Review câu chữ mục 1.3 | 1.3 | #11, #12 | INCOMPLETE |
| A07 | Thống kê và phân loại thị trường | 1.4 | #13 | INCOMPLETE |
| A08 | Research + bảng 20 software defect | 2.0, 2.1 | #14, #15 | INCOMPLETE |
| A09 | Giải thích D18 (Claude) | 2.1 (D18), 2.2 | #16 | VALID |
| A10 | Giải thích D18 (Gemini) | 2.2 | #17 | INVALID |
| A11 | Xác nhận hallucination của Gemini | 2.2 | #18 | VALID |
| A12 | Bộ 15 test case quạt (bản gốc của AI) | 3.3 | #4 | INCOMPLETE |
| A13 | Phản hồi của AI về edge case của SV | 3.3, 3.4 | #5 | VALID |

---

### A01 – Khung báo cáo

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 17:38, 17:41, 18:34 – 29/09/2026<br>**Prompt #2:** "Đây là dàn ý hiện tại của tôi, chỉ có các đề mục. Giờ tôi muốn bạn giúp tôi hoàn thiện dàn ý (như là vẽ bảng trước các chỗ cần vẽ, list những yêu cầu viết chi tiết, placeholder cho những chỗ cần ảnh minh chứng,...) Sau khi viết xong, output ra lại file .md giúp tôi" (#1, #3: xem Phụ lục A) |
| (2) AI output | File `appendix/ai-outputs/23120255_HW01_Report.md`. Trích: *"Mình có thêm 3 mục mới so với dàn ý ban đầu… 1.4 Tổng hợp xu hướng thị trường… 3.2 Phạm vi và chiến lược kiểm thử… Phụ lục D."* Ở #3, AI đề xuất *"Bảng phân loại… trong 1.4… nên bỏ."* |
| (3) Verdict | **VALID** |
| (4) Reasoning | Khung bám đúng các yêu cầu của đề (R1–R3, Audit Report, Critique, Disclosure, tự đánh giá) và nhắc được các điểm dễ sót như mindmap G9.1, Mantis, file Excel. Mục 3.2 "Phạm vi và chiến lược kiểm thử" phù hợp với nội dung test planning trong ISTQB CTFL v4.0 §5.1 (test plan gồm phạm vi, cách tiếp cận). Đề xuất bỏ bảng phân loại ở 1.4 (#3) là ý kiến, không phải lỗi; tôi không theo vì bảng này trực tiếp đáp ứng outcome "phân biệt việc AI thay thế / hỗ trợ / không thay thế". |
| (5) Student fix | Giữ nguyên khung. **Không bỏ** bảng phân loại ở 1.4 (khác đề xuất của AI). Đổi đường dẫn ảnh sang `R1_jobs/`, `R2_defects/`, `R3_device/`. |

### A02 – Tìm thêm tin tuyển dụng có yêu cầu AI

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 00:27 30/09/2026<br>**Prompt #6:** "…Hiện tại tôi đang cố tìm các jd có 'yêu cầu AI/LLM/AI-assisted automation.', nhưng tìm không ra. Bạn giúp tôi tìm thêm 2 cái nữa nhé" (kèm 8 link, nguyên văn ở Phụ lục A) |
| (2) AI output | Trích: *"1. QA Engineer (Claude Code, Python, React, Manual Tester) — Brarista… 2. [Hanoi] Fullstack QA Engineer Lead (Manual, Auto, AI) — Money Forward Vietnam… Dự phòng: Lead Penetration Tester (Web, API & AI Applications) — Galaxy Holdings… Nhược điểm: đây là vị trí security testing, không hẳn là QA/QC."* Kèm link và trích dẫn JD. |
| (3) Verdict | **VALID** |
| (4) Reasoning | Tôi mở cả 3 link bằng tài khoản của mình: đều còn hoạt động, đăng trong 60 ngày, và các câu trích về AI khớp nguyên văn trong JD. AI tự nêu rủi ro của tin dự phòng (security testing không hẳn là QA/QC), giúp tôi chuẩn bị lý do khi bị hỏi. Việc xác minh ngày đăng và chụp màn hình có tên tài khoản do tôi tự làm. |
| (5) Student fix | Không sửa nội dung. Dùng cả 3 tin (J08, J09, J10). Tự chụp screenshot. |

### A03 – Điền bảng 10 tin tuyển dụng (1.1)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 01:15 30/09/2026<br>**Prompt #7:** "Giúp tôi tiếp tục điền vào bảng sau nhé: …" (kèm bảng và 7 link, nguyên văn ở Phụ lục A) |
| (2) AI output | Bảng 1.1 đầy đủ 10 dòng (nguyên văn ở Phụ lục A, #7). Các ô lương của J03, J04, J06, J09, J10 để `[đăng nhập để xem]`; J07 ghi "Lên đến 35 triệu VND (thỏa thuận)". |
| (3) Verdict | **INCOMPLETE** |
| (4) Reasoning | Thông tin vị trí, cấp độ, địa điểm, ngày đăng khớp với JD khi tôi đối chiếu. Tuy nhiên AI không đọc được lương (ITviec ẩn khi chưa đăng nhập), và mức lương J07 lấy từ phần phúc lợi trong JD, khác với mức hiển thị khi đăng nhập. AI cũng tự phát hiện và sửa lỗi lệch cột ở J03 trong bảng của tôi. |
| (5) Student fix | Lương: `[đăng nhập để xem]` → **"Không công bố ('You'll love it')"** (J03, J04, J06, J09, J10). J07: ~~"Lên đến 35 triệu VND"~~ → **"800 – 1,500 USD"** (theo trang khi đăng nhập). J08: → **"800 – 1,000 USD"**. J05: bổ sung **"400.000 VND/tháng phí đỗ xe"**. Cột "Yêu cầu AI?": đổi phần giải thích thành trích dẫn từ JD. |

### A04 – Tóm tắt JD cho 10 tin (1.2)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 01:35 30/09/2026<br>**Prompt #8:** "Tiếp tục giúp tôi điền 1.2 nhé, ý nào bắt buộc phải tự viết thì giữ nguyên để tôi tự viết nhé…" |
| (2) AI output | File `appendix/ai-outputs/HW01_R1_1.2.md`. AI điền mô tả, kỹ năng, lương cho J02–J10; **để trống** J01 (*"LinkedIn chặn công cụ đọc trang của mình"*) và toàn bộ AI Impact Analysis. |
| (3) Verdict | **INCOMPLETE** |
| (4) Reasoning | Phần tóm tắt J02–J10 khớp với JD khi tôi đối chiếu từng tin. AI không truy cập được LinkedIn nên thiếu J01. AI chủ động để trống AI Impact Analysis vì đây là phần phân tích của SV. |
| (5) Student fix | **Tự viết J01** (mô tả, kỹ năng từ JD LinkedIn). **Tự viết toàn bộ 10 ô AI Impact Analysis.** Rà lại câu chữ các ô mô tả. |

### A05 – Mindmap vai trò QA/QC (1.3)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 02:42 và 02:51 30/09/2026<br>**Prompt #9:** "Giờ giúp tôi thực hiện 1.3 nhé, có thể vẽ ảnh để rồi tôi tìm lỗi cũng được…"<br>**Prompt #10:** "Mình thấy là tạo bằng mermaid nó rối và khó nhìn quá. Bạn có thể giúp mình tạo sinh ảnh Mindmap colorful luôn được không?…" |
| (2) AI output | Mã nguồn `appendix/ai-outputs/mindmap_ai.mmd` và ảnh `R1_jobs/mindmap_QA_QC.png` (Hình ở mục 1.3). 9 nhánh: QA, QC, Vai trò theo ISTQB, Chức danh trên thị trường, Test levels, Test types, Kiểm thử sau thay đổi, Kỹ năng cốt lõi, AI trong QA/QC. |
| (3) Verdict | **INCOMPLETE** |
| (4) Reasoning | Nội dung từng nhánh con phần lớn đúng (ví dụ 2 vai trò test management và testing khớp ISTQB CTFL v4.0.1 §1.4.5), nhưng có 3 lỗi cấu trúc và nội dung: (E1) đặt kiến thức kỹ thuật (test levels, test types – chương 2.2) ngang hàng với vai trò, lệch khỏi yêu cầu "QA/QC role mindmap"; (E2) thiếu chức danh QC, dù 5/10 tin ở R1 có "QC" trong tên vị trí; (E3) node "Con người quyết định release" nằm trong nhánh các việc AI làm. Chi tiết ở bảng lỗi mục 1.3. |
| (5) Student fix | **E1:** gom Test levels + Test types vào nhánh mới **"Kiến thức nền tảng"**, chuyển "Kiểm thử sau thay đổi" vào **Test types** (theo tài liệu môn học). **E2:** thêm **"QC Intern / Fresher"**. **E3:** ~~"Con người quyết định release"~~. Ảnh sau sửa: `R1_jobs/mindmap_fixed.png`. |

### A06 – Review câu chữ mục 1.3

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 04:58 và 05:02 30/09/2026<br>**Prompt #11:** "Sau đây là mình chỉnh lại mindmap, bạn xem có câu từ gì cần chỉnh lại không nhé: …"<br>**Prompt #12:** "Về cái bạn nói là mình trích sai ISTQB. Thì hiện tại mình đang trích từ của thầy, phiên bản v4.0.1, nên là đúng rồi nhé…" (kèm ảnh tài liệu môn học) |
| (2) AI output | #11 trích: *"Bạn viết: 'trong CTFL v4.0 thì Kiểm thử sau thay đổi cũng là một Test type'. Câu này không đúng với v4.0… Confirmation testing và regression testing được tách ra một mục riêng là §2.2.3."* Kèm góp ý: E2 là 5/10 tin chứ không phải 4; E3 nên chuyển node thay vì xóa.<br>#12 trích: *"Bạn chỉ cần ghi căn cứ đúng nguồn… Nên ghi: 'Tài liệu học ISTQB Foundation (CTFL v4.0.1) của môn học, chương 2.2'."* |
| (3) Verdict | **INCOMPLETE** |
| (4) Reasoning | Góp ý về câu chữ và lỗi chính tả hữu ích. Về cách phân loại "Kiểm thử sau thay đổi", AI đối chiếu với syllabus ISTQB gốc, còn tôi dùng tài liệu ISTQB v4.0.1 của môn học (xếp change-related testing là một test type). Hai nguồn trình bày khác nhau; tôi chọn theo tài liệu môn học và ghi rõ nguồn này trong cột "Căn cứ" theo gợi ý ở #12. |
| (5) Student fix | Cột "Căn cứ" của E1: ~~"CTFL v4.0 chương 2.2"~~ → **"tài liệu ISTQB (v4.0.1) của môn học, chương 2.2"**. Giữ cách sửa E1–E3 của mình. |

> 📝 Gợi ý (xóa trước khi nộp): bảng 1.3 hiện vẫn ghi E2 "4/10 JD (J03, J04, J05, J06)" và còn lỗi chính tả "Kiêm thử". Nếu giữ con số 4/10 thì nên ghi lý do không tính J07; nếu không, sửa thành 5/10 (J03–J07) cho khớp với A05 ở trên.

### A07 – Thống kê và phân loại thị trường (1.4)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 05:05 30/09/2026<br>**Prompt #13:** "Bạn lúc nãy đã thực hiện 1.1 và 1.2, vậy nên giúp mình điền vào 1.4 nhé: …" |
| (2) AI output | Nguyên văn ở Phụ lục A, #13. Trích: *"Số tin Manual / Automation / AI-QA / Khác: 4 / 1 / 3 / 1 + J01 [bạn tự phân loại]"*; *"Top 5 kỹ năng (/9, chưa tính J01)"*; bảng phân loại AI thay thế / hỗ trợ / không thay thế; đoạn nhận xét. |
| (3) Verdict | **INCOMPLETE** |
| (4) Reasoning | Số liệu tính trên 9 tin vì AI không có JD của J01, nên thống kê chưa đủ 10/10. Cách đếm kỹ năng là do AI tự diễn giải JD, cần tôi kiểm tra lại tiêu chí. Bảng phân loại có dẫn chứng theo từng mã tin, đối chiếu được với 1.2. |
| (5) Student fix | Xếp **J01 vào Automation** → 4 / **2** / 3 / 1. Đếm lại top 5 kỹ năng trên **/10** (Tiếng Anh, Automation, Lập trình: **8/10**). Rà lại đoạn nhận xét cho khớp với AI Impact Analysis đã tự viết ở 1.2. |

### A08 – Research và bảng 20 software defect (2.0, 2.1)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus (chế độ Research) · **Thời gian:** 05:16 và 07:02 30/09/2026<br>**Prompt #14:** "Giờ qua thực hiện requirement 2. Hãy giúp tôi research 'software defects publicized between 2022 and 2026.' Không bịa nguồn…"<br>**Prompt #15:** "Giờ hãy giúp tôi điền thông tin đầy đủ vào các form này nhé: …" |
| (2) AI output | Báo cáo research (Phụ lục A, #14) và file `appendix/ai-outputs/HW01_R2.md`: 20 defect (8 AI/LLM, 12 Non-AI), mỗi defect 1–2 nguồn; thống kê Critical 9 · High 9 · Medium 2 · Low 0; phần "Caveats" nêu các chỗ nguồn không thống nhất (Rogers, EchoLeak, Replit). |
| (3) Verdict | **INCOMPLETE** |
| (4) Reasoning | Tôi mở toàn bộ link và đối chiếu: số liệu khớp với nguồn. Tuy nhiên có 2 điểm chưa đạt: link thứ 2 của D16 (AOL) đã không còn truy cập được; và ô "Giải pháp" của D18 ghi chính quyền mới "dự định" gỡ chatbot, trong khi nguồn cập nhật 02/2026 cho biết chatbot đã bị gỡ. AI tự nêu độ tin cậy thấp hơn ở D20 và lý do không có defect mức Low. |
| (5) Student fix | D16: ghi chú **"link 2 đã hết hạn vào 30/09/2026, link 1 vẫn đủ thông tin"**. D18: ~~"dự định gỡ bỏ"~~ → **"Chính quyền Mamdani gỡ bỏ chatbot (02/2026), gọi nó là 'functionally unusable'"** (xác minh ở A09). |

### A09 – Giải thích D18 (Claude)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 07:06 30/09/2026<br>**Prompt #16:** "…Giờ mình muốn bạn giải thích thêm về 1 số thông tin của defect này (với mỗi ý, hãy ghi nguồn tham khảo): Sự cố được công bố vào ngày nào? Con số thiệt hại là bao nhiêu? …" (9 câu hỏi, nguyên văn ở Phụ lục A) |
| (2) AI output | Nguyên văn ở Phụ lục A, #16. Trích: *"Không có nguồn nào công bố thiệt hại… Con số duy nhất có nguồn là chi phí làm chatbot: gần 600.000 USD"*; *"Không có báo cáo nguyên nhân gốc chính thức"*; *"Hiện nay chatbot còn hoạt động không? Không… 'beta test has ended'"*. |
| (3) Verdict | **VALID** |
| (4) Reasoning | Tôi mở từng nguồn (The Markup 2024 và 2026, AP, Reuters, NYC Mayor's Office) và không tìm thấy thông tin sai. Với các câu hỏi không có dữ liệu (thiệt hại, số người bị ảnh hưởng, nguyên nhân gốc), AI trả lời "không có nguồn" thay vì đoán; đây là hành vi đúng khi thiếu test oracle. Vì không có hallucination nên lượt này không dùng được cho mục 2.2; tôi chuyển sang hỏi Gemini (A10). |
| (5) Student fix | Không sửa. Dùng các nguồn ở đây làm "đáp án chuẩn" để đối chiếu câu trả lời của Gemini. |

### A10 – Giải thích D18 (Gemini)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Gemini Flash · **Thời gian:** 08:08 30/09/2026<br>**Prompt #17:** cùng 9 câu hỏi như #16 (nguyên văn ở Phụ lục A) |
| (2) AI output | Ảnh khoanh đỏ: Hình 2.1 (`R2_defects/R2_ai_hallucination.png`). Câu sai: *"Người phát ngôn của Microsoft tuyên bố rằng họ cung cấp nền tảng kỹ thuật và hỗ trợ khách hàng thử nghiệm, nhưng việc kiểm soát nội dung và dữ liệu đầu vào thuộc trách nhiệm quản trị của thành phố."* |
| (3) Verdict | **INVALID** |
| (4) Reasoning | Không nguồn gốc nào có phát ngôn này. The Markup ghi Microsoft từ chối bình luận; AP ghi Microsoft nói đang làm việc cùng thành phố *"to improve the service and ensure the outputs are accurate and grounded on the city's official documentation"*. Gemini bịa một phát ngôn và gán cho nguồn cụ thể (hallucination), đồng thời làm lệch cán cân trách nhiệm từ "cùng sửa lỗi" thành "trách nhiệm của thành phố" (framing bias). Chi tiết ở mục 2.2. |
| (5) Student fix | Thay bằng phát ngôn thật của Microsoft theo AP, kèm link và ảnh khoanh đỏ (Hình 2.2). |

### A11 – Xác nhận hallucination (Claude)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 08:55 30/09/2026<br>**Prompt #18:** "Mình vừa hỏi Gemini với câu hỏi tương tự thì có thấy câu trả lời này: … Bạn nghĩ đây có phải là hallucination và có thêm bias gì nữa không?" |
| (2) AI output | Nguyên văn ở Phụ lục A, #18. Trích: *"Có, đây là hallucination… Gemini tạo ra một phát ngôn không tồn tại rồi gán cho một nguồn cụ thể"*; *"thành phố thực sự có trách nhiệm… Cái sai là gán kết luận đó cho Microsoft"*; *"mình không kết luận được Gemini 'cố ý bênh Microsoft'"*. |
| (3) Verdict | **VALID** |
| (4) Reasoning | AI xác nhận dựa trên nguồn gốc (The Markup, AP) và tự tìm thêm nguồn NBC New York để kiểm tra. AI cũng chỉ ra chỗ tôi hiểu quá mức: thành phố vẫn có trách nhiệm thật, cái sai là gán lời cho Microsoft. AI phân biệt rõ giữa sự thật có nguồn và giả thuyết về nguyên nhân (không kết luận Gemini cố ý). |
| (5) Student fix | Điều chỉnh cách viết ở 2.2: loại lỗi là **"Hallucination và framing bias"**; phần nguyên nhân ghi rõ là **giả thuyết**. |

### A12 – Bộ 15 test case quạt (bản gốc của AI)

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 18:48 29/09/2026<br>**Prompt #4:** "…Giờ mình sẽ làm bài 3, hiện tại mình chỉ có một cái quạt điện để test. Nó là Quạt Kakashi, Model: B300, chỉ có thể có các thao tác với chỗ làm cho quạt quay, hoặc đứng yên. Và các nút để mở quạt số 1, 2, 3 và tắt quạt số 0. Hãy giúp mình viết các test case để làm bài tập 3 nhé." |
| (2) AI output | File `appendix/ai-outputs/HW01_R3_TestCases_AI_Draft.md`: 5 giả định G1–G5, 15 TC (AI-TC01–AI-TC15), bảng lý do chọn input. AI ghi rõ: *"mình **không** tự nghĩ sẵn 3 edge case. Phần đó bạn phải tự tìm."* |
| (3) Verdict | **INCOMPLETE** |
| (4) Reasoning | Các TC bao phủ tốt luồng chức năng chính bằng EP (từng mức gió), state transition (chuyển số, nhảy cóc) và decision table (tốc độ × xoay) theo ISTQB CTFL v4.0.1 §4.2. Cả 5 giả định G1–G5 đúng với quạt thật. Nhưng bộ TC chỉ dùng input hợp lệ (mỗi lần 1 phím), không có TC nào cho thao tác nhiều phím cùng lúc hay lỗi phần cứng như dây lỏng; đây là vùng error guessing (§4.4.1) mà người dùng thật dễ gặp. AI-TC04 có expected "ghi lại thời gian dừng (s)" nhưng không có ngưỡng Pass/Fail, tức là thiếu test oracle. |
| (5) Student fix | Giữ 10 TC (xem bảng dưới), bỏ 5 TC trùng lặp hoặc tốn thời gian. **Thêm 5 edge case tự viết TC11–TC15.** Lược bỏ phép đo "dải giấy" ở TC01, TC02 vì không cần để kết luận. |

**Đánh giá từng TC do AI sinh:**

| TC của AI | Verdict | Lý do ngắn | Xử lý |
|---|---|---|---|
| AI-TC01 Bật số 1 | VALID | Expected đo được (≤ 3 s) | Giữ → **TC01** (lược dải giấy) |
| AI-TC02 Bật số 2 | VALID | Đúng nhưng trùng với AI-TC05 (1 < 2 < 3) | Loại (trùng lặp) |
| AI-TC03 Bật số 3 | VALID | Đúng | Giữ → **TC02** (lược dải giấy) |
| AI-TC04 Tắt từ số 3 | INCOMPLETE | "Ghi lại thời gian dừng" không có ngưỡng Pass/Fail | Giữ → **TC03** |
| AI-TC05 Tăng dần 1 < 2 < 3 | VALID | Có phép đo dB, so sánh được | Giữ → **TC04** |
| AI-TC06 Nhảy cóc 3 → 1 | VALID | State transition không liền kề | Giữ → **TC05** |
| AI-TC07 Nhảy cóc 1 → 3 | VALID | Đúng nhưng cùng loại với AI-TC06 | Loại (trùng kỹ thuật) |
| AI-TC08 Bật xoay | VALID | Có ngưỡng chênh chu kỳ ≤ 10% | Giữ → **TC06** |
| AI-TC09 Tắt xoay giữa hành trình | VALID | Đúng | Giữ → **TC07** |
| AI-TC10 Xoay ở số 3, kiểm tra 2 biên | VALID | Đúng nhưng cần dán mốc, tốn thời gian | Loại (ưu tiên thấp) |
| AI-TC11 Bật xoay khi quạt tắt | VALID | Giả định G3 đúng với quạt thật | Giữ → **TC08** |
| AI-TC12 Nhấn lại phím đang chọn | VALID | Đúng | Giữ → **TC10** |
| AI-TC13 Mất điện và có điện lại | VALID | Đúng, có ý an toàn | Giữ → **TC09** |
| AI-TC14 Chạy liên tục 30 phút | VALID | Đúng nhưng tốn 30 phút, phòng test đã 39°C | Loại (chi phí thời gian, an toàn) |
| AI-TC15 Đế không xê dịch | VALID | Đúng nhưng ít rủi ro với quạt bàn | Loại (ưu tiên thấp) |

> 📝 Gợi ý (xóa trước khi nộp): TC03 trong bảng 3.3 vẫn giữ expected "Ghi lại thời gian dừng (s)". Nếu muốn ô (5) "Student fix" có thay đổi thật, nên thêm ngưỡng do bạn tự chọn, ví dụ "dừng hẳn trong ≤ 10 s" (actual 6 s → Pass). Expected của TC08 còn ghi "(theo G3)" – bảng 3.2 của bạn dùng mã F3, nên sửa thành "(theo F3)".

### A13 – Phản hồi của AI về edge case của SV

| Mục | Nội dung |
|---|---|
| (1) Prompt + tool | **Tool:** Claude Opus · **Thời gian:** 23:44 29/09/2026<br>**Prompt #5:** "[bảng TC11–TC15] Tôi đã nghĩ ra và thử các edge case trên. Hãy thành thật là: Bạn có suy nghĩ ra không, vì sao bỏ sót." |
| (2) AI output | Nguyên văn ở Phụ lục A, #5. Trích: *"Phần mình đã nghĩ tới nhưng không đưa vào: ý chung 'nhấn 2 phím cùng lúc'… Nên với TC11 và TC12, nói 'AI không tìm ra' là không chính xác. Đúng hơn là 'AI không đưa vào output'."*; *"Phần mình không nghĩ tới: nhấn nhanh khác với nhấn giữ… Dây hoặc phích tiếp xúc chập chờn (TC15)."* |
| (3) Verdict | **VALID** |
| (4) Reasoning | AI trả lời trung thực, tách rõ phần đã nghĩ nhưng không đưa vào output với phần hoàn toàn không nghĩ tới. Các góp ý (định lượng thời gian nhấn, đặt tiêu đề TC15 trung lập, cô lập nguyên nhân bằng cách đổi ổ cắm) đúng với nguyên tắc viết test case rõ ràng, tái hiện được (CTFL v4.0.1 §5.5 defect management). Điều này cho thấy "output của AI" không phản ánh hết những gì AI "biết". |
| (5) Student fix | TC11, TC12: thêm **"(dưới 0.5s)"** vào bước nhấn. TC15: tiêu đề ~~"Quạt đang chạy thì đụng dây, làm quạt bị tắt…"~~ → **"Quạt duy trì hoạt động dù bị tác động nhẹ ở dây nguồn"**. Ghi nhận ở 3.4: TC11–TC12 là "AI có nghĩ nhưng không đưa vào output". |

---

### 4.x Tổng kết độ chính xác của AI

**Theo artifact (13 artifact):**

| Verdict | Số lượng | Tỉ lệ |
|---|---|---|
| VALID | 5 (A01, A02, A09, A11, A13) | 38,5% |
| INVALID | 1 (A10 – Gemini) | 7,7% |
| INCOMPLETE | 7 (A03–A08, A12) | 53,8% |
| **Tổng** | 13 | 100% |

**Theo từng test case của AI (15 TC, A12):** VALID 14 (93,3%) · INVALID 0 (0%) · INCOMPLETE 1 (6,7%). Tuy nhiên 0/5 edge case thực tế nằm trong output của AI.

**Nhận xét:** AI hầu như không sai khi có nguồn để bám (A02, A08, A09), nhưng thường chưa đủ: thiếu dữ liệu nằm sau đăng nhập (lương, LinkedIn), thiếu thông tin mới cập nhật (D18), và thiếu kịch bản phụ thuộc thiết bị thật. Lỗi nghiêm trọng duy nhất (INVALID) xảy ra khi AI trả lời mà không bị buộc trích nguồn nguyên văn (Gemini, A10).

**Khi nào NÊN dùng AI cho bài này:**
- Dựng khung báo cáo, bảng biểu, checklist nộp bài.
- Tìm kiếm và gom nguồn ban đầu (tin tuyển dụng, defect) – với điều kiện tự mở lại từng link.
- Sinh bộ test case nền cho luồng chức năng chính (happy path, chuyển trạng thái).
- Review câu chữ, phát hiện lỗi trình bày và lỗi logic trong bảng.

**Khi nào KHÔNG NÊN dùng AI (hoặc phải kiểm chứng 100%):**
- Phát ngôn, con số, ngày tháng, nguyên nhân gốc của sự cố – phải có nguồn nguyên văn.
- Thông tin sau đăng nhập hoặc thay đổi theo thời gian (lương, ngày đăng, trạng thái hiện tại của sản phẩm).
- Edge case phụ thuộc thiết bị thật, độ mòn, dung sai cơ khí.
- Phân tích và kết luận được chấm điểm (AI Impact Analysis, AI Critique) và mọi artifact trong danh sách cấm (ảnh, video, screenshot, prompt log).
