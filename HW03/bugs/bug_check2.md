# Kiểm lại 14 bug SV sửa (5/6f) – AI, chỉ đọc

Đối chiếu commit `496ad20` (SV sửa BUG-58, 62, 63, 64, 70, 72, 73, 75, 76, 78, 79, 80, 81, 82) với các điểm đã liệt kê trong `bug_check.md` (5/6e) và cùng tiêu chí (a)–(h). AI chỉ liệt kê, không đề xuất câu chữ, không sửa file BUG. Số liệu tái hiện tham chiếu `bugs/repro/repro_P1.json`, `repro_P2.json` (P1 Chrome, P2 Firefox Playwright; **P3 không chạy lại**).

Chung: 14/14 không còn `<SV viết>`/🔒; Severity/Priority không đổi (đúng thang); 0/14 tiêu đề có tiền tố `[HW03-C2…]`.

## Tổng hợp

| Nhóm | Số | Mã |
|---|---|---|
| Đã xử lý hết điểm của `bug_check.md`, không có điểm mới | 6 | BUG-58, 62, 70, 80, 81, 82 |
| Còn điểm chưa xử lý / điểm mới do lần sửa | 8 | BUG-63, 64, 72, 73, 75, 76, 78, 79 |

## Đã xử lý

- **BUG-58:** 3 câu Nhận định đều có "(chưa kiểm chứng)".
- **BUG-62:** Steps/Expected/Actual ghi nhãn thật ("Username", "Nhập Email của bạn"); Steps có bước nhập mật khẩu ở `/login` → làm đúng Steps ra 1 request `/api/login` (khớp repro cô lập).
- **BUG-70:** câu nguyên nhân có "(chưa kiểm chứng)"; dẫn `ForgotPassword.jsx:26` khớp mã SUT.
- **BUG-80:** Nhận định có "(chưa kiểm chứng)".
- **BUG-81:** Steps "ví dụ đơn #3"; Actual ghi cả số đơn theo Tiền điều kiện (#1…#5) và lượt auto (#8…#12).
- **BUG-82:** tiêu đề bỏ "Quên MK" (khớp Actual P1); Expected còn 1 nhánh (Autofill). Bước Autofill vẫn chưa được AI tái hiện (không chạy được bằng Playwright) – không đổi so với 5/6e.

## Còn điểm

### BUG-63
- Chưa xử lý (5/6e, cô lập): Actual Hồ sơ vẫn ghi "Cả 3 trường … khi để trống đều khiến form bị chặn". Repro: xoá Địa chỉ bị chặn là do ô SĐT đang trống (hộp thoại "Số điện thoại không hợp lệ…"), không phải do Địa chỉ; `Profile.jsx` không có `required`/kiểm tra cho Địa chỉ. (Expected đã sửa đúng tên nhãn.)

### BUG-64
- Actual phần Hồ sơ đổi sang hộp thoại "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số." (khớp repro AI trên P1, P2), nhưng ghi "Cả P1, P2 và P3": **P3 chưa có dữ kiện** cho giá trị `123` (Dữ kiện P3 trong file là lượt auto, hộp thoại "Cập nhật thành công!"). Mục "Dữ kiện (AI chép)" vẫn là lượt auto → Actual và Dữ kiện trong file không còn khớp nhau; nguồn của Actual mới (repro 5/6e) chưa được dẫn trong file.

### BUG-72
- **Mục "Dữ kiện (AI chép)" bị sửa:** dòng "Actual nguyên văn CL-32 P3 (auto)" bỏ đoạn "912345678 được lưu · Lỗi: Error:" – không còn khớp `notes_nt.P3` của CL-32 trong `checklist/checklist.json` (chuỗi gốc có đoạn này). Dòng P1, P2 giữ nguyên.
- Dòng mới "*(Tái hiện trên P1, P2, P3)*" ở mục Các bước: lượt tái hiện 5/6e chỉ chạy P1, P2; P3 chỉ có dữ kiện lượt auto.

### BUG-73
- Actual mới ghi hộp thoại "Số điện thoại không hợp lệ…" và "không gửi request API nào" cho "Cả P1, P2 và P3": hai dữ kiện này có ở repro P1, P2; **P3 chưa có** (Dữ kiện P3 auto chỉ ghi `sau F5: ["Test User","",""]`).

### BUG-75
- Tiền điều kiện / Steps gọi `912345678` là "Số điện thoại hợp lệ" – theo FR-04.2 (README.md:65) SĐT hợp lệ phải bắt đầu bằng 0; `912345678` chính là giá trị BUG-72 nêu là không hợp lệ. (Tên/giá trị nhất quán giữa 2 bug.)
- Actual "Cả P1, P2 và P3" với Steps mới (có SĐT `912345678`): P1, P2 có repro cô lập (lưu được, navbar không đổi khi chưa tải lại); **P3 chưa có dữ kiện** với điều kiện này – Dữ kiện P3 (auto) chạy khi SĐT trống, cập nhật bị chặn.

### BUG-76
- Expected bug đổi còn 1 nhánh "tự động chuyển hướng … về `/login`"; Expected item CL-49 (căn cứ Nielsen #3, #9) chấp nhận **hoặc** chuyển hướng **hoặc** thông báo kèm link/nút → Expected bug hẹp hơn căn cứ item.
- Định dạng: sau dòng Expected có dòng gạch đầu dòng rỗng `- ` và không còn dòng trống trước `## Actual`.

### BUG-78
- Steps 3, 4 mới dùng giá trị lọt kiểm tra của web (`Abcd efg1`, SĐT `912345678`), nhưng Actual vẫn ghi kết quả của giá trị bị chặn ("0 request, 2 hộp thoại" do bộ kiểm tra chặn). Làm đúng Steps mới, repro cô lập ra: B2 **2 request** `/api/reset-password` (hộp thoại "Đổi mật khẩu thành công!" rồi "Mã OTP không đúng hoặc có lỗi xảy ra."); Hồ sơ **2 request PUT**, 2 hộp thoại "Cập nhật thành công!" (P1, P2) → Steps và Actual không khớp.
- Steps 4 gọi `912345678` là "SĐT hợp lệ" (xem BUG-75).
- (Đã xử lý: bỏ câu TimeoutError.)

### BUG-79
- Chưa xử lý (5/6e): Actual P2/P3 "Trang tải xong là tất cả dữ liệu cũng xong hết" khớp Dữ kiện, nhưng ảnh `P3_CL-63_1` ("Bạn chưa có đơn hàng nào.") và `P3_CL-63_2` (bảng đơn) thể hiện trạng thái rỗng rồi mới tới bảng; repro P2 (trễ request, không phải throttling thật) cũng thấy trạng thái rỗng trước bảng.
- Actual P1 "hiển thị trạng thái rỗng … trước khi danh sách đơn hàng thực tế kịp tải ra" vẫn không có trong Dữ kiện P1 (repro P1 có thấy hiện tượng này).
