# A_FR01 – kiểu assertion theo TC (bước 3, bản AI)

Spec: `HW04/tests/A_FR01.spec.ts`. Mọi assertion là `expect.soft` (một TC ghi đủ mọi điểm lệch). Oracle đọc từ `expected` nguyên văn trong `HW04/data/A_FR01.json` (hàm `oracleOf`); dữ liệu nhập lấy từ `inputs`.

## 4 kiểu assertion

| Kiểu | Matcher | Kiểm gì |
|---|---|---|
| UI – trạng thái | `toHaveURL`, `toBeVisible` | URL sau khi bấm "Đăng Ký" (`/login` hoặc vẫn `/register`); hộp lỗi đỏ hiện |
| UI – nội dung thông báo | `toHaveText`, `toContainText` | hộp lỗi có chữ; thông báo nhắc đúng trường/điều kiện mà expected nêu |
| Oracle dữ liệu qua API | `toEqual` | `GET /api/admin/users` trước/sau: danh sách user mới (name, email), user seed không bị sửa/xoá; không gửi `POST /api/register` (A16) |
| Đếm / giá trị | `toHaveValue`, `toHaveCount` | ô trống khi mở form và hiện đúng chuỗi đã gõ; số hộp lỗi = 0 khi expected "Không có thông báo lỗi" |

## Theo TC

| TC | Loại oracle | UI – trạng thái | Nội dung thông báo | API trước/sau (`toEqual`) | Đếm / giá trị |
|---|---|---|---|---|---|
| 01, 02, 64, 68, 74, 77 | thành công | `toHaveURL(/login)` | – | đúng 1 user mới `[{name, email}]` | `toHaveValue` ×6, `toHaveCount(0)` hộp lỗi |
| 211 | thành công + đăng nhập lại | `toHaveURL(/)` sau đăng nhập | – | đúng 1 user mới (name/email từ `inputs`, vì expected chỉ ghi "Đăng ký thành công") | `toHaveValue` ×6, `toHaveCount(0)` hộp lỗi đăng ký + đăng nhập; token localStorage `not.toBeNull` |
| 05, 07, 17 | từ chối, ô bắt buộc rỗng | `toHaveURL(/register)`; nếu không có validationMessage: `toBeVisible` hộp lỗi | nếu có hộp lỗi: `toHaveText(/\S/)` | không có user mới `[]`; seed không sửa/xoá `[]`; nếu trình duyệt chặn (A16): không gửi POST `[]` + validationMessage `not.toEqual('')` | `toHaveValue` ×6 |
| 18, 22, 23, 63 | từ chối, luật mật khẩu | như trên | như trên | như trên | `toHaveValue` ×6 |
| 202 | từ chối, "báo mật khẩu thiếu ký tự đặc biệt" | `toBeVisible` hộp lỗi (expected không nêu URL) | `toHaveText(/\S/)`, `toContainText(/mật khẩu/i)`, `toContainText(/ký tự đặc biệt/i)` | không có user mới `[]` | `toHaveValue` ×6 |

## Ghi chú cho SV review

- Nhánh "hộp lỗi đỏ HOẶC A16" của expected từ chối được cài bằng: có validationMessage trên ô expected nêu → kiểm A16; không có → kiểm hộp lỗi. Nhánh chạy phụ thuộc phản ứng thật của form.
- Ô "Xác nhận mật khẩu" không có trên form → bỏ bước nhập, ghi annotation `A17` (theo notes HW02), không Blocked vì 15 TC đã chọn đều có V5 = V4.
- Tiền điều kiện "Email trong CSDL: chưa có" bị vi phạm → `blocked(...)`.
- `beforeAll`: restart backend (CSDL seed sạch) một lần mỗi lượt chạy; sau mỗi TC fixture `users` xoá user mới tạo.
