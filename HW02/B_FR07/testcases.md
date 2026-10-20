### Phạm vi
Trang 'Giỏ Hàng' (/cart) và các điểm thêm vào giỏ trên frontend-web (tầng UI), endpoint GET/POST /api/cart (tầng API, suite riêng — B7 SV chốt). Trong phạm vi: FR-07 (phân lớp + BVA); FR-06.2/FR-06.3 ô 'Số lượng' và phản hồi khi thêm (B6 SV chốt); badge FR-23.2 (B9). Thuộc tính GUI (FR-07.2 sự tồn tại nút +/-, FR-21 ₫, FR-23 breadcrumb/highlight, FR-24 alt) kiểm bằng suite TS-GUI riêng, không phân lớp, giới hạn trang giỏ và các điểm thêm vào giỏ (B16 SV chốt). Ngoài phạm vi: thanh toán (FR-08, chỉ dùng FR-08.1 để suy ra B11), mã giảm giá (FR-09), giỏ hàng trên Mobile (FR-20), giữ giỏ khi tải lại trang/đăng nhập/đăng xuất (B10 SV chốt).

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
| FR-06.2 | (B6 SV chốt) Trang chi tiết có ô nhập Số lượng, chỉ nhận số nguyên dương, tối thiểu là 1. |
| FR-06.3 | (B6 SV chốt) Nút Thêm vào giỏ hàng — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật). |
| FR-08.1 | (liên quan) Chỉ người dùng đã đăng nhập mới tiến hành thanh toán được — dùng để suy ra B11. |
| FR-21.3 | (GUI, B16) Luôn dùng ký hiệu ₫ với định dạng phân cách hàng nghìn. |
| FR-23.1 | (GUI, B16) Thanh điều hướng (Navbar) phải highlight trang đang được chọn — xét trên trang Giỏ hàng. |
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

### Bước 2 — Complete Set of Partitions
| EC | Biến | Lớp tương đương | Hợp lệ | Hướng dẫn | Ghi chú |
|---|---|---|---|---|---|
| EC1 | Số lượng khi thêm | Số nguyên ≥ 1 (vd 2) | ✔ | range | Không có cận trên (B1 SV chốt) → miền hợp lệ một phía. Áp UI (ô 'Số lượng:') + API (body.quantity). |
| EC2 | Số lượng khi thêm | Số nguyên ≤ 0 (vd 0, -3) | ✘ | range | Lớp không hợp lệ phía dưới của miền ≥ 1. Phía trên không có lớp không hợp lệ (B1). |
| EC3 | Số lượng khi thêm | Số không nguyên (vd 1.5) | ✘ | type | FR-06 'chỉ nhận số nguyên'. UI + API. |
| EC4 | Số lượng khi thêm | Rỗng (không nhập gì) | ✘ | must-be | UI: xoá trắng ô Số lượng rồi bấm thêm. API: quantity = "" . |
| EC5 | Số lượng khi thêm | Không phải số (vd 'abc') | ✘ | type | UI: input type=number có thể không cho gõ chữ (trừ e/E) — nếu không nhập được thì ghi notes, quan sát ở bước 6. API: quantity = "abc". |
| EC6 | Số lượng khi thêm | API: quantity là chuỗi số (vd "2") | ✘ | type | Chỉ tầng API (B18 đề xuất): sai kiểu JSON (chuỗi thay vì số). |
| EC7 | Số lượng khi thêm | API: thiếu trường quantity hoặc null | ✘ | must-be | Chỉ tầng API (B18 đề xuất). |
| EC8 | Sản phẩm được thêm (so với nội dung giỏ hiện có) | Sản phẩm chưa có trong giỏ | ✔ | set | → tạo dòng mới (FR-07.3 suy ngược). UI + API. |
| EC9 | Sản phẩm được thêm (so với nội dung giỏ hiện có) | Sản phẩm đã có trong giỏ, thêm lại từ cùng một trang | ✔ | split | FR-07.3 → tăng Số lượng, không tạo dòng mới. Tách theo nguồn thêm (B5 đề xuất). |
| EC10 | Sản phẩm được thêm (so với nội dung giỏ hiện có) | Sản phẩm đã có trong giỏ, thêm lại từ trang khác (Trang chủ ↔ Chi tiết) | ✔ | split | Hai nút thêm khác nhau ('Thêm vào giỏ' ở /, 'Thêm vào giỏ hàng' ở /product/:id) → có lý do tin bị xử lý khác nhau (B5). Chỉ tầng UI. |
| EC11 | Sản phẩm được thêm (so với nội dung giỏ hiện có) | API: id đã có trong giỏ (POST lần 2 cùng id) | ✔ | set | Tầng API của FR-07.3: GET /api/cart phải có 1 phần tử, quantity cộng dồn. |
| EC12 | Sản phẩm được thêm (so với nội dung giỏ hiện có) | API: id không tồn tại trong products (vd 99999) | ✘ | set | Ngoài tập sản phẩm (B18 đề xuất). |
| EC13 | Sản phẩm được thêm (so với nội dung giỏ hiện có) | API: thiếu id / id sai kiểu (vd "abc") | ✘ | type | B18 đề xuất. |
| EC14 | Đơn giá sản phẩm | UI: sản phẩm seed, đơn giá nguyên dương (4.000.000–45.000.000) | ✔ | set | Không do người dùng nhập. Đại diện chọn theo code server.js:162 (gray-box): suite API lấy cả id chẵn và id lẻ (B19); không tách lớp. |
| EC15 | Đơn giá sản phẩm | API: body.price khớp giá CSDL | ✔ | set | B8. |
| EC16 | Đơn giá sản phẩm | API: body.price khác giá CSDL (khác số, ≤ 0, sai kiểu, thiếu) | ✔ | split | B8 SV chốt: price client bị bỏ qua, giỏ dùng giá CSDL → hợp lệ, oracle = giá CSDL. |
| EC17 | Thao tác chỉnh Số lượng trong giỏ | Bấm '+' | ✔ | set | FR-07.2. Chỉ UI (API không có endpoint sửa). SUT chưa thấy nút → A17 (B3). |
| EC18 | Thao tác chỉnh Số lượng trong giỏ | Bấm '-' | ✔ | set | FR-07.2. Chỉ UI. |
| EC19 | Số lượng hiện tại của dòng (trước thao tác +/- hoặc thêm trùng) | Số lượng hiện tại = 1 | ✔ | split | Điểm đặc biệt cho '-': giữ 1 (B3 SV chốt). Biến trạng thái, không có lớp không hợp lệ. |
| EC20 | Số lượng hiện tại của dòng (trước thao tác +/- hoặc thêm trùng) | Số lượng hiện tại ≥ 2 | ✔ | split | '-' giảm 1; '+' tăng 1 (không cận trên, B1). |
| EC21 | Thao tác xoá dòng và lựa chọn trong dialog | Bấm nút xoá rồi chọn Xác nhận trong dialog | ✔ | set | FR-07.4, B14: dòng bị xoá, Tổng cộng cập nhật. |
| EC22 | Thao tác xoá dòng và lựa chọn trong dialog | Bấm nút xoá rồi chọn Hủy trong dialog | ✔ | set | B14: giỏ giữ nguyên. |
| EC23 | Số dòng trong giỏ (trạng thái) | Giỏ có 0 dòng | ✔ | count | → empty state (FR-07.7). Biến trạng thái, không có lớp không hợp lệ. |
| EC24 | Số dòng trong giỏ (trạng thái) | Giỏ có đúng 1 dòng | ✔ | count | Xoá dòng cuối → chuyển sang empty state. |
| EC25 | Số dòng trong giỏ (trạng thái) | Giỏ có ≥ 2 dòng | ✔ | count | Tổng cộng = Σ nhiều Thành tiền (B4); xoá 1 dòng không ảnh hưởng dòng khác. |
| EC26 | Trạng thái đăng nhập / token | UI: chưa đăng nhập | ✔ | set | B11 đề xuất: khách vẫn dùng giỏ (suy từ FR-08.1). |
| EC27 | Trạng thái đăng nhập / token | UI: đã đăng nhập (test@eshop.com hoặc user {ts}) | ✔ | set |  |
| EC28 | Trạng thái đăng nhập / token | API: token hợp lệ | ✔ | must-be | SEC-02. |
| EC29 | Trạng thái đăng nhập / token | API: thiếu header Authorization | ✘ | must-be | SEC-02, B17: 4xx. |
| EC30 | Trạng thái đăng nhập / token | API: token sai/giả mạo | ✘ | must-be | SEC-02, B17: 4xx. |
| EC31 | Tên sản phẩm trong body (API) | API: body.name khớp tên CSDL | ✔ | set | B8. |
| EC32 | Tên sản phẩm trong body (API) | API: body.name khác tên CSDL (kể cả chuỗi chứa thẻ HTML) | ✔ | split | Áp B8 cho tên (AI suy rộng, SV xác nhận): name client bị bỏ qua, giỏ dùng tên CSDL. |
| EC33 | Thao tác 'Tiếp tục mua sắm' | Bấm 'Tiếp tục mua sắm' | ✔ | set | FR-07.5. Hai trạng thái giỏ (trống / có hàng) do V7 phủ. |
| EC34 | Danh sách dòng trong giỏ | Bảng giỏ hiển thị đủ 5 cột (Sản phẩm, Đơn giá, Số lượng, Thành tiền, Thao tác), mỗi sản phẩm 1 dòng | ✔ | set | FR-07.1, FR-07.3. UI. |
| EC35 | Danh sách dòng trong giỏ | Không có bảng (giỏ trống) | ✔ | set | Đi cùng EC48 (empty state). |
| EC36 | Danh sách dòng trong giỏ | API: GET /api/cart trả mảng, mỗi id một phần tử, chỉ chứa hàng của user sở hữu token | ✔ | set | FR-07.3 áp cho API (B7); mỗi user một giỏ (B0a). |
| EC37 | Số lượng của dòng sau thao tác | Số lượng tăng đúng bằng số lượng thêm (cộng dồn) | ✔ | set | FR-07.3. |
| EC38 | Số lượng của dòng sau thao tác | Số lượng tăng 1 | ✔ | set | '+' (FR-07.2). |
| EC39 | Số lượng của dòng sau thao tác | Số lượng giảm 1 | ✔ | set | '-' khi ≥ 2. |
| EC40 | Số lượng của dòng sau thao tác | Số lượng giữ nguyên | ✔ | set | '-' khi = 1 (B3), hoặc lần thêm bị từ chối (B2). |
| EC41 | Thành tiền của dòng | Thành tiền = Đơn giá × Số lượng, hiển thị ₫ + phân cách hàng nghìn | ✔ | set | B4, FR-21.3, B13. |
| EC42 | Tổng cộng | Nhãn 'Tổng cộng', giá trị = Σ Thành tiền, hiển thị ₫ | ✔ | set | FR-07.6, B4. |
| EC43 | Badge số lượng trên link 'Giỏ hàng' | Badge = tổng Số lượng trong giỏ (≥ 1) | ✔ | set | FR-23.2, B9 SV chốt. |
| EC44 | Badge số lượng trên link 'Giỏ hàng' | Giỏ trống: badge ẩn hoặc hiển thị 0 | ✔ | set | SRS im lặng; đề xuất chấp nhận cả hai. |
| EC45 | Phản hồi trực quan sau khi thêm | Có phản hồi trực quan (toast hoặc badge cập nhật) sau lần thêm hợp lệ | ✔ | set | FR-06.3, FR-24.1. |
| EC46 | Phản hồi trực quan sau khi thêm | Không báo 'đã thêm' khi lần thêm bị từ chối | ✔ | set | B2 SV chốt: không yêu cầu thông báo lỗi; chỉ yêu cầu không có phản hồi 'đã thêm' và giỏ không đổi. |
| EC47 | Dialog xác nhận xoá | Dialog xác nhận hiện ra trước khi xoá | ✔ | must-be | FR-07.4, FR-24.2. |
| EC48 | Trạng thái giỏ trống (empty state) | Empty state có hình minh hoạ/icon và thông báo giỏ trống | ✔ | must-be | FR-07.7, FR-24.3, B15. |
| EC49 | Trang đích sau 'Tiếp tục mua sắm' | URL sau khi bấm là trang chủ '/' | ✔ | must-be | FR-07.5. |
| EC50 | Phản hồi API giỏ hàng | API: 2xx và GET /api/cart phản ánh thay đổi | ✔ | set |  |
| EC51 | Phản hồi API giỏ hàng | API: 4xx kèm trường error, giỏ không đổi | ✔ | set | B17. Không 2xx, không 5xx. |

