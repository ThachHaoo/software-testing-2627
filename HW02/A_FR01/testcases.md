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
| EC1 | Không rỗng, chỉ chữ Latin không dấu và khoảng trắng (ví dụ 'Nguyen Van A') | TC-FR01-01, TC-FR01-28 |
| EC2 | Không rỗng, có chữ tiếng Việt có dấu (ví dụ 'Nguyễn Văn Ánh') | TC-FR01-02, TC-FR01-29 |
| EC3 | Rỗng (0 ký tự) | TC-FR01-05, TC-FR01-32 |
| EC4 | Chỉ gồm khoảng trắng (ví dụ '   ') | TC-FR01-06, TC-FR01-33 |
| EC5 | Tầng API: trường name thiếu trong body hoặc bằng null | TC-FR01-52 |
| EC6 | Tầng API: name không phải chuỗi (ví dụ số 123) | TC-FR01-53 |
| EC7 | Đúng định dạng <local>@<domain>.<tld> (ví dụ 'newuser@domain.com') | TC-FR01-01, TC-FR01-02, TC-FR01-28, TC-FR01-29 |
| EC8 | Đúng định dạng nhưng có khoảng trắng đầu/cuối (ví dụ '  newuser@domain.com  ') | TC-FR01-03, TC-FR01-30 |
| EC9 | Rỗng (0 ký tự) | TC-FR01-07, TC-FR01-34 |
| EC10 | Không có ký tự '@' (ví dụ 'newuserdomain.com') | TC-FR01-08, TC-FR01-35 |
| EC11 | Có nhiều hơn một '@' (ví dụ 'new@user@domain.com') | TC-FR01-09, TC-FR01-36 |
| EC12 | Phần local rỗng (ví dụ '@domain.com') | TC-FR01-10, TC-FR01-37 |
| EC13 | Phần domain rỗng (ví dụ 'newuser@') | TC-FR01-11, TC-FR01-38 |
| EC14 | Phần domain không có dấu '.' (ví dụ 'newuser@domain') | TC-FR01-12, TC-FR01-39 |
| EC15 | Có khoảng trắng bên trong (ví dụ 'new user@domain.com') | TC-FR01-13, TC-FR01-40 |
| EC16 | Tầng API: trường email thiếu trong body hoặc bằng null | TC-FR01-54 |
| EC17 | Tầng API: email không phải chuỗi (ví dụ số 123) | TC-FR01-55 |
| EC18 | Email chưa tồn tại trong bảng users | TC-FR01-01, TC-FR01-02, TC-FR01-28, TC-FR01-29 |
| EC19 | Chỉ khác email đã có ở chữ hoa/thường (ví dụ 'TEST@eshop.com' khi đã có 'test@eshop.com') | TC-FR01-04, TC-FR01-31 |
| EC20 | Trùng chính xác email đã có (ví dụ 'test@eshop.com') | TC-FR01-14, TC-FR01-41 |
| EC21 | Trùng email đã có sau khi cắt khoảng trắng đầu/cuối (ví dụ ' test@eshop.com ') | TC-FR01-15, TC-FR01-42 |
| EC22 | Độ dài ≥ 8 ký tự (các điều kiện khác thoả) | TC-FR01-01, TC-FR01-02, TC-FR01-28, TC-FR01-29 |
| EC23 | Độ dài 1–7 ký tự (các điều kiện khác thoả) | TC-FR01-16, TC-FR01-43 |
| EC24 | Rỗng (0 ký tự) | TC-FR01-17, TC-FR01-44 |
| EC25 | Có ≥ 1 chữ hoa A–Z | TC-FR01-01, TC-FR01-02, TC-FR01-28, TC-FR01-29 |
| EC26 | Không có chữ hoa nào (các điều kiện khác thoả) | TC-FR01-18, TC-FR01-45 |
| EC27 | Chữ hoa duy nhất là chữ có dấu tiếng Việt, ví dụ 'Ê' (các điều kiện khác thoả) | TC-FR01-19, TC-FR01-46 |
| EC28 | Có ≥ 1 chữ thường a–z | TC-FR01-01, TC-FR01-02, TC-FR01-28, TC-FR01-29 |
| EC29 | Không có chữ thường nào (các điều kiện khác thoả) | TC-FR01-20, TC-FR01-47 |
| EC30 | Chữ thường duy nhất là chữ có dấu tiếng Việt, ví dụ 'ê' (các điều kiện khác thoả) | TC-FR01-21, TC-FR01-48 |
| EC31 | Có ≥ 1 chữ số 0–9 | TC-FR01-01, TC-FR01-02, TC-FR01-28, TC-FR01-29 |
| EC32 | Không có chữ số nào (các điều kiện khác thoả) | TC-FR01-22, TC-FR01-49 |
| EC33 | Có ≥ 1 ký tự thuộc {@ $ ! % * ? &}, không có ký tự đặc biệt ngoài tập | TC-FR01-01, TC-FR01-28 |
| EC34 | Có ≥ 1 ký tự thuộc tập và thêm ký tự đặc biệt ngoài tập (ví dụ '!' và '#') | TC-FR01-02, TC-FR01-29 |
| EC35 | Không có ký tự đặc biệt nào (các điều kiện khác thoả) | TC-FR01-23, TC-FR01-50 |
| EC36 | Chỉ có ký tự đặc biệt ngoài tập, ví dụ '#', '^', '-', khoảng trắng (các điều kiện khác thoả) | TC-FR01-24, TC-FR01-51 |
| EC37 | Tầng API: trường password thiếu trong body hoặc bằng null | TC-FR01-56 |
| EC38 | Tầng API: password không phải chuỗi (ví dụ số 12345678) | TC-FR01-57 |
| EC39 | Khớp chính xác với Mật khẩu | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04 |
| EC40 | Rỗng | TC-FR01-25 |
| EC41 | Khác Mật khẩu ít nhất một ký tự (không chỉ khác hoa/thường) | TC-FR01-26 |
| EC42 | Chỉ khác Mật khẩu ở chữ hoa/thường (ví dụ 'Abcd1234!' và 'abcd1234!') | TC-FR01-27 |
| EC43 | Không có thông báo lỗi | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04 |
| EC44 | Có thông báo lỗi trên form (hộp lỗi hoặc bong bóng HTML5) | TC-FR01-05, TC-FR01-06, TC-FR01-07, TC-FR01-08, TC-FR01-09, TC-FR01-10, TC-FR01-11, TC-FR01-12, TC-FR01-13, TC-FR01-14, TC-FR01-15, TC-FR01-16, TC-FR01-17, TC-FR01-18, TC-FR01-19, TC-FR01-20, TC-FR01-21, TC-FR01-22, TC-FR01-23, TC-FR01-24, TC-FR01-25, TC-FR01-26, TC-FR01-27 |
| EC45 | Chuyển tới trang Đăng nhập /login | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04 |
| EC46 | Ở lại trang /register | TC-FR01-05, TC-FR01-06, TC-FR01-07, TC-FR01-08, TC-FR01-09, TC-FR01-10, TC-FR01-11, TC-FR01-12, TC-FR01-13, TC-FR01-14, TC-FR01-15, TC-FR01-16, TC-FR01-17, TC-FR01-18, TC-FR01-19, TC-FR01-20, TC-FR01-21, TC-FR01-22, TC-FR01-23, TC-FR01-24, TC-FR01-25, TC-FR01-26, TC-FR01-27 |
| EC47 | HTTP 200, body {"message": "User registered successfully", "id": n} | TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31 |
| EC48 | HTTP 4xx, body có trường error | TC-FR01-32, TC-FR01-33, TC-FR01-34, TC-FR01-35, TC-FR01-36, TC-FR01-37, TC-FR01-38, TC-FR01-39, TC-FR01-40, TC-FR01-41, TC-FR01-42, TC-FR01-43, TC-FR01-44, TC-FR01-45, TC-FR01-46, TC-FR01-47, TC-FR01-48, TC-FR01-49, TC-FR01-50, TC-FR01-51, TC-FR01-52, TC-FR01-53, TC-FR01-54, TC-FR01-55, TC-FR01-56, TC-FR01-57 |
| EC49 | Tạo đúng 1 bản ghi user mới với name/email đã nhập | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31 |
| EC50 | Không tạo bản ghi (số user không đổi) | TC-FR01-05, TC-FR01-06, TC-FR01-07, TC-FR01-08, TC-FR01-09, TC-FR01-10, TC-FR01-11, TC-FR01-12, TC-FR01-13, TC-FR01-14, TC-FR01-15, TC-FR01-16, TC-FR01-17, TC-FR01-18, TC-FR01-19, TC-FR01-20, TC-FR01-21, TC-FR01-22, TC-FR01-23, TC-FR01-24, TC-FR01-25, TC-FR01-26, TC-FR01-27, TC-FR01-32, TC-FR01-33, TC-FR01-34, TC-FR01-35, TC-FR01-36, TC-FR01-37, TC-FR01-38, TC-FR01-39, TC-FR01-40, TC-FR01-41, TC-FR01-42, TC-FR01-43, TC-FR01-44, TC-FR01-45, TC-FR01-46, TC-FR01-47, TC-FR01-48, TC-FR01-49, TC-FR01-50, TC-FR01-51, TC-FR01-52, TC-FR01-53, TC-FR01-54, TC-FR01-55, TC-FR01-56, TC-FR01-57 |

