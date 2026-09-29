# Prompt Log – HW01
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude

---

## #1 | 14:32 29/09/2026 | Claude Opus | R3
**Mục đích:** Sinh test case nháp cho quạt điện

**Prompt:**
```
Sinh 15 test case cho quạt đứng <hãng> <model>, 3 mức gió, có xoay,
không remote. Mỗi TC gồm Objective, Input, Steps, Expected.
```

**Output:**
```
TC01: Kiểm tra bật quạt ở mức 1
...
```

**Xử lý:** Giữ TC01–TC08 (VALID). TC09 sai vì quạt không có hẹn giờ
(INVALID). TC11 thiếu bước kiểm tra độ rung (INCOMPLETE, đã sửa).
→ AI-02 Artifact #3

---

## #1 | 17:38 29/09/2026 | Claude Opus | General
**Mục đích:** Đưa context bài tập cho AI để viết format report

**Prompt:**
```
Bạn là một Software Testing Senior có nhiều năm kinh nghiệm, đang hỗ trợ mình suy nghĩ và hoàn thành bài tập.
Hiện tại mình đang thực hiện bài tập với yêu cầu: tìm hiểu các job description, tìm các case defect, vẽ roadmap và thực hiện test trên một thiết bị vật lý. Yêu cầu được ghi rõ trong file mình đưa.
Hãy giúp mình từng bước hoàn thành bài tập. HIện tại mình đã viết xong dàn ý cơ bản cho report của bài. Giờ mình cần bạn nắm context, sau đó mình sẽ đưa dàn ý bài để bạn bổ sung cho dàn ý đầy đủ (tức là mình chỉ cần điền vào các ô trống), sau khi dàn ý đầy đủ, mình sẽ làm bài tập 3.
```
*Đính kèm*: file yêu cầu đề.

**Output:**
```
Mình sẽ đọc file đề bài để nắm yêu cầu trước.

Mình đã đọc xong đề. Tóm tắt ngắn gọn phần cần nắm, kèm vài điểm dễ bị trừ điểm mà bạn nên để ý khi bổ sung dàn ý.

## Cấu trúc bài HW01

| Phần | Điểm | Cần nộp |
|---|---|---|
| R1: Thị trường việc làm QA/QC | 40 | 10 tin tuyển dụng đăng trong vòng 60 ngày trước ngày nộp, trong đó ≥3 tin yêu cầu kỹ năng AI/LLM. Mỗi tin có link, ảnh chụp có ngày và tên tài khoản của bạn, JD, kỹ năng, lương, và 1–2 câu "AI Impact Analysis". |
| R2: 20 defect (2022–2026) | 20 | ≥5 defect liên quan AI/LLM. Mỗi defect có nguồn, mô tả, severity, hậu quả, cách xử lý. Thêm 1 chỗ AI bị bias hoặc hallucinate khi giải thích defect. |
| R3: Test thiết bị vật lý | 25 | Ảnh thiết bị chụp chung với thẻ SV, thông tin brand/model/năm/serial (che 4 ký tự giữa), 15 TC, ≥3 edge case mà AI không tìm ra, chạy thật ≥5 TC và quay video ≤60s có giọng bạn thuyết minh. |
| AI-1/2/3 | 15 | Audit Report 5 mục cho mỗi artifact, AI Critique 200–300 từ, Disclosure, checklist AI-05 |

## Những điểm dễ sót

1. **Điểm R3 không khớp nhau.** Phần mô tả ghi 40 điểm, còn rubric ghi 25 điểm. Rubric cộng lại đúng 100 (40+20+25+15), nên có lẽ con số 40 là tính cả phần AI compliance. Bạn nên hỏi lại TA cho chắc.
2. **Mindmap không nằm trong gạch đầu dòng nào.** Bảng CLO G9.1 yêu cầu dùng AI vẽ mindmap vai trò QA/QC rồi tìm 3 lỗi của nó, nhưng 3 yêu cầu R1–R3 không nhắc đến. Dàn ý nên có mục riêng cho phần này, đặt trong R1.
3. **Cần screenshot bug trên FIT Mantis**, kèm ảnh trang chủ Mantis hiện username là MSSV. Với HW01, bug này hợp lý nhất là lấy từ các TC bị Fail ở R3. Vì vậy trong 5 TC chạy thật, nên cố tìm ít nhất 1 TC Fail.
4. **Cần file Excel** gồm Test Cases, Checklist và Test Summary Report. Cột Actual/Verdict phải điền từ kết quả chạy thật, không được để trống.
5. **Phải chứng minh được ≥3 edge case là do bạn tìm.** Cách làm là cho AI sinh TC trước, lưu lại prompt log có timestamp, sau đó mới thêm edge case của bạn và đánh dấu rõ. Audit Report cũng cần làm theo trình tự này.
6. **Các thứ cấm dùng AI tạo ra**: ảnh thiết bị kèm thẻ SV, giọng thuyết minh video, screenshot tin tuyển dụng, prompt log. Nếu bị phát hiện thì cả bài 0 điểm.
7. **Thi vấn đáp ngẫu nhiên.** Bạn có thể bị hỏi vì sao chọn input X mà không phải Y, nên mỗi TC ở R3 nên ghi kèm lý do chọn input, ví dụ theo kỹ thuật BVA, EP hay state transition.
8. **Cuối report cần có**: tỉ lệ VALID/INVALID/INCOMPLETE của AI, kết luận khi nào nên hoặc không nên dùng AI, và phần self-assessment.

Bạn gửi dàn ý đi, mình sẽ bổ sung thành khung đầy đủ để bạn chỉ cần điền vào các ô trống.
```

