### Phạm vi
SV chốt 2026-10-20 (C5=a, C6=a, C8=a, C12, C13). form 'Thêm sản phẩm mới' / 'Sửa sản phẩm', nút 'Sửa', 'Xóa' và bảng sản phẩm ở tab 'Sản phẩm' của web admin (tầng UI); endpoint POST /api/products, PUT /api/products/:id, DELETE /api/products/:id, GET /api/products(/:id) (tầng API, suite riêng). Trong phạm vi: FR-15 (phân lớp + BVA); kiểm soát quyền của FR-12.2 cho 3 endpoint ghi của /api/products (C5); thuộc tính GUI của form/bảng sản phẩm (FR-21.3, FR-22.1, FR-22.4, FR-24.4, SEC-04) kiểm bằng suite TS-GUI riêng, không phân lớp (C12). Ngoài phạm vi: import CSV (FR-16), Category CRUD (FR-14, của thành viên khác), Dashboard (FR-13), hiển thị sản phẩm trên frontend-web/mobile (FR-05, FR-06, FR-20) (C13).

### Yêu cầu (test basis)
| Mã | Nội dung |
|---|---|
| FR-15.1 | Admin có thể Thêm / Xem / Sửa / Xóa sản phẩm. |
| FR-15.2 | Tên sản phẩm: bắt buộc, tối đa 255 ký tự. |
| FR-15.3 | Giá: bắt buộc, phải là số dương (> 0). |
| FR-15.4 | Danh mục: bắt buộc, phải chọn từ danh sách có sẵn. |
| FR-15.5 | Khi Sửa một sản phẩm, chỉ sản phẩm đó bị thay đổi — các sản phẩm khác giữ nguyên. |
| FR-12.2 | (liên quan, C5) Các API có tính ảnh hưởng dữ liệu POST/PUT/DELETE /api/products phải yêu cầu (1) Token JWT hợp lệ, (2) role = 'admin' trong Token. |
| API-PROD | GET /api/products, GET /api/products/:id, POST /api/products, PUT /api/products/:id, DELETE /api/products/:id; body Thêm/Sửa JSON {name, price, description, imageUrl, category_id} (api_specification.md dòng 78–100). Không mô tả phản hồi lỗi. |
| SEC-02 | (liên quan, C5) Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ (README.md dòng 279). |
| SEC-03 | (liên quan, C5) API Admin phải kiểm tra role = 'admin' trong Token, không chỉ kiểm tra sự tồn tại của Token (README.md dòng 280). |
| FR-21.3 | (GUI, C12) Luôn dùng ký hiệu ₫ với định dạng phân cách hàng nghìn — áp cho cột 'Giá' của bảng sản phẩm. |
| FR-22.1 | (GUI, C12) Tất cả trường bắt buộc phải có ký hiệu * bên cạnh nhãn — áp cho Tên, Giá, Danh mục. |
| FR-22.4 | (GUI, C12) Thông báo lỗi phải xuất hiện trên nút submit, không phải bên dưới. |
| FR-24.4 | (GUI, C12) Tất cả ảnh sản phẩm phải có thuộc tính alt mô tả nội dung ảnh (không để rỗng). |
| SEC-04 | (GUI, C12) Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng innerHTML trực tiếp (README.md dòng 281) — áp cho tên sản phẩm trong bảng. |

