# Kế hoạch đánh giá usability – U1 (AI nháp, T2 1/10)

Theo khung **9 phần** của slide (*The 9-part test plan*). Flow U1 chốt ở `report_plan.md` mục e. 📝 = em chốt/sửa.

## 1. Mục đích

Đánh giá người dùng lần đầu có tự mua được một sản phẩm có áp mã giảm giá trên EShop web và tự kiểm tra được đơn vừa đặt hay không; tìm các điểm vướng trên flow này.

## 2. Câu hỏi cần trả lời (problem statements)

- Q1. Người dùng có tìm được sản phẩm cần mua không (ô tìm kiếm hay duyệt lưới), mất bao lâu?
- Q2. Từ giỏ hàng tới thanh toán, người dùng có biết bước tiếp theo không? Họ do dự ở đâu?
- Q3. Người dùng có tìm thấy ô mã giảm giá và hiểu số tiền sau giảm không?
- Q4. Sau khi đặt hàng, người dùng có tìm được đơn của mình và hiểu trạng thái đơn không?
- Q5. Khi gặp lỗi, họ có tự khắc phục được không? Mức tự tin và tin tưởng sau khi xong (SEQ, SUS, câu hỏi mở)?

## 3. Mục tiêu và nhiệm vụ

| Thành phần | Nội dung |
|---|---|
| Nhiệm vụ (mục tiêu giao cho người tham gia) | Mua 1 chiếc tai nghe chống ồn, dùng mã giảm giá được cửa hàng tặng, rồi kiểm tra đơn hàng đã được ghi nhận chưa và đang ở trạng thái nào |
| Trạng thái đầu | Backend vừa khởi động lại (CSDL seed); trình duyệt mở `http://localhost:5173`, **chưa đăng nhập**, giỏ trống |
| Thông tin phát cho người tham gia | Tài khoản `test@eshop.com` / `Test1234!`; mã giảm giá `VIP100` (xem ghi chú ở mục 6) |
| Tiêu chí thành công | Trong Hồ sơ → Lịch sử đơn hàng có 1 đơn mới, Tổng tiền = giá tai nghe − 100.000 ₫ (6.000.000 − 100.000 = 5.900.000 ₫), và người tham gia **nói được** trạng thái đơn |
| Mốc thời gian (benchmark) | ≤ 5 phút — giả định, chỉnh sau pilot 📝 |

Nhiệm vụ chỉ nêu mục tiêu, không nêu bước (không nói "dùng ô tìm kiếm", "vào Hồ sơ").

## 4. Hồ sơ người dùng

Người từng mua hàng online ít nhất 1 lần, chưa dùng EShop, không học lớp Software Testing HW03. Ưu tiên non-IT; cơ cấu IT/non-IT theo danh sách em đã tuyển 📝. Thông tin nhân khẩu ghi ở bảng người tham gia (em tự lập).

## 5. Phương pháp và thiết kế

- Moderated, trực tiếp, think-aloud; 1 pilot + 7 phiên chính, mỗi phiên 1 người, cùng một nhiệm vụ.
- Thứ tự mỗi phiên (~20 phút): giới thiệu + xin đồng ý (3') → nhiệm vụ (≤ 10') → SEQ (1') → SUS (3') → câu hỏi mở (5').
- Pilot dùng để kiểm: câu chữ nhiệm vụ có rõ không, flow có chạy hết không, thời gian; sửa xong mới chạy phiên chính. Kết quả pilot không tính vào 7 phiên.

## 6. Môi trường và thiết bị

- PC của em, Chrome trên Windows (= P1), `http://localhost:5173`; backend `:3000`.
- **Restart backend trước mỗi phiên** (seed lại CSDL: xoá đơn và lượt dùng mã của phiên trước).
- Quay màn hình + ghi âm khi người tham gia đồng ý; công cụ quay 📝.
- Lưu ý khi chuẩn bị (AI phát hiện khi kiểm flow bằng API 04/11, em quyết):
  - Mã `SAVE10` trả `discount_amount` âm, `final_amount` gấp 10 lần tổng (vd tổng 6.000.000 → 60.000.000) — `../eshop-sut/backend/server.js:363` trở đi. Vì vậy kit dùng `VIP100` (fixed 100.000 ₫, ngưỡng 300.000 ₫, 2 lượt/người); `BIGBUY` cũng cho kết quả đúng.
  - Giỏ hàng ở web là state React: tải lại trang (F5) hoặc gõ URL làm mất giỏ (bài học HW02). Không nhắc người tham gia; nếu xảy ra thì ghi vào phiếu quan sát.

## 7. Vai trò người điều phối (em)

- Đọc lời mở đầu, nhắc think-aloud; không gợi ý, không giải thích giao diện.
- Chỉ can thiệp khi người tham gia bế tắc: không tiến triển ≥ 2 phút hoặc tự xin trợ giúp; mỗi lần can thiệp ghi vào phiếu quan sát (tính là "có trợ giúp").
- Câu nhắc trung tính được dùng: "Bạn đang nghĩ gì?", "Bạn mong đợi điều gì sẽ xảy ra?".

## 8. Đo lường và dữ liệu thu

| Loại | Chỉ số | Nguồn |
|---|---|---|
| Hiệu năng (khách quan) | Thời gian hoàn thành; hoàn thành có/không trợ giúp; số lần chọn sai/lỗi; số lần do dự; số lần cần trợ giúp | `observation_sheet.md`, video |
| Cảm nhận (chủ quan) | SEQ (1–7) ngay sau nhiệm vụ; SUS 10 câu (0–100); 4 câu hỏi mở: rõ ràng, khôi phục lỗi, tốc độ, tin cậy | `participant_kit.md` |

Tính SUS: câu lẻ (điểm − 1), câu chẵn (5 − điểm), tổng × 2,5.

## 9. Nội dung báo cáo

Mục tiêu và nhiệm vụ; bảng 7 người tham gia (che 4 số giữa); tóm tắt từng phiên; SEQ/SUS từng người + trung bình; tỉ lệ hoàn thành và thời gian; nhóm pain point (lỗi riêng lẻ ↔ vấn đề thiết kế); findings xếp theo severity; bug thật → GitHub Issues; giới hạn của nghiên cứu. Thang severity 📝.