**Xử lý:** Đọc và gửi tiếp file dàn ý report để hoàn thiện dàn ý report.

---

## #2 | 17:41 29/09/2026 | Claude Opus | General
**Mục đích:** Hoàn thiện dàn ý cơ bản

**Prompt:**
```
Đây là dàn ý hiện tại của tôi, chỉ có các đề mục. Giờ tôi muốn bạn giúp tôi hoàn thiện dàn ý (như là vẽ bảng trước các chỗ cần vẽ, list những yêu cầu viết chi tiết, placeholder cho những chỗ cần ảnh minh chứng,...)
Sau khi viết xong, output ra lại file .md giúp tôi
```
*Đính kèm:* file report đã viết dàn ý cơ bản 
**Output:**
```
Mình đã làm xong file `.md` từ dàn ý của bạn. Các đề mục gốc vẫn giữ nguyên, mình chỉ thêm bảng, chỗ chèn ảnh và hướng dẫn viết cho từng mục.

**Mình có thêm 3 mục mới** so với dàn ý ban đầu, nên số thứ tự phần 3 bị dịch:
- **1.4 Tổng hợp xu hướng thị trường.** Đề có yêu cầu phân biệt việc AI thay thế, hỗ trợ và không thay thế được. Dàn ý cũ chưa có chỗ nào cho yêu cầu này.
- **3.2 Phạm vi và chiến lược kiểm thử.** Mục này ghi chức năng thiết bị, kỹ thuật thiết kế test và những gì nằm ngoài phạm vi. Nhờ đó bạn có căn cứ để trả lời khi bị hỏi vấn đáp "vì sao chọn input X".
- **Phụ lục D.** Cấu trúc thư mục zip, liệt kê các file mà đề bắt buộc nộp.

Các mục cũ 3.2–3.5 giờ thành 3.3–3.6.

**Một số quy ước trong file:**
- Chỗ nào ghi `[...]` là ô bạn cần điền.
- Ảnh được chèn bằng `![...](images/...)`, bạn đặt ảnh vào thư mục `images/` đúng tên file là được.
- Mục nào có biểu tượng 🔒 thì bắt buộc tự làm, không được dùng AI tạo.
- Các khối hướng dẫn có biểu tượng 📝, nhớ xóa hết trước khi xuất PDF.
- Mỗi prompt gửi AI được gán một mã P01, P02… Mã này dùng chung cho bài, Audit Report và prompt log, nên khi đối chiếu sẽ khớp nhau.

**Chuẩn bị cho bài 3:** bạn nên cho AI sinh test case trước và lưu lại prompt kèm output. Sau đó bạn mới tự tìm edge case. Làm theo thứ tự này thì mới chứng minh được 3 edge case là của bạn, và AI đã bỏ sót chúng.

Khi bạn chọn xong thiết bị cho bài 3, gửi mình loại thiết bị và model nhé.
```
**Xử lý:** Lấy file dàn ý mà Claude đã hoàn thiện rồi viết tiếp

---

## #3 | 18:34 29/09/2026 | Claude Opus | General
**Mục đích:** Xác định brainstorm lại có nên bỏ mục 1.4 mà Claude vừa thêm hay không

**Prompt:**
```
Về phần "Tổng hợp xu hướng thị trường", ban đầu mình dự định cho mỗi cái phân biệt "AI thay thế, hỗ trợ, và không thay thế được" ở trong bảng 1.1 và chi tiết 1.2 cho từng cái luôn. Vậy theo bạn mình có nên bỏ 1.4 mới của bạn đi không?
```

