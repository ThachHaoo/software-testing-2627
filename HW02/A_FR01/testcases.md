### Phạm vi
Form 'Đăng Ký Tài Khoản' trên frontend-web (tầng UI) và endpoint POST /api/register (tầng API). Trong phạm vi: FR-01 (phân lớp + BVA) và FR-22.1–FR-22.4 (thuộc tính tĩnh của form — kiểm bằng suite GUI riêng, không phân lớp, vì không phải miền giá trị nhập). Ngoài phạm vi: FR-21 (tiêu chuẩn giao diện chung, áp dụng toàn hệ thống, không riêng form đăng ký) và SEC-01 (mật khẩu không lưu plaintext — yêu cầu bảo mật tham khảo, không thuộc FR-01 và không quan sát được qua UI/API đăng ký); đăng ký trên Mobile (Pool D, FR-20); đăng nhập (FR-02); các trang khác.

### Yêu cầu (test basis)
| Mã | Nội dung |
|---|---|
| FR-01.1 | Người dùng phải cung cấp Họ Tên (trường bắt buộc). |
| FR-01.2 | Người dùng phải cung cấp Email (trường bắt buộc). |
| FR-01.3 | Email phải có định dạng hợp lệ (user@domain.com). |
| FR-01.4 | Email phải là duy nhất trong hệ thống. |
| FR-01.5 | Người dùng phải cung cấp Mật khẩu (trường bắt buộc). |
| FR-01.6 | Mật khẩu tối thiểu 8 ký tự. |
| FR-01.7a | Mật khẩu có ít nhất 1 chữ hoa. |
| FR-01.7b | Mật khẩu có ít nhất 1 chữ thường. |
| FR-01.7c | Mật khẩu có ít nhất 1 chữ số. |
| FR-01.8 | Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &. |
| FR-01.9 | Phải có trường Xác nhận mật khẩu; hệ thống từ chối nếu Mật khẩu và Xác nhận mật khẩu không khớp. |
| FR-01.10 | Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập. |
| FR-22.1 | Trường bắt buộc có ký hiệu * bên cạnh nhãn. |
| FR-22.2 | Trường Email dùng type="email". |
| FR-22.3 | Trường Mật khẩu dùng type="password". |
| FR-22.4 | Thông báo lỗi xuất hiện phía trên nút submit. |