### Bước 3b — Minimum Set of Test Cases (Domain) · TS-DOM-UI — Domain — minimum set, tầng UI (FR-01)
**Ghi chú suite:** giữ đủ lớp theo quy tắc mỗi case không hợp lệ phủ một lớp
**Tiền điều kiện:** Trước mỗi lượt chạy cả suite: khởi động lại backend (node server.js) để CSDL seed sạch, có admin@eshop.com và test@eshop.com (A13).; Web http://localhost:5173 đang chạy.; Có token admin: POST /api/login với admin@eshop.com / Admin123! (dùng cho GET/DELETE /api/admin/users, A12).; Thay {ts} trong cột Email bằng Date.now() lúc chạy case để email là duy nhất (A19).; Trạng thái ban đầu của mỗi case: trang /register vừa tải xong, cả 4 ô (Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu nếu có) đều trống; chưa đăng nhập (localStorage không có token).; Chạy tay: dùng cửa sổ ẩn danh và tắt autofill. Playwright: browser context mới cho mỗi case.

**Quy trình chung:**
1. Gọi GET /api/admin/users (token admin) và lưu danh sách id/email/name. → HTTP 200; danh sách có admin@eshop.com và test@eshop.com.
2. Mở http://localhost:5173/register. → Form 'Đăng Ký Tài Khoản' hiển thị; các ô Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu (nếu có) đều trống.
3. Nhập lần lượt Họ Tên → Email → Mật khẩu → Xác nhận mật khẩu bằng cách gõ đúng chuỗi trong cột. Ô có giá trị `''` (rỗng): không nhập gì, giữ ô trống. Giá trị có ␣: gõ đúng số dấu cách đó. Nếu form không có ô Xác nhận mật khẩu: case có V5 = EC39 bỏ qua bước nhập V5 và ghi notes; case EC40–EC42 dừng, Blocked (A17). → Mỗi ô hiển thị đúng giá trị đã gõ; Mật khẩu và Xác nhận mật khẩu hiện dạng che.
4. Bấm nút 'Đăng Ký' đúng một lần. → Hệ thống phản hồi: hiện lỗi, trình duyệt chặn submit, hoặc chuyển trang.
5. Quan sát hộp lỗi đỏ trên form, bong bóng kiểm tra của trình duyệt (validationMessage của ô) và URL trên thanh địa chỉ. → Khớp phần UI của cột Expected.
6. Gọi lại GET /api/admin/users và so với danh sách lưu ở bước 1. → Số user mới và name/email của user mới như cột Expected (oracle tương đối).

