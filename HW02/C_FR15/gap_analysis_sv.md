Feature C - AI gap analysis

| #TC | Tiêu đề | EC phủ | Tầng | Kỹ thuật | Expected | Lý do chọn input |
|---|---|---|---|---|---|---|
| TC-FR15-200 | UI - Chèn payload XSS `<script>alert(1)</script>` vào ô 'Tên sản phẩm' ở form Thêm | EC1, EC5, EC17, EC31 | UI | Security (XSS) | Thêm thành công (hoặc báo lỗi); tên trên bảng hiện chữ thuần chứ tuyệt đối không được tự bật cửa sổ alert XSS. | Thử dán đoạn mã độc nhảy thông báo vào ô tên món đồ xem màn hình Admin có bị lừa cho chạy mã độc không. |
| TC-FR15-201 | UI - Nhập giá tiền dạng E-notation `1e5` vào ô 'Giá tiền' | EC1, EC5, EC17, EC31 | UI | Type / JS Math | Thêm thành công, giá hiển thị đúng 100.000 ₫ (hoặc form chặn từ đầu); DB lưu chuẩn số 100000. | Thử gõ giá tiền kiểu có chữ 'e' (`1e5`) xem màn hình có biết đường đổi ra đúng 100.000 hay bị tính sai bét. |
| TC-FR15-202 | UI - Nhập Giá tiền có các số 0 đứng đầu (`00700000`) | EC1, EC5, EC17, EC31 | UI | Boundary / EG | Thêm thành công, bảng hiện đúng 7.000.000 ₫, DB lưu đúng số 7000000. | Thử gõ thêm mấy số 0 thừa đằng trước xem giao diện có biết tự bỏ đi không hay lại hiển thị nguyên chuỗi lạ quắc. |
| TC-FR15-205 | UI - Dán chuỗi Unicode Full-width `１５０００００` vào ô Giá tiền | EC1, EC5, EC20, EC31 | UI | Unicode / Type Confusion | Form chặn không cho nhập/dán, hoặc báo lỗi giá không hợp lệ; không lưu dữ liệu rác vào DB. | Dùng bộ số kiểu béo (full-width) từ bàn phím tiếng Trung/Nhật nhìn y chang số thật xem màn hình có bị nhìn nhầm không. |
| TC-FR15-206 | UI - Bấm nút 'Sửa' SP1, chỉnh thông tin rồi bấm 'Sửa' SP2 luôn mà không bấm 'Hủy' | EC3, EC11, EC24 | UI | State Transition | Form tự đổi sang đúng thông tin SP2; khi bấm 'Lưu' thì chỉ SP2 bị đổi, SP1 giữ nguyên không bị ảnh hưởng. | Đang chuyển dở sang sửa món khác mà không bấm hủy xem màn hình có bị nhầm lẫn dữ liệu giữa hai món đồ không. |
| TC-FR15-207 | API - Chèn SQL Injection `Robert'); DROP TABLE products;--` vào trường `name` | EC1, EC5, EC17, EC31 | API | Security (SQLi) | Trả về 2xx hoặc 4xx; tên lưu nguyên văn chuỗi đó và bảng sản phẩm trong DB vẫn an toàn nguyên vẹn. | Thử gõ câu lệnh phá hoại cơ sở dữ liệu vào ô tên xem backend có bị sập hay bị xóa sạch bảng sản phẩm không. |
| TC-FR15-208 | API - POST /api/products gửi `price` dưới dạng số âm cực đại `-999999999999` | EC1, EC5, EC19, EC31 | API | Business Logic / Boundary | Trả về HTTP 4xx kèm thông báo lỗi; DB không được tạo thêm sản phẩm mới. | Gửi một mức giá âm kỷ lục xem máy chủ có khờ dại chấp nhận món đồ có giá âm hay không. |
| TC-FR15-209 | API - POST /api/products khi gửi `price` = `Infinity` thô | EC1, EC5, EC31 | API | JS Math / Exception | Trả về HTTP 4xx kèm thông báo lỗi (không văng trang lỗi 500 lộ thông tin); DB không bị thay đổi. | Gửi chữ 'vô cực' dạng số xem server có biết đường từ chối hay lại bị ngợp rồi lăn ra sập. |
| TC-FR15-211 | API - POST /api/products gửi Header `Content-Type: text/plain` chứa JSON thô | EC1, EC5, EC17, EC31 | API | Middleware Mismatch | Trả về HTTP 4xx (400 hoặc 415) hoặc trả lỗi 500 có bắt ngoại lệ; DB không tạo sản phẩm. | Dán nhãn sai cho gói tin gửi đi xem máy chủ có biết đường kiểm tra nhãn để từ chối hay lại bị lỗi văng trang web. |
| TC-FR15-213 | API - PUT /api/products/:id truyền thêm trường `"id": 1` và `"role": "admin"` vào Body | EC3, EC11, EC24, EC35 | API | Security (Mass Assignment) | Trả về HTTP 2xx; DB cập nhật các thông tin cơ bản nhưng ID của sản phẩm tuyệt đối không bị đè đổi. | Cố tình nhét thêm các trường cấm vào gói tin cập nhật xem hệ thống có dại dột cho đè mã sản phẩm hay quyền hạn không. |
| TC-FR15-214 | API - POST /api/products gửi `price` là số thập phân cực nhỏ `1e-324` | EC1, EC5, EC31 | API | JS Math / Underflow | Trả về HTTP 4xx kèm thông báo lỗi (vì JS tự biến `1e-324` thành 0); DB không bị thay đổi. | Gửi một giá tiền siêu nhỏ xem hệ thống có bị nhầm thành số 0 rồi cho qua cửa một cách vô lý hay không. |

