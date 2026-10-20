---
name: domain-bva-testing
description: Áp dụng Domain Testing (phân lớp tương đương) và Boundary Value Analysis cho một chức năng có ô nhập/tham số theo đúng 4 bước bài giảng (biến vào/ra → lớp tương đương → minimum set → giá trị biên), lưu test case vào một file JSON, kiểm tra độ phủ, xuất bảng Markdown, sinh khung test tự động và gộp kết quả chạy. Dùng khi người dùng nói "domain testing", "phân lớp tương đương", "equivalence partitioning", "BVA", "giá trị biên", "thiết kế test case cho form/API", hoặc gọi /domain-bva-testing kèm mã feature.
---

# Domain Testing + BVA theo từng bước

Skill này dẫn AI đi qua kỹ thuật **đúng như bài giảng** (Kaner & Bach; slide Domain Testing của môn), **mỗi lần gọi làm một bước rồi dừng** để người dùng review và commit. Không gộp cả kỹ thuật vào một lượt trả lời: đề bài chấm việc "dẫn AI qua từng bước của kỹ thuật", và người review cần thấy được từng quyết định.

Dữ liệu của một feature nằm trong **một file** `testcases.json` (schema của skill `test-case-writing` + phần mở rộng `domain`, xem `references/schema-domain.md`). Mọi bảng Markdown, khung test tự động và số liệu tổng hợp đều sinh ra từ file này.

## Quy tắc bắt buộc

1. **Đọc test basis thật trước khi viết bất cứ gì:** đoạn đặc tả của feature, mã nguồn UI (tên nhãn, `type`, `required`, thông báo lỗi thật), API spec/route backend. Ghi đúng tên trường/nút/thông báo như trên giao diện. Không bịa trường hay endpoint.
2. **Đặc tả là oracle.** Expected suy ra từ đặc tả, không suy ra từ việc code đang làm gì. Chỗ đặc tả im lặng → ghi vào `meta.assumptions` (giả định + lý do) thay vì tự quyết ngầm.
3. **Bản nháp của AI được đóng băng:** sau mỗi bước AI tạo/sửa `testcases.json`, chạy `scripts/freeze.py` để lưu bản gốc vào `appendix/ai-outputs/` trước khi người dùng sửa. Không bao giờ sửa file đã đóng băng.
4. **Đánh dấu nguồn từng TC:** `origin: "AI"` cho case AI đề xuất, `"Human"` cho case người dùng thêm, `"Both"` cho case AI đề xuất rồi người dùng sửa đáng kể.
5. **Khi người dùng đang tự tìm case còn thiếu (G9.3), không gợi ý thêm.** Sau bước 4, dừng. Chỉ khi người dùng đã thêm case của họ và hỏi "vì sao bạn bỏ sót", mới trả lời — trung thực, tách rõ *đã nghĩ tới nhưng không đưa vào output* với *không nghĩ tới*, và nguyên nhân (prompt thiếu thông tin, giới hạn công cụ, độ phức tạp của feature).
6. Nếu một quy định khoá học/đội (ví dụ CLAUDE.md, skill khoá học) hạn chế việc AI làm, quy định đó thắng skill này.

## Các bước (mỗi lần gọi một bước)

Gọi: `/domain-bva-testing <feature-dir> <bước>` — ví dụ `HW02/A_FR01 1`. Nếu thiếu số bước, đọc `testcases.json` để biết bước kế tiếp và hỏi lại trước khi làm.

### Bước 0 — Khởi tạo
- Tạo `<feature-dir>/testcases.json` với `meta` (title, feature, sut_version = commit SUT, environment, scope, references, assumptions rỗng) và `requirements` (tách đặc tả của feature thành các dòng có mã, ví dụ `FR-01.2`).
- Liệt kê nguồn đã đọc (file + dòng) trong `meta.references`.

### Bước 1 — Biến vào/ra
- Điền `domain.variables`: mỗi biến **đầu vào** (trường form, tham số API, trạng thái dữ liệu có sẵn ảnh hưởng kết quả) và **đầu ra** (thông báo, chuyển trang, bản ghi được tạo/không tạo, giá trị tính được), kèm `source` (nhãn UI / field API) và `constraint` trích từ đặc tả.
- Xuất bảng bằng `render_md.py`. Dừng.

