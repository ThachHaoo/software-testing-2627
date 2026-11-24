# perf_plan.json – schema

Mọi test plan trong skill đều sinh từ **một** file `perf_plan.json` (H1 = a: `gen_jmx.py` sinh `.jmx`, không sửa `.jmx` bằng tay).

- Đường dẫn `data[].file` tính từ `<hw-dir>`, mặc định là thư mục chứa plan.
- Ví dụ đầy đủ: `assets/example_plan.json`. Ví dụ này chỉ có `GET /api/products`, không phải workflow của bài.

## Khung

```jsonc
{
  "meta": {...},
  "data": [...],
  "setup": [...],          // tuỳ chọn – setUp Thread Group (vd đăng ký user từ CSV mỗi lần chạy)
  "workflow": [...],       // chuỗi request của 1 VU, dùng chung cho mọi scenario
  "assertions": {...},     // id request → danh sách assertion
  "lockout_flow": {...},
  "scenarios": {"smoke": {...}, "load": {...}, "stress": {...}, "soak": {...}, "spike": {...}},
  "listeners": {...},      // scenario → report view
  "thresholds": {...},
  "review_log": [...],
  "assumptions": [...]
}
```

## meta

| Khoá | Kiểu | Ý nghĩa |
|---|---|---|
| `mssv` | chuỗi | Dùng trong tên plan `<mssv>_<Type>_<YYYYMMDD>` |
| `hw`, `description`, `sut` | chuỗi | Mô tả; `sut` ghi repo@commit |
| `base` | object | `protocol`, `host`, `port`, `connect_timeout_ms`, `response_timeout_ms` → HTTP Request Defaults |
| `plan_dir` | chuỗi | Thư mục `.jmx` (mặc định `testplans`) |
| `lockout_required` | bool | `true` khi workflow có login có cơ chế khoá; khi đó check_plan bắt buộc có `lockout_flow` với user riêng |
| `auth_header` | chuỗi | Giá trị header `Authorization` của request có `auth: true` (mặc định `Bearer ${token}`) |

## data[] (CSV)

| Khoá | Ý nghĩa |
|---|---|
| `id` | Mã tham chiếu (`setup[].data`, `lockout_flow.data`) |
| `file` | Đường dẫn CSV (có header = `columns`) |
| `columns` | Tên biến JMeter (`${email}`…), theo đúng thứ tự cột |
| `scope` | `main`: CSV Data Set nằm trong mọi Thread Group chính · `setup`: chỉ dùng cho setUp · `lockout`: chỉ luồng lockout |
| `share` | `all` / `group` / `thread` → shareMode của CSV Data Set |
| `recycle`, `stop_thread` | Như CSV Data Set. setUp luôn đặt `recycle=false`, `stop_thread=true` |
| `generator` | `gen_csv.py` dùng để sinh file. Các kiểu: `users` {count, start, email, password, name, extra}; `values` {values}; `range` {start, stop}; `manual` (SV tự viết) |
| `note` | Ghi chú nguồn dữ liệu (vd dòng seed trong `database.js`) |

## Request (dùng trong workflow[], setup[].requests[], lockout_flow.requests[])

| Khoá | Bắt buộc | Ý nghĩa |
|---|---|---|
| `id` | ✓ | Duy nhất trong toàn plan; là khoá của `assertions` |
| `label` | ✓ | Tên sampler, cũng là label trong jtl (nên đánh số `01_…` để giữ thứ tự) |
| `method`, `path` | ✓ | `path` có thể chứa `${biến}` |
| `source` | ✓ | **file:dòng trong mã SUT thật** (vd `server.js:297-309`). check_plan từ chối nếu thiếu |
| `auth` | | `true` thì thêm header `Authorization` = `meta.auth_header` |
| `body` | | Chuỗi hoặc object JSON (gửi raw). `null` nghĩa là không có body |
| `once_per_vu` | | `true` thì đặt trong Once Only Controller (vd login một lần mỗi VU vì JWT không hết hạn) |
| `think_before_ms` | | Timer chạy **trước** request: `{"type":"constant","ms":…}` · `{"type":"uniform","min":…,"max":…}` · `{"type":"gaussian","ms":…,"dev":…}` |
| `extract` | | `[{"type":"json","var":"token","path":"$.token","default":"NOT_FOUND"}]` |

