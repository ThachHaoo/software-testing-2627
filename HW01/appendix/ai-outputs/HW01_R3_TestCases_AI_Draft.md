# R3 – Bộ test case do AI sinh (bản nháp để audit)

**Thiết bị:** Quạt điện Kakashi, Model B300
**Tool:** Claude (claude-opus-5-5) · **Thời gian:** [HH:MM 29/09/2026] → ghi vào prompt log với mã `P[..]`
**Nguồn tất cả TC:** `AI` (sau khi review, bạn đổi thành `AI*` nếu có sửa)

## Giả định của AI (bạn cần kiểm tra lại trên thiết bị thật)

| # | Giả định | Nếu sai thì ảnh hưởng TC nào |
|---|---|---|
| G1 | Bảng điều khiển gồm các phím cơ dạng piano: 0 (tắt), 1, 2, 3. Nhấn một phím số thì phím đang chọn bật lên. | TC01–TC07, TC12 |
| G2 | Chế độ xoay được bật/tắt bằng núm cơ (nhấn xuống/kéo lên) trên đỉnh hộp motor. | TC08–TC11 |
| G3 | Cơ cấu xoay chạy chung motor cánh, nên xoay chỉ hoạt động khi quạt đang quay. | TC11 |
| G4 | Nguồn điện 220V / 50Hz, dùng ổ cắm dân dụng. | Tất cả |
| G5 | Không có hẹn giờ, remote hay chế độ gió tự nhiên. | Phạm vi |

## Điều kiện chuẩn (PRE) và cách đo

- **PRE:** quạt đặt trên mặt bàn phẳng, khô, đã cắm điện 220V. Phím ở 0, xoay tắt, đầu quạt hướng thẳng. Phòng không bật quạt/điều hòa khác.
- **Đo tốc độ gió (tương đối):** treo dải khăn giấy dài khoảng 15 cm cách mặt quạt 1 m, ngang tâm cánh, rồi quan sát góc lệch của dải giấy. Có thể dùng thêm app đo độ ồn (dB) trên điện thoại, đặt cách quạt 1 m.
- **Đo xoay:** dán băng keo đánh dấu 2 biên của đầu quạt trên mặt bàn. Dùng đồng hồ bấm giờ đo thời gian 1 chu kỳ (trái → phải → trái).
- **Đo độ ổn định:** dùng bút đánh dấu vị trí 4 góc đế quạt lên giấy lót.

## Bảng test case