### Bước 2 — Lớp tương đương
- Điền `domain.partitions` (EC1, EC2…): mỗi điều kiện → lớp hợp lệ/không hợp lệ theo hướng dẫn của bài giảng: khoảng giá trị → 1 hợp lệ + 2 không hợp lệ; số lượng → 1 + 2; tập giá trị xử lý khác nhau → 1 lớp/giá trị + 1 ngoài tập; điều kiện "phải là" → 1 + 1; sai kiểu. Có lý do tin rằng các phần tử của một lớp bị xử lý khác nhau thì **tách lớp** và ghi lý do vào `note`.
- Phân lớp cả **biến đầu ra**.
- Ghi `guideline` (range/count/set/must-be/type/split) cho mỗi lớp. Dừng.

### Bước 3 — Test case Domain (minimum set)
- Tạo suite `TS-DOM` (`format: "matrix"`, `procedure` viết một lần, `columns` = các biến đầu vào). Tách suite theo tầng (UI / API) nếu quy trình khác nhau — mỗi suite một quy trình.
- **Mỗi case thuộc đúng một tầng** (`layer: "UI"` hoặc `"API"`). Ý "kiểm cả UI lẫn API" → hai case riêng, mỗi case nằm trong suite của tầng đó. Expected của case API chỉ nói về phản hồi (mã HTTP, body) và dữ liệu lưu; không nhắc thông báo, chuyển trang hay yếu tố giao diện.
- Trường đặc tả yêu cầu mà giao diện có thể không có (ví dụ ô xác nhận): viết **một** case kiểm sự tồn tại của trường; các case khác ghi trong `notes` cách xử lý khi trường vắng mặt (bỏ bước nhập, verdict theo Bước 6).
- **Tiền điều kiện phải nêu trạng thái ban đầu quan sát được**: trang vừa tải xong, **mọi ô trống**, chưa đăng nhập/không còn phiên cũ, trình duyệt không tự điền (autofill), dữ liệu sẵn có trong CSDL. Không giả định ngầm.
- **Quy trình phải nói rõ cách nhập từng loại giá trị**: thứ tự các ô; giá trị thường → gõ đúng chuỗi trong cột; "rỗng" → không nhập gì, để nguyên ô trống; khoảng trắng → gõ đúng số dấu cách ghi trong cột (bảng hiển thị `␣`); bấm nút submit đúng một lần; nêu chỗ quan sát kết quả (hộp lỗi, URL, phản hồi API, CSDL). Mỗi bước có một phản hồi quan sát được.
- Quy tắc chọn: case **hợp lệ** phủ càng nhiều lớp hợp lệ càng tốt; mỗi case **không hợp lệ** phủ **đúng một** lớp không hợp lệ, các biến khác giữ giá trị hợp lệ.
- Mỗi case có `covers` (danh sách EC), `technique: "EP"`, `rationale` (vì sao chọn giá trị này là đại diện tốt nhất), `expected_result` có oracle kiểm chứng được (đúng chữ thông báo nếu đặc tả nêu; nếu không, ghi giả định).
- `ec_target` (⊆ `covers`) = lớp vào case cần thử + lớp ra mà Expected khẳng định; truy vết yêu cầu sinh từ `ec_target`. Giả định quyết định Expected ghi vào `assumptions` của case.
- Thuộc tính chung (nhãn, định dạng, phản hồi trực quan…) chỉ khẳng định ở **một** case; các case khác không lặp lại.
- Phần dữ liệu không thay đổi ghi **tương đối** (SAU = TRƯỚC); giá trị tuyệt đối chỉ dùng cho đầu ra case thực sự kiểm.
- Đặc tả im lặng và chưa có giả định → không viết Expected cho điểm đó (không tạo Fail không căn cứ); hỏi người dùng chốt giả định trước.
- Chạy `check_domain.py` — mọi EC phải được phủ, không case nào phủ hai lớp không hợp lệ. Dừng.

