---
name: jmeter-perf-testing
description: Kiểm thử hiệu năng backend REST bằng JMeter theo 10 bước có điểm dừng cho người review — khảo sát SUT → workflow → tham số scenario (smoke/load/stress/soak/spike) → sinh .jmx từ perf_plan.json + kiểm tra → smoke → SV review → chạy non-GUI kèm typeperf → AI phân tích jtl (đối chiếu stats_truth) → AI đề xuất tối ưu (SV phân loại) → render bảng vào report. Output AI đóng băng trước khi sửa; tên plan {MSSV}_{Type}_{YYYYMMDD}. Dùng khi người dùng nói "performance test", "load/stress/spike/soak test", "JMeter", "jtl", "endurance threshold", "HW05", hoặc gọi /jmeter-perf-testing kèm thư mục bài và số bước.
---

# Kiểm thử hiệu năng bằng JMeter, từng bước

Mỗi lần gọi skill **chỉ làm một bước rồi dừng** để người dùng review và commit. Đề chấm việc dẫn AI qua từng bước, và phần review cần diff giữa bản AI sinh và bản SV sửa.

- Cú pháp gọi: `/jmeter-perf-testing <hw-dir> <bước 0–9>`, ví dụ `HW05 3`.
- Thiếu số bước thì xem commit `<HW> perf k/9` gần nhất rồi hỏi lại.

Đường dẫn trong `<hw-dir>`:

| Thành phần | Đường dẫn |
|---|---|
| Kế hoạch | `perf_plan.json` |
| CSV | `data/` |
| Test plan | `testplans/<MSSV>_<Type>_<YYYYMMDD>.jmx` |
| Lượt chạy | `runs/<plan>_<ts>/` (jtl, `html/`, `typeperf_node.csv`, `RUN.md`) |
| Phân tích | `analysis/` |
| Đóng băng | `appendix/ai-outputs/step<k>/` |

## Luật (vi phạm thì dừng, báo người dùng)

1. **Đọc mã SUT thật trước khi viết request.**
   - Mỗi request có `source` dạng file:dòng; check_plan từ chối request thiếu trường này.
   - Không bịa endpoint, trường, mã lỗi hay nhãn.
   - Expected suy ra từ SRS. Chỗ SRS im lặng thì ghi vào `assumptions`.
   - Hành vi lệch SRS (vd khoá sau 2 lần sai) ghi là quan sát, không tự kết luận là bug.
2. **Đóng băng output AI** bằng `freeze.py` sau các bước 1, 2, 7, 8, trước khi SV sửa. Không bao giờ sửa file đã đóng băng.
3. **Bước của SV thì dừng hẳn** (5 review; phần phân loại ở 7 và 8).
   - Không gợi ý lỗi, edge case, assertion hay tham số còn thiếu trong lúc SV tự tìm.
   - Khi SV hỏi "vì sao AI bỏ sót": trung thực, tách *đã nghĩ tới nhưng không đưa vào* với *không nghĩ tới*.
4. **Tên plan** `{MSSV}_{Type}_{YYYYMMDD}`, Type ∈ Smoke/Load/Stress/Soak/Spike. `YYYYMMDD` là **ngày chạy chính thức**: `gen_jmx.py --date` bắt buộc, không tự lấy ngày hôm nay.
   - Chạy lại vào ngày khác thì sinh lại plan với ngày mới.
   - Không đổi tên file sau khi đã chạy.
5. **Không sửa jtl, HTML report hay `RUN.md`.** Lượt chính thức do SV chạy và SV quyết định.
   - Lượt hỏng do hạ tầng (máy treo, backend không lên) thì ghi lại và chạy lại; không dùng làm số liệu.
6. **Bug, AI Critique và đề xuất Continuous Performance Testing do SV viết.** AI chỉ gom dữ kiện (mã lỗi, số lượng, mốc thời gian, dòng jtl).
7. Quy định của khoá học và repo (CLAUDE.md, skill khoá học) thắng skill này.

## Các bước – mỗi bước một commit `<HW> perf k/9: …`

### 0 – Khảo sát (AI)

- Đọc README/SRS (oracle) và mã backend. Ghi lại:
  - cách chạy, port, base URL;
  - loại CSDL (WAL? index?), kết nối, middleware, rate limit;
  - endpoint ứng viên: method, path, auth, body và response mẫu;
  - cơ chế khoá tài khoản (ngưỡng, thời gian, nơi lưu, cách reset);
  - dữ liệu seed và cách reset;
  - môi trường máy: hostname, CPU/RAM, Java, JMeter.
- Ghi vào `<hw-dir>/notes/sut_recon.md` kèm file:dòng → commit → dừng.

### 1 – Workflow (AI đề xuất → đóng băng → SV duyệt)