### Bước 3a — Test Cases Providing Coverage of Partitions
| EC | Lớp | Test case phủ |
|---|---|---|
| EC1 | Số nguyên ≥ 1 (vd 2) | TC-FR07-02, TC-FR07-03, TC-FR07-04, TC-FR07-20, TC-FR07-21, TC-FR07-22, TC-FR07-23, TC-FR07-36, TC-FR07-37, TC-FR07-38, TC-FR07-39 |
| EC2 | Số nguyên ≤ 0 (vd 0, -3) | TC-FR07-10, TC-FR07-30 |
| EC3 | Số không nguyên (vd 1.5) | TC-FR07-11, TC-FR07-31 |
| EC4 | Rỗng (không nhập gì) | TC-FR07-12, TC-FR07-32 |
| EC5 | Không phải số (vd 'abc') | TC-FR07-13, TC-FR07-33 |
| EC6 | API: quantity là chuỗi số (vd "2") | TC-FR07-34 |
| EC7 | API: thiếu trường quantity hoặc null | TC-FR07-35 |
| EC8 | Sản phẩm chưa có trong giỏ | TC-FR07-02, TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13, TC-FR07-20, TC-FR07-22, TC-FR07-23, TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-38, TC-FR07-39 |
| EC9 | Sản phẩm đã có trong giỏ, thêm lại từ cùng một trang | TC-FR07-03 |
| EC10 | Sản phẩm đã có trong giỏ, thêm lại từ trang khác (Trang chủ ↔ Chi tiết) | TC-FR07-04 |
| EC11 | API: id đã có trong giỏ (POST lần 2 cùng id) | TC-FR07-21 |
| EC12 | API: id không tồn tại trong products (vd 99999) | TC-FR07-36 |
| EC13 | API: thiếu id / id sai kiểu (vd "abc") | TC-FR07-37 |
| EC14 | UI: sản phẩm seed, đơn giá nguyên dương (4.000.000–45.000.000) | TC-FR07-02, TC-FR07-04, TC-FR07-05, TC-FR07-07, TC-FR07-08, TC-FR07-09, TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13 |
| EC15 | API: body.price khớp giá CSDL | TC-FR07-20, TC-FR07-21, TC-FR07-23, TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-38, TC-FR07-39 |
| EC16 | API: body.price khác giá CSDL (khác số, ≤ 0, sai kiểu, thiếu) | TC-FR07-22 |
| EC17 | Bấm '+' | TC-FR07-05 |
| EC18 | Bấm '-' | TC-FR07-06, TC-FR07-07 |
| EC19 | Số lượng hiện tại = 1 | TC-FR07-05, TC-FR07-07 |
| EC20 | Số lượng hiện tại ≥ 2 | TC-FR07-06 |
| EC21 | Bấm nút xoá rồi chọn Xác nhận trong dialog | TC-FR07-08 |
| EC22 | Bấm nút xoá rồi chọn Hủy trong dialog | TC-FR07-09 |
| EC23 | Giỏ có 0 dòng | TC-FR07-01, TC-FR07-02, TC-FR07-20, TC-FR07-23 |
| EC24 | Giỏ có đúng 1 dòng | TC-FR07-03, TC-FR07-05, TC-FR07-06, TC-FR07-07, TC-FR07-09, TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13, TC-FR07-21, TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-36, TC-FR07-37, TC-FR07-38, TC-FR07-39 |
| EC25 | Giỏ có ≥ 2 dòng | TC-FR07-04, TC-FR07-08, TC-FR07-22 |
| EC26 | UI: chưa đăng nhập | TC-FR07-01, TC-FR07-03, TC-FR07-05, TC-FR07-07, TC-FR07-09 |
| EC27 | UI: đã đăng nhập (test@eshop.com hoặc user {ts}) | TC-FR07-02, TC-FR07-04, TC-FR07-06, TC-FR07-08, TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13 |
| EC28 | API: token hợp lệ | TC-FR07-20, TC-FR07-21, TC-FR07-22, TC-FR07-23, TC-FR07-36, TC-FR07-37 |
| EC29 | API: thiếu header Authorization | TC-FR07-38 |
| EC30 | API: token sai/giả mạo | TC-FR07-39 |
| EC31 | API: body.name khớp tên CSDL | TC-FR07-20, TC-FR07-21, TC-FR07-22, TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-38, TC-FR07-39 |
| EC32 | API: body.name khác tên CSDL (kể cả chuỗi chứa thẻ HTML) | TC-FR07-23 |
| EC33 | Bấm 'Tiếp tục mua sắm' | TC-FR07-01, TC-FR07-02 |
| EC34 | Bảng giỏ hiển thị đủ 5 cột (Sản phẩm, Đơn giá, Số lượng, Thành tiền, Thao tác), mỗi sản phẩm 1 dòng | TC-FR07-02, TC-FR07-08 |
| EC35 | Không có bảng (giỏ trống) | TC-FR07-01 |
| EC36 | API: GET /api/cart trả mảng, mỗi id một phần tử, chỉ chứa hàng của user sở hữu token | TC-FR07-20, TC-FR07-21 |
| EC37 | Số lượng tăng đúng bằng số lượng thêm (cộng dồn) | TC-FR07-03, TC-FR07-04, TC-FR07-21 |
| EC38 | Số lượng tăng 1 | TC-FR07-05 |
| EC39 | Số lượng giảm 1 | TC-FR07-06 |
| EC40 | Số lượng giữ nguyên | TC-FR07-07, TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13 |
| EC41 | Thành tiền = Đơn giá × Số lượng, hiển thị ₫ + phân cách hàng nghìn | TC-FR07-02, TC-FR07-03, TC-FR07-04, TC-FR07-05, TC-FR07-06 |
| EC42 | Nhãn 'Tổng cộng', giá trị = Σ Thành tiền, hiển thị ₫ | TC-FR07-02, TC-FR07-03, TC-FR07-04, TC-FR07-05, TC-FR07-06, TC-FR07-08 |
| EC43 | Badge = tổng Số lượng trong giỏ (≥ 1) | TC-FR07-02, TC-FR07-03, TC-FR07-04, TC-FR07-05, TC-FR07-06, TC-FR07-08 |
| EC44 | Giỏ trống: badge ẩn hoặc hiển thị 0 | TC-FR07-01 |
| EC45 | Có phản hồi trực quan (toast hoặc badge cập nhật) sau lần thêm hợp lệ | TC-FR07-02, TC-FR07-03, TC-FR07-04 |
| EC46 | Không báo 'đã thêm' khi lần thêm bị từ chối | TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13 |
| EC47 | Dialog xác nhận hiện ra trước khi xoá | TC-FR07-08, TC-FR07-09 |
| EC48 | Empty state có hình minh hoạ/icon và thông báo giỏ trống | TC-FR07-01 |
| EC49 | URL sau khi bấm là trang chủ '/' | TC-FR07-01, TC-FR07-02 |
| EC50 | API: 2xx và GET /api/cart phản ánh thay đổi | TC-FR07-20, TC-FR07-21, TC-FR07-22, TC-FR07-23 |
| EC51 | API: 4xx kèm trường error, giỏ không đổi | TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-36, TC-FR07-37, TC-FR07-38, TC-FR07-39 |