### Bước 4 — Test case BVA
- Tạo suite `TS-BVA`. Với mỗi lớp có thứ tự (số, độ dài, ngày…), sinh các điểm theo mô hình 9 điểm của bài giảng: `LB-1, LB, LB+1, NOM, UB-1, UB, UB+1`, và `MIN_UI`/`MAX_UI` (giá trị nhỏ/lớn nhất nhập được qua giao diện) khi có ý nghĩa. Bước nhảy = đơn vị nhỏ nhất của miền (1 ký tự, 1 đơn vị tiền, 1 ngày).
- Biến đang xét chạy qua các điểm biên; **các biến khác giữ nominal hợp lệ**.
- Miền không có cận trên (theo giả định): khai `no_upper_bound: "<mã giả định>"` ở biến, dùng điểm `LARGE` cho đại diện giá trị lớn; case có mã giả định đó trong `assumptions` (`check_domain.py` báo lỗi nếu thiếu).
- Mỗi case có `bva_point`, `covers`, `technique: "BVA"`, `rationale`. Chạy `check_domain.py`. **Dừng hẳn** — bước tiếp theo là của người dùng.

### Bước 5 — (Người dùng) bổ sung và gap analysis
- Người dùng thêm suite `TS-SV` (`origin: "Human"`) và chạy `check_domain.py`. Mỗi case có `technique` (thường `EG`); case chọn từ hiểu biết mã nguồn ghi `approach: "gray-box"`.
- Khi được hỏi, so sánh case người dùng thêm với bản đóng băng của bước 3–4 và trả lời theo quy tắc 5. Không viết hộ phần phân tích nguyên nhân trong report.

### Bước 6 — Thực thi
- Sinh khung test tự động từ `testcases.json` (Playwright cho web/API; xem `references/automation.md`): mỗi test có tiêu đề bắt đầu bằng mã TC, ghi `actual` bằng annotation và chụp màn hình. Mobile (Expo) chạy tay: điền `actual_result`/`status` trực tiếp.
- Người dùng chạy trên máy của họ; sau đó `merge_results.py` gộp kết quả vào `testcases.json`. Không tự đổi Expected sau khi đã có Actual — ngoại lệ duy nhất: điểm quan sát trong Expected không tồn tại trên hệ thống; khi đó ghi lý do vào `notes`.
- **Quy tắc verdict** (ghi thành giả định trong `meta.assumptions` trước khi chạy):
  - Kết quả lệch Expected **vì biến mục tiêu** của case → `Fail`.
  - Case không đi tới được điểm kiểm **vì biến khác** (một lỗi đã có ở case khác chặn đường) → `Blocked`, ghi mã case gốc vào `notes`. Không tính là Fail lần hai.
  - Trường đặc tả yêu cầu nhưng không có trên giao diện → case kiểm sự tồn tại `Fail`; các case cần nhập trường đó → `Blocked` (case gốc = case kiểm sự tồn tại).
  - Bị từ chối đúng như Expected nhưng thông báo/lý do không chứng minh được luật mục tiêu (lý do chung, hoặc do một luật khác, hoặc chức năng nền hỏng nên giá trị nào cũng bị "từ chối") → vẫn `Pass` theo hộp đen, ghi "Pass hộp đen" + case gốc vào `notes`.
  - Case bị chặn bởi hai lỗi khác nhau → ghi cả hai case gốc.
- `auto_status` giữ kết quả tự động gốc do `merge_results.py` ghi; người dùng chỉnh `status` theo quy tắc trên, không sửa `auto_status`. `merge_results.py` không ghi đè `status` người dùng đã chỉnh (trừ `--force`).
- Mỗi lượt chạy ghi results riêng có timestamp; evidence chỉ giữ lượt mới nhất. Ghi nhật ký lượt chạy (thời điểm, phạm vi, script) và chọn lượt chính thức (chạy toàn bộ sau khi dữ liệu được làm sạch).
- Đường tự động bị chặn (Blocked) nhưng case vẫn kiểm được bằng đường khác (gọi API tạo dữ liệu, thao tác tay): người dùng kiểm tay, ghi bước và quan sát vào `notes`, ảnh `TC-xx_manual_*.png`; `status` theo kết quả kiểm tay, `auto_status` giữ Blocked.
- Evidence đặt tên `TC-xx_ui/_api/_req/_res/_failed/_manual_*`; không chép trace; giữ nguyên bản gốc (bản cần che thông tin để đăng công khai tạo riêng).