**Dọn dẹp:** Sau mỗi case, kể cả khi Fail: xoá mọi user mới so với danh sách ở bước 1 bằng DELETE /api/admin/users/:id (token admin). Nếu xoá thất bại: ghi vào notes của case, không đổi verdict (A19).

| #TC | Tiêu đề | EC phủ | Họ Tên | Email | Email trong CSDL | Mật khẩu | Xác nhận mật khẩu | Expected | Lý do chọn input | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-FR01-01 | Kiểm tra đăng ký thành công qua UI khi Họ Tên không dấu, email mới và mật khẩu mạnh | EC1, EC7, EC18, EC22, EC25, EC28, EC31, EC33, EC39, EC43, EC45, EC49 | Nguyen Van A | dom01_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'dom01_{ts}@domain.com' như cột dữ liệu. | Case hợp lệ thứ nhất: giá trị danh nghĩa đơn giản nhất của các lớp hợp lệ có căn cứ SRS (tên ASCII, email đúng mẫu chưa tồn tại, mật khẩu 9 ký tự chỉ dùng ký tự đặc biệt trong tập). | AI |
| TC-FR01-02 | Kiểm tra đăng ký thành công qua UI khi Họ Tên có dấu và mật khẩu có thêm ký tự đặc biệt ngoài tập | EC2, EC7, EC18, EC22, EC25, EC28, EC31, EC34, EC39, EC43, EC45, EC49 | Nguyễn Văn Ánh | dom02_{ts}@domain.com | chưa có | Abcd1234!# | Abcd1234!# | Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyễn Văn Ánh' và email 'dom02_{ts}@domain.com' như cột dữ liệu. | Case hợp lệ thứ hai: phủ các lớp hợp lệ còn lại có căn cứ SRS (EC2 tên có dấu — SRS không giới hạn ký tự; EC34 — A5 cho phép ký tự ngoài tập đi kèm). | AI |
| TC-FR01-03 | Kiểm tra đăng ký thành công qua UI khi email có khoảng trắng đầu/cuối | EC8, EC39, EC43, EC45, EC49 | Nguyen Van A | `␣␣dom03_{ts}@domain.com␣␣` | chưa có | Abcd1234! | Abcd1234! | Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'dom03_{ts}@domain.com' như cột dữ liệu. Email lưu đã được cắt khoảng trắng (A3). | Lớp dựa trên giả định A3 nên tách thành case riêng; hai khoảng trắng mỗi bên, phần còn lại là email mới đúng mẫu. | AI |
| TC-FR01-04 | Kiểm tra đăng ký thành công qua UI khi email chỉ khác hoa/thường với tài khoản đã có | EC19, EC39, EC43, EC45, EC49 | Nguyen Van A | Test@eshop.com | đã có 'test@eshop.com' (seed) | Abcd1234! | Abcd1234! | Không có thông báo lỗi; trình duyệt chuyển tới /login (FR-01.10); so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'Test@eshop.com' như cột dữ liệu; user seed 'test@eshop.com' không bị sửa. | Lớp dựa trên giả định A3 nên tách thành case riêng; biến thể 'Test@eshop.com' khác biến thể của case API để hai case không phụ thuộc nhau. | AI |
| TC-FR01-05 | Kiểm tra từ chối đăng ký qua UI khi Họ Tên rỗng | EC3, EC44, EC46, EC50 | `''` (rỗng) | dom05_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Họ Tên' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chuỗi rỗng là đại diện duy nhất của lớp 'rỗng'. | AI |
| TC-FR01-06 | Kiểm tra từ chối đăng ký qua UI khi Họ Tên chỉ gồm khoảng trắng | EC4, EC44, EC46, EC50 | `␣␣␣` | dom06_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Họ Tên' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | 3 khoảng trắng: vượt qua required của HTML5 nhưng vẫn rỗng sau khi cắt (A1). | AI |
| TC-FR01-07 | Kiểm tra từ chối đăng ký qua UI khi Email rỗng | EC9, EC44, EC46, EC50 | Nguyen Van A | `''` (rỗng) | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chuỗi rỗng là đại diện duy nhất của lớp 'rỗng'. | AI |
| TC-FR01-08 | Kiểm tra từ chối đăng ký qua UI khi Email không có ký tự '@' | EC10, EC44, EC46, EC50 | Nguyen Van A | dom08_{ts}domain.com | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Giữ nguyên các phần khác của mẫu, chỉ bỏ '@' để lỗi chỉ đến từ thiếu '@'. | AI |
| TC-FR01-09 | Kiểm tra từ chối đăng ký qua UI khi Email có hai ký tự '@' | EC11, EC44, EC46, EC50 | Nguyen Van A | dom09@x_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thêm đúng một '@' thừa, phần local và domain vẫn không rỗng. | AI |
| TC-FR01-10 | Kiểm tra từ chối đăng ký qua UI khi Email có phần local rỗng | EC12, EC44, EC46, EC50 | Nguyen Van A | @dom{ts}.com | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Domain đúng mẫu, chỉ thiếu phần trước '@'. | AI |
| TC-FR01-11 | Kiểm tra từ chối đăng ký qua UI khi Email có phần domain rỗng | EC13, EC44, EC46, EC50 | Nguyen Van A | dom11_{ts}@ | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Phần local đúng mẫu, chỉ thiếu phần sau '@'. | AI |
| TC-FR01-12 | Kiểm tra từ chối đăng ký qua UI khi Email có domain không chứa dấu chấm | EC14, EC44, EC46, EC50 | Nguyen Van A | dom12_{ts}@domain | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | HTML5 type=email chấp nhận dạng này nhưng thiếu .tld theo A2 — đại diện điển hình nhất của lớp. | AI |
| TC-FR01-13 | Kiểm tra từ chối đăng ký qua UI khi Email có khoảng trắng ở giữa phần local | EC15, EC44, EC46, EC50 | Nguyen Van A | dom 13_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Một khoảng trắng duy nhất ở giữa, đầu/cuối không có khoảng trắng để không lẫn với EC8. | AI |
| TC-FR01-14 | Kiểm tra từ chối đăng ký qua UI khi Email trùng chính xác tài khoản đã có | EC20, EC44, EC46, EC50 | Nguyen Van A | test@eshop.com | đã có 'test@eshop.com' (seed) | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Tài khoản seed luôn có sau khi backend khởi động (A13). | AI |
| TC-FR01-15 | Kiểm tra từ chối đăng ký qua UI khi Email trùng tài khoản đã có sau khi cắt khoảng trắng đầu/cuối | EC21, EC44, EC46, EC50 | Nguyen Van A | `␣test@eshop.com␣` | đã có 'test@eshop.com' (seed) | Abcd1234! | Abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Email' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Một khoảng trắng mỗi bên — ít nhất để khác chuỗi nguyên văn nhưng trùng sau khi cắt (A3). | AI |
| TC-FR01-16 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu 7 ký tự thoả các điều kiện còn lại | EC23, EC44, EC46, EC50 | Nguyen Van A | dom16_{ts}@domain.com | chưa có | Abc12!x | Abc12!x | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | 7 ký tự có đủ chữ hoa, chữ thường, chữ số và '!' → chỉ vi phạm độ dài. Điểm 7 được xét lại ở BVA. | AI |
| TC-FR01-17 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu rỗng | EC24, EC44, EC46, EC50 | Nguyen Van A | dom17_{ts}@domain.com | chưa có | `''` (rỗng) | `''` (rỗng) | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chuỗi rỗng là đại diện duy nhất của lớp 'rỗng'. | AI |
| TC-FR01-18 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu không có chữ hoa | EC26, EC44, EC46, EC50 | Nguyen Van A | dom18_{ts}@domain.com | chưa có | abcd1234! | abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Lấy danh nghĩa 'Abcd1234!' đổi 'A' thành 'a' → chỉ thiếu chữ hoa. | AI |
| TC-FR01-19 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu chỉ có chữ hoa có dấu tiếng Việt | EC27, EC44, EC46, EC50 | Nguyen Van A | dom19_{ts}@domain.com | chưa có | Êbcd1234! | Êbcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thay 'A' bằng 'Ê' → chữ hoa duy nhất nằm ngoài A–Z (A6). | AI |
| TC-FR01-20 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu không có chữ thường | EC29, EC44, EC46, EC50 | Nguyen Van A | dom20_{ts}@domain.com | chưa có | ABCD1234! | ABCD1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Viết hoa toàn bộ giá trị danh nghĩa → chỉ thiếu chữ thường. | AI |
| TC-FR01-21 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu chỉ có chữ thường có dấu tiếng Việt | EC30, EC44, EC46, EC50 | Nguyen Van A | dom21_{ts}@domain.com | chưa có | ABCê1234! | ABCê1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chữ thường duy nhất là 'ê' (A6), các điều kiện khác thoả. | AI |
| TC-FR01-22 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu không có chữ số | EC32, EC44, EC46, EC50 | Nguyen Van A | dom22_{ts}@domain.com | chưa có | Abcdefgh! | Abcdefgh! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | 9 ký tự, thay các chữ số bằng chữ thường → chỉ thiếu chữ số. | AI |
| TC-FR01-23 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu không có ký tự đặc biệt | EC35, EC44, EC46, EC50 | Nguyen Van A | dom23_{ts}@domain.com | chưa có | Abcd12345 | Abcd12345 | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thay '!' bằng '5' → chỉ thiếu ký tự đặc biệt. | AI |
| TC-FR01-24 | Kiểm tra từ chối đăng ký qua UI khi Mật khẩu chỉ có ký tự đặc biệt ngoài tập cho phép | EC36, EC44, EC46, EC50 | Nguyen Van A | dom24_{ts}@domain.com | chưa có | Abcd1234# | Abcd1234# | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thay '!' bằng '#' (ngoài tập, A5); độ dài và các loại ký tự khác giữ nguyên. | AI |
| TC-FR01-25 | Kiểm tra từ chối đăng ký qua UI khi Xác nhận mật khẩu rỗng | EC40, EC44, EC46, EC50 | Nguyen Van A | dom25_{ts}@domain.com | chưa có | Abcd1234! | `''` (rỗng) | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Xác nhận mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chuỗi rỗng (A7). | AI |
| TC-FR01-26 | Kiểm tra từ chối đăng ký qua UI khi Xác nhận mật khẩu khác Mật khẩu | EC41, EC44, EC46, EC50 | Nguyen Van A | dom26_{ts}@domain.com | chưa có | Abcd1234! | Abcd1234? | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Xác nhận mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chỉ khác ký tự cuối ('?' thay '!'); cả hai chuỗi đều là mật khẩu mạnh nên lỗi chỉ đến từ không khớp. | AI |
| TC-FR01-27 | Kiểm tra từ chối đăng ký qua UI khi Xác nhận mật khẩu chỉ khác Mật khẩu ở chữ hoa/thường | EC42, EC44, EC46, EC50 | Nguyen Van A | dom27_{ts}@domain.com | chưa có | Abcd1234! | abcd1234! | Có thông báo lỗi trên form (hộp lỗi đỏ, hoặc theo A16: không gửi POST /api/register và ô 'Xác nhận mật khẩu' có validationMessage không rỗng); URL vẫn là /register; so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Khác đúng một ký tự về hoa/thường (A7). | AI |

