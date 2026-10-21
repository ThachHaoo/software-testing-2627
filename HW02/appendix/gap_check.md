# Đối chiếu gap analysis SV với dữ kiện (chỉ dữ kiện)

> AI sinh bằng script từ `HW02/<feature>/gap_analysis_sv.md` (bản SV commit `129cfcc`), `testcases.json`, `ai_gap_answer.md`, `git log`. Không nhận xét câu chữ, không kết luận bên nào đúng. File SV không bị sửa.

## A_FR01

### b) SV-xx → TC (từ `notes` "Nguồn: SV-xx" trong JSON)

| SV-xx (dòng file SV) | TC trong JSON |
|---|---|
| SV-01 (dòng 5) | TC-FR01-200 |
| SV-02 (dòng 6) | TC-FR01-201 |
| SV-03 (dòng 7) | TC-FR01-202, TC-FR01-224 |
| SV-04 (dòng 8) | TC-FR01-203, TC-FR01-225 |
| SV-05 (dòng 9) | TC-FR01-204, TC-FR01-226 |
| SV-06 (dòng 10) | TC-FR01-205, TC-FR01-227 |
| SV-07 (dòng 11) | TC-FR01-206 |
| SV-08 (dòng 12) | TC-FR01-207 |
| SV-09 (dòng 13) | TC-FR01-208 |
| SV-10 (dòng 14) | TC-FR01-209 |
| SV-11 (dòng 15) | TC-FR01-210, TC-FR01-228 |
| SV-12 (dòng 16) | TC-FR01-211, TC-FR01-229 |
| SV-13 (dòng 17) | TC-FR01-212 |
| SV-14 (dòng 18) | TC-FR01-213 |
| SV-15 (dòng 19) | TC-FR01-214 |
| SV-16 (dòng 20) | TC-FR01-215, TC-FR01-230 |
| SV-17 (dòng 21) | TC-FR01-216 |
| SV-18 (dòng 22) | TC-FR01-217, TC-FR01-231 |
| SV-19 (dòng 23) | TC-FR01-218, TC-FR01-232 |
| SV-20 (dòng 24) | TC-FR01-219 |
| SV-21 (dòng 25) | TC-FR01-220 |
| SV-22 (dòng 26) | TC-FR01-221 |
| SV-23 (dòng 27) | TC-FR01-222 |
| SV-24 (dòng 28) | TC-FR01-223 |

SV-xx không ánh xạ được: không có. TC trong JSON có "Nguồn: SV-xx" nhưng mã SV-xx không có trong file SV: không có.

### a) Mã trong file SV không có trong `testcases.json`

Không có.

### c) Cột "AI đã nghĩ tới?" của SV khác nhãn trong `ai_gap_answer.md`

Quy ước so: nhãn AI chứa "Đã nghĩ tới"/"Một phần" hoặc "Nhóm 1" ↔ "Có"; "Không nghĩ tới" hoặc "Nhóm 2" ↔ "Không"; nhãn khác (vd "Không phải bỏ sót", "Nhóm 3") luôn được liệt kê.

| Mã | Dòng file SV | SV ghi | Nhãn AI (nguyên văn: ô (b) với A, tên nhóm với B–D) |
|---|---|---|---|
| SV-01 | dòng 36 | Có | Lớp: đã có. Hiện tượng che lỗi: **không nghĩ tới**. |
| SV-02 | dòng 36 | Có | Không phải bỏ sót; chỉ khác giá trị đại diện (`1` so với bỏ '@' khỏi email đúng mẫu). |
| SV-06 | dòng 36 | Có | **Không nghĩ tới** việc tách lớp hợp lệ của email: AI tách 6 lớp không hợp lệ (EC10–EC15) nhưng chỉ có 2 lớp hợp lệ (EC7, EC8). |
| SV-21 | dòng 37 | Có | **Không nghĩ tới** phần local dạng ngoặc kép mà RFC cho phép. |
| SV-22 | dòng 37 | Có | **Không nghĩ tới.** |
| SV-03 | dòng 38 | Không | **Đã nghĩ tới** (có trong mô tả lớp) nhưng không đưa vào dữ liệu test. |
| SV-04 | dòng 39 | Không | **Đã nghĩ tới:** chính AI viết luật "không rỗng hai bên dấu chấm" trong A2 (bước 1) nhưng ở bước 2 không tách lớp cho luật này. |
| SV-05 | dòng 39 | Không | **Đã nghĩ tới** — như SV-04. |
| SV-07 | dòng 39 | Không | **Một phần:** bản nháp bước 1 của AI đề xuất so sánh không phân biệt hoa/thường; nhưng AI không nghĩ tới việc tách phần local và phần domain theo RFC 5321. |
| SV-13 | dòng 41 | Không | **Đã nghĩ tới một phần:** ở bước 4 AI có grep `limit` trong server.js và thấy `bodyParser.json()` không truyền limit, nhưng không suy ra giới hạn mặc định ~100 KB và không đưa giá trị rất lớn vào. |
| SV-16 | dòng 42 | Không | **Đã nghĩ tới:** AI đọc SEC-05 trong README (dòng 282) ở bước 0 nhưng không đưa vào phạm vi, cũng không dùng để chọn đại diện. |
| SV-18 | dòng 43 | Không | **Đã nghĩ tới** chuyện mã hoá Unicode (note của EC1/EC2) nhưng chỉ chọn ký tự trong BMP, **không nghĩ tới** ký tự 4 byte (emoji). |