- Viết `perf_plan.json`: `meta`, `workflow[]`, `data[]`, `setup[]`, `assertions`, `lockout_flow`, `assumptions`. Schema: `references/schema.md`.
- Workflow phủ đủ các nhóm endpoint mà đề yêu cầu. Mỗi request phải có `source`, assertion, và extractor nếu cần token.
- Login có lockout:
  - CSV chính chỉ chứa credential đúng;
  - một luồng nhỏ riêng cố ý nhập sai, dùng tập user riêng (`scope: "lockout"`), assert thông báo khoá;
  - user đăng ký lại ở setUp vì restart backend làm mất dữ liệu.
- `gen_csv.py` → `check_plan.py` (bỏ qua lỗi "không có .jmx") → `freeze.py --step 1` → commit → **dừng cho SV duyệt**.

### 2 – Tham số scenario (AI đề xuất → đóng băng)

- Điền `scenarios.{smoke,load,stress,soak,spike}`, `listeners`, `thresholds`. Mỗi scenario có `rationale`: λ, W = RT + think, N theo Little's Law, dựa trên số đo smoke nếu đã có.
- Báo cụ thể think time, ramp-up và số thread của từng scenario.
- Listener của 3 plan chính không trùng loại. Soak không gắn listener.
- Stress dạng bậc thang và spike dựng bằng nhiều Thread Group lõi (`delay_s`, `duration_s`), không cần plugin. Xem `references/jmeter-practices.md`.
- `freeze.py --step 2` → commit → dừng.

### 3 – Sinh + kiểm (AI)

- `gen_jmx.py --date <YYYYMMDD>` sinh `.jmx`.
- `check_plan.py` phải 0 lỗi. Các mục được kiểm:
  - sampler nào cũng có assertion;
  - CSV tồn tại;
  - tên đúng mẫu;
  - listener 3 plan chính khác nhau;
  - có luồng lockout với user tách riêng.
- Không sửa `.jmx` bằng tay. Muốn đổi gì thì sửa `perf_plan.json` rồi sinh lại. Commit → dừng.

### 4 – Smoke (AI chạy được)

- `run_scenario.ps1 -Jmx …Smoke….jmx -OutDir <hw-dir>/runs`, với 1–2 VU, khoảng 30 giây.
- Kiểm assertion, token, dữ liệu CSV và đơn được tạo. `jtl_stats.py` lấy RT nền cho bước 2.
- Lỗi do plan (không phải do SUT) thì sửa `perf_plan.json`, sinh lại, ghi `review_log`.
- Báo kết quả → dừng.

### 5 – SV review và sửa (SV)

- SV đọc `perf_plan.json` và `.jmx` (mở bằng GUI JMeter), so với bản đóng băng step1/step2 rồi sửa.
- Mỗi lần sửa một commit `<HW> perf 5/9x – sửa: …` và một dòng `review_log`.
- AI không gợi ý gì (luật 3). Sau khi SV commit xong phần của mình, AI chỉ sinh lại `.jmx` và chạy `check_plan.py`.

### 6 – Chạy (SV chạy lượt chính thức)

- Thứ tự: smoke → load → stress → soak → spike.
- Lượt chính thức chạy `run_scenario.ps1 -Official` (RUN.md ghi "Lượt chính thức: CÓ"); smoke/lượt thử không có `-Official` và được export-ignore (`runs/*_Smoke_*`, lượt thử thêm từng dòng vào `.gitattributes`).
- Mỗi lượt nằm trong `runs/<plan>_<yyyyMMddTHHmmss>/`; script tự làm:
  - restart backend;
  - typeperf CPU/RAM tiến trình node;
  - `java -jar ApacheJMeter.jar -n -t -l -e -o`;
  - ghi `RUN.md`.
- GUI chỉ dùng để chụp hoặc quay ở tải nhỏ (H2 = a), mở cùng khung hình với Task Manager.
- **Bằng chứng report view** (3 loại listener khác nhau): listener trong `.jmx` không ghi file. Sau lượt chính thức, mở `.jmx` bằng GUI JMeter → chọn listener của scenario (Aggregate / Summary / View Results Tree chỉ lỗi / Response Time Graph) → ô *Write results to file / Read from file* bấm **Browse…** chọn `runs/<plan>_<ts>/<plan>.jtl` → chờ nạp xong → chụp, lưu `evidence/<scenario>/`. Không sửa jtl khi mở.
- Khi stress hoặc spike làm khoá tài khoản: reset (restart backend) giữa các lượt và ghi các bước vào `RUN.md`.
- Nộp jtl đầy đủ. Kiểm dung lượng (Moodle ≤ 20 MB mỗi file) trước khi commit.

### 7 – AI phân tích (AI → đóng băng → SV tìm chỗ đọc sai)

- AI đọc jtl, `html/statistics.json` và `typeperf_node.csv`, rồi viết phân tích và đề xuất ngưỡng vào `analysis/ai_analysis_<scenario>.md` (H3 = b: được xem cả jtl lẫn stats_truth).
- `jtl_stats.py <jtl> --json stats_truth.json --md stats_truth.md --compare html/statistics.json` cho ra số liệu chuẩn, kèm phần trăm lệch với HTML report.
- `freeze.py --step 7` → commit → **dừng**. SV tự đối chiếu và viết chỗ AI đọc sai kèm giá trị đúng từ jtl. AI không chỉ ra chỗ sai của chính mình.

