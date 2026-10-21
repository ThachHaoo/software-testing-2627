Feature B - AI gap analysis

| #TC | Tiêu đề | EC phủ | Tầng | Kỹ thuật | Expected | Lý do chọn input |
|---|---|---|---|---|---|---|
| TC-FR07-200 | UI - Chèn payload XSS `<script>alert(1)</script>` vào ô Số lượng ở trang chi tiết | EC5 | UI | Security (XSS) | Ô input chặn hoặc xóa mã độc ngay khi gõ/dán; bấm 'Thêm' thì không bị nhảy thông báo lạ và giỏ hàng giữ nguyên. | Thử dán một đoạn mã độc vào ô nhập số lượng xem màn hình giao diện có biết đường chặn lại hay bị lừa chạy mã độc. |
| TC-FR07-201 | UI - Bấm liên tục 20 lần nút 'Thêm vào giỏ' ở Trang chủ (Spam click) | EC1, EC37 | UI | Race Condition / Time-series | Vào giỏ hàng thấy đúng 1 dòng món đó với Số lượng = 20, Thành tiền = 20 nhân Đơn giá, màn hình không văng lỗi. | Giả lập cảnh người dùng nhấn nút mua hàng lia lịa do mạng lag hoặc cố tình nhấp chuột thật nhanh để phá. |
| TC-FR07-203 | UI - Nhập số lượng dạng E-notation `1e5` vào ô Số lượng ở trang chi tiết | EC1, EC5 | UI | Type / JS Math | Giỏ hàng tính đúng Số lượng = 100000 và Thành tiền chuẩn; không bị biến thành số 1 hay bị lỗi không xác định (`NaN`). | Thử gõ số kiểu có chữ 'e' (`1e5`) vào ô số lượng xem màn hình có biết đường đổi ra đúng 100.000 hay bị tính sai bét. |
| TC-FR07-205 | UI - Đổi Số lượng giữa 2 lần bấm 'Thêm vào giỏ' liên tiếp ở trang chi tiết | EC1, EC8, EC9, EC37, EC45 | UI | State Transition | Lần đầu thêm 2 món, lần sau chọn 5 món rồi thêm tiếp thì giỏ hàng phải cộng dồn đúng thành 7 món. | Kiểm tra nghi vấn chương trình bị ngáo, bỏ quên lần chọn đầu tiên mà chỉ ăn đúng số lượng ở lần chọn thứ hai. |
| TC-FR07-206 | UI - Nhập Số lượng có số 0 đứng đầu (`007`) | EC1, EC8, EC41 | UI | Boundary / EG | Giỏ hàng hiện đúng số lượng là `7` và tính tiền chuẩn theo số 7. | Thử gõ thêm mấy số 0 đằng trước xem giao diện có biết tự bỏ số 0 thừa đi không hay lại hiển thị nguyên chuỗi lạ quắc. |
| TC-FR07-208 | API - Thêm sản phẩm qua API với `quantity` = `1e-324` | EC2, EC51 | API | JS Math / Underflow | Trả về lỗi không chấp nhận, giỏ hàng giữ nguyên không bị thay đổi. | Gửi một số thực siêu nhỏ xem hệ thống có bị nhầm thành số 0 rồi cho qua cửa một cách vô lý hay không. |
| TC-FR07-209 | API - Thêm sản phẩm qua API với `quantity` = `Infinity` thô | EC51 | API | JS Math / Exception | Trả về lỗi không chấp nhận, giỏ hàng giữ nguyên không bị thay đổi. | Gửi chữ 'vô cực' dạng số xem server có biết đường từ chối hay lại bị ngợp rồi lăn ra sập. |
| TC-FR07-210 | API - Gửi `price` âm cực đại `-999999999999` để cố tình làm âm tổng tiền | EC16, EC50 | API | Business Logic / Boundary | Server vẫn xử lý bình thường nhưng BẮT BUỘC phải tự lấy giá chuẩn trong máy ra tính, mặc kệ giá âm gửi lên. | Thử gửi giá tiền âm kỷ lục xem backend có khờ dại tin lời người dùng rồi tính ra tổng tiền âm để cửa hàng phải thối ngược tiền lại không. |
| TC-FR07-211 | API - Type Confusion: Gửi `id` dạng mảng `[1, 2, 3]` thay vì số | EC13, EC51 | API | Type Confusion | Trả về lỗi kiểu dữ liệu, giỏ hàng giữ nguyên không bị thay đổi. | Cố tình gửi một danh sách mã thay vì một mã đơn lẻ xem hệ thống có bị rối rồi xử lý lung tung không. |
| TC-FR07-212 | API - Type Confusion: Gửi `id` dạng object `{"id": 1}` thay vì số | EC13, EC51 | API | Type Confusion | Trả về lỗi kiểu dữ liệu, giỏ hàng giữ nguyên không bị thay đổi. | Thử tráo kiểu dữ liệu mã sản phẩm thành dạng đối tượng phức tạp xem backend có phát hiện ra để chặn lại không. |
| TC-FR07-213 | API - Bắn 50 request POST /api/cart song song đồng thời | EC1, EC37, EC50 | API | Concurrency / Lost Updates | Cả 50 gói tin đều được xử lý ngon lành, giỏ hàng tính đúng tổng dồn đủ 50 món không bị rơi mất món nào. | Giả lập tình huống bắn dồn dập 50 yêu cầu thêm hàng trong cùng một thời điểm xem server có bị sót mất yêu cầu nào không. |
| TC-FR07-214 | API - Gửi Header `Content-Type: text/plain` nhưng body là JSON hợp lệ | EC51 | API | Middleware Mismatch | Trả về lỗi không đúng định dạng (400 hoặc 415), giỏ hàng không bị ảnh hưởng. | Dán nhãn sai cho gói tin gửi đi xem máy chủ có biết đường kiểm tra nhãn để từ chối hay lại bị lỗi văng trang web. |
| TC-FR07-215 | API - Gửi `quantity` vượt giới hạn `MAX_SAFE_INTEGER` (`9007199254740993`) | EC1, EC50 | API | Boundary / Integer Overflow | Trả về thông báo xử lý phù hợp; nếu nhận thì khi tính tiền không được bị tính sai lệch số do vượt giới hạn. | Nhập một số lượng bự chảng vượt quá khả năng tính toán an toàn của máy tính xem hệ thống có bị tính sai tiền không. |