### Bước 1 — Biến vào/ra
| Mã | Biến | Vào/Ra | Nguồn | Kiểu | Ràng buộc (đặc tả) | Ghi chú |
|---|---|---|---|---|---|---|
| V1 | Thao tác CRUD | Vào | UI: tiêu đề form 'Thêm sản phẩm mới' / 'Sửa sản phẩm' (App.jsx dòng 487–489), nút 'Lưu sản phẩm' (545–547), nút 'Sửa' và 'Xóa' trên từng dòng bảng (592–603), bảng sản phẩm (567–608) · API: POST /api/products, GET /api/products(/:id), PUT /api/products/:id, DELETE /api/products/:id (api_specification.md dòng 80–90) | enum {Thêm, Xem, Sửa, Xóa} | Admin thực hiện được cả 4 thao tác (FR-15.1). Ràng buộc đầu vào áp cho Thêm và Sửa (C8). | Nút 'Hủy sửa' (App.jsx dòng 548–565): SRS im lặng – chấp nhận mọi cách hợp lý (C13). |
| V2 | Tên sản phẩm | Vào | UI: ô placeholder 'Tên sản phẩm' (App.jsx dòng 491–499) · API: body.name (api_specification.md dòng 94) | string | Bắt buộc; độ dài 1–255 ký tự (FR-15.2). Chuỗi chỉ khoảng trắng → C3. Đơn vị đếm → C4. Sai kiểu/thiếu ở API → C9. | Quan sát code (gray-box): ô có thuộc tính required, không có maxLength; không có phần tử nhãn (chỉ placeholder). Chỉ ghi nhận, chưa kết luận. |
| V3 | Giá | Vào | UI: ô placeholder 'Giá tiền', type="number" (App.jsx dòng 500–507) · API: body.price (api_specification.md dòng 95) | number (₫) | Bắt buộc; > 0, số thực (FR-15.3, C1 SV chốt: bước nhảy 0.1, LB = 0.1). Không có cận trên (C2, no_upper_bound). Sai kiểu/thiếu ở API → C9. | Quan sát code (gray-box): ô không có required/min; cột products.price kiểu INTEGER (database.js dòng 67). Chỉ ghi nhận, chưa kết luận. |
| V4 | Danh mục | Vào | UI: ô chọn (select, không nhãn) lấy danh sách từ GET /api/categories (App.jsx dòng 528–543; 49–50), mặc định category_id 1 (dòng 101) · API: body.category_id (api_specification.md dòng 98) · Dữ liệu: 3 danh mục seed id 1–3 (database.js dòng 84–88) | integer (id danh mục) | Bắt buộc; phải thuộc danh sách danh mục có sẵn (FR-15.4, C11). Thiếu/sai kiểu ở API → C9. | Gray-box: lớp 'không chọn' và 'ngoài danh sách' chỉ tạo được qua API (C11). |
| V5 | Mô tả | Vào | UI: ô textarea placeholder 'Mô tả' (App.jsx dòng 517–526) · API: body.description (api_specification.md dòng 96) | string | FR-15 không ràng buộc — SRS im lặng – chấp nhận mọi cách hợp lý (C13). Giữ giá trị nominal hợp lệ trong mọi case. |  |
| V6 | URL Ảnh | Vào | UI: ô placeholder 'URL Ảnh' (App.jsx dòng 509–515) · API: body.imageUrl (api_specification.md dòng 97) | string (URL) | FR-15 không ràng buộc — SRS im lặng – chấp nhận mọi cách hợp lý (C13). Giữ giá trị nominal hợp lệ trong mọi case. Ảnh hiển thị phải có alt (FR-24.4, TS-GUI). |  |
| V7 | Sản phẩm mục tiêu (khi Xem chi tiết / Sửa / Xóa) | Vào | UI: dòng bảng được bấm 'Sửa' / 'Xóa' (App.jsx dòng 594, 600) · API: tham số đường dẫn :id | integer (id sản phẩm) | Tồn tại → thao tác áp lên đúng sản phẩm đó (FR-15.1, FR-15.5). Không tồn tại → C10 (chỉ ở API). |  |
| V8 | Danh tính người gọi / token | Vào | UI: phiên admin sau 'Admin Login' (adminToken trong localStorage, App.jsx dòng 7, 35–39, 61–74) · API: header Authorization: Bearer <token> (server.js dòng 100–110) | enum {không token, token sai, token role user, token role admin} | POST/PUT/DELETE /api/products chỉ chấp nhận token hợp lệ có role admin (FR-12.2, SEC-02, SEC-03). Phạm vi → C5. | Quan sát code (gray-box): kiểm role khi đăng nhập UI nằm ở client (App.jsx dòng 65–67); route POST/PUT/DELETE /api/products không gắn authenticateToken (server.js dòng 167, 179, 191). Chỉ ghi nhận, chưa kết luận. |
| V9 | Các sản phẩm khác trong CSDL (trạng thái) | Vào | Dữ liệu: bảng products — 5 sản phẩm seed (database.js dòng 97–103) + sản phẩm do case tạo | list | Có ít nhất 1 sản phẩm khác ngoài sản phẩm mục tiêu, để quan sát FR-15.5. |  |
| V10 | Bản ghi sản phẩm sau thao tác | Ra | API: GET /api/products (server.js dòng 141–157), GET /api/products/:id (dòng 159–165); trường id, name, price, description, imageUrl, category_id (database.js dòng 64–71) | record | Thêm hợp lệ → thêm đúng 1 bản ghi, các trường = giá trị nhập; Sửa hợp lệ → bản ghi mục tiêu = giá trị mới; Xóa → bản ghi không còn (FR-15.1). Dữ liệu không hợp lệ / không đủ quyền → không tạo, không đổi (C5, C6, C7). | Quan sát code (gray-box): GET /api/products/:id trả 200 {} khi không tìm thấy (server.js dòng 161) và trả price dạng chuỗi khi id chẵn (dòng 162) — ảnh hưởng cách so sánh ở điểm quan sát; chưa kết luận, xác nhận ở bước 6. |
| V11 | Danh sách sản phẩm trên UI | Ra | UI: tab 'Sản phẩm' (App.jsx dòng 240–243), bảng cột 'Ảnh', 'Tên SP', 'Giá', 'Hành động' (dòng 567–608) | list | Phản ánh kết quả Thêm/Sửa/Xóa (FR-15.1 – Xem). Thuộc tính chung — khẳng định ở đúng 1 case TS-GUI (C12): ₫ + phân cách hàng nghìn ở cột 'Giá' (FR-21.3), alt ảnh (FR-24.4), tên hiển thị an toàn (SEC-04). |  |
| V12 | Các sản phẩm khác sau khi Sửa | Ra | UI: các dòng khác của bảng sản phẩm · API: các phần tử khác trong GET /api/products | list | Giữ nguyên — SAU = TRƯỚC (FR-15.5). Quan sát cả UI và API (mỗi tầng một case). |  |
| V13 | Phản hồi API sản phẩm | Ra | API: mã HTTP + body của POST/PUT/DELETE /api/products(/:id); body thành công quan sát được trong code: {"message": "Product created", "id"} (server.js dòng 174), {"message": "Product updated"} (dòng 186), {"message": "Product deleted"} (dòng 194) | HTTP | Hợp lệ → 2xx (api_specification không quy định body → không khẳng định nội dung). Dữ liệu không hợp lệ → 4xx kèm error (C6, C9); id không tồn tại → 4xx (C10); không đủ quyền → 4xx (C5). |  |
| V14 | Phản hồi trên UI khi lưu / xóa | Ra | UI: hộp alert (App.jsx dòng 115, 129, 138), form trở về trạng thái 'Thêm sản phẩm mới' (dòng 120–127), bong bóng kiểm tra HTML5 của ô có required | enum | Thành công: SRS im lặng – chấp nhận mọi cách hợp lý, không khẳng định nội dung (C13). Bị từ chối: oracle theo C7. Thuộc tính chung — vị trí thông báo lỗi trên nút 'Lưu sản phẩm' (FR-22.4) khẳng định ở đúng 1 case TS-GUI (C12). |  |

