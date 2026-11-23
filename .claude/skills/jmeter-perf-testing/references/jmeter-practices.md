# Thực hành JMeter dùng cho skill (rút gọn, có nguồn)

Nguồn tham khảo: **QAInsights/perf-skills**, https://github.com/QAInsights/perf-skills, commit `950702c53ba69c7684e315ad9e9881f05e4e0a93` (29/08/2026).

- Chỉ mượn ý từ các file dưới, diễn đạt lại bằng tiếng Việt; không chép nguyên `SKILL.md` hay script nào của repo đó:
  - `skills/perf/references/tools/jmeter.md`;
  - `skills/perf/references/topics/workload-design.md`;
  - `skills/perf/references/topics/results-analysis.md`.
- Repo đó chỉ được đọc như dữ liệu tham khảo, không chạy script nào trong đó.
- Mỗi mục bên dưới ghi file nguồn. Các ghi chú "→ skill này" là phần áp dụng riêng cho skill; perf-skills không có.

## 1. Cấu trúc test plan (nguồn: `tools/jmeter.md` – HTTP Sampler Best Practices, Correlation, CSV Data Set Config)

- Đặt host, port, protocol một lần ở **HTTP Request Defaults**, không ghi cứng trong từng sampler. `Content-Type` đặt ở Header Manager cấp cao.
  - → skill này: `gen_jmx.py` sinh HTTP Request Defaults từ `meta.base`; sampler để trống domain, port, protocol.
- Giữ **KeepAlive** bật, tắt follow redirect khi API không cần.
- Token động lấy bằng **JSON Extractor** (`$.token`), có giá trị mặc định `NOT_FOUND`. Nên kiểm cả giá trị đã trích.
  - → skill này: `extract[]`. Muốn kiểm token thì thêm assertion vào `assertions[<id>]`; check_plan chỉ bắt buộc sampler có ≥ 1 assertion.
- **CSV Data Set**: số dòng ≥ số VU đỉnh để tránh hai VU dùng chung dữ liệu; chọn chế độ chia sẻ (All threads / Current thread group) theo mức cách ly cần có.
  - → skill này: mỗi thread group có CSV riêng trong phạm vi của nó. Luồng lockout dùng file user riêng, check_plan kiểm hai file không chung user.

## 2. Think time và ramp-up (nguồn: `topics/workload-design.md` – Little's Law, Think Time Design, Ramp-Up Strategy)

- **Little's Law**: N = λ × W, trong đó W = thời gian phản hồi + think time. Chỉ biết số VU mà không biết think time thì không suy ra được tải.
  - → skill này: bước 2 ghi rõ λ mục tiêu, W và N trong `scenarios.*.rationale`.
- Trong mô hình đóng (closed model), không đặt think time = 0 trừ khi cố ý benchmark API. Phân phối đều (uniform) hoặc Gaussian thực tế hơn hằng số.
- Ramp-up quá gắt sinh "thundering herd" làm số liệu sai lệch. Nên loại giai đoạn ramp khỏi phép tính SLA. Với stress dạng bậc thang, giữ mỗi bậc đủ lâu (≥ 2–3 lần thời gian giao dịch) trước khi tăng tiếp.
  - → skill này: dựng bậc bằng nhiều Thread Group lõi có `delay_s` và `duration_s`, không cần plugin Stepping Thread Group.
- Timer: Constant, Uniform Random, Gaussian Random.
  - → skill này: `think_before_ms` hỗ trợ đủ ba loại. Timer là con của sampler nên chạy **trước** sampler đó.

## 3. Chạy (nguồn: `tools/jmeter.md` – Running JMeter Non-GUI, JMeter-Specific Tips)

- Lượt tải chạy **non-GUI** (`-n -t -l -e -o`), vì GUI ngốn tài nguyên của chính JMeter và làm sai số liệu.
  - → skill này: H2 = a. GUI chỉ dùng để chụp ảnh hoặc quay video ở tải nhỏ.
- Không dùng **View Results Tree** trong lượt tải (tốn bộ nhớ). Không đặt listener trong vòng lặp.
  - → skill này: nếu dùng View Results Tree thì chỉ bật `errors_only`. Soak không gắn listener.
- Tăng heap JVM khi tải lớn (`-Xms/-Xmx`).
  - → skill này: tham số `-Heap` của `run_scenario.ps1`, mặc định 1 GB giống `jmeter.bat`.
- Dùng `-J` để truyền thuộc tính, trong plan đọc bằng `${__P(...)}`.
  - → skill này: `-Jlistener.dir` cho đường dẫn file của listener.

## 4. Đọc kết quả (nguồn: `topics/results-analysis.md` – Core Metrics, Response Time Percentiles, Reading JMeter Reports, Bottleneck Identification)

- Không kết luận chỉ dựa vào trung bình. Báo p50, p95, p99 và max; p95 là chỉ số SLA thông dụng, p99 cho thấy đuôi phân phối.
- Đọc throughput cùng với số thread đang hoạt động: throughput đi ngang trong khi thread tăng là dấu hiệu bão hoà. Error rate phải tách theo mã phản hồi.
- Thứ tự cô lập nút thắt: error rate → throughput đi ngang → CPU > 80% → truy vấn CSDL chậm → tràn pool hoặc kết nối → mạng.
  - → skill này: bước 7 đối chiếu với `typeperf_node.csv`. SUT không có pool, chỉ có một kết nối SQLite (`sut_recon.md` §3), nên mọi kết luận về pool phải dựa vào mã thật.
- Trích số liệu từ jtl bằng script.
  - → skill này: `jtl_stats.py` tính percentile theo cách của JMeter và đối chiếu với `statistics.json` của HTML report.

---

## Thông báo bản quyền (MIT) của nguồn tham khảo

```
Copyright 2026 NaveenKumar Namachivayam

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the “Software”), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