### Bước 7 — (Người dùng) bug report
- Với case Fail: cô lập nguyên nhân (chạy lại, reset dữ liệu, so UI với API) trước khi kết luận là bug. Mô tả bug do người dùng viết; AI chỉ kiểm tra trường còn thiếu.
- Phần AI được làm, theo thứ tự, mỗi bước chờ người dùng duyệt:
  1. **Gom dữ kiện**: nhóm các case Fail/Blocked theo triệu chứng và đoạn mã liên quan (trích nguyên văn, số dòng), chạy lại case nghi flaky; không đặt tên bug, không đề xuất severity/priority, không kết luận nguyên nhân.
  2. Người dùng chốt danh sách bug.
  3. **Dựng khung** `BUG-xx.md`: chỉ điền dữ kiện (môi trường, bằng chứng, TC liên quan, yêu cầu/giả định bị vi phạm, trích dẫn nguồn); để trống tiêu đề, bước, Expected, Actual, nhận định, severity, priority. Mục Yêu cầu **chỉ** ghi yêu cầu/giả định mà Actual cho thấy bị vi phạm, thêm dòng "Đạt trong cùng case" / "Chưa đánh giá được" / "Không áp dụng"; yêu cầu không có câu đặc tả riêng ghi "(ngầm định)".
  4. Người dùng viết mô tả và commit bản viết trước khi AI sửa dữ kiện. Nhận định về tác động phải dựa trên dữ kiện (mã/evidence).
  5. **Sửa dữ kiện**: đối chiếu payload/Actual với evidence (`_req`/`_res`, `actual_result`, ảnh) và sửa chỗ sai; khẳng định chưa có bằng chứng → thêm "(chưa kiểm chứng)"; không sửa văn phong, severity, priority.
  6. **Chạy thật bước tái hiện** trước khi tạo issue: lệnh/thao tác phải chạy được trên môi trường của người dùng (điều hướng không làm mất trạng thái; tiền điều kiện có bước dựng dữ liệu; lệnh shell đặt đúng content-type, mã hoá body, đọc được body lỗi); dán output vào dữ kiện; output lệch Actual → báo, không sửa Actual.
  7. Kiểm issue trùng trên tracker trước khi tạo; tạo issue bằng tài khoản của người dùng từ file người dùng đã viết; tiền tố tiêu đề (nếu có) chỉ thêm trên tracker; ghi URL vào file.

## Lệnh

```bash
python <skill>/scripts/freeze.py <feature-dir>/testcases.json --step 3 --out <hw>/appendix/ai-outputs
python <skill>/scripts/check_domain.py <feature-dir>/testcases.json
python .claude/skills/test-case-writing/scripts/lint_testcases.py <feature-dir>/testcases.json   # linter của giảng viên
python <skill>/scripts/render_md.py <feature-dir>/testcases.json -o <feature-dir>/testcases.md
python <skill>/scripts/merge_results.py <feature-dir>/testcases.json <playwright-results.json>
```

`render_md.py` sinh đủ các bảng theo slide: Biến vào/ra · Complete Set of Partitions · Test Cases Providing Coverage of Partitions · Minimum Set of Test Cases · Boundary Value Test Cases · Bổ sung của SV · Truy vết · Giả định · Kết quả chạy.

## Tài nguyên

- `references/schema-domain.md` — phần mở rộng `domain` và các trường thêm cho case
- `references/automation.md` — cách viết test Playwright đọc từ JSON để `merge_results.py` gộp được
- `assets/example-sum.json` — ví dụ hoàn chỉnh (bài cộng hai số −99…99 của slide)