### Bước 2 — Complete Set of Partitions
| EC | Biến | Lớp tương đương | Hợp lệ | Hướng dẫn | Yêu cầu | Ghi chú |
|---|---|---|---|---|---|---|
| EC1 | Thao tác CRUD | Thêm | ✔ | set | FR-15.1 | 1 lớp/giá trị của tập thao tác (FR-15.1). Không có lớp 'ngoài tập': SRS không nêu thao tác nào khác để đặt Expected → cảnh báo 'không có lớp không hợp lệ' giữ nguyên. |
| EC2 | Thao tác CRUD | Xem | ✔ | set | FR-15.1 | 1 lớp/giá trị của tập thao tác (FR-15.1). Không có lớp 'ngoài tập': SRS không nêu thao tác nào khác để đặt Expected → cảnh báo 'không có lớp không hợp lệ' giữ nguyên. |
| EC3 | Thao tác CRUD | Sửa | ✔ | set | FR-15.1 | 1 lớp/giá trị của tập thao tác (FR-15.1). Không có lớp 'ngoài tập': SRS không nêu thao tác nào khác để đặt Expected → cảnh báo 'không có lớp không hợp lệ' giữ nguyên. |
| EC4 | Thao tác CRUD | Xóa | ✔ | set | FR-15.1 | 1 lớp/giá trị của tập thao tác (FR-15.1). Không có lớp 'ngoài tập': SRS không nêu thao tác nào khác để đặt Expected → cảnh báo 'không có lớp không hợp lệ' giữ nguyên. |
| EC5 | Tên sản phẩm | [Thêm] Độ dài 1–255 ký tự, có ít nhất 1 ký tự khác khoảng trắng (vd 'Tai nghe {ts}') | ✔ | range | FR-15.2 | Lớp hợp lệ của khoảng 1–255 (FR-15.2). UI + API (POST /api/products). Đếm ký tự theo C4. Tách theo thao tác (C8). |
| EC6 | Tên sản phẩm | [Thêm] Rỗng — 0 ký tự | ✘ | range | FR-15.2 | Lớp không hợp lệ phía dưới (bắt buộc). UI: ô 'Tên sản phẩm' để trống; API: name = "". |
| EC7 | Tên sản phẩm | [Thêm] Dài hơn 255 ký tự | ✘ | range | FR-15.2 | Lớp không hợp lệ phía trên. UI + API. |
| EC8 | Tên sản phẩm | [Thêm] Chỉ gồm khoảng trắng (vd '   ') | ✘ | split | FR-15.2, C3 | C3 SV chốt: coi như trống. Tách khỏi lớp 'rỗng' vì độ dài > 0 — có lý do tin bị xử lý khác chuỗi rỗng. UI + API. |
| EC9 | Tên sản phẩm | [Thêm] API: thiếu trường name hoặc name = null | ✘ | must-be | FR-15.2, C9 | Chỉ tầng API (C9). Đại diện thiếu/null chọn ở bước 3. |
| EC10 | Tên sản phẩm | [Thêm] API: name không phải chuỗi (vd số 123) | ✘ | type | FR-15.2, C9 | Chỉ tầng API (C9). |
| EC11 | Tên sản phẩm | [Sửa] Độ dài 1–255 ký tự, có ít nhất 1 ký tự khác khoảng trắng (vd 'Tai nghe {ts}') | ✔ | range | FR-15.2 | Lớp hợp lệ của khoảng 1–255 (FR-15.2). UI + API (PUT /api/products/:id). Đếm ký tự theo C4. Tách theo thao tác (C8). |
| EC12 | Tên sản phẩm | [Sửa] Rỗng — 0 ký tự | ✘ | range | FR-15.2 | Lớp không hợp lệ phía dưới (bắt buộc). UI: ô 'Tên sản phẩm' để trống; API: name = "". |
| EC13 | Tên sản phẩm | [Sửa] Dài hơn 255 ký tự | ✘ | range | FR-15.2 | Lớp không hợp lệ phía trên. UI + API. |
| EC14 | Tên sản phẩm | [Sửa] Chỉ gồm khoảng trắng (vd '   ') | ✘ | split | FR-15.2, C3 | C3 SV chốt: coi như trống. Tách khỏi lớp 'rỗng' vì độ dài > 0 — có lý do tin bị xử lý khác chuỗi rỗng. UI + API. |
| EC15 | Tên sản phẩm | [Sửa] API: thiếu trường name hoặc name = null | ✘ | must-be | FR-15.2, C9 | Chỉ tầng API (C9). Đại diện thiếu/null chọn ở bước 3. |
| EC16 | Tên sản phẩm | [Sửa] API: name không phải chuỗi (vd số 123) | ✘ | type | FR-15.2, C9 | Chỉ tầng API (C9). |
| EC17 | Giá | [Thêm] Số nguyên > 0 (vd 1500000) | ✔ | range | FR-15.3 | Lớp hợp lệ của miền > 0 (FR-15.3). Không có cận trên (C2) → miền một phía. UI + API (POST /api/products). |
| EC18 | Giá | [Thêm] Số thập phân > 0, không nguyên (vd 0.5; 1500000.5) | ✔ | split | FR-15.3, C1 | Lớp HỢP LỆ — Expected = chấp nhận (C1 SV chốt: mọi số thực > 0 hợp lệ); lớp số nguyên cùng biến cũng là lớp hợp lệ. Tách khỏi lớp số nguyên vì có lý do tin bị xử lý khác (gray-box): cột products.price kiểu INTEGER (../eshop-sut/backend/database.js dòng 67). UI + API. |
| EC19 | Giá | [Thêm] Số ≤ 0 (vd 0; -1000) | ✘ | range | FR-15.3 | Lớp không hợp lệ phía dưới. Phía trên không có lớp không hợp lệ (C2). UI + API. |
| EC20 | Giá | [Thêm] UI: ô 'Giá tiền' để trống | ✘ | must-be | FR-15.3 | Chỉ tầng UI (bắt buộc). Chuỗi không phải số gõ vào ô type=number cho giá trị rỗng → cùng lớp. Bản API tương ứng: lớp thiếu/null. |
| EC21 | Giá | [Thêm] API: thiếu trường price hoặc price = null | ✘ | must-be | FR-15.3, C9 | Chỉ tầng API (C9). |
| EC22 | Giá | [Thêm] API: price là chuỗi chữ (vd "abc") | ✘ | type | FR-15.3, C9 | Chỉ tầng API (C9). |
| EC23 | Giá | [Thêm] API: price là chuỗi số (vd "100000") | ✘ | type | FR-15.3, C9 | Chỉ tầng API. C9 SV chốt: chuỗi số là sai kiểu. Tách khỏi chuỗi chữ vì giá trị số của nó hợp lệ — có lý do tin bị xử lý khác (chuyển kiểu ngầm). |
| EC24 | Giá | [Sửa] Số nguyên > 0 (vd 1500000) | ✔ | range | FR-15.3 | Lớp hợp lệ của miền > 0 (FR-15.3). Không có cận trên (C2) → miền một phía. UI + API (PUT /api/products/:id). |
| EC25 | Giá | [Sửa] Số thập phân > 0, không nguyên (vd 0.5; 1500000.5) | ✔ | split | FR-15.3, C1 | Lớp HỢP LỆ — Expected = chấp nhận (C1 SV chốt: mọi số thực > 0 hợp lệ); lớp số nguyên cùng biến cũng là lớp hợp lệ. Tách khỏi lớp số nguyên vì có lý do tin bị xử lý khác (gray-box): cột products.price kiểu INTEGER (../eshop-sut/backend/database.js dòng 67). UI + API. |
| EC26 | Giá | [Sửa] Số ≤ 0 (vd 0; -1000) | ✘ | range | FR-15.3 | Lớp không hợp lệ phía dưới. Phía trên không có lớp không hợp lệ (C2). UI + API. |
| EC27 | Giá | [Sửa] UI: ô 'Giá tiền' để trống | ✘ | must-be | FR-15.3 | Chỉ tầng UI (bắt buộc). Chuỗi không phải số gõ vào ô type=number cho giá trị rỗng → cùng lớp. Bản API tương ứng: lớp thiếu/null. |
| EC28 | Giá | [Sửa] API: thiếu trường price hoặc price = null | ✘ | must-be | FR-15.3, C9 | Chỉ tầng API (C9). |
| EC29 | Giá | [Sửa] API: price là chuỗi chữ (vd "abc") | ✘ | type | FR-15.3, C9 | Chỉ tầng API (C9). |
| EC30 | Giá | [Sửa] API: price là chuỗi số (vd "100000") | ✘ | type | FR-15.3, C9 | Chỉ tầng API. C9 SV chốt: chuỗi số là sai kiểu. Tách khỏi chuỗi chữ vì giá trị số của nó hợp lệ — có lý do tin bị xử lý khác (chuyển kiểu ngầm). |
| EC31 | Danh mục | [Thêm] category_id thuộc danh sách danh mục có sẵn (vd 2) | ✔ | set | FR-15.4, C11 | C11: danh sách = bảng categories lúc lưu (seed id 1–3). Các danh mục xử lý như nhau → 1 lớp. UI (ô chọn) + API. |
| EC32 | Danh mục | [Thêm] API: category_id không có trong danh sách (vd 999) | ✘ | set | FR-15.4, C11 | Chỉ tầng API — ô chọn trên UI chỉ có danh mục có sẵn (C11, gray-box). |
| EC33 | Danh mục | [Thêm] API: thiếu trường category_id hoặc category_id = null | ✘ | must-be | FR-15.4, C9 | Chỉ tầng API (C9). |
| EC34 | Danh mục | [Thêm] API: category_id là chuỗi chữ (vd "abc") | ✘ | type | FR-15.4, C9 | Chỉ tầng API (C9). |
| EC35 | Danh mục | [Sửa] category_id thuộc danh sách danh mục có sẵn (vd 2) | ✔ | set | FR-15.4, C11 | C11: danh sách = bảng categories lúc lưu (seed id 1–3). Các danh mục xử lý như nhau → 1 lớp. UI (ô chọn) + API. |
| EC36 | Danh mục | [Sửa] API: category_id không có trong danh sách (vd 999) | ✘ | set | FR-15.4, C11 | Chỉ tầng API — ô chọn trên UI chỉ có danh mục có sẵn (C11, gray-box). |
| EC37 | Danh mục | [Sửa] API: thiếu trường category_id hoặc category_id = null | ✘ | must-be | FR-15.4, C9 | Chỉ tầng API (C9). |
| EC38 | Danh mục | [Sửa] API: category_id là chuỗi chữ (vd "abc") | ✘ | type | FR-15.4, C9 | Chỉ tầng API (C9). |
| EC39 | Mô tả | Chuỗi mô tả bất kỳ (nominal, vd 'Mô tả {ts}') | ✔ | set |  | SRS im lặng – chấp nhận mọi cách hợp lý (C13). Không có lớp không hợp lệ → cảnh báo giữ nguyên. |
| EC40 | URL Ảnh | URL ảnh dạng http(s) (nominal, vd 'https://placehold.co/300') | ✔ | set |  | SRS im lặng – chấp nhận mọi cách hợp lý (C13). Không có lớp không hợp lệ → cảnh báo giữ nguyên. |
| EC41 | Sản phẩm mục tiêu (khi Xem chi tiết / Sửa / Xóa) | id sản phẩm tồn tại (sản phẩm do case tạo, C0) | ✔ | set | FR-15.1 | UI (dòng được bấm 'Sửa'/'Xóa') + API (:id). |
| EC42 | Sản phẩm mục tiêu (khi Xem chi tiết / Sửa / Xóa) | [Xem] API: GET /api/products/:id với id không tồn tại | ✘ | set | FR-15.1, C10 | Chỉ tầng API (C10). Tách theo thao tác: ba endpoint khác nhau (theo lý do của C8). |
| EC43 | Sản phẩm mục tiêu (khi Xem chi tiết / Sửa / Xóa) | [Sửa] API: PUT /api/products/:id với id không tồn tại | ✘ | set | FR-15.1, C10 | Chỉ tầng API (C10). Tách theo thao tác: ba endpoint khác nhau (theo lý do của C8). |
| EC44 | Sản phẩm mục tiêu (khi Xem chi tiết / Sửa / Xóa) | [Xóa] API: DELETE /api/products/:id với id không tồn tại | ✘ | set | FR-15.1, C10 | Chỉ tầng API (C10). Tách theo thao tác: ba endpoint khác nhau (theo lý do của C8). |
| EC45 | Danh tính người gọi / token | Token hợp lệ, role admin | ✔ | set | FR-12.2 | UI luôn chạy trong phiên admin. API: Authorization: Bearer <token admin>. |
| EC46 | Danh tính người gọi / token | [Thêm] API: POST không có header Authorization | ✘ | must-be | FR-12.2, SEC-02 | Chỉ tầng API (C5). |
| EC47 | Danh tính người gọi / token | [Thêm] API: POST với token không hợp lệ (chuỗi không phải JWT của hệ thống) | ✘ | must-be | FR-12.2, SEC-02 | Chỉ tầng API (C5). |
| EC48 | Danh tính người gọi / token | [Thêm] API: POST với token hợp lệ của role user (test@eshop.com) | ✘ | set | FR-12.2, SEC-03 | Chỉ tầng API (C5). Tách khỏi 'token không hợp lệ': token xác thực được nhưng sai role (SEC-03). |
| EC49 | Danh tính người gọi / token | [Sửa] API: PUT không có header Authorization | ✘ | must-be | FR-12.2, SEC-02 | Chỉ tầng API (C5). |
| EC50 | Danh tính người gọi / token | [Sửa] API: PUT với token không hợp lệ (chuỗi không phải JWT của hệ thống) | ✘ | must-be | FR-12.2, SEC-02 | Chỉ tầng API (C5). |
| EC51 | Danh tính người gọi / token | [Sửa] API: PUT với token hợp lệ của role user (test@eshop.com) | ✘ | set | FR-12.2, SEC-03 | Chỉ tầng API (C5). Tách khỏi 'token không hợp lệ': token xác thực được nhưng sai role (SEC-03). |
| EC52 | Danh tính người gọi / token | [Xóa] API: DELETE không có header Authorization | ✘ | must-be | FR-12.2, SEC-02 | Chỉ tầng API (C5). |
| EC53 | Danh tính người gọi / token | [Xóa] API: DELETE với token không hợp lệ (chuỗi không phải JWT của hệ thống) | ✘ | must-be | FR-12.2, SEC-02 | Chỉ tầng API (C5). |
| EC54 | Danh tính người gọi / token | [Xóa] API: DELETE với token hợp lệ của role user (test@eshop.com) | ✘ | set | FR-12.2, SEC-03 | Chỉ tầng API (C5). Tách khỏi 'token không hợp lệ': token xác thực được nhưng sai role (SEC-03). |
| EC55 | Các sản phẩm khác trong CSDL (trạng thái) | Có ≥ 1 sản phẩm khác ngoài sản phẩm mục tiêu (5 sản phẩm seed + sản phẩm của case) | ✔ | count | FR-15.5 | Trạng thái dữ liệu cần để quan sát FR-15.5. Không có lớp không hợp lệ (0 sản phẩm khác không phải đầu vào sai) → cảnh báo giữ nguyên. |
| EC56 | Bản ghi sản phẩm sau thao tác | Thêm hợp lệ: thêm đúng 1 bản ghi; name, price, category_id = giá trị gửi | ✔ | set | FR-15.1 | Quan sát GET /api/products trước/sau (C0). So price theo giá trị số; kiểu dữ liệu price chỉ khẳng định ở EC59 (C15). |
| EC57 | Bản ghi sản phẩm sau thao tác | Sửa hợp lệ: bản ghi mục tiêu có name, price, category_id = giá trị mới | ✔ | set | FR-15.1 | Quan sát GET /api/products/:id. So price theo giá trị số; kiểu dữ liệu price chỉ khẳng định ở EC59 (C15). |
| EC58 | Bản ghi sản phẩm sau thao tác | Xóa hợp lệ: bản ghi mục tiêu không còn trong GET /api/products | ✔ | set | FR-15.1 |  |
| EC59 | Bản ghi sản phẩm sau thao tác | Xem: GET /api/products/:id trả bản ghi có các trường = giá trị đã lưu; price là số JSON | ✔ | set | FR-15.1, C15 | C15 SV chốt (b): nơi duy nhất khẳng định kiểu dữ liệu price. |
| EC60 | Bản ghi sản phẩm sau thao tác | Tầng API bị từ chối: số bản ghi và bản ghi mục tiêu SAU = TRƯỚC | ✔ | set | C6 | C6; dùng chung cho từ chối do dữ liệu, id không tồn tại, không đủ quyền. |
| EC61 | Bản ghi sản phẩm sau thao tác | Tầng UI bị từ chối: số bản ghi và bản ghi mục tiêu SAU = TRƯỚC | ✔ | set | C7 | C7. Quan sát bằng GET /api/products (C0). |
| EC62 | Danh sách sản phẩm trên UI | Sau Thêm hợp lệ: bảng có thêm 1 dòng, 'Tên SP' và 'Giá' = giá trị nhập | ✔ | set | FR-15.1 | So giá trị số; định dạng ₫ kiểm riêng ở TS-GUI (C12). |
| EC63 | Danh sách sản phẩm trên UI | Sau Sửa hợp lệ: dòng mục tiêu hiển thị giá trị mới | ✔ | set | FR-15.1 |  |
| EC64 | Danh sách sản phẩm trên UI | Sau Xóa: dòng mục tiêu không còn trong bảng | ✔ | set | FR-15.1 |  |
| EC65 | Danh sách sản phẩm trên UI | Xem: tab 'Sản phẩm' hiển thị đủ các sản phẩm có trong GET /api/products | ✔ | set | FR-15.1 |  |
| EC66 | Danh sách sản phẩm trên UI | UI bị từ chối: bảng không đổi (SAU = TRƯỚC) | ✔ | set | C7 |  |
| EC67 | Các sản phẩm khác sau khi Sửa | Các sản phẩm khác giữ nguyên sau khi Sửa (SAU = TRƯỚC) | ✔ | must-be | FR-15.5 | Áp cả UI (bảng) và API (GET /api/products); mỗi tầng một case. |
| EC68 | Phản hồi API sản phẩm | API: 2xx khi thao tác hợp lệ | ✔ | set | API-PROD | Không khẳng định nội dung body (api_specification không quy định). |
| EC69 | Phản hồi API sản phẩm | API: 4xx kèm trường error khi dữ liệu vi phạm FR-15.2–15.4 hoặc sai kiểu/thiếu trường | ✔ | set | C6 | Không 2xx, không 5xx; không cố định mã (C6). |
| EC70 | Phản hồi API sản phẩm | API: 4xx khi id không tồn tại | ✔ | set | C10 | Không 2xx, không 5xx (C10). |
| EC71 | Phản hồi API sản phẩm | API: 4xx khi không đủ quyền (thiếu/sai token, role user) | ✔ | set | FR-12.2 | C5; không cố định mã. |
| EC72 | Phản hồi trên UI khi lưu / xóa | UI bị từ chối: có thông báo lỗi trên form (kể cả bong bóng kiểm tra HTML5) | ✔ | must-be | C7 | Nội dung chữ ghi làm Actual. Vị trí (FR-22.4) kiểm riêng ở TS-GUI (C12). |
| EC73 | Phản hồi trên UI khi lưu / xóa | UI thành công: không hiển thị thông báo lỗi | ✔ | set | FR-15.1 | (ngầm định) Nội dung thông báo thành công không khẳng định (C13). |

