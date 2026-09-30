# Prompt Log – HW01
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude, Gemini

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

**Output:** File `23120255_HW01_Report.md` do AI tạo, lưu nguyên bản tại
`ai-outputs/23120255_HW01_Report.md`
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

## #4 | 18:48 29/09/2026 | Claude Opus | R3
**Mục đích:** Xác định không cần thay đổi dàn ý và sinh test case cho quạt điện

**Prompt:**
```
Mình nghĩ là không cần bỏ bảng phân loại, cấu trúc hiện tại ổn rồi. Giờ mình sẽ làm bài 3, hiện tại mình chỉ có một cái quạt điện để test. Nó là Quạt Kakashi, Model: B300, chỉ có thể có các thao tác với chỗ làm cho quạt quay, hoặc đứng yên. Và các nút để mở quạt số 1, 2, 3 và tắt quạt số 0. Hãy giúp mình viết các test case để làm bài tập 3 nhé.
```

**Output:** File `HW01_R3_TestCases_AI_Draft.md` do AI tạo, lưu nguyên bản tại
`ai-outputs/HW01_R3_TestCases_AI_Draft.md`
```
Mình viết bộ test case cho quạt ngay đây. Có một điểm quan trọng: bộ này chính là output của AI trong bài của bạn, nên mình **không** tự nghĩ sẵn 3 edge case. Phần đó bạn phải tự tìm thì mới đạt yêu cầu G9.3.

Mình đã viết xong 15 test case cho quạt Kakashi B300, kèm cột lý do chọn input và gợi ý chọn TC để quay video. Bản này chưa chạy thật trên quạt, nên các cột Actual và Verdict vẫn để trống.

Một số việc bạn cần làm với bản này:

1. **Lưu prompt và output ngay.** Bạn ghi prompt vừa rồi và file này vào prompt log, có timestamp. Đây là bằng chứng output gốc của AI (mục A05 trong Audit Report). Sau này bạn cần nó để chứng minh edge case của bạn không có trong output của AI.

2. **Kiểm tra 5 giả định G1–G5 với quạt thật.** Mình đoán cách điều khiển xoay là núm nhấn/kéo trên đỉnh motor, và xoay chạy chung motor với cánh. Nếu quạt của bạn khác thì TC08–TC11 sẽ thành INVALID. Những chỗ sai kiểu này bạn có thể ghi luôn vào Audit Report.

3. **Tự đánh giá từng TC** là VALID, INVALID hay INCOMPLETE. Ví dụ, expected của TC04 ("ghi lại thời gian dừng") chưa có ngưỡng Pass/Fail. Kiểu thiếu sót này tính là INCOMPLETE.

4. **Tự tìm ít nhất 3 edge case rồi thay vào chỗ 3 TC của AI**, để tổng vẫn là 15. Nên bỏ những TC yếu nhất, ví dụ TC12 hoặc TC15. Mình cố ý không gợi ý edge case nào. Nếu mình gợi ý thì chúng thành edge case do AI tìm, và bạn mất điểm G9.3. Cách tìm là thao tác thật với quạt nhiều lần, rồi để ý những chỗ phím hay núm phản ứng lạ.

5. **Không mở vỏ quạt**, không cho vật gì vào lưới, và không để tay gần cánh khi test.

Khi bạn chạy thử và có kết quả, hoặc đã review xong, gửi mình để làm tiếp file Excel (Test Cases, Checklist, Test Summary) và phần Audit Report cho R3.
```

**Xử lý:** Đọc file, đưa các test case của AI vào báo cáo, tự nghĩ thêm các edge case rồi bỏ đi các case không cần thiết cho AI sinh ra.

---

## #5 | 23:44 29/09/2026 | Claude Opus | R3
**Mục đích:** Kiểm chứng và hỏi AI tại sao không nghĩ ra các edge case mà mình vừa nghĩ ra

**Prompt:**
```
```markdown
| TC11 | Ấn phím số 1 và phím số 2 cùng lúc rồi thả ra cùng lúc |  Quạt đặt trên mặt bàn phẳng, khô, đã cắm điện 220V. Phím ở 0, xoay tắt, đầu quạt hướng thẳng. Phòng không bật quạt/điều hòa khác. | Phím 1 và phím 2 | 1. Nhấn phím 1 và phím 2 rồi thả ra<br>2. Quan sát 10 s | Quạt quay nhẹ, sau khi thả ra thì quạt dừng lại, các phím đều về trạng thái ban đầu  | Ngay lúc ấn thì quạt quay nhẹ, sau khi thả ra thì quạt dừng lại, các phím đều về trạng thái ban đầu | Pass | Tự viết (edge case) |
| TC12 | Ấn một lúc 2 phím khác khi quạt đang chạy | Quạt ở số 1, xoay tắt | Phím 2 và phím 3 | 1. Nhấn phím 2 và phím 3<br>2. Quan sát 10 s | Tất cả các phím đều tắt, quạt ngừng quay | Phím 1 bị nảy lên (tắt), phím 2 và phím 3 cũng trở về trạng thái ban đầu, quạt bắt đầu ngừng quay | Pass | Tự viết (edge case) |
| TC13 | Ấn và giữ phím số 1 và phím số 2 cùng lúc, sau đó thả ra cùng lúc |  Quạt đặt trên mặt bàn phẳng, khô, đã cắm điện 220V. Phím ở 0, xoay tắt, đầu quạt hướng thẳng. Phòng không bật quạt/điều hòa khác. | Phím 1 và phím 2 |1. Nhấn và giữ phím 1 và phím 2 cùng lúc<br>2. Giữ nguyên và quan sát trong 10s<br>3. Thả ra và quan sát trong 10s | Lúc nhấn và giữ phím thì quạt chạy, thả ra thì các phím về trạng thái ban đầu, quạt ngừng quay | Ngay lúc nhấn và giữ phím thì quạt chạy, sau khi thả ra thì quạt ngừng chạy, các phím cũng về vị trí ban đầu | Pass | Tự viết (edge case) |
| TC14 | Ấn và giữ phím số 2 và phím số 3 cùng lúc, sau đó thả ra cùng lúc |  Quạt đặt trên mặt bàn phẳng, khô, đã cắm điện 220V. Phím ở 0, xoay tắt, đầu quạt hướng thẳng. Phòng không bật quạt/điều hòa khác. | Phím 2 và phím 3 | 1. Nhấn và giữ phím 2 và phím 3 cùng lúc<br>2. Giữ nguyên và quan sát trong 10s<br>3. Thả ra và quan sát trong 10s | Lúc nhấn và giữ phím thì quạt chạy, thả ra thì các phím về trạng thái ban đầu, quạt ngừng quay | Ngay lúc nhấn và giữ phím thì quạt chạy, sau khi thả ra thì quạt vẫn tiếp tục chạy, cả 2 phím 2 và 3 đều ở trạng thái bật | Fail | Tự viết (edge case) |
| TC15 | Quạt đang chạy thì đụng dây, làm quạt bị tắt mặc dù ổ cắm vẫn trong ổ |  Quạt ở số 1, xoay tắt | Dây điện của quạt | 1. Quan sát ổ cắm ban đầu 5s<br>2. Đụng dây điện rồi quan sát quạt<br>3. Quan sát lại ổ cắm  | Ban đầu quạt chạy bình thường, ổ cắm cũng bình thường, sau khi đụng dây điện nhẹ thì quạt vẫn chạy, nhìn lại ổ cắm vẫn trong ổ bình thường. | Ban đầu quạt chạy bình thường, ổ cắm cũng bình thường, sau khi đụng dây điện nhẹ thì quạt tắt, nhìn lại ổ cắm vẫn trong ổ bình thường. | Fail | Tự viết (edge case) |

Tôi đã nghĩ ra và thử các edge case trên.
Hãy thành thật là: Bạn có suy nghĩ ra không, vì sao bỏ sót. (vì mình không thấy bạn đưa vào trong test case)
```

**Output:**
```
Nói thật là có một phần mình đã nghĩ tới, còn phần lớn thì không.

**Phần mình đã nghĩ tới nhưng không đưa vào:** ý chung "nhấn 2 phím cùng lúc". Lúc viết bộ TC, mình có cân nhắc kiểu thao tác này rồi cố ý bỏ ra, vì đã nói trước là sẽ không gợi ý edge case để bạn tự tìm. Nên với TC11 và TC12, nói "AI không tìm ra" là không chính xác. Đúng hơn là "AI không đưa vào output". Prompt log của bạn vẫn là bằng chứng hợp lệ về output, nhưng bạn nên ghi rõ điểm này trong Audit Report hoặc AI Critique. Đây lại là một nhận xét hay: output của AI không phản ánh hết những gì AI "biết", và AI có thể tự lọc bớt kết quả theo ngữ cảnh.

**Phần mình không nghĩ tới:**
- **Nhấn nhanh khác với nhấn giữ (TC11 so với TC13), và kết quả phụ thuộc cặp phím (TC13 so với TC14).** Việc cặp 2+3 bị kẹt cả hai phím còn cặp 1+2 thì không, mình không đoán được. Đây là dung sai cơ khí của riêng chiếc quạt này.
- **Dây hoặc phích tiếp xúc chập chờn (TC15).** Mình chỉ nghĩ tới việc rút hẳn phích (TC13 cũ), không nghĩ tới trường hợp phích vẫn cắm mà điện vẫn mất.

**Vì sao mình bỏ sót:**
1. Mình không có thiết bị thật. Mình suy luận từ một mô hình "quạt phím piano chung chung", nên những lỗi phụ thuộc độ mòn, dung sai hay tuổi thọ của đúng chiếc quạt này nằm ngoài khả năng của mình.
2. Mình thiết kế test chủ yếu theo đặc tả, với các input hợp lệ (mỗi lần 1 phím). Các lớp input không hợp lệ và thao tác vụng về của người dùng thật bị ưu tiên thấp.
3. Mình có xu hướng liệt kê những kịch bản "phổ biến" hay có trong tài liệu. Lỗi dây lỏng là vấn đề phần cứng xuống cấp, không nằm trong chức năng của quạt nên mình không nghĩ tới.

**Góp ý về 5 TC của bạn:**
- **Expected đang giống hệt Actual (TC11, TC13).** Nhìn vào dễ bị cho là viết expected sau khi đã chạy. Expected phải có oracle trước khi chạy. Ví dụ, cơ cấu khóa liên động của phím piano thì expected hợp lý là "không phím nào bị giữ, quạt không chạy" hoặc "chỉ 1 phím được giữ". Viết "quạt quay nhẹ" làm expected thì không có căn cứ.
- **TC11 và TC13 cần định lượng.** Ví dụ: nhấn nhanh dưới 0,5 giây, còn nhấn giữ là 10 giây. Nếu không, TA sẽ thấy hai TC này trùng nhau.
- **TC14 Fail là bug tốt, nên log lên Mantis với severity High.** Khi 2 phím tốc độ cùng được giữ, có thể 2 đầu dây cuộn motor đang được cấp điện cùng lúc, dễ gây quá nhiệt. Đừng để quạt chạy lâu ở trạng thái này.
- **TC15 cần sửa mấy chỗ:**
  - *Tiêu đề:* đang mô tả luôn lỗi. Nên đổi thành mục tiêu trung lập, ví dụ "Quạt duy trì hoạt động khi dây nguồn bị tác động nhẹ".
  - *Tái hiện:* ghi rõ chạm vào vị trí nào (gần phích hay gần chân đế), đẩy dây xa bao nhiêu cm, và lặp mấy lần ra lỗi mấy lần (ví dụ 4/5).
  - *Cô lập nguyên nhân:* cắm sang ổ khác rồi thử lại. Nếu vẫn lỗi thì là lỗi của quạt, nếu hết lỗi thì là lỗi của ổ điện nhà bạn, không phải defect của sản phẩm. Phải làm bước này thì mới log Mantis được.
  - *An toàn:* tiếp xúc chập chờn có thể gây tia lửa điện. Chỉ nên thử vài lần để ghi nhận, rồi đừng dùng quạt ở ổ đó nữa.
- **Thiếu cột "Kỹ thuật".** Có thể ghi: TC11–TC14 là Error guessing kết hợp EP với lớp input không hợp lệ (nhiều phím), TC15 là Error guessing (lỗi phần cứng/môi trường).

Muốn vững khi bị hỏi vấn đáp, bạn nên chọn TC14 và TC15 làm edge case chính, vì mình hoàn toàn không nghĩ tới hai trường hợp này. TC13 có thể làm edge case thứ ba, vì mình không lường trước được sự khác biệt giữa nhấn nhanh và nhấn giữ.
```

**Xử lý:** Hoàn thiện các edge case vừa viết theo Claude vì có vẻ nó chưa tốt lắm

---

## #6 | 00:27 30/09/2026 | Claude Opus | R1
**Mục đích:** Thực hiện requirement 1, tìm các link về job có yêu cầu AI/LLM/AI-assisted automation mà mình tìm chưa ra

**Prompt:**
```
Tôi đã viết xong Requirement 3 rồi. Giờ tôi muốn làm tiếp Requirement 1.
Hiện tại tôi đã tìm được các link qua các platform:

1. https://www.linkedin.com/jobs/search-results/?currentJobId=4193261952&eBP=CwEAAAGg7cSmFgM1lRNlcB2BYUipAWbYl4s3ALmp_tzwZBnQ2qVwbUdmmMYYJRudYTKrY_8qHT6TvVuEgIb1zhPeorxMD7Lw-j9eFcxyxwMk6VW0QV1tQOCxRD2-f9_HKYMtiP6gDiM7RXBULuiRTyDQ7z86ENllBtRNvHc6ZqE9gBeZ1pe7wBxtOUv336H8wZC4R4RiLLwwMX_Otj8QUyvzaJn3H-fQt_vODCdWcJkaQEVfsZeG0Kg3HgPzqkyfEBFCks4eSajPCvjdOjx0EPBYDC1zkFIM4IrpD5fsE7IwUTGrTZfcXgvjoV1POw8bpz5r6jo6VqG1cf9OwC3I-VL2wfnsaMg54d6SNo5CyOcGhadI0jHyc9ZpBRrbtQlgPVZuUAqJJTjzgRkZi2_PLToE-1HBYhXd0ku5ManGCg18OUwbYKXmIYxSXAepTmRcY_aGkAQo4MEWXuM71e6xyRD5XmYfv9GHhl-I634InvSN&refId=WJZ2qDVtj1akBj37TK1MLw%3D%3D&trackingId=76ACJZvSqhJ9EpOYCZramw%3D%3D&keywords=Software%20Tester&origin=SEMANTIC_SEARCH_LANDING_PAGE
2. https://www.topcv.vn/viec-lam/software-testing-lead/2302520.html?ta_source=JobSearchList_LinkDetail&u_sr_id=IAo5dajlmSZENgw7YbEeqNugFPV1UUL9lmRRxeSi_1790695848
3. https://itviec.com/it-jobs/qa-engineer-tester-qa-qc-ol-vietnam-3927?lab_feature=preview_jd_page
4. https://itviec.com/it-jobs/manual-tester-qa-qc-good-english-netcompany-2659?lab_feature=preview_jd_page
5. https://itviec.com/it-jobs/software-test-automation-engineer-motorola-solutions-1324?lab_feature=preview_jd_page
6. https://itviec.com/it-jobs/quality-control-intern-software-tester-phu-hung-securities-phs-1247?lab_feature=preview_jd_page
7. https://itviec.com/it-jobs/senior-middle-automation-test-qa-qc-8seneca-1756?lab_feature=preview_jd_page (có yêu cầu AI/LLM/AI-assisted automation.)
8. https://itviec.com/it-jobs/automation-tester-qa-qc-tester-japanese-n3-trustedai-2550?lab_feature=preview_jd_page ("ứng dụng AI vào các tác vụ test")

Hiện tại tôi đang cố tìm các jd có "yêu cầu AI/LLM/AI-assisted automation.", nhưng tìm không ra. Bạn giúp tôi tìm thêm 2 cái nữa nhé
```

**Output:**
```
Mình sẽ tìm thêm tin tuyển dụng QA/QC có yêu cầu AI/LLM, đăng trong khoảng 60 ngày gần đây.

Có 3 tin nhìn khá phù hợp. Mình sẽ mở từng tin để xác minh nội dung yêu cầu AI.

Mình tìm được 2 tin phù hợp trên ITviec, đều ghi rõ yêu cầu AI/LLM trong JD. Ngoài ra có thêm 1 tin dự phòng.

**1. QA Engineer (Claude Code, Python, React, Manual Tester) — Brarista** (Nên chọn)
- Link: https://itviec.com/it-jobs/qa-engineer-claude-code-python-react-manual-tester-brarista-4435
- Làm remote, nhận ứng viên ở HCM, Đà Nẵng và Hà Nội. Tin đăng khoảng 22 ngày trước (tính đến 30/09), nên vẫn trong khoảng 60 ngày.
- Yêu cầu AI được ghi thẳng: *"You'll use Claude Code to generate exhaustive test matrices, build regression suites..."* và *"You're excellent with Claude Code, and you can prove it."* Công ty cũng ghi phần lớn code do AI viết và có người review.
- Tin này hợp cho phần AI Impact vì cho thấy rõ vai trò mới của tester. AI lo việc sinh test matrix. Tester lo kiểm tra lại tag sản phẩm do AI gợi ý, và chịu trách nhiệm chất lượng bản release.

