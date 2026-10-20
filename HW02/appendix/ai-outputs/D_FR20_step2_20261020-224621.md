### Phạm vi
Màn hình 'Đăng Ký Tài Khoản' của app mobile (tầng Mobile, chạy tay trên Android thật, Expo Go). Theo D1 = a (gọn): Domain — mỗi lớp không hợp lệ tạo được từ UI một case; lớp con mà chỉ server xử lý lấy 1 đại diện/biến và tham chiếu TC API của A_FR01; BVA chỉ độ dài Mật khẩu (biến client mobile xử lý trước khi gửi, gray-box); GUI FR-22.1–22.4 theo D13 = a ở suite TS-GUI riêng, không phân lớp. Ngoài phạm vi: tầng API (đã phủ ở A_FR01), FR-21, SEC-01, đăng nhập (FR-02), các chức năng mobile khác của FR-20. Mã TC TC-FR20-xx.

### Yêu cầu (test basis)
| Mã | Nội dung |
|---|---|
| FR-20.1 | Ứng dụng Mobile có đầy đủ chức năng Đăng ký (README.md dòng 235: 'Đầy đủ các chức năng: Xem sản phẩm, Đăng nhập, Đăng xuất, Đăng ký, Giỏ hàng, Thanh toán, Hồ sơ, Lịch sử đơn hàng.'). |
| FR-01.1 | Người dùng phải cung cấp Họ Tên (trường bắt buộc). [áp cho mobile theo D2] |
| FR-01.2 | Người dùng phải cung cấp Email (trường bắt buộc). [D2] |
| FR-01.3 | Email phải có định dạng hợp lệ (user@domain.com). [D2] |
| FR-01.4 | Email phải là duy nhất trong hệ thống. [D2] |
| FR-01.5 | Người dùng phải cung cấp Mật khẩu (trường bắt buộc). [D2] |
| FR-01.6 | Mật khẩu tối thiểu 8 ký tự. [D2] |
| FR-01.7a | Mật khẩu có ít nhất 1 chữ hoa. [D2] |
| FR-01.7b | Mật khẩu có ít nhất 1 chữ thường. [D2] |
| FR-01.7c | Mật khẩu có ít nhất 1 chữ số. [D2] |
| FR-01.8 | Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &. [D2] |
| FR-01.9 | Phải có trường Xác nhận mật khẩu; hệ thống từ chối nếu Mật khẩu và Xác nhận mật khẩu không khớp. [D2] |
| FR-01.10 | Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập (mobile: màn hình 'Đăng Nhập'). [D2, D11] |
| FR-22.1 | Trường bắt buộc có ký hiệu * bên cạnh nhãn. [phạm vi theo D13] |
| FR-22.2 | Trường Email phải dùng type="email" (mobile: cách hiểu theo D13). [D13] |
| FR-22.3 | Trường Mật khẩu phải dùng type="password" (không hiển thị rõ) (mobile: cách hiểu theo D13). [D13] |
| FR-22.4 | Thông báo lỗi phải xuất hiện trên nút submit, không phải bên dưới. [D13] |