### Bước 3b — Minimum Set of Test Cases (Domain) · TS-DOM-UI — Domain — minimum set, tầng UI (FR-07, FR-06)
**Ghi chú suite:** Giỏ web là state React (B0d): chỉ mở URL trực tiếp ở bước 1, sau đó điều hướng bằng link trong app.
**Tiền điều kiện:** Trước mỗi lượt chạy cả suite: khởi động lại backend (node server.js) → CSDL seed sạch, userCarts rỗng (B0c).; Có token admin: POST /api/login với admin@eshop.com / Admin123! (dùng cho DELETE /api/admin/users/:id khi dọn dẹp).; Thay {ts} bằng Date.now() lúc chạy case để mỗi case có user riêng (B0a).; Sản phẩm seed (database.js dòng 98–102): id 1 'iPhone 15 Pro Max' 30.000.000 ₫ · id 2 'Samsung Galaxy S24 Ultra' 28.000.000 ₫ · id 3 'MacBook Pro M3' 45.000.000 ₫ · id 4 'Tai nghe AirPods Pro 2' 6.000.000 ₫ · id 5 'Bàn phím cơ Keychron Q1' 4.000.000 ₫. Giá trị CSDL dùng bảng này, không đọc qua GET /api/products/:id.; Web http://localhost:5173 đang chạy.; Trạng thái ban đầu của mỗi case: browser context mới (Playwright) hoặc cửa sổ ẩn danh, tắt autofill (chạy tay); localStorage không có token; giỏ web rỗng.

**Quy trình chung:**
1. Nếu cột 'Đăng nhập' = 'user {ts}': gọi POST /api/register {name: 'Cart Tester', email: 'cartNN_{ts}@domain.com', password: 'Abcd1234!'} (NN = số TC), rồi mở http://localhost:5173/login, nhập ô 'Username' = email đó, ô 'Mật khẩu' = 'Abcd1234!', bấm nút đăng nhập. Nếu = 'khách': mở http://localhost:5173/. Đây là lần mở URL trực tiếp DUY NHẤT của case (giỏ web là state React, B0d). → Trang chủ 'Danh sách sản phẩm' hiển thị; navbar có 'Chào, Cart Tester' (user) hoặc link 'Đăng nhập' (khách).
2. Dựng 'Giỏ ban đầu' theo đúng thứ tự trong cột. 'TC: <id>' = ở trang chủ bấm 'Thêm vào giỏ' trên thẻ sản phẩm đó đúng một lần. 'CT: <id> × n' = bấm 'Xem chi tiết' trên thẻ, xoá trắng ô 'Số lượng:', gõ n, bấm 'Thêm vào giỏ hàng' đúng một lần, rồi bấm link 'EShop' trên navbar để về trang chủ. '—' = không thêm gì. Chỉ điều hướng bằng link trong app, không tải lại trang. → Mỗi lần thêm có phản hồi trên trang.
3. Bấm link 'Giỏ hàng' trên navbar. Ghi lại trạng thái TRƯỚC: số dòng; Sản phẩm, Đơn giá, Số lượng, Thành tiền của từng dòng; Tổng cộng; badge trên link 'Giỏ hàng'. → Giỏ khớp cột 'Giỏ ban đầu' (sản phẩm, số lượng). Không khớp → dừng, Blocked, ghi case gốc gây chặn (B20).
4. Thực hiện cột 'Thao tác' đúng một lần. Thao tác ở trang chi tiết: từ trang giỏ bấm link 'EShop' → 'Xem chi tiết' trên thẻ sản phẩm → ô 'Số lượng:' xoá trắng rồi gõ đúng chuỗi trong cột ('' = để trống) → bấm 'Thêm vào giỏ hàng' đúng một lần. Thao tác '+', '-', xoá: bấm nút trên dòng sản phẩm ghi trong cột; dialog: bấm nút ghi trong cột. → Hệ thống phản hồi (phản hồi trực quan, dialog, đổi số, chuyển trang hoặc không đổi gì).
5. Quan sát ngay sau thao tác: toast/badge, dialog, URL trên thanh địa chỉ. → Khớp phần phản hồi trong cột Expected.
6. Nếu không ở trang giỏ: bấm link 'Giỏ hàng' trên navbar (trừ khi Expected yêu cầu quan sát trang khác). Ghi trạng thái SAU, so với TRƯỚC ở bước 3. → Chênh lệch TRƯỚC → SAU đúng như cột Expected (oracle tương đối, B0b).