**Output:**
```
Mình nghĩ bạn không cần bỏ hẳn 1.4, nhưng nên cắt bớt.

Bảng phân loại "thay thế / hỗ trợ / không thay thế" trong 1.4 đúng là trùng với dòng AI Impact Analysis ở 1.2, vì template 1.2 mình làm đã tách sẵn 3 ý này cho từng tin. Bảng đó nên bỏ.

Phần còn lại của 1.4 vẫn đáng giữ, vì đề có outcome "mô tả bức tranh thị trường QA/QC 2026+", mà 10 tin rời rạc thì chưa cho thấy được bức tranh chung. Bạn chỉ cần một bảng thống kê nhỏ (số tin theo từng loại, dải lương, top kỹ năng, số tin yêu cầu AI) và 3–5 câu kết luận rút ra từ 10 tin. Viết phần này mất khoảng 15 phút, và bạn tự viết được hoàn toàn mà không cần dùng AI.

Về bảng 1.1, mình không khuyên nhồi cả 3 nhóm phân loại vào đó, vì bảng đã có 10 cột, thêm nữa sẽ bị vỡ khi xuất PDF. Nếu muốn nhìn nhanh, bạn chỉ nên thêm một cột ngắn như "Mức tác động AI: Cao / TB / Thấp", còn phần phân tích chi tiết vẫn để ở 1.2.

Tóm lại mình đề xuất:
- **1.1:** giữ nguyên, có thể thêm một cột "Mức tác động AI".
- **1.2:** giữ AI Impact tách 3 ý như hiện tại.
- **1.4:** đổi tên thành "Tổng kết", chỉ giữ bảng thống kê và đoạn kết luận, bỏ bảng phân loại.

Nếu bạn đồng ý thì mình sửa lại file luôn nhé.
```

**Xử lý:** Đọc output của Claude và xác định thêm 1.4 là hợp lý, đồng thời, thấy không cần phải bỏ bảng phân loại.

---

## #1 | 14:32 29/09/2026 | Claude Opus | R3
**Mục đích:** Sinh test case nháp cho quạt điện

**Prompt:**
```
Sinh 15 test case cho quạt đứng <hãng> <model>, 3 mức gió, có xoay,
không remote. Mỗi TC gồm Objective, Input, Steps, Expected.
```

**Output:**
```
TC01: Kiểm tra bật quạt ở mức 1
...
```

**Xử lý:** Giữ TC01–TC08 (VALID). TC09 sai vì quạt không có hẹn giờ
(INVALID). TC11 thiếu bước kiểm tra độ rung (INCOMPLETE, đã sửa).
→ AI-02 Artifact #3

---

## #1 | 14:32 29/09/2026 | Claude Opus | R3
**Mục đích:** Sinh test case nháp cho quạt điện

**Prompt:**
```
Sinh 15 test case cho quạt đứng <hãng> <model>, 3 mức gió, có xoay,
không remote. Mỗi TC gồm Objective, Input, Steps, Expected.
```

**Output:**
```
TC01: Kiểm tra bật quạt ở mức 1
...
```

**Xử lý:** Giữ TC01–TC08 (VALID). TC09 sai vì quạt không có hẹn giờ
(INVALID). TC11 thiếu bước kiểm tra độ rung (INCOMPLETE, đã sửa).
→ AI-02 Artifact #3

---

## #1 | 14:32 29/09/2026 | Claude Opus | R3
**Mục đích:** Sinh test case nháp cho quạt điện

**Prompt:**
```
Sinh 15 test case cho quạt đứng <hãng> <model>, 3 mức gió, có xoay,
không remote. Mỗi TC gồm Objective, Input, Steps, Expected.
```

**Output:**
```
TC01: Kiểm tra bật quạt ở mức 1
...
```

**Xử lý:** Giữ TC01–TC08 (VALID). TC09 sai vì quạt không có hẹn giờ
(INVALID). TC11 thiếu bước kiểm tra độ rung (INCOMPLETE, đã sửa).
→ AI-02 Artifact #3

---

## #1 | 14:32 29/09/2026 | Claude Opus | R3
**Mục đích:** Sinh test case nháp cho quạt điện

**Prompt:**
```
Sinh 15 test case cho quạt đứng <hãng> <model>, 3 mức gió, có xoay,
không remote. Mỗi TC gồm Objective, Input, Steps, Expected.
```

**Output:**
```
TC01: Kiểm tra bật quạt ở mức 1
...
```

**Xử lý:** Giữ TC01–TC08 (VALID). TC09 sai vì quạt không có hẹn giờ
(INVALID). TC11 thiếu bước kiểm tra độ rung (INCOMPLETE, đã sửa).
→ AI-02 Artifact #3

---