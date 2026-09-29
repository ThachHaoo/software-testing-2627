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