**2. [Hanoi] Fullstack QA Engineer Lead (Manual, Auto, AI) — Money Forward Vietnam** (Nên chọn)
- Link: https://itviec.com/it-jobs/hanoi-fullstack-qa-engineer-lead-manual-auto-ai-money-forward-vietnam-co-ltd-4636
- Làm tại Hà Nội, tin mới đăng.
- Yêu cầu AI: *"Lead the team in adopting Generative AI tools (Cursor, GitHub Copilot, LLM assistants) to accelerate test design, script generation, and triage"*, *"exploratory testing and output validation for AI-assisted product features (chatbots, agents...)"*, và đặt ra hướng dẫn dùng AI an toàn cho team.
- Tin này có cả hai chiều: **dùng AI để test** và **test sản phẩm AI**. Viết AI Impact Analysis từ tin này sẽ rất dễ.

**Dự phòng: Lead Penetration Tester (Web, API & AI Applications) — Galaxy Holdings**
- Link: https://itviec.com/it-jobs/lead-penetration-tester-web-api-ai-applications-galaxy-holdings-4535
- Làm tại HCM, tin đăng khoảng 1 ngày trước. Yêu cầu kiểm thử prompt injection, rò rỉ dữ liệu qua RAG và OWASP Top 10 for LLM. Tin này lại nối được với các defect AI ở R2.
- Nhược điểm: đây là vị trí security testing, không hẳn là QA/QC. Chỉ nên dùng khi một trong hai tin trên bị gỡ.

**Những điểm cần lưu ý:**
- Mức lương trên ITviec chỉ hiện khi đăng nhập. Bạn vẫn phải đăng nhập để screenshot có tên tài khoản, nên lúc đó điền luôn lương.
- Nên chụp screenshot sớm, vì tin có thể bị gỡ trước deadline.
- Bạn nên xem lại ngày đăng của tin LinkedIn số 1. Mã job `4193261952` trông khá cũ. Nếu LinkedIn hiện "Reposted" thì lấy ngày repost, và ghi rõ trong bài.
- Nhớ ghi lượt nhờ mình tìm tin này vào prompt log. Trong Audit Report, lượt này nên được ghi là AI hỗ trợ tìm kiếm. Việc xác minh và chụp ảnh là do bạn tự làm.

