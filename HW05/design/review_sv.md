# C – review thiết kế, tham số, JMX và log smoke của SV (bước 5)

## Danh sách của SV (nguyên văn)

Soi thiết kế, tham số, `.jmx` và log smoke:

1. Lệch cấu hình `delay_s` của luồng Lockout giữa tài liệu thiết kế tham số và cả 4 file `.jmx` có bật Lockout:
   - Trong `02_scenarios.md` (mục 2 và mục 3 Smoke), tài liệu ghi rõ luồng Lockout bắt đầu sau 30 s (`delay_s = 30`).
   - Thực tế trong XML của cả 4 file `.jmx` (`Smoke`, `Load`, `Stress`, `Spike`), Thread Group `Lockout – user riêng, cố ý sai` đang để `<boolProp name="ThreadGroup.scheduler">false</boolProp>` và `<stringProp name="ThreadGroup.delay"></stringProp>` (chạy ngay lập tức tại t = 0 song song với luồng chính, thay vì trễ 30 s như mô tả).

2. Lệch số dòng `users.csv` giữa thiết kế (`01_workflow_design.md`) và thực tế trong `.jmx` / smoke log:
   - `01_workflow_design.md` (mục 3) ghi `users.csv` có `200 (tạm, ≥ VU đỉnh – bước 2 chốt)`.
   - Trong các file `.jmx` (`setUp 1 – đăng ký user chính (400 dòng)`) và nhật ký smoke (`04_smoke_log.md`: `setUp: đăng ký 400 + 20 user`), thực tế đã nâng lên 400 dòng nhưng tài liệu thiết kế chưa cập nhật đồng bộ.

3. Rủi ro thiếu RAM trống thực tế cho kịch bản Stress 300 VU và Spike 300 VU:
   - `02_scenarios.md` tính trần 300 thread dựa trên trạng thái máy còn khoảng 4,8 GB RAM trống.
   - Tuy nhiên, log chạy Smoke thực tế (`04_smoke_log.md`, lượt 2) ghi nhận RAM trống lúc bắt đầu chỉ còn 2.729 / 16.017 MB (~2,66 GB), trong đó riêng JMeter (heap 1 GB) đã chiếm ~1,2 GB private memory. Chạy đồng thời JMeter + Node backend ở mức 300 thread trên cùng máy có nguy cơ cao bị swap bộ nhớ hoặc tràn RAM, làm sai lệch thời gian phản hồi (RT) đo được.

4. Khớp chuỗi `"id":${orderId},` ở `04_GET_my_orders` phụ thuộc chặt vào định dạng JSON không khoảng trắng và vị trí trường:
   - Assertion `Đơn vừa tạo có trong lịch sử` kiểm tra chuỗi con `"id":${orderId},` (có dấu phẩy ngay sau `orderId`, không có khoảng trắng sau dấu hai chấm).
   - Dù smoke hiện tại đang Pass, cách kiểm tra chuỗi thô này sẽ Fail giả nếu trường `id` nằm ở cuối object JSON (trước dấu `}`) hoặc nếu serializer thay đổi định dạng thêm khoảng trắng (`"id": 123`).

5. Các điểm chưa chốt / còn để mở trong tài liệu cần rà soát trước khi chạy chính thức:
   - Soak (TẠM): Đang đặt tạm 150 VU trong 900 s (15 phút) với `think_scale = 0,25`; bắt buộc phải cập nhật lại bằng 70–80% bậc ổn định cao nhất sau khi có kết quả chạy Stress chính thức (giả định A13).
   - Ngưỡng SLA và Duration Assertion (A11): Ngưỡng hỏng `2000 ms`, `p95 ≤ 500 ms`, `Error % ≤ 1%` đều là giả định do SRS không quy định yêu cầu phi chức năng (A9).
   - Bậc thang Stress trong XML: Các bậc 1–6 được cấu hình bằng 6 Thread Group độc lập, mỗi nhóm 50 VU với `delay` cộng dồn `0 / 120 / 240 / 360 / 480 / 600` s và `duration` giảm dần `720 / 600 / 480 / 360 / 240 / 120` s để cộng gộp thành 50 → 300 VU kết thúc cùng lúc ở giây 720. Cần lưu ý khi phân tích log phải gom theo cửa sổ thời gian (time-bucket) chứ không đọc tách rời từng Thread Group.
