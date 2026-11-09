# Danh sách Failed – T1 checklist C2 (sinh bằng `tools/failed_list_hw03.py` từ `checklist.json`)

47 item Failed · ô Failed theo nền tảng: P1 44, P2 47, P3 44 (tổng 135).
Đối chiếu `HW03/bugs/issues.json` (158 issue nhóm, tới #203) và BUG-01…57 HW02 của em: **trùng 14**, **trùng một phần 4** (màn còn lại là MỚI), **MỚI 28**; loại khỏi lập bug: CL-34 (quyết định 5/6a).
CL-30, CL-48 trên P3 = Blocked (T-P3: Playwright timeout) nên không còn trong danh sách.

Cột *kết quả từ*: `tay` = lượt chạy tay trên trình duyệt thật; `auto` = lượt Playwright (P1 Chrome 157 tham chiếu – Q1; P2 Firefox 131 của Playwright; P3 Chrome Android thật). Đối chiếu trùng do AI làm theo tiêu đề issue + màn hình + notes; **SV xác nhận** trước khi viết BUG-58… (T1 bước 6). Mỗi item = một ứng viên bug, chưa phải bug.

| # | Item | Màn hình | Mục kiểm tra | Failed trên | Kết quả từ | Issue trùng / MỚI | Ghi chú đối chiếu |
|---|---|---|---|---|---|---|---|
| 1 | CL-01 | Tất cả màn C2 | Ngôn ngữ giao diện nhất quán tiếng Việt | P1, P2, P3 | tay | trùng #9 | notes cả 3 nền tảng chỉ nêu chuỗi tiếng Anh ở Đăng nhập ("Username", "Sign In") |
| 2 | CL-02 | Đăng nhập, Quên mật khẩu, Hồ sơ | Mỗi trang có đúng 1 thẻ <h1> | P1, P2, P3 | auto | **MỚI** |  |
| 3 | CL-03 | Đăng nhập | Tiêu đề trang mô tả đúng chức năng Đăng nhập | P1, P2, P3 | auto | trùng #9 | tiêu đề form Đăng nhập là "Đăng Ký" |
| 4 | CL-04 | Tất cả màn C2 | Nút hành động tích cực màu xanh dương | P1, P2, P3 | auto | trùng #160 | SV chốt trùng (5/6b): #160 nút tích cực màu xanh lá |
| 5 | CL-06 | Quên mật khẩu (bước 2) | Nút chính và nút phụ phân biệt được bằng hình thức | P1, P2, P3 | tay | **MỚI** |  |
| 6 | CL-08 | Lịch sử đơn | Tổng tiền dùng ký hiệu ₫ và phân cách hàng nghìn | P2, P3 | tay | trùng #170 (BUG-24) | SV chốt trùng (5/6b): #170 định dạng tiền |
| 7 | CL-09 | Lịch sử đơn | Ngày đặt hiển thị nhất quán theo định dạng Việt Nam | P2, P3 | tay | **MỚI** |  |
| 8 | CL-10 | Đăng nhập | Thứ tự Tab theo vị trí hiển thị (trên→dưới, trái→phải) | P1, P2 | auto | **MỚI** |  |
| 9 | CL-12 | Quên mật khẩu (bước 2) | Thứ tự Tab ở bước 2 theo vị trí hiển thị (trên→dưới, trái→phải) | P1, P2 | auto | **MỚI** |  |
| 10 | CL-13 | Tất cả màn C2 | Tiêu đề tab trình duyệt mô tả trang | P1, P2, P3 | auto | **MỚI** |  |
| 11 | CL-14 | Tất cả màn C2 | Khai báo ngôn ngữ trang là tiếng Việt | P1, P2, P3 | auto | **MỚI** |  |
| 12 | CL-16 | Navbar | Tên người dùng hiển thị an toàn (không render HTML) | P1, P2, P3 | auto | trùng #122 | cùng lời chào navbar; HW02 BUG-11/#27 là XSS ở Đăng ký (nguồn dữ liệu khác) |
| 13 | CL-17 | Đăng nhập, Quên mật khẩu (bước 1) | Ô Email dùng type="email" | P1, P2, P3 | auto | trùng một phần #4 + MỚI | #4 phủ /login; /forgot-password bước 1 chưa có issue |
| 14 | CL-66 | Đăng nhập, Quên mật khẩu (bước 1) | Email sai định dạng bị chặn trước khi gửi | P1, P2, P3 | auto | trùng một phần #4 + MỚI | #4 (không kiểm tra định dạng) phủ /login; /forgot-password chưa có issue |
| 15 | CL-18 | Đăng nhập | Nhãn ô đăng nhập là 'Email' | P1, P2, P3 | auto | trùng #9 | nhãn "Username" |
| 16 | CL-19 | Đăng nhập, Quên mật khẩu (bước 2) | Ô mật khẩu che ký tự | P1, P2, P3 | auto | trùng #5 | chỉ /login fail; bước 2 Quên MK đạt (notes auto) |
| 17 | CL-20 | Đăng nhập, Quên mật khẩu | Dấu * trên nhãn trường bắt buộc | P1, P2, P3 | auto | trùng một phần #7 + MỚI | #7 phủ /login; Quên MK bước 1/2 chưa có issue |
| 18 | CL-21 | Hồ sơ | Dấu * trên trường mà form bắt buộc nhập | P1, P2, P3 | auto | **MỚI** |  |
| 19 | CL-22 | Đăng nhập | Thông báo lỗi đăng nhập nằm phía trên nút submit | P1, P2, P3 | auto | trùng #6 |  |
| 20 | CL-23 | Quên mật khẩu, Hồ sơ | Thông báo lỗi validate hiển thị trong trang, phía trên nút submit | P1, P2, P3 | auto | **MỚI** |  |
| 21 | CL-24 | Quên mật khẩu | Có chỉ báo bước (Step Indicator) | P1, P2, P3 | tay | **MỚI** |  |
| 22 | CL-25 | Quên mật khẩu (bước 1) | Có nút 'Quay lại đăng nhập' | P1, P2, P3 | auto | **MỚI** |  |
| 23 | CL-26 | Quên mật khẩu (bước 2) | Có ô 'Xác nhận mật khẩu mới' | P1, P2, P3 | auto | **MỚI** (liên quan #30 (BUG-14)) | #30 là form Đăng ký; Quên MK bước 2 chưa có issue |
| 24 | CL-28 | Quên mật khẩu (bước 2) | Mã OTP hiển thị có đúng 6 chữ số | P1, P2, P3 | auto | **MỚI** |  |
| 25 | CL-29 | Quên mật khẩu (bước 2) | Mật khẩu mới hợp lệ theo FR-01 được chấp nhận | P1, P2, P3 | auto | **MỚI** (liên quan #17 (BUG-01)) | #17 cùng thông báo "Mật khẩu quá yếu!" ở Đăng ký; Quên MK bước 2 chưa có issue |
| 26 | CL-31 | Hồ sơ | SĐT hợp lệ (bắt đầu 0, 10–11 số) được chấp nhận | P1, P2, P3 | auto | trùng #111, #112 | Web từ chối SĐT 10/11 số đầu 0 |
| 27 | CL-32 | Hồ sơ | SĐT không hợp lệ bị từ chối, thông báo nêu đúng quy tắc | P1, P2, P3 | auto | trùng một phần #97, #113 + MỚI | #97 (API lưu SĐT 9 số), #113 (Web nhận đầu khác 0); phần thông báo không nêu quy tắc chưa có issue |
| 28 | CL-34 | Hồ sơ | Họ Tên chỉ gồm khoảng trắng bị từ chối | P2 | auto | loại khỏi lập bug (5/6a) | xem notes |
| 29 | CL-37 | Hồ sơ | Cập nhật hồ sơ được lưu bền | P1, P2, P3 | auto | **MỚI** (liên quan #111, #123) | SV xem: trường quay về giá trị cũ sau F5, có thể do #111 chặn lưu hoặc #123 |
| 30 | CL-38 | Đăng nhập, Hồ sơ | Nhãn gắn với ô nhập (bấm nhãn → focus ô) | P1, P2, P3 | auto | **MỚI** |  |
| 31 | CL-40 | Navbar | Navbar highlight trang đang chọn | P1, P2, P3 | auto | trùng #169 (BUG-23) | SV chốt trùng (5/6b): #169 navbar không highlight trang hiện tại |
| 32 | CL-41 | Navbar | Link 'Giỏ hàng' có badge số lượng | P1, P2, P3 | auto | trùng #166 (BUG-20) | badge Giỏ hàng trên navbar (HW02 của SV) |
| 33 | CL-42 | Navbar | Nút đăng xuất có nhãn 'Đăng xuất' | P1, P2, P3 | auto | **MỚI** |  |
| 34 | CL-49 | Hồ sơ | /profile khi chưa đăng nhập dẫn được tới Đăng nhập | P1, P2, P3 | auto | **MỚI** |  |
| 35 | CL-50 | Tất cả màn C2 | URL không tồn tại hiển thị trang 404 có lối về | P1, P2, P3 | auto | **MỚI** |  |
| 36 | CL-52 | Đăng nhập | Sai 3 lần liên tiếp → khoá 30 giây | P1, P2, P3 | tay | trùng #1, #2, #3 | bộ đếm +2, khoá từ lần 2, khoá 180 s |
| 37 | CL-53 | Đăng nhập | Có chỉ báo đang xử lý và chống gửi trùng | P1, P2, P3 | tay | **MỚI** |  |
| 38 | CL-56 | Hồ sơ, Navbar | Đổi Họ Tên cập nhật ngay trên navbar | P1, P2, P3 | auto | **MỚI** |  |
| 39 | CL-59 | Lịch sử đơn | Không cho người dùng huỷ đơn ở trạng thái không được huỷ | P1, P2, P3 | auto | **MỚI** |  |
| 40 | CL-60 | Lịch sử đơn | Huỷ đơn có hộp xác nhận | P1, P2, P3 | auto | trùng #165 (BUG-19) | SV chốt trùng (5/6b): #165 thao tác huỷ/xoá không có hộp xác nhận |
| 41 | CL-62 | Lịch sử đơn | Empty state có hình minh hoạ và thông báo thân thiện | P1, P2, P3 | tay | trùng #167 (BUG-21) | SV chốt trùng (5/6b): #167 empty state không có hình minh hoạ |
| 42 | CL-63 | Lịch sử đơn | Có trạng thái đang tải khi lấy lịch sử đơn | P1, P2, P3 | tay | **MỚI** |  |
| 43 | SV-02 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Khả năng tự động điền (Autofill/Autocompletion) và dán (Paste) dữ liệu vào các trường nhập liệu | P1, P2, P3 | tay | **MỚI** |  |
| 44 | SV-03 | Đăng nhập, Quên mật khẩu B2, Hồ sơ | Trả lại con trỏ focus về đúng trường nhập liệu bị lỗi sau khi submit thất bại | P1, P2, P3 | auto | **MỚI** |  |
| 45 | SV-04 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Độ tương phản màu sắc của văn bản và nhãn so với nền (Color Contrast Ratio) | P1, P2, P3 | tay | **MỚI** |  |
| 46 | SV-05 | Đăng nhập, Quên mật khẩu B1 / B2, Hồ sơ | Kích thước vùng tương tác của con trỏ (Target Size) đối với các nút và link | P1, P2, P3 | auto | **MỚI** |  |
| 47 | SV-06 | Quên mật khẩu B1 / B2, Hồ sơ | Chống gửi trùng dữ liệu (Debounce/Disable) khi nhấp đúp/nhấp liên tiếp vào nút submit ở điều kiện mạng bình thường | P1, P2, P3 | auto | **MỚI** |  |
