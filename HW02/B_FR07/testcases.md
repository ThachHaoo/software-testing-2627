### Phạm vi
DỰ THẢO — chờ SV chốt (B6, B7, B16). Đề xuất: trang 'Giỏ Hàng' (/cart) và các điểm thêm vào giỏ trên frontend-web (tầng UI), endpoint GET/POST /api/cart (tầng API). Trong phạm vi đề xuất: FR-07 (phân lớp + BVA); ô 'Số lượng' và nút thêm của FR-06 vì là nguồn dữ liệu vào giỏ; thuộc tính GUI liên quan giỏ (FR-21 ₫, FR-23 badge/breadcrumb, FR-24) kiểm bằng suite GUI riêng, không phân lớp. Ngoài phạm vi đề xuất: thanh toán (FR-08, chỉ dùng FR-08 để suy ra khách chưa đăng nhập vẫn có giỏ), mã giảm giá (FR-09), giỏ hàng trên Mobile (FR-20).

### Yêu cầu (test basis)
| Mã | Nội dung |
|---|---|
| FR-07.1 | Giỏ hàng hiển thị danh sách sản phẩm với các cột: Sản phẩm, Đơn giá, Số lượng, Thành tiền, Thao tác. |
| FR-07.2 | Cột Số lượng có nút +/- để chỉnh số lượng. |
| FR-07.3 | Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới. |
| FR-07.4 | Nút Xóa sản phẩm phải có dialog xác nhận trước khi thực hiện. |
| FR-07.5 | Có nút Tiếp tục mua sắm để quay về trang chủ. |
| FR-07.6 | Tổng tiền hiển thị nhãn chính xác "Tổng cộng" (không phải "Tổng tạm tính"). |
| FR-07.7 | Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng. |
| FR-06.2 | (liên quan, B6) Trang chi tiết có ô nhập Số lượng, chỉ nhận số nguyên dương, tối thiểu là 1. |
| FR-06.3 | (liên quan, B6) Nút Thêm vào giỏ hàng — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật). |
| FR-08.1 | (liên quan) Chỉ người dùng đã đăng nhập mới tiến hành thanh toán được — dùng để suy ra B11. |
| FR-21.3 | (GUI, B16) Luôn dùng ký hiệu ₫ với định dạng phân cách hàng nghìn. |
| FR-23.2 | (GUI, B16) Link "Giỏ hàng" phải hiển thị badge số lượng sản phẩm trong giỏ. |
| FR-23.4 | (GUI, B16) Breadcrumb bắt buộc có ở trang con Giỏ hàng. |
| FR-24.1 | (GUI, B16) Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge). |
| FR-24.2 | Khi xóa item khỏi giỏ phải có dialog xác nhận (trùng FR-07.4). |
| FR-24.3 | Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện (bổ sung FR-07.7). |
| FR-24.4 | (GUI, B16) Tất cả ảnh sản phẩm phải có thuộc tính alt mô tả nội dung (không rỗng). |
| API-CART | GET /api/cart lấy giỏ; POST /api/cart body JSON {id, name, price, quantity}; yêu cầu header Authorization: Bearer <token> (api_specification.md dòng 110–127). Không có endpoint sửa/xoá dòng giỏ. |
| SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ (README.md dòng 279). |
| SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng innerHTML trực tiếp (README.md dòng 281) — áp cho tên sản phẩm hiển thị trong giỏ. |

