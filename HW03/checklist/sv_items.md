# HW03 – T1 bước 2b: Item em tự bổ sung 🔒

> Khung do AI dựng (chỉ cấu trúc + quy tắc viết, không có ví dụ item). Nội dung từng item do em tự viết. Xoá khối hướng dẫn này trước khi nộp.
>
> **Quy tắc viết**
> - `ia`: đúng 1 mã IA-01 / IA-02 / IA-03 / IA-04.
> - `man_hinh`: trong phạm vi C2 (Đăng nhập · Quên mật khẩu B1 / B2 · Hồ sơ · Lịch sử đơn · navbar khi đã đăng nhập).
> - `muc_kiem_tra`: 1 điều cần kiểm, viết trung lập (không viết sẵn kết quả lỗi).
> - `can_cu`: điều khoản SRS `FR-xx (README.md:dòng)` / heuristic (tên + số) / checklist theo control trong slide / WCAG SC / giả định mới GA4+ do em chốt (ghi ở mục Giả định). Không dùng "các app thường làm", hành vi SUT quan sát được hay logic code.
> - `expected`: quan sát được ở đâu, bằng cách nào + một câu "Fail nếu …".
> - `nen_tang`: P1, P2, P3. Nền tảng nào N/A thì ghi kèm mã giả định.
> - `uu_tien`: Mandatory / Optional.
> - `luc_them`: trước khi chạy / trong lúc chạy P1 / P2 / P3 (ghi trung thực).
> - `ly_do_AI_bo_sot.loai`: prompt (chất lượng input của em) / giới hạn model / đặc điểm giao diện / khác.
> - `ly_do_AI_bo_sot.giai_thich`: 1–3 câu, lời của em.
> - Không trùng 68 item CL-01…CL-68. Trường để trống → AI ghi "(SV chưa ghi)", không tự điền.

## Giả định mới (nếu có)

| Mã | Nội dung | Loại (quyết định Expected / phạm vi) | Lý do em chốt |
|---|---|---|---|
| GA4 | Bàn phím ảo trên mobile (P3) khi bật lên đẩy viewport hoặc che một phần form không được làm che khuất nút submit hoặc input đang focus. | Phạm vi UI/Usability trên Mobile (P3) | Đặc thù của thiết bị di động thật khi người dùng nhập dữ liệu form. |

## Item

### SV-01
- ia: IA-01
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Hiển thị con trỏ focus (Focus Ring/Indicator) rõ ràng khi duyệt bằng bàn phím
- can_cu: WCAG 2.2 SC 2.4.7 (Focus Visible); Norman #1 (Visibility); Slide "Checklist - Text Box", Slide "Checklist - Button"
- expected: Bấm phím Tab để điều hướng qua các input/button trên form: phần tử đang nhận focus phải xuất hiện viền đổi màu hoặc khung viền bao quanh (focus ring) rõ ràng. Fail nếu không thấy con trỏ focus hoặc viền focus bị ẩn/mờ (`outline: none` không có viền thay thế).
- nen_tang: P1, P2 (P3 N/A theo NA1)
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: Ở bản v1, AI chỉ tập trung tạo item kiểm tra thứ tự Tab (Tab Order - CL-10..12) mà bỏ qua khía cạnh thị giác (Focus Visibility) của con trỏ bàn phím theo tiêu chuẩn Accessibility (WCAG).

### SV-02
- ia: IA-02
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu
- can_cu: Shneiderman #8 (Giảm tải trí nhớ ngắn hạn); Nielsen #7 (Linh hoạt và hiệu quả); Slide "Checklist - Text Box"
- expected: *Tiền điều kiện:* Trình duyệt đã lưu thông tin đăng nhập/tài khoản trước đó.<br>Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit. Fail nếu bất kỳ vế nào (dán hoặc autofill) bị hệ thống ngăn chặn/làm sai lệch dữ liệu.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: AI chỉ quét cấu trúc mã nguồn tĩnh (HTML/React JSX) nên chỉ kiểm tra thuộc tính `type`, `required`, `placeholder` mà không lường trước các hành vi tương tác thực tế của người dùng như dán mã OTP hoặc dùng trình quản lý mật khẩu Autofill.

