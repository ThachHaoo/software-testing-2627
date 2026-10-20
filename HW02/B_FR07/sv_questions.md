# B_FR07 – Câu hỏi khi chuẩn hoá case SV (bước 5b)

Case SV đã chép vào `testcases.json` (suite TS-SV-UI, TS-SV-API), giữ nguyên văn Tiêu đề, EC, Expected, Lý do. AI không tự điền các chỗ dưới đây; case liên quan có notes "CHỜ SV làm rõ (Qx)".

## Chặn bước 6 (cần trả lời trước khi viết script cho case đó)

| Mã | Case | Chỗ mơ hồ | Phương án |
|---|---|---|---|
| Q1 | TC-FR07-202 | Expected "Tab 2 thấy id 5" chưa nói Số lượng/Thành tiền sau '+' ở Tab 2, và Tab 1 quan sát gì. | SV ghi Expected đầy đủ cho cả hai tab |
| Q2 | TC-FR07-203 | EC mục tiêu là EC5 (lớp không hợp lệ "Không phải số", giỏ không đổi theo B2) nhưng Expected là chấp nhận Số lượng 100000 (hành vi của lớp hợp lệ EC1). | (a) `1e5` thuộc EC1, Expected giữ nguyên · (b) thuộc EC5, Expected đổi thành bị từ chối |
| Q3 | TC-FR07-204 | (1) EC phủ EC26 (khách) nhưng cột Đăng nhập = user {ts}. (2) "sửa token/cart": giỏ web không lưu localStorage (B0d), vậy sửa khoá nào? (3) F5 làm mất giỏ (B0d, B10) nên Giỏ ban đầu "TC: id 2" không quan sát được sau F5. | SV chọn: khoá localStorage cần sửa; EC đăng nhập; giữ hay bỏ cột Giỏ ban đầu |
| Q4 | TC-FR07-205 | Cột kỹ thuật ghi "GB"; schema nhận EP/BVA/EG/ST. | (a) EG · (b) giá trị khác (SV ghi rõ, AI vá schema nếu cần) |
| Q5 | TC-FR07-212 | Tiêu đề: id là object `{"id": 1}`; cột id lại ghi `[1, 2, 3]` (giống TC-211). Linter báo TC-211/212 trùng dữ liệu. | (a) cột id = `{"id": 1}` · (b) giữ `[1, 2, 3]` |
| Q6 | TC-FR07-215 | Expected nói "Thành tiền không bị tràn số", nhưng phản hồi API không có Thành tiền (GET /api/cart trả lại phần tử như đã gửi, server.js:284–288). | (a) quan sát trường `quantity` trong GET /api/cart · (b) quan sát giá trị khác (SV ghi rõ) |

## Không chặn (2 điểm)

- **Kỹ thuật (technique) để trống ở 14 case:** TC-200…204 và TC-207…215. SV không ghi nên AI để trống, check_domain báo 14 WARN. Chỉ TC-206 có "EG".
- **Expected chưa có nguồn SRS hoặc mã giả định:**
  - TC-200: không bật alert;
  - TC-201: Console không có lỗi;
  - TC-204: không màn hình trắng, tự xoá storage hỏng;
  - TC-207: name phải được sanitize/escape. SEC-04 đã gỡ khỏi phạm vi ở bước 3;
  - TC-213: không mất request.

  SV không ghi chúng là giả định nên AI chưa gán mã B mới. Nếu SV muốn ghi thành giả định, mã kế tiếp là **B23**.
- Ghi chú thêm (không phải câu hỏi):
  - TC-213 và TC-214 khác nhau ở cách gửi (50 request song song, Content-Type: text/plain) chứ không ở cột dữ liệu, nên linter báo "identical data". Ngoại lệ quy trình đã ghi trong notes của từng case.
  - Linter báo 11 WARN "title thiếu CONDITION". Tiêu đề giữ nguyên văn SV.

## Trả lời của SV (áp ở 5/7c)

| Mã | Trả lời |
|---|---|
| Q1 | TC-FR07-202 bỏ: SRS không quy định đồng bộ giữa các tab. |
| Q2 | TC-FR07-203: ec_target đổi EC5 → EC1 (Expected coi `1e5` là hợp lệ). |
| Q3 | TC-FR07-204 bỏ khỏi B_FR07: ý thuộc phần xác thực, xem xét ở feature khác. |
| Q4 | Mọi case SV technique = EG; TC-205, 211, 212 thêm `approach: gray-box`. |
| Q5 | TC-FR07-212: cột id = `{"id": 1}` (SV điền nhầm mảng ở 5/7). |
| Q6 | TC-FR07-215: Expected = HTTP 2xx và GET /api/cart trả quantity đúng bằng giá trị đã gửi; assumptions B1. |
| — | TC-FR07-207 bỏ: không có điểm quan sát / căn cứ SRS (cùng lý do EC32). |