### Bước 1 — Biến vào/ra
| Mã | Biến | Vào/Ra | Nguồn | Kiểu | Ràng buộc (đặc tả) | Ghi chú |
|---|---|---|---|---|---|---|
| V1 | Số lượng khi thêm | Vào | UI: ô nhãn 'Số lượng:' (ProductDetail.jsx dòng 54–61, input type="number", không có min/max/required); nút 'Thêm vào giỏ' ở Trang chủ luôn thêm 1 (Home.jsx dòng 97–102) · API: body.quantity (api_specification.md dòng 125) | integer | Nguyên dương, tối thiểu 1 (FR-06.2). Cận trên: SRS im lặng → B1. Cách từ chối giá trị sai → B2. | Ô nhập trên UI nhận chuỗi; giá trị rỗng, thập phân, âm, ký tự e/E/+/- là chuỗi gõ được vào input number. |
| V2 | Sản phẩm được thêm (so với nội dung giỏ hiện có) | Vào | UI: nút 'Thêm vào giỏ hàng' (ProductDetail.jsx dòng 64–69) và 'Thêm vào giỏ' (Home.jsx dòng 97–102) · API: body.id (api_specification.md dòng 122) | enum | Chưa có trong giỏ → tạo dòng mới; đã có (cùng sản phẩm, B5) → tăng Số lượng, không tạo dòng mới (FR-07.3). API: id phải là sản phẩm tồn tại → B18. |  |
| V3 | Đơn giá sản phẩm | Vào | Dữ liệu: products.price INTEGER (database.js dòng 64–71); seed 4.000.000–45.000.000 (dòng 98–102) · API: body.price do client gửi (api_specification.md dòng 124) | integer (₫) | Không do người dùng nhập ở UI. Dùng tính Thành tiền/Tổng cộng (B4). Giá do client gửi ở API → B8. | Quan sát code: GET /api/products/:id trả price dạng chuỗi khi id chẵn (server.js dòng 162). Chỉ ghi nhận, chưa kết luận; xác nhận ở bước 6. |
| V4 | Thao tác chỉnh Số lượng trong giỏ | Vào | UI: nút '+' / '-' trong cột Số lượng theo FR-07.2 (SRS) · API: không có endpoint sửa (API-CART) | enum {+, -} | '+' tăng 1, '-' giảm 1 (FR-07.2, bước nhảy 1 theo thông lệ). '-' tại Số lượng = 1 → B3; '+' tại cận trên → B1. | Quan sát code: Cart.jsx dòng 47 hiển thị Số lượng dạng chữ, chưa thấy nút +/-. Chưa kết luận lỗi, xác nhận khi thực thi (bước 6); xử lý như A17 nếu thiếu. |
| V5 | Số lượng hiện tại của dòng (trước thao tác +/- hoặc thêm trùng) | Vào | Trạng thái giỏ trước thao tác (cột 'Số lượng', Cart.jsx dòng 47 · GET /api/cart) | integer | ≥ 1 (FR-06.2). Điểm đặc biệt: = 1 (biên cho '-'), = cận trên (biên cho '+', B1). |  |
| V6 | Thao tác xoá dòng và lựa chọn trong dialog | Vào | UI: nút xoá ở cột 'Thao tác' (Cart.jsx dòng 50–55, nhãn 'Xóa'); dialog xác nhận theo FR-07.4/FR-24.2 | enum {Xác nhận, Hủy} | Phải có dialog trước khi xoá (FR-07.4). Hủy → giữ nguyên; Xác nhận → xoá dòng (B14). | Quan sát code: onClick gọi removeFromCart(index) trực tiếp (Cart.jsx dòng 51). Chưa kết luận lỗi, xác nhận ở bước 6. |
| V7 | Số dòng trong giỏ (trạng thái) | Vào | Trạng thái giỏ trước thao tác (bảng Cart.jsx dòng 43–58; nhánh cart.length === 0 dòng 20–27 · GET /api/cart) | integer | 0 → hiển thị empty state (FR-07.7); ≥ 1 → hiển thị bảng. Không có cận trên trong SRS. |  |
| V8 | Trạng thái đăng nhập / token | Vào | UI: có/không đăng nhập (AuthContext.jsx, token trong localStorage) · API: header Authorization: Bearer <token> (api_specification.md dòng 112; server.js dòng 100–110) | enum | UI: khách chưa đăng nhập vẫn dùng giỏ (suy từ FR-08.1, B11). API: thiếu/sai token → từ chối (SEC-02, B17). |  |
| V9 | Tên sản phẩm trong body (API) | Vào | API: body.name (api_specification.md dòng 123) | string | SRS im lặng; client tự gửi tên → B8. Khi hiển thị phải escape (SEC-04). |  |
| V10 | Thao tác 'Tiếp tục mua sắm' | Vào | UI: nút/link 'Tiếp tục mua sắm' (FR-07.5) — code có link '← Mua tiếp' (Cart.jsx dòng 66–68) và 'Tiếp tục mua sắm' ở trạng thái trống (dòng 24) | enum {bấm} | Bấm → quay về trang chủ (FR-07.5). Nhãn chính xác → B12. |  |
| V11 | Danh sách dòng trong giỏ | Ra | UI: bảng trang /cart (Cart.jsx dòng 32–60) · API: mảng JSON từ GET /api/cart (server.js dòng 284–288) | list | Đủ 5 cột Sản phẩm, Đơn giá, Số lượng, Thành tiền, Thao tác (FR-07.1); số dòng = số sản phẩm khác nhau (FR-07.3). |  |
| V12 | Số lượng của dòng sau thao tác | Ra | UI: cột 'Số lượng' · API: phần tử .quantity trong GET /api/cart | integer | Thêm trùng → cộng dồn (FR-07.3); '+'/'-' → ±1 (FR-07.2); luôn ≥ 1 (FR-06.2, B3). |  |
| V13 | Thành tiền của dòng | Ra | UI: cột 'Thành tiền' (Cart.jsx dòng 48) | integer (₫) | = Đơn giá × Số lượng (B4); hiển thị ₫ + phân cách hàng nghìn (FR-21.3, B13). |  |
| V14 | Tổng cộng | Ra | UI: dòng tổng dưới bảng (Cart.jsx dòng 62–64) | integer (₫) | Nhãn đúng 'Tổng cộng' (FR-07.6); giá trị = Σ Thành tiền (B4); định dạng ₫ (FR-21.3). |  |
| V15 | Badge số lượng trên link 'Giỏ hàng' | Ra | UI: navbar, link 'Giỏ hàng' (App.jsx dòng 23) | integer | Hiển thị badge số lượng sản phẩm trong giỏ (FR-23.2); nghĩa 'số lượng' → B9. |  |
| V16 | Phản hồi trực quan sau khi thêm | Ra | UI: toast hoặc badge cập nhật; code đổi chữ nút thành 'Đã thêm' trong 2 giây (ProductDetail.jsx dòng 28–30, 68) | enum | Có phản hồi trực quan (toast/badge) sau mỗi lần thêm (FR-06.3, FR-24.1). |  |
| V17 | Dialog xác nhận xoá | Ra | UI: dialog sau khi bấm nút xoá | enum {hiện, không hiện} | Phải hiện trước khi xoá (FR-07.4, FR-24.2); kết quả theo lựa chọn ở V6 (B14). |  |
| V18 | Trạng thái giỏ trống (empty state) | Ra | UI: nhánh giỏ trống (Cart.jsx dòng 20–27) | enum | Có hình minh hoạ/icon và thông báo rõ ràng (FR-07.7, FR-24.3, B15). |  |
| V19 | Trang đích sau 'Tiếp tục mua sắm' | Ra | UI: URL trình duyệt | string | URL = trang chủ '/' (FR-07.5). |  |
| V20 | Phản hồi API giỏ hàng | Ra | API: mã HTTP + body của POST /api/cart (thành công: {"message": "Added to cart"}, server.js dòng 294) và GET /api/cart | HTTP | Dữ liệu hợp lệ → 2xx và GET phản ánh thay đổi; dữ liệu/token không hợp lệ → 4xx, giỏ không đổi (B7, B17, B18). |  |
| V21 | Thông báo lỗi khi Số lượng không hợp lệ | Ra | UI: trang chi tiết sản phẩm (chưa thấy phần tử thông báo trong ProductDetail.jsx) | enum | SRS không quy định nội dung → B2; oracle chính là giỏ không đổi. |  |

