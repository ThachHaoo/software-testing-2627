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
| Mốc thời gian (benchmark) | ≤ 6 phút (SV chốt 10/11: người tham gia chỉ có 5–10 phút) |

Nhiệm vụ chỉ nêu mục tiêu, không nêu bước (không nói "dùng ô tìm kiếm", "vào Hồ sơ").

## 4. Hồ sơ người dùng

Người từng mua hàng online ít nhất 1 lần, chưa dùng EShop, không học lớp Software Testing HW03. Ưu tiên non-IT; cơ cấu IT/non-IT theo danh sách em đã tuyển 📝. Thông tin nhân khẩu ghi ở bảng người tham gia (em tự lập).

## 5. Phương pháp và thiết kế

- **Remote synchronous moderated** (từ xa, đồng bộ, có điều phối) qua **Google Meet**: người tham gia dùng máy tính của mình, mở link em gửi, **chia sẻ màn hình** và think-aloud; em quan sát, ghi phiếu. 1 pilot + 7 phiên chính, mỗi phiên 1 người, cùng một nhiệm vụ.
- Quay phiên trên máy em bằng **Xbox Game Bar hoặc OBS** (màn hình Meet + tiếng) chỉ khi người tham gia đồng ý (lời mở đầu của kit).
- Thứ tự mỗi phiên (~10 phút): mở đầu 1' → nhiệm vụ ≤ 6' → Google Form (SEQ + SUS + 4 câu mở) 3'. Lý do: người tham gia chỉ có 5–10 phút (SV chốt 10/11). Kịch bản chi tiết: `usability/moderator_script.md`.
- SEQ, SUS và 4 câu hỏi mở thu bằng **Google Form** (AI dựng bằng Apps Script từ `participant_kit.md`, 19:23 10/11). CSV/Responses của form có họ tên + SĐT → **không đưa vào repo**; chỉ chép điểm SEQ/SUS và câu trả lời mở (theo mã P0x) vào JSON phiên.
- Pilot dùng để kiểm: câu chữ nhiệm vụ có rõ không, flow có chạy hết không, thời gian; sửa xong mới chạy phiên chính. Kết quả pilot không tính vào 7 phiên.

## 6. Môi trường và thiết bị

- SUT chạy trên PC của em: backend `:3000` + web Vite `:5173` của nhánh local **`usability-tunnel`** (`../eshop-sut`, commit `e33212d`, không push), công khai tạm thời qua **Cloudflare quick tunnel** (`https://<ngẫu nhiên>.trycloudflare.com`, link đổi mỗi lần chạy).
- Mỗi phiên: `powershell -ExecutionPolicy Bypass -File tools/usability_session.ps1` (restart backend → Vite → tunnel → in link) → gửi link qua Meet chat; xong phiên Ctrl+C. Hết đợt usability: `tools/sut_main.ps1` đưa SUT về `main`.
- **Restart backend trước mỗi phiên** (seed lại CSDL: xoá đơn và lượt dùng mã của phiên trước) – đã nằm trong `usability_session.ps1`.
- Đã thử 10/11: em mở link bằng điện thoại qua 4G, đi hết luồng đăng nhập → tìm SP → thêm giỏ → VIP100 → đặt hàng → thấy đơn đã giảm giá trong Hồ sơ.
- **Khác biệt so với môi trường chạy checklist (T1/T3):**
  - Trình duyệt, hệ điều hành, độ phân giải là **của người tham gia** (ghi vào phiếu quan sát), không phải P1/P2/P3.
  - Truy cập **qua Internet** (tunnel Cloudflare) thay vì `localhost` → độ trễ cao hơn; thời gian hoàn thành có thể bao gồm độ trễ mạng.
  - Nhánh `usability-tunnel` **chỉ đổi URL API**: `http://localhost:3000/api` → đường dẫn tương đối `/api` (Vite proxy sang `:3000`) + cho phép host `*.trycloudflare.com`; giao diện và logic giống `main` @ `de0f48f`.
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