### Bước 1 — Biến vào/ra
| Mã | Biến | Vào/Ra | Nguồn | Kiểu | Ràng buộc (đặc tả) | Ghi chú |
|---|---|---|---|---|---|---|
| V1 | Họ Tên | Vào | Mobile: ô nhãn 'Họ Tên' (App.js dòng 804–809; TextInput không đặt keyboardType/autoCapitalize/secureTextEntry) → body.name của POST /api/register (dòng 226) | string | Bắt buộc (FR-01.1). SRS không nêu độ dài/tập ký tự → D3. | Tương ứng A_FR01 V1. |
| V2 | Email | Vào | Mobile: ô nhãn 'Email' (App.js dòng 810–816; autoCapitalize="none", không đặt keyboardType) → body.email (dòng 227) | string | Bắt buộc (FR-01.2); định dạng user@domain.com (FR-01.3, D4). Loại bàn phím → D13. | Tương ứng A_FR01 V2. |
| V3 | Email đã tồn tại trong hệ thống | Vào | Trạng thái dữ liệu server: tài khoản seed test@eshop.com, admin@eshop.com (README.md dòng 23–24) + tài khoản do case tạo | boolean (trạng thái CSDL) | Email nhập phải chưa tồn tại (FR-01.4). Cách so sánh → D5. | Tương ứng A_FR01 V3. |
| V4 | Mật khẩu | Vào | Mobile: ô nhãn 'Mật khẩu' (App.js dòng 817–823; secureTextEntry); chữ gợi ý 'Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt.' (dòng 824–827) → body.password (dòng 228) | string | Bắt buộc (FR-01.5); độ dài ≥ 8, không có cận trên (FR-01.6, D6); ≥1 chữ hoa (FR-01.7a), ≥1 chữ thường (FR-01.7b) (D8); ≥1 chữ số (FR-01.7c); ≥1 ký tự thuộc {@ $ ! % * ? &} (FR-01.8, D7). | Tương ứng A_FR01 V4. |
| V5 | Xác nhận mật khẩu | Vào | SRS FR-01 (README.md dòng 35). Màn 'Đăng Ký Tài Khoản' (App.js dòng 797–837) chỉ có ba ô Họ Tên, Email, Mật khẩu; body gửi đi không có trường tương ứng (dòng 225–229) | string | Phải bằng đúng V4 (FR-01.9, D9). | Tương ứng A_FR01 V5. Quan sát mã nguồn: không có ô. Chưa kết luận lỗi; xác nhận khi chạy (bước 6) theo D9. |
| V6 | Cách nhập giá trị trên điện thoại | Vào | Bàn phím ảo Android (gõ, dán, tự viết hoa, tự sửa, gợi ý từ); khoảng trắng gõ bằng phím cách | enum (theo D12) | SRS im lặng. Theo D12 = a: không phải biến phân lớp — giá trị case là chuỗi thực sự trong ô ngay trước khi bấm 'Đăng Ký'; gõ/dán cùng chuỗi là cùng lớp. | Biến mới của mobile, A không có. |
| V7 | Thông báo trên app sau khi bấm 'Đăng Ký' | Ra | Mobile: chữ lỗi (errorBoxText) phía trên ô 'Họ Tên' (App.js dòng 801–803); hộp thoại Alert (dòng 233); kênh khác nếu xuất hiện khi chạy (toast…) — ghi mọi kênh | message \| none (theo kênh) | Bị từ chối → theo D10; thành công → SRS im lặng về thông báo (D11), chỉ ghi Actual. Vị trí thông báo lỗi chỉ kiểm ở case FR-22.4 (D13). | Tương ứng A_FR01 V6 (A16 bong bóng HTML5 không áp dụng). |
| V8 | Màn hình sau khi bấm 'Đăng Ký' | Ra | Mobile: tiêu đề màn hình — 'Đăng Nhập' (App.js dòng 762) hoặc 'Đăng Ký Tài Khoản' (dòng 800); không có URL | enum {màn Đăng Nhập, màn Đăng Ký Tài Khoản} | Thành công → màn 'Đăng Nhập' (FR-01.10); bị từ chối → ở lại màn 'Đăng Ký Tài Khoản' (D10). | Tương ứng A_FR01 V7 (URL /login, /register). |
| V9 | Tài khoản phía server | Ra | Quan sát theo D11: trang admin 'Quản lý Người dùng' (frontend-admin App.jsx dòng 881–892: ID, Email, Role, Số ĐT); đăng nhập thử trên app (header 'Chào, <tên>', App.js dòng 432); hoặc API (D11 c) | enum {tạo đúng 1 tài khoản, không tạo} | Hợp lệ → tạo đúng 1 tài khoản với email đã nhập, đăng nhập được bằng mật khẩu đã nhập, Họ Tên đúng; không hợp lệ → danh sách người dùng SAU = TRƯỚC (D10). | Tương ứng A_FR01 V9. A_FR01 V8 (phản hồi API) không dùng (D1 = a). |