### Bước 3b — Minimum Set of Test Cases (Domain) · TS-DOM-API — Domain — minimum set, tầng API (FR-01)
**Ghi chú suite:** giữ đủ lớp theo quy tắc mỗi case không hợp lệ phủ một lớp
**Tiền điều kiện:** Trước mỗi lượt chạy cả suite: khởi động lại backend (node server.js) để CSDL seed sạch, có admin@eshop.com và test@eshop.com (A13).; Có token admin: POST /api/login với admin@eshop.com / Admin123! (dùng cho GET/DELETE /api/admin/users, A12).; Thay {ts} trong cột Email bằng Date.now() lúc chạy case để email là duy nhất (A19).

**Quy trình chung:**
1. Gọi GET /api/admin/users (token admin) và lưu danh sách id/email/name. → HTTP 200; danh sách có admin@eshop.com và test@eshop.com.
2. Gửi đúng một request POST http://localhost:3000/api/register, header Content-Type: application/json. Body gồm khoá name/email/password lấy từ cột Họ Tên/Email/Mật khẩu: '— thiếu trường —' = bỏ khoá khỏi body; 'số …' = giá trị số JSON; `''` = chuỗi rỗng; khoảng trắng (␣) giữ nguyên. → Nhận được phản hồi HTTP.
3. Ghi lại HTTP status và body JSON của phản hồi. → Khớp phần API của cột Expected.
4. Gọi lại GET /api/admin/users và so với danh sách lưu ở bước 1. → Số user mới và name/email của user mới như cột Expected (oracle tương đối).