**Dọn dẹp:** Sau mỗi case, kể cả khi Fail: nếu case đã tạo user {ts}, xoá bằng DELETE /api/admin/users/:id (token admin). Xoá thất bại: ghi notes, không đổi verdict (B0c). Giỏ của user đó nằm trong RAM tới lần khởi động lại backend kế tiếp — không ảnh hưởng case khác vì mỗi case một user.

| #TC | Tiêu đề | EC phủ | Đăng nhập | Giỏ ban đầu | Thao tác | Expected | Lý do chọn input | Nguồn |
|---|---|---|---|---|---|---|---|---|
| TC-FR07-01 | Kiểm tra trang giỏ hàng trống và nút 'Tiếp tục mua sắm' khi khách chưa đăng nhập mở giỏ rỗng | EC23, EC26, EC33, EC35, EC44, EC48, EC49 | khách | — | Ở trang giỏ: bấm 'Tiếp tục mua sắm' | Bước 3: trang giỏ không có bảng; có hình minh hoạ/icon và thông báo giỏ trống (FR-07.7); badge ẩn hoặc 0. Bước 5: URL = http://localhost:5173/ (FR-07.5). | Case hợp lệ gộp mọi lớp của trạng thái giỏ rỗng: không cần dựng dữ liệu nên không phụ thuộc đường thêm vào giỏ. | AI |
| TC-FR07-02 | Kiểm tra thêm sản phẩm mới với số lượng 2 từ trang chi tiết khi user đã đăng nhập và giỏ rỗng | EC1, EC8, EC14, EC23, EC27, EC33, EC34, EC41, EC42, EC43, EC45, EC49 | user {ts} | — | CT: id 2 × 2, rồi ở trang giỏ bấm 'Tiếp tục mua sắm' | Bước 5 (sau khi bấm 'Thêm vào giỏ hàng'): có phản hồi trực quan (toast hoặc badge cập nhật). TRƯỚC → SAU: 0 → 1 dòng; bảng có đủ 5 cột 'Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác'; dòng 'Samsung Galaxy S24 Ultra', Đơn giá 28.000.000 ₫, Số lượng 2, Thành tiền 56.000.000 ₫; nhãn 'Tổng cộng' = 56.000.000 ₫; badge 2. Sau khi bấm 'Tiếp tục mua sắm' (có ở giỏ không rỗng): URL = http://localhost:5173/, badge vẫn 2. | Case hợp lệ chính: số lượng danh nghĩa 2 (khác giá trị mặc định 1 để thấy ô Số lượng có tác dụng); Thành tiền khác Đơn giá nên kiểm được phép nhân; kiểm 'Tiếp tục mua sắm' ở giỏ có hàng (TC-01 đã kiểm ở giỏ rỗng). | AI |
| TC-FR07-03 | Kiểm tra thêm lại cùng sản phẩm từ trang chi tiết khi sản phẩm đã có trong giỏ | EC1, EC9, EC24, EC26, EC37, EC41, EC42, EC43, EC45 | khách | CT: id 5 × 1 | CT: id 5 × 3 | Có phản hồi trực quan sau khi thêm. TRƯỚC → SAU: vẫn 1 dòng (không tạo dòng mới); 'Bàn phím cơ Keychron Q1' Số lượng 1 → 4; Thành tiền 16.000.000 ₫; Tổng cộng 16.000.000 ₫; badge 4. | Đại diện EC9 (thêm lại từ cùng trang, B5): số lượng thêm 3 ≠ 1 để phân biệt 'cộng dồn' với 'tăng 1'. | AI |
| TC-FR07-04 | Kiểm tra thêm lại sản phẩm từ trang chi tiết khi sản phẩm đã được thêm từ trang chủ và giỏ có 2 dòng | EC1, EC10, EC14, EC25, EC27, EC37, EC41, EC42, EC43, EC45 | user {ts} | TC: id 1; TC: id 4 | CT: id 4 × 2 | Mỗi lần bấm 'Thêm vào giỏ' ở bước 2 có phản hồi trực quan (FR-24.1). TRƯỚC → SAU: vẫn 2 dòng; dòng 'Tai nghe AirPods Pro 2' Số lượng 1 → 3, Thành tiền 18.000.000 ₫; dòng 'iPhone 15 Pro Max' giữ Số lượng 1, Thành tiền 30.000.000 ₫; Tổng cộng 48.000.000 ₫; badge 4. | Đại diện EC10 (thêm lại từ trang khác, B5) trong giỏ ≥ 2 dòng: kiểm cùng lúc gộp đúng dòng và Tổng cộng là tổng nhiều Thành tiền. | AI |
| TC-FR07-05 | Kiểm tra nút '+' khi dòng có số lượng 1 | EC14, EC17, EC19, EC24, EC26, EC38, EC41, EC42, EC43 | khách | TC: id 5 | Bấm '+' trên dòng id 5 | TRƯỚC → SAU: 'Bàn phím cơ Keychron Q1' Số lượng 1 → 2; Thành tiền 4.000.000 → 8.000.000 ₫; Tổng cộng 8.000.000 ₫; badge 2; vẫn 1 dòng. | Đại diện '+' tại điểm danh nghĩa nhỏ nhất (Số lượng 1); dựng giỏ bằng trang chủ để không phụ thuộc ô Số lượng. | AI |
| TC-FR07-06 | Kiểm tra nút '-' khi dòng có số lượng 3 | EC18, EC20, EC24, EC27, EC39, EC41, EC42, EC43 | user {ts} | CT: id 5 × 3 | Bấm '-' trên dòng id 5 | TRƯỚC → SAU: Số lượng 3 → 2; Thành tiền 12.000.000 → 8.000.000 ₫; Tổng cộng 8.000.000 ₫; badge 2; vẫn 1 dòng. | Đại diện '-' khi Số lượng ≥ 2 (lấy 3, không phải biên 2 — biên để bước 4). | AI |
| TC-FR07-07 | Kiểm tra nút '-' khi dòng có số lượng 1 | EC14, EC18, EC19, EC24, EC26, EC40 | khách | TC: id 5 | Bấm '-' trên dòng id 5 | Không có dialog xoá, dòng không bị xoá. TRƯỚC → SAU: Số lượng giữ 1; Thành tiền 4.000.000 ₫; Tổng cộng 4.000.000 ₫; badge 1 (B3). | EC19 với '-' có kết quả riêng (giữ 1, B3 SV chốt) nên cần case riêng, không gộp với TC-06. | AI |
| TC-FR07-08 | Kiểm tra xoá một dòng và xác nhận trong dialog khi giỏ có 2 dòng | EC14, EC21, EC25, EC27, EC34, EC42, EC43, EC47 | user {ts} | TC: id 4; TC: id 5 | Bấm nút xoá trên dòng id 4 → dialog: chọn xác nhận | Sau khi bấm nút xoá: hiện dialog xác nhận, dòng chưa bị xoá khi dialog đang mở (FR-07.4). Sau khi xác nhận: TRƯỚC → SAU: 2 → 1 dòng; không còn 'Tai nghe AirPods Pro 2'; 'Bàn phím cơ Keychron Q1' giữ nguyên Số lượng 1; Tổng cộng 10.000.000 → 4.000.000 ₫; badge 2 → 1. | Xoá trong giỏ ≥ 2 dòng để kiểm được cả 'xoá đúng dòng' và 'dòng còn lại không đổi'. Xoá dòng cuối (1 → 0) để bước 4 (biên số dòng). | AI |
| TC-FR07-09 | Kiểm tra huỷ trong dialog xoá khi giỏ có 1 dòng | EC14, EC22, EC24, EC26, EC47 | khách | TC: id 4 | Bấm nút xoá trên dòng id 4 → dialog: chọn Hủy | Sau khi bấm nút xoá: hiện dialog xác nhận. Sau khi Hủy: TRƯỚC → SAU: giỏ không đổi — 1 dòng 'Tai nghe AirPods Pro 2' Số lượng 1, Tổng cộng 6.000.000 ₫, badge 1 (B14). | Nhánh Hủy của dialog — kết quả khác nhánh xác nhận nên case riêng. | AI |
| TC-FR07-10 | Kiểm tra thêm từ trang chi tiết khi số lượng âm | EC2, EC8, EC14, EC24, EC27, EC46, EC40 | user {ts} | TC: id 1 | CT: id 5 × -3 | Không có phản hồi 'đã thêm'; TRƯỚC → SAU: giỏ không đổi — vẫn 1 dòng id 1 Số lượng 1, không có dòng id 5, Tổng cộng 30.000.000 ₫, badge 1 (B2). | Đại diện giữa lớp ≤ 0 (−3); giá trị 0 là LB-1, để bước 4. Giỏ ban đầu có hàng khác để 'giỏ không đổi' quan sát được. | AI |
| TC-FR07-11 | Kiểm tra thêm từ trang chi tiết khi số lượng là số thập phân | EC3, EC8, EC14, EC24, EC27, EC46, EC40 | user {ts} | TC: id 1 | CT: id 5 × 1.5 | Không có phản hồi 'đã thêm'; TRƯỚC → SAU: giỏ không đổi — vẫn 1 dòng id 1 Số lượng 1, không có dòng id 5, Tổng cộng 30.000.000 ₫, badge 1 (B2). | 1.5 nằm giữa hai số nguyên hợp lệ 1 và 2 — làm tròn lên/xuống đều cho ra số hợp lệ nên lộ được việc chấp nhận ngầm. | AI |
| TC-FR07-12 | Kiểm tra thêm từ trang chi tiết khi ô số lượng để trống | EC4, EC8, EC14, EC24, EC27, EC46, EC40 | user {ts} | TC: id 1 | CT: id 5 × '' (xoá trắng ô) | Không có phản hồi 'đã thêm'; TRƯỚC → SAU: giỏ không đổi — vẫn 1 dòng id 1 Số lượng 1, không có dòng id 5, Tổng cộng 30.000.000 ₫, badge 1 (B2). | Lớp rỗng: ô có giá trị mặc định 1 nên phải chủ động xoá trắng. | AI |
| TC-FR07-13 | Kiểm tra thêm từ trang chi tiết khi số lượng không phải số | EC5, EC8, EC14, EC24, EC27, EC46, EC40 | user {ts} | TC: id 1 | CT: id 5 × 'abc' | Không có phản hồi 'đã thêm'; TRƯỚC → SAU: giỏ không đổi — vẫn 1 dòng id 1 Số lượng 1, không có dòng id 5, Tổng cộng 30.000.000 ₫, badge 1 (B2). | Đại diện chuỗi chữ thường gặp. | AI |