### Bước 3a — Test Cases Providing Coverage of Partitions
| EC | Lớp | Test case phủ |
|---|---|---|
| EC1 | Thêm | ⚠ chưa phủ |
| EC2 | Xem | ⚠ chưa phủ |
| EC3 | Sửa | ⚠ chưa phủ |
| EC4 | Xóa | ⚠ chưa phủ |
| EC5 | [Thêm] Độ dài 1–255 ký tự, có ít nhất 1 ký tự khác khoảng trắng (vd 'Tai nghe {ts}') | ⚠ chưa phủ |
| EC6 | [Thêm] Rỗng — 0 ký tự | ⚠ chưa phủ |
| EC7 | [Thêm] Dài hơn 255 ký tự | ⚠ chưa phủ |
| EC8 | [Thêm] Chỉ gồm khoảng trắng (vd '   ') | ⚠ chưa phủ |
| EC9 | [Thêm] API: thiếu trường name hoặc name = null | ⚠ chưa phủ |
| EC10 | [Thêm] API: name không phải chuỗi (vd số 123) | ⚠ chưa phủ |
| EC11 | [Sửa] Độ dài 1–255 ký tự, có ít nhất 1 ký tự khác khoảng trắng (vd 'Tai nghe {ts}') | ⚠ chưa phủ |
| EC12 | [Sửa] Rỗng — 0 ký tự | ⚠ chưa phủ |
| EC13 | [Sửa] Dài hơn 255 ký tự | ⚠ chưa phủ |
| EC14 | [Sửa] Chỉ gồm khoảng trắng (vd '   ') | ⚠ chưa phủ |
| EC15 | [Sửa] API: thiếu trường name hoặc name = null | ⚠ chưa phủ |
| EC16 | [Sửa] API: name không phải chuỗi (vd số 123) | ⚠ chưa phủ |
| EC17 | [Thêm] Số nguyên > 0 (vd 1500000) | ⚠ chưa phủ |
| EC18 | [Thêm] Số thập phân > 0, không nguyên (vd 0.5; 1500000.5) | ⚠ chưa phủ |
| EC19 | [Thêm] Số ≤ 0 (vd 0; -1000) | ⚠ chưa phủ |
| EC20 | [Thêm] UI: ô 'Giá tiền' để trống | ⚠ chưa phủ |
| EC21 | [Thêm] API: thiếu trường price hoặc price = null | ⚠ chưa phủ |
| EC22 | [Thêm] API: price là chuỗi chữ (vd "abc") | ⚠ chưa phủ |
| EC23 | [Thêm] API: price là chuỗi số (vd "100000") | ⚠ chưa phủ |
| EC24 | [Sửa] Số nguyên > 0 (vd 1500000) | ⚠ chưa phủ |
| EC25 | [Sửa] Số thập phân > 0, không nguyên (vd 0.5; 1500000.5) | ⚠ chưa phủ |
| EC26 | [Sửa] Số ≤ 0 (vd 0; -1000) | ⚠ chưa phủ |
| EC27 | [Sửa] UI: ô 'Giá tiền' để trống | ⚠ chưa phủ |
| EC28 | [Sửa] API: thiếu trường price hoặc price = null | ⚠ chưa phủ |
| EC29 | [Sửa] API: price là chuỗi chữ (vd "abc") | ⚠ chưa phủ |
| EC30 | [Sửa] API: price là chuỗi số (vd "100000") | ⚠ chưa phủ |
| EC31 | [Thêm] category_id thuộc danh sách danh mục có sẵn (vd 2) | ⚠ chưa phủ |
| EC32 | [Thêm] API: category_id không có trong danh sách (vd 999) | ⚠ chưa phủ |
| EC33 | [Thêm] API: thiếu trường category_id hoặc category_id = null | ⚠ chưa phủ |
| EC34 | [Thêm] API: category_id là chuỗi chữ (vd "abc") | ⚠ chưa phủ |
| EC35 | [Sửa] category_id thuộc danh sách danh mục có sẵn (vd 2) | ⚠ chưa phủ |
| EC36 | [Sửa] API: category_id không có trong danh sách (vd 999) | ⚠ chưa phủ |
| EC37 | [Sửa] API: thiếu trường category_id hoặc category_id = null | ⚠ chưa phủ |
| EC38 | [Sửa] API: category_id là chuỗi chữ (vd "abc") | ⚠ chưa phủ |
| EC39 | Chuỗi mô tả bất kỳ (nominal, vd 'Mô tả {ts}') | ⚠ chưa phủ |
| EC40 | URL ảnh dạng http(s) (nominal, vd 'https://placehold.co/300') | ⚠ chưa phủ |
| EC41 | id sản phẩm tồn tại (sản phẩm do case tạo, C0) | ⚠ chưa phủ |
| EC42 | [Xem] API: GET /api/products/:id với id không tồn tại | ⚠ chưa phủ |
| EC43 | [Sửa] API: PUT /api/products/:id với id không tồn tại | ⚠ chưa phủ |
| EC44 | [Xóa] API: DELETE /api/products/:id với id không tồn tại | ⚠ chưa phủ |
| EC45 | Token hợp lệ, role admin | ⚠ chưa phủ |
| EC46 | [Thêm] API: POST không có header Authorization | ⚠ chưa phủ |
| EC47 | [Thêm] API: POST với token không hợp lệ (chuỗi không phải JWT của hệ thống) | ⚠ chưa phủ |
| EC48 | [Thêm] API: POST với token hợp lệ của role user (test@eshop.com) | ⚠ chưa phủ |
| EC49 | [Sửa] API: PUT không có header Authorization | ⚠ chưa phủ |
| EC50 | [Sửa] API: PUT với token không hợp lệ (chuỗi không phải JWT của hệ thống) | ⚠ chưa phủ |
| EC51 | [Sửa] API: PUT với token hợp lệ của role user (test@eshop.com) | ⚠ chưa phủ |
| EC52 | [Xóa] API: DELETE không có header Authorization | ⚠ chưa phủ |
| EC53 | [Xóa] API: DELETE với token không hợp lệ (chuỗi không phải JWT của hệ thống) | ⚠ chưa phủ |
| EC54 | [Xóa] API: DELETE với token hợp lệ của role user (test@eshop.com) | ⚠ chưa phủ |
| EC55 | Có ≥ 1 sản phẩm khác ngoài sản phẩm mục tiêu (5 sản phẩm seed + sản phẩm của case) | ⚠ chưa phủ |
| EC56 | Thêm hợp lệ: thêm đúng 1 bản ghi; name, price, category_id = giá trị gửi | ⚠ chưa phủ |
| EC57 | Sửa hợp lệ: bản ghi mục tiêu có name, price, category_id = giá trị mới | ⚠ chưa phủ |
| EC58 | Xóa hợp lệ: bản ghi mục tiêu không còn trong GET /api/products | ⚠ chưa phủ |
| EC59 | Xem: GET /api/products/:id trả bản ghi có các trường = giá trị đã lưu; price là số JSON | ⚠ chưa phủ |
| EC60 | Tầng API bị từ chối: số bản ghi và bản ghi mục tiêu SAU = TRƯỚC | ⚠ chưa phủ |
| EC61 | Tầng UI bị từ chối: số bản ghi và bản ghi mục tiêu SAU = TRƯỚC | ⚠ chưa phủ |
| EC62 | Sau Thêm hợp lệ: bảng có thêm 1 dòng, 'Tên SP' và 'Giá' = giá trị nhập | ⚠ chưa phủ |
| EC63 | Sau Sửa hợp lệ: dòng mục tiêu hiển thị giá trị mới | ⚠ chưa phủ |
| EC64 | Sau Xóa: dòng mục tiêu không còn trong bảng | ⚠ chưa phủ |
| EC65 | Xem: tab 'Sản phẩm' hiển thị đủ các sản phẩm có trong GET /api/products | ⚠ chưa phủ |
| EC66 | UI bị từ chối: bảng không đổi (SAU = TRƯỚC) | ⚠ chưa phủ |
| EC67 | Các sản phẩm khác giữ nguyên sau khi Sửa (SAU = TRƯỚC) | ⚠ chưa phủ |
| EC68 | API: 2xx khi thao tác hợp lệ | ⚠ chưa phủ |
| EC69 | API: 4xx kèm trường error khi dữ liệu vi phạm FR-15.2–15.4 hoặc sai kiểu/thiếu trường | ⚠ chưa phủ |
| EC70 | API: 4xx khi id không tồn tại | ⚠ chưa phủ |
| EC71 | API: 4xx khi không đủ quyền (thiếu/sai token, role user) | ⚠ chưa phủ |
| EC72 | UI bị từ chối: có thông báo lỗi trên form (kể cả bong bóng kiểm tra HTML5) | ⚠ chưa phủ |
| EC73 | UI thành công: không hiển thị thông báo lỗi | ⚠ chưa phủ |