Số TC em bổ sung: **11**

---

**Các kịch bản đề xuất nhưng gạt bỏ / không thực thi:**
- **TC-FR15-203 (Spam click Lưu SP UI):** Bỏ qua do không chạy thực tế kịch bản dồn dập ở UI.
- **TC-FR15-204 (Multi-tab Concurrency Admin):** Bỏ qua do không thực thi kịch bản đa phiên.
- **TC-FR15-210 (API category_id dạng mảng):** Bỏ qua do cắt giảm biến thể type confusion.
- **TC-FR15-212 (API POST Concurrent 30 request):** Bỏ qua kịch bản kiểm thử tải song song DB.
- **TC-FR15-215 (API price MAX_SAFE_INTEGER):** Bỏ qua kịch bản tràn số quá lớn.
- **TC-FR15-216 (GUI Alt Text Image):** Bỏ qua kịch bản kiểm thử thuộc tính GUI thẻ HTML.
- **TC-FR15-217 (GUI Trim Tên SP):** Bỏ qua do gộp vào luồng làm sạch form tiêu chuẩn.

---

**Vì sao AI bỏ sót** 

| Case/bug AI bỏ sót | Loại nguyên nhân (prompt / giới hạn công cụ / độ phức tạp feature) | AI đã nghĩ tới nhưng không đưa vào? | Giải thích |
|---|---|---|---|
| TC-FR15-202, TC-FR15-206, TC-FR15-208 | Prompt (Cơ chế Minimum Set / Tối ưu số lượng case) | Có | AI vốn đã phân tích ra các nhóm dữ liệu đúng hay sai rồi. Nhưng vì bị dặn chỉ chọn ít case nhất có thể nên nó gọt bỏ các biến thể dữ liệu thực tế (như gõ thêm số 0 đầu hay chuyển đổi qua lại giữa các nút). |
| TC-FR15-200, TC-FR15-207, TC-FR15-213 | Độ phức tạp feature (Mảng Security / Injection) | Không | AI đinh ninh hệ thống chạy trong một thế giới màu hồng và người dùng ai cũng đàng hoàng. Nếu tài liệu không dặn check bảo mật thì nó sẽ không bao giờ tự nghĩ ra các kịch bản phá hoại như gõ SQLi, Stored XSS hay nhét thêm trường cấm. |
| TC-FR15-201, TC-FR15-205, TC-FR15-209, TC-FR15-214 | Giới hạn công cụ (Không chạy thử app thật) | Không | AI không bật chương trình thật lên để bấm thử, nên nó hoàn toàn không biết được những trò lắt léo của máy tính khi xử lý số (như gõ chữ 'e' vào ô số, dùng số kiểu béo CJK, hay số quá nhỏ tự biến thành 0). |
| TC-FR15-211 | Giới hạn công cụ (Tầng Middleware Parser) | Không | AI chỉ chăm chăm nhìn vào phần nội dung nghiệp vụ bên trong gói tin, chứ không hề kiểm tra xem nếu dán nhãn sai cho gói tin thì các bộ lọc bên ngoài của máy chủ có biết đường chặn lại hay không. |