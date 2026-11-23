# HW05/CLAUDE.md — Performance Testing on EShop (đang làm)

Phần chung (vai trò, khối báo cáo, giới hạn AI, prompt log, git, zip, SUT) ở `CLAUDE.md` gốc. File này chỉ giữ phần riêng HW05.

## 1. Đề và rubric

- Đề: `context/HW05_assignment.md`, trích bằng pdftotext từ `context/HW05_assignment.pdf`.
- Bloom-AI: **G9.2 + G9.3 + G9.4 + G9.6**. Deadline **10:00 02/12/2026** (Moodle).
- Rubric (§15): Load 30 · Stress 20 · Spike 20 · Task 2 = 10 · Task 3 = 10 · Agent Skills 10.
- Tên zip: `23120255_HW05_AI_Performance_<ggg>.zip`.
- Kế hoạch nộp bài, danh sách file theo §14, mâu thuẫn trong đề, các mục cần khai cho Audit: `HW05/report_plan.md` (không nộp).

## 2. Yêu cầu chính (đối chiếu đề khi viết report)

- **3 test plan** Load / Stress / Spike cùng một workflow end-to-end, phủ cả 3 nhóm endpoint (auth / read / transactional).
  - AI dẫn từng bước, không dùng một prompt chung chung.
  - Dữ liệu từ CSV.
  - 3 loại listener khác nhau, không lặp lại.
- Tên test plan: `23120255_<ScenarioType>_<YYYYMMDD>`. 🔒 Tên file, jtl, video và hardware report không được để AI sinh hoặc bịa (§11).
- Mỗi lượt chạy cần:
  - ảnh JMeter kèm resource monitor của tiến trình backend;
  - file `.jtl` thô đầy đủ và thư mục HTML report;
  - hardware report (dxdiag/screenfetch + bảng spec), hostname phải khớp các bài trước.
- Soak 10–15 phút để tìm endurance threshold, báo bằng số.
- Video YouTube unlisted ≥ 6 phút: công cụ và resource monitor cùng khung hình, thuyết minh tiếng Việt bằng giọng SV.
- Task 2: AI phân tích jtl và đề xuất ngưỡng.
  - SV tìm chỗ AI đọc sai, kèm giá trị đúng lấy từ jtl.
  - SV phân loại đề xuất tối ưu của AI là khả thi hay bịa.
- Task 3: mô hình continuous perf testing (theo dõi commit, quyết định có chạy không, gắn cờ khi p95 hồi quy), kèm lưu đồ và phân tích đánh đổi.
- Agent Skill kèm video riêng; AI Critique 200–300 từ 🔒; Audit; commit log; README có tự chấm và test summary.

## 3. Môi trường

- SUT: `../eshop-sut` main @ `de0f48f`. Backend `http://localhost:3000`, khởi động bằng `node server.js`.
  - Mỗi lần khởi động: DROP + seed lại CSDL (`database.js:14-21`, `database.js:115`).
- JMeter **5.6.3**: `D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3\bin\jmeter.bat`. Không có trong PATH, chưa đặt `JMETER_HOME`, chưa có Plugins Manager.
- Java: Temurin 25.0.3 (đã đặt `JAVA_HOME`).
- Máy: `LAPTOP-NFIGFMR1`, i5-13500H, 12 nhân/16 luồng, RAM 15,6 GB, Windows 11. JMeter chạy chung máy với SUT.
- Khảo sát chi tiết: `HW05/notes/sut_recon.md`.

## 4. Mâu thuẫn trong đề

Xem `HW05/report_plan.md` mục d (SK, AS, G9, K6, VD, DL, HN, GR, CA).

## 5. Quyết định đã chốt

| Mã | Quyết định | Ngày |
|---|---|---|
| W = C | Workflow: `POST /api/login` → `GET /api/products` → `POST /api/checkout` → `GET /api/orders/my-orders`. Checkout không cần giỏ; body `total_amount` (+ `items` tuỳ chọn, backend bỏ qua) | 23/11 |
| T | JMeter 5.6.3 tại `D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3\` | 23/11 |
| L | Prompt log HW05 lấy lượt từ **2026-11-23 12:39**; notes/extra ở `HW05/appendix/` | 23/11 |
| LK | Lockout và reset theo `sut_recon.md` §5 (xem chi tiết dưới bảng) | 23/11 |
| D1 | setUp Thread Group đăng ký user từ CSV ở mỗi lần chạy, vì restart backend làm mất user đã đăng ký | 23/11 |
| D2 | CSV chính chỉ chứa credential đúng; thêm một luồng nhỏ cố ý nhập sai với tập user riêng, assert thông báo khoá | 23/11 |
| D3 | Load: Aggregate Report · Stress: Summary Report · Spike: View Results Tree (chỉ lỗi) / Response Time Graph | 23/11 |
| D4 | `YYYYMMDD` trong tên file = ngày chạy chính thức | 23/11 |

Chi tiết LK (lockout và reset):

- Mỗi lần sai mật khẩu bộ đếm tăng 2, nên lần sai thứ 2 đã bị khoá 180 giây.
- Khi đang khoá, mật khẩu đúng cũng nhận 403.
- Reset bằng cách:
  - chờ hết 3 phút rồi login đúng; hoặc
  - restart backend, sau đó phải đăng ký lại user (D1).

**Thứ tự chạy:** smoke → load → stress → soak → spike.

- **Soak:**
  - Mức tải = 70–80% mức ổn định tìm được ở stress, chạy 10–15 phút.
  - Tên `23120255_Soak_YYYYMMDD`, không gắn listener.
  - `typeperf` ghi CPU/RAM của tiến trình `node` ra CSV.
- **Trước mỗi lượt:** restart backend và ghi lại các bước reset.

## 6. Giới hạn riêng HW05 (bổ sung mục 3 của `CLAUDE.md` gốc)

- AI không chạy lượt chính thức thay SV, không sinh hay sửa jtl/HTML report, không tự đặt tên file theo ngày chưa chạy.
- Task 2: AI chỉ sinh bản phân tích (đóng băng vào `HW05/appendix/ai-outputs/` trước khi SV review). Phần "đọc sai ở đâu" và "khả thi hay bịa" do SV viết.
- Bug và nội dung Issue do SV viết. Issue liên quan đã có: #275, #278, #279, #280, #281, #283.