### Bước 1 — Biến vào/ra
| Mã | Biến | Vào/Ra | Nguồn | Kiểu | Ràng buộc (đặc tả) | Ghi chú |
|---|---|---|---|---|---|---|
| V1 | Họ Tên | Vào | UI: ô nhãn 'Họ Tên' (Register.jsx dòng 36–43, input type="text", required) · API: body.name (server.js dòng 21; api_specification.md dòng 16) | string | Bắt buộc (FR-01.1). SRS không nêu độ dài/tập ký tự → xem A1. |  |
| V2 | Email | Vào | UI: ô nhãn 'Email' (Register.jsx dòng 46–53, input type="text", required) · API: body.email (server.js dòng 21; api_specification.md dòng 17) | string | Bắt buộc (FR-01.2); định dạng user@domain.com (FR-01.3, xem A2); FR-22.2 yêu cầu type="email". | Quan sát mã nguồn: ô Email type=text. Chưa kết luận lỗi, xác nhận khi thực thi (bước 6). |
| V3 | Email đã tồn tại trong hệ thống | Vào | Trạng thái dữ liệu: bảng users (database.js dòng 50–61); tài khoản seed admin@eshop.com, test@eshop.com (database.js dòng 92–93) | boolean (trạng thái CSDL) | Email nhập vào phải chưa tồn tại (FR-01.4). Cách so sánh hoa/thường, khoảng trắng → xem A3. |  |
| V4 | Mật khẩu | Vào | UI: ô nhãn 'Mật khẩu' (Register.jsx dòng 56–63, input type="password", required; gợi ý dòng 64–66) · API: body.password (server.js dòng 21; api_specification.md dòng 18) | string | Bắt buộc (FR-01.5); độ dài ≥ 8 (FR-01.6, không có cận trên – A4); ≥1 chữ hoa (FR-01.7a), ≥1 chữ thường (FR-01.7b), ≥1 chữ số (FR-01.7c) (A6); ≥1 ký tự thuộc {@ $ ! % * ? &} (FR-01.8, A5). |  |
| V5 | Xác nhận mật khẩu | Vào | SRS FR-01 (README.md dòng 35). Không thấy ô tương ứng trong Register.jsx (form dòng 34–80 chỉ có Họ Tên, Email, Mật khẩu) và không có trong body API (server.js dòng 21; api_specification.md dòng 14–19) | string | Phải bằng đúng V4 (FR-01.9, A7). Tầng API: xem A8. | Quan sát mã nguồn: form không có ô Xác nhận mật khẩu. Chưa kết luận lỗi, xác nhận khi thực thi (bước 6). |
| V6 | Thông báo lỗi trên form | Ra | UI: hộp lỗi đỏ (Register.jsx dòng 33) – nội dung từ kiểm tra phía client (dòng 18) hoặc response.data.error / 'Đăng ký thất bại.' (dòng 26); bong bóng kiểm tra HTML5 của trình duyệt cho thuộc tính required/type | message \| none | Dữ liệu không hợp lệ → có thông báo lỗi trên form; hợp lệ → không có lỗi. Nội dung chữ không được SRS quy định (A10). Vị trí thông báo chỉ kiểm ở case FR-22.4. |  |
| V7 | Trang đích sau khi bấm 'Đăng Ký' | Ra | UI: URL trình duyệt; navigate('/login') (Register.jsx dòng 24); route /register (App.jsx dòng 53) | enum {/login, /register} | Thành công → chuyển tới trang Đăng nhập /login (FR-01.10); thất bại → ở lại /register (A10). |  |
| V8 | Phản hồi API | Ra | API: HTTP status + body của POST /api/register (server.js dòng 26–27; api_specification.md dòng 21) | HTTP status + JSON | Hợp lệ → 200 {"message": "User registered successfully", "id": n}; không hợp lệ → 4xx kèm trường error (A11). |  |
| V9 | Bản ghi tài khoản trong CSDL | Ra | Bảng users (database.js dòng 50–61); quan sát qua GET /api/admin/users (api_specification.md dòng 176) hoặc POST /api/login (A12) | enum {tạo đúng 1 bản ghi, không tạo} | Hợp lệ → tạo đúng 1 user mới với name/email đã nhập, đăng nhập được; không hợp lệ → số user không đổi. |  |