### Bước 2 — Complete Set of Partitions
| EC | Biến | Lớp tương đương | Hợp lệ | Hướng dẫn | Yêu cầu | Ghi chú |
|---|---|---|---|---|---|---|
| EC1 | Họ Tên | Không rỗng sau khi bỏ khoảng trắng (đại diện có chữ tiếng Việt có dấu, vd 'Nguyễn Văn Ánh') | ✔ | must-be | FR-01.1, D3 | FR-01.1, D3. Gộp A EC1 (Latin không dấu) + EC2 (có dấu); A tách vì mã hoá/lưu trữ phía server. (gray-box) Tiền đề gộp: giá trị trong ô (D12 = a) = giá trị gửi trong body POST /api/register. Ô 'Họ Tên' là ô có kiểm soát value={registerName} (App.js dòng 807), onChangeText={setRegisterName} (dòng 808) lưu nguyên chuỗi; handleRegister không gán lại registerName (dòng 209–219 chỉ kiểm registerPassword) và gửi name: registerName (dòng 226) qua JSON.stringify (dòng 225) → client không trim/biến đổi; việc phân biệt các lớp con do server xử lý → theo D1 = a lấy 1 đại diện. Tham chiếu A: TC-FR01-28, TC-FR01-29 (API). |
| EC2 | Họ Tên | Rỗng hoặc chỉ gồm khoảng trắng (vd '' hoặc '␣␣␣') | ✘ | must-be | FR-01.1, D3 | FR-01.1 bắt buộc; D3: chỉ khoảng trắng coi như rỗng. A tách EC3/EC4 vì required của HTML5 chặn '' nhưng không chặn chuỗi toàn khoảng trắng — mobile không có HTML5. (gray-box) Tiền đề gộp: giá trị trong ô (D12 = a) = giá trị gửi trong body POST /api/register. Ô 'Họ Tên' là ô có kiểm soát value={registerName} (App.js dòng 807), onChangeText={setRegisterName} (dòng 808) lưu nguyên chuỗi; handleRegister không gán lại registerName (dòng 209–219 chỉ kiểm registerPassword) và gửi name: registerName (dòng 226) qua JSON.stringify (dòng 225) → client không trim/biến đổi; việc phân biệt các lớp con do server xử lý → theo D1 = a lấy 1 đại diện. Tham chiếu A: TC-FR01-32 (rỗng), TC-FR01-33 (chỉ khoảng trắng), TC-FR01-79 (API). |
| EC3 | Email | Đúng định dạng <local>@<domain>.<tld> (vd 'newuser@domain.com'); kể cả có khoảng trắng đầu/cuối (D5 cắt trước khi xử lý) | ✔ | must-be | FR-01.2, FR-01.3, D4, D5 | FR-01.2, FR-01.3, D4, D5. Gộp A EC7 + EC8 (khoảng trắng đầu/cuối). (gray-box) Tiền đề gộp: giá trị trong ô (D12 = a) = giá trị gửi trong body POST /api/register. Ô 'Email' là ô có kiểm soát value={registerEmail} (App.js dòng 813), onChangeText={setRegisterEmail} (dòng 814) lưu nguyên chuỗi; autoCapitalize="none" (dòng 815) chỉ tác động bàn phím lúc nhập; handleRegister không gán lại registerEmail (dòng 209–219) và gửi email: registerEmail (dòng 227) qua JSON.stringify (dòng 225) → client không trim/biến đổi; việc phân biệt các lớp con do server xử lý → theo D1 = a lấy 1 đại diện. Tham chiếu A: TC-FR01-28 (EC7), TC-FR01-30 (EC8) (API). |
| EC4 | Email | Rỗng (0 ký tự) | ✘ | must-be | FR-01.2 | FR-01.2 bắt buộc. Tách khỏi lớp sai định dạng vì vi phạm điều khoản khác (bắt buộc vs định dạng). Tham chiếu A: TC-FR01-34 (API). |
| EC5 | Email | Sai định dạng theo D4 (đại diện: không có '@', vd 'newuserdomain.com') | ✘ | must-be | FR-01.3, D4 | FR-01.3, D4. Gộp A EC10–EC15 (không '@', nhiều '@', local rỗng, domain rỗng, domain không có '.', khoảng trắng bên trong); A tách theo bộ kiểm HTML5 type=email / regex client / backend — mobile không có HTML5. (gray-box) Tiền đề gộp: giá trị trong ô (D12 = a) = giá trị gửi trong body POST /api/register. Ô 'Email' là ô có kiểm soát value={registerEmail} (App.js dòng 813), onChangeText={setRegisterEmail} (dòng 814) lưu nguyên chuỗi; autoCapitalize="none" (dòng 815) chỉ tác động bàn phím lúc nhập; handleRegister không gán lại registerEmail (dòng 209–219) và gửi email: registerEmail (dòng 227) qua JSON.stringify (dòng 225) → client không trim/biến đổi; việc phân biệt các lớp con do server xử lý → theo D1 = a lấy 1 đại diện. Tham chiếu A: TC-FR01-35, 36, 37, 38, 39, 40 (API). |
| EC6 | Email đã tồn tại trong hệ thống | Email chưa tồn tại theo cách so sánh của D5 (gồm cả chỉ khác hoa/thường ở phần local, vd 'Test@eshop.com' khi đã có 'test@eshop.com') | ✔ | set | FR-01.4, D5 | FR-01.4, D5. Gộp A EC18 + EC19. (gray-box) Tiền đề gộp: giá trị trong ô (D12 = a) = giá trị gửi trong body POST /api/register. Ô 'Email' là ô có kiểm soát value={registerEmail} (App.js dòng 813), onChangeText={setRegisterEmail} (dòng 814) lưu nguyên chuỗi; autoCapitalize="none" (dòng 815) chỉ tác động bàn phím lúc nhập; handleRegister không gán lại registerEmail (dòng 209–219) và gửi email: registerEmail (dòng 227) qua JSON.stringify (dòng 225) → client không trim/biến đổi; việc phân biệt các lớp con do server xử lý → theo D1 = a lấy 1 đại diện. Tham chiếu A: TC-FR01-28 (EC18), TC-FR01-31 (EC19) (API). |
| EC7 | Email đã tồn tại trong hệ thống | Trùng email đã có theo D5: trùng chính xác, trùng sau khi cắt khoảng trắng đầu/cuối, hoặc chỉ khác hoa/thường ở phần domain (đại diện: 'test@eshop.com') | ✘ | set | FR-01.4, D5 | FR-01.4, D5. Gộp A EC20 + EC21; phần 'chỉ khác hoa/thường ở phần domain' suy ra từ D5 (A3 bản cuối, bước 5 của A, 8d837f1). (gray-box) Tiền đề gộp: giá trị trong ô (D12 = a) = giá trị gửi trong body POST /api/register. Ô 'Email' là ô có kiểm soát value={registerEmail} (App.js dòng 813), onChangeText={setRegisterEmail} (dòng 814) lưu nguyên chuỗi; autoCapitalize="none" (dòng 815) chỉ tác động bàn phím lúc nhập; handleRegister không gán lại registerEmail (dòng 209–219) và gửi email: registerEmail (dòng 227) qua JSON.stringify (dòng 225) → client không trim/biến đổi; việc phân biệt các lớp con do server xử lý → theo D1 = a lấy 1 đại diện. Tham chiếu A: TC-FR01-41 (trùng chính xác), TC-FR01-42 (trùng sau cắt khoảng trắng) (API); A không có TC API của AI cho phần domain. |
| EC8 | Mật khẩu | Độ dài ≥ 8 ký tự (các điều kiện khác thoả) | ✔ | range | FR-01.6, D6 | FR-01.6. Chỉ có cận dưới LB = 8, không có cận trên (D6, no_upper_bound) → một lớp không hợp lệ phía dưới. (gray-box) client mobile có bước kiểm Mật khẩu trước khi gửi (App.js dòng 211–219) và server cũng xử lý → giữ đủ lớp con như A cho tầng Mobile (D1 = a: BVA/phân lớp đủ cho biến client xử lý). Tham chiếu A: TC-FR01-83, 84, 85 (API). |
| EC9 | Mật khẩu | Độ dài 1–7 ký tự (các điều kiện khác thoả) | ✘ | range | FR-01.6 | FR-01.6. Tham chiếu A: TC-FR01-43, 82 (API). |
| EC10 | Mật khẩu | Rỗng (0 ký tự) | ✘ | must-be | FR-01.5 | FR-01.5 bắt buộc. Tách khỏi lớp 1–7 ký tự vì vi phạm điều khoản khác (bắt buộc vs độ dài). Tham chiếu A: TC-FR01-44 (API). |
| EC11 | Mật khẩu | Có ≥ 1 chữ hoa A–Z | ✔ | must-be | FR-01.7a, D8 | FR-01.7a, D8. |
| EC12 | Mật khẩu | Không có chữ hoa nào (các điều kiện khác thoả) | ✘ | must-be | FR-01.7a | FR-01.7a. Tham chiếu A: TC-FR01-45 (API). |
| EC13 | Mật khẩu | Chữ hoa duy nhất là chữ có dấu tiếng Việt, vd 'Ê' (các điều kiện khác thoả) | ✘ | split | FR-01.7a, D8 | FR-01.7a, D8: chỉ A–Z tính là chữ hoa. Tách vì bộ kiểm theo Unicode và theo [A-Z] cho kết quả khác nhau (như A EC27). (gray-box) client mobile có bước kiểm Mật khẩu trước khi gửi (App.js dòng 211–219) và server cũng xử lý → giữ đủ lớp con như A cho tầng Mobile (D1 = a: BVA/phân lớp đủ cho biến client xử lý). Tham chiếu A: TC-FR01-46 (API). |
| EC14 | Mật khẩu | Có ≥ 1 chữ thường a–z | ✔ | must-be | FR-01.7b, D8 | FR-01.7b, D8. |
| EC15 | Mật khẩu | Không có chữ thường nào (các điều kiện khác thoả) | ✘ | must-be | FR-01.7b | FR-01.7b. Tham chiếu A: TC-FR01-47 (API). |
| EC16 | Mật khẩu | Chữ thường duy nhất là chữ có dấu tiếng Việt, vd 'ê' (các điều kiện khác thoả) | ✘ | split | FR-01.7b, D8 | FR-01.7b, D8, cùng lý do lớp chữ hoa có dấu (như A EC30). (gray-box) client mobile có bước kiểm Mật khẩu trước khi gửi (App.js dòng 211–219) và server cũng xử lý → giữ đủ lớp con như A cho tầng Mobile (D1 = a: BVA/phân lớp đủ cho biến client xử lý). Tham chiếu A: TC-FR01-48 (API). |
| EC17 | Mật khẩu | Có ≥ 1 chữ số 0–9 | ✔ | must-be | FR-01.7c | FR-01.7c. |
| EC18 | Mật khẩu | Không có chữ số nào (các điều kiện khác thoả) | ✘ | must-be | FR-01.7c | FR-01.7c. Tham chiếu A: TC-FR01-49 (API). |
| EC19 | Mật khẩu | Có ≥ 1 ký tự thuộc {@ $ ! % * ? &}, không có ký tự đặc biệt ngoài tập | ✔ | set | FR-01.8 | FR-01.8. |
| EC20 | Mật khẩu | Có ≥ 1 ký tự thuộc tập và thêm ký tự đặc biệt ngoài tập (vd '!' và '#') | ✔ | split | FR-01.8, D7 | D7: ký tự ngoài tập được phép xuất hiện thêm. Tách vì bộ kiểm dạng whitelist sẽ từ chối lớp này (như A EC34). (gray-box) client mobile có bước kiểm Mật khẩu trước khi gửi (App.js dòng 211–219) và server cũng xử lý → giữ đủ lớp con như A cho tầng Mobile (D1 = a: BVA/phân lớp đủ cho biến client xử lý). Tham chiếu A: TC-FR01-29 (API). |
| EC21 | Mật khẩu | Không có ký tự đặc biệt nào (các điều kiện khác thoả) | ✘ | set | FR-01.8 | FR-01.8. Tham chiếu A: TC-FR01-50 (API). |
| EC22 | Mật khẩu | Chỉ có ký tự đặc biệt ngoài tập, vd '#', '^', '-' (các điều kiện khác thoả) | ✘ | set | FR-01.8, D7 | D7: tập đóng → coi như thiếu ký tự đặc biệt; lớp 'ngoài tập' theo hướng dẫn set. (gray-box) client mobile có bước kiểm Mật khẩu trước khi gửi (App.js dòng 211–219) và server cũng xử lý → giữ đủ lớp con như A cho tầng Mobile (D1 = a: BVA/phân lớp đủ cho biến client xử lý). Tham chiếu A: TC-FR01-51 (API). |
| EC23 | Xác nhận mật khẩu | Khớp chính xác với Mật khẩu | ✔ | must-be | FR-01.9, D9 | FR-01.9, D9. Màn hình không có ô (V5 note) → xử lý theo D9. |
| EC24 | Xác nhận mật khẩu | Không khớp: khác Mật khẩu ít nhất một ký tự (không chỉ khác hoa/thường), hoặc bỏ trống | ✘ | must-be | FR-01.9, D9 | FR-01.9; D9: 'bỏ trống = không khớp' → bỏ trống và khác ít nhất một ký tự cho cùng Expected (bị từ chối) → gộp. |
| EC25 | Xác nhận mật khẩu | Chỉ khác Mật khẩu ở chữ hoa/thường (vd 'Abcd1234!' và 'abcd1234!') | ✘ | split | FR-01.9, D9 | D9: so khớp phân biệt hoa/thường. Tách vì so sánh không phân biệt hoa/thường sẽ cho là khớp (như A EC42). |
| EC26 | Cách nhập giá trị trên điện thoại | Giá trị của ô = chuỗi thực sự trong ô ngay trước khi bấm 'Đăng Ký' (gõ bằng bàn phím ảo hoặc dán) | ✔ | must-be | D12 | D12 = a: cách nhập không phải biến phân lớp; một lớp duy nhất để mọi case ghi nhận. Không có lớp không hợp lệ (check_domain sẽ cảnh báo – chủ ý). |
| EC27 | Thông báo trên app sau khi bấm 'Đăng Ký' | Không có thông báo lỗi ở mọi kênh (thông báo thành công, nếu có, chỉ ghi Actual) | ✔ | output | FR-20.1, D11 | Khi mọi đầu vào hợp lệ. D11: SRS im lặng về thông báo thành công. |
| EC28 | Thông báo trên app sau khi bấm 'Đăng Ký' | Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại, toast…) | ✘ | output | D10 | D10. Nội dung chữ chỉ ghi Actual, không phân loại theo chữ của SUT; vị trí chỉ kiểm ở case FR-22.4 (D13). |
| EC29 | Màn hình sau khi bấm 'Đăng Ký' | Chuyển sang màn 'Đăng Nhập' | ✔ | output | FR-01.10, D11 | FR-01.10, D11. |
| EC30 | Màn hình sau khi bấm 'Đăng Ký' | Ở lại màn 'Đăng Ký Tài Khoản' | ✘ | output | D10 | D10. |
| EC31 | Tài khoản phía server | Tạo đúng 1 tài khoản mới: thêm đúng 1 dòng có Email đã nhập ở trang admin 'Quản lý Người dùng'; đăng nhập được bằng mật khẩu đã nhập; header hiển thị 'Chào, <Họ Tên đã nhập>' | ✔ | output | FR-20.1, D11 | FR-20.1, FR-01.10 (thành công), D11. |
| EC32 | Tài khoản phía server | Không tạo tài khoản: danh sách người dùng SAU = TRƯỚC | ✘ | output | D10, D11 | D10, D11. |