| TC ID | Objective | Kỹ thuật | Precondition | Input / Test data | Steps | Expected | Actual | Verdict | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| TC01 | Bật quạt ở số 1 từ trạng thái tắt | EP (lớp "tốc độ 1") | PRE | Phím 1 | 1. Nhấn phím 1<br>2. Quan sát cánh và dải giấy trong 10 s | Phím 1 giữ ở trạng thái nhấn. Cánh bắt đầu quay trong ≤ 3 s và đạt tốc độ ổn định. Dải giấy lệch nhẹ. Không có tiếng lạ. | [...] | [...] | AI |
| TC02 | Bật quạt ở số 2 từ trạng thái tắt | EP (lớp "tốc độ 2") | PRE | Phím 2 | 1. Nhấn phím 2<br>2. Quan sát 10 s | Phím 2 giữ. Cánh quay ổn định. Dải giấy lệch nhiều hơn so với TC01. | [...] | [...] | AI |
| TC03 | Bật quạt ở số 3 từ trạng thái tắt | EP (lớp "tốc độ 3") | PRE | Phím 3 | 1. Nhấn phím 3<br>2. Quan sát 10 s | Phím 3 giữ. Cánh quay mạnh nhất. Dải giấy lệch nhiều nhất trong 3 mức. Quạt không rung lắc bất thường. | [...] | [...] | AI |
| TC04 | Tắt quạt bằng phím 0 khi đang chạy tối đa | State transition (3 → 0) | Quạt đang ở số 3 ≥ 30 s | Phím 0 | 1. Nhấn phím 0<br>2. Bấm giờ từ lúc nhấn đến khi cánh dừng hẳn | Phím 3 bật lên. Motor ngắt điện ngay. Cánh quay chậm dần rồi dừng hoàn toàn, không quay ngược, không có tiếng va chạm. Ghi lại thời gian dừng (s). | [...] | [...] | AI |
| TC05 | Tốc độ tăng dần đúng thứ tự 1 < 2 < 3 | State transition (1 → 2 → 3) | PRE; app đo dB sẵn sàng | Phím 1, 2, 3 (mỗi mức giữ 15 s) | 1. Nhấn 1, chờ 15 s, ghi dB và góc lệch dải giấy<br>2. Nhấn 2, lặp lại<br>3. Nhấn 3, lặp lại | Cả dB và góc lệch dải giấy tăng dần theo thứ tự số 1 < số 2 < số 3. Mỗi lần chuyển số, chỉ phím mới được giữ. | [...] | [...] | AI |
| TC06 | Chuyển trực tiếp từ số 3 xuống số 1 | State transition (3 → 1, nhảy cóc) | Quạt ở số 3 ≥ 15 s | Phím 1 | 1. Nhấn phím 1<br>2. Quan sát 15 s | Phím 3 bật lên, phím 1 giữ. Cánh giảm tốc về mức số 1 (bằng TC01), không dừng hẳn giữa chừng. | [...] | [...] | AI |
| TC07 | Chuyển trực tiếp từ số 1 lên số 3 | State transition (1 → 3, nhảy cóc) | Quạt ở số 1 ≥ 15 s | Phím 3 | 1. Nhấn phím 3<br>2. Quan sát 15 s | Phím 1 bật lên, phím 3 giữ. Cánh tăng tốc lên mức số 3 (bằng TC03), không có tiếng rít hay giật. | [...] | [...] | AI |
| TC08 | Bật chế độ xoay khi quạt đang chạy | Decision table (tốc độ = 1, xoay = Bật) | Quạt ở số 1, xoay tắt, đã dán mốc biên | Núm xoay: bật | 1. Bật núm xoay<br>2. Bấm giờ 3 chu kỳ liên tiếp<br>3. Quan sát 2 biên | Đầu quạt xoay qua lại đều giữa 2 biên. Thời gian các chu kỳ gần bằng nhau (chênh ≤ 10%). Không giật, không kẹt tại biên. | [...] | [...] | AI |
| TC09 | Tắt xoay giữa hành trình | State transition (Xoay → Dừng xoay) | Quạt số 2, đang xoay, đầu quạt ở khoảng giữa 2 biên | Núm xoay: tắt | 1. Tắt núm xoay khi đầu quạt ở giữa hành trình<br>2. Quan sát 10 s | Đầu quạt dừng tại vị trí hiện tại (hoặc chỉ trôi rất ít), cánh vẫn quay số 2 bình thường. | [...] | [...] | AI |
| TC10 | Bật núm xoay khi quạt đang tắt | Decision table (tốc độ = 0, xoay = Bật) | PRE | Núm xoay: bật; phím 0 | 1. Bật núm xoay<br>2. Quan sát 10 s<br>3. Nhấn phím 1 và quan sát tiếp | Bước 2: đầu quạt không xoay, cánh không quay. Bước 3: cánh quay và đầu quạt bắt đầu xoay (theo G3). | [...] | [...] | AI |
| TC11 | Nhấn lại phím đang được chọn / nhấn 0 khi đã tắt | EP (thao tác thừa) | a) Quạt ở số 2; b) Quạt đang tắt | a) Phím 2; b) Phím 0 | 1. (a) Nhấn lại phím 2, quan sát 5 s<br>2. (b) Chuyển về trạng thái tắt, nhấn lại phím 0, quan sát 5 s | (a) Quạt tiếp tục chạy số 2, không bị tắt hay đổi số. (b) Quạt vẫn tắt, không có phím nào bị kẹt. | [...] | [...] | AI |
| TC12 | Mất điện khi đang chạy và có điện trở lại | Error guessing / State transition | Quạt số 2, xoay bật | Rút phích cắm, chờ 10 s, cắm lại | 1. Rút phích<br>2. Chờ cánh dừng hẳn<br>3. Cắm lại phích | Bước 2: quạt dừng. Bước 3: vì phím cơ vẫn giữ số 2, quạt tự chạy lại ở số 2 và vẫn xoay ngay khi có điện (cần lưu ý an toàn: người dùng có thể không lường trước). | [...] | [...] | AI |

## Lý do chọn input (gợi ý của AI – bạn phải tự hiểu để trả lời vấn đáp)

| TC | Lý do |
|---|---|
| TC01–TC03 | Tốc độ là miền rời rạc {0,1,2,3}, mỗi giá trị là một lớp tương đương riêng nên mỗi lớp cần 1 TC. |
| TC04 | Tắt từ số 3 là trường hợp khó nhất vì quán tính lớn nhất; nếu dừng an toàn ở số 3 thì các số thấp hơn cũng an toàn. |
| TC05 | Kiểm tra quan hệ thứ tự giữa các mức, không chỉ kiểm tra từng mức riêng lẻ. |
| TC06, TC07 | Chuyển tiếp không liền kề (nhảy cóc) thường bị bỏ qua nếu chỉ test 1→2→3. |
| TC08–TC11 | Bảng quyết định 2 yếu tố: tốc độ (0 / thấp / cao) × xoay (bật / tắt), chọn các tổ hợp có rủi ro. |
| TC10 | Hai biên của góc xoay là vị trí cơ cấu đổi chiều, nơi dễ kẹt hoặc va đập nhất. |
| TC13 | Phím cơ giữ trạng thái, nên có điện lại quạt tự chạy. Đây là hành vi cần xác nhận. |
| TC14, TC15 | Số 3 + xoay là tải cơ học và rung lớn nhất. |

## Gợi ý chọn ≥ 5 TC để quay video (≤ 60 s mỗi video)

TC05 (tăng dần 1→2→3), TC06 (nhảy cóc 3→1), TC08 hoặc TC10 (xoay), TC11 (xoay khi tắt), TC13 (mất điện), cùng **ít nhất 1 edge case của bạn**. Không nên quay TC14 vì kéo dài 30 phút, chỉ cần ghi kết quả.