### d) Bảng case thứ nhất của SV so với JSON (Tiêu đề / EC / Expected, so chuỗi chính xác)

EC của JSON lấy `ec_target` (không có thì `covers`); EC của SV = các mã `EC\d+` trong cột "EC phủ". 24/24 dòng có khác biệt.

| Mã SV | TC JSON | Khác ở |
|---|---|---|
| SV-01 | TC-FR01-200 | Tiêu đề, EC, Expected |
| SV-02 | TC-FR01-201 | Tiêu đề, EC, Expected |
| SV-03 | TC-FR01-202, TC-FR01-224 | Tiêu đề, Expected |
| SV-04 | TC-FR01-203, TC-FR01-225 | Tiêu đề, EC, Expected |
| SV-05 | TC-FR01-204, TC-FR01-226 | Tiêu đề, EC, Expected |
| SV-06 | TC-FR01-205, TC-FR01-227 | Tiêu đề, EC, Expected |
| SV-07 | TC-FR01-206 | Tiêu đề, EC, Expected |
| SV-08 | TC-FR01-207 | Tiêu đề, EC, Expected |
| SV-09 | TC-FR01-208 | Tiêu đề, EC, Expected |
| SV-10 | TC-FR01-209 | Tiêu đề, EC, Expected |
| SV-11 | TC-FR01-210, TC-FR01-228 | Tiêu đề, EC, Expected |
| SV-12 | TC-FR01-211, TC-FR01-229 | Tiêu đề, EC, Expected |
| SV-13 | TC-FR01-212 | Tiêu đề, EC, Expected |
| SV-14 | TC-FR01-213 | Tiêu đề, EC, Expected |
| SV-15 | TC-FR01-214 | Tiêu đề, EC, Expected |
| SV-16 | TC-FR01-215, TC-FR01-230 | Tiêu đề, EC, Expected |
| SV-17 | TC-FR01-216 | Tiêu đề, EC, Expected |
| SV-18 | TC-FR01-217, TC-FR01-231 | Tiêu đề, EC, Expected |
| SV-19 | TC-FR01-218, TC-FR01-232 | Tiêu đề, EC, Expected |
| SV-20 | TC-FR01-219 | Tiêu đề, EC, Expected |
| SV-21 | TC-FR01-220 | Tiêu đề, Expected |
| SV-22 | TC-FR01-221 | Tiêu đề, EC, Expected |
| SV-23 | TC-FR01-222 | Tiêu đề, EC, Expected |
| SV-24 | TC-FR01-223 | Tiêu đề, EC, Expected |

Số đếm: file SV ghi "Số TC em bổ sung: ?"; bảng thứ nhất có 24 dòng; JSON có 25 case `origin: Human` (= cột "TC SV thêm" của `summary.py`).

## B_FR07

### a) Mã trong file SV không có trong `testcases.json`

Không có.

### c) Cột "AI đã nghĩ tới?" của SV khác nhãn trong `ai_gap_answer.md`

Quy ước so: nhãn AI chứa "Đã nghĩ tới"/"Một phần" hoặc "Nhóm 1" ↔ "Có"; "Không nghĩ tới" hoặc "Nhóm 2" ↔ "Không"; nhãn khác (vd "Không phải bỏ sót", "Nhóm 3") luôn được liệt kê.

| Mã | Dòng file SV | SV ghi | Nhãn AI (nguyên văn: ô (b) với A, tên nhóm với B–D) |
|---|---|---|---|
| TC-FR07-206 | dòng 34 | Có | Nhóm 2 – Không nghĩ tới |

### d) Bảng case thứ nhất của SV so với JSON (Tiêu đề / EC / Expected, so chuỗi chính xác)

EC của JSON lấy `ec_target` (không có thì `covers`); EC của SV = các mã `EC\d+` trong cột "EC phủ". 13/13 dòng có khác biệt.

| Mã SV | TC JSON | Khác ở |
|---|---|---|
| TC-FR07-200 | TC-FR07-200 | Tiêu đề, Expected |
| TC-FR07-201 | TC-FR07-201 | Tiêu đề, EC, Expected |
| TC-FR07-203 | TC-FR07-203 | Tiêu đề, EC, Expected |
| TC-FR07-205 | TC-FR07-205 | Tiêu đề, EC, Expected |
| TC-FR07-206 | TC-FR07-206 | Tiêu đề, EC, Expected |
| TC-FR07-208 | TC-FR07-208 | Tiêu đề, Expected |
| TC-FR07-209 | TC-FR07-209 | Tiêu đề, EC, Expected |
| TC-FR07-210 | TC-FR07-210 | Tiêu đề, Expected |
| TC-FR07-211 | TC-FR07-211 | Tiêu đề, Expected |
| TC-FR07-212 | TC-FR07-212 | Tiêu đề, Expected |
| TC-FR07-213 | TC-FR07-213 | Tiêu đề, EC, Expected |
| TC-FR07-214 | TC-FR07-214 | Tiêu đề, EC, Expected |
| TC-FR07-215 | TC-FR07-215 | Tiêu đề, Expected |