Số TC em bổ sung: **13**

---

**Các kịch bản đề xuất nhưng gạt bỏ / không thực thi:**
- **TC-FR07-202 (Multi-tab Concurrency):** Bỏ qua do không thực thi chạy thực tế trên môi trường đa phiên.
- **TC-FR07-204 (localStorage JSON rác):** Bỏ qua do hệ thống giỏ hàng phía Web thực tế không dùng `localStorage` để lưu giỏ (B0d).
- **TC-FR07-207 (API XSS name):** Bỏ qua do tách riêng phạm vi kiểm thử API thuần túy.

---

**Vì sao AI bỏ sót** 

| Case/bug AI bỏ sót | Loại nguyên nhân (prompt / giới hạn công cụ / độ phức tạp feature) | AI đã nghĩ tới nhưng không đưa vào? | Giải thích |
|---|---|---|---|
| TC-FR07-205, TC-FR07-206, TC-FR07-210 | Prompt (Cơ chế Minimum Set / Giả định B8) | Có | AI vốn đã hình dung ra các bước thêm hàng và đinh ninh server sẽ tự lấy giá chuẩn trong máy. Nhưng vì bị dặn chỉ chọn ít case nhất có thể nên nó tiện tay gọt bỏ hết các trường hợp dữ liệu biến tấu này. |
| TC-FR07-200 | Độ phức tạp feature (Mảng Security / Injection) | Không | AI nghĩ trang web chạy trong một thế giới màu hồng và người dùng ai cũng đàng hoàng, nên nếu tài liệu không dặn check bảo mật thì nó không bao giờ tự nghĩ ra các trò chèn mã độc phá hoại. |
| TC-FR07-201, TC-FR07-213 | Độ phức tạp feature (Yếu tố thời gian & Tương tranh) | Không | AI chỉ nhìn ứng dụng theo kiểu một người thao tác thong thả từng bước một. Nó không thể hình dung ra cảnh người dùng nhấp chuột điên cuồng do mạng lag hay hàng chục yêu cầu bắn vào máy chủ cùng một lúc. |
| TC-FR07-203, TC-FR07-208, TC-FR07-209, TC-FR07-215 | Giới hạn công cụ (Không chạy thử app thật) | Không | AI không bật chương trình thật lên để bấm thử, nên nó hoàn toàn không biết được những trò lắt léo của máy tính khi xử lý số (như vụ gõ chữ 'e' vào ô số, số quá nhỏ tự biến thành 0, hay số quá bự làm tính sai tiền). |
| TC-FR07-211, TC-FR07-212 | Độ phức tạp feature (Trò Type Confusion Exploit) | Không | AI chưa từng trải qua mấy trò cố tình gửi sai kiểu dữ liệu (như gửi nguyên một danh sách thay vì một số đơn lẻ) để làm máy chủ bị lúng túng rồi xử lý lỗi. |
| TC-FR07-214 | Giới hạn công cụ (Tầng Middleware Parser) | Không | AI chỉ chăm chăm nhìn vào phần nội dung nghiệp vụ bên trong gói tin, chứ không hề kiểm tra xem nếu dán nhãn sai cho gói tin thì các bộ lọc bên ngoài của máy chủ có biết đường chặn lại hay không. |