### Bước 3a — Test Cases Providing Coverage of Partitions
| EC | Lớp | Test case phủ |
|---|---|---|
| EC1 | Không rỗng sau khi bỏ khoảng trắng (đại diện có chữ tiếng Việt có dấu, vd 'Nguyễn Văn Ánh') | ⚠ chưa phủ |
| EC2 | Rỗng hoặc chỉ gồm khoảng trắng (vd '' hoặc '␣␣␣') | ⚠ chưa phủ |
| EC3 | Đúng định dạng <local>@<domain>.<tld> (vd 'newuser@domain.com'); kể cả có khoảng trắng đầu/cuối (D5 cắt trước khi xử lý) | ⚠ chưa phủ |
| EC4 | Rỗng (0 ký tự) | ⚠ chưa phủ |
| EC5 | Sai định dạng theo D4 (đại diện: không có '@', vd 'newuserdomain.com') | ⚠ chưa phủ |
| EC6 | Email chưa tồn tại theo cách so sánh của D5 (gồm cả chỉ khác hoa/thường ở phần local, vd 'Test@eshop.com' khi đã có 'test@eshop.com') | ⚠ chưa phủ |
| EC7 | Trùng email đã có theo D5: trùng chính xác, trùng sau khi cắt khoảng trắng đầu/cuối, hoặc chỉ khác hoa/thường ở phần domain (đại diện: 'test@eshop.com') | ⚠ chưa phủ |
| EC8 | Độ dài ≥ 8 ký tự (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC9 | Độ dài 1–7 ký tự (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC10 | Rỗng (0 ký tự) | ⚠ chưa phủ |
| EC11 | Có ≥ 1 chữ hoa A–Z | ⚠ chưa phủ |
| EC12 | Không có chữ hoa nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC13 | Chữ hoa duy nhất là chữ có dấu tiếng Việt, vd 'Ê' (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC14 | Có ≥ 1 chữ thường a–z | ⚠ chưa phủ |
| EC15 | Không có chữ thường nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC16 | Chữ thường duy nhất là chữ có dấu tiếng Việt, vd 'ê' (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC17 | Có ≥ 1 chữ số 0–9 | ⚠ chưa phủ |
| EC18 | Không có chữ số nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC19 | Có ≥ 1 ký tự thuộc {@ $ ! % * ? &}, không có ký tự đặc biệt ngoài tập | ⚠ chưa phủ |
| EC20 | Có ≥ 1 ký tự thuộc tập và thêm ký tự đặc biệt ngoài tập (vd '!' và '#') | ⚠ chưa phủ |
| EC21 | Không có ký tự đặc biệt nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC22 | Chỉ có ký tự đặc biệt ngoài tập, vd '#', '^', '-' (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC23 | Khớp chính xác với Mật khẩu | ⚠ chưa phủ |
| EC24 | Không khớp: khác Mật khẩu ít nhất một ký tự (không chỉ khác hoa/thường), hoặc bỏ trống | ⚠ chưa phủ |
| EC25 | Chỉ khác Mật khẩu ở chữ hoa/thường (vd 'Abcd1234!' và 'abcd1234!') | ⚠ chưa phủ |
| EC26 | Giá trị của ô = chuỗi thực sự trong ô ngay trước khi bấm 'Đăng Ký' (gõ bằng bàn phím ảo hoặc dán) | ⚠ chưa phủ |
| EC27 | Không có thông báo lỗi ở mọi kênh (thông báo thành công, nếu có, chỉ ghi Actual) | ⚠ chưa phủ |
| EC28 | Có thông báo lỗi ở ít nhất một kênh (chữ trên màn hình, hộp thoại, toast…) | ⚠ chưa phủ |
| EC29 | Chuyển sang màn 'Đăng Nhập' | ⚠ chưa phủ |
| EC30 | Ở lại màn 'Đăng Ký Tài Khoản' | ⚠ chưa phủ |
| EC31 | Tạo đúng 1 tài khoản mới: thêm đúng 1 dòng có Email đã nhập ở trang admin 'Quản lý Người dùng'; đăng nhập được bằng mật khẩu đã nhập; header hiển thị 'Chào, <Họ Tên đã nhập>' | ⚠ chưa phủ |
| EC32 | Không tạo tài khoản: danh sách người dùng SAU = TRƯỚC | ⚠ chưa phủ |

### Truy vết yêu cầu ↔ test case
Sinh tự động: yêu cầu của một TC = hợp các yêu cầu của các EC mục tiêu (ec_target; TC không có ec_target thì dùng EC phủ) theo cột Yêu cầu ở bảng Bước 2, cộng với trường requirements và assumptions của TC (dùng cho case GUI không gắn EC). Mã giả định (B…) hiện thành dòng riêng.

| Yêu cầu | Test case | Số TC |
|---|---|---|
| FR-20.1 | ⚠ | 0 |
| FR-01.1 | ⚠ | 0 |
| FR-01.2 | ⚠ | 0 |
| FR-01.3 | ⚠ | 0 |
| FR-01.4 | ⚠ | 0 |
| FR-01.5 | ⚠ | 0 |
| FR-01.6 | ⚠ | 0 |
| FR-01.7a | ⚠ | 0 |
| FR-01.7b | ⚠ | 0 |
| FR-01.7c | ⚠ | 0 |
| FR-01.8 | ⚠ | 0 |
| FR-01.9 | ⚠ | 0 |
| FR-01.10 | ⚠ | 0 |
| FR-22.1 | ⚠ | 0 |
| FR-22.2 | ⚠ | 0 |
| FR-22.3 | ⚠ | 0 |
| FR-22.4 | ⚠ | 0 |

### Giả định khi đặc tả chưa nói rõ
- D0 (độc lập, trạng thái ban đầu, dữ liệu) [loại: quy trình · truy vết: không · căn cứ: CLAUDE.md (backend khởi động lại → CSDL seed lại), tiền lệ A13/A19 · SV chốt 2026-10-20, chấp nhận đề xuất AI]: đầu mỗi case tải lại app trong Expo Go (Reload) → màn hình chủ, chưa đăng nhập, rồi vào 'Đăng nhập' (header) → 'Đăng ký ngay'; ba ô trống. Lý do phải tải lại (gray-box, chỉ để viết quy trình): state của form nằm trong component App (App.js dòng 42–46), không thấy chỗ đặt lại khi rời/vào lại màn hình. Mỗi case dùng email riêng có hậu tố {ts}; email đã tồn tại dùng tài khoản seed test@eshop.com. Oracle tương đối (danh sách người dùng SAU so với TRƯỚC trong chính case). Restart backend xoá mọi tài khoản đã tạo.
- D1 (PHẠM VI) [loại: phạm vi · truy vết: không · căn cứ: FR-20 dòng 235; mục tiêu 'ít case vì chạy tay'; dữ kiện gray-box: app mobile gọi cùng endpoint POST /api/register với body {name, email, password} như web (App.js dòng 222–229) · SV chốt 2026-10-20, phương án a]: GỌN — chỉ tầng Mobile (UI app); Domain: mỗi lớp không hợp lệ tạo được từ UI một case, các lớp con mà chỉ server xử lý (vd nhiều dạng sai định dạng email) lấy 1 đại diện/biến và tham chiếu case API của A_FR01 thay vì lặp; BVA chỉ biến mà tầng client mobile xử lý trước khi gửi (gray-box: App.js dòng 211–219 chỉ kiểm Mật khẩu → BVA độ dài Mật khẩu quanh LB = 8); GUI (theo D13) ≤ 5 case. Ước tính ~25–30 EC, ~18–22 TC, ~1,3–1,5 giờ chạy tay. Ngoài phạm vi: tầng API, FR-21, SEC-01, đăng nhập (FR-02), các chức năng mobile khác của FR-20 — lý do SV: ít case vì chạy tay; tầng API đã phủ ở A; mobile gọi cùng POST /api/register (App.js 222–229, chỉ dùng để chọn đại diện).
- D2 (FR-20 áp FR-01 cho mobile) [loại: quyết định Expected · truy vết: có · căn cứ: FR-20 dòng 235 'Đầy đủ các chức năng: … Đăng ký …'; FR-01 dòng 30–36 · SV chốt 2026-10-20, phương án a]: chức năng Đăng ký trên mobile phải tuân toàn bộ FR-01 (dòng 32–36) như web → Expected của mọi lớp lấy từ FR-01 — lý do SV: FR-20 yêu cầu chức năng Đăng ký trên mobile; luật của chức năng này định nghĩa ở FR-01; SRS không ghi ngoại lệ cho mobile.
- D3 (kế thừa A1 – Họ Tên) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 32 'phải cung cấp' · SV chốt 2026-10-20, phương án a]: chỉ rỗng là không hợp lệ; chuỗi chỉ gồm khoảng trắng coi như rỗng (bị từ chối); không có cận trên độ dài — lý do SV: giữ nguyên như A.
- D4 (kế thừa A2 – Email định dạng) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 33 chỉ đưa mẫu 'user@domain.com' · SV chốt 2026-10-20, phương án a]: hợp lệ = <local>@<domain>.<tld> (đúng một '@', local không rỗng, domain có ít nhất một '.', không rỗng hai bên dấu chấm). Khác A: trên mobile không có trình duyệt nên quy tắc HTML5 (tham chiếu phụ của A2) không áp dụng; không có cận trên độ dài — lý do SV: giữ nguyên như A.
- D5 (kế thừa A3 – Email duy nhất) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 33 'là duy nhất'; A3 bản cuối (A_FR01, 8d837f1) · SV chốt 2026-10-20, phương án b]: A3 (Email – duy nhất): Email so sánh sau khi cắt khoảng trắng đầu/cuối; phần local phân biệt hoa/thường, phần domain không phân biệt (RFC 5321 §2.4). SV sửa ở bước 5. — lý do SV: Kế thừa A3 bản cuối (SV sửa ở bước 5 của A, 8d837f1); giữ cùng luật với A để so sánh web vs mobile.
- D6 (kế thừa A4 – Mật khẩu độ dài) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 34 'Tối thiểu 8 ký tự' · SV chốt 2026-10-20, phương án a]: chỉ có cận dưới 8; không có cận trên → biến V4 khai no_upper_bound = D6, phía trên dùng 1 điểm LARGE — lý do SV: giữ nguyên như A.
- D7 (kế thừa A5 – ký tự đặc biệt) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 34 liệt kê (@, $, !, %, *, ?, &) · SV chốt 2026-10-20, phương án a]: tập ĐÓNG — mật khẩu chỉ có ký tự đặc biệt ngoài tập bị coi là thiếu ký tự đặc biệt; ký tự ngoài tập được phép xuất hiện thêm nếu đã có ≥ 1 ký tự trong tập — lý do SV: giữ nguyên như A.
- D8 (kế thừa A6 – chữ hoa/thường) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 34, SRS im lặng về chữ có dấu · SV chốt 2026-10-20, phương án a]: chỉ tính A–Z / a–z; chữ có dấu tiếng Việt không tính là chữ hoa/thường — lý do SV: giữ nguyên như A.
- D9 (kế thừa A7 + A17 – Xác nhận mật khẩu) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 35 'Phải có trường Xác nhận mật khẩu' · SV chốt 2026-10-20, phương án a]: so khớp tuyệt đối, phân biệt hoa/thường; bỏ trống = không khớp. Nếu màn hình không có ô này: 1 case kiểm sự tồn tại → Fail; case có V5 hợp lệ bỏ bước nhập V5 và ghi notes; các case V5 không hợp lệ → Blocked (case gốc = case kiểm sự tồn tại) — lý do SV: giữ nguyên như A.
- D10 (oracle khi bị từ chối) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 33–35 ('từ chối'), SRS không quy định nội dung/kênh thông báo; tiền lệ A10; A16 (bong bóng HTML5) không áp dụng cho mobile · SV chốt 2026-10-20, phương án a]: oracle chính = không có tài khoản mới phía server (D11). Kèm theo: có thông báo lỗi trên app ở bất kỳ kênh nào (chữ trên màn hình, hộp thoại, toast) + vẫn ở màn 'Đăng Ký Tài Khoản'; nội dung chữ chỉ ghi Actual, không phân loại theo chữ của SUT — lý do SV: khớp quy ước C (oracle chính = dữ liệu không đổi; thông báo mọi kênh; không phân loại thông báo theo chữ).
- D11 (oracle khi thành công + điểm quan sát dữ liệu server) [loại: quyết định Expected · truy vết: có · căn cứ: FR-01 dòng 36 'được chuyển tới trang Đăng nhập'; SRS im lặng về thông báo thành công; tiền lệ A12 · SV chốt 2026-10-20, phương án a]: thành công = app chuyển sang màn 'Đăng Nhập' + tạo đúng 1 tài khoản. Hộp thoại/thông báo thành công: SRS im lặng → không khẳng định, chỉ ghi Actual. Điểm quan sát tài khoản: trang admin 'Quản lý Người dùng' (đếm dòng, cột Email; không có cột Họ Tên) TRƯỚC/SAU + đăng nhập thử trên app bằng email/mật khẩu vừa tạo (header hiển thị 'Chào, <Họ Tên>' → kiểm Họ Tên) — lý do SV: kiểm được 'đúng 1 tài khoản' khi chạy tay.
- D12 (cách nhập trên mobile) [loại: quyết định Expected · truy vết: có · căn cứ: SRS im lặng; mobile có bàn phím ảo với tự viết hoa / tự sửa / gợi ý; ô Họ Tên và Mật khẩu không đặt autoCapitalize (App.js dòng 805–809, 818–823), ô Email đặt autoCapitalize="none" (dòng 815) · SV chốt 2026-10-20, phương án a]: giá trị của case = chuỗi thực sự có trong ô ngay trước khi bấm 'Đăng Ký' (SV đọc lại, chụp màn hình; bàn phím tự sửa/tự viết hoa làm đổi chuỗi → sửa lại cho đúng giá trị case, ghi notes); gõ và dán cùng một chuỗi coi là cùng lớp, không thành biến riêng; khoảng trắng đầu/cuối là một phần giá trị (xử lý theo D3/D5) — lý do SV: mục tiêu ít case.
- D13 (yêu cầu GUI trên mobile) [loại: phạm vi + quyết định Expected · truy vết: có · căn cứ: FR-22 dòng 252–255 viết theo khái niệm web (type="email", type="password"); tiền lệ A14 (suite GUI riêng, không phân lớp) và phạm vi A (bỏ FR-21) · SV chốt 2026-10-20, phương án a]: FR-22.1 ('*' cạnh nhãn), FR-22.4 (thông báo lỗi phía trên nút 'Đăng Ký') áp nguyên; FR-22.2/22.3 hiểu tương đương mobile: Email → bàn phím email (keyboardType email-address), Mật khẩu → che ký tự (secureTextEntry); kiểm ở TS-GUI, không phân lớp; FR-21 ngoài phạm vi — lý do SV: nhất quán với A, giữ dòng so sánh web vs mobile (SRS không đủ căn cứ, SV quyết).
- D14 (verdict khi chạy tay) [loại: quy trình · truy vết: không · căn cứ: quyết định đã chốt A20/A17 (CLAUDE.md), quy tắc verdict của skill · SV chốt 2026-10-20, chấp nhận đề xuất AI]: chạy tay nên status do SV điền trực tiếp, auto_status để trống; lệch do biến mục tiêu → Fail; bị biến khác chặn → Blocked + case gốc; 'Pass hộp đen' khi bị từ chối đúng nhưng lý do không chứng minh luật mục tiêu. Evidence: ảnh chụp màn hình điện thoại TC-FR20-xx_manual_*.png (+ ảnh trang admin theo D11).
- D15 (thiết bị, locale, bàn phím) [loại: môi trường · truy vết: không · căn cứ: P2 (SV chốt Android thật, Expo Go) · SV chốt 2026-10-20, chấp nhận đề xuất AI]: SV ghi model, phiên bản Android, bản Expo Go, ngôn ngữ hệ thống, bàn phím (vd Gboard) khi chạy; ghi vào meta.environment và HW02/env/environment.md.

**Tổng:** chưa có test case (bước 3–4).
