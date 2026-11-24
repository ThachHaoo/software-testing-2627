# 04 – Nhật ký smoke (bước 4 skill `jmeter-perf-testing`)

Smoke: `testplans/23120255_Smoke_20261125.jmx` (ngày tạm), 2 VU × 60 s và luồng lockout 1 thread × 20 vòng. Chạy bằng `run_scenario.ps1`, không có `-Official`.

Mỗi lỗi được ghi ở đây **trước** khi sửa. Mỗi lần sửa là một commit `HW05 T1-4: sửa smoke – …`. File trong `appendix/ai-outputs/` không bị sửa.

## Lượt 1 – `runs/23120255_Smoke_20261125_20261125T002509/`

- Kết quả: 549 mẫu, lỗi 14,57% (80 mẫu). `jtl_stats` lệch `statistics.json` 0,00%.
- setUp: đăng ký 400 + 20 user, 0 lỗi.
- Luồng chính (login → products → checkout → my-orders): 12–13 mẫu mỗi label, 0 lỗi. Token, orderId và assertion "đơn có trong my-orders" đều qua.
- Luồng lockout: L1–L4 đều 20/20 bị tính lỗi.

### S1 – Mẫu lockout bị tính lỗi dù phản hồi đúng kỳ vọng

- **Triệu chứng:**
  - L1 và L2 trả 401, khớp assertion `code = 401`.
  - L3 và L4 trả 403.
  - Cả 80 mẫu có `success=false` nhưng `failureMessage` rỗng, nghĩa là không assertion nào fail.
- **Nguyên nhân:**
  - JMeter mặc định coi mọi phản hồi 4xx/5xx là sample lỗi, trước khi chạy assertion.
  - Muốn assertion quyết định kết quả cho phản hồi 4xx mong đợi, Response Assertion phải bật *Ignore Status* (`Assertion.assume_success`).
  - `gen_jmx.py` luôn ghi `Assertion.assume_success = false` (`.claude/skills/jmeter-perf-testing/scripts/gen_jmx.py:124`).
  - Schema không có cách khai báo "phản hồi 4xx là đúng" (`references/schema.md`, mục assertions).
  - Plan khai L3/L4 chỉ bằng `not_contains`, không có assertion nào cho phép 403 (`perf_plan.json`, `assertions.lock_wrong_3` và `lock_correct_after`).
- **Loại lỗi:** harness (gen_jmx/schema) cộng plan. Không phải lỗi SUT.
- **Ghi nhận thêm (chưa kết luận):** L3, tức lần sai thứ 3, đã nhận 403 "khoá", nghĩa là tài khoản bị khoá từ lần sai thứ 2 (`server.js:54-57`). Chỉ là dữ kiện; assertion L3 theo SRS chỉ yêu cầu "không cấp token".
- **Cách sửa:**
  1. Thêm trường `ignore_status` cho assertion `code`/`contains`/`not_contains`/`equals_body`. `code` với mã không phải 2xx/3xx tự bật trường này.
  2. `gen_jmx.py` đưa assertion có `ignore_status` lên đầu danh sách, vì JMeter đặt lại `success = true` khi chạy assertion đó; nếu nó chạy sau thì sẽ che lỗi của assertion đứng trước.
  3. Trong plan, L3/L4 đặt `ignore_status: true` ở `not_contains`.
  4. Ghi một dòng `review_log` (by AI, step 4).

## Lượt 2 – `runs/23120255_Smoke_20261125_20261125T002744/` (sau S1, commit `b8c96ad`)

- Kết quả: 549 mẫu, **0 lỗi (0,00%)**, 8,68 req/s. `jtl_stats` lệch `statistics.json` 0,00%.
- Luồng chính: login 13, products 13, checkout 12, my-orders 11 mẫu, 0 lỗi.
  - p95 theo ms: login 11, products 5, checkout 20, my-orders 5.
  - Đơn tạo được, và `orderId` có trong `my-orders`.
- Lockout: L1 401 ×20, L2 401 ×20, L3 403 ×20, L4 403 ×20, mọi assertion qua.
  - Mã phản hồi giống lượt 1, nên `ignore_status` không đổi phản hồi; chỉ để assertion quyết định kết quả.
  - L3 nhận 403 ở lần sai thứ 3, nghĩa là bị khoá từ lần sai thứ 2. Dữ kiện, chưa kết luận; trùng nội dung issue #280.
- Tài nguyên: RAM trống lúc bắt đầu chỉ còn 2.729 / 16.017 MB (`RUN.md`). JMeter dùng khoảng 1,2 GB private (heap 1 GB). Đây là rủi ro cho stress 300 thread.
- **Smoke sạch, dừng trước bước 5 (SV review).**