**Dọn dẹp:** Sau mỗi case, kể cả khi Fail: xoá mọi user mới so với danh sách ở bước 1 bằng DELETE /api/admin/users/:id (token admin). Nếu xoá thất bại: ghi vào notes của case, không đổi verdict (A19).

| #TC | Tiêu đề | EC phủ | Họ Tên | Email | Email trong CSDL | Mật khẩu | Expected | Lý do chọn input | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR01-28 | Kiểm tra đăng ký thành công qua API khi Họ Tên không dấu, email mới và mật khẩu mạnh | EC1, EC7, EC18, EC22, EC25, EC28, EC31, EC33, EC47, EC49 | Nguyen Van A | api28_{ts}@domain.com | chưa có | Abcd1234! | HTTP 200, body {"message": "User registered successfully", "id": n}; so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'api28_{ts}@domain.com' như cột dữ liệu. | Case hợp lệ thứ nhất: giá trị danh nghĩa đơn giản nhất của các lớp hợp lệ có căn cứ SRS (tên ASCII, email đúng mẫu chưa tồn tại, mật khẩu 9 ký tự chỉ dùng ký tự đặc biệt trong tập). | AI |
| TC-FR01-29 | Kiểm tra đăng ký thành công qua API khi Họ Tên có dấu và mật khẩu có thêm ký tự đặc biệt ngoài tập | EC2, EC7, EC18, EC22, EC25, EC28, EC31, EC34, EC47, EC49 | Nguyễn Văn Ánh | api29_{ts}@domain.com | chưa có | Abcd1234!# | HTTP 200, body {"message": "User registered successfully", "id": n}; so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyễn Văn Ánh' và email 'api29_{ts}@domain.com' như cột dữ liệu. | Case hợp lệ thứ hai: phủ các lớp hợp lệ còn lại có căn cứ SRS (EC2 tên có dấu — SRS không giới hạn ký tự; EC34 — A5 cho phép ký tự ngoài tập đi kèm). | AI |
| TC-FR01-30 | Kiểm tra đăng ký thành công qua API khi email có khoảng trắng đầu/cuối | EC8, EC47, EC49 | Nguyen Van A | `␣␣api30_{ts}@domain.com␣␣` | chưa có | Abcd1234! | HTTP 200, body {"message": "User registered successfully", "id": n}; so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'api30_{ts}@domain.com' như cột dữ liệu. Email lưu đã được cắt khoảng trắng (A3). | Lớp dựa trên giả định A3 nên tách thành case riêng; hai khoảng trắng mỗi bên, phần còn lại là email mới đúng mẫu. | AI |
| TC-FR01-31 | Kiểm tra đăng ký thành công qua API khi email chỉ khác hoa/thường với tài khoản đã có | EC19, EC47, EC49 | Nguyen Van A | TEST@eshop.com | đã có 'test@eshop.com' (seed) | Abcd1234! | HTTP 200, body {"message": "User registered successfully", "id": n}; so với danh sách lấy ở bước 1 của chính case: đúng 1 user mới, có name 'Nguyen Van A' và email 'TEST@eshop.com' như cột dữ liệu; user seed 'test@eshop.com' không bị sửa. | Lớp dựa trên giả định A3 nên tách thành case riêng; biến thể 'TEST@eshop.com' khác biến thể của case UI để hai case không phụ thuộc nhau. | AI |
| TC-FR01-32 | Kiểm tra từ chối đăng ký qua API khi Họ Tên rỗng | EC3, EC48, EC50 | `''` (rỗng) | api32_{ts}@domain.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chuỗi rỗng là đại diện duy nhất của lớp 'rỗng'. | AI |
| TC-FR01-33 | Kiểm tra từ chối đăng ký qua API khi Họ Tên chỉ gồm khoảng trắng | EC4, EC48, EC50 | `␣␣␣` | api33_{ts}@domain.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | 3 khoảng trắng: vượt qua required của HTML5 nhưng vẫn rỗng sau khi cắt (A1). | AI |
| TC-FR01-34 | Kiểm tra từ chối đăng ký qua API khi Email rỗng | EC9, EC48, EC50 | Nguyen Van A | `''` (rỗng) | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chuỗi rỗng là đại diện duy nhất của lớp 'rỗng'. | AI |
| TC-FR01-35 | Kiểm tra từ chối đăng ký qua API khi Email không có ký tự '@' | EC10, EC48, EC50 | Nguyen Van A | dom35_{ts}domain.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Giữ nguyên các phần khác của mẫu, chỉ bỏ '@' để lỗi chỉ đến từ thiếu '@'. | AI |
| TC-FR01-36 | Kiểm tra từ chối đăng ký qua API khi Email có hai ký tự '@' | EC11, EC48, EC50 | Nguyen Van A | dom36@x_{ts}@domain.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thêm đúng một '@' thừa, phần local và domain vẫn không rỗng. | AI |
| TC-FR01-37 | Kiểm tra từ chối đăng ký qua API khi Email có phần local rỗng | EC12, EC48, EC50 | Nguyen Van A | @dom{ts}.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Domain đúng mẫu, chỉ thiếu phần trước '@'. | AI |
| TC-FR01-38 | Kiểm tra từ chối đăng ký qua API khi Email có phần domain rỗng | EC13, EC48, EC50 | Nguyen Van A | dom38_{ts}@ | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Phần local đúng mẫu, chỉ thiếu phần sau '@'. | AI |
| TC-FR01-39 | Kiểm tra từ chối đăng ký qua API khi Email có domain không chứa dấu chấm | EC14, EC48, EC50 | Nguyen Van A | dom39_{ts}@domain | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | HTML5 type=email chấp nhận dạng này nhưng thiếu .tld theo A2 — đại diện điển hình nhất của lớp. | AI |
| TC-FR01-40 | Kiểm tra từ chối đăng ký qua API khi Email có khoảng trắng ở giữa phần local | EC15, EC48, EC50 | Nguyen Van A | dom 40_{ts}@domain.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Một khoảng trắng duy nhất ở giữa, đầu/cuối không có khoảng trắng để không lẫn với EC8. | AI |
| TC-FR01-41 | Kiểm tra từ chối đăng ký qua API khi Email trùng chính xác tài khoản đã có | EC20, EC48, EC50 | Nguyen Van A | test@eshop.com | đã có 'test@eshop.com' (seed) | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Tài khoản seed luôn có sau khi backend khởi động (A13). | AI |
| TC-FR01-42 | Kiểm tra từ chối đăng ký qua API khi Email trùng tài khoản đã có sau khi cắt khoảng trắng đầu/cuối | EC21, EC48, EC50 | Nguyen Van A | `␣test@eshop.com␣` | đã có 'test@eshop.com' (seed) | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Một khoảng trắng mỗi bên — ít nhất để khác chuỗi nguyên văn nhưng trùng sau khi cắt (A3). | AI |
| TC-FR01-43 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu 7 ký tự thoả các điều kiện còn lại | EC23, EC48, EC50 | Nguyen Van A | api43_{ts}@domain.com | chưa có | Abc12!x | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | 7 ký tự có đủ chữ hoa, chữ thường, chữ số và '!' → chỉ vi phạm độ dài. Điểm 7 được xét lại ở BVA. | AI |
| TC-FR01-44 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu rỗng | EC24, EC48, EC50 | Nguyen Van A | api44_{ts}@domain.com | chưa có | `''` (rỗng) | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chuỗi rỗng là đại diện duy nhất của lớp 'rỗng'. | AI |
| TC-FR01-45 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu không có chữ hoa | EC26, EC48, EC50 | Nguyen Van A | api45_{ts}@domain.com | chưa có | abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Lấy danh nghĩa 'Abcd1234!' đổi 'A' thành 'a' → chỉ thiếu chữ hoa. | AI |
| TC-FR01-46 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu chỉ có chữ hoa có dấu tiếng Việt | EC27, EC48, EC50 | Nguyen Van A | api46_{ts}@domain.com | chưa có | Êbcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thay 'A' bằng 'Ê' → chữ hoa duy nhất nằm ngoài A–Z (A6). | AI |
| TC-FR01-47 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu không có chữ thường | EC29, EC48, EC50 | Nguyen Van A | api47_{ts}@domain.com | chưa có | ABCD1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Viết hoa toàn bộ giá trị danh nghĩa → chỉ thiếu chữ thường. | AI |
| TC-FR01-48 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu chỉ có chữ thường có dấu tiếng Việt | EC30, EC48, EC50 | Nguyen Van A | api48_{ts}@domain.com | chưa có | ABCê1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Chữ thường duy nhất là 'ê' (A6), các điều kiện khác thoả. | AI |
| TC-FR01-49 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu không có chữ số | EC32, EC48, EC50 | Nguyen Van A | api49_{ts}@domain.com | chưa có | Abcdefgh! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | 9 ký tự, thay các chữ số bằng chữ thường → chỉ thiếu chữ số. | AI |
| TC-FR01-50 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu không có ký tự đặc biệt | EC35, EC48, EC50 | Nguyen Van A | api50_{ts}@domain.com | chưa có | Abcd12345 | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thay '!' bằng '5' → chỉ thiếu ký tự đặc biệt. | AI |
| TC-FR01-51 | Kiểm tra từ chối đăng ký qua API khi Mật khẩu chỉ có ký tự đặc biệt ngoài tập cho phép | EC36, EC48, EC50 | Nguyen Van A | api51_{ts}@domain.com | chưa có | Abcd1234# | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Thay '!' bằng '#' (ngoài tập, A5); độ dài và các loại ký tự khác giữ nguyên. | AI |
| TC-FR01-52 | Kiểm tra từ chối đăng ký qua API khi body thiếu trường name | EC5, EC48, EC50 | — thiếu trường — | api52_{ts}@domain.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Bỏ hẳn khoá name khỏi body — đại diện cho 'thiếu hoặc null' (A15). | AI |
| TC-FR01-53 | Kiểm tra từ chối đăng ký qua API khi name là số JSON | EC6, EC48, EC50 | số 123 | api53_{ts}@domain.com | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Giá trị số JSON thay cho chuỗi (A15). | AI |
| TC-FR01-54 | Kiểm tra từ chối đăng ký qua API khi body thiếu trường email | EC16, EC48, EC50 | Nguyen Van A | — thiếu trường — | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Bỏ hẳn khoá email khỏi body (A15). | AI |
| TC-FR01-55 | Kiểm tra từ chối đăng ký qua API khi email là số JSON | EC17, EC48, EC50 | Nguyen Van A | số 123 | chưa có | Abcd1234! | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Giá trị số JSON thay cho chuỗi (A15). | AI |
| TC-FR01-56 | Kiểm tra từ chối đăng ký qua API khi body thiếu trường password | EC37, EC48, EC50 | Nguyen Van A | api56_{ts}@domain.com | chưa có | — thiếu trường — | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Bỏ hẳn khoá password khỏi body (A15). | AI |
| TC-FR01-57 | Kiểm tra từ chối đăng ký qua API khi password là số JSON | EC38, EC48, EC50 | Nguyen Van A | api57_{ts}@domain.com | chưa có | số 12345678 | HTTP 4xx (không phải 2xx, không phải 5xx), body JSON có trường error (A11); so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa. | Số 8 chữ số: đủ độ dài nếu bị ép thành chuỗi, nên lỗi chỉ đến từ sai kiểu (A15). | AI |