### Bước 3b — Minimum Set of Test Cases (Domain) · TS-DOM-API — Domain — minimum set, tầng API /api/cart (FR-07, FR-06)
**Ghi chú suite:** Giá trị danh nghĩa: token T của user {ts}, giỏ ban đầu id 1 × 1, body id 5 (tên/giá CSDL) quantity 1.
**Tiền điều kiện:** Trước mỗi lượt chạy cả suite: khởi động lại backend (node server.js) → CSDL seed sạch, userCarts rỗng (B0c).; Có token admin: POST /api/login với admin@eshop.com / Admin123! (dùng cho DELETE /api/admin/users/:id khi dọn dẹp).; Thay {ts} bằng Date.now() lúc chạy case để mỗi case có user riêng (B0a).; Sản phẩm seed (database.js dòng 98–102): id 1 'iPhone 15 Pro Max' 30.000.000 ₫ · id 2 'Samsung Galaxy S24 Ultra' 28.000.000 ₫ · id 3 'MacBook Pro M3' 45.000.000 ₫ · id 4 'Tai nghe AirPods Pro 2' 6.000.000 ₫ · id 5 'Bàn phím cơ Keychron Q1' 4.000.000 ₫. Giá trị CSDL dùng bảng này, không đọc qua GET /api/products/:id.

**Quy trình chung:**
1. Gọi POST /api/register {name: 'Cart Tester', email: 'apiNN_{ts}@domain.com', password: 'Abcd1234!'} (NN = số TC), rồi POST /api/login cùng email/mật khẩu → lưu token T. → HTTP 200 cho cả hai; phản hồi login có token.
2. Dựng 'Giỏ ban đầu': mỗi mục 'id k × n' → POST /api/cart, header Authorization: Bearer T, body {id: k, name: <tên CSDL>, price: <giá CSDL>, quantity: n}. '—' = không gửi. → HTTP 200 cho mỗi request.
3. GET /api/cart (Bearer T) → lưu TRƯỚC. → HTTP 200; mảng khớp cột 'Giỏ ban đầu'. Không khớp → dừng, Blocked, ghi case gốc (B20).
4. Gửi đúng một POST /api/cart, Content-Type: application/json. Header theo cột 'Token': 'T' = Bearer T; 'thiếu' = không gửi header Authorization; 'sai' = 'Bearer abc.def.ghi'. Body lấy từ các cột id/name/price/quantity: 'CSDL' = giá trị trong bảng sản phẩm seed; '— thiếu —' = bỏ khoá khỏi body; "…" = chuỗi JSON; số không ngoặc = số JSON; `""` = chuỗi rỗng. → Nhận được phản hồi HTTP.
5. Ghi lại HTTP status và body JSON. → Khớp phần phản hồi trong cột Expected.
6. GET /api/cart (Bearer T) → SAU; so với TRƯỚC. → Chênh lệch TRƯỚC → SAU đúng như cột Expected (oracle tương đối, B0b).

**Dọn dẹp:** Sau mỗi case, kể cả khi Fail: nếu case đã tạo user {ts}, xoá bằng DELETE /api/admin/users/:id (token admin). Xoá thất bại: ghi notes, không đổi verdict (B0c). Giỏ của user đó nằm trong RAM tới lần khởi động lại backend kế tiếp — không ảnh hưởng case khác vì mỗi case một user.

