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
| EC | Biến | Lớp tương đương | Hợp lệ | Hướng dẫn | Ghi chú |
|---|---|---|---|---|---|

### Bước 3a — Test Cases Providing Coverage of Partitions
| EC | Lớp | Test case phủ |
|---|---|---|

### Truy vết yêu cầu ↔ test case
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
- C9 (thiếu trường / sai kiểu ở API) [loại: quyết định Expected · truy vết: có · căn cứ: SRS im lặng về body JSON; tiền lệ A15, B18 · SV chốt 2026-10-20, phương án a theo khuyến nghị]: name/price/category_id thiếu, null hoặc sai kiểu JSON (name là số; price là chuỗi — kể cả chuỗi số như "100000"; category_id là chuỗi chữ) → 4xx, không tạo/không đổi bản ghi.
- C10 (id không tồn tại khi Xem/Sửa/Xóa) [loại: quyết định Expected · truy vết: có · căn cứ: SRS im lặng; api_specification không mô tả lỗi; tiền lệ A11 · SV chốt 2026-10-20, chấp nhận đề xuất AI]: GET/PUT/DELETE /api/products/:id với id không có trong CSDL → 4xx (không 2xx, không 5xx), không tạo bản ghi mới, các sản phẩm khác không đổi. Chỉ tạo được ở tầng API (UI chỉ chọn được sản phẩm đang hiển thị).
- C11 (Danh mục – 'danh sách có sẵn') [loại: quyết định Expected · truy vết: có · căn cứ: FR-15.4 'phải chọn từ danh sách có sẵn' · SV chốt 2026-10-20, chấp nhận đề xuất AI]: danh sách có sẵn = các danh mục tồn tại trong bảng categories (GET /api/categories) tại thời điểm lưu. category_id không có trong danh sách hoặc thiếu → không hợp lệ. Quan sát (gray-box): ô chọn danh mục trên UI luôn có giá trị, mặc định category_id 1 (App.jsx dòng 101, 528–543) → lớp 'không chọn'/'ngoài danh sách' chỉ tạo được qua API.
- C12 (GUI liên quan) [loại: phạm vi · truy vết: không · căn cứ: tiền lệ A14, B16 (SV chốt) · SV chốt 2026-10-20, chấp nhận đề xuất AI]: thuộc tính tĩnh/hiển thị của form và bảng sản phẩm — FR-22.1 ('*' cạnh nhãn Tên, Giá, Danh mục), FR-22.4 (thông báo lỗi trên nút 'Lưu sản phẩm'), FR-21.3 (cột 'Giá' dùng ₫ + phân cách hàng nghìn), FR-24.4 (alt ảnh trong cột 'Ảnh'), SEC-04 (tên sản phẩm hiển thị an toàn) — kiểm bằng suite TS-GUI riêng, mỗi thuộc tính khẳng định ở đúng 1 case, không phân lớp. Quan sát: form chỉ có placeholder, không có phần tử nhãn (App.jsx dòng 491–543) — xử lý ở bước 3 theo A17.
- C13 (ngoài phạm vi / SRS im lặng) [loại: phạm vi · truy vết: không · căn cứ: SRS · SV chốt 2026-10-20, chấp nhận đề xuất AI]: ngoài phạm vi — FR-16 (import CSV), FR-14 (Category CRUD, chỉ dùng 3 danh mục seed làm dữ liệu), FR-13, hiển thị sản phẩm trên frontend-web/mobile (FR-05, FR-06, FR-20). SRS im lặng – chấp nhận mọi cách hợp lý, không đặt Expected: tên trùng với sản phẩm khác; Mô tả và URL Ảnh (giữ giá trị nominal hợp lệ); hộp xác nhận trước khi Xóa sản phẩm (FR-24.2 chỉ nói giỏ hàng); nội dung thông báo khi lưu/xóa thành công; nút 'Hủy sửa'.
- C14 (quy tắc verdict) [loại: quy trình · truy vết: không · căn cứ: quy ước đã chốt từ A_FR01/B_FR07 (A17, A20) · SV chốt 2026-10-20, chấp nhận đề xuất AI]: lệch Expected do biến mục tiêu → Fail; bị chặn bởi lỗi đã có ở case khác → Blocked, ghi case gốc; trường SRS yêu cầu mà UI không có → case kiểm sự tồn tại Fail, case phụ thuộc Blocked; từ chối đúng nhưng lý do không chứng minh luật mục tiêu → 'Pass hộp đen' ghi trong notes.

**Tổng:** chưa có test case (bước 3–4).