Số đếm: file SV ghi "Số TC em bổ sung: 13"; bảng thứ nhất có 13 dòng; JSON có 13 case `origin: Human` (= cột "TC SV thêm" của `summary.py`).

## C_FR15

### a) Mã trong file SV không có trong `testcases.json`

Không có.

### c) Cột "AI đã nghĩ tới?" của SV khác nhãn trong `ai_gap_answer.md`

Quy ước so: nhãn AI chứa "Đã nghĩ tới"/"Một phần" hoặc "Nhóm 1" ↔ "Có"; "Không nghĩ tới" hoặc "Nhóm 2" ↔ "Không"; nhãn khác (vd "Không phải bỏ sót", "Nhóm 3") luôn được liệt kê.

| Mã | Dòng file SV | SV ghi | Nhãn AI (nguyên văn: ô (b) với A, tên nhóm với B–D) |
|---|---|---|---|
| TC-FR15-202 | dòng 36 | Có | Nhóm 2 – Không nghĩ tới |
| TC-FR15-206 | dòng 36 | Có | Nhóm 2 – Không nghĩ tới |
| TC-FR15-200 | dòng 37 | Không | Nhóm 1 – Đã nghĩ tới nhưng không đưa vào |

### d) Bảng case thứ nhất của SV so với JSON (Tiêu đề / EC / Expected, so chuỗi chính xác)

EC của JSON lấy `ec_target` (không có thì `covers`); EC của SV = các mã `EC\d+` trong cột "EC phủ". 11/11 dòng có khác biệt.

| Mã SV | TC JSON | Khác ở |
|---|---|---|
| TC-FR15-200 | TC-FR15-200 | Tiêu đề, EC, Expected |
| TC-FR15-201 | TC-FR15-201 | Tiêu đề, EC, Expected |
| TC-FR15-202 | TC-FR15-202 | Tiêu đề, EC, Expected |
| TC-FR15-205 | TC-FR15-205 | Tiêu đề, EC, Expected |
| TC-FR15-206 | TC-FR15-206 | Tiêu đề, EC, Expected |
| TC-FR15-207 | TC-FR15-207 | Tiêu đề, EC, Expected |
| TC-FR15-208 | TC-FR15-208 | Tiêu đề, EC, Expected |
| TC-FR15-209 | TC-FR15-209 | Tiêu đề, EC, Expected |
| TC-FR15-211 | TC-FR15-211 | Tiêu đề, EC, Expected |
| TC-FR15-213 | TC-FR15-213 | Tiêu đề, EC, Expected |
| TC-FR15-214 | TC-FR15-214 | Tiêu đề, EC, Expected |

Số đếm: file SV ghi "Số TC em bổ sung: 11"; bảng thứ nhất có 11 dòng; JSON có 11 case `origin: Human` (= cột "TC SV thêm" của `summary.py`).

## D_FR20

### a) Mã trong file SV không có trong `testcases.json`

Không có.

### c) Cột "AI đã nghĩ tới?" của SV khác nhãn trong `ai_gap_answer.md`

Quy ước so: nhãn AI chứa "Đã nghĩ tới"/"Một phần" hoặc "Nhóm 1" ↔ "Có"; "Không nghĩ tới" hoặc "Nhóm 2" ↔ "Không"; nhãn khác (vd "Không phải bỏ sót", "Nhóm 3") luôn được liệt kê.

| Mã | Dòng file SV | SV ghi | Nhãn AI (nguyên văn: ô (b) với A, tên nhóm với B–D) |
|---|---|---|---|
| TC-FR20-204 | dòng 21 | Có | Nhóm 3 – Đã có nhưng bị gỡ theo quyết định SV |
| TC-FR20-206 | dòng 22 | Không | Nhóm 1 – Đã nghĩ tới nhưng không đưa vào |

### d) Bảng case thứ nhất của SV so với JSON (Tiêu đề / EC / Expected, so chuỗi chính xác)

EC của JSON lấy `ec_target` (không có thì `covers`); EC của SV = các mã `EC\d+` trong cột "EC phủ". 6/6 dòng có khác biệt.

| Mã SV | TC JSON | Khác ở |
|---|---|---|
| TC-FR20-200 | TC-FR20-200 | Tiêu đề, Expected |
| TC-FR20-201 | TC-FR20-201 | Tiêu đề, Expected |
| TC-FR20-203 | TC-FR20-203 | Tiêu đề, Expected |
| TC-FR20-204 | TC-FR20-204 | Tiêu đề, Expected |
| TC-FR20-205 | TC-FR20-205 | Tiêu đề, Expected |
| TC-FR20-206 | TC-FR20-206 | Tiêu đề, Expected |

Số đếm: file SV ghi "Số TC em bổ sung: 6"; bảng thứ nhất có 6 dòng; JSON có 6 case `origin: Human` (= cột "TC SV thêm" của `summary.py`).