Sources:
- [ITviec – tester jobs](https://itviec.com/it-jobs/tester)
- [ITviec – AI tester jobs](https://itviec.com/it-jobs/ai-tester)
- [Brarista – QA Engineer (Claude Code)](https://itviec.com/it-jobs/qa-engineer-claude-code-python-react-manual-tester-brarista-4435)
- [Money Forward – Fullstack QA Engineer Lead (AI)](https://itviec.com/it-jobs/hanoi-fullstack-qa-engineer-lead-manual-auto-ai-money-forward-vietnam-co-ltd-4636)
- [Galaxy Holdings – Lead Penetration Tester (AI Applications)](https://itviec.com/it-jobs/lead-penetration-tester-web-api-ai-applications-galaxy-holdings-4535)
```

**Xử lý:** Lọc lại 10 job rồi đưa vào bài report

---

## #7 | 01:15 30/09/2026 | Claude Opus | R1
**Mục đích:** Điền 7 job còn lại vào theo format đã ghi vào 1.1

**Prompt:**
```
Giúp tôi tiếp tục điền vào bảng sau nhé:

```markdown
### 1.1 Bảng 10 tin tuyển dụng

**Ngày thu thập:** [dd/mm/2026] | **Mốc 60 ngày:** từ [dd/mm/2026] đến [dd/mm/2026]

| # | Vị trí | Công ty | Nền tảng | Ngày đăng | Cấp độ | Hình thức / Địa điểm | Mức lương | Yêu cầu AI? | Link |
|---|---|---|---|---|---|---|---|---|---|
| J01 | Test Engineer | Corsair | LinkedIn | Hiển thị "1 week ago" tính từ 30/09/2026 | Intern | Onsite, Fulltime - Vietnam | Không công bố | Không | [link](https://www.linkedin.com/jobs/search-results/?currentJobId=4193261952&eBP=CwEAAAGg7cSmFgM1lRNlcB2BYUipAWbYl4s3ALmp_tzwZBnQ2qVwbUdmmMYYJRudYTKrY_8qHT6TvVuEgIb1zhPeorxMD7Lw-j9eFcxyxwMk6VW0QV1tQOCxRD2-f9_HKYMtiP6gDiM7RXBULuiRTyDQ7z86ENllBtRNvHc6ZqE9gBeZ1pe7wBxtOUv336H8wZC4R4RiLLwwMX_Otj8QUyvzaJn3H-fQt_vODCdWcJkaQEVfsZeG0Kg3HgPzqkyfEBFCks4eSajPCvjdOjx0EPBYDC1zkFIM4IrpD5fsE7IwUTGrTZfcXgvjoV1POw8bpz5r6jo6VqG1cf9OwC3I-VL2wfnsaMg54d6SNo5CyOcGhadI0jHyc9ZpBRrbtQlgPVZuUAqJJTjzgRkZi2_PLToE-1HBYhXd0ku5ManGCg18OUwbYKXmIYxSXAepTmRcY_aGkAQo4MEWXuM71e6xyRD5XmYfv9GHhl-I634InvSN&refId=WJZ2qDVtj1akBj37TK1MLw%3D%3D&trackingId=76ACJZvSqhJ9EpOYCZramw%3D%3D&keywords=Software%20Tester&origin=SEMANTIC_SEARCH_LANDING_PAGE) |
| J02 | Software Testing Lead | Công ty cổ phần dịch vụ công nghệ tin học HPT | TopCV | Hiển thị "Cập nhật 1 tuần trước" kể từ 30/09/2026| Lead | Onsite, Fulltime - Vietnam | Thoả thuận | Không | [link](https://www.topcv.vn/viec-lam/software-testing-lead/2302520.html?ta_source=JobSearchList_LinkDetail&u_sr_id=IAo5dajlmSZENgw7YbEeqNugFPV1UUL9lmRRxeSi_1790695848) |
| J03 | QA Engineer (Tester/ QA QC) | OL Vietnam | itViec | 29/08/2026 | Onsite | Không ghi rõ (yêu cầu "significant experience" manual testing) | Onsite, Fulltime - Vietnam | Không | [link](https://itviec.com/it-jobs/qa-engineer-tester-qa-qc-ol-vietnam-3927?lab_feature=preview_jd_page) |
| J04 | [...] | [...] | [...] | [dd/mm/2026] | [...] | [...] | [...] | [Có/Không] | [link] |
| J05 | [...] | [...] | [...] | [dd/mm/2026] | [...] | [...] | [...] | [Có/Không] | [link] |
| J06 | [...] | [...] | [...] | [dd/mm/2026] | [...] | [...] | [...] | [Có/Không] | [link] |
| J07 | [...] | [...] | [...] | [dd/mm/2026] | [...] | [...] | [...] | [Có/Không] | [link] |
| J08 | [...] | [...] | [...] | [dd/mm/2026] | [...] | [...] | [...] | [Có/Không] | [link] |
| J09 | [...] | [...] | [...] | [dd/mm/2026] | [...] | [...] | [...] | [Có/Không] | [link] |
| J10 | [...] | [...] | [...] | [dd/mm/2026] | [...] | [...] | [...] | [Có/Không] | [link] |


Đây là thứ tự cần điền:
J04:https://itviec.com/it-jobs/manual-tester-qa-qc-good-english-netcompany-2659?lab_feature=preview_jd_page
J05:https://itviec.com/it-jobs/quality-control-intern-software-tester-phu-hung-securities-phs-1247?lab_feature=preview_jd_page
J06:https://itviec.com/it-jobs/senior-middle-automation-test-qa-qc-8seneca-1756?lab_feature=preview_jd_page
J07:https://itviec.com/it-jobs/automation-tester-qa-qc-tester-japanese-n3-trustedai-2550?lab_feature=preview_jd_page
J08:https://itviec.com/it-jobs/qa-engineer-claude-code-python-react-manual-tester-brarista-4435
J09:https://itviec.com/it-jobs/hanoi-fullstack-qa-engineer-lead-manual-auto-ai-money-forward-vietnam-co-ltd-4636
J10:https://itviec.com/it-jobs/lead-penetration-tester-web-api-ai-applications-galaxy-holdings-4535
```

**Output:**
```
Mình sẽ mở 4 tin còn lại (J04–J07) để lấy thông tin. J08–J10 mình đã có dữ liệu từ lượt trước.

Mình đã điền xong bảng. Có 3 chỗ trong bảng cũ cần sửa, mình ghi ở dưới bảng.

```markdown
### 1.1 Bảng 10 tin tuyển dụng

**Ngày thu thập:** 30/09/2026 | **Mốc 60 ngày:** từ 01/08/2026 đến 30/09/2026

| # | Vị trí | Công ty | Nền tảng | Ngày đăng | Cấp độ | Hình thức / Địa điểm | Mức lương | Yêu cầu AI? | Link |
|---|---|---|---|---|---|---|---|---|---|
| J01 | Test Engineer | Corsair | LinkedIn | ~23/09/2026 (hiển thị "1 week ago" lúc 30/09/2026) | Intern | Onsite, Fulltime – Việt Nam | Không công bố | Không | [link](https://www.linkedin.com/jobs/view/4193261952/) |
| J02 | Software Testing Lead | Công ty cổ phần dịch vụ công nghệ tin học HPT | TopCV | ~23/09/2026 (hiển thị "Cập nhật 1 tuần trước" lúc 30/09/2026) | Lead | Onsite, Fulltime – Việt Nam | Thoả thuận | Không | [link](https://www.topcv.vn/viec-lam/software-testing-lead/2302520.html) |
| J03 | QA Engineer (Tester/ QA QC) | OL Vietnam | ITviec | 29/08/2026 | Không ghi rõ (yêu cầu "significant experience" manual testing) | Onsite, Fulltime – Việt Nam | [đăng nhập để xem] | Không | [link](https://itviec.com/it-jobs/qa-engineer-tester-qa-qc-ol-vietnam-3927) |
| J04 | Manual Tester (QA/QC, Good English) | Netcompany | ITviec | ~09/09/2026 (hiển thị "21 days ago" lúc 30/09/2026) | Fresher/Junior (nhận Fresher) | Onsite – TP.HCM | [đăng nhập để xem] | Không | [link](https://itviec.com/it-jobs/manual-tester-qa-qc-good-english-netcompany-2659) |
| J05 | Quality Control Intern (Software Tester) | Phu Hung Securities (PHS) | ITviec | 29/09/2026 (hiển thị "15 hours ago" lúc 30/09/2026) | Intern | Onsite – TP.HCM | Trợ cấp 2.000.000 VND/tháng | Không | [link](https://itviec.com/it-jobs/quality-control-intern-software-tester-phu-hung-securities-phs-1247) |
| J06 | Senior/Middle Automation Test (QA QC) | 8Seneca | ITviec | 29/09/2026 (hiển thị "7 hours ago" lúc 30/09/2026) | Middle (3+ năm) / Senior (5+ năm, 2+ năm lead) | Onsite – Hà Nội | [đăng nhập để xem] | Có (AI coding agents sinh test code, pipeline AI-first) | [link](https://itviec.com/it-jobs/senior-middle-automation-test-qa-qc-8seneca-1756) |
| J07 | Automation Tester (QA QC/ Tester/ Japanese N3+) | TrustedAI | ITviec | ~24/09/2026 (hiển thị "6 days ago" lúc 30/09/2026) | Middle (3+ năm, có kinh nghiệm lead) | Onsite – Hà Nội | Lên đến 35 triệu VND (thỏa thuận) | Có (ứng dụng AI vào tác vụ test; ưu tiên kinh nghiệm test chatbot/RAG) | [link](https://itviec.com/it-jobs/automation-tester-qa-qc-tester-japanese-n3-trustedai-2550) |
| J08 | QA Engineer (Claude Code, Python, React, Manual Tester) | Brarista | ITviec | ~08/09/2026 (hiển thị "22 days ago" lúc 30/09/2026) | Fresher – Middle (không yêu cầu số năm) | Remote – TP.HCM / Đà Nẵng / Hà Nội | [đăng nhập để xem] | Có (bắt buộc thành thạo Claude Code) | [link](https://itviec.com/it-jobs/qa-engineer-claude-code-python-react-manual-tester-brarista-4435) |
| J09 | [Hanoi] Fullstack QA Engineer Lead (Manual, Auto, AI) | Money Forward Vietnam | ITviec | 30/09/2026 (hiển thị "1 hour ago" lúc 30/09/2026) | Lead (8+ năm, 3+ năm lead) | Hybrid – Hà Nội | [đăng nhập để xem] | Có (dẫn dắt team dùng GenAI; test tính năng AI) | [link](https://itviec.com/it-jobs/hanoi-fullstack-qa-engineer-lead-manual-auto-ai-money-forward-vietnam-co-ltd-4636) |
| J10 | Lead Penetration Tester (Web, API & AI Applications) | Galaxy Holdings | ITviec | 29/09/2026 (hiển thị "23 hours ago" lúc 30/09/2026) | Lead (6+ năm, 2+ năm quản lý team) | Onsite – TP.HCM (Thủ Đức) | [đăng nhập để xem] | Có (test prompt injection, RAG, OWASP LLM Top 10) | [link](https://itviec.com/it-jobs/lead-penetration-tester-web-api-ai-applications-galaxy-holdings-4535) |

**Tổng số tin yêu cầu AI/LLM:** 5/10 (J06–J10, yêu cầu ≥ 3)

**Những chỗ mình đã sửa trong bảng cũ:**
- **J03 bị lệch cột.** Chữ "Onsite" đang nằm ở cột Cấp độ, còn mô tả kinh nghiệm lại nằm ở cột Hình thức. Mình đã chuyển lại đúng cột.
- **Rút gọn link.** Link LinkedIn đang là link trang kết quả tìm kiếm, rất dài và dễ hết hạn. Mình đổi sang link cố định dạng `/jobs/view/<id>/`. Các link ITviec và TopCV thì mình bỏ phần tham số tracking phía sau.
- **Ngày đăng.** Mình quy đổi các mốc như "x days ago" ra ngày cụ thể và vẫn giữ chữ gốc trong ngoặc. Screenshot của bạn nên chụp đúng dòng chữ gốc đó.

**Những việc bạn cần tự làm:**
- **Điền lương bằng tài khoản của bạn.** Ô nào ghi `[đăng nhập để xem]` là do ITviec ẩn lương khi chưa đăng nhập. Lương của J05 và J07 mình lấy từ phần mô tả phúc lợi trong JD.
- **Kiểm tra lại ngày đăng của J01 (LinkedIn).** Mã job 4193261952 có vẻ cũ, nên nhiều khả năng đây là tin được đăng lại. Nếu trên trang có chữ "Reposted" thì bạn ghi thêm vào cột Ngày đăng.
- **Tính mốc 60 ngày theo ngày nộp bài.** Đề tính 60 ngày ngược từ ngày nộp, không phải ngày thu thập. Tin cũ nhất là J03 (29/08), nên bạn phải nộp trước khoảng 28/10 thì tin này mới còn hợp lệ.
- **Dùng J10 cẩn thận.** J10 là vị trí security testing. Nếu TA hỏi vì sao chọn, bạn có thể trả lời rằng nó cho thấy một nhánh mới của nghề: kiểm thử bảo mật cho ứng dụng AI.
```

**Xử lý:** Điền vào bảng và kiểm tra lại.

---

## #8 | 01:35 35/09/2026 | Claude Opus | R1
**Mục đích:** Điền báo cáo vào những chỗ cần điền ở 1.2 (tức là những chỗ AI có thể điền)

**Prompt:**
```
Tiếp tục giúp tôi điền 1.2 nhé, ý nào bắt buộc phải tự viết thì giữ nguyên để tôi tự viết nhé. Về screenshot làm tương tự J01: R1_jobs/J01.png; R1_jobs/J02.png,...
Có thể tham khảo 1.1 hoàn thiện:

| # | Vị trí | Công ty | Nền tảng | Ngày đăng | Cấp độ | Hình thức / Địa điểm | Mức lương | Yêu cầu AI? | Link |
|---|---|---|---|---|---|---|---|---|---|
| J01 | Test Engineer | Corsair | LinkedIn | ~23/09/2026 (hiển thị "1 week ago" lúc 30/09/2026) | Intern | Onsite, Fulltime – Việt Nam | Không công bố | Không | [link](https://www.linkedin.com/jobs/view/4193261952/) |
| J02 | Software Testing Lead | Công ty cổ phần dịch vụ công nghệ tin học HPT | TopCV | ~23/09/2026 (hiển thị "Cập nhật 1 tuần trước" lúc 30/09/2026) | Lead | Onsite, Fulltime – Việt Nam | Thoả thuận | Không | [link](https://www.topcv.vn/viec-lam/software-testing-lead/2302520.html) |
| J03 | QA Engineer (Tester/ QA QC) | OL Vietnam | ITviec | 29/08/2026 | Không ghi rõ (yêu cầu "significant experience" manual testing) | Onsite, Fulltime – Việt Nam | Không công bố ("You'll love it") | Không | [link](https://itviec.com/it-jobs/qa-engineer-tester-qa-qc-ol-vietnam-3927) |
| J04 | Manual Tester (QA/QC, Good English) | Netcompany | ITviec | 09/09/2026 | Fresher/Junior (nhận Fresher) | Onsite – TP.HCM | Không công bố ("You'll love it") | Không | [link](https://itviec.com/it-jobs/manual-tester-qa-qc-good-english-netcompany-2659) |
| J05 | Quality Control Intern (Software Tester) | Phu Hung Securities (PHS) | ITviec | 29/09/2026 | Intern | Onsite – TP.HCM | Không công bố ("You'll love it"), Trợ cấp 2.000.000 VND/tháng và 400.000 VND/tháng cho phí đỗ xe | Không | [link](https://itviec.com/it-jobs/quality-control-intern-software-tester-phu-hung-securities-phs-1247) |
| J06 | Senior/Middle Automation Test (QA QC) | 8Seneca | ITviec | 29/09/2026 | Middle (3+ năm) / Senior (5+ năm, 2+ năm lead) | Onsite – Hà Nội | Không công bố ("You'll love it") | Có (AI-first way of working, proven in QA) | [link](https://itviec.com/it-jobs/senior-middle-automation-test-qa-qc-8seneca-1756) |
| J07 | Automation Tester (QA QC/ Tester/ Japanese N3+) | TrustedAI | ITviec | 24/09/2026 | Middle (3+ năm, có kinh nghiệm lead) | Onsite – Hà Nội | 800 - 1,500 USD | Có (ứng dụng AI vào các tác vụ test) | [link](https://itviec.com/it-jobs/automation-tester-qa-qc-tester-japanese-n3-trustedai-2550) |
| J08 | QA Engineer (Claude Code, Python, React, Manual Tester) | Brarista | ITviec | 08/09/2026 | Fresher – Middle (không yêu cầu số năm) | Remote – TP.HCM / Đà Nẵng / Hà Nội | 800 - 1,000 USD | Có (You're excellent with Claude Code) | [link](https://itviec.com/it-jobs/qa-engineer-claude-code-python-react-manual-tester-brarista-4435) |
| J09 | [Hanoi] Fullstack QA Engineer Lead (Manual, Auto, AI) | Money Forward Vietnam | ITviec | 30/09/2026 | Lead (8+ năm, 3+ năm lead) | Hybrid – Hà Nội | Không công bố ("You'll love it") | Có (AI Adoption & AI-Augmented Testing) | [link](https://itviec.com/it-jobs/hanoi-fullstack-qa-engineer-lead-manual-auto-ai-money-forward-vietnam-co-ltd-4636) |
| J10 | Lead Penetration Tester (Web, API & AI Applications) | Galaxy Holdings | ITviec | 29/09/2026 | Lead (6+ năm, 2+ năm quản lý team) | Onsite – TP.HCM (Thủ Đức) | Không công bố ("You'll love it") | Có (Ứng dụng AI/LLM để tăng tốc phân tích và soạn báo cáo, đồng thời kiểm soát rủi ro rò rỉ dữ liệu khi sử dụng AI.) | [link](https://itviec.com/it-jobs/lead-penetration-tester-web-api-ai-applications-galaxy-holdings-4535) |
```

**Output:** File `HW01_R1_1.2.md` do AI tạo, lưu nguyên bản tại
`ai-outputs/HW01_R1_1.2.md`
```
Mình sẽ mở lại từng JD để lấy mô tả công việc và kỹ năng. Mình sẽ để trống phần AI Impact Analysis cho bạn tự viết, vì đây là phần phân tích được chấm điểm và dễ bị hỏi lúc vấn đáp.

Mình đã điền xong mục 1.2 cho J02–J10. Mỗi tin có mô tả công việc, kỹ năng bắt buộc, kỹ năng ưu tiên, kỹ năng AI, lương và ngày đăng, khớp với bảng 1.1 của bạn. Đường dẫn ảnh đã đổi sang `R1_jobs/Jxx.png`.

**Những ô mình để trống cho bạn tự viết:**
- **AI Impact Analysis của cả 10 tin.** Đây là phần phân tích được chấm điểm và dễ bị hỏi lúc vấn đáp. Mỗi tin đã có sẵn gợi ý để bạn bám vào:
  - J08: AI sinh test matrix, còn người kiểm tra lại tag sản phẩm do AI gợi ý.
  - J06: công ty yêu cầu phân biệt được test do AI sinh đúng với test "trông hợp lý nhưng sai".
  - J09: vị trí này vừa dùng AI để test, vừa test tính năng AI.
  - J10: kiểm thử bảo mật cho chính ứng dụng AI.
- **J01 (LinkedIn): ô mô tả và kỹ năng.** LinkedIn chặn công cụ đọc trang của mình nên mình không lấy được nội dung. Bạn copy JD từ tài khoản của bạn, gửi mình thì mình tóm tắt giúp.

**Những điểm cần chú ý:**
- Phần mô tả công việc là mình tóm tắt từ JD. Đề hướng dẫn tóm tắt "theo lời của bạn", nên bạn cần làm một trong hai việc: sửa lại theo cách diễn đạt của mình, hoặc ghi rõ phần này do AI tóm tắt vào Audit Report và Disclosure.
- Nhớ ghi các lượt hỏi 1.1 và 1.2 vào prompt log.
- **J07:** JD có ghi "lên đến 35 triệu, thỏa thuận theo năng lực". Con số này khác với mức 800 – 1,500 USD bạn điền. Bạn nên kiểm tra xem khi đăng nhập ITviec hiển thị mức nào, rồi ghi cho nhất quán.
- **J02:** TopCV ghi địa điểm là TP.HCM (Phú Nhuận). Cột Hình thức / Địa điểm của J02 trong bảng 1.1 nên sửa từ "Việt Nam" thành "TP.HCM".
```

**Xử lý:** Đưa các thông tin vào 1.2, những thông tin cần thiết còn lại chưa điền thì đọc lại và jd và điền.

---

## #9 | 02:42 29/09/2026 | Claude Opus | R1
**Mục đích:** Nhờ Claude vẽ MindMap

**Prompt:**
```
Giờ giúp tôi thực hiện 1.3 nhé, có thể vẽ ảnh để rồi tôi tìm lỗi cũng được: ### 1.3 Mindmap vai trò QA/QC do AI sinh và 3 lỗi

> 📝 **Hướng dẫn (CLO G9.1):**
> - Cho AI vẽ mindmap vai trò/quy trình QA/QC (nên yêu cầu output dạng Mermaid hoặc Markdown để dễ render). Lưu prompt vào log.
> - Tìm **đúng 3 lỗi có căn cứ**, đối chiếu với **ISTQB CTFL v4.0** (ghi rõ mục, ví dụ 1.4 "Test Activities, Testware and Test Roles", 1.5 "Essential Skills and Good Practices"). Các kiểu lỗi dễ gặp: nhầm QA với QC, xếp sai hoạt động vào vai trò, gộp test level với test type, thiếu vai trò test management/test analysis, gán hoạt động cho sai giai đoạn.
> - Vẽ lại mindmap đã sửa, **đánh dấu** các nhánh đã sửa (đổi màu hoặc thêm ký hiệu ✎).

**Prompt:** xem `P[..]` – Phụ lục A

**Mindmap do AI sinh (bản gốc):**

![Mindmap AI sinh](images/mindmap_ai.png)

**3 lỗi phát hiện:**

| # | Vị trí trong mindmap | AI viết | Vì sao sai | Căn cứ (ISTQB / slide) | Sửa thành |
|---|---|---|---|---|---|
| E1 | [Nhánh ...] | [...] | [...] | [CTFL v4.0 §...] | [...] |
| E2 | [Nhánh ...] | [...] | [...] | [CTFL v4.0 §...] | [...] |
| E3 | [Nhánh ...] | [...] | [...] | [CTFL v4.0 §...] | [...] |

**Mindmap sau khi sửa:**

![Mindmap đã sửa](images/mindmap_fixed.png)

<details><summary>Mã nguồn mindmap (Mermaid)</summary>

```mermaid
mindmap
  root((QA/QC Roles))
    [...]

</details>
```

**Output:** File `mindmap_ai.mmd` do AI tạo, lưu nguyên bản tại
`ai-outputs/mindmap_ai.mmd`
```
Mình sẽ vẽ mindmap (dạng Mermaid) rồi xuất ra ảnh PNG cho bạn.

Ảnh bị chồng nhãn, khó đọc. Mình sẽ render lại theo bố cục dạng cây.

Mình đã vẽ xong mindmap vai trò QA/QC với 9 nhánh. Bạn nhận được hai file: `mindmap_ai.png` là ảnh, `mindmap_ai.mmd` là mã nguồn Mermaid để dán vào khối `<details>`. Ảnh được vẽ theo dạng cây trái sang phải, vì bố cục hình tròn mặc định của Mermaid bị chồng nhãn, không đọc được.

**Mình không cố ý cài lỗi vào.** Đây là bản làm thật của mình. Nếu mình biết trước chỗ sai rồi chỉ cho bạn thì mục G9.1 không còn giá trị. Vì vậy việc tìm lỗi là của bạn. Có thể bạn sẽ tìm được ít hơn 3 lỗi "sai hẳn". Khi đó, những chỗ thiếu, xếp sai nhánh hoặc gộp nhầm khái niệm vẫn tính là lỗi, miễn bạn chỉ ra được căn cứ.

**Cách soát:** đặt từng nhánh cạnh mục tương ứng trong ISTQB CTFL v4.0:

| Nhánh | Đối chiếu với |
|---|---|
| QA / QC | §1.2.2 Testing and Quality Assurance |
| Vai trò theo ISTQB | §1.4.5 Roles in Testing, §1.4.1 Test Activities and Tasks |
| Test levels | §2.2.1 |
| Test types | §2.2.2 |
| Kiểm thử sau thay đổi | §2.2.3 |
| Kỹ năng cốt lõi | §1.5.1 Generic Skills Required for Testing |
| Chức danh thị trường, AI trong QA/QC | 10 tin tuyển dụng của bạn ở 1.1–1.2 |

Nên tải bản PDF CTFL v4.0 chính thức từ istqb.org để trích đúng số mục.

**Khi vẽ bản đã sửa:** bạn thêm ký hiệu `✎` vào các node đã sửa trong file `.mmd` rồi gửi lại cho mình. Mình sẽ render thành `mindmap_fixed.png` cùng kiểu, với các node đã sửa có viền đỏ.

Nhớ ghi lượt nhờ mình vẽ mindmap này vào prompt log, kèm timestamp. Đây là mục A01 trong Audit Report.
```

**Xử lý:** Cảm thấy Mindmap bằng mermaid khó nhìn, nên muốn làm lại mindmap khác nhiều màu sắc hơn như trên mạng, để dễ nhìn hơn.

---

## #10 | 02:51 30/09/2026 | Claude Opus | R1
**Mục đích:** Tạo lại Mindmap dễ nhìn hơn

**Prompt:**
```
Mình thấy là tạo bằng mermaid nó rối và khó nhìn quá. Bạn có thể giúp mình tạo sinh ảnh Mindmap colorful luôn được không?
Có thể tham khảo qua hình mindmap này chẳng hạn
```
*Đính kèm:* Cùng với một ảnh mindmap lấy trên mạng theo: [link](https://learningfundamentals.com.au/resources/)
ư
**Output:** File `mindmap_ai.png` do AI tạo, lưu nguyên bản tại
`ai-outputs/mindmap_ai.png`
```
Mình sẽ tự vẽ mindmap theo phong cách giống ảnh mẫu: nhánh cong nhiều màu, to ở gốc và thon dần ra ngọn, chữ viết tay. Mình viết code để dựng ảnh này thay vì dùng Mermaid.

Phần đánh dấu ✎ đã chạy đúng. Mình gửi bạn ảnh bản gốc:

Mình đã vẽ lại mindmap trong file `mindmap_ai.png` theo kiểu giống ảnh mẫu: nhánh cong nhiều màu, to ở gốc và thon dần ra ngọn, chữ viết tay có hỗ trợ tiếng Việt, mỗi nhánh chính có một icon. Nội dung giữ nguyên 100% so với bản Mermaid lúc nãy, nên file `mindmap_ai.mmd` vẫn là mã nguồn gốc để bạn dán vào báo cáo và ghi vào Audit Report.

Mình không dùng được công cụ tạo ảnh bằng AI, nên ảnh này được vẽ bằng code. Vì vậy mindmap không có hình minh họa hoạt hình như ảnh mẫu, chỉ có icon emoji ở mỗi nhánh.

Khi bạn tìm xong 3 lỗi, cách làm bản đã sửa như sau:
1. Sửa trực tiếp file `mindmap_ai.mmd`: đổi chữ, thêm, bớt hoặc chuyển node sang nhánh khác.
2. Thêm ký hiệu `✎` vào cuối các node đã sửa.
3. Gửi file cho mình, mình sẽ xuất ra `mindmap_fixed.png` cùng kiểu. Các node có ✎ sẽ được khoanh viền đỏ nét đứt, mình đã chạy thử và nó hoạt động.
```

**Xử lý:** Thấy mindmap đã oke, giữ lại và tìm lỗi

---

## #11 | 04:58 30/09/2026 | Claude Opus | R1
**Mục đích:** Kiểm tra xem có cần chỉnh lại câu từ gì ở 1.3 không

**Prompt:**
```
Sau đây là mình chỉnh lại mindmap, bạn xem có câu từ gì cần chỉnh lại không nhé:

```markdown
### 1.3 Mindmap vai trò QA/QC do AI sinh và 3 lỗi

**Prompt:** xem `Prompt #10` – Phụ lục A

**Mindmap do AI sinh (bản gốc):**

![Mindmap AI sinh](R1_jobs/mindmap_QA_QC.png)

**3 lỗi phát hiện:**

| # | Vị trí trong mindmap | AI viết | Vì sao sai | Căn cứ | Sửa thành |
|---|---|---|---|---|---|
| E1 | 3 nhánh lớn: "Test levels", "Test types", "Kiểm thử sau thay đổi" | Đặt 3 nhánh kiến thức kỹ thuật lại cùng cấp với các nhánh vai trò (như QA, QC, Chức danh,...) | Đề thì yêu cầu mindmap vai trò QA/QC. Mà test levels, test types và kiểm thử sau thay đổi chính là kiến thức kỹ thuật mà mọi vai trò cần nắm, không phải vai trò. Đặt cùng cấp như vậy làm cho mindmap không còn ý chính về vai trò nữa. Với lại trong CTFL v4.0 thì "Kiểm thử sau thay đổi" cũng là một Test types thuộc về "Test types", vậy nên đưa nó vào "Test types" sẽ hợp lý hơn | Yêu cầu (AI Tool draws a QA/QC role mindmap); CTFL v4.0 chương 2.2 xếp các mục này là kiến thức về kiểm thử, không phải vai trò | Gộp nhánh "Kiêm thử sau thay đổi vào trong "Test types" tức là sau "Test types" sẽ có: "Functional", "Non-functional", "Black-box", "White-box", "Kiểm thử sau thay đổi". Còn các nhánh con của "Kiểm thử sau thay đổi giữ nguyên". Tiếp tục gộp 2 nhánh "Test types" và "Test levels" thành một nhánh lớn "Kiến thức nền tảng" (giữ nguyên nội dung trong tương tự), tách rõ khỏi các nhánh vai trò|
| E2 | Nhánh lớn "Chức danh trên thị trường" | Liệt kê 7 chức danh, không có chức danh nào là QC hoặc là thuộc QC | Thiếu chức danh QC, cách gọi phổ biến của nghề kiểm thử tại Việt Nam (Bằng chứng là có 4 JD ghi là QC); Có thể là vì AI nghĩ QA QC là một nên không liệt kê, hoặc là ảnh hưởng từ data của nước ngoài | Từ R1: 4/10 JD có chữ QC trong tên vị trí (J03, J04, J05, J06); Outcomes của đề: "Describe the 2026+ QA/QC job-market landscape" | Thêm "QC Intern / Fresher" vào nhánh lớn "Chức danh trên thị trường" |
| E3 | Nhánh lớn "AI trong QA/QC" | Nhánh con "Con người quyết định release" nằm chung với việc AI hỗ trợ/thay thế (sinh test case, sinh script, kiểm thử hệ thống AI) | Những nhánh con đó không cùng chung ngữ nghĩa: các mục còn lại là việc AI làm, còn quyết định release thì là trách nhiệm của con người. | Vào ngữ nghĩa của nhánh lớn, rồi suy xuống nhánh con | Bỏ luôn "Con người quyết định Release" trong nhánh lớn "AI trong QA/QC" |

**Mindmap sau khi sửa:**

![Mindmap đã sửa](R1_jobs/mindmap_fixed.png)
```
*Đính kèm:* File ảnh mới sau khi sửa

**Output:**
```
Nhìn chung 3 lỗi bạn tìm đều có lý. Tuy vậy có **một chỗ sai về ISTQB** trong E1 mà bạn nên sửa trước khi nộp, vì rất dễ bị bắt lỗi lúc vấn đáp.

## Vấn đề chính: E1 trích sai ISTQB

Bạn viết: *"trong CTFL v4.0 thì 'Kiểm thử sau thay đổi' cũng là một Test type"*. Câu này **không đúng với v4.0**:
- **CTFL v3.1** (bản cũ) có 4 test type: functional, non-functional, white-box và **change-related testing**. Theo bản này thì câu của bạn đúng.
- **CTFL v4.0** chỉ còn 4 test type ở §2.2.2 là functional, non-functional, black-box, white-box. Confirmation và regression testing được tách ra một mục riêng là **§2.2.3**, không còn là test type nữa.

Nghĩa là ở điểm này, bản gốc của AI (tách "Kiểm thử sau thay đổi" thành nhánh riêng) lại khớp với v4.0. Bạn có 2 cách xử lý:
1. **(Nên chọn)** Bỏ lập luận "là một test type". Trong nhánh "Kiến thức nền tảng", để 3 nhánh con ngang hàng nhau: Test levels, Test types, Kiểm thử sau thay đổi. Lỗi chính của E1 là đặt kiến thức kỹ thuật ngang hàng với các vai trò, và lỗi đó vẫn đứng vững.
2. Giữ cách gộp như hiện tại nhưng ghi rõ căn cứ là CTFL v3.1 §2.3.4. Cách này yếu hơn vì đề yêu cầu dùng bản mới nhất.

Căn cứ mạnh nhất cho E1 là **CTFL v4.0 §1.4.5**. Mục này chỉ định nghĩa 2 vai trò kiểm thử (test management role và testing role), nên test levels và test types không thể là "vai trò".

## Các chỗ khác cần chỉnh

- **E2, phần bằng chứng:** tên vị trí có "QC" hoặc "Quality Control" là **5/10 tin (J03–J07)**, không phải 4. Tuy nhiên ITviec thường tự gắn cụm "QA QC" vào tên tin như một nhãn danh mục, nên bằng chứng mạnh nhất là J05 "Quality Control **Intern**", vì đó là chức danh thật.
- **E2, lý do AI bỏ sót:** mình xác nhận thật là mình liệt kê chức danh theo cách gọi quốc tế, chia theo chức năng (manual, automation, performance…), và không nghĩ tới cách gọi "QC" phổ biến ở Việt Nam. Như vậy giả thuyết thứ hai của bạn (ảnh hưởng từ dữ liệu nước ngoài) sát với thực tế hơn.
- **E2, tính nhất quán:** bảng ghi "QC Intern / Fresher" là 1 node, nhưng hình vẽ lại có 2 node. Bạn nên chọn một cách rồi sửa cho khớp.
- **E3, cách sửa:** "bỏ luôn" làm mất một ý quan trọng. Đề có outcome *"Distinguish work that AI can replace / assist / cannot replace"*, mà "con người quyết định release" chính là ví dụ tiêu biểu cho việc AI **không thay thế** được. Cách sửa tốt hơn là **di chuyển** node này chứ không xóa: chia nhánh "AI trong QA/QC" thành 2 nhánh con "AI làm / hỗ trợ" và "Con người chịu trách nhiệm". Nhờ vậy căn cứ của E3 cũng mạnh hơn, vì bám trực tiếp vào outcome của đề thay vì chỉ dựa vào ngữ nghĩa.
- **Mã prompt:** bạn ghi "Prompt #10", còn template dùng dạng `P10`. Nên chọn một kiểu rồi dùng thống nhất trong cả bài.
- **Lỗi chính tả:** "Kiêm thử", thiếu dấu ngoặc kép đóng, "Release" viết hoa không cần thiết, "giữ nguyên nội dung trong tương tự".

## Bản đã chỉnh (theo cách 1)

```markdown
### 1.3 Mindmap vai trò QA/QC do AI sinh và 3 lỗi

**Prompt:** xem `P10` – Phụ lục A

**Mindmap do AI sinh (bản gốc):**

![Mindmap AI sinh](R1_jobs/mindmap_QA_QC.png)

**3 lỗi phát hiện:**

| # | Vị trí trong mindmap | AI viết | Vì sao sai | Căn cứ | Sửa thành |
|---|---|---|---|---|---|
| E1 | 3 nhánh lớn "Test levels", "Test types", "Kiểm thử sau thay đổi" | Đặt 3 nhánh kiến thức kỹ thuật ngang hàng với các nhánh vai trò (QA, QC, Vai trò theo ISTQB, Chức danh...) | Đề yêu cầu mindmap **vai trò** QA/QC. Test levels, test types và kiểm thử sau thay đổi là kiến thức kỹ thuật mà mọi vai trò đều cần nắm, bản thân chúng không phải vai trò. Đặt ngang hàng làm mindmap mất trọng tâm và khiến người đọc hiểu nhầm đây là các "loại vai trò". | Đề bài (G9.1: "AI Tool draws a QA/QC role mindmap"); CTFL v4.0 §1.4.5 chỉ định nghĩa 2 vai trò (test management role, testing role); các nội dung trên thuộc §2.2 (Test Levels and Test Types) | Gom 3 nhánh vào một nhánh lớn mới "Kiến thức nền tảng" (giữ nguyên các nhánh con), tách rõ khỏi các nhánh vai trò |
| E2 | Nhánh lớn "Chức danh trên thị trường" | Liệt kê 7 chức danh, không có chức danh QC nào | Thiếu chức danh QC, là cách gọi phổ biến của nghề kiểm thử tại Việt Nam, đặc biệt ở cấp đầu vào. Có thể AI dựng danh sách theo cách gọi quốc tế (chia theo chức năng: manual, automation, performance...) nên bỏ qua cách gọi của thị trường Việt Nam. | Kết quả R1: 5/10 tin có "QC" hoặc "Quality Control" trong tên vị trí (J03–J07), trong đó J05 tuyển đúng chức danh "Quality Control Intern"; Outcome của đề: "Describe the 2026+ QA/QC job-market landscape" | Thêm "QC Intern / Fresher" vào nhánh "Chức danh trên thị trường" |
| E3 | Nhánh lớn "AI trong QA/QC" | Node "Con người quyết định release" nằm chung với các việc AI làm (sinh test case, sinh script, kiểm thử hệ thống AI) | Các node trong nhánh không cùng ngữ nghĩa: 3 node là việc AI làm hoặc hỗ trợ, còn quyết định release là trách nhiệm của con người, tức phần AI **không thay thế** được. Gộp chung làm mờ ranh giới giữa hai nhóm, trong khi đây là ý chính đề muốn phân biệt. | Outcome của đề: "Distinguish work that AI can replace / assist / cannot replace in QA/QC"; JD J06, J08 (con người kiểm tra lại output của AI) | Tách nhánh "AI trong QA/QC" thành 2 nhánh con: "AI làm / hỗ trợ" (sinh test case, test data; sinh và bảo trì script; kiểm thử hệ thống AI) và "Con người chịu trách nhiệm" (quyết định release) |

**Mindmap sau khi sửa:**

![Mindmap đã sửa](R1_jobs/mindmap_fixed.png)


Khi bạn chốt xong nội dung, gửi mình file `.mmd` đã sửa (thêm `✎` ở các node thay đổi), hoặc chỉ cần bảo "vẽ theo bảng trên". Mình sẽ xuất `mindmap_fixed.png` cùng kiểu với bản gốc, thay cho hình vẽ tay.
```

**Xử lý:** AI bảo mình sửa sai, vậy nên sẽ đưa ra bằng chứng dùng tài liệu đúng để bẻ AI

---

## #12 | 05:02 30/09/2026 | Claude Opus | R1
**Mục đích:** Đưa bằng chứng để bẻ AI

**Prompt:**
```
Về cái bạn nói là mình trích sai ISTQB. Thì hiện tại mình đang trích từ của thầy, phiên bản v4.0.1, nên là đúng rồi nhé. Vậy ngoài cái đó bạn lầm tưởng là sai thì hết rồi nhé
```
*Đính kèm*: ảnh ở [link](https://www.fit.hcmus.edu.vn/~lqvu/Courses/SoftwareTesting/istqb-foundation-selfstudy.html#ch2) hiển thị 4 loại kiểm thử ở mục 02 có "Changed-related testing)
**Output:**
```
Mình vẫn giữ ý đó, nhưng chỉ ở mức "cách ghi căn cứ", không phải cách bạn sửa mindmap.

Ảnh bạn gửi là **tài liệu tóm tắt của thầy**, không phải văn bản syllabus chính thức. Trong syllabus chính thức CTFL v4.0/v4.0.1 của ISTQB:
- **§2.2.2 Test Types** chỉ liệt kê: functional, non-functional, black-box, white-box.
- **Confirmation testing và regression testing** nằm riêng ở **§2.2.3**. Cụm "change-related testing" không còn là test type như ở bản v3.1.

Chính tài liệu của thầy cũng ghi "Bốn loại kiểm thử", nhưng lại gộp black-box và white-box thành một dòng rồi thêm change-related vào. Cấu trúc đó giống v3.1 hơn v4.0. Bạn có thể tự kiểm tra trong 2 phút bằng file PDF syllabus chính thức trên istqb.org, mục 2.2.2.

Khi làm bài, bạn không cần đổi cách sửa. Chấm theo tài liệu môn học là hợp lý. Bạn chỉ cần **ghi căn cứ đúng nguồn** để TA không bắt bẻ được:
- Nên ghi: *"Tài liệu học ISTQB Foundation (CTFL v4.0.1) của môn học, chương 2.2: change-related testing là một test type"*.
- Không nên ghi: *"CTFL v4.0 §2.2.2"*. Nếu TA mở syllabus gốc ra đối chiếu thì câu này không khớp.

Ngoài chỗ đó thì 3 lỗi của bạn ổn. Các góp ý còn lại chỉ là tùy chọn, bạn quyết định:
- E2: bằng chứng là 5/10 tin chứ không phải 4.
- E3: nên chuyển node sang chỗ khác thay vì xóa.
- Sửa lỗi chính tả.

Bạn muốn mình xuất `mindmap_fixed.png` theo phương án của bạn không (Kiểm thử sau thay đổi nằm trong Test types, cả nhóm nằm dưới "Kiến thức nền tảng", thêm QC Intern và QC Fresher, bỏ node release)?
```

**Xử lý:** Vậy là đã xong 1.3

---

## #13 | 05:05 30/09/2026 | Claude Opus | R1
**Mục đích:** Hỗ trợ viết báo cáo mục 1.4

**Prompt:**
```
Bạn lúc nãy đã thực hiện 1.1 và 1.2, vậy nên giúp mình điền vào 1.4 nhé:
### 1.4 Tổng hợp xu hướng thị trường 2026+

> 📝 **Hướng dẫn:** Phần này đáp ứng 2 outcome của đề: *mô tả bức tranh thị trường* và *phân biệt việc AI thay thế / hỗ trợ / không thay thế*. Rút ra từ chính 10 tin ở trên, không lấy số liệu chung chung trên mạng.

**Thống kê từ 10 tin:**

| Chỉ số | Giá trị |
|---|---|
| Số tin Manual / Automation / AI-QA / Khác | [x / x / x / x] |
| Số tin yêu cầu AI/LLM | [x]/10 |
| Dải lương Junior / Senior | [...] / [...] |
| Top 5 kỹ năng xuất hiện nhiều nhất | [1. ... (x/10), 2. ..., ...] |
| Công cụ AI được nhắc đến | [...] |

**Phân loại công việc QA/QC theo mức độ tác động của AI:**

| Nhóm | Công việc cụ thể | Minh chứng từ tin tuyển dụng |
|---|---|---|
| AI **có thể thay thế** | [VD: sinh test data, viết test script lặp lại...] | [J..] |
| AI **hỗ trợ** (người vẫn quyết định) | [VD: sinh test case nháp, phân tích log...] | [J..] |
| AI **không thay thế** | [VD: đánh giá rủi ro nghiệp vụ, exploratory testing, giao tiếp stakeholder...] | [J..] |

**Nhận xét (3–5 câu):** [...]
```

**Output:**
```
Mình điền bảng dựa trên dữ liệu JD đã lấy ở 1.1–1.2. J01 (LinkedIn) mình không đọc được JD, nên các số liệu tính trên **9 tin** và J01 để bạn tự phân loại rồi cộng vào.

### 1.4 Tổng hợp xu hướng thị trường 2026+

**Thống kê từ 10 tin:**

| Chỉ số | Giá trị |
|---|---|
| Số tin Manual / Automation / AI-QA / Khác | 4 / 1 / 3 / 1 + J01 [bạn tự phân loại]<br>• Manual: J02, J03, J04, J05<br>• Automation: J07<br>• AI-QA (AI là kỹ năng bắt buộc): J06, J08, J09<br>• Khác (Security testing): J10 |
| Số tin yêu cầu AI/LLM | 5/10 (J06–J10); trong đó 4 tin bắt buộc (J06, J08, J09, J10), 1 tin ưu tiên (J07) |
| Dải lương | Chỉ 3/10 tin công bố lương:<br>• Intern: trợ cấp 2.000.000 VND/tháng + 400.000 VND gửi xe (J05)<br>• Fresher – Middle: 800 – 1,000 USD (J08)<br>• Middle: 800 – 1,500 USD (J07)<br>• Senior / Lead: không tin nào công bố (J02, J06, J09, J10) |
| Top 5 kỹ năng xuất hiện nhiều nhất (/9, chưa tính J01) | 1. Tiếng Anh (7/9)<br>2. Automation testing – Selenium / Playwright / Cypress... (7/9)<br>3. Lập trình / scripting – Java, TypeScript, Python, JS (7/9)<br>4. Sử dụng công cụ AI / kiểm thử sản phẩm AI (5/9)<br>5. API testing – REST, Postman (5/9) |
| Công cụ AI được nhắc đến | Claude Code (J06, J08), Cursor (J06, J08, J09), GitHub Copilot (J06, J09), ChatGPT (J06), LLM assistants (J09), Playwright MCP / browser agents (J06 – ưu tiên) |

**Phân loại công việc QA/QC theo mức độ tác động của AI:**

| Nhóm | Công việc cụ thể | Minh chứng từ tin tuyển dụng |
|---|---|---|
| AI **có thể thay thế** (phần lớn khối lượng, người chỉ review) | Sinh test matrix cho số lượng tổ hợp lớn; sinh và bảo trì test script / automation code; chuyển business rule thành test chạy được; soạn nháp báo cáo | J08 (Claude Code sinh test matrix, regression suite), J06 (AI coding agent sinh test code, pipeline "business rule → test case"), J09 (script generation), J10 (dùng AI soạn báo cáo) |
| AI **hỗ trợ** (người vẫn quyết định) | Thiết kế test case, triage bug; phân tích kết quả kiểm thử; gắn tag / phân loại dữ liệu (người phải kiểm tra lại output của AI) | J09 (GenAI tăng tốc test design và triage), J10 (AI tăng tốc phân tích), J08 (verify tag sản phẩm do AI gợi ý), J06 (phân biệt test AI sinh đúng với test "trông hợp lý nhưng sai") |
| AI **không thay thế** | Quyết định go/no-go release dựa trên rủi ro; exploratory testing (đặc biệt với tính năng AI); UAT và giao tiếp với khách hàng / stakeholder; dẫn dắt, mentor team; đặt quy định dùng AI an toàn; kiểm thử bảo mật cho chính hệ thống AI | J06 (go/no-go, UAT, lead 2 kỹ sư), J09 (release decision theo rủi ro, exploratory testing chatbot/agent, guideline dùng AI an toàn, cầu nối với PM Nhật), J10 (prompt injection, rò rỉ dữ liệu qua RAG, AI red teaming), J02 (quản lý stakeholder) |

**Nhận xét (3–5 câu):** Thị trường QA/QC 2026 đang chia hai rõ rệt. Các vị trí đầu vào (Intern/Fresher: J04, J05) vẫn chủ yếu là manual testing và không yêu cầu AI, còn phần lớn vị trí Middle trở lên đòi hỏi automation, lập trình và dùng AI như một kỹ năng bắt buộc (J06, J08, J09). AI đang đảm nhận phần "sinh ra" (test case, script, test matrix), trong khi con người chuyển sang phần "kiểm chứng và quyết định": kiểm tra output của AI, đánh giá rủi ro, quyết định release. Ngoài ra còn xuất hiện nhu cầu mới là **kiểm thử chính hệ thống AI** (chatbot, agent, RAG, prompt injection – J07, J09, J10). Đây là mảng mà kiến thức kiểm thử truyền thống chưa đủ. Mức lương hầu như không được công bố (7/10 tin), nên khó so sánh chênh lệch thu nhập giữa tester có kỹ năng AI và tester không có.

**Những điểm bạn cần xem lại:**
- **Số đếm kỹ năng là cách mình tự diễn giải JD.** Ví dụ, mình tính J05 có tiếng Anh vì JD ghi "Basic English", và tính J07 có lập trình vì JD ghi "nền tảng dev". Nếu TA hỏi, bạn cần nói được mình đã đếm theo tiêu chí nào.
- **J01:** bạn xem JD rồi xếp vào một nhóm, sau đó cập nhật 3 dòng liên quan: Manual/Automation/..., Top 5 (đổi mẫu số /9 thành /10), và dải lương nếu J01 có ghi.
- **Phần Nhận xét là phân tích.** Nên viết lại theo cách của bạn, hoặc ghi rõ trong Audit Report là AI soạn nháp. Nó cũng nên khớp với các ô AI Impact Analysis bạn tự viết ở 1.2, để hai phần không mâu thuẫn nhau.
```

**Xử lý:** Đưa vào 1.4 rồi review lại và chỉnh sửa

---

## #14 | 05:16 30/09/2026 | Claude Opus | R2
**Mục đích:** Nhờ AI research các software defect case thực tế

**Prompt:**
```
Giờ qua thực hiện requirement 2. Hãy giúp tôi research "software defects publicized between 2022 and 2026."
Không bịa nguồn
Cứ research theo các tiêu chí: 

| ID | Tên defect | Năm công bố | Tổ chức / Sản phẩm | Nhóm | Loại lỗi | Severity | Nguồn | 
| ID | Mô tả | Hậu quả | Giải pháp (thực tế) | Bài học kiểm thử |

Sau khi research xong, tôi sẽ đưa format để bạn điền vào nhé
```

**Output:** Cùng với artifact research mà AI tạo ra, ở đây chưa sử dụng, dùng nó để làm context cho prompt tiếp theo
```
Mình bắt đầu nghiên cứu 20 software defect được công bố trong giai đoạn 2022–2026, trong đó có ít nhất 5 defect liên quan AI/LLM. Mỗi defect đều sẽ kèm nguồn thật để bạn kiểm chứng.

Mình đã tổng hợp xong 20 software defect có thật, công bố trong giai đoạn 2022–2026. Trong đó 8 defect thuộc nhóm AI/LLM (vượt mức tối thiểu 5), 12 defect còn lại là Non-AI. Mỗi defect đều có nguồn gốc (postmortem, cơ quan quản lý, bản án hoặc advisory) hoặc bài của báo lớn.

- **Độ nghiêm trọng:** 9 Critical, 9 High, 2 Medium và 0 Low. Nếu giảng viên bắt buộc phải có mức Low, bạn nên bổ sung một lỗi UI nhỏ lấy từ bug tracker công khai.
- **Bài học kiểm thử quan trọng nhất:** các sự cố lớn nhất (CrowdStrike 2024, AWS 10/2025, Cloudflare 11/2025, Google Cloud 6/2025) đều giống nhau ở một điểm. Một file cấu hình hoặc dữ liệu đúng cú pháp nhưng sai ngữ nghĩa đã được đẩy ra toàn cầu mà không qua kiểm tra, không có canary và không triển khai theo giai đoạn.
- **Những chỗ AI hay viết sai, dùng để kiểm tra:**
  - CrowdStrike: template có 21 trường nhưng code chỉ truyền 20 giá trị, AI hay viết ngược lại.
  - Mata v. Avianca: chỉ có một khoản phạt 5.000 USD áp chung cho hai luật sư và hãng luật, không phải mỗi luật sư bị phạt 5.000 USD.
  - Bard: con số mất 100 tỷ USD vốn hóa bị quy hết cho lỗi của Bard, trong khi Reuters gắn nó với cả buổi ra mắt kém ấn tượng.
  - Optus: nâng cấp của Singtel chỉ là tác nhân kích hoạt, nguyên nhân gốc nằm ở các router của Optus.
- **Chi tiết cần lưu ý:**
  - Thời lượng sự cố Rogers khác nhau tùy nguồn (15 hoặc 26 giờ).
  - Nguồn không thống nhất về thời điểm vá EchoLeak.
  - Vụ Replit chỉ đáng tin ở mức trung bình vì nguồn chính là bài đăng của chính người bị hại.
  - Sự cố ChatGPT Redis được xếp vào Non-AI. Nếu giảng viên tính cả nó là AI thì nhóm AI/LLM sẽ có 9 defect.

Báo cáo còn liệt kê các ứng viên đã bị loại kèm lý do, ví dụ Southwest 2022 và Log4Shell.
```

**Xử lý:** Sử dụng thông tin mà Claude vừa research hiện tại để thực hiện tiếp mục 2

---

## #15 | 07:02 30/09/2026 | Claude Opus | R2
**Mục đích:** Điền các defect vào mục 2, đồng thời check lại thông tin

**Prompt:**
```
Giờ hãy giúp tôi điền thông tin đầy đủ vào các form này nhé:
## 2. Requirement 2 – 20 Software Defects 2022–2026

### 2.0 Thang đánh giá Severity

| Mức | Định nghĩa áp dụng trong bài |
|---|---|
| Critical | [VD: gây thiệt hại tài chính/an toàn lớn, sập hệ thống diện rộng, lộ dữ liệu quy mô lớn] |
| High | [VD: mất chức năng chính, ảnh hưởng nhiều người dùng, có workaround khó] |
| Medium | [VD: lỗi chức năng phụ, có workaround] |
| Low | [VD: lỗi hiển thị, ảnh hưởng nhỏ] |

### 2.1 Bảng 20 defect

**Bảng tổng quan:**

| ID | Tên defect | Năm công bố | Tổ chức / Sản phẩm | Nhóm | Loại lỗi | Severity | Nguồn |
|---|---|---|---|---|---|---|---|
| D01 | [...] | [2022–2026] | [...] | [AI/LLM / Non-AI] | [VD: Hallucination / Prompt injection / Bias / Logic / Config / Security...] | [...] | [link] |
| D02 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D03 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D04 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D05 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D06 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D07 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D08 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D09 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D10 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D11 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D12 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D13 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D14 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D15 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D16 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D17 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D18 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D19 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |
| D20 | [...] | [...] | [...] | [...] | [...] | [...] | [link] |

**Thống kê:** AI/LLM: [x]/20 (yêu cầu >= 5) · Critical [x] · High [x] · Medium [x] · Low [x]

**Bảng chi tiết:**

> 📝 Mỗi ô 1–3 câu. "Giải pháp" = cách hãng đã khắc phục thực tế (theo nguồn) + bài học kiểm thử (loại test nào lẽ ra bắt được lỗi này).

| ID | Mô tả | Hậu quả | Giải pháp (thực tế) | Bài học kiểm thử |
|---|---|---|---|---|
| D01 | [...] | [...] | [...] | [...] |
| D02 | [...] | [...] | [...] | [...] |
| D03 | [...] | [...] | [...] | [...] |
| D04 | [...] | [...] | [...] | [...] |
| D05 | [...] | [...] | [...] | [...] |
| D06 | [...] | [...] | [...] | [...] |
| D07 | [...] | [...] | [...] | [...] |
| D08 | [...] | [...] | [...] | [...] |
| D09 | [...] | [...] | [...] | [...] |
| D10 | [...] | [...] | [...] | [...] |
| D11 | [...] | [...] | [...] | [...] |
| D12 | [...] | [...] | [...] | [...] |
| D13 | [...] | [...] | [...] | [...] |
| D14 | [...] | [...] | [...] | [...] |
| D15 | [...] | [...] | [...] | [...] |
| D16 | [...] | [...] | [...] | [...] |
| D17 | [...] | [...] | [...] | [...] |
| D18 | [...] | [...] | [...] | [...] |
| D19 | [...] | [...] | [...] | [...] |
| D20 | [...] | [...] | [...] | [...] |

```

**Output:** File `HW01_R2.md` do AI tạo, lưu nguyên bản tại
`ai-outputs/HW01_R2.md`
```
Mình đã điền xong Requirement 2 vào file `HW01_R2.md`, gồm thang severity 4 mức, bảng tổng quan 20 defect và bảng chi tiết. Thống kê: 8/20 defect thuộc nhóm AI/LLM, gồm 9 Critical, 9 High, 2 Medium và không có Low. Dữ liệu đều lấy từ báo cáo research; mỗi dòng có 1–2 nguồn dạng link rút gọn. Mình không thêm số liệu nào ngoài nguồn. Các con số như "khoảng 3 giờ" hay "812 CAD" là mình tự cộng hoặc trừ từ mốc giờ và số tiền trong nguồn.

**Cần kiểm tra trước khi nộp:**
- **Mức Low đang là 0.** Đề không bắt buộc phải có mỗi mức một defect, nhưng nếu TA hỏi thì bạn có thể giải thích: sự cố được báo chí đưa tin thường có hậu quả lớn, nên mẫu 20 defect tự nhiên lệch về phía nặng.
- **Nhóm của D12 (ChatGPT Redis).** Mình xếp D12 vào Non-AI vì lỗi nằm ở thư viện Redis, không phải ở model. Nếu bạn muốn tính là AI thì con số AI/LLM thành 9/20.
- **Độ tin cậy của D20 (Replit) chỉ ở mức trung bình**, vì nguồn chính là bài đăng trên X của chính người bị hại. Nếu muốn an toàn hơn, bạn có thể thay D20 bằng một vụ khác, ví dụ vụ chatbot Chevrolet bán xe 1 USD, sau khi tự kiểm chứng.
- **Nên mở từng link một lần** để chắc link còn sống, và cũng là để trả lời được nếu bị hỏi lúc vấn đáp.

**Cho mục 2.2 (AI bịa hoặc lệch khi giải thích):** cách dễ nhất là hỏi một AI bất kỳ về D01 CrowdStrike hoặc D14 Mata v. Avianca. AI thường nói ngược 20/21 trường ở D01, hoặc nói "mỗi luật sư bị phạt 5.000 USD" ở D14. Đáp án đúng kèm nguồn nằm trong phần cuối của báo cáo research. Bạn cần tự hỏi, tự chụp màn hình và khoanh đỏ câu sai.

Nhớ ghi lượt research này vào prompt log và vào Audit Report.
```

**Xử lý:** Lấy dữ liệu HW01_R2.md vào, rồi sau đó kiểm tra với các resource trong research.

---

## #16 | 07:06 30/09/2026 | Claude Opus | R2
**Mục đích:** Hỏi AI kĩ hơn về case D18

**Prompt:**
```
Mình đã kiểm tra lại các phần 2.1 mà bạn làm, mình đã xác thực nó đúng với các resource mà bạn gắn link.
Giờ mình muốn bạn giúp mình giải thích 1 defect trong danh sách, chính là defect D18 - Chatbot MyCity của NYC khuyên doanh nghiệp làm trái luật
Giờ mình muốn bạn giải thích thêm về 1 số thông tin của defect này (với mỗi ý, hãy ghi nguồn tham khảo):

* Sự cố được công bố vào ngày nào?
* con số thiệt hại là bao nhiêu?
* Nguyên nhân gốc xảy ra defect này là gì?
* Có bao nhiêu người bị ảnh hưởng về vấn đề này.
* Ai đã chịu trách nhiệm cho vấn đề này
* Ai phát triển chatbot và dựa trên nền tảng gì?
* Nêu 2–3 ví dụ cụ thể về câu trả lời sai của chatbot.
* Chính quyền đã phản ứng thế nào?
* Hiện nay chatbot đó còn hoạt động không?
```

**Output:**
```
Mình sẽ đối chiếu trực tiếp với các nguồn gốc để trả lời từng ý.

Dưới đây là câu trả lời cho từng ý. Mình đối chiếu trực tiếp với các nguồn gốc, và chỗ nào nguồn không nói thì mình ghi rõ là không có.

**1. Sự cố được công bố vào ngày nào?**
Ngày **29/03/2024**. The Markup đăng bài điều tra của Colin Lecher (phối hợp với THE CITY). Chatbot thì đã ra mắt từ trước đó, ngày **16/10/2023**, ở dạng thử nghiệm beta.
Nguồn: [The Markup, 29/03/2024](https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law); [NYC Mayor's Office, 16/10/2023](https://www.nyc.gov/mayors-office/news/2023/10/mayor-adams-releases-first-of-its-kind-plan-responsible-artificial-intelligence-use-nyc)

**2. Con số thiệt hại là bao nhiêu?**
**Không có nguồn nào công bố thiệt hại** cho doanh nghiệp hay người dân. Con số duy nhất có nguồn là **chi phí làm chatbot**: gần **600.000 USD** để xây nền tảng, và khoảng **500.000 USD/năm** để duy trì. Đây là chi phí, không phải thiệt hại do lỗi gây ra.
Nguồn: [The Markup, 30/01/2026](https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law); [Entrepreneur](https://www.entrepreneur.com/business-news/nycs-first-ai-chatbot-keeps-getting-important-things-wrong/472280)

**3. Nguyên nhân gốc là gì?**
**Không có báo cáo nguyên nhân gốc chính thức.** Reuters viết rằng cả Microsoft lẫn Tòa thị chính đều không nói rõ lỗi do đâu. Những gì có nguồn:
- Chatbot chạy trên dịch vụ Microsoft Azure AI.
- Chatbot được lấy dữ liệu từ hơn 2.000 trang web doanh nghiệp của NYC.
- Microsoft cam kết làm cho câu trả lời "grounded on the city's official documentation" (bám vào tài liệu chính thức của thành phố). Câu này ngầm cho thấy trước đó câu trả lời chưa bám đủ vào tài liệu.

Kết luận "LLM hallucination do grounding chưa đủ" là **suy luận hợp lý**, không phải nguyên nhân gốc đã được xác nhận.
Nguồn: [Reuters (StreetInsider), 04/04/2024](https://www.streetinsider.com/Reuters/New+York+City+defends+AI+chatbot+that+advised+entrepreneurs+to+break+laws/23031207.html); [AP (KSAT), 03/04/2024](https://www.ksat.com/tech/2024/04/03/nycs-ai-chatbot-was-caught-telling-businesses-to-break-the-law-the-city-isnt-taking-it-down/); [NYC Mayor's Office](https://www.nyc.gov/mayors-office/news/2023/10/mayor-adams-releases-first-of-its-kind-plan-responsible-artificial-intelligence-use-nyc)

**4. Có bao nhiêu người bị ảnh hưởng?**
**Không có số liệu.** Thành phố chỉ nói chatbot "has already provided thousands of people with timely, accurate answers", tức là đã trả lời đúng cho hàng nghìn người. Đây là lời tự nhận của thành phố, không phải số người bị trả lời sai. Trong đợt kiểm tra của The Markup, cả **10/10 nhân viên** hỏi về voucher nhà ở đều nhận câu trả lời sai.
Nguồn: [The Markup, 29/03/2024](https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)

**5. Ai chịu trách nhiệm?**
Chatbot do chính quyền NYC thời Thị trưởng Eric Adams vận hành. Cơ quan trực tiếp phụ trách là **Office of Technology and Innovation (OTI)**. OTI thừa nhận có vấn đề và hứa sẽ "significantly mitigate inaccurate answers" (giảm đáng kể câu trả lời sai). Không có ai bị kỷ luật hay chịu chế tài pháp lý.
Nguồn: [Reuters (StreetInsider)](https://www.streetinsider.com/Reuters/New+York+City+defends+AI+chatbot+that+advised+entrepreneurs+to+break+laws/23031207.html)

**6. Ai phát triển và dựa trên nền tảng gì?**
OTI phối hợp với Department of Small Business Services (SBS) phát triển chatbot, đặt trên trang MyCity Business. Chatbot chạy trên **Microsoft Azure AI** (không phải ChatGPT của OpenAI).
Nguồn: [NYC Mayor's Office](https://www.nyc.gov/mayors-office/news/2023/10/mayor-adams-releases-first-of-its-kind-plan-responsible-artificial-intelligence-use-nyc); [The Markup](https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)

**7. Ví dụ câu trả lời sai**
- Chatbot nói *"No, landlords do not need to accept"* voucher Section 8. Thực tế luật NYC cấm phân biệt đối xử theo nguồn thu nhập.
- Chatbot nói *"Yes, you can take a cut of your worker's tips"*. Thực tế chủ doanh nghiệp không được lấy tiền tip của nhân viên.
- Chatbot nói nhà hàng được từ chối tiền mặt. Thực tế luật năm 2020 bắt buộc phải nhận tiền mặt.
- AP còn ghi nhận chatbot nói vẫn được phục vụ phô mai **bị chuột gặm** cho khách, và nói chủ được đuổi việc nhân viên khi họ khiếu nại quấy rối tình dục.

Nguồn: [The Markup](https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law); [AP (KSAT)](https://www.ksat.com/tech/2024/04/03/nycs-ai-chatbot-was-caught-telling-businesses-to-break-the-law-the-city-isnt-taking-it-down/)

**8. Chính quyền phản ứng thế nào?**
Thị trưởng Adams thừa nhận *"It's wrong in some areas, and we've got to fix it"* nhưng vẫn giữ chatbot hoạt động. Ông nói: *"Only those who are fearful sit down and say, 'Oh, it is not working the way we want, now we have to run away from it all together.' I don't live that way."* Thành phố bổ sung cảnh báo rằng câu trả lời không phải tư vấn pháp lý và có thể sai. Microsoft cam kết cải thiện độ chính xác.
Nguồn: [AP (KSAT)](https://www.ksat.com/tech/2024/04/03/nycs-ai-chatbot-was-caught-telling-businesses-to-break-the-law-the-city-isnt-taking-it-down/); [Reuters (StreetInsider)](https://www.streetinsider.com/Reuters/New+York+City+defends+AI+chatbot+that+advised+entrepreneurs+to+break+laws/23031207.html)

**9. Hiện nay chatbot còn hoạt động không?**
**Không.** Tháng 01/2026, chính quyền của Thị trưởng mới Zohran Mamdani quyết định khai tử chatbot. Họ gọi nó là *"functionally unusable"* (thực tế không dùng được) và coi đây là biện pháp cắt giảm ngân sách. Bản cập nhật ngày 04/02/2026 ghi nhận trang chatbot đã hiện thông báo "beta test has ended" và chuyển người dùng về NYC.gov.
Nguồn: [The Markup, 30/01/2026 (cập nhật 04/02/2026)](https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law)

---

**Cần sửa ở bảng 2.1:** ô "Giải pháp" của D18 đang ghi "chính quyền mới **dự định** gỡ bỏ". Nên sửa thành **"chính quyền mới đã gỡ bỏ chatbot (trang báo 'beta test has ended', 02/2026)"**.

**Gợi ý cho mục 2.2:** khi bạn hỏi một AI khác về D18, những chỗ nó dễ trả lời sai nhất là:
- Nói chatbot "dùng ChatGPT".
- Coi 600.000 USD là "thiệt hại".
- Bịa ra nguyên nhân gốc cụ thể hoặc số người bị ảnh hưởng.
- Nói chatbot vẫn đang chạy, nếu kiến thức của AI đó cũ hơn năm 2026.

Nhớ đối chiếu mọi câu trả lời với các nguồn ở trên. Bản giải thích này của mình cũng cần ghi vào prompt log.
```

**Xử lý:** Sau khi check lại thấy đúng như LLM nói, và không có gì hallucination nên chưa viết được, thử mở session mới rồi hỏi lại.

---

## #17 | 08:08 30/09/2026 | Gemini Flash | R2
**Mục đích:** Hỏi thông tin chi tiết về D18 với Gemini để kiểm tra có bị Hallucination không

**Prompt:**
```
Mình đang tìm hiểu về một sự cố phần mềm liên quan đến AI: chatbot MyCity của thành phố New York (NYC) đã đưa ra lời khuyên khiến doanh nghiệp làm trái luật.

Hãy giải thích giúp mình tìm hiểu thêm về các thông tin sau về sự cố này (với mỗi ý, hãy ghi nguồn tham khảo):
Sự cố được công bố vào ngày nào?
Con số thiệt hại là bao nhiêu?
Nguyên nhân gốc xảy ra defect này là gì?
Có bao nhiêu người bị ảnh hưởng về vấn đề này?
Ai đã chịu trách nhiệm cho vấn đề này?
Ai phát triển chatbot và dựa trên nền tảng gì?
Nêu 2–3 ví dụ cụ thể về câu trả lời sai của chatbot.
Chính quyền đã phản ứng thế nào?
Hiện nay chatbot đó còn hoạt động không?
```

**Output:**
```
Mình đang tìm hiểu về một sự cố phần mềm liên quan đến AI: chatbot MyCity của thành phố New York (NYC) đã đưa ra lời khuyên khiến doanh nghiệp làm trái luật.

Hãy giải thích giúp mình tìm hiểu thêm về các thông tin sau về sự cố này (với mỗi ý, hãy ghi nguồn tham khảo):
Sự cố được công bố vào ngày nào?
Con số thiệt hại là bao nhiêu?
Nguyên nhân gốc xảy ra defect này là gì?
Có bao nhiêu người bị ảnh hưởng về vấn đề này?
Ai đã chịu trách nhiệm cho vấn đề này?
Ai phát triển chatbot và dựa trên nền tảng gì?
Nêu 2–3 ví dụ cụ thể về câu trả lời sai của chatbot.
Chính quyền đã phản ứng thế nào?
Hiện nay chatbot đó còn hoạt động không?
```

**Xử lý:** Phát hiện có hallucination, hỏi lại Claude xem chính xác đó có phải Hallucination không?

---

## #18 | 08:55 30/09/2026 | Claude Opus | R2
**Mục đích:** Hỏi xác nhận lại với Claude cùng với bằng chứng của mình xem có phải là hallucination không

**Prompt:**
```
Mình vừa hỏi Gemini với câu hỏi tương tự thì có thấy câu trả lời này:
"Đơn vị cung cấp nền tảng đám mây: Microsoft (cung cấp dịch vụ Azure AI). Người phát ngôn của Microsoft tuyên bố rằng họ cung cấp nền tảng kỹ thuật và hỗ trợ khách hàng thử nghiệm, nhưng việc kiểm soát nội dung và dữ liệu đầu vào thuộc trách nhiệm quản trị của thành phố."
Nhưng nếu mình đọc ở ksat thì lại là: "to improve the service and ensure the outputs are accurate and grounded on the city’s official documentation."
Mình cảm thấy câu trả lời của Gemini giống như là đổ trách nhiệm cho quản trị của thành phố trong khi thật sự không phải như vậy. Bạn nghĩ đây có phải là hallucination và có thêm bias gì nữa không?
```

**Output:**
```
Có, đây là hallucination. Nhưng mình nghĩ nên gọi đúng tên loại lỗi, và phần "bias" cần viết thận trọng hơn cách bạn đang nghĩ.

## 1. Hallucination: bịa ra phát ngôn và gán cho Microsoft

Theo các nguồn mình kiểm tra, Microsoft chỉ có hai lần phản hồi về vụ này:

| Nguồn | Microsoft nói gì |
|---|---|
| [The Markup, 29/03/2024](https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law) | **Từ chối bình luận** |
| [AP (NBC New York)](https://www.nbcnewyork.com/news/local/nycs-ai-chatbot-was-caught-telling-businesses-to-break-the-law-the-city-isnt-taking-it-down/5287713/), [AP (KSAT)](https://www.ksat.com/tech/2024/04/03/nycs-ai-chatbot-was-caught-telling-businesses-to-break-the-law-the-city-isnt-taking-it-down/) | Microsoft cho biết đang *làm việc cùng nhân viên thành phố* "to improve the service and ensure the outputs are accurate and grounded on the city's official documentation" |

Không nguồn nào có một "người phát ngôn Microsoft" nói rằng việc kiểm soát nội dung và dữ liệu đầu vào thuộc trách nhiệm của thành phố. Nói cách khác, Gemini tạo ra một **phát ngôn không tồn tại** rồi gán cho một nguồn cụ thể. Đây là loại hallucination nguy hiểm nhất, vì câu trả lời trông như có trích dẫn nên người đọc dễ tin.

Một lưu ý: mình chưa đọc hết mọi bài báo trên đời. Cách viết an toàn trong bài là: *"không tìm thấy phát ngôn này trong các nguồn gốc (The Markup, AP, Reuters)"*.

## 2. Bias: có, nhưng nên mô tả chính xác

Chỗ bạn cần sửa lại: **thành phố thực sự có trách nhiệm**. Thành phố sở hữu và vận hành chatbot qua OTI và SBS; Thị trưởng Adams nói *"we've got to fix it"*; OTI hứa sẽ giảm câu trả lời sai. Vì vậy kết luận "thành phố chịu trách nhiệm" tự nó **không sai**. Cái sai là:
- **Gán kết luận đó cho Microsoft**, như thể Microsoft tự nói ra.
- **Làm lệch cán cân trách nhiệm.** Phát ngôn thật của Microsoft cho thấy Microsoft cùng tham gia sửa lỗi, tức là trách nhiệm chung. Bản của Gemini biến Microsoft thành bên đứng ngoài, chỉ "cung cấp nền tảng".

Như vậy có thể gọi là **framing bias** (thiên lệch trong cách trình bày): câu trả lời nghiêng về hướng giảm nhẹ trách nhiệm của nhà cung cấp công nghệ.

Về nguyên nhân, mình không kết luận được Gemini "cố ý bênh Microsoft". Giả thuyết hợp lý hơn là Gemini lấy khuôn mẫu **"Shared Responsibility Model"** quen thuộc của các nhà cung cấp cloud (nhà cung cấp lo hạ tầng, khách hàng lo dữ liệu và nội dung) rồi áp lên vụ việc cụ thể này như thể đó là phát ngôn thật. Đây là kiểu hallucination điển hình: điền vào chỗ trống bằng một câu *nghe hợp lý* thay vì một câu *có thật*. Trong báo cáo, bạn nên viết đây là **giả thuyết**, đừng viết như sự thật.

## 3. Gợi ý viết vào mục 2.2

| Mục | Nội dung |
|---|---|
| Câu AI trả lời sai | "Người phát ngôn của Microsoft tuyên bố rằng họ cung cấp nền tảng kỹ thuật... nhưng việc kiểm soát nội dung và dữ liệu đầu vào thuộc trách nhiệm quản trị của thành phố." |
| Loại | Hallucination (bịa phát ngôn và gán cho nguồn cụ thể), kèm framing bias (làm lệch cán cân trách nhiệm) |
| Sự thật theo nguồn | The Markup: Microsoft từ chối bình luận. AP: Microsoft nói đang làm việc cùng thành phố "to improve the service and ensure the outputs are accurate and grounded on the city's official documentation", tức là trách nhiệm chung, không phải đẩy trách nhiệm cho thành phố. |
| Vì sao AI sai (giả thuyết) | AI có thể đã áp khuôn mẫu "shared responsibility" phổ biến của cloud lên vụ việc cụ thể, và tạo ra một phát ngôn nghe hợp lý thay vì trích dẫn thật. |
| Cách phát hiện / phòng tránh | Với mọi câu "X tuyên bố rằng...", phải yêu cầu AI đưa link nguồn rồi tự mở nguồn đối chiếu; không chấp nhận trích dẫn không có nguồn. |

Nhớ chụp màn hình câu trả lời của Gemini, khoanh đỏ câu sai, và ghi prompt kèm timestamp vào prompt log. Câu trả lời này cũng là một ví dụ rất tốt cho phần AI Critique.
```

**Xử lý:** Xác nhận đó là hallucination thật, đồng thời đó cũng là một framing bias. Giờ trình bày vào báo cáo

---

## #19 | 09:44 30/09/2026 | Claude Opus | General
**Mục đích:** Hỗ trợ viết báo cáo mục 4

**Prompt:**
```
Được rồi. Mình đã xong hết các R1, R2, R3
Sau đây là file report hiện tại của mình
Cùng với các prompt_log mình đã sử dụng (không cần quan tâm các prompt #1 mẫu, mình đặt dàn ý trước để viết cho nhanh)
Giờ giúp mình hoàn thành mục: "4. AI Audit Report" nhé
```
*Đính kèm:* 2 file report và prompt_log hiện tại.

**Output:** File `HW01_Section4_AuditReport.md` do AI tạo, lưu nguyên bản tại
`ai-outputs/HW01_Section4_AuditReport.md`
```
Mục 4 đã xong, nằm trong file `HW01_Section4_AuditReport.md`. Có 13 artifact, dựng từ các lượt #1–#18 trong prompt log và nội dung report hiện tại của bạn. Mỗi artifact có đủ 5 mục; câu nào mình trích nguyên văn thì khớp với prompt log.

Tổng hợp theo artifact:

| Kết quả | Số lượng | Tỉ lệ |
|---|---|---|
| VALID | 5 | 38,5% |
| INVALID | 1 (của Gemini) | 7,7% |
| INCOMPLETE | 7 | 53,8% |

Riêng 15 test case do AI sinh: 14 VALID, 1 INCOMPLETE, và không có edge case thực tế nào nằm trong output của AI.

**Cần sửa trong prompt log trước khi nộp.** Mấy chỗ dưới đây dễ bị coi là khai báo sai, mà khai báo sai có thể khiến bài bị 0 điểm:
- **Các mục mẫu "#1 | 14:32 29/09/2026" phải xóa hết.** Có 1 mục ở đầu file và 5 bản lặp ở cuối file. Nội dung ghi "TC09 sai vì quạt không có hẹn giờ… TC11 thiếu bước kiểm tra độ rung", nhưng chưa từng có lượt nào như vậy. Nếu để lại, người chấm sẽ thấy đây là log bịa.
- **#17 (Gemini):** ô Output đang chép lại nguyên prompt. Bạn cần dán câu trả lời thật của Gemini vào đó, vì đây là bằng chứng chính cho mục 2.2.
- **Timestamp:** #8 ghi "35/09/2026" (không có ngày này), #9 ghi "29/09/2026" nhưng thực tế phải là 30/09.

**Các chỗ mình để hộp 📝 gợi ý, bạn tự quyết:**
- **TC03:** expected vẫn chưa có ngưỡng Pass/Fail. Nếu bạn thêm ngưỡng thì ô "Student fix" của A12 mới có thay đổi thật.
- **TC08:** đang ghi "(theo G3)", cần đổi thành "F3".
- **E2 ở mục 1.3:** bạn ghi 4/10, còn A05 mình ghi 5/10, cần thống nhất một con số.

**Nên kiểm tra lại:**
- **Số mục ISTQB:** mình dẫn §1.4.5, §4.2, §4.4.1, §5.1 và §5.5 theo syllabus v4.0. Bạn đối chiếu lại với tài liệu của thầy xem số mục có khớp không.
- **Tính tổng cho mục 7:** mình tính Gemini là 1 artifact. Nếu bạn dùng tỉ lệ này cho phần Tự đánh giá, nên nói rõ cách tính.
```

**Xử lý:** Giữ TC01–TC08 (VALID). TC09 sai vì quạt không có hẹn giờ
(INVALID). TC11 thiếu bước kiểm tra độ rung (INCOMPLETE, đã sửa).
→ AI-02 Artifact #3

---

## #20 | 10:17 30/09/2026 | Claude Opus | General
**Mục đích:** Hỗ trợ chỉnh sửa phần AI Critique

**Prompt:**
```
Đây là bản nháp mình đã viết cho: "

## 5. AI Critique

> 📝 **Hướng dẫn:** 1 đoạn **200–300 từ**, tự viết. Trả lời đủ 3 câu hỏi của đề:
> 1. AI sai / bias / thiếu ở đâu? → dẫn ví dụ cụ thể (E1–E3 mindmap, hallucination 2.2, edge case 3.4).
> 2. Vì sao AI không bắt được? → thiếu ngữ cảnh vật lý, dữ liệu huấn luyện có hạn, xu hướng trả lời "trung bình/phổ biến", tự tin khi không chắc...
> 3. Nguyên tắc rút ra khi cộng tác với AI? → 1–2 nguyên tắc cụ thể, có thể áp dụng lại ở HW sau.

[Đoạn văn 200–300 từ]

**Số từ:** [...]

---"

"Qua HW01, em thấy rằng AI ít khi sai theo một pattern để người dùng nhận diện, đáng sợ nhất là câu trả lời nào cũng cảm giác đầy đủ, có nguồn xác thực nhưng đôi khi không đúng hoặc không đủ. Ví dụ như Gemini đã Hallucination về D18 của em, bịa lời phát ngôn của Microsoft đổ lỗi cho quản trị thành phố, trong khi thực sự thì Microsoft sẽ cố gắng hỗ trợ khắc phục, sau đó nó còn gắn liền thêm nguồn PCMag làm cho người dùng an tâm rằng có nguồn. Nhưng khi nhấn vào thì không thấy phát ngôn đó ở đâu cả. Và AI có lẽ cũng thường framing bias cho các nhà cung cấp AI rằng họ thường vô tội (có thể là do Gemini hoặc ở session hiện tại). Hơn nữa qua phần thiết kế test case, có thể thấy rằng AI không thể bắt được hết các edge case được, vì nó không hề có đủ trải nghiệm, không có thiết bị thật để làm mà chỉ suy luận, nên hầu hết các test mà nó sinh ra toàn ở happy path hoặc ở chức năng chính của quạt. Và khi sinh gì đó có vẻ như nó thường thiếu/sai như là hallucination, không đủ thông tin về thị trường. Vì những điều đó, nên chúng ta phải kiểm tra lại những gì mà được AI sinh ra, phải có một nguồn sự thật để kiểm chứng lại, AI có thể tạo sinh rất mạnh, nhưng có thể một nửa số đó chưa đủ tốt, vì vậy cũng cần sự can thiệp của con người để làm cho nó tốt hơn."
Bạn nghĩ có cần chỉnh sửa gì không
```

**Output:**
```
Bản nháp của bạn trả lời đủ cả 3 câu hỏi và dài 264 từ, nằm trong khoảng 200–300. Ý mở đầu cũng là ý hay nhất bài: câu trả lời sai của AI "trông vẫn đầy đủ, có nguồn". Có 4 chỗ mình nghĩ nên sửa, xếp theo mức độ quan trọng:

**1. Có hai câu đang khẳng định quá mức.**
- *"đổ lỗi cho quản trị thành phố, trong khi thực sự thì Microsoft sẽ cố gắng hỗ trợ khắc phục"*: thành phố thực sự có trách nhiệm (họ vận hành chatbot). Cái sai của Gemini là **bịa lời phát ngôn rồi gán cho Microsoft**. Bạn nên viết đúng như vậy để khớp với mục 2.2 và A10.
- *"AI có lẽ cũng thường framing bias cho các nhà cung cấp AI rằng họ thường vô tội"*: bạn mới có 1 ví dụ, chưa đủ để nói "thường". Nếu TA hỏi thì bạn khó bảo vệ. Nên giới hạn lại, kiểu "trong trường hợp này, câu trả lời nghiêng về giảm trách nhiệm của nhà cung cấp". Phần trong ngoặc "(có thể là do Gemini hoặc ở session hiện tại)" chưa rõ nghĩa, nên bỏ.

**2. Phần edge case chưa chính xác và bỏ sót điểm mạnh nhất của bạn.**
- Nói *"toàn ở happy path"* là hơi quá, vì bộ TC của AI có state transition và decision table. Nói đúng hơn là AI **chỉ dùng input hợp lệ, mỗi lần 1 phím**.
- Bạn chưa nhắc tới phát hiện ở #5/A13: AI **có nghĩ tới** thao tác nhấn 2 phím nhưng **không đưa vào output**. Đây là chi tiết riêng của bài bạn, rất đúng tinh thần "Why did the AI fail to catch it?", nên dành 1 câu cho nó.

**3. Thiếu ví dụ từ mindmap (G9.1).** Hướng dẫn yêu cầu dẫn cả E1–E3. Chỉ cần nửa câu, ví dụ E2 (thiếu chức danh QC vì AI dùng cách gọi chức danh quốc tế, trong khi 5/10 tin ở R1 có chữ "QC").

**4. Nguyên tắc cuối bài còn chung chung.** Câu "phải kiểm tra lại, cần sự can thiệp của con người" ai cũng viết được. Nên đổi thành 2 nguyên tắc cụ thể mà bạn đã thực sự làm trong bài, ví dụ:
- Buộc AI trích nguyên văn kèm URL cho từng ý, rồi tự mở nguồn và Ctrl+F để đối chiếu.
- Cho AI sinh test case trước, rồi người tìm edge case trên thiết bị thật; sau đó hỏi AI "có gì bạn đã nghĩ tới mà không đưa vào không".

Cụm *"có thể một nửa số đó chưa đủ tốt"* nên thay bằng số liệu của bạn: 7/13 artifact bị INCOMPLETE (54%, theo mục 4.x). Như vậy phần Critique sẽ nối được với Audit Report.

**Lỗi nhỏ:**
- Xưng hô chưa thống nhất: đoạn này dùng "em", còn Audit Report dùng "tôi". Nên chọn một.
- "Hallucination" giữa câu nên viết thường.
- *"AI ít khi sai theo một pattern để người dùng nhận diện"* hơi khó hiểu. Có thể viết lại thành "lỗi của AI không có dấu hiệu dễ nhận ra".

**Về độ dài:** thêm ý 2, 3 và 4 thì bài sẽ vượt 300 từ. Bạn có thể cắt câu *"Và khi sinh gì đó có vẻ như nó thường thiếu/sai như là hallucination, không đủ thông tin về thị trường"*, vì ý này đã được phần đầu và con số 54% nói thay rồi.

Sửa xong bạn gửi lại, mình đếm từ và soát lần cuối cho. Câu chữ nên là của bạn, vì đề ghi rõ phần này "mandatory, tự viết".
```

**Xử lý:** Tham khảo ý kiến của AI, sửa lại vì cảm thấy cần thiết rồi đưa vào báo cáo

---

## #21 | 10:29 30/09/2026 | Claude Opus | General
**Mục đích:** Hỗ trợ hoàn thiện phần Mandatory Disclosure

**Prompt:**
```
```markdown
## 6. Mandatory Disclosure

> 📝 Điền cụ thể, khớp với cột "Nguồn" ở 3.3 và danh sách artifact ở mục 4. Không để lại dấu ngoặc vuông.

*"[Mindmap vai trò QA/QC (1.3), bộ test case ban đầu (3.3), ...] was initially generated by [Claude – model ...]; I reviewed and modified [section 1.3 – 3 errors E1–E3, section 3.3 – TC.., TC.., ...], added [edge cases TC13, TC14, TC15]; [section 1.1–1.2 job research, 2.1 defect verification, 3.5 execution & videos, 5 AI Critique] was written entirely by me. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category below."*

**Prohibited category (không dùng AI):** ảnh thiết bị + thẻ SV; giọng thuyết minh video; 10 screenshot tin tuyển dụng; prompt log có timestamp.

Hỗ trợ mình viết lại đoạn này theo tiếng Việt nhé. Như thể chúng ta đã cùng nhau viết report này vậy
```

**Output:**
```
Mình viết lại dựa trên đúng những gì đã diễn ra trong prompt log và mục 4. Đề phạt 0 điểm nếu khai báo sai, nên mình ghi đầy đủ cả những phần AI đã hỗ trợ, kể cả mục 4.

```markdown
## 6. Mandatory Disclosure

*"Các phần sau được **Claude (claude-opus-5-5)** tạo bản đầu tiên: khung báo cáo (dàn ý, bảng biểu, placeholder); danh sách gợi ý tin tuyển dụng J08–J10 và phần điền bảng 1.1; phần tóm tắt mô tả công việc và kỹ năng của J02–J10 (1.2); mindmap vai trò QA/QC bản gốc (1.3); bảng thống kê, bảng phân loại và đoạn nhận xét nháp ở 1.4; báo cáo research và hai bảng 20 defect (2.0, 2.1); phần giải thích D18 dùng làm đáp án đối chứng (2.2); bộ 15 test case ban đầu và các giả định về thiết bị, từ đó tôi xây dựng TC01–TC10 và bảng chức năng F1–F4 (3.2, 3.3); bản nháp AI Audit Report (mục 4). **Gemini Flash** được dùng một lần để kiểm tra hallucination (mục 2.2).*

*Tôi đã xem xét và chỉnh sửa: mục 1.1 (đối chiếu từng tin bằng tài khoản của mình, sửa mức lương J03–J10); mục 1.3 (tìm và sửa 3 lỗi E1–E3, quyết định nội dung mindmap đã sửa); mục 1.4 (phân loại J01, đếm lại kỹ năng trên 10 tin); mục 2.1 (mở và kiểm chứng toàn bộ nguồn, cập nhật D16 và D18); mục 3.3 (chọn giữ 10/15 test case của AI, lược bớt phép đo, chạy thật và điền Actual/Verdict); mục 4 (rà soát và xác nhận từng verdict).*

*Tôi đã bổ sung các edge case **TC11, TC12, TC13, TC14, TC15**, tự nghĩ ra và thử trên quạt thật trước khi hỏi lại AI.*

*Các phần do tôi tự viết hoàn toàn: nội dung J01 và toàn bộ 10 ô **AI Impact Analysis** (1.2); phần phân tích lỗi của mindmap (1.3); việc hỏi Gemini, phát hiện câu bịa và chụp minh chứng (2.2); thông tin thiết bị (3.1); việc thực thi 5 test case, quay video có thuyết minh và phần kết luận (3.5); **AI Critique** (mục 5); **Tự đánh giá** (mục 7).*

*AI Audit Report chi tiết nằm ở mục 4 và file AI-02 (Phụ lục B); toàn bộ prompt kèm timestamp nằm ở Phụ lục A. Tôi xác nhận không dùng AI để tạo bất kỳ artifact nào thuộc danh mục bị cấm dưới đây."*

**Danh mục cấm dùng AI:** ảnh thiết bị chụp cùng thẻ sinh viên; giọng thuyết minh trong video; 10 ảnh chụp màn hình tin tuyển dụng; prompt log có timestamp.


**Trước khi dán vào báo cáo, bạn cần kiểm tra mấy chỗ sau cho khớp với thực tế:**
- **`mindmap_fixed.png`:** nếu ảnh này là mình render từ file `.mmd` do bạn sửa, thì câu "quyết định nội dung mindmap đã sửa" là đúng. Nếu bạn tự vẽ bằng công cụ khác thì có thể ghi mạnh hơn.
- **Mục 2.2:** phần phân loại "hallucination + framing bias" có dựa trên xác nhận của mình (#18). Nếu muốn chặt chẽ hơn, bạn có thể thêm "(đã đối chiếu với Claude, #18)" vào câu tự viết.
- **Mục 5:** chỉ ghi "tự viết hoàn toàn" nếu bản cuối đúng là câu chữ của bạn. Mình mới góp ý, chưa viết hộ câu nào.
- **Mục 1.4:** đoạn nhận xét là mình soạn nháp. Nếu bạn đã viết lại gần như toàn bộ thì có thể chuyển nó sang nhóm "tự viết".
- **Khai báo có đúng như lời không:** "Tôi đã xem xét và chỉnh sửa" nghĩa là bạn cam kết đã thật sự kiểm tra các mục đó. Hiện còn 3 việc chưa xong nên sửa trước khi nộp: xóa các mục mẫu "#1" trong prompt log, dán output thật của Gemini vào #17, và sửa timestamp #8, #9. Nếu chưa sửa mà vẫn khai "đã rà soát" thì chính chỗ đó lại thành điểm yếu.
```

**Xử lý:** Kiểm tra lại xem có thông tin nào sai không, sau đó đưa bản hoàn thiện vào

---

## #22 | 10:36 30/09/2026 | Claude Opus | General
**Mục đích:** Hỗ trợ hoàn thiện phần phụ lục

**Prompt:**
```
## Phụ lục

### A: Prompt log

> 📝 🔒 Tự ghi, **mọi prompt** gửi AI đều phải có. Nộp kèm file riêng `prompt_log.md`; ở đây để bảng tóm tắt.

| Mã | Thời gian (HH:MM dd/mm/yyyy) | Tool / model | Mục đích | Dùng ở section | File/đoạn output |
|---|---|---|---|---|---|
| P01 | [..:.. ../../2026] | Claude [...] | [...] | [..] | [prompt_log.md#p01] |
| P02 | [...] | [...] | [...] | [...] | [...] |

Mẫu mỗi entry trong `prompt_log.md`:

```markdown
## P01 – [HH:MM dd/mm/yyyy] – Claude [model]
**Mục đích:** [...]
**Prompt:**
> [nguyên văn]
**Output:** [nguyên văn hoặc link screenshot]
**Dùng ở:** Section [..] – Audit entry A[..]

### B: AI-02, AI-03, AI-05

| Template | File | Trạng thái |
|---|---|---|
| [AI-02] AI Audit Report | `AI-02_AuditReport_23120255.[pdf/docx]` | [ ] |
| [AI-03] AI Disclosure Form (ký) | `AI-03_Disclosure_23120255.pdf` | [ ] |
| [AI-05] Privacy & Responsible Use Checklist (ký) | `AI-05_Checklist_23120255.pdf` | [ ] |
| [AI-06] Student Acknowledgement (ký tuần 1) | [đã nộp ngày ../../2026] | [ ] |

### C: Git commit log

> 📝 Chạy `git log --oneline --date=format:'%H:%M %d/%m/%Y' --pretty=format:'%h %ad %s'` trong thư mục HW01 và dán kết quả hoặc screenshot.


[commit log]


### D: Cấu trúc thư mục nộp (zip + GitHub)

23120255_HW01_AI_<grade>.zip
├── 23120255_HW01_Report.pdf
├── prompt_log.md
├── HW01_TestCases.xlsx          # sheets: Test Cases / Checklist / Test Summary Report
├── mindmap/
│   ├── mindmap_ai.png
│   └── mindmap_fixed.(png|md)
├── images/
│   ├── J01.png … J10.png
│   ├── device_with_student_id.jpg
│   ├── mantis_home.png, mantis_bug_*.png
│   └── ...
├── videos.md                    # >= 5 link YouTube Unlisted
└── ai-templates/
    ├── AI-02_AuditReport_23120255.*
    ├── AI-03_Disclosure_23120255.pdf
    └── AI-05_Checklist_23120255.pdf

Giúp tôi hoàn thiện phần này nhé
```

**Output:**
```
Mình điền dựa trên prompt log của bạn và các file đã tạo trong buổi làm việc.

```markdown
## Phụ lục

### A: Prompt log

Toàn bộ prompt và output nguyên văn nằm ở file riêng `appendix/A_prompt_log.md`. Mỗi entry gồm: mã `#n`, thời gian, công cụ, section, mục đích, prompt, output và cách xử lý. Output dạng file được lưu nguyên bản trong `appendix/ai-outputs/`. Bảng dưới là tóm tắt.

| Mã | Thời gian | Tool / model | Mục đích | Dùng ở section | Output / Audit entry |
|---|---|---|---|---|---|
| #1 | 17:38 29/09/2026 | Claude Opus 5.5 | Đưa đề bài để AI nắm context | Toàn bài | Nguyên văn trong log · A01 |
| #2 | 17:41 29/09/2026 | Claude Opus 5.5 | Hoàn thiện dàn ý báo cáo | Toàn bài | `ai-outputs/23120255_HW01_Report.md` · A01 |
| #3 | 18:34 29/09/2026 | Claude Opus 5.5 | Hỏi có nên bỏ mục 1.4 | 1.4 | Nguyên văn trong log · A01 |
| #4 | 18:48 29/09/2026 | Claude Opus 5.5 | Sinh test case cho quạt Kakashi B300 | 3.2, 3.3 | `ai-outputs/HW01_R3_TestCases_AI_Draft.md` · A12 |
| #5 | 23:44 29/09/2026 | Claude Opus 5.5 | Hỏi AI vì sao bỏ sót 5 edge case | 3.3, 3.4 | Nguyên văn trong log · A13 |
| #6 | 00:27 30/09/2026 | Claude Opus 5.5 | Tìm thêm tin tuyển dụng có yêu cầu AI | 1.1 | Nguyên văn trong log · A02 |
| #7 | 01:15 30/09/2026 | Claude Opus 5.5 | Điền bảng 10 tin tuyển dụng | 1.1 | Nguyên văn trong log · A03 |
| #8 | 01:35 30/09/2026 | Claude Opus 5.5 | Tóm tắt JD cho 1.2 | 1.2 | `ai-outputs/HW01_R1_1.2.md` · A04 |
| #9 | 02:42 30/09/2026 | Claude Opus 5.5 | Vẽ mindmap vai trò QA/QC (Mermaid) | 1.3 | `ai-outputs/mindmap_ai.mmd` · A05 |
| #10 | 02:51 30/09/2026 | Claude Opus 5.5 | Vẽ lại mindmap nhiều màu | 1.3 | `ai-outputs/mindmap_ai.png` · A05 |
| #11 | 04:58 30/09/2026 | Claude Opus 5.5 | Review câu chữ mục 1.3 | 1.3 | Nguyên văn trong log · A06 |
| #12 | 05:02 30/09/2026 | Claude Opus 5.5 | Phản biện về nguồn ISTQB | 1.3 | Nguyên văn trong log · A06 |
| #13 | 05:05 30/09/2026 | Claude Opus 5.5 | Điền thống kê và phân loại 1.4 | 1.4 | Nguyên văn trong log · A07 |
| #14 | 05:16 30/09/2026 | Claude Opus 5.5 (Research) | Research 20 software defect 2022–2026 | 2.1 | Báo cáo research trong log · A08 |
| #15 | 07:02 30/09/2026 | Claude Opus 5.5 | Điền bảng 2.0, 2.1 | 2.0, 2.1 | `ai-outputs/HW01_R2.md` · A08 |
| #16 | 07:56 30/09/2026 | Claude Opus 5.5 | Giải thích chi tiết D18 | 2.1, 2.2 | Nguyên văn trong log · A09 |
| #17 | 08:08 30/09/2026 | Gemini Flash | Hỏi D18 để kiểm tra hallucination | 2.2 | `R2_defects/R2_ai_hallucination.png` · A10 |
| #18 | 08:55 30/09/2026 | Claude Opus 5.5 | Xác nhận hallucination và bias | 2.2 | Nguyên văn trong log · A11 |
| #19 | 09:43 30/09/2026 | Claude Opus 5.5 | Soạn nháp AI Audit Report | 4 | `ai-outputs/HW01_Section4_AuditReport.md` |
| #20 | 10:17 30/09/2026 | Claude Opus 5.5 | Góp ý bản nháp AI Critique (không viết hộ) | 5 | Nguyên văn trong log |
| #21 | 10:29 30/09/2026 | Claude Opus 5.5 | Viết lại Mandatory Disclosure bằng tiếng Việt | 6 | Nguyên văn trong log |
| #22 | 10:35 30/09/2026 | Claude Opus 5.5 | Hoàn thiện Phụ lục | Phụ lục | Nguyên văn trong log |

**Tổng:** 22 lượt; Claude 21 lượt, Gemini 1 lượt.

### B: AI-02, AI-03, AI-05

| Template | File | Trạng thái |
|---|---|---|
| [AI-02] AI Audit Report (5 mục / artifact) | `ai-templates/AI-02_AuditReport_23120255.pdf` | [ ] Đã điền (nội dung như mục 4) |
| [AI-03] AI Disclosure Form | `ai-templates/AI-03_Disclosure_23120255.pdf` | [ ] Đã ký |
| [AI-05] Privacy & Responsible Use Checklist | `ai-templates/AI-05_Checklist_23120255.pdf` | [ ] Đã ký |
| [AI-06] Student Acknowledgement | Đã nộp tuần 1 | [ ] Ngày nộp: ../../2026 |

### C: Git commit log

Repo: [ThachHaoo/software-testing-2627 – HW01](https://github.com/ThachHaoo/software-testing-2627/tree/main/HW01)

[dán kết quả lệnh: git log --date=format:'%H:%M %d/%m/%Y' --pretty=format:'%h %ad %s' -- HW01]

### D: Cấu trúc thư mục nộp (zip + GitHub)

23120255_HW01_AI_<grade>.zip
├── 23120255_HW01_Report.pdf
├── HW01_TestCases.xlsx              # sheets: Test Cases / Checklist / Test Summary Report
├── R1_jobs/
│   ├── J01.png, J02_1.png, J02_2.png, J03.png … J10.png
│   ├── mindmap_QA_QC.png            # bản gốc do AI sinh
│   └── mindmap_fixed.png            # bản đã sửa (E1–E3)
├── R2_defects/
│   ├── R2_ai_hallucination.png      # Hình 2.1 – câu trả lời của Gemini
│   └── R2_defect_fact.png           # Hình 2.2 – phát ngôn thật trên AP
├── R3_device/
│   ├── AnhThietBi_TheSinhVien.jpg
│   ├── mantis_home.png              # trang chủ Mantis, username = 23120255
│   └── mantis_bug_TC14.png, mantis_bug_TC15.png
├── videos.md                        # 5 link YouTube: TC01, TC08, TC13, TC14, TC15
├── appendix/
│   ├── A_prompt_log.md
│   └── ai-outputs/
│       ├── 23120255_HW01_Report.md
│       ├── HW01_R3_TestCases_AI_Draft.md
│       ├── HW01_R1_1.2.md
│       ├── mindmap_ai.mmd, mindmap_ai.png
│       ├── HW01_R2.md
│       └── HW01_Section4_AuditReport.md
└── ai-templates/
    ├── AI-02_AuditReport_23120255.pdf
    ├── AI-03_Disclosure_23120255.pdf
    └── AI-05_Checklist_23120255.pdf


**Những chỗ cần bạn xử lý:**
- **Prompt log:** bảng tóm tắt được lập từ log của bạn, nhưng file `A_prompt_log.md` vẫn phải do bạn tự ghi, vì đây là artifact cấm dùng AI.
  - Thêm entry #19–#22 cho các lượt vừa rồi.
  - Sửa #16 từ 07:06 thành 07:56, #8 từ "35/09" thành 30/09, #9 từ 29/09 thành 30/09.
  - Xóa các mục mẫu "#1 | 14:32".
  - Dán output thật của Gemini vào #17.
- **Thiếu Mantis và Excel.** Báo cáo hiện kết thúc R3 ở mục 3.5, không có mục **3.6 Test Summary (+ Mantis)**. Đề bắt buộc nộp screenshot bug trên FIT Mantis (kèm trang chủ hiện username = MSSV) và file Excel. TC14 và TC15 đang Fail nên có sẵn 2 bug để log. Trong cây thư mục mình đã để sẵn tên file; nếu bạn đặt tên khác thì sửa lại cho khớp.
- **Git log:** chạy lệnh trong mục C sau lần commit cuối cùng rồi dán vào, để log có đầy đủ commit.
- **Mục B:** chỉ đánh dấu các ô khi đã thật sự điền và ký form. Ngày nộp AI-06 thì bạn tự điền.
```

**Xử lý:** Kiểm tra lại xem có thông tin nào sai không, rồi đưa bản hoàn thiện vào report

---

## #23 | 10:42 30/09/2026 | Claude Opus | General
**Mục đích:** Hỗ trợ hoàn thiện phần tự đánh giá và checklist

**Prompt:**
```
Giúp tôi tự đánh giá và hoàn thành Checklist nhé:

```markdown
## 7. Tự đánh giá

| No. | Tiêu chí | Điểm tối đa | Tự đánh giá | Căn cứ / tự nhận xét |
|---|---|---|---|---|
| 1 | Job Market 2026+ (10 jobs × 3 pts + AI Impact) | 40 | [..] | [VD: đủ 10 tin trong 60 ngày, x tin AI, đủ screenshot...] |
| 2 | Software Defects 2022–2026 (20 defects) | 20 | [..] | [...] |
| 3 | Physical-product test design (15 TCs + 5 videos) | 25 | [..] | [...] |
| AI-1 | [AI-02] AI Audit Report (5-section) attached | 8 | [..] | [...] |
| AI-2 | AI Critique 200–300 words + [AI-03] Disclosure attached | 4 | [..] | [...] |
| AI-3 | [AI-05] Checklist signed + anti-cheat artifacts | 3 | [..] | [...] |
| | **Tổng** | **100** | **[...]** | |

> 📝 Tổng tự đánh giá = 3 chữ số trong tên file `23120255_HW01_AI_<grade>.zip`.

**Checklist trước khi nộp:**

- [x] 10 tin đều trong 60 ngày, >= 3 tin AI, mọi screenshot thấy username + ngày
- [x] 20 defect 2022–2026, >= 5 defect AI/LLM, đủ link nguồn
- [x] 1 chỗ AI hallucinate/bias có screenshot
- [x] Mindmap AI + 3 lỗi + bản sửa (PNG/Markdown)
- [x] Ảnh thiết bị + thẻ SV cùng khung; serial đã che 4 ký tự giữa
- [x] 15 TC, >= 3 edge case SV tự tìm có chứng minh
- [x] >= 5 video <= 60s, có giọng thuyết minh, YouTube Unlisted
- [ ] File Excel: Test Cases / Checklist / Test Summary Report
- [x] AI Audit Report 5 mục cho mọi artifact + tỉ lệ VALID/INVALID/INCOMPLETE
- [x] AI Critique 200–300 từ
- [x] Mandatory Disclosure đã điền cụ thể
- [x] AI-02, AI-03 (đã ký), AI-05 (đã ký); AI-06 đã ký từ tuần 1
- [x] Prompt log .md có timestamp mọi prompt
- [ ] Đã xóa hết khối 📝 và dấu `[...]`
- [ ] Tên file zip: `23120255_HW01_AI_<grade>.zip`

```

**Output:**
```
Mình chấm theo hướng hơi khắt khe, vì TA thường trừ điểm đúng ở những chỗ bạn còn thiếu. Dưới đây là 2 kịch bản. Bảng điền sẵn theo kịch bản bạn đã sửa xong các việc còn tồn (xem danh sách cuối bài).

```markdown
## 7. Tự đánh giá

| No. | Tiêu chí | Điểm tối đa | Tự đánh giá | Căn cứ / tự nhận xét |
|---|---|---|---|---|
| 1 | Job Market 2026+ (10 jobs × 3 pts + AI Impact) | 40 | 37 | Đủ 10 tin trong 60 ngày (sớm nhất 29/08/2026), 5/10 tin yêu cầu AI (≥ 3); mỗi tin có link, screenshot có username và ngày, mô tả, kỹ năng, lương, AI Impact Analysis tách 3 ý. Có mindmap AI + 3 lỗi + bản sửa (G9.1) và tổng hợp thị trường (1.4). Tự trừ: J10 là vị trí security testing, không hẳn QA/QC; một số ô AI Impact còn chung chung; 7/10 tin không công bố lương. |
| 2 | Software Defects 2022–2026 (20 defects) | 20 | 19 | Đủ 20 defect 2022–2026, 8 defect AI/LLM (≥ 5); mỗi defect có nguồn, mô tả, severity, hậu quả, giải pháp, bài học kiểm thử; đã tự mở và kiểm chứng toàn bộ link. Tìm được 1 chỗ Gemini hallucinate + framing bias, có ảnh khoanh đỏ và nguồn đối chiếu. Tự trừ: 1 link phụ (D16) đã hết hạn; không có defect mức Low. |
| 3 | Physical-product test design (15 TCs + 5 videos) | 25 | 22 | 15 TC đủ Objective / Input / Steps / Expected / Actual / Verdict; 5 edge case tự tìm (≥ 3) có đối chiếu với output gốc của AI; 5 video ≤ 60 s có thuyết minh; 2 TC Fail được log lên Mantis. Tự trừ: quạt không có serial number (đã ghi rõ); expected của một số edge case chưa có oracle độc lập; TC15 chưa cô lập nguyên nhân bằng ổ cắm khác. |
| AI-1 | [AI-02] AI Audit Report (5-section) attached | 8 | 8 | 13 artifact, mỗi artifact đủ 5 mục; đánh giá riêng 15 TC của AI; có tỉ lệ VALID / INVALID / INCOMPLETE và kết luận khi nào nên / không nên dùng AI. |
| AI-2 | AI Critique 200–300 words + [AI-03] Disclosure attached | 4 | 4 | Critique tự viết, trong khoảng 200–300 từ, dẫn ví dụ cụ thể (Gemini/D18, edge case, mindmap); Disclosure ghi cụ thể phần AI tạo / SV sửa / SV tự viết; AI-03 đã ký. |
| AI-3 | [AI-05] Checklist signed + anti-cheat artifacts | 3 | 3 | AI-05 đã ký; ảnh thiết bị + thẻ SV, video có giọng thuyết minh, screenshot tin tuyển dụng có username, prompt log 22 lượt có timestamp đều tự làm. |
| | **Tổng** | **100** | **93** | |

**Checklist trước khi nộp:**

- [x] 10 tin đều trong 60 ngày, >= 3 tin AI, mọi screenshot thấy username + ngày
- [x] 20 defect 2022–2026, >= 5 defect AI/LLM, đủ link nguồn
- [x] 1 chỗ AI hallucinate/bias có screenshot
- [x] Mindmap AI + 3 lỗi + bản sửa (PNG/Markdown)
- [x] Ảnh thiết bị + thẻ SV cùng khung; quạt không có serial number (đã ghi rõ ở 3.1)
- [x] 15 TC, >= 3 edge case SV tự tìm có chứng minh
- [x] >= 5 video <= 60s, có giọng thuyết minh, YouTube Unlisted
- [ ] Mục 3.6 Test Summary + screenshot Mantis (trang chủ có username 23120255 + bug TC14, TC15)
- [ ] File Excel: Test Cases / Checklist / Test Summary Report
- [x] AI Audit Report 5 mục cho mọi artifact + tỉ lệ VALID/INVALID/INCOMPLETE
- [ ] AI Critique 200–300 từ (bản cuối, đã đếm lại số từ)
- [x] Mandatory Disclosure đã điền cụ thể
- [x] AI-02, AI-03 (đã ký), AI-05 (đã ký); AI-06 đã ký từ tuần 1
- [ ] Prompt log .md có timestamp mọi prompt (thêm #19–#22, sửa timestamp #8/#9/#16, xóa mục mẫu "#1 | 14:32", dán output thật của Gemini vào #17)
- [ ] Đã xóa hết khối 📝 và dấu `[...]`
- [ ] Tên file zip: `23120255_HW01_AI_093.zip`

**Vì sao mình bỏ tick 4 ô** mà trước đó bạn đã tick hoặc chưa có:
- **Mantis:** checklist cũ không có dòng này, nhưng danh sách nộp bài của đề bắt buộc phải có. Mình đã thêm vào.
- **Serial number:** ô này bạn tick "đã che 4 ký tự giữa", nhưng thực tế quạt không có serial. Mình giữ tick nhưng sửa lại câu cho đúng sự thật.
- **Prompt log:** hiện vẫn còn các mục mẫu bịa và #17 chưa có output thật. Khi chưa sửa thì không nên tick.
- **AI Critique:** bạn đang sửa lại theo góp ý, nên chỉ tick sau khi có bản cuối.

**Hai kịch bản điểm:**

| Tình trạng lúc nộp | R3 | AI-2 | AI-3 | Tổng |
|---|---|---|---|---|
| Đã làm xong Mantis, Excel, prompt log, Critique | 22 | 4 | 3 | **93** |
| Chưa làm Mantis và Excel | ~18 | 4 | 3 | **~89** |
| Prompt log vẫn còn mục mẫu hoặc output sai | – | – | 0 | có thể bị **mất cả cột AI** |

Chỗ rủi ro nhất là prompt log. Đề ghi rõ nếu thiếu Audit Report, prompt log hoặc Critique thì mất toàn bộ cột AI compliance, và khai báo sai thì bị 0 điểm. Vì vậy nên sửa prompt log trước tiên. Điểm tự đánh giá chỉ nên chốt sau khi làm xong các việc trên, và nhớ cập nhật con số trong tên file zip cho khớp.
```

**Xử lý:** Xem bản đánh giá và checklist mà Claude vừa thêm, xem có chỗ nào thiếu, chỗ nào thừa không, sửa lại rồi đưa vào.

---

## #24 | 10:46 30/09/2026 | Claude Opus | General
**Mục đích:** Xác minh không sử dụng Mantis

**Prompt:**
```
Mình không làm Mantis nhé, vì hỏi mà thầy chưa trả lời nên có lẽ bài này chưa cần Mantis
```

**Output:**
```
Được, vậy mình bỏ Mantis ra. Nhưng nên ghi rõ lý do trong báo cáo: danh sách nộp bài của đề có mục "Bug screenshots: FIT Mantis", nên nếu bài không có gì mà cũng không giải thích thì TA dễ trừ điểm.

**Cách giảm rủi ro:** thêm một mục 3.6 ngắn. Mục này ghi nhận 2 bug từ TC14 và TC15 ngay trong báo cáo (và trong sheet Test Summary của file Excel), kèm một dòng giải thích vì sao chưa có Mantis:

```markdown
### 3.6 Test Summary

| Chỉ số | Số lượng | Tỉ lệ |
|---|---|---|
| Tổng TC thiết kế | 15 | 100% |
| Đã thực thi | 15 | 100% |
| Pass | 13 | 86,7% |
| Fail | 2 | 13,3% |
| TC từ AI (giữ nguyên / đã sửa) / SV tự viết | 10 / 5 | – |

**Defect tìm được:**

| Bug ID | TC | Tóm tắt | Severity | Priority | Trạng thái |
|---|---|---|---|---|---|
| BUG-01 | TC14 | Nhấn giữ đồng thời phím 2 và 3 rồi thả ra: cả hai phím bị kẹt ở trạng thái bật, quạt vẫn chạy | High | High | New |
| BUG-02 | TC15 | Tác động nhẹ vào dây nguồn khi quạt đang chạy thì quạt tắt, dù phích vẫn cắm trong ổ | High | High | New |

> Ghi chú: Chưa log bug lên FIT Mantis vì đã hỏi giảng viên về yêu cầu này cho HW01 nhưng chưa nhận được phản hồi trước hạn nộp. Bug được ghi nhận đầy đủ tại bảng trên và sheet Test Summary trong file Excel.

Bạn kiểm tra lại dòng "Đã thực thi 15/15". Nếu thực tế bạn chỉ chạy thật 5 TC có quay video thì sửa thành 5, và ghi 10 TC còn lại là Not Run. Tuy vậy bảng 3.3 của bạn đã có Actual cho cả 15 TC, nên nếu bạn chạy đủ thì giữ nguyên số 15.

**Các chỗ cần sửa lại cho khớp:**

1. **Mục 7, dòng 3 (R3):** câu "2 TC Fail được log lên Mantis" đổi thành **"2 TC Fail được ghi nhận thành bug trong Test Summary (chưa log Mantis, đã hỏi giảng viên)"**. Điểm tự đánh giá nên hạ xuống **21** vì vẫn có rủi ro bị trừ. Tổng mới là **92**, tên file sẽ là `23120255_HW01_AI_092.zip`.
2. **Checklist:** thay dòng Mantis bằng
   `- [x] Mục 3.6 Test Summary + bảng bug (Mantis: chưa yêu cầu, đã hỏi giảng viên)`
3. **Phụ lục D:** xóa 2 dòng `mantis_home.png` và `mantis_bug_TC14.png, mantis_bug_TC15.png` trong thư mục `R3_device/`.

Nếu thầy trả lời trước hạn nộp và vẫn yêu cầu Mantis, bạn chỉ cần log 2 bug trong bảng trên, chụp màn hình rồi bỏ dòng ghi chú là xong.
```

**Xử lý:** Bỏ các Mantis ra khỏi bài và thêm ### 3.6 để thay thế cho Mantis
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