### Bước 2 — Complete Set of Partitions
| EC | Biến | Lớp tương đương | Hợp lệ | Hướng dẫn | Ghi chú |
|---|---|---|---|---|---|
| EC1 | Họ Tên | Không rỗng, chỉ chữ Latin không dấu và khoảng trắng (ví dụ 'Nguyen Van A') | ✔ | split | FR-01.1. Tách khỏi EC2 vì chuỗi ASCII và chuỗi Unicode có dấu đi qua mã hoá/lưu trữ khác nhau. |
| EC2 | Họ Tên | Không rỗng, có chữ tiếng Việt có dấu (ví dụ 'Nguyễn Văn Ánh') | ✔ | split | FR-01.1. SRS không giới hạn tập ký tự (A1) → hợp lệ. |
| EC3 | Họ Tên | Rỗng (0 ký tự) | ✘ | must-be | FR-01.1 bắt buộc. |
| EC4 | Họ Tên | Chỉ gồm khoảng trắng (ví dụ '   ') | ✘ | split | A1: coi như rỗng. Tách khỏi EC3 vì thuộc tính required của HTML5 chặn '' nhưng không chặn chuỗi toàn khoảng trắng → hai lớp bị xử lý khác nhau. |
| EC5 | Họ Tên | Tầng API: trường name thiếu trong body hoặc bằng null | ✘ | must-be | Chỉ tầng API (A15). |
| EC6 | Họ Tên | Tầng API: name không phải chuỗi (ví dụ số 123) | ✘ | type | Chỉ tầng API (A15). |
| EC7 | Email | Đúng định dạng <local>@<domain>.<tld> (ví dụ 'newuser@domain.com') | ✔ | must-be | FR-01.2, FR-01.3, A2. |
| EC8 | Email | Đúng định dạng nhưng có khoảng trắng đầu/cuối (ví dụ '  newuser@domain.com  ') | ✔ | split | A3: khoảng trắng đầu/cuối được cắt → hợp lệ. Tách lớp vì phần cắt khoảng trắng có thể có hoặc không có ở UI/API. |
| EC9 | Email | Rỗng (0 ký tự) | ✘ | must-be | FR-01.2 bắt buộc. |
| EC10 | Email | Không có ký tự '@' (ví dụ 'newuserdomain.com') | ✘ | split | FR-01.3. Tách các lớp sai định dạng EC10–EC15 theo từng phần của mẫu user@domain.com bị vi phạm, vì mỗi kiểu lỗi có thể được bộ kiểm tra (HTML5 type=email, regex phía client, backend) xử lý khác nhau. |
| EC11 | Email | Có nhiều hơn một '@' (ví dụ 'new@user@domain.com') | ✘ | split | FR-01.3, A2 (đúng một '@'). |
| EC12 | Email | Phần local rỗng (ví dụ '@domain.com') | ✘ | split | FR-01.3, A2. |
| EC13 | Email | Phần domain rỗng (ví dụ 'newuser@') | ✘ | split | FR-01.3, A2. |
| EC14 | Email | Phần domain không có dấu '.' (ví dụ 'newuser@domain') | ✘ | split | A2: mẫu SRS có .tld. Tách riêng vì HTML5 type=email chấp nhận 'user@domain' → xử lý khác các lớp sai định dạng còn lại. |
| EC15 | Email | Có khoảng trắng bên trong (ví dụ 'new user@domain.com') | ✘ | split | FR-01.3, A2. Khác EC8: khoảng trắng nằm giữa, không bị cắt. |
| EC16 | Email | Tầng API: trường email thiếu trong body hoặc bằng null | ✘ | must-be | Chỉ tầng API (A15). |
| EC17 | Email | Tầng API: email không phải chuỗi (ví dụ số 123) | ✘ | type | Chỉ tầng API (A15). |
| EC18 | Email đã tồn tại trong hệ thống | Email chưa tồn tại trong bảng users | ✔ | set | FR-01.4. |
| EC19 | Email đã tồn tại trong hệ thống | Chỉ khác email đã có ở chữ hoa/thường (ví dụ 'TEST@eshop.com' khi đã có 'test@eshop.com') | ✔ | split | A3 (SV chốt): so sánh phân biệt hoa/thường → coi là email mới, hợp lệ. |
| EC20 | Email đã tồn tại trong hệ thống | Trùng chính xác email đã có (ví dụ 'test@eshop.com') | ✘ | set | FR-01.4. Dùng tài khoản seed (A13). |
| EC21 | Email đã tồn tại trong hệ thống | Trùng email đã có sau khi cắt khoảng trắng đầu/cuối (ví dụ ' test@eshop.com ') | ✘ | split | A3 (SV chốt): cắt khoảng trắng rồi mới so sánh → trùng. Tách khỏi EC20 vì so khớp chuỗi nguyên văn sẽ không phát hiện trùng. |
| EC22 | Mật khẩu | Độ dài ≥ 8 ký tự (các điều kiện khác thoả) | ✔ | range | FR-01.6. Miền chỉ có cận dưới LB = 8, không có UB (A4) → chỉ có một lớp không hợp lệ phía dưới (EC23); MIN_UI/MAX_UI xét ở bước 4. |
| EC23 | Mật khẩu | Độ dài 1–7 ký tự (các điều kiện khác thoả) | ✘ | range | FR-01.6. |
| EC24 | Mật khẩu | Rỗng (0 ký tự) | ✘ | must-be | FR-01.5 bắt buộc. Tách khỏi EC23 vì required của HTML5 chặn chuỗi rỗng trước khi chạy kiểm tra độ mạnh. |
| EC25 | Mật khẩu | Có ≥ 1 chữ hoa A–Z | ✔ | must-be | FR-01.7a. |
| EC26 | Mật khẩu | Không có chữ hoa nào (các điều kiện khác thoả) | ✘ | must-be | FR-01.7a. |
| EC27 | Mật khẩu | Chữ hoa duy nhất là chữ có dấu tiếng Việt, ví dụ 'Ê' (các điều kiện khác thoả) | ✘ | split | A6: chỉ A–Z tính là chữ hoa. Tách khỏi EC26 vì bộ kiểm tra theo Unicode và theo [A-Z] cho kết quả khác nhau. |
| EC28 | Mật khẩu | Có ≥ 1 chữ thường a–z | ✔ | must-be | FR-01.7b. |
| EC29 | Mật khẩu | Không có chữ thường nào (các điều kiện khác thoả) | ✘ | must-be | FR-01.7b. |
| EC30 | Mật khẩu | Chữ thường duy nhất là chữ có dấu tiếng Việt, ví dụ 'ê' (các điều kiện khác thoả) | ✘ | split | A6, cùng lý do EC27. |
| EC31 | Mật khẩu | Có ≥ 1 chữ số 0–9 | ✔ | must-be | FR-01.7c. |
| EC32 | Mật khẩu | Không có chữ số nào (các điều kiện khác thoả) | ✘ | must-be | FR-01.7c. |
| EC33 | Mật khẩu | Có ≥ 1 ký tự thuộc {@ $ ! % * ? &}, không có ký tự đặc biệt ngoài tập | ✔ | set | FR-01.8. |
| EC34 | Mật khẩu | Có ≥ 1 ký tự thuộc tập và thêm ký tự đặc biệt ngoài tập (ví dụ '!' và '#') | ✔ | split | A5: ký tự ngoài tập được phép xuất hiện thêm. Tách khỏi EC33 vì regex dạng whitelist sẽ từ chối lớp này. |
| EC35 | Mật khẩu | Không có ký tự đặc biệt nào (các điều kiện khác thoả) | ✘ | set | FR-01.8. |
| EC36 | Mật khẩu | Chỉ có ký tự đặc biệt ngoài tập, ví dụ '#', '^', '-', khoảng trắng (các điều kiện khác thoả) | ✘ | set | A5: tập đóng → coi như thiếu ký tự đặc biệt. Lớp 'ngoài tập' theo hướng dẫn set. |
| EC37 | Mật khẩu | Tầng API: trường password thiếu trong body hoặc bằng null | ✘ | must-be | Chỉ tầng API (A15). |
| EC38 | Mật khẩu | Tầng API: password không phải chuỗi (ví dụ số 12345678) | ✘ | type | Chỉ tầng API (A15). |
| EC39 | Xác nhận mật khẩu | Khớp chính xác với Mật khẩu | ✔ | must-be | FR-01.9. Chỉ tầng UI (A8). |
| EC40 | Xác nhận mật khẩu | Rỗng | ✘ | must-be | A7: rỗng coi như không khớp. Tách khỏi EC41 vì có thể bị chặn bởi required trước khi so sánh. |
| EC41 | Xác nhận mật khẩu | Khác Mật khẩu ít nhất một ký tự (không chỉ khác hoa/thường) | ✘ | must-be | FR-01.9. |
| EC42 | Xác nhận mật khẩu | Chỉ khác Mật khẩu ở chữ hoa/thường (ví dụ 'Abcd1234!' và 'abcd1234!') | ✘ | split | A7: so sánh phân biệt hoa/thường. Tách khỏi EC41 vì so sánh không phân biệt hoa/thường sẽ cho là khớp. |
| EC43 | Thông báo lỗi trên form | Không có thông báo lỗi | ✔ | output | Khi mọi đầu vào hợp lệ. |
| EC44 | Thông báo lỗi trên form | Có thông báo lỗi trên form (hộp lỗi hoặc bong bóng HTML5) | ✘ | output | A10, A16. Nội dung chữ ghi làm Actual; vị trí chỉ kiểm ở FR-22.4. |
| EC45 | Trang đích sau khi bấm 'Đăng Ký' | Chuyển tới trang Đăng nhập /login | ✔ | output | FR-01.10. |
| EC46 | Trang đích sau khi bấm 'Đăng Ký' | Ở lại trang /register | ✘ | output | A10. |
| EC47 | Phản hồi API | HTTP 200, body {"message": "User registered successfully", "id": n} | ✔ | output | api_specification.md dòng 21. |
| EC48 | Phản hồi API | HTTP 4xx, body có trường error | ✘ | output | A11. 5xx hoặc không phản hồi không thuộc lớp mong đợi nào → không đạt oracle. |
| EC49 | Bản ghi tài khoản trong CSDL | Tạo đúng 1 bản ghi user mới với name/email đã nhập | ✔ | output | A12: quan sát qua GET /api/admin/users hoặc đăng nhập. |
| EC50 | Bản ghi tài khoản trong CSDL | Không tạo bản ghi (số user không đổi) | ✘ | output | A12. |