### Truy vết yêu cầu ↔ test case
Sinh tự động: yêu cầu của một TC = hợp các yêu cầu của các EC mục tiêu (ec_target; TC không có ec_target thì dùng EC phủ) theo cột Yêu cầu ở bảng Bước 2, cộng với trường requirements và assumptions của TC (dùng cho case GUI không gắn EC). Mã giả định (B…) hiện thành dòng riêng.

| Yêu cầu | Test case | Số TC |
|---|---|---|
| FR-15.1 | ⚠ | 0 |
| FR-15.2 | ⚠ | 0 |
| FR-15.3 | ⚠ | 0 |
| FR-15.4 | ⚠ | 0 |
| FR-15.5 | ⚠ | 0 |
| FR-12.2 | ⚠ | 0 |
| API-PROD | ⚠ | 0 |
| SEC-02 | ⚠ | 0 |
| SEC-03 | ⚠ | 0 |
| FR-21.3 | ⚠ | 0 |
| FR-22.1 | ⚠ | 0 |
| FR-22.4 | ⚠ | 0 |
| FR-24.4 | ⚠ | 0 |
| SEC-04 | ⚠ | 0 |

### Giả định khi đặc tả chưa nói rõ
- C0 (độc lập và điểm quan sát) [loại: quy trình · truy vết: không · căn cứ: CLAUDE.md (backend khởi động lại → CSDL seed lại), tiền lệ A19/B0b · SV chốt 2026-10-20, chấp nhận đề xuất AI]: mỗi case tạo sản phẩm riêng có tên chứa {ts}; Sửa/Xóa chỉ thao tác trên sản phẩm do case tạo; oracle tương đối (danh sách/bản ghi SAU so với TRƯỚC trong chính case). Điểm quan sát dữ liệu: GET /api/products và GET /api/products/:id (api_specification dòng 80–85, không yêu cầu token). Cleanup lớp 2: DELETE /api/products/:id bằng token admin cuối suite; khởi động lại backend seed lại toàn bộ.
- C1 (Giá – số thực dương) [loại: quyết định Expected · truy vết: có · căn cứ: FR-15.3 'phải là số dương (> 0)' · SV chốt 2026-10-20, phương án a]: mọi số thực > 0 hợp lệ, kể cả số thập phân (vd 0.5) — lý do SV: FR-15 chỉ quy định > 0. Bước nhảy 0.1 do SV chọn → LB = 0.1 (LB−1 = 0, LB+1 = 0.2). Ghi chú SV: thực tế giá thường ≥ 1000 đồng — chỉ dùng để chọn đại diện hợp lệ điển hình, KHÔNG phải cận dưới, KHÔNG quyết định Expected.
- C2 (Giá – cận trên) [loại: quyết định Expected · truy vết: có · căn cứ: SRS im lặng (FR-15.3 chỉ có > 0) · SV chốt 2026-10-20, phương án a theo khuyến nghị]: không có cận trên → biến V3 khai no_upper_bound = C2; BVA phía trên dùng 1 điểm LARGE hợp lệ (như B1).
- C3 (Tên – chuỗi chỉ gồm khoảng trắng) [loại: quyết định Expected · truy vết: có · căn cứ: FR-15.2 'bắt buộc', SRS im lặng về khoảng trắng; tiền lệ A1 · SV chốt 2026-10-20, phương án a theo khuyến nghị]: chuỗi chỉ gồm khoảng trắng coi như trống → bị từ chối; tách lớp riêng với chuỗi rỗng.
- C4 (Tên – đơn vị đếm 255 ký tự) [loại: chọn đại diện · truy vết: không · căn cứ: FR-15.2 'tối đa 255 ký tự', không nói đơn vị · SV chốt 2026-10-20, chấp nhận đề xuất AI]: 1 ký tự = 1 Unicode code point (dạng NFC). Điểm biên độ dài dùng chuỗi ASCII không có khoảng trắng đầu/cuối để tránh phụ thuộc cách đếm/cắt; 1 đại diện NOM có chữ tiếng Việt có dấu.
- C5 (phạm vi FR-12 – quyền) [loại: phạm vi · truy vết: không · căn cứ: FR-12.2 nêu đích danh POST/PUT/DELETE /api/products; SEC-02, SEC-03 · SV chốt 2026-10-20, phương án a theo khuyến nghị; không mở rộng sang cổng 'Admin Login']: tầng API, biến V8 (không token / token sai / token role user / token admin) cho 3 endpoint ghi; không đủ quyền → 4xx, dữ liệu không đổi (theo C6). FR-12.1 (cổng đăng nhập UI) ngoài phạm vi — đã bỏ biến ra V15 và dòng yêu cầu FR-12.1.
- C6 (tầng API áp FR-15) [loại: quyết định Expected · truy vết: có · căn cứ: FR-15 là yêu cầu hệ thống; tiền lệ A9, A11, B7, B17 · SV chốt 2026-10-20, phương án a theo khuyến nghị]: API là tầng riêng, suite riêng: POST/PUT gọi trực tiếp với dữ liệu vi phạm FR-15.2–15.4 → 4xx (không 2xx, không 5xx) kèm trường error, không tạo/không đổi bản ghi; không cố định mã cụ thể.
- C7 (oracle khi UI từ chối) [loại: quyết định Expected · truy vết: có · căn cứ: FR-22.4 'Thông báo lỗi phải xuất hiện trên nút submit' (README.md dòng 255) — quy định vị trí, ngụ ý form có thông báo lỗi; tiền lệ A10/A16 · SV chốt 2026-10-20, phương án a theo khuyến nghị]: dữ liệu không đổi (GET trước/sau) + có thông báo lỗi trên form (bong bóng kiểm tra HTML5 được tính như A16); nội dung chữ chỉ ghi làm Actual. Vị trí thông báo kiểm riêng ở TS-GUI (C12).
- C8 (ràng buộc khi Sửa) [loại: quyết định Expected · truy vết: có · căn cứ: FR-15 đặt 'Ràng buộc đầu vào' chung cho Thêm/Sửa · SV chốt 2026-10-20, phương án a]: FR-15.2–15.4 áp cho cả Thêm và Sửa; tách lớp theo thao tác — lý do SV: Thêm và Sửa là hai thao tác khác nhau, không gộp lớp. Mỗi lớp của Tên/Giá/Danh mục có bản Thêm và bản Sửa.
- C9 (thiếu trường / sai kiểu ở API) [loại: quyết định Expected · truy vết: có · căn cứ: SRS im lặng về body JSON; tiền lệ A15, B18 · SV chốt 2026-10-20, phương án a — SV chốt: phân biệt rạch ròi giữa số và chuỗi]: name/price/category_id thiếu, null hoặc sai kiểu JSON (name là số; price là chuỗi — kể cả chuỗi số như "100000"; category_id là chuỗi chữ) → 4xx, không tạo/không đổi bản ghi.
- C10 (id không tồn tại khi Xem/Sửa/Xóa) [loại: quyết định Expected · truy vết: có · căn cứ: SRS im lặng; api_specification không mô tả lỗi; tiền lệ A11 · SV chốt 2026-10-20, chấp nhận đề xuất AI]: GET/PUT/DELETE /api/products/:id với id không có trong CSDL → 4xx (không 2xx, không 5xx), không tạo bản ghi mới, các sản phẩm khác không đổi. Chỉ tạo được ở tầng API (UI chỉ chọn được sản phẩm đang hiển thị).
- C11 (Danh mục – 'danh sách có sẵn') [loại: quyết định Expected · truy vết: có · căn cứ: FR-15.4 'phải chọn từ danh sách có sẵn' · SV chốt 2026-10-20, chấp nhận đề xuất AI]: danh sách có sẵn = các danh mục tồn tại trong bảng categories (GET /api/categories) tại thời điểm lưu. category_id không có trong danh sách hoặc thiếu → không hợp lệ. Quan sát (gray-box): ô chọn danh mục trên UI luôn có giá trị, mặc định category_id 1 (App.jsx dòng 101, 528–543) → lớp 'không chọn'/'ngoài danh sách' chỉ tạo được qua API.
- C12 (GUI liên quan) [loại: phạm vi · truy vết: không · căn cứ: tiền lệ A14, B16 (SV chốt) · SV chốt 2026-10-20, chấp nhận đề xuất AI]: thuộc tính tĩnh/hiển thị của form và bảng sản phẩm — FR-22.1 ('*' cạnh nhãn Tên, Giá, Danh mục), FR-22.4 (thông báo lỗi trên nút 'Lưu sản phẩm'), FR-21.3 (cột 'Giá' dùng ₫ + phân cách hàng nghìn), FR-24.4 (alt ảnh trong cột 'Ảnh'), SEC-04 (tên sản phẩm hiển thị an toàn) — kiểm bằng suite TS-GUI riêng, mỗi thuộc tính khẳng định ở đúng 1 case, không phân lớp. Quan sát: form chỉ có placeholder, không có phần tử nhãn (App.jsx dòng 491–543) — xử lý ở bước 3 theo A17.
- C13 (ngoài phạm vi / SRS im lặng) [loại: phạm vi · truy vết: không · căn cứ: SRS · SV chốt 2026-10-20, chấp nhận đề xuất AI]: ngoài phạm vi — FR-16 (import CSV), FR-14 (Category CRUD, chỉ dùng 3 danh mục seed làm dữ liệu), FR-13, hiển thị sản phẩm trên frontend-web/mobile (FR-05, FR-06, FR-20). SRS im lặng – chấp nhận mọi cách hợp lý, không đặt Expected: tên trùng với sản phẩm khác; Mô tả và URL Ảnh (giữ giá trị nominal hợp lệ); hộp xác nhận trước khi Xóa sản phẩm (FR-24.2 chỉ nói giỏ hàng); nội dung thông báo khi lưu/xóa thành công; nút 'Hủy sửa'.
- C14 (quy tắc verdict) [loại: quy trình · truy vết: không · căn cứ: quy ước đã chốt từ A_FR01/B_FR07 (A17, A20) · SV chốt 2026-10-20, chấp nhận đề xuất AI]: lệch Expected do biến mục tiêu → Fail; bị chặn bởi lỗi đã có ở case khác → Blocked, ghi case gốc; trường SRS yêu cầu mà UI không có → case kiểm sự tồn tại Fail, case phụ thuộc Blocked; từ chối đúng nhưng lý do không chứng minh luật mục tiêu → 'Pass hộp đen' ghi trong notes.
- C15 (kiểu dữ liệu price trong phản hồi GET) [loại: quyết định Expected · truy vết: có · căn cứ: SRS im lặng về response; giả định SV · SV chốt 2026-10-20, phương án b — SV chốt: price trong response phải là số JSON; lý do giống C9 — phân biệt rạch ròi giữa chuỗi và số, không chấp nhận ngoại lệ]: price trong phản hồi GET /api/products/:id phải là số JSON; price dạng chuỗi (kể cả chuỗi số) lệch Expected. Kiểu dữ liệu price chỉ khẳng định ở EC59; EC56/EC57 so price theo giá trị số.

**Tổng:** chưa có test case (bước 3–4).