| #TC | Tiêu đề | EC phủ | Token | Giỏ ban đầu | id | name | price | quantity | Expected | Lý do chọn input | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-FR07-20 | Kiểm tra thêm sản phẩm mới số lượng 2 qua API khi giỏ rỗng (sản phẩm id lẻ) | EC1, EC8, EC15, EC23, EC28, EC31, EC36, EC50 | T | — | 1 | CSDL | CSDL | 2 | HTTP 2xx. TRƯỚC → SAU: [] → đúng 1 phần tử id 1, name 'iPhone 15 Pro Max', price 30000000, quantity 2. | Case hợp lệ chính tầng API: body đúng mẫu api_specification, giá/tên khớp CSDL; id lẻ (B19). | AI |
| TC-FR07-21 | Kiểm tra thêm lại cùng sản phẩm qua API khi sản phẩm đã có trong giỏ (sản phẩm id chẵn) | EC1, EC11, EC15, EC24, EC28, EC31, EC36, EC37, EC50 | T | id 2 × 1 | 2 | CSDL | CSDL | 3 | HTTP 2xx. TRƯỚC → SAU: vẫn 1 phần tử id 2 (không thêm phần tử mới); quantity 1 → 4. | FR-07.3 áp cho tầng API (B7); số lượng 3 ≠ 1 để phân biệt cộng dồn với tăng 1; id chẵn (B19). | AI |
| TC-FR07-22 | Kiểm tra thêm qua API khi price trong body khác giá CSDL và giỏ có 2 dòng (sản phẩm id chẵn) | EC1, EC8, EC16, EC25, EC28, EC31, EC50 | T | id 1 × 1; id 5 × 1 | 4 | CSDL | 1 | 1 | HTTP 2xx. TRƯỚC → SAU: 2 → 3 phần tử; phần tử id 4 có price 6000000 (giá CSDL, không phải 1); id 1 và id 5 không đổi. | Lớp dựa trên quyết định B8 có case hợp lệ riêng để lỗi (nếu có) không lẫn với lớp khác; price 1 khác xa giá thật nên dễ thấy. | AI |
| TC-FR07-23 | Kiểm tra thêm qua API khi name trong body khác tên CSDL và chứa thẻ HTML (sản phẩm id lẻ) | EC1, EC8, EC15, EC23, EC28, EC32, EC50 | T | — | 5 | "<b>Hack</b>" | CSDL | 1 | HTTP 2xx. TRƯỚC → SAU: [] → 1 phần tử id 5, name 'Bàn phím cơ Keychron Q1' (tên CSDL), price 4000000. | Lớp dựa trên suy rộng B8 cho tên — case riêng; chuỗi HTML để nếu tên client được giữ thì còn kiểm được SEC-04 ở nơi hiển thị. | AI |
| TC-FR07-30 | Kiểm tra thêm qua API khi quantity âm | EC2, EC8, EC24, EC15, EC31, EC51 | T | id 1 × 1 | 5 | CSDL | CSDL | -3 | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | Đại diện giữa lớp ≤ 0; 0 để bước 4. | AI |
| TC-FR07-31 | Kiểm tra thêm qua API khi quantity là số thập phân | EC3, EC8, EC24, EC15, EC31, EC51 | T | id 1 × 1 | 5 | CSDL | CSDL | 1.5 | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | Giữa hai số nguyên hợp lệ. | AI |
| TC-FR07-32 | Kiểm tra thêm qua API khi quantity là chuỗi rỗng | EC4, EC8, EC24, EC15, EC31, EC51 | T | id 1 × 1 | 5 | CSDL | CSDL | "" | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | Tương đương ô Số lượng để trống ở UI. | AI |
| TC-FR07-33 | Kiểm tra thêm qua API khi quantity là chuỗi chữ | EC5, EC8, EC24, EC15, EC31, EC51 | T | id 1 × 1 | 5 | CSDL | CSDL | "abc" | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | Không phải số. | AI |
| TC-FR07-34 | Kiểm tra thêm qua API khi quantity là chuỗi số | EC6, EC8, EC24, EC15, EC31, EC51 | T | id 1 × 1 | 5 | CSDL | CSDL | "2" | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | Sai kiểu JSON nhưng trông như hợp lệ (B18) — dễ bị ép kiểu ngầm. | AI |
| TC-FR07-35 | Kiểm tra thêm qua API khi thiếu trường quantity | EC7, EC8, EC24, EC15, EC31, EC51 | T | id 1 × 1 | 5 | CSDL | CSDL | — thiếu — | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | Thiếu trường là dạng phổ biến nhất của EC7 (null tương đương, B18). | AI |
| TC-FR07-36 | Kiểm tra thêm qua API khi id sản phẩm không tồn tại | EC1, EC12, EC24, EC28, EC51 | T | id 1 × 1 | 99999 | "Không tồn tại" | 1000 | 1 | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 99999. | id lớn hơn hẳn số sản phẩm seed (5) nên chắc chắn không tồn tại; name/price không có giá trị CSDL nên điền giá trị bất kỳ. | AI |
| TC-FR07-37 | Kiểm tra thêm qua API khi id là chuỗi chữ | EC1, EC13, EC24, EC28, EC51 | T | id 1 × 1 | "abc" | CSDL của id 5 | CSDL của id 5 | 1 | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có phần tử mới. | Sai kiểu id (B18); thiếu id tương đương, để bước 5/BVA nếu cần. | AI |
| TC-FR07-38 | Kiểm tra thêm qua API khi thiếu header Authorization | EC1, EC8, EC29, EC24, EC15, EC31, EC51 | thiếu | id 1 × 1 | 5 | CSDL | CSDL | 1 | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | SEC-02; GET ở bước 6 dùng token T hợp lệ để thấy giỏ của user không đổi. | AI |
| TC-FR07-39 | Kiểm tra thêm qua API khi token sai | EC1, EC8, EC30, EC24, EC15, EC31, EC51 | sai | id 1 × 1 | 5 | CSDL | CSDL | 1 | HTTP 4xx (không 2xx, không 5xx), body có trường error (B17). TRƯỚC → SAU: GET /api/cart không đổi — 1 phần tử id 1 quantity 1, không có id 5. | Token sai định dạng/chữ ký. | AI |

### TS-GUI — GUI — trang giỏ và các điểm thêm vào giỏ (FR-07.2 tồn tại nút, FR-21, FR-23, FR-24)
| #TC | Tiêu đề | EC phủ | Expected | Lý do chọn input | Nguồn |
|---|---|---|---|---|---|
| TC-FR07-90 | Kiểm tra sự tồn tại nút '+' và '-' trong cột Số lượng khi giỏ có 1 dòng |  | Ô Số lượng của dòng có nút '+' và nút '-' (FR-07.2). | Case kiểm sự tồn tại theo A17: TC-05, TC-06, TC-07 phụ thuộc case này (B20). | AI |
| TC-FR07-91 | Kiểm tra breadcrumb khi mở trang Giỏ hàng |  | Trang Giỏ hàng có breadcrumb thể hiện vị trí (ví dụ 'Trang chủ > Giỏ hàng'); mục trang chủ bấm được. | FR-23 liệt kê Giỏ hàng là trang con bắt buộc có breadcrumb. | AI |
| TC-FR07-92 | Kiểm tra highlight link 'Giỏ hàng' trên navbar khi đang ở trang Giỏ hàng |  | Link 'Giỏ hàng' được highlight (kiểu hiển thị khác các link khác) khi ở /cart; ở trang chủ thì không. | Giới hạn B16: chỉ xét trang giỏ. | AI |
| TC-FR07-93 | Kiểm tra ký hiệu ₫ và phân cách hàng nghìn khi xem giá trên trang chủ, trang chi tiết và trang giỏ |  | Mọi số tiền ở 3 trang dùng ký hiệu '₫' và có phân cách hàng nghìn (6.000.000 ₫ hoặc 6,000,000 ₫, B13). | Ba điểm hiển thị giá nằm trong phạm vi B16. | AI |
| TC-FR07-94 | Kiểm tra thuộc tính alt khi xem ảnh sản phẩm trên trang chủ và trang chi tiết |  | Mọi ảnh sản phẩm có alt không rỗng, mô tả nội dung ảnh (ví dụ chứa tên sản phẩm). | Điểm thêm vào giỏ đều hiển thị ảnh sản phẩm (B16). | AI |

