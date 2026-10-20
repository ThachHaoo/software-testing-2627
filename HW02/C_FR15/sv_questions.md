# C_FR15 – Câu hỏi khi chuẩn hoá case SV (bước 5b)

Case SV đã chép vào `testcases.json` (suite TS-SV-UI, TS-SV-API, TS-SV-GUI), giữ nguyên văn Tiêu đề, Kỹ thuật, Approach, EC, Expected, Căn cứ, Lý do. Cột Căn cứ được tách cơ học: mã C… vào `assumptions`, mã khác vào `requirements`. Trường SV chưa ghi được đánh "(SV chưa ghi)". AI không tự điền các chỗ dưới đây.

## Chặn bước 6 (cần trả lời trước khi viết script cho case đó)

| Mã | Case | Chỗ cần SV quyết | Phương án |
|---|---|---|---|
| Q1 | TC-204 (C19), TC-209 (C20) | Hai mã giả định được dẫn nhưng mục "Giả định mới" trong `sv_cases.md` vẫn là dòng mẫu, nên nội dung C19/C20 chưa có. | SV ghi C19, C20: chủ đề, loại, căn cứ, "SV chốt + lý do" |
| Q2 | TC-207…215 | `check_domain` báo 9 ERROR "ec_target có EC không nằm trong covers": 207 (EC68), 208 (EC69), 209 (EC69, C20), 210 (EC34, EC69), 211 (EC69), 212 (EC68), 213 (EC57), 214 (EC19, EC69), 215 (EC17, EC68). Ngoài ra TC-209 có mã giả định `C20` nằm trong ô EC mục tiêu. | (a) AI thêm các EC này vào EC phủ, chuyển `C20` sang Căn cứ (sửa cơ học, không đổi ý case) · (b) SV tự sửa |
| Q3 | 203, 204, 207, 212, 213, 216, 217 | Có phần Expected chưa có căn cứ SRS hoặc giả định SV đã chốt:<br>• 203: nút bị disable; chỉ tạo đúng 1 sản phẩm (C13 = SRS im lặng)<br>• 204: không màn hình trắng (dẫn C19, chưa có)<br>• 207: tên lưu nguyên văn, bảng `products` an toàn (SEC-04 là escape khi hiển thị; SEC-05 không có trong requirements của C_FR15)<br>• 212: tạo đúng 30 bản ghi, id tăng dần (C0 là giả định quy trình)<br>• 213: `id` của M không bị đè (C13)<br>• 216: alt chứa đầy đủ tên và được escape (FR-24.4 chỉ yêu cầu alt không rỗng, mô tả nội dung)<br>• 217: tên được tự động trim (C4 là giả định chọn đại diện, SRS im lặng) | Với từng case: (a) SV ghi giả định mới C19+ (SV chốt + lý do) · (b) bỏ phần Expected không có căn cứ · (c) bỏ case (giữ khoảng trống số) |
| Q4 | 200, 201, 207, 211, 215 | Expected có nhiều nhánh, hoặc trái giả định đã chốt:<br>• 211: "hoặc HTTP 500 có bắt lỗi" — C6 (SV chốt) yêu cầu 4xx, không 5xx<br>• 201: EC mục tiêu là EC17 (hợp lệ, Expected chấp nhận) nhưng Expected có nhánh "hoặc form chặn"<br>• 200: "Thêm thành công (hoặc báo lỗi/escape)"<br>• 207, 215: "HTTP 2xx hoặc 4xx" | Với từng case: SV chọn một nhánh, hoặc ghi rõ "chấp nhận cả hai, chỉ kiểm phần <…>" |
| Q5 | TC-204 | EC mục tiêu là EC41 (id tồn tại), nhưng lúc Tab 2 lưu thì M đã bị xoá. Lớp "id không tồn tại khi Sửa" (EC43) đang ghi "chỉ tầng API" (C10). | (a) giữ EC41 · (b) đổi sang EC43 và SV sửa C10 cho phép tầng UI |

## Không chặn

- **Trường SV chưa ghi (đánh "(SV chưa ghi)"):**
  - TC-216, TC-217: Expected của từng bước. Bảng GUI của khung chỉ có cột "Các bước" mà không có Expected theo bước, nhưng linter bắt buộc trường này.
  - TC-216, TC-217: Cleanup. Hai case này tạo sản phẩm.
- **Kỹ thuật:** cả 18 case ghi giá trị ngoài EP/BVA/EG/ST (vd "Security (XSS)", "Concurrency (Spam Click)"). Giữ nguyên văn; check_domain không cảnh báo.
- **Linter:** 15 WARN "title thiếu CONDITION" (tiêu đề giữ nguyên văn SV); 3 WARN "not traced to any requirement" ở TC-209, 210, 211 vì Căn cứ chỉ có mã C.
- **Ngoại lệ quy trình** (ghi trong notes của case: "thực hiện theo Tiêu đề của SV"): 203 (bấm 10 lần), 204 (2 tab), 206 (Sửa SP1 rồi SP2), 209 (body không phải JSON), 211 (Content-Type text/plain), 212 (30 request song song), 213 (khoá `id`, `role` thêm vào body — cột dữ liệu không thể hiện được).
- TC-217 nằm ở bảng GUI nhưng kiểm dữ liệu lưu (FR-15.2) chứ không kiểm thuộc tính giao diện. SV có thể giữ hoặc chuyển sang TS-SV-UI.