### SV-03
- ia: IA-02
- man_hinh: Đăng nhập, Quên mật khẩu B2, Hồ sơ
- muc_kiem_tra: Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại
- can_cu: Slide "Checklist - input-field validation" (Golden Rule: "On error, return focus to the offending field"); Shneiderman #5 (Xử lý lỗi đơn giản)
- expected: Nhập dữ liệu sai quy tắc (ví dụ: SĐT sai định dạng ở Hồ sơ hoặc Mật khẩu mới không đủ điều kiện ở Quên mật khẩu B2) rồi bấm submit: sau khi thông báo lỗi xuất hiện, con trỏ gõ phím (cursor) phải tự động quay lại focus ở đúng ô bị lỗi đó. Fail nếu con trỏ nhảy mất focus hoặc không quay lại ô nhập bị lỗi.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: Prompt chưa chỉ định cụ thể nguyên tắc Golden Rule từ slide validation vào yêu cầu sinh, nên AI bỏ qua quy tắc xử lý con trỏ focus khi form gặp lỗi.

### SV-04
- ia: IA-01
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio)
- can_cu: WCAG 2.2 SC 1.4.3 (Contrast Minimum)
- expected: Kiểm tra bằng công cụ DevTools Accessibility / Lighthouse: tỉ lệ tương phản màu sắc của chữ (văn bản, label, placeholder, text trên button) so với màu nền đạt tối thiểu 4.5:1 (đối với chữ thường). Fail nếu tỉ lệ tương phản < 4.5:1 khiến chữ mờ khó đọc.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: Prompt không nhắc đến các tiêu chuẩn khả năng truy cập (Accessibility) và AI không trực tiếp vận hành SUT để kiểm tra giao diện thực tế.

### SV-05
- ia: IA-01
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Kích thước vùng tương tác cảm ứng (Touch Target Size) của các nút và link trên thiết bị di động
- can_cu: WCAG 2.2 SC 2.5.8 (Target Size Minimum - 24x24px / 44x44px)
- expected: Trên màn hình di động P3 (hoặc DevTools Mobile Emulator), dùng thước đo DevTools kiểm tra chiều cao và chiều rộng vùng bấm của các nút ('Sign In', 'Lấy mã OTP', 'Cập nhật') và các liên kết ('Quên mật khẩu?', 'Đăng ký ngay'): vùng bấm phải đạt tối thiểu 24x24 px (khuyến nghị 44x44 px) và không nằm quá sát nhau gây bấm nhầm. Fail nếu nút/link quá nhỏ (< 24px) khó thao tác bằng ngón tay.
- nen_tang: P1, P2 (P3 N/A theo NA1)
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: AI xem nền tảng P3 tương tự như một trình duyệt web thông thường mà không nghĩ tới đặc thù thao tác bằng ngón tay trên màn hình cảm ứng di động.

### SV-06
- ia: IA-04
- man_hinh: Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Chống gửi trùng dữ liệu (Debounce/Disable) khi nhấp đúp/nhấp liên tiếp vào nút submit ở điều kiện mạng bình thường
- can_cu: Slide "Double-submit on double-click"; Nielsen #5 (Phòng ngừa lỗi)
- expected: Ở điều kiện mạng bình thường (không bật throttling), nhấp chuột thật nhanh (double-click) vào nút 'Lấy mã OTP', 'Đặt lại mật khẩu' hoặc 'Cập nhật': hệ thống lập tức khóa nút hoặc debounce request sao cho chỉ có đúng 1 request API được gửi đi. Fail nếu gửi từ 2 request trở lên hoặc hiển thị nhiều thông báo trùng lặp.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: prompt
  - giai_thich: AI đã nghĩ tới trường hợp mạng chậm (CL-53), nhưng do slide "Double-submit" nằm ngoài phần ngữ cảnh AI đã đọc nên AI bỏ sót kịch bản người dùng nhấp đúp chuột nhanh ở điều kiện mạng bình thường cho các form khác Đăng nhập.

<!-- Thêm item: chép nguyên khối ### SV-xx ở trên, tăng số. -->
