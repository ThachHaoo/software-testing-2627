# Kiểm trùng issue FR-02 (2026-11-05)

Nguồn: `gh issue list -R tkob-team/eshop-sut --state all -L 500 --json number,title,author,body,state` (158 issue), lọc title+body theo `FR-?02|login_attempts|khóa tài khoản|lockout|locked|180 giây|+2|server.js:54/57`. Chỉ liệt kê issue FR-02 (bỏ kết quả khớp nhầm của FR-01/04/07/08/15/20).

## Trùng trực tiếp finding AI (server.js:54 / :57)

| Issue | Author | Trạng thái | Tiêu đề |
|---|---|---|---|
| #1 | nphoang-itus | OPEN | [BUG-FR02-01] Bộ đếm đăng nhập sai tăng 2 mỗi lần thay vì đúng 1 |
| #2 | nphoang-itus | OPEN | [BUG-FR02-02] Tài khoản bị khóa ngay sau lần sai thứ 2 (đặc tả: từ lần thứ 3) |
| #3 | nphoang-itus | OPEN | [BUG-FR02-03] Thời gian khóa 180 giây thay vì 30 giây |

→ CL-52 Failed vì nguyên nhân này thì ghi "đã biết – #1/#2/#3", không tạo issue mới.

## Issue FR-02 khác (đối chiếu khi gộp kết quả C2 – Đăng nhập)

| Issue | Tiêu đề |
|---|---|
| #4 | [BUG-FR02-04] Ô email form đăng nhập Web là `type="text"`, không kiểm tra định dạng |
| #5 | [BUG-FR02-05] Ô mật khẩu form đăng nhập Web là `type="text"`: mật khẩu hiển thị rõ |
| #6 | [BUG-FR02-06] Thông báo lỗi đăng nhập nằm dưới nút submit |
| #7 | [BUG-FR02-07] Trường bắt buộc của form đăng nhập không có ký hiệu `*` |
| #8 | [BUG-FR02-08] Phản hồi đăng nhập và `GET /api/users/me` trả về mật khẩu dạng thô |
| #9 | [BUG-FR02-09] Form đăng nhập: tiêu đề "Đăng Ký", nhãn "Username", nút "Sign In" |
| #62 | [BUG-FR02-10] Email đăng nhập phân biệt hoa/thường |
| #63 | [BUG-FR02-11] Thông báo khóa tài khoản lộ trạng thái |
| #64 | [BUG-FR02-12] Hết khóa nhưng bộ đếm không đặt lại |

Tất cả OPEN, author nphoang-itus.