### Bước 2 — Complete Set of Partitions
| EC | Biến | Lớp tương đương | Hợp lệ | Hướng dẫn | Ghi chú |
|---|---|---|---|---|---|

### Bước 3a — Test Cases Providing Coverage of Partitions
| EC | Lớp | Test case phủ |
|---|---|---|

### Truy vết yêu cầu ↔ test case
| Yêu cầu | Test case | Số TC |
|---|---|---|
| FR-07.1 | ⚠ | 0 |
| FR-07.2 | ⚠ | 0 |
| FR-07.3 | ⚠ | 0 |
| FR-07.4 | ⚠ | 0 |
| FR-07.5 | ⚠ | 0 |
| FR-07.6 | ⚠ | 0 |
| FR-07.7 | ⚠ | 0 |
| FR-06.2 | ⚠ | 0 |
| FR-06.3 | ⚠ | 0 |
| FR-08.1 | ⚠ | 0 |
| FR-21.3 | ⚠ | 0 |
| FR-23.2 | ⚠ | 0 |
| FR-23.4 | ⚠ | 0 |
| FR-24.1 | ⚠ | 0 |
| FR-24.2 | ⚠ | 0 |
| FR-24.3 | ⚠ | 0 |
| FR-24.4 | ⚠ | 0 |
| API-CART | ⚠ | 0 |
| SEC-02 | ⚠ | 0 |
| SEC-04 | ⚠ | 0 |

