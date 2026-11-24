# 02 – Tham số kịch bản (bản AI, bước 2 skill `jmeter-perf-testing`)

> Bản AI sinh (Claude Code, 25/11/2026), đóng băng ở `appendix/ai-outputs/step2/`. SV duyệt và sửa ở bước 5.
> Nguồn số liệu là `perf_plan.json`: `scenarios`, `listeners`, `thresholds`, `assumptions` (A6–A14).
> Chưa có số đo smoke của workflow C khi chọn tham số. RT nền tạm lấy từ smoke ví dụ (`GET /api/products`, mean 5–8 ms) và làm tròn lên 10 ms/request.

## 1. Ràng buộc máy và cách tính

- Máy `LAPTOP-NFIGFMR1`: i5-13500H, 12 nhân / 16 luồng, RAM 16 GB. Lúc chạy thử E2E chỉ còn khoảng 4,8 GB trống.
- **JMeter và backend chạy chung máy**, nên mọi thread JMeter tranh CPU và RAM với node.
- Heap JMeter 1 GB (mặc định của `run_scenario.ps1`, giống `jmeter.bat`). Trần đề xuất là **300 thread** (A12).
- Backend: một tiến trình Node đơn luồng, một kết nối SQLite, không có index (`sut_recon.md` §2–3). Dự kiến nút thắt ở CPU của node hoặc ở hàng đợi SQLite, không ở mạng (localhost).
- Little's Law: N = λ × W. Với một vòng 4 request:
  - think time cơ sở trung bình = 2 + 2 + 3,5 + 1,5 = **9 s** (uniform 1–3 / 1–3 / 2–5 / 1–2 s);
  - W ≈ 9 s + 4 × 10 ms ≈ **9,04 s**;
  - mỗi VU ở `think_scale` 1,0 sinh khoảng **0,44 req/s**.
- Giảm think time cho stress, soak và spike bằng `think_scale`, thay vì tăng thread vượt trần máy sinh tải. Đây là tính năng harness thêm ở commit `d47ce3a`.

## 2. Bảng tham số

| Kịch bản | Thread | Ramp-up | Thời lượng / giữ | think_scale (think/vòng) | λ ước tính | Luồng lockout | Report view |
|---|---|---|---|---|---|---|---|
| Smoke | 2 | 2 s | 60 s | 1,0 (≈ 9 s) | ≈ 0,9 req/s | có | Summary Report |
| Load | 50 | 60 s | 660 s (giữ 10 phút sau ramp) | 1,0 (≈ 9 s) | ≈ 22 req/s (5,5 đơn/s) | có | **Aggregate Report** |
| Stress | 50 → 300, +50 mỗi 120 s (6 bậc, mỗi bậc ramp 30 s) | 30 s/bậc | 720 s | 0,25 (≈ 2,25 s) | ≈ 87 → 522 req/s | có | **Summary Report** |
| Soak (TẠM) | 150 | 60 s | 900 s (15 phút) | 0,25 | ≈ 260 req/s | không | không gắn listener (chỉ jtl) |
| Spike | nền 50 suốt 600 s + đột biến 250 lúc t = 180 s | nền 30 s, đột biến **5 s** | đột biến giữ 120 s, hồi phục 300 s | 0,5 (≈ 4,5 s) | ≈ 44 → 264 → 44 req/s | có | **View Results Tree (chỉ lỗi) + Response Time Graph** |

- 3 plan chính dùng 3 loại listener khác nhau, không trùng (D3). `check_plan.py` có kiểm điều này.
- Luồng lockout (D2): 1 thread, 20 vòng, mỗi vòng một user riêng, bắt đầu sau 30 s (`delay_s`).
  - Sinh trong smoke, load, stress, spike. Soak tắt luồng này để chỉ đo độ bền.
  - Mọi lượt đều restart backend trước khi chạy, nên trạng thái khoá không mang từ lượt này sang lượt sau.

## 3. Lý do từng con số

### Smoke

- Mục đích là kiểm plan, không đo tải.
- 2 VU × 60 s ≈ 6–7 vòng mỗi VU: đi qua đủ 4 sampler, 2 extractor, 2 setUp và luồng lockout (20 user × 4 request, xong khoảng 45 s sau `delay_s` 30 s).