## assertions

`{"<request id>": [assertion, …]}`. Mỗi request phải có ≥ 1 assertion.

| type | Trường | JMeter |
|---|---|---|
| `code` | `equals` | Response Assertion, Response Code, Equals |
| `contains` / `not_contains` | `text` | Response Assertion, body, Substring (/ NOT) |
| `equals_body` | `text` | Response Assertion, body, Equals |
| `json` | `path`, `value` (tuỳ chọn), `regex`, `invert` | JSON Assertion: không có `value` thì chỉ kiểm path tồn tại |
| `duration` | `ms` | Duration Assertion |

Mọi loại đều nhận thêm `name` và `message` (thông báo khi fail).

## setup[]

`[{"name": "...", "data": "<data id>", "requests": [request…]}]`.

- Mỗi phần tử sinh một **setUp Thread Group**: 1 thread, loops = số dòng CSV, đọc CSV đó.
- Dùng để đăng ký user ở mỗi lượt chạy. Lý do: restart backend làm mất user đã đăng ký.

## lockout_flow

| Khoá | Ý nghĩa |
|---|---|
| `enabled` | Bật Thread Group "Lockout – user riêng, cố ý sai" |
| `data` | id CSV có `scope: "lockout"`; **không chung user** với CSV chính (check_plan kiểm cột đầu) |
| `threads`, `ramp_s`, `loops`, `delay_s`, `duration_s` | Như Thread Group |
| `requests` | Chuỗi request cố ý sai, có assertion trong `assertions` |

Scenario có thể tắt luồng này bằng `"lockout": false` (vd smoke, soak).

## scenarios.<smoke|load|stress|soak|spike>

| Khoá | Ý nghĩa |
|---|---|
| `groups` | `[{"name","threads","ramp_s","delay_s","duration_s"}]` (hoặc `loops` thay cho `duration_s`). Mỗi group là một Thread Group lõi |
| `lockout` | `false` thì không sinh luồng lockout trong plan này |
| `think_scale` | Hệ số nhân mọi `think_before_ms` của workflow trong plan này (mặc định 1.0; 0 = bỏ timer). Dùng khi stress/soak cần nhiều req/s hơn mà không tăng số thread quá sức máy sinh tải. Không áp cho setUp và luồng lockout |
| `rationale` | Lý do chọn tham số: λ mục tiêu, W = RT + think, N theo Little's Law, nguồn số liệu (vd kết quả smoke) |

- Stress dạng bậc thang: các group bắt đầu lệch nhau theo `delay_s` và cùng kết thúc.
- Spike: một group nền chạy suốt lượt, cộng một group đột biến có `ramp_s` nhỏ, bắt đầu ở `delay_s`.

## listeners.<scenario>

`[{"type": "summary|aggregate|view_results_tree|response_time_graph|table", "errors_only": bool}]`

- Listener **không ghi file** (filename rỗng): jtl chính thức (`-l`) là nguồn số liệu duy nhất. Bằng chứng report view: mở `.jmx` bằng GUI → chọn listener → **Browse…** chọn jtl của lượt chính thức → chụp màn hình.
- 3 plan chính (load, stress, spike) **không được dùng chung loại listener** nào (đề HW05 §6).
- Soak để `[]`: không gắn listener, chỉ ghi `.jtl` qua `-l`.

## thresholds

`{"p95_ms": {"<label>|*": số}, "error_pct": số}`: ngưỡng SV chốt, dùng ở bước 7 và 9 để đối chiếu.

## review_log[]

`[{"date": "YYYY-MM-DD HH:MM", "by": "SV|AI", "step": 5, "change": "...", "reason": "...", "commit": "<hash>"}]`: mỗi lần sửa plan sau bản đóng băng.

## assumptions[]

Danh sách chuỗi: chỗ SRS im lặng hoặc giả định về dữ liệu. SV duyệt.