**Các bước chi tiết:**

**TC-FR07-90** — Kiểm tra sự tồn tại nút '+' và '-' trong cột Số lượng khi giỏ có 1 dòng

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.; Khách chưa đăng nhập; browser context mới.
- Dữ liệu: Sản phẩm id 4 'Tai nghe AirPods Pro 2'
- Bước 1: Mở http://localhost:5173/; bấm 'Thêm vào giỏ' trên thẻ 'Tai nghe AirPods Pro 2' đúng một lần. → Có phản hồi trên trang.
- Bước 2: Bấm link 'Giỏ hàng' trên navbar. → Trang giỏ hiển thị 1 dòng.
- Bước 3: Tìm trong ô Số lượng của dòng: nút '+' và nút '-'. → Có đủ 2 nút bấm được.
- Dọn dẹp: Không cần: không tạo user; giỏ web mất khi đóng context.

**TC-FR07-91** — Kiểm tra breadcrumb khi mở trang Giỏ hàng

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.; Khách chưa đăng nhập; browser context mới.
- Dữ liệu: Sản phẩm id 4 'Tai nghe AirPods Pro 2'
- Bước 1: Mở http://localhost:5173/; bấm 'Thêm vào giỏ' trên thẻ 'Tai nghe AirPods Pro 2' đúng một lần. → Có phản hồi trên trang.
- Bước 2: Bấm link 'Giỏ hàng' trên navbar. → Trang giỏ hiển thị 1 dòng.
- Bước 3: Tìm breadcrumb ở đầu nội dung trang. → Có breadcrumb.
- Dọn dẹp: Không cần: không tạo user; giỏ web mất khi đóng context.

**TC-FR07-92** — Kiểm tra highlight link 'Giỏ hàng' trên navbar khi đang ở trang Giỏ hàng

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.; Khách chưa đăng nhập; browser context mới.
- Dữ liệu: Sản phẩm id 4 'Tai nghe AirPods Pro 2'
- Bước 1: Mở http://localhost:5173/; bấm 'Thêm vào giỏ' trên thẻ 'Tai nghe AirPods Pro 2' đúng một lần. → Có phản hồi trên trang.
- Bước 2: Bấm link 'Giỏ hàng' trên navbar. → Trang giỏ hiển thị 1 dòng.
- Bước 3: So kiểu hiển thị link 'Giỏ hàng' với các link khác trên navbar (màu, gạch chân, nền, font). → Link 'Giỏ hàng' khác biệt.
- Dọn dẹp: Không cần: không tạo user; giỏ web mất khi đóng context.

**TC-FR07-93** — Kiểm tra ký hiệu ₫ và phân cách hàng nghìn khi xem giá trên trang chủ, trang chi tiết và trang giỏ

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.; Khách chưa đăng nhập; browser context mới.
- Dữ liệu: Sản phẩm id 4 'Tai nghe AirPods Pro 2'
- Bước 1: Mở http://localhost:5173/; đọc giá trên thẻ 'Tai nghe AirPods Pro 2'. → Giá hiển thị.
- Bước 2: Bấm 'Xem chi tiết' trên thẻ đó; đọc giá. → Giá hiển thị.
- Bước 3: Bấm link 'EShop' → 'Thêm vào giỏ' trên thẻ đó một lần → link 'Giỏ hàng'; đọc Đơn giá, Thành tiền, Tổng cộng. → Các số tiền hiển thị.
- Dọn dẹp: Không cần: không tạo user; giỏ web mất khi đóng context.

**TC-FR07-94** — Kiểm tra thuộc tính alt khi xem ảnh sản phẩm trên trang chủ và trang chi tiết

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.; Khách chưa đăng nhập; browser context mới.
- Dữ liệu: Sản phẩm id 4 'Tai nghe AirPods Pro 2'
- Bước 1: Mở http://localhost:5173/; đọc thuộc tính alt của mọi ảnh sản phẩm. → Đọc được alt.
- Bước 2: Bấm 'Xem chi tiết' trên thẻ 'Tai nghe AirPods Pro 2'; đọc alt của ảnh lớn. → Đọc được alt.
- Bước 3: Bấm link 'EShop' → 'Thêm vào giỏ' → link 'Giỏ hàng'; nếu trang giỏ có ảnh sản phẩm thì đọc alt. → Ghi nhận có/không có ảnh.
- Dọn dẹp: Không cần: không tạo user; giỏ web mất khi đóng context.

### Truy vết yêu cầu ↔ test case
| Yêu cầu | Test case | Số TC |
|---|---|---|
| FR-07.1 | TC-FR07-02 | 1 |
| FR-07.2 | TC-FR07-05, TC-FR07-06, TC-FR07-07, TC-FR07-90 | 4 |
| FR-07.3 | TC-FR07-03, TC-FR07-04, TC-FR07-21 | 3 |
| FR-07.4 | TC-FR07-07, TC-FR07-08, TC-FR07-09 | 3 |
| FR-07.5 | TC-FR07-01, TC-FR07-02 | 2 |
| FR-07.6 | TC-FR07-02, TC-FR07-04, TC-FR07-05, TC-FR07-06, TC-FR07-08 | 5 |
| FR-07.7 | TC-FR07-01 | 1 |
| FR-06.2 | TC-FR07-02, TC-FR07-07, TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13, TC-FR07-20, TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35 | 13 |
| FR-06.3 | TC-FR07-02, TC-FR07-03, TC-FR07-10 | 3 |
| FR-08.1 | TC-FR07-01, TC-FR07-22 | 2 |
| FR-21.3 | TC-FR07-02, TC-FR07-93 | 2 |
| FR-23.1 | TC-FR07-92 | 1 |
| FR-23.2 | TC-FR07-01, TC-FR07-02, TC-FR07-03, TC-FR07-04, TC-FR07-05, TC-FR07-06, TC-FR07-08 | 7 |
| FR-23.4 | TC-FR07-91 | 1 |
| FR-24.1 | TC-FR07-02, TC-FR07-04 | 2 |
| FR-24.2 | TC-FR07-08, TC-FR07-09 | 2 |
| FR-24.3 | TC-FR07-01 | 1 |
| FR-24.4 | TC-FR07-94 | 1 |
| API-CART | TC-FR07-20, TC-FR07-21, TC-FR07-22, TC-FR07-23, TC-FR07-30, TC-FR07-31, TC-FR07-32, TC-FR07-33, TC-FR07-34, TC-FR07-35, TC-FR07-36, TC-FR07-37, TC-FR07-38, TC-FR07-39 | 14 |
| SEC-02 | TC-FR07-20, TC-FR07-38, TC-FR07-39 | 3 |
| SEC-04 | TC-FR07-23 | 1 |