### Load

- 50 người dùng đồng thời là mức "bình thường" giả định (A10); SRS và đề không cho số mục tiêu.
- λ = 50 / 9,04 ≈ 5,5 vòng/s ≈ 22 req/s.
- Ramp 60 s (khoảng 1 VU mỗi 1,2 s) để không dồn cục ("thundering herd").
- Giữ 10 phút sau ramp: có ≥ 10 điểm trên timeline theo phút, và phút ramp được loại khỏi phần đánh giá SLA.

### Stress

- Bậc thang +50 VU mỗi 120 s tới 300 VU; các bậc cùng kết thúc ở 720 s.
- Mỗi bậc: ramp 30 s, sau đó giữ khoảng 90 s, dài hơn nhiều so với 2–3 lần thời gian một giao dịch.
- `think_scale` 0,25 cho khoảng 1,74 req/s mỗi VU. Theo từng bậc: 87 / 174 / 261 / 348 / 435 / 522 req/s.
- Mục tiêu:
  - tìm **bậc ổn định cao nhất** (p95 ≤ 500 ms và lỗi ≤ 1%), dùng làm gốc cho soak;
  - tìm **điểm gãy** nếu có.
- Nếu tới 522 req/s vẫn ổn định thì báo "chưa gãy trong giới hạn máy sinh tải" (A12). Không suy diễn quá giới hạn này.

### Soak (tạm)

- 150 VU = 75% của bậc 4 (200 VU), cùng `think_scale` với stress, cho khoảng 260 req/s trong 15 phút.
- **Phải chỉnh** thành 70–80% mức ổn định đo được ở lượt stress chính thức trước khi chạy soak (A13); thay đổi đó ghi vào `review_log`.
- Tên plan `23120255_Soak_<YYYYMMDD>`, không gắn listener.
- CPU/RAM của node và JMeter lấy từ `monitor.csv`, dùng để tìm trần bộ nhớ.

### Spike

- Nền 50 VU. Ở t = 180 s thêm 250 VU trong 5 s (số VU tăng gấp 6), giữ 120 s, rồi về nền 300 s để xem hồi phục.
- `think_scale` 0,5: đỉnh khoảng 264 req/s, tức vùng bậc 3 của stress. Tăng đủ đột ngột mà không vượt trần máy sinh tải.
- 180 s nền đầu lượt dùng làm baseline.

## 4. Ngưỡng và assertion thời gian

| Ngưỡng | Giá trị | Dùng ở đâu |
|---|---|---|
| Duration Assertion | 2000 ms cho 4 request workflow | Sample vượt ngưỡng bị tính **lỗi** ("hỏng" theo góc nhìn người dùng) |
| p95 | ≤ 500 ms mỗi request | Ngưỡng SLA khi đánh giá (bước 7/9), không gắn thành assertion |
| Error % | ≤ 1% | Điều kiện để một bậc stress được coi là "ổn định" |

- SRS không có yêu cầu phi chức năng (A9). Cả 3 ngưỡng là giả định A11, SV chốt ở bước 5.
- p95 không gắn thành assertion vì như vậy error% sẽ lẫn "chậm" với "sai".

## 5. Điểm cần lưu ý khi đọc kết quả

- Bảng `orders` lớn dần: stress ước khoảng 50 nghìn đơn. `my-orders` không phân trang, không có index trên `user_id`, nên mỗi user nhận mảng hơn 100 đơn vào cuối lượt.
  - RT của `04_GET_my_orders` tăng theo thời gian một phần do dữ liệu, không chỉ do tải (A14).
  - Khi so các bậc stress cần tách hai yếu tố này.
- Sample setUp (`00_setup_*`) và lockout (`L1`–`L4`) nằm chung jtl. Khi tính số liệu của workflow, lọc bằng `jtl_stats.py --exclude-label "^(00_setup|L[1-4])_"`; khi đối chiếu với `statistics.json` thì không lọc.
- Restart backend trước mỗi lượt là bước reset (đề §6). `RUN.md` của từng lượt ghi lại các bước này.