### TS-GUI — GUI — thuộc tính form (FR-22) và sự tồn tại trường (FR-01.9)
| #TC | Tiêu đề | EC phủ | Expected | Lý do chọn input | Nguồn |
|---|---|---|---|---|---|
| TC-FR01-90 | Kiểm tra ký hiệu * bên cạnh nhãn khi xem các trường bắt buộc của form Đăng ký |  | Cả 4 nhãn trường bắt buộc theo FR-01 đều có ký hiệu '*'. | FR-01 liệt kê 4 trường bắt buộc; FR-22.1 yêu cầu '*' cho mọi trường bắt buộc. | AI |
| TC-FR01-91 | Kiểm tra thuộc tính type của ô Email khi mở form Đăng ký |  | Ô Email có type="email". | Kiểm trực tiếp thuộc tính mà FR-22.2 quy định. | AI |
| TC-FR01-92 | Kiểm tra thuộc tính type của ô Mật khẩu và Xác nhận mật khẩu khi mở form Đăng ký |  | Ô Mật khẩu và ô Xác nhận mật khẩu đều có type="password" và che ký tự đã nhập. | FR-22.3 quy định type=password; áp dụng cho cả ô Xác nhận mật khẩu theo A18. | AI |
| TC-FR01-93 | Kiểm tra vị trí thông báo lỗi so với nút 'Đăng Ký' khi mật khẩu thiếu chữ hoa |  | Thông báo lỗi nằm phía trên nút 'Đăng Ký'. | Chọn dữ liệu vượt qua kiểm tra HTML5 để thông báo lỗi chắc chắn nằm trong DOM và đo được vị trí (A16). | AI |
| TC-FR01-94 | Kiểm tra sự tồn tại của trường Xác nhận mật khẩu khi mở form Đăng ký |  | Form có trường Xác nhận mật khẩu (FR-01.9). | Case kiểm sự tồn tại của trường mà A17 nhắc tới; tách khỏi các case nhập liệu để kết luận riêng. | AI |