### 8 – AI đề xuất tối ưu (AI → đóng băng → SV phân loại)

- AI đề xuất tối ưu (index, WAL, pool, cache…), mỗi đề xuất trỏ tới file:dòng trong SUT, vào `analysis/ai_optimizations.md`.
- `freeze.py --step 8` → commit → **dừng**. SV phân loại khả thi hay bịa, kèm lý do.

### 9 – Render (AI)

- `render_md.py <report.md> <key> <file> [--section …]`: chèn bảng stats_truth, `RUN.md` và timeline vào report, chỉ thay phần giữa `<!-- BEGIN:key -->` và `<!-- END:key -->`.
- Không viết phần nhận xét, Critique hay bug. Commit → dừng.

## Chế độ demo – quay video skill hoặc chạy thử

- Copy `assets/example_plan.json` vào một thư mục chưa track (thêm thư mục đó vào `.git/info/exclude`).
- Chạy lần lượt bước 3 → 4 → 7 với `--date` bất kỳ. Không chạm `perf_plan.json`, `testplans/` hay `runs/` chính thức.
- Xong thì xoá thư mục đó.

```bash
S=.claude/skills/jmeter-perf-testing/scripts; D=HW05/_demo
mkdir -p $D && cp .claude/skills/jmeter-perf-testing/assets/example_plan.json $D/perf_plan.json
python $S/gen_csv.py $D/perf_plan.json && python $S/gen_jmx.py $D/perf_plan.json --date 20261123 && python $S/check_plan.py $D/perf_plan.json
powershell -ExecutionPolicy Bypass -File $S/run_scenario.ps1 -Jmx $D/testplans/23120255_Smoke_20261123.jmx -OutDir $D/runs
python $S/jtl_stats.py $D/runs/<run>/23120255_Smoke_20261123.jtl --md $D/runs/<run>/stats_truth.md --compare $D/runs/<run>/html/statistics.json
```

## Lệnh

```bash
S=.claude/skills/jmeter-perf-testing/scripts
python $S/gen_csv.py HW05/perf_plan.json [--force]
python $S/gen_jmx.py HW05/perf_plan.json --date 20261125 [--scenario load]
python $S/check_plan.py HW05/perf_plan.json
powershell -ExecutionPolicy Bypass -File $S/run_scenario.ps1 -Jmx HW05/testplans/23120255_Load_20261125.jmx -OutDir HW05/runs [-NoRestart] [-Heap "-Xms2g -Xmx2g"]
python $S/jtl_stats.py HW05/runs/<run>/<plan>.jtl --json HW05/runs/<run>/stats_truth.json --md HW05/runs/<run>/stats_truth.md --compare HW05/runs/<run>/html/statistics.json
python $S/freeze.py --step 1 --out HW05/appendix/ai-outputs HW05/perf_plan.json --note "#n"
python $S/render_md.py HW05/23120255_HW05_Report.md load_stats HW05/runs/<run>/stats_truth.md
```

- Môi trường: JMeter 5.6.3 (`-JmeterHome`, mặc định `D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3`), Java 17 trở lên, Windows PowerShell 5.1.
- Backend được chạy từ `../eshop-sut/backend` (`-BackendDir`).

## Tài nguyên

- `scripts/gen_csv.py`: sinh CSV từ `data[].generator`, không ghi đè nếu không có `--force`.
- `scripts/gen_jmx.py`: sinh `.jmx` từ các phần tử lõi JMeter, gồm:
  - HTTP Defaults, Header Manager;
  - setUp Thread Group, CSV Data Set;
  - Once Only Controller, JSON Extractor;
  - Response/JSON/Duration Assertion;
  - timer;
  - Thread Group theo stage, Thread Group lockout;
  - listener (không ghi file; xem bằng chứng report view ở bước 6).
- `scripts/check_plan.py`: kiểm plan và `.jmx` (xem bước 3).
- `scripts/run_scenario.ps1`: restart backend, typeperf, JMeter non-GUI, `RUN.md`.
- `scripts/jtl_stats.py`: số liệu theo label (percentile tính như JMeter), timeline theo phút, lỗi hay gặp, đối chiếu `statistics.json`.
- `scripts/freeze.py`: đóng băng output AI theo `step<k>/`, không ghi đè; file `.jmx` đổi đuôi thành `.jmx.txt`.
- `scripts/render_md.py`: chèn nội dung giữa marker.
- `references/schema.md`: schema của `perf_plan.json`.
- `references/jmeter-practices.md`: thực hành JMeter mượn từ QAInsights/perf-skills (MIT, có nguồn và commit).
- `assets/example_plan.json`: ví dụ nhỏ chỉ có `GET /api/products?search=`.