### Giả định khi đặc tả chưa nói rõ
- B0a (độc lập, đã chốt từ phiên thảo luận): mỗi case dùng user riêng tạo qua POST /api/register với email chứa {ts}, đăng nhập lấy token riêng → userCarts[userId] riêng (server.js dòng 14, 291–293). Case UI chạy trong browser context mới (giỏ web là state React, rỗng khi mở trang).
- B0b (oracle tương đối, đã chốt): oracle so giỏ trước/sau trong chính case (số dòng, số lượng, Thành tiền, Tổng cộng) — không giả định giỏ rỗng tuyệt đối ngoài tiền điều kiện của case.
- B0c (cleanup 2 lớp, như A19): lớp 1 — dữ liệu riêng {ts} + oracle tương đối nên case không phụ thuộc cleanup; lớp 2 — cuối suite xoá user test bằng DELETE /api/admin/users/:id (token admin); khởi động lại backend xoá toàn bộ userCarts và seed lại CSDL.
- B0d (quan sát, không phải yêu cầu): giỏ web nằm trong state React, không gọi /api/cart và không lưu localStorage (CartContext.jsx dòng 6; grep 'api/cart' trong frontend-web không có kết quả) → tải lại trang/page.goto làm mất giỏ. Script UI phải điều hướng bằng link trong app sau khi đã thêm hàng.
- B1 (cận trên Số lượng) (AI đề xuất, chờ SV chốt): SRS không nêu. Nguồn gợi ý — SRS: FR-06 chỉ có 'tối thiểu là 1'; code: input type=number không có min/max (ProductDetail.jsx dòng 56–61), bảng products không có cột tồn kho (database.js dòng 64–71); thông lệ: giới hạn theo tồn kho hoặc một hằng số (vd 99). Lựa chọn: (a) không có cận trên — BVA chỉ quanh LB=1, MAX_UI là giá trị lớn nhất gõ được; (b) SV đặt hằng số UB.
- B2 (Số lượng không hợp lệ khi thêm) (AI đề xuất, chờ SV chốt): FR-06 nói 'chỉ nhận số nguyên dương, tối thiểu là 1' nhưng không nói cách từ chối. Nguồn gợi ý — thông lệ: không thêm vào giỏ + có thông báo, hoặc chặn nhập. Đề xuất oracle: giỏ trước/sau không đổi (số dòng và số lượng); nội dung thông báo chỉ ghi làm Actual.
- B3 (nút '-' khi Số lượng = 1) (AI đề xuất, chờ SV chốt): SRS im lặng. Nguồn gợi ý — FR-06 'tối thiểu là 1'; thông lệ: (a) giữ 1 / nút bị vô hiệu, (b) xoá dòng (khi đó có cần dialog FR-07.4 không?).
- B4 (Thành tiền và Tổng cộng) (AI đề xuất, chờ SV chốt): SRS không ghi công thức. Nguồn gợi ý — thông lệ: Thành tiền = Đơn giá × Số lượng; Tổng cộng = Σ Thành tiền các dòng; FR-08 'tổng tiền tính tự động từ giỏ hàng'.
- B5 ('cùng một sản phẩm') (AI đề xuất, chờ SV chốt): SRS không định nghĩa. Nguồn gợi ý — code/API: sản phẩm định danh bằng id (body.id, products.id). Đề xuất: cùng id = cùng sản phẩm, kể cả thêm từ hai nơi khác nhau (Trang chủ 'Thêm vào giỏ' và trang chi tiết 'Thêm vào giỏ hàng').
- B6 (phạm vi FR-06) (AI đề xuất, chờ SV chốt): ô 'Số lượng' và nút thêm thuộc FR-06, nhưng là nguồn dữ liệu duy nhất vào giỏ trên web. Lựa chọn: đưa FR-06.2/FR-06.3 vào phạm vi FR-07 (đề xuất), hoặc chỉ dùng làm thao tác chuẩn bị. Cần kiểm FR-06 có trùng feature của thành viên khác trong nhóm không.
- B7 (tầng API) (AI đề xuất, chờ SV chốt): FR-07 không nhắc API; api_specification §4 có GET/POST /api/cart; web không gọi API này (B0d). Nguồn gợi ý — A9 của A_FR01: yêu cầu hệ thống áp cho cả API. Lựa chọn: (a) kiểm API như tầng riêng, áp FR-07.3 (gộp cùng id) và FR-06.2 (quantity nguyên dương) cho body; (b) chỉ dùng API làm điểm quan sát/thiết lập.
- B8 (giá/tên do client gửi ở POST /api/cart) (AI đề xuất, chờ SV chốt): body chứa price, name (api_specification dòng 120–126). SRS FR-07 im lặng; FR-08 yêu cầu backend tự tính lại tổng, không nhận total_amount từ client. Lựa chọn: giỏ phải dùng giá theo CSDL (price trong body bị bỏ qua) hay chấp nhận giá client.
- B9 (badge 'Giỏ hàng') (AI đề xuất, chờ SV chốt): FR-23 'badge số lượng sản phẩm trong giỏ' — mơ hồ giữa số dòng (số sản phẩm khác nhau) và tổng Số lượng. Nguồn gợi ý — thông lệ: đa số shop hiển thị tổng số lượng; cũng có nơi đếm dòng. Cần chốt để có oracle.
- B10 (giữ giỏ khi tải lại trang / đăng nhập / đăng xuất) (AI đề xuất, chờ SV chốt): SRS im lặng. Nguồn gợi ý — FR-08 ngụ ý khách chưa đăng nhập có giỏ; thông lệ: giỏ giữ khi tải lại. Lựa chọn: đưa vào phạm vi (biến trạng thái phiên) hay ghi ngoài phạm vi.
- B11 (khách chưa đăng nhập dùng giỏ ở UI) (AI đề xuất, chờ SV chốt): FR-08 chỉ yêu cầu đăng nhập khi thanh toán → đề xuất: khách chưa đăng nhập vẫn thêm/xem/sửa giỏ được. Tầng API: SEC-02 + api_specification §4 yêu cầu Bearer → thiếu/sai token bị từ chối 4xx.
- B12 (nhãn chính xác) (AI đề xuất, chờ SV chốt): FR-07 in đậm 'Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác', 'Tiếp tục mua sắm', 'Tổng cộng'. Đề xuất: so khớp đúng chữ (không phân biệt hoa/thường). 'Nút Xóa sản phẩm' — chữ in đậm nhưng có thể là mô tả chức năng chứ không phải nhãn; cần chốt có so khớp chữ 'Xóa sản phẩm' hay không.
- B13 (định dạng tiền) (AI đề xuất, chờ SV chốt): FR-21 '₫ với định dạng phân cách hàng nghìn' — không nói ký tự phân cách. Nguồn gợi ý — thông lệ vi-VN dùng '.', code dùng toLocaleString() theo locale trình duyệt (Cart.jsx dòng 46, 48, 63). Lựa chọn: chấp nhận '.' hoặc ','; hay bắt buộc '.'.
- B14 (dialog xoá) (AI đề xuất, chờ SV chốt): FR-07/FR-24 chỉ yêu cầu có dialog. Đề xuất: chọn Hủy → giỏ giữ nguyên; chọn Đồng ý → dòng bị xoá, Tổng cộng cập nhật; dialog native (window.confirm) hay modal đều chấp nhận.
- B15 (empty state) (AI đề xuất, chờ SV chốt): 'hình minh họa và thông báo rõ ràng' — oracle đề xuất: có phần tử ảnh/icon (img/svg) và có dòng chữ báo giỏ trống; không cố định nội dung chữ.
- B16 (GUI liên quan) (AI đề xuất, chờ SV chốt): FR-21 (₫), FR-23 (badge, breadcrumb trang Giỏ hàng, highlight navbar), FR-24 (phản hồi khi thêm, alt ảnh) là thuộc tính tĩnh/phản hồi, không phải miền giá trị → đề xuất kiểm bằng suite TS-GUI riêng (như A14), không phân lớp.
- B17 (mã lỗi API) (AI đề xuất, chờ SV chốt): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).
- B18 (sai kiểu ở API) (AI đề xuất, chờ SV chốt): SRS im lặng về body JSON. Đề xuất như A15: quantity thiếu/null/chuỗi/số thực/0/âm; id thiếu hoặc không tồn tại trong products → bị từ chối 4xx, giỏ không đổi. Các lớp này chỉ tạo được ở tầng API.

**Tổng:** chưa có test case (bước 3–4).