**Các bước chi tiết:**

**TC-FR01-90** — Kiểm tra ký hiệu * bên cạnh nhãn khi xem các trường bắt buộc của form Đăng ký

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.
- Dữ liệu: Nhãn: 'Họ Tên', 'Email', 'Mật khẩu', 'Xác nhận mật khẩu'
- Bước 1: Mở http://localhost:5173/register. → Form 'Đăng Ký Tài Khoản' hiển thị.
- Bước 2: Đọc nhãn của 4 trường 'Họ Tên', 'Email', 'Mật khẩu', 'Xác nhận mật khẩu'. → Mỗi nhãn có ký tự '*' ngay bên cạnh tên trường.
- Dọn dẹp: Không cần: case chỉ đọc thuộc tính giao diện, không gửi form, không tạo dữ liệu.

**TC-FR01-91** — Kiểm tra thuộc tính type của ô Email khi mở form Đăng ký

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.
- Dữ liệu: Thuộc tính cần đọc: type của ô 'Email'
- Bước 1: Mở http://localhost:5173/register. → Form 'Đăng Ký Tài Khoản' hiển thị.
- Bước 2: Đọc thuộc tính type của thẻ input thuộc nhãn 'Email' (DevTools hoặc locator.getAttribute('type')). → Giá trị type là "email".
- Dọn dẹp: Không cần: case chỉ đọc thuộc tính giao diện, không gửi form, không tạo dữ liệu.

