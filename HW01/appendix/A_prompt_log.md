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

## #12 | 05:02 30/09/2026 | Claude Opus | R3
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

## #13 | 05:05 30/09/2026 | Claude Opus | R3
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