### Giả định khi đặc tả chưa nói rõ
- B0a (độc lập, đã chốt từ phiên thảo luận): mỗi case dùng user riêng tạo qua POST /api/register với email chứa {ts}, đăng nhập lấy token riêng → userCarts[userId] riêng (server.js dòng 14, 291–293). Case UI chạy trong browser context mới (giỏ web là state React, rỗng khi mở trang).
- B0b (oracle tương đối, đã chốt): oracle so giỏ trước/sau trong chính case (số dòng, số lượng, Thành tiền, Tổng cộng) — không giả định giỏ rỗng tuyệt đối ngoài tiền điều kiện của case.
- B0c (cleanup 2 lớp, như A19): lớp 1 — dữ liệu riêng {ts} + oracle tương đối nên case không phụ thuộc cleanup; lớp 2 — cuối suite xoá user test bằng DELETE /api/admin/users/:id (token admin); khởi động lại backend xoá toàn bộ userCarts và seed lại CSDL.
- B0d (quan sát, không phải yêu cầu): giỏ web nằm trong state React, không gọi /api/cart và không lưu localStorage (CartContext.jsx dòng 6; grep 'api/cart' trong frontend-web không có kết quả) → tải lại trang/page.goto làm mất giỏ. Script UI phải điều hướng bằng link trong app sau khi đã thêm hàng.
- B1 (cận trên Số lượng) (SV chốt 2026-10-20): KHÔNG có cận trên. Lý do: SRS chỉ quy định ≥ 1 (FR-06). BVA phía trên dùng 1 đại diện 'giá trị lớn' hợp lệ thay cho UB/UB±1.
- B2 (Số lượng không hợp lệ khi thêm) (SV chốt 2026-10-20): oracle từ chối = giỏ không đổi (số dòng, Số lượng, Tổng cộng, badge). Không yêu cầu thông báo lỗi — lý do: FR-06 chỉ nói 'chỉ nhận số nguyên dương', không yêu cầu thông báo. Bỏ EC52 và biến V21; nội dung thông báo (nếu có) chỉ ghi làm Actual.
- B3 (nút '-' khi Số lượng = 1) (SV chốt 2026-10-20): giữ nguyên 1. Lý do: FR-06 'tối thiểu là 1'; xoá dòng phải qua dialog FR-07.4. Ghi chú: SUT chưa thấy nút +/− (Cart.jsx dòng 47) → xử lý theo quy tắc A17 ở bước 3 (1 case kiểm sự tồn tại, case phụ thuộc → Blocked).
- B4 (Thành tiền và Tổng cộng) (AI đề xuất, chờ SV chốt): SRS không ghi công thức. Nguồn gợi ý — thông lệ: Thành tiền = Đơn giá × Số lượng; Tổng cộng = Σ Thành tiền các dòng; FR-08 'tổng tiền tính tự động từ giỏ hàng'.
- B5 ('cùng một sản phẩm') (SV chốt 2026-10-20): cùng id = cùng sản phẩm; tách lớp EC9 (thêm lại từ cùng trang) và EC10 (thêm lại từ trang khác) — lý do: hai điểm thêm vào giỏ (Trang chủ 'Thêm vào giỏ', Chi tiết 'Thêm vào giỏ hàng') đều thấy được trên UI.
- B6 (phạm vi FR-06) (SV chốt 2026-10-20): CÓ — ô Số lượng và phản hồi khi thêm (FR-06.2, FR-06.3) nằm trong phạm vi. Bug thuộc FR-06 đặt tiêu đề [FR-06].
- B7 (tầng API) (SV chốt 2026-10-20): CÓ — /api/cart là tầng riêng, suite riêng (UI / API).
- B8 (giá/tên do client gửi ở POST /api/cart) (SV chốt 2026-10-20): giá lấy từ CSDL, không tin giá client — lý do: FR-08 'tổng tiền được tính tự động, không cho phép người dùng chỉnh sửa trực tiếp'. EC16 hợp lệ, oracle = giá CSDL. Tên (EC32) áp dụng tương tự: AI suy rộng từ quyết định về giá, SV xác nhận khi review bước 3.
- B9 (badge 'Giỏ hàng') (SV chốt 2026-10-20): badge đếm TỔNG Số lượng. Giả định của SV, lý do: FR-23 'badge số lượng sản phẩm trong giỏ'. Câu SRS vẫn có thể hiểu là số dòng (số sản phẩm khác nhau) — ghi nhận độ mơ hồ.
- B10 (giữ giỏ khi tải lại trang / đăng nhập / đăng xuất) (SV chốt 2026-10-20): NGOÀI phạm vi — lý do: SRS im lặng. Không phân lớp; procedure UI vẫn tránh tải lại trang giữa chừng (B0d).
- B11 (khách chưa đăng nhập dùng giỏ ở UI) (AI đề xuất, chờ SV chốt): FR-08 chỉ yêu cầu đăng nhập khi thanh toán → đề xuất: khách chưa đăng nhập vẫn thêm/xem/sửa giỏ được. Tầng API: SEC-02 + api_specification §4 yêu cầu Bearer → thiếu/sai token bị từ chối 4xx.
- B12 (nhãn chính xác) (AI đề xuất, chờ SV chốt): FR-07 in đậm 'Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác', 'Tiếp tục mua sắm', 'Tổng cộng'. Đề xuất: so khớp đúng chữ (không phân biệt hoa/thường). 'Nút Xóa sản phẩm' — chữ in đậm nhưng có thể là mô tả chức năng chứ không phải nhãn; cần chốt có so khớp chữ 'Xóa sản phẩm' hay không.
- B13 (định dạng tiền) (AI đề xuất, chờ SV chốt): FR-21 '₫ với định dạng phân cách hàng nghìn' — không nói ký tự phân cách. Nguồn gợi ý — thông lệ vi-VN dùng '.', code dùng toLocaleString() theo locale trình duyệt (Cart.jsx dòng 46, 48, 63). Lựa chọn: chấp nhận '.' hoặc ','; hay bắt buộc '.'.
- B14 (dialog xoá) (AI đề xuất, chờ SV chốt): FR-07/FR-24 chỉ yêu cầu có dialog. Đề xuất: chọn Hủy → giỏ giữ nguyên; chọn Đồng ý → dòng bị xoá, Tổng cộng cập nhật; dialog native (window.confirm) hay modal đều chấp nhận.
- B15 (empty state) (AI đề xuất, chờ SV chốt): 'hình minh họa và thông báo rõ ràng' — oracle đề xuất: có phần tử ảnh/icon (img/svg) và có dòng chữ báo giỏ trống; không cố định nội dung chữ.
- B16 (GUI liên quan) (SV chốt 2026-10-20): có suite TS-GUI riêng, giới hạn trang Giỏ hàng (/cart) và các điểm thêm vào giỏ (Trang chủ /, Chi tiết /product/:id): sự tồn tại nút +/- (A17), breadcrumb, highlight navbar, ký hiệu ₫ + phân cách hàng nghìn, alt ảnh. Không phân lớp.
- B17 (mã lỗi API) (AI đề xuất, chờ SV chốt): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106).
- B18 (sai kiểu / id không tồn tại ở API) (SV chốt 2026-10-20): giữ 4 lớp chỉ có ở tầng API — EC6, EC7 (quantity) và EC12, EC13 (id) — phải bị từ chối 4xx, giỏ không đổi.
- B19 (đại diện id chẵn/lẻ ở API) (SV chốt 2026-10-20): suite TS-DOM-API lấy đại diện cả sản phẩm id chẵn và id lẻ. Đại diện chọn theo code server.js:162 (gray-box), không phải lớp mới.
- B20 (A17/A20 áp cho B_FR07) (AI đề xuất theo quy ước đã chốt từ A_FR01): nút +/- thiếu → TC-FR07-90 (kiểm sự tồn tại) Fail; các case cần bấm +/- → Blocked, case gốc TC-FR07-90. Giỏ ban đầu không dựng được đúng như cột (do lỗi đã có ở case khác) → Blocked, ghi case gốc.

**Tổng:** 32 TC · Not run: 32 · Nguồn: AI 32