**TC-FR01-92** — Kiểm tra thuộc tính type của ô Mật khẩu và Xác nhận mật khẩu khi mở form Đăng ký

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.
- Dữ liệu: Mật khẩu: 'Abcd1234!'
- Bước 1: Mở http://localhost:5173/register. → Form 'Đăng Ký Tài Khoản' hiển thị.
- Bước 2: Đọc thuộc tính type của thẻ input thuộc nhãn 'Mật khẩu'. → Giá trị type là "password".
- Bước 3: Gõ 'Abcd1234!' vào ô 'Mật khẩu'. → Ô hiển thị ký tự che (•), không hiện chuỗi 'Abcd1234!'.
- Bước 4: Đọc thuộc tính type của thẻ input thuộc nhãn 'Xác nhận mật khẩu' (A18). → Giá trị type là "password".
- Dọn dẹp: Không cần: case chỉ đọc thuộc tính giao diện, không gửi form, không tạo dữ liệu.

**TC-FR01-93** — Kiểm tra vị trí thông báo lỗi so với nút 'Đăng Ký' khi mật khẩu thiếu chữ hoa

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.
- Dữ liệu: Mật khẩu 'abcd1234!' (thiếu chữ hoa); Email 'gui93_{ts}@domain.com'
- Bước 1: Mở http://localhost:5173/register. → Form 'Đăng Ký Tài Khoản' hiển thị.
- Bước 2: Nhập Họ Tên 'Nguyen Van A', Email 'gui93_{ts}@domain.com', Mật khẩu 'abcd1234!', Xác nhận mật khẩu 'abcd1234!' rồi bấm 'Đăng Ký'. → Hộp thông báo lỗi xuất hiện trong DOM (mọi ô đã điền nên trình duyệt không chặn bằng bong bóng HTML5).
- Bước 3: Lấy boundingBox của hộp lỗi và của nút 'Đăng Ký'. → Cạnh dưới của hộp lỗi (y + height) ≤ cạnh trên (y) của nút 'Đăng Ký'.
- Dọn dẹp: Nếu user 'gui93_{ts}@domain.com' bị tạo: xoá bằng DELETE /api/admin/users/:id (token admin).

**TC-FR01-94** — Kiểm tra sự tồn tại của trường Xác nhận mật khẩu khi mở form Đăng ký

- Tiền điều kiện: Web http://localhost:5173 và backend http://localhost:3000 đang chạy.
- Dữ liệu: Nhãn cần tìm: 'Xác nhận mật khẩu'
- Bước 1: Mở http://localhost:5173/register. → Form 'Đăng Ký Tài Khoản' hiển thị.
- Bước 2: Tìm ô nhập có nhãn 'Xác nhận mật khẩu' trong form. → Có đúng 1 ô nhập với nhãn 'Xác nhận mật khẩu', nằm sau ô 'Mật khẩu'.
- Dọn dẹp: Không cần: case chỉ đọc thuộc tính giao diện, không gửi form, không tạo dữ liệu.

### Truy vết yêu cầu ↔ test case
| Yêu cầu | Test case | Số TC |
|---|---|---|
| FR-01.1 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-05, TC-FR01-06, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-32, TC-FR01-33, TC-FR01-52, TC-FR01-53 | 14 |
| FR-01.2 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-07, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-34, TC-FR01-54, TC-FR01-55 | 12 |
| FR-01.3 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-08, TC-FR01-09, TC-FR01-10, TC-FR01-11, TC-FR01-12, TC-FR01-13, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-35, TC-FR01-36, TC-FR01-37, TC-FR01-38, TC-FR01-39, TC-FR01-40 | 20 |
| FR-01.4 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-14, TC-FR01-15, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-41, TC-FR01-42 | 12 |
| FR-01.5 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-17, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-44, TC-FR01-56, TC-FR01-57 | 12 |
| FR-01.6 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-16, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-43 | 10 |
| FR-01.7a | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-18, TC-FR01-19, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-45, TC-FR01-46 | 12 |
| FR-01.7b | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-20, TC-FR01-21, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-47, TC-FR01-48 | 12 |
| FR-01.7c | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-22, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-49 | 10 |
| FR-01.8 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-23, TC-FR01-24, TC-FR01-28, TC-FR01-29, TC-FR01-30, TC-FR01-31, TC-FR01-50, TC-FR01-51 | 12 |
| FR-01.9 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04, TC-FR01-25, TC-FR01-26, TC-FR01-27, TC-FR01-94 | 8 |
| FR-01.10 | TC-FR01-01, TC-FR01-02, TC-FR01-03, TC-FR01-04 | 4 |
| FR-22.1 | TC-FR01-90 | 1 |
| FR-22.2 | TC-FR01-91 | 1 |
| FR-22.3 | TC-FR01-92 | 1 |
| FR-22.4 | TC-FR01-93 | 1 |

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
- A17 (Thiếu ô Xác nhận mật khẩu): nếu form không có ô Xác nhận mật khẩu (xem note V5): case kiểm sự tồn tại của trường (TC-FR01-94) → Fail; case có V5 = EC39 bỏ qua bước nhập V5 và ghi notes; chỉ các case EC40–EC42 → Blocked kèm mã bug. Không xoá case.
- A18 (FR-22.3 cho ô Xác nhận mật khẩu): FR-22.3 chỉ nêu 'Trường Mật khẩu'. Giả định ô Xác nhận mật khẩu cũng là trường mật khẩu → cũng phải dùng type="password" (kiểm ở TC-FR01-92).
- A19 (Độc lập giữa các case): tính độc lập giữa các case dựa trên dữ liệu riêng ({ts}) và oracle tương đối; cleanup là lớp bảo vệ thứ hai, vì API xoá user (FR-19) nằm ngoài phạm vi và có thể có lỗi.

**Tổng:** 62 TC · Not run: 62 · Nguồn: AI 62