### Bước 3a — Test Cases Providing Coverage of Partitions
| EC | Lớp | Test case phủ |
|---|---|---|
| EC1 | Không rỗng, chỉ chữ Latin không dấu và khoảng trắng (ví dụ 'Nguyen Van A') | ⚠ chưa phủ |
| EC2 | Không rỗng, có chữ tiếng Việt có dấu (ví dụ 'Nguyễn Văn Ánh') | ⚠ chưa phủ |
| EC3 | Rỗng (0 ký tự) | ⚠ chưa phủ |
| EC4 | Chỉ gồm khoảng trắng (ví dụ '   ') | ⚠ chưa phủ |
| EC5 | Tầng API: trường name thiếu trong body hoặc bằng null | ⚠ chưa phủ |
| EC6 | Tầng API: name không phải chuỗi (ví dụ số 123) | ⚠ chưa phủ |
| EC7 | Đúng định dạng <local>@<domain>.<tld> (ví dụ 'newuser@domain.com') | ⚠ chưa phủ |
| EC8 | Đúng định dạng nhưng có khoảng trắng đầu/cuối (ví dụ '  newuser@domain.com  ') | ⚠ chưa phủ |
| EC9 | Rỗng (0 ký tự) | ⚠ chưa phủ |
| EC10 | Không có ký tự '@' (ví dụ 'newuserdomain.com') | ⚠ chưa phủ |
| EC11 | Có nhiều hơn một '@' (ví dụ 'new@user@domain.com') | ⚠ chưa phủ |
| EC12 | Phần local rỗng (ví dụ '@domain.com') | ⚠ chưa phủ |
| EC13 | Phần domain rỗng (ví dụ 'newuser@') | ⚠ chưa phủ |
| EC14 | Phần domain không có dấu '.' (ví dụ 'newuser@domain') | ⚠ chưa phủ |
| EC15 | Có khoảng trắng bên trong (ví dụ 'new user@domain.com') | ⚠ chưa phủ |
| EC16 | Tầng API: trường email thiếu trong body hoặc bằng null | ⚠ chưa phủ |
| EC17 | Tầng API: email không phải chuỗi (ví dụ số 123) | ⚠ chưa phủ |
| EC18 | Email chưa tồn tại trong bảng users | ⚠ chưa phủ |
| EC19 | Chỉ khác email đã có ở chữ hoa/thường (ví dụ 'TEST@eshop.com' khi đã có 'test@eshop.com') | ⚠ chưa phủ |
| EC20 | Trùng chính xác email đã có (ví dụ 'test@eshop.com') | ⚠ chưa phủ |
| EC21 | Trùng email đã có sau khi cắt khoảng trắng đầu/cuối (ví dụ ' test@eshop.com ') | ⚠ chưa phủ |
| EC22 | Độ dài ≥ 8 ký tự (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC23 | Độ dài 1–7 ký tự (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC24 | Rỗng (0 ký tự) | ⚠ chưa phủ |
| EC25 | Có ≥ 1 chữ hoa A–Z | ⚠ chưa phủ |
| EC26 | Không có chữ hoa nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC27 | Chữ hoa duy nhất là chữ có dấu tiếng Việt, ví dụ 'Ê' (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC28 | Có ≥ 1 chữ thường a–z | ⚠ chưa phủ |
| EC29 | Không có chữ thường nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC30 | Chữ thường duy nhất là chữ có dấu tiếng Việt, ví dụ 'ê' (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC31 | Có ≥ 1 chữ số 0–9 | ⚠ chưa phủ |
| EC32 | Không có chữ số nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC33 | Có ≥ 1 ký tự thuộc {@ $ ! % * ? &}, không có ký tự đặc biệt ngoài tập | ⚠ chưa phủ |
| EC34 | Có ≥ 1 ký tự thuộc tập và thêm ký tự đặc biệt ngoài tập (ví dụ '!' và '#') | ⚠ chưa phủ |
| EC35 | Không có ký tự đặc biệt nào (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC36 | Chỉ có ký tự đặc biệt ngoài tập, ví dụ '#', '^', '-', khoảng trắng (các điều kiện khác thoả) | ⚠ chưa phủ |
| EC37 | Tầng API: trường password thiếu trong body hoặc bằng null | ⚠ chưa phủ |
| EC38 | Tầng API: password không phải chuỗi (ví dụ số 12345678) | ⚠ chưa phủ |
| EC39 | Khớp chính xác với Mật khẩu | ⚠ chưa phủ |
| EC40 | Rỗng | ⚠ chưa phủ |
| EC41 | Khác Mật khẩu ít nhất một ký tự (không chỉ khác hoa/thường) | ⚠ chưa phủ |
| EC42 | Chỉ khác Mật khẩu ở chữ hoa/thường (ví dụ 'Abcd1234!' và 'abcd1234!') | ⚠ chưa phủ |
| EC43 | Không có thông báo lỗi | ⚠ chưa phủ |
| EC44 | Có thông báo lỗi trên form (hộp lỗi hoặc bong bóng HTML5) | ⚠ chưa phủ |
| EC45 | Chuyển tới trang Đăng nhập /login | ⚠ chưa phủ |
| EC46 | Ở lại trang /register | ⚠ chưa phủ |
| EC47 | HTTP 200, body {"message": "User registered successfully", "id": n} | ⚠ chưa phủ |
| EC48 | HTTP 4xx, body có trường error | ⚠ chưa phủ |
| EC49 | Tạo đúng 1 bản ghi user mới với name/email đã nhập | ⚠ chưa phủ |
| EC50 | Không tạo bản ghi (số user không đổi) | ⚠ chưa phủ |

### Truy vết yêu cầu ↔ test case
| Yêu cầu | Test case | Số TC |
|---|---|---|
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
- A1 (Họ Tên): FR-01 chỉ nói 'phải cung cấp'. SRS không nêu độ dài tối thiểu/tối đa hay tập ký tự → chỉ coi 'rỗng' là không hợp lệ. Chuỗi chỉ gồm khoảng trắng: giả định bị coi như rỗng (bị từ chối). Không có cận trên → không sinh UB/MAX_UI cho Họ Tên trừ khi SV quyết định khác.
- A2 (Email – định dạng): FR-01 chỉ đưa mẫu 'user@domain.com'. Giả định định dạng hợp lệ = <local>@<domain>.<tld>: đúng một '@', phần local không rỗng, phần domain có ít nhất một dấu '.' và không rỗng hai bên dấu chấm. FR-22 yêu cầu type="email" nên quy tắc HTML5 của trình duyệt dùng làm tham chiếu phụ. SRS không nêu độ dài tối đa → không kiểm cận trên độ dài email.
- A3 (Email – duy nhất): SRS không nói so sánh có phân biệt hoa/thường và có cắt khoảng trắng đầu/cuối hay không. Giả định (SV chốt 2026-10-19): so sánh CÓ phân biệt hoa/thường (TEST@eshop.com khác test@eshop.com, coi là email mới) và khoảng trắng đầu/cuối được cắt trước khi so sánh (' test@eshop.com ' trùng test@eshop.com). Expected của các case liên quan email trùng tuân theo giả định này.
- A4 (Mật khẩu – độ dài): chỉ có cận dưới 8 ký tự. SRS không có cận trên → không có UB; BVA độ dài chỉ quanh LB = 8 (7, 8, 9) và NOM.
- A5 (Mật khẩu – ký tự đặc biệt): hiểu danh sách (@, $, !, %, *, ?, &) là tập ĐÓNG: mật khẩu chỉ chứa ký tự đặc biệt ngoài tập này (ví dụ #, ^, -, khoảng trắng) bị coi là thiếu ký tự đặc biệt → bị từ chối. SRS không nói ký tự ngoài tập có được phép xuất hiện thêm hay không → giả định được phép nếu đã có ít nhất một ký tự trong tập.
- A6 (Mật khẩu – chữ hoa/thường): giả định chỉ tính chữ Latin A–Z / a–z; chữ có dấu tiếng Việt (Ă, ê…) không tính là chữ hoa/thường. SRS im lặng. Expected của EC27/EC30 phụ thuộc giả định này; kết quả lệch được phân tích là SRS mơ hồ trước khi kết luận lỗi.
- A7 (Xác nhận mật khẩu): FR-01 yêu cầu trường này; so sánh phân biệt hoa/thường, khớp tuyệt đối với Mật khẩu. Bỏ trống trường này coi như không khớp → bị từ chối.
- A8 (Xác nhận mật khẩu ở tầng API): api_specification.md dòng 14–19 không có trường xác nhận trong body. Giả định yêu cầu 'khớp hai trường' chỉ kiểm ở tầng UI; ở tầng API biến này không áp dụng. Cần SV xác nhận.
- A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- A10 (Thông báo lỗi): SRS không quy định nội dung chữ của thông báo lỗi. Oracle cho case nhập liệu không hợp lệ = có thông báo lỗi hiển thị trên form + vẫn ở trang /register + không tạo bản ghi user; nội dung chữ chỉ ghi lại làm Actual. Vị trí thông báo lỗi (phía trên nút 'Đăng Ký') chỉ kiểm ở case GUI của FR-22.4, không đưa vào oracle của case nhập liệu.
- A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- A12 (Quan sát bản ghi): kiểm 'có/không tạo user' bằng GET /api/admin/users với token của admin@eshop.com / Admin123!, hoặc đăng nhập POST /api/login bằng tài khoản vừa tạo.
- A13 (Dữ liệu sẵn có): email đã tồn tại dùng tài khoản seed test@eshop.com (database.js dòng 93). Backend khởi động lại → CSDL seed lại, tài khoản tạo trong lúc test mất; mỗi case dùng email mới (ví dụ gắn timestamp) để case độc lập.
- A14 (FR-22 thuộc tính form): ký hiệu '*', type="email", type="password", vị trí thông báo lỗi là thuộc tính tĩnh của form, không phải miền giá trị nhập → không phân lớp ở bước 2; kiểm bằng suite GUI riêng (SV chốt 2026-10-19).
- A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.
- A16 (Thông báo kiểm tra HTML5): khi trình duyệt chặn submit bằng bong bóng kiểm tra của thuộc tính required/type, bong bóng đó được coi là 'thông báo lỗi trên form' trong oracle của V6. SRS không phân biệt cơ chế hiển thị (SV xác nhận 2026-10-19). Cách quan sát: bong bóng HTML5 không nằm trong DOM → oracle = form không gửi request POST /api/register + ô liên quan ở trạng thái :invalid / validationMessage không rỗng.
- A17 (Thiếu ô Xác nhận mật khẩu): nếu form không có ô Xác nhận mật khẩu (xem note V5): case kiểm sự tồn tại của trường → Fail; các case cần nhập V5 ở tầng UI → Blocked kèm mã bug. Không xoá case.

**Tổng:** chưa có test case (bước 3–4).
