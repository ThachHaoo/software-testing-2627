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
- can_cu: WCAG 2.2 SC 2.4.7 (Focus Visible); Norman #1 (Visibility); Slide "Checklist - Text Box & Button"
- expected: Bấm phím Tab để điều hướng qua các input/button trên form: phần tử đang nhận focus phải xuất hiện viền đổi màu hoặc khung viền bao quanh (focus ring) rõ ràng. Fail nếu không thấy con trỏ focus hoặc viền focus bị ẩn/mờ (`outline: none` không có viền thay thế).
- nen_tang: P1, P2 (P3 N/A theo NA1)
- uu_tien: Mandatory
- luc_them: trong lúc chạy P1
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI thường chỉ tập trung tạo item kiểm tra thứ tự Tab (Tab Order - CL-10..12) mà bỏ qua khía cạnh thị giác (Focus Visibility) của con trỏ bàn phím theo tiêu chuẩn Accessibility (WCAG).

### SV-02
- ia: IA-02
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu
- can_cu: Shneiderman #8 (Giảm tải trí nhớ ngắn hạn); Nielsen #7 (Linh hoạt và hiệu quả); Slide "Checklist - Text Box"
- expected: Thực hiện thao tác Paste (Ctrl+V) hoặc chọn gợi ý Autofill của trình duyệt vào các ô Email, OTP, Mật khẩu: dữ liệu phải được điền chính xác vào ô nhập và form chấp nhận dữ liệu đó khi submit. Fail nếu ô nhập chặn thao tác Paste hoặc không nhận giá trị Autofill từ trình duyệt.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trong lúc chạy P3
- ly_do_AI_bo_sot:
  - loai: đặc điểm giao diện
  - giai_thich: AI chỉ quét cấu trúc mã nguồn tĩnh (HTML/React JSX) nên chỉ kiểm tra thuộc tính `type`, `required`, `placeholder` mà không lường trước các hành vi tương tác thực tế của người dùng như dán mã OTP hoặc dùng trình quản lý mật khẩu Autofill.

### SV-03
- ia: IA-02
- man_hinh: Đăng nhập, Quên mật khẩu B2, Hồ sơ
- muc_kiem_tra: Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại
- can_cu: Slide "Checklist - input-field validation" (Golden Rule: "On error, return focus to the offending field"); Shneiderman #5 (Xử lý lỗi đơn giản)
- expected: Nhập dữ liệu sai quy tắc (ví dụ: SĐT sai định dạng ở Hồ sơ hoặc Mật khẩu mới không đủ điều kiện ở Quên mật khẩu B2) rồi bấm submit: sau khi xuất hiện thông báo lỗi và đóng thông báo, con trỏ gõ phím (cursor) phải tự động quay lại focus ở đúng ô bị lỗi đó. Fail nếu con trỏ nhảy mất focus hoặc không quay lại ô nhập bị lỗi.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trước khi chạy
- ly_do_AI_bo_sot:
  - loai: chất lượng input prompt
  - giai_thich: Prompt ban đầu chỉ yêu cầu kiểm tra sự xuất hiện của thông báo lỗi (CL-22, CL-23, CL-30) mà không yêu cầu cụ thể việc kiểm tra con trỏ focus sau khi lỗi xảy ra theo quy tắc Golden Rule trong slide giảng dạy.

### SV-04
- ia: IA-01
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio)
- can_cu: WCAG 2.2 SC 1.4.3 (Contrast Minimum); Slide "Accessibility & colour-blindness checks" (Colour Blindness Simulator / Page Filter)
- expected: Kiểm tra bằng công cụ DevTools Accessibility / Lighthouse: tỉ lệ tương phản màu sắc của chữ (văn bản, label, placeholder, text trên button) so với màu nền đạt tối thiểu 4.5:1 (đối với chữ thường). Fail nếu tỉ lệ tương phản < 4.5:1 khiến chữ mờ khó đọc.
- nen_tang: P1, P2, P3
- uu_tien: Optional
- luc_them: trong lúc chạy P2
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI khi đọc code CSS/Tailwind chỉ kiểm tra được sự tồn tại của tên màu (ví dụ `text-yellow-300`, `bg-blue-600`) mà không thể tính toán hay đánh giá trực quan tỷ lệ tương phản thực tế trên màn hình hiển thị.

### SV-05
- ia: IA-01
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Bố cục form khi bàn phím ảo (Virtual Keyboard) hiển thị trên di động
- can_cu: Giả định GA4; Slide "Why GUI testing is hard - Unsolicited events / Window management"
- expected: Trên di động P3, chạm vào một ô input bất kỳ để bật bàn phím ảo: màn hình tự động cuộn nhẹ để giữ ô input và nút submit của form luôn nằm trong vùng nhìn thấy được, không bị bàn phím che khuất hoàn toàn. Fail nếu bàn phím ảo che mất input/nút submit mà người dùng không thể cuộn tới để bấm.
- nen_tang: P3
- uu_tien: Mandatory
- luc_them: trong lúc chạy P3
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI không thể mô phỏng được hành vi vật lý của hệ điều hành di động (OS Virtual Keyboard Pop-up) khi gõ phím trên thiết bị di động thật.

### SV-06
- ia: IA-04
- man_hinh: Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ
- muc_kiem_tra: Chống gửi trùng dữ liệu (Debounce/Disable) khi click liên tiếp vào nút submit
- can_cu: Slide "Double-submit on double-click" (No debounce -> duplicate orders); Nielsen #5 (Phòng ngừa lỗi)
- expected: Nhấp chuột thật nhanh (double-click hoặc multi-click) vào nút 'Sign In', 'Đặt lại mật khẩu' hoặc 'Cập nhật': nút phải lập tức bị vô hiệu hóa (disabled) ngay ở click đầu tiên hoặc debounce request để chỉ gửi đúng 1 request API lên backend. Fail nếu bấm đúp gửi từ 2 request trở lên hoặc làm bắn thông báo trùng lặp.
- nen_tang: P1, P2, P3
- uu_tien: Mandatory
- luc_them: trong lúc chạy P1
- ly_do_AI_bo_sot:
  - loai: giới hạn model
  - giai_thich: AI đã có item CL-53 kiểm tra chống gửi trùng khi mạng chậm (Slow 3G), nhưng bỏ sót trường hợp người dùng nhấp đúp chuột nhanh (double-click fast tap) ở điều kiện mạng bình thường - một lỗi GUI rất phổ biến được nêu trong Slide.

<!-- Thêm item: chép nguyên khối ### SV-xx ở trên, tăng số. -->
