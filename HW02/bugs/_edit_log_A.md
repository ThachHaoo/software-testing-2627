# Nhật ký sửa issue A_FR01 (7/7e)

Đính chính 2026-10-20: chỉ thay mục `## Yêu cầu` trong body bằng mục tương ứng của `HW02/bugs/BUG-xx.md` sau commit 7/7e; phần còn lại của body giữ nguyên. Mỗi issue thêm 1 comment.

## #17 — BUG-01 — [FR-01] Đăng ký không cho mật khẩu hợp lệ, nó nói "Mật khẩu quá yếu!"

### Mục Yêu cầu — trước

```
- **FR-01.6:** Mật khẩu tối thiểu 8 ký tự.
- **FR-01.7a:** Mật khẩu có ít nhất 1 chữ hoa.
- **FR-01.7b:** Mật khẩu có ít nhất 1 chữ thường.
- **FR-01.7c:** Mật khẩu có ít nhất 1 chữ số.
- **FR-01.8:** Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &.
- **FR-01.10:** Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.
```

### Mục Yêu cầu — sau

```
- **FR-01.10:** Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.
- **Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8** (ngầm định — Actual chỉ có thông báo gộp, không xác định được luật riêng nào bị cài sai)
```

### Comment

> Đính chính 2026-10-20: trường Yêu cầu trước đây liệt kê cả yêu cầu không bị vi phạm; nay chỉ giữ FR-01.10; chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định — Actual chỉ có thông báo gộp, không xác định được luật riêng nào bị cài sai). Bước/Actual/Expected không đổi.

- Đã sửa body và kiểm lại bằng `gh issue view` (mục Yêu cầu khớp). Comment: https://github.com/tkob-team/eshop-sut/issues/17#issuecomment-6285166445

## #20 — BUG-04 — [FR-01] Backend API POST /api/register không kiểm tra Email (rỗng, sai định dạng, thiếu trường, sai kiểu) vẫn trả HTTP 200 và tạo user

### Mục Yêu cầu — trước

```
- **FR-01.1:** Người dùng phải cung cấp Họ Tên (trường bắt buộc).
- **FR-01.2:** Người dùng phải cung cấp Email (trường bắt buộc).
- **FR-01.3:** Email phải có định dạng hợp lệ (user@domain.com).
- **FR-01.5:** Người dùng phải cung cấp Mật khẩu (trường bắt buộc).
- **A2** (giả định, SRS im lặng): A2 (Email – định dạng): FR-01 chỉ đưa mẫu 'user@domain.com'. Giả định định dạng hợp lệ = <local>@<domain>.<tld>: đúng một '@', phần local không rỗng, phần domain có ít nhất một dấu '.' và không rỗng hai bên dấu chấm. FR-22 yêu cầu type="email" nên quy tắc HTML5 của trình duyệt dùng làm tham chiếu phụ. SRS không nêu độ dài tối đa → không kiểm cận trên độ dài email.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- **A15** (giả định, SRS im lặng): A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.
- **A21** (giả định, SRS im lặng): A21 (email chỉ gồm ký tự ASCII): FR-22.2 bắt ô Email dùng type="email". A2 lấy quy tắc HTML5 làm tham chiếu phụ, và theo định nghĩa “valid e-mail address” của HTML5, phần local chỉ gồm ký tự ASCII. Vì vậy email có ký tự ngoài ASCII là sai định dạng. → TC-219: tеst@eshop.com (chữ е Cyrillic) phải bị từ chối, 4xx, không tạo user. Thêm EC52 “Email có ký tự ngoài ASCII” (không hợp lệ), do TC-219 phủ. Nay case này có oracle, không còn là quan sát suông. (AI đề xuất, SV duyệt 2026-10-19)
```

### Mục Yêu cầu — sau

```
- **FR-01.1:** Người dùng phải cung cấp Họ Tên (trường bắt buộc).
- **FR-01.2:** Người dùng phải cung cấp Email (trường bắt buộc).
- **FR-01.3:** Email phải có định dạng hợp lệ (user@domain.com).
- **FR-01.5:** Người dùng phải cung cấp Mật khẩu (trường bắt buộc).
- **A2** (giả định, SRS im lặng): A2 (Email – định dạng): FR-01 chỉ đưa mẫu 'user@domain.com'. Giả định định dạng hợp lệ = <local>@<domain>.<tld>: đúng một '@', phần local không rỗng, phần domain có ít nhất một dấu '.' và không rỗng hai bên dấu chấm. FR-22 yêu cầu type="email" nên quy tắc HTML5 của trình duyệt dùng làm tham chiếu phụ. SRS không nêu độ dài tối đa → không kiểm cận trên độ dài email.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- **A15** (giả định, SRS im lặng): A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.
- **A21** (giả định, SRS im lặng): A21 (email chỉ gồm ký tự ASCII): FR-22.2 bắt ô Email dùng type="email". A2 lấy quy tắc HTML5 làm tham chiếu phụ, và theo định nghĩa “valid e-mail address” của HTML5, phần local chỉ gồm ký tự ASCII. Vì vậy email có ký tự ngoài ASCII là sai định dạng. → TC-219: tеst@eshop.com (chữ е Cyrillic) phải bị từ chối, 4xx, không tạo user. Thêm EC52 “Email có ký tự ngoài ASCII” (không hợp lệ), do TC-219 phủ. Nay case này có oracle, không còn là quan sát suông. (AI đề xuất, SV duyệt 2026-10-19)
- (FR-01.1, FR-01.5 chỉ do TC-213)
```

### Comment

> Đính chính 2026-10-20: trường Yêu cầu trước đây liệt kê cả yêu cầu không bị vi phạm; nay chỉ giữ FR-01.1, FR-01.2, FR-01.3, FR-01.5, A2, A9, A11, A15, A21 — ghi rõ FR-01.1, FR-01.5 chỉ do TC-213. Bước/Actual/Expected không đổi.

- Đã sửa body và kiểm lại bằng `gh issue view` (mục Yêu cầu khớp). Comment: https://github.com/tkob-team/eshop-sut/issues/20#issuecomment-6285167630

## #22 — BUG-06 — [FR-01] Gửi 2 request đăng ký đồng thời (race condition) cùng 1 email thì cả 2 đều trả HTTP 200, tạo ra 2 user trùng email trong CSDL

### Mục Yêu cầu — trước

```
- **FR-01.4:** Email phải là duy nhất trong hệ thống.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
```

### Mục Yêu cầu — sau

```
- **FR-01.4:** Email phải là duy nhất trong hệ thống.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
```

### Comment

> Đính chính 2026-10-20: trường Yêu cầu trước đây liệt kê cả yêu cầu không bị vi phạm; nay chỉ giữ FR-01.4, A9, A11 (bổ sung A11). Bước/Actual/Expected không đổi.

- Đã sửa body và kiểm lại bằng `gh issue view` (mục Yêu cầu khớp). Comment: https://github.com/tkob-team/eshop-sut/issues/22#issuecomment-6285168706

## #24 — BUG-08 — [FR-01] Backend API POST /api/register không Trim khoảng trắng thừa ở hai đầu Email trước khi lưu vào CSDL

### Mục Yêu cầu — trước

```
- **A3** (giả định, SRS im lặng): A3 (Email – duy nhất): Email so sánh sau khi cắt khoảng trắng đầu/cuối; phần local phân biệt hoa/thường, phần domain không phân biệt (RFC 5321 §2.4). SV sửa ở bước 5.
- **FR-01.4:** Email phải là duy nhất trong hệ thống.
```

### Mục Yêu cầu — sau

```
- **A3** (giả định, SRS im lặng): A3 (Email – duy nhất): Email so sánh sau khi cắt khoảng trắng đầu/cuối; phần local phân biệt hoa/thường, phần domain không phân biệt (RFC 5321 §2.4). SV sửa ở bước 5.
```

### Comment

> Đính chính 2026-10-20: trường Yêu cầu trước đây liệt kê cả yêu cầu không bị vi phạm; nay chỉ giữ A3. Bước/Actual/Expected không đổi.

- Đã sửa body và kiểm lại bằng `gh issue view` (mục Yêu cầu khớp). Comment: https://github.com/tkob-team/eshop-sut/issues/24#issuecomment-6285169746

## #25 — BUG-09 — [FR-01] Gửi mật khẩu hợp lệ dài 200.000 ký tự qua API làm backend trả về trang lỗi HTML HTTP 413 PayloadTooLargeError

### Mục Yêu cầu — trước

```
- **FR-01.6:** Mật khẩu tối thiểu 8 ký tự.
- **A4** (giả định, SRS im lặng): A4 (Mật khẩu – độ dài): chỉ có cận dưới 8 ký tự. SRS không có cận trên → không có UB; BVA độ dài chỉ quanh LB = 8 (7, 8, 9) và NOM.
```

### Mục Yêu cầu — sau

```
- **A4** (giả định, SRS im lặng): A4 (Mật khẩu – độ dài): chỉ có cận dưới 8 ký tự. SRS không có cận trên → không có UB; BVA độ dài chỉ quanh LB = 8 (7, 8, 9) và NOM.
```

### Comment

> Đính chính 2026-10-20: trường Yêu cầu trước đây liệt kê cả yêu cầu không bị vi phạm; nay chỉ giữ A4. Bước/Actual/Expected không đổi.

- Đã sửa body và kiểm lại bằng `gh issue view` (mục Yêu cầu khớp). Comment: https://github.com/tkob-team/eshop-sut/issues/25#issuecomment-6285170775

## #26 — BUG-10 — [FR-01] Gửi request POST /api/register với Content-Type: text/plain, văng lỗi HTTP 500 kèm trang HTML stack trace

### Mục Yêu cầu — trước

```
- **API-REG:** POST /api/register nhận body JSON {name, email, password}; thành công trả 200 {"message": "User registered successfully", "id": n} (api_specification.md dòng 14–21).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
```

### Mục Yêu cầu — sau

```
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
```

### Comment

> Đính chính 2026-10-20: trường Yêu cầu trước đây liệt kê cả yêu cầu không bị vi phạm; nay chỉ giữ A11. Bước/Actual/Expected không đổi.

- Đã sửa body và kiểm lại bằng `gh issue view` (mục Yêu cầu khớp). Comment: https://github.com/tkob-team/eshop-sut/issues/26#issuecomment-6285171845


## Toàn văn body trước/sau

<details>
<summary>#17 — body trước</summary>

````markdown
# BUG-01

- **ID:** BUG-01
- **Tiêu đề:** Đăng ký không cho mật khẩu hợp lệ, nó nói "Mật khẩu quá yếu!"
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2)
- Web http://localhost:5173/register (frontend-web)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, chưa đăng nhập. Email muốn đăng ký chưa tồn tại.

## Các bước tái hiện

1. Mở /register, nhập: `Nguyen Van A` · `dom01_1792424523821@domain.com` · `Abcd1234!`
2. Ấn "Đăng Ký" 

## Expected (trích SRS)

FR-01: mật khẩu "tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (@, $, !, %, *, ?, &)" → `Abcd1234!` hợp lệ → chuyển hướng sang /login và tạo 1 user.

## Actual

Hộp lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.", ở lại /register, không gửi `POST /api/register`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-01_ui.png`, `TC-FR01-64_ui.png`
<img width="1280" height="800" alt="TC-FR01-01_ui" src="https://github.com/user-attachments/assets/2200d08d-b4e5-45a0-910d-c3857aa943e2" />

<img width="1280" height="800" alt="TC-FR01-64_ui" src="https://github.com/user-attachments/assets/893ed509-164f-45a9-a0e5-df2d381454e1" />

<details>
<summary>Ảnh từng TC (14)</summary>

- TC-FR01-01: `HW02/A_FR01/evidence/TC-FR01-01_ui.png`, `HW02/A_FR01/evidence/TC-FR01-01_failed.png`
- TC-FR01-02: `HW02/A_FR01/evidence/TC-FR01-02_ui.png`, `HW02/A_FR01/evidence/TC-FR01-02_failed.png`
- TC-FR01-64: `HW02/A_FR01/evidence/TC-FR01-64_ui.png`, `HW02/A_FR01/evidence/TC-FR01-64_failed.png`
- TC-FR01-65: `HW02/A_FR01/evidence/TC-FR01-65_ui.png`, `HW02/A_FR01/evidence/TC-FR01-65_failed.png`
- TC-FR01-66: `HW02/A_FR01/evidence/TC-FR01-66_ui.png`, `HW02/A_FR01/evidence/TC-FR01-66_failed.png`
- TC-FR01-68: `HW02/A_FR01/evidence/TC-FR01-68_ui.png`, `HW02/A_FR01/evidence/TC-FR01-68_failed.png`
- TC-FR01-69: `HW02/A_FR01/evidence/TC-FR01-69_ui.png`, `HW02/A_FR01/evidence/TC-FR01-69_failed.png`
- TC-FR01-71: `HW02/A_FR01/evidence/TC-FR01-71_ui.png`, `HW02/A_FR01/evidence/TC-FR01-71_failed.png`
- TC-FR01-72: `HW02/A_FR01/evidence/TC-FR01-72_ui.png`, `HW02/A_FR01/evidence/TC-FR01-72_failed.png`
- TC-FR01-74: `HW02/A_FR01/evidence/TC-FR01-74_ui.png`, `HW02/A_FR01/evidence/TC-FR01-74_failed.png`
- TC-FR01-75: `HW02/A_FR01/evidence/TC-FR01-75_ui.png`, `HW02/A_FR01/evidence/TC-FR01-75_failed.png`
- TC-FR01-77: `HW02/A_FR01/evidence/TC-FR01-77_ui.png`, `HW02/A_FR01/evidence/TC-FR01-77_failed.png`
- TC-FR01-78: `HW02/A_FR01/evidence/TC-FR01-78_ui.png`, `HW02/A_FR01/evidence/TC-FR01-78_failed.png`
- TC-FR01-211: `HW02/A_FR01/evidence/TC-FR01-211_ui.png`, `HW02/A_FR01/evidence/TC-FR01-211_failed.png`
</details>

## TC liên quan

- Fail (14): TC-FR01-01, TC-FR01-02, TC-FR01-64, TC-FR01-65, TC-FR01-66, TC-FR01-68, TC-FR01-69, TC-FR01-71, TC-FR01-72, TC-FR01-74, TC-FR01-75, TC-FR01-77, TC-FR01-78, TC-FR01-211
- Blocked ghi case gốc (22): TC-FR01-03, TC-FR01-04, TC-FR01-06, TC-FR01-08, TC-FR01-09, TC-FR01-10, TC-FR01-11, TC-FR01-12, TC-FR01-13, TC-FR01-14, TC-FR01-15, TC-FR01-61, TC-FR01-62, TC-FR01-200, TC-FR01-203, TC-FR01-204, TC-FR01-205, TC-FR01-208, TC-FR01-215, TC-FR01-217, TC-FR01-218, TC-FR01-223
- Nhóm dữ kiện: G1 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.6:** Mật khẩu tối thiểu 8 ký tự.
- **FR-01.7a:** Mật khẩu có ít nhất 1 chữ hoa.
- **FR-01.7b:** Mật khẩu có ít nhất 1 chữ thường.
- **FR-01.7c:** Mật khẩu có ít nhất 1 chữ số.
- **FR-01.8:** Mật khẩu có ít nhất 1 ký tự đặc biệt thuộc tập @, $, !, %, *, ?, &.
- **FR-01.10:** Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G1): `frontend-web/src/pages/Register.jsx dòng 15–20`
- Các case Blocked ghi case gốc: TC-FR01-01 (A17/A20).
- SRS `eshop-sut/README.md` dòng 34 (FR-01, mật khẩu): "- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`)."
- FR-01.8 (tập ký tự, cùng dòng 34): "1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`)"
- FR-01.10, dòng 36: "- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập."
- Dữ liệu nhập (`HW02/A_FR01/testcases.json`, `{ts}` = timestamp lúc chạy):

  | TC | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu |
  |---|---|---|---|---|
  | TC-FR01-01 | `Nguyen Van A` | `dom01_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` |
  | TC-FR01-64 (LB, 8 ký tự) | `Nguyen Van A` | `bva64_{ts}@domain.com` | `Abc12!xy` | `Abc12!xy` |

### Nhận định

Lỗi ở kiểm tra phía client (0 POST). Ngược lại, `Abcd 1234` (không có ký tự đặc biệt) lại được chấp nhận (TC-202) (xem BUG-02). 22 case Blocked vì cần mật khẩu hợp lệ để qua bước này. 

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#17 — body sau</summary>

````markdown
# BUG-01

- **ID:** BUG-01
- **Tiêu đề:** Đăng ký không cho mật khẩu hợp lệ, nó nói "Mật khẩu quá yếu!"
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2)
- Web http://localhost:5173/register (frontend-web)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, chưa đăng nhập. Email muốn đăng ký chưa tồn tại.

## Các bước tái hiện

1. Mở /register, nhập: `Nguyen Van A` · `dom01_1792424523821@domain.com` · `Abcd1234!`
2. Ấn "Đăng Ký" 

## Expected (trích SRS)

FR-01: mật khẩu "tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (@, $, !, %, *, ?, &)" → `Abcd1234!` hợp lệ → chuyển hướng sang /login và tạo 1 user.

## Actual

Hộp lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.", ở lại /register, không gửi `POST /api/register`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-01_ui.png`, `TC-FR01-64_ui.png`
<img width="1280" height="800" alt="TC-FR01-01_ui" src="https://github.com/user-attachments/assets/2200d08d-b4e5-45a0-910d-c3857aa943e2" />

<img width="1280" height="800" alt="TC-FR01-64_ui" src="https://github.com/user-attachments/assets/893ed509-164f-45a9-a0e5-df2d381454e1" />

<details>
<summary>Ảnh từng TC (14)</summary>

- TC-FR01-01: `HW02/A_FR01/evidence/TC-FR01-01_ui.png`, `HW02/A_FR01/evidence/TC-FR01-01_failed.png`
- TC-FR01-02: `HW02/A_FR01/evidence/TC-FR01-02_ui.png`, `HW02/A_FR01/evidence/TC-FR01-02_failed.png`
- TC-FR01-64: `HW02/A_FR01/evidence/TC-FR01-64_ui.png`, `HW02/A_FR01/evidence/TC-FR01-64_failed.png`
- TC-FR01-65: `HW02/A_FR01/evidence/TC-FR01-65_ui.png`, `HW02/A_FR01/evidence/TC-FR01-65_failed.png`
- TC-FR01-66: `HW02/A_FR01/evidence/TC-FR01-66_ui.png`, `HW02/A_FR01/evidence/TC-FR01-66_failed.png`
- TC-FR01-68: `HW02/A_FR01/evidence/TC-FR01-68_ui.png`, `HW02/A_FR01/evidence/TC-FR01-68_failed.png`
- TC-FR01-69: `HW02/A_FR01/evidence/TC-FR01-69_ui.png`, `HW02/A_FR01/evidence/TC-FR01-69_failed.png`
- TC-FR01-71: `HW02/A_FR01/evidence/TC-FR01-71_ui.png`, `HW02/A_FR01/evidence/TC-FR01-71_failed.png`
- TC-FR01-72: `HW02/A_FR01/evidence/TC-FR01-72_ui.png`, `HW02/A_FR01/evidence/TC-FR01-72_failed.png`
- TC-FR01-74: `HW02/A_FR01/evidence/TC-FR01-74_ui.png`, `HW02/A_FR01/evidence/TC-FR01-74_failed.png`
- TC-FR01-75: `HW02/A_FR01/evidence/TC-FR01-75_ui.png`, `HW02/A_FR01/evidence/TC-FR01-75_failed.png`
- TC-FR01-77: `HW02/A_FR01/evidence/TC-FR01-77_ui.png`, `HW02/A_FR01/evidence/TC-FR01-77_failed.png`
- TC-FR01-78: `HW02/A_FR01/evidence/TC-FR01-78_ui.png`, `HW02/A_FR01/evidence/TC-FR01-78_failed.png`
- TC-FR01-211: `HW02/A_FR01/evidence/TC-FR01-211_ui.png`, `HW02/A_FR01/evidence/TC-FR01-211_failed.png`
</details>

## TC liên quan

- Fail (14): TC-FR01-01, TC-FR01-02, TC-FR01-64, TC-FR01-65, TC-FR01-66, TC-FR01-68, TC-FR01-69, TC-FR01-71, TC-FR01-72, TC-FR01-74, TC-FR01-75, TC-FR01-77, TC-FR01-78, TC-FR01-211
- Blocked ghi case gốc (22): TC-FR01-03, TC-FR01-04, TC-FR01-06, TC-FR01-08, TC-FR01-09, TC-FR01-10, TC-FR01-11, TC-FR01-12, TC-FR01-13, TC-FR01-14, TC-FR01-15, TC-FR01-61, TC-FR01-62, TC-FR01-200, TC-FR01-203, TC-FR01-204, TC-FR01-205, TC-FR01-208, TC-FR01-215, TC-FR01-217, TC-FR01-218, TC-FR01-223
- Nhóm dữ kiện: G1 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.10:** Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.
- **Chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8** (ngầm định — Actual chỉ có thông báo gộp, không xác định được luật riêng nào bị cài sai)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G1): `frontend-web/src/pages/Register.jsx dòng 15–20`
- Các case Blocked ghi case gốc: TC-FR01-01 (A17/A20).
- SRS `eshop-sut/README.md` dòng 34 (FR-01, mật khẩu): "- **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`)."
- FR-01.8 (tập ký tự, cùng dòng 34): "1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`)"
- FR-01.10, dòng 36: "- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập."
- Dữ liệu nhập (`HW02/A_FR01/testcases.json`, `{ts}` = timestamp lúc chạy):

  | TC | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu |
  |---|---|---|---|---|
  | TC-FR01-01 | `Nguyen Van A` | `dom01_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` |
  | TC-FR01-64 (LB, 8 ký tự) | `Nguyen Van A` | `bva64_{ts}@domain.com` | `Abc12!xy` | `Abc12!xy` |

### Nhận định

Lỗi ở kiểm tra phía client (0 POST). Ngược lại, `Abcd 1234` (không có ký tự đặc biệt) lại được chấp nhận (TC-202) (xem BUG-02). 22 case Blocked vì cần mật khẩu hợp lệ để qua bước này. 

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#20 — body trước</summary>

````markdown
# BUG-04

- **ID:** BUG-04
- **Tiêu đề:** Backend API POST /api/register không kiểm tra Email (rỗng, sai định dạng, thiếu trường, sai kiểu) vẫn trả HTTP 200 và tạo user
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL được seed sạch. Họ Tên và Mật khẩu trong payload hợp lệ theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi vi phạm trường Email (bắt buộc & định dạng hợp lệ):
   - **Case 1 (rỗng):** `{"name": "Nguyen Van A", "email": "", "password": "Abcd1234!"}`
   - **Case 2 (thiếu '@'):** `{"name": "Nguyen Van A", "email": "dom35_1792424698374domain.com", "password": "Abcd1234!"}`
   - **Case 3 (nhiều '@'):** `{"name": "Nguyen Van A", "email": "dom36@x_1792424699665@domain.com", "password": "Abcd1234!"}`
   - **Case 4 (thiếu local):** `{"name": "Nguyen Van A", "email": "@dom1792424701038.com", "password": "Abcd1234!"}`
   - **Case 5 (thiếu domain):** `{"name": "Nguyen Van A", "email": "dom38_1792424702726@", "password": "Abcd1234!"}`
   - **Case 6 (domain thiếu dấu chấm):** `{"name": "Nguyen Van A", "email": "dom39_1792424704059@domain", "password": "Abcd1234!"}`
   - **Case 7 (khoảng trắng ở giữa):** `{"name": "Nguyen Van A", "email": "dom 40_1792424705518@domain.com", "password": "Abcd1234!"}`
   - **Case 8 (thiếu khoá email):** `{"name": "Nguyen Van A", "password": "Abcd1234!"}`
   - **Case 9 (sai kiểu - số JSON):** `{"name": "Nguyen Van A", "email": 123, "password": "Abcd1234!"}`
   - **Case 10 (body rỗng {}):** `{}`

## Expected (trích SRS)

FR-01.2 và FR-01.3 yêu cầu Email là trường bắt buộc và phải đúng định dạng (`user@domain.com`). Tầng API kiểm tra dữ liệu đầu vào (A9, A15), từ chối request không hợp lệ bằng mã lỗi HTTP 4xx kèm trường `error` trong body JSON (A11) và không tạo tài khoản mới.

## Actual

API đều trả về **HTTP 200** `{"message":"User registered successfully","id": <id>}` và tạo thành công user mới trong CSDL với Email bị trống/null/chuỗi sai định dạng/số.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-34_api.png`, `TC-FR01-35_api.png`

<img width="1280" height="720" alt="TC-FR01-34_api" src="https://github.com/user-attachments/assets/1df6fd0d-8e03-45c4-bf22-0c7056742d01" />

<img width="1280" height="720" alt="TC-FR01-35_api" src="https://github.com/user-attachments/assets/e5b4a91b-af30-4703-a5da-982a71778534" />

- TC-FR01-34: `HW02/A_FR01/evidence/TC-FR01-34_req.json`, `HW02/A_FR01/evidence/TC-FR01-34_res.json`, `HW02/A_FR01/evidence/TC-FR01-34_api.png`
- TC-FR01-35: `HW02/A_FR01/evidence/TC-FR01-35_req.json`, `HW02/A_FR01/evidence/TC-FR01-35_res.json`, `HW02/A_FR01/evidence/TC-FR01-35_api.png`
- TC-FR01-36: `HW02/A_FR01/evidence/TC-FR01-36_req.json`, `HW02/A_FR01/evidence/TC-FR01-36_res.json`, `HW02/A_FR01/evidence/TC-FR01-36_api.png`
- TC-FR01-37: `HW02/A_FR01/evidence/TC-FR01-37_req.json`, `HW02/A_FR01/evidence/TC-FR01-37_res.json`, `HW02/A_FR01/evidence/TC-FR01-37_api.png`
- TC-FR01-38: `HW02/A_FR01/evidence/TC-FR01-38_req.json`, `HW02/A_FR01/evidence/TC-FR01-38_res.json`, `HW02/A_FR01/evidence/TC-FR01-38_api.png`
- TC-FR01-39: `HW02/A_FR01/evidence/TC-FR01-39_req.json`, `HW02/A_FR01/evidence/TC-FR01-39_res.json`, `HW02/A_FR01/evidence/TC-FR01-39_api.png`
- TC-FR01-40: `HW02/A_FR01/evidence/TC-FR01-40_req.json`, `HW02/A_FR01/evidence/TC-FR01-40_res.json`, `HW02/A_FR01/evidence/TC-FR01-40_api.png`
- TC-FR01-54: `HW02/A_FR01/evidence/TC-FR01-54_req.json`, `HW02/A_FR01/evidence/TC-FR01-54_res.json`, `HW02/A_FR01/evidence/TC-FR01-54_api.png`
- TC-FR01-55: `HW02/A_FR01/evidence/TC-FR01-55_req.json`, `HW02/A_FR01/evidence/TC-FR01-55_res.json`, `HW02/A_FR01/evidence/TC-FR01-55_api.png`
- TC-FR01-201: `HW02/A_FR01/evidence/TC-FR01-201_req.json`, `HW02/A_FR01/evidence/TC-FR01-201_res.json`, `HW02/A_FR01/evidence/TC-FR01-201_api.png`
- TC-FR01-213: `HW02/A_FR01/evidence/TC-FR01-213_req.json`, `HW02/A_FR01/evidence/TC-FR01-213_res.json`, `HW02/A_FR01/evidence/TC-FR01-213_api.png`
- TC-FR01-219: `HW02/A_FR01/evidence/TC-FR01-219_req.json`, `HW02/A_FR01/evidence/TC-FR01-219_res.json`, `HW02/A_FR01/evidence/TC-FR01-219_api.png`
- TC-FR01-220: `HW02/A_FR01/evidence/TC-FR01-220_req.json`, `HW02/A_FR01/evidence/TC-FR01-220_res.json`, `HW02/A_FR01/evidence/TC-FR01-220_api.png`
- TC-FR01-221: `HW02/A_FR01/evidence/TC-FR01-221_req.json`, `HW02/A_FR01/evidence/TC-FR01-221_res.json`, `HW02/A_FR01/evidence/TC-FR01-221_api.png`
- TC-FR01-225: `HW02/A_FR01/evidence/TC-FR01-225_req.json`, `HW02/A_FR01/evidence/TC-FR01-225_res.json`, `HW02/A_FR01/evidence/TC-FR01-225_api.png`
- TC-FR01-226: `HW02/A_FR01/evidence/TC-FR01-226_req.json`, `HW02/A_FR01/evidence/TC-FR01-226_res.json`, `HW02/A_FR01/evidence/TC-FR01-226_api.png`

## TC liên quan

- Fail (16): TC-FR01-34, TC-FR01-35, TC-FR01-36, TC-FR01-37, TC-FR01-38, TC-FR01-39, TC-FR01-40, TC-FR01-54, TC-FR01-55, TC-FR01-201, TC-FR01-213, TC-FR01-219, TC-FR01-220, TC-FR01-221, TC-FR01-225, TC-FR01-226
- Nhóm dữ kiện: G3, G6 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.1:** Người dùng phải cung cấp Họ Tên (trường bắt buộc).
- **FR-01.2:** Người dùng phải cung cấp Email (trường bắt buộc).
- **FR-01.3:** Email phải có định dạng hợp lệ (user@domain.com).
- **FR-01.5:** Người dùng phải cung cấp Mật khẩu (trường bắt buộc).
- **A2** (giả định, SRS im lặng): A2 (Email – định dạng): FR-01 chỉ đưa mẫu 'user@domain.com'. Giả định định dạng hợp lệ = <local>@<domain>.<tld>: đúng một '@', phần local không rỗng, phần domain có ít nhất một dấu '.' và không rỗng hai bên dấu chấm. FR-22 yêu cầu type="email" nên quy tắc HTML5 của trình duyệt dùng làm tham chiếu phụ. SRS không nêu độ dài tối đa → không kiểm cận trên độ dài email.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- **A15** (giả định, SRS im lặng): A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.
- **A21** (giả định, SRS im lặng): A21 (email chỉ gồm ký tự ASCII): FR-22.2 bắt ô Email dùng type="email". A2 lấy quy tắc HTML5 làm tham chiếu phụ, và theo định nghĩa “valid e-mail address” của HTML5, phần local chỉ gồm ký tự ASCII. Vì vậy email có ký tự ngoài ASCII là sai định dạng. → TC-219: tеst@eshop.com (chữ е Cyrillic) phải bị từ chối, 4xx, không tạo user. Thêm EC52 “Email có ký tự ngoài ASCII” (không hợp lệ), do TC-219 phủ. Nay case này có oracle, không còn là quan sát suông. (AI đề xuất, SV duyệt 2026-10-19)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- G6 (TC-FR01-213) đưa vào làm bằng chứng bổ sung theo quyết định SV.
- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G3, G6): `backend/server.js dòng 20–29`

### Nhận định

- Tương tự BUG-03, nguyên nhân xuất phát từ việc backend handler hoàn toàn thiếu logic validate cho biến email. Request gửi trực tiếp tới API không qua bộ kiểm tra regex/HTML5 của browser nên lọt thẳng xuống câu lệnh SQL INSERT INTO users.

- Việc cho phép tạo tài khoản với email rỗng hoặc sai định dạng khiến dữ liệu CSDL bị rác, đồng thời người dùng sẽ không thể dùng tài khoản này để đăng nhập lại sau đó (chưa kiểm chứng).

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#20 — body sau</summary>

````markdown
# BUG-04

- **ID:** BUG-04
- **Tiêu đề:** Backend API POST /api/register không kiểm tra Email (rỗng, sai định dạng, thiếu trường, sai kiểu) vẫn trả HTTP 200 và tạo user
- **Severity:** Critical
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL được seed sạch. Họ Tên và Mật khẩu trong payload hợp lệ theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi vi phạm trường Email (bắt buộc & định dạng hợp lệ):
   - **Case 1 (rỗng):** `{"name": "Nguyen Van A", "email": "", "password": "Abcd1234!"}`
   - **Case 2 (thiếu '@'):** `{"name": "Nguyen Van A", "email": "dom35_1792424698374domain.com", "password": "Abcd1234!"}`
   - **Case 3 (nhiều '@'):** `{"name": "Nguyen Van A", "email": "dom36@x_1792424699665@domain.com", "password": "Abcd1234!"}`
   - **Case 4 (thiếu local):** `{"name": "Nguyen Van A", "email": "@dom1792424701038.com", "password": "Abcd1234!"}`
   - **Case 5 (thiếu domain):** `{"name": "Nguyen Van A", "email": "dom38_1792424702726@", "password": "Abcd1234!"}`
   - **Case 6 (domain thiếu dấu chấm):** `{"name": "Nguyen Van A", "email": "dom39_1792424704059@domain", "password": "Abcd1234!"}`
   - **Case 7 (khoảng trắng ở giữa):** `{"name": "Nguyen Van A", "email": "dom 40_1792424705518@domain.com", "password": "Abcd1234!"}`
   - **Case 8 (thiếu khoá email):** `{"name": "Nguyen Van A", "password": "Abcd1234!"}`
   - **Case 9 (sai kiểu - số JSON):** `{"name": "Nguyen Van A", "email": 123, "password": "Abcd1234!"}`
   - **Case 10 (body rỗng {}):** `{}`

## Expected (trích SRS)

FR-01.2 và FR-01.3 yêu cầu Email là trường bắt buộc và phải đúng định dạng (`user@domain.com`). Tầng API kiểm tra dữ liệu đầu vào (A9, A15), từ chối request không hợp lệ bằng mã lỗi HTTP 4xx kèm trường `error` trong body JSON (A11) và không tạo tài khoản mới.

## Actual

API đều trả về **HTTP 200** `{"message":"User registered successfully","id": <id>}` và tạo thành công user mới trong CSDL với Email bị trống/null/chuỗi sai định dạng/số.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-34_api.png`, `TC-FR01-35_api.png`

<img width="1280" height="720" alt="TC-FR01-34_api" src="https://github.com/user-attachments/assets/1df6fd0d-8e03-45c4-bf22-0c7056742d01" />

<img width="1280" height="720" alt="TC-FR01-35_api" src="https://github.com/user-attachments/assets/e5b4a91b-af30-4703-a5da-982a71778534" />

- TC-FR01-34: `HW02/A_FR01/evidence/TC-FR01-34_req.json`, `HW02/A_FR01/evidence/TC-FR01-34_res.json`, `HW02/A_FR01/evidence/TC-FR01-34_api.png`
- TC-FR01-35: `HW02/A_FR01/evidence/TC-FR01-35_req.json`, `HW02/A_FR01/evidence/TC-FR01-35_res.json`, `HW02/A_FR01/evidence/TC-FR01-35_api.png`
- TC-FR01-36: `HW02/A_FR01/evidence/TC-FR01-36_req.json`, `HW02/A_FR01/evidence/TC-FR01-36_res.json`, `HW02/A_FR01/evidence/TC-FR01-36_api.png`
- TC-FR01-37: `HW02/A_FR01/evidence/TC-FR01-37_req.json`, `HW02/A_FR01/evidence/TC-FR01-37_res.json`, `HW02/A_FR01/evidence/TC-FR01-37_api.png`
- TC-FR01-38: `HW02/A_FR01/evidence/TC-FR01-38_req.json`, `HW02/A_FR01/evidence/TC-FR01-38_res.json`, `HW02/A_FR01/evidence/TC-FR01-38_api.png`
- TC-FR01-39: `HW02/A_FR01/evidence/TC-FR01-39_req.json`, `HW02/A_FR01/evidence/TC-FR01-39_res.json`, `HW02/A_FR01/evidence/TC-FR01-39_api.png`
- TC-FR01-40: `HW02/A_FR01/evidence/TC-FR01-40_req.json`, `HW02/A_FR01/evidence/TC-FR01-40_res.json`, `HW02/A_FR01/evidence/TC-FR01-40_api.png`
- TC-FR01-54: `HW02/A_FR01/evidence/TC-FR01-54_req.json`, `HW02/A_FR01/evidence/TC-FR01-54_res.json`, `HW02/A_FR01/evidence/TC-FR01-54_api.png`
- TC-FR01-55: `HW02/A_FR01/evidence/TC-FR01-55_req.json`, `HW02/A_FR01/evidence/TC-FR01-55_res.json`, `HW02/A_FR01/evidence/TC-FR01-55_api.png`
- TC-FR01-201: `HW02/A_FR01/evidence/TC-FR01-201_req.json`, `HW02/A_FR01/evidence/TC-FR01-201_res.json`, `HW02/A_FR01/evidence/TC-FR01-201_api.png`
- TC-FR01-213: `HW02/A_FR01/evidence/TC-FR01-213_req.json`, `HW02/A_FR01/evidence/TC-FR01-213_res.json`, `HW02/A_FR01/evidence/TC-FR01-213_api.png`
- TC-FR01-219: `HW02/A_FR01/evidence/TC-FR01-219_req.json`, `HW02/A_FR01/evidence/TC-FR01-219_res.json`, `HW02/A_FR01/evidence/TC-FR01-219_api.png`
- TC-FR01-220: `HW02/A_FR01/evidence/TC-FR01-220_req.json`, `HW02/A_FR01/evidence/TC-FR01-220_res.json`, `HW02/A_FR01/evidence/TC-FR01-220_api.png`
- TC-FR01-221: `HW02/A_FR01/evidence/TC-FR01-221_req.json`, `HW02/A_FR01/evidence/TC-FR01-221_res.json`, `HW02/A_FR01/evidence/TC-FR01-221_api.png`
- TC-FR01-225: `HW02/A_FR01/evidence/TC-FR01-225_req.json`, `HW02/A_FR01/evidence/TC-FR01-225_res.json`, `HW02/A_FR01/evidence/TC-FR01-225_api.png`
- TC-FR01-226: `HW02/A_FR01/evidence/TC-FR01-226_req.json`, `HW02/A_FR01/evidence/TC-FR01-226_res.json`, `HW02/A_FR01/evidence/TC-FR01-226_api.png`

## TC liên quan

- Fail (16): TC-FR01-34, TC-FR01-35, TC-FR01-36, TC-FR01-37, TC-FR01-38, TC-FR01-39, TC-FR01-40, TC-FR01-54, TC-FR01-55, TC-FR01-201, TC-FR01-213, TC-FR01-219, TC-FR01-220, TC-FR01-221, TC-FR01-225, TC-FR01-226
- Nhóm dữ kiện: G3, G6 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.1:** Người dùng phải cung cấp Họ Tên (trường bắt buộc).
- **FR-01.2:** Người dùng phải cung cấp Email (trường bắt buộc).
- **FR-01.3:** Email phải có định dạng hợp lệ (user@domain.com).
- **FR-01.5:** Người dùng phải cung cấp Mật khẩu (trường bắt buộc).
- **A2** (giả định, SRS im lặng): A2 (Email – định dạng): FR-01 chỉ đưa mẫu 'user@domain.com'. Giả định định dạng hợp lệ = <local>@<domain>.<tld>: đúng một '@', phần local không rỗng, phần domain có ít nhất một dấu '.' và không rỗng hai bên dấu chấm. FR-22 yêu cầu type="email" nên quy tắc HTML5 của trình duyệt dùng làm tham chiếu phụ. SRS không nêu độ dài tối đa → không kiểm cận trên độ dài email.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).
- **A15** (giả định, SRS im lặng): A15 (Sai kiểu / thiếu trường ở tầng API): SRS không nói gì về body JSON. Giả định trường name/email/password bị thiếu, bằng null hoặc không phải chuỗi JSON (ví dụ số 123) là dữ liệu không hợp lệ → phải bị từ chối với 4xx, không tạo user (theo A9, A11). Các lớp này chỉ tạo được ở tầng API vì ô nhập trên UI luôn gửi chuỗi.
- **A21** (giả định, SRS im lặng): A21 (email chỉ gồm ký tự ASCII): FR-22.2 bắt ô Email dùng type="email". A2 lấy quy tắc HTML5 làm tham chiếu phụ, và theo định nghĩa “valid e-mail address” của HTML5, phần local chỉ gồm ký tự ASCII. Vì vậy email có ký tự ngoài ASCII là sai định dạng. → TC-219: tеst@eshop.com (chữ е Cyrillic) phải bị từ chối, 4xx, không tạo user. Thêm EC52 “Email có ký tự ngoài ASCII” (không hợp lệ), do TC-219 phủ. Nay case này có oracle, không còn là quan sát suông. (AI đề xuất, SV duyệt 2026-10-19)
- (FR-01.1, FR-01.5 chỉ do TC-213)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- G6 (TC-FR01-213) đưa vào làm bằng chứng bổ sung theo quyết định SV.
- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G3, G6): `backend/server.js dòng 20–29`

### Nhận định

- Tương tự BUG-03, nguyên nhân xuất phát từ việc backend handler hoàn toàn thiếu logic validate cho biến email. Request gửi trực tiếp tới API không qua bộ kiểm tra regex/HTML5 của browser nên lọt thẳng xuống câu lệnh SQL INSERT INTO users.

- Việc cho phép tạo tài khoản với email rỗng hoặc sai định dạng khiến dữ liệu CSDL bị rác, đồng thời người dùng sẽ không thể dùng tài khoản này để đăng nhập lại sau đó (chưa kiểm chứng).

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#22 — body trước</summary>

````markdown
# BUG-06

- **ID:** BUG-06
- **Tiêu đề:** Gửi 2 request đăng ký đồng thời (race condition) cùng 1 email thì cả 2 đều trả HTTP 200, tạo ra 2 user trùng email trong CSDL
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch sẽ. Email dùng để test (`hiep.sv10@domain.com`) chưa từng tồn tại trong hệ thống.

## Các bước tái hiện

1. Chuẩn bị 2 request `POST http://localhost:3000/api/register` cùng payload:
   `{"name": "Lê Tấn Hiệp", "email": "hiep.sv10@domain.com", "password": "Hiep123$"}`
2. Gửi đồng thời 2 request này tới backend bằng `Promise.all` (hoặc Postman Runner / Playwright parallel execution).

## Expected (trích SRS)

FR-01.4 yêu cầu Email phải là duy nhất trong hệ thống. Ngay cả khi 2 request bắn tới cùng một lúc, hệ thống vẫn phải xử lý bất đồng bộ chuẩn: chỉ đúng 1 request được phép thành công (HTTP 200), request còn lại phải bị chặn lại với mã lỗi HTTP 4xx và báo email đã tồn tại (A9, A11), đảm bảo chỉ có duy nhất 1 user được tạo trong CSDL.

## Actual

Cả 2 request gửi đồng thời đều lọt qua ngon ơ, đều nhận về phản hồi **HTTP 200** `{"message":"User registered successfully","id": <id>}`. Kết quả là trong CSDL xuất hiện 2 bản ghi user mới có ID khác nhau nhưng xài chung y nguyên email `hiep.sv10@domain.com`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-209_api.png`

<img width="1280" height="720" alt="TC-FR01-209_ap" src="https://github.com/user-attachments/assets/c5b32b9e-1a1a-40ba-98a7-6c785b7c5edf" />

- TC-FR01-209: `HW02/A_FR01/evidence/TC-FR01-209_req.json`, `HW02/A_FR01/evidence/TC-FR01-209_res.json`, `HW02/A_FR01/evidence/TC-FR01-209_api.png`

## TC liên quan

- Fail (1): TC-FR01-209
- Nhóm dữ kiện: G8 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.4:** Email phải là duy nhất trong hệ thống.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- SV ghi chú: liên quan BUG-05.
- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G8): `backend/server.js dòng 20–29`; `backend/database.js dòng 50–54`
- TC-FR01-209 chạy lại 3 lần (`--repeat-each=3`, `HW02/tests/results/isolate_209.json`): 3/3 failed; mỗi lần cả 2 request HTTP 200 và tạo 2 user cùng email.

### Nhận định

- Thiếu Constraint ở DB: Bảng users trong database.js hoàn toàn không có ràng buộc UNIQUE cho cột email. Do đó SQLite không hề có cơ chế tự động reject khi có 2 dòng dữ liệu trùng email nạp vô cùng lúc.

- Không có Check-Then-Act hay Transaction: Kể cả backend sau này có viết thêm câu lệnh SELECT kiểm tra email trước khi INSERT, nếu không dùng Transaction/Lock DB hoặc UNIQUE constraint ở tầng database thì khi 2 request tới cùng thời điểm, cả 2 đều SELECT ra "chưa tồn tại" rồi cùng INSERT xuống.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#22 — body sau</summary>

````markdown
# BUG-06

- **ID:** BUG-06
- **Tiêu đề:** Gửi 2 request đăng ký đồng thời (race condition) cùng 1 email thì cả 2 đều trả HTTP 200, tạo ra 2 user trùng email trong CSDL
- **Severity:** High
- **Priority:** High

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch sẽ. Email dùng để test (`hiep.sv10@domain.com`) chưa từng tồn tại trong hệ thống.

## Các bước tái hiện

1. Chuẩn bị 2 request `POST http://localhost:3000/api/register` cùng payload:
   `{"name": "Lê Tấn Hiệp", "email": "hiep.sv10@domain.com", "password": "Hiep123$"}`
2. Gửi đồng thời 2 request này tới backend bằng `Promise.all` (hoặc Postman Runner / Playwright parallel execution).

## Expected (trích SRS)

FR-01.4 yêu cầu Email phải là duy nhất trong hệ thống. Ngay cả khi 2 request bắn tới cùng một lúc, hệ thống vẫn phải xử lý bất đồng bộ chuẩn: chỉ đúng 1 request được phép thành công (HTTP 200), request còn lại phải bị chặn lại với mã lỗi HTTP 4xx và báo email đã tồn tại (A9, A11), đảm bảo chỉ có duy nhất 1 user được tạo trong CSDL.

## Actual

Cả 2 request gửi đồng thời đều lọt qua ngon ơ, đều nhận về phản hồi **HTTP 200** `{"message":"User registered successfully","id": <id>}`. Kết quả là trong CSDL xuất hiện 2 bản ghi user mới có ID khác nhau nhưng xài chung y nguyên email `hiep.sv10@domain.com`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-209_api.png`

<img width="1280" height="720" alt="TC-FR01-209_ap" src="https://github.com/user-attachments/assets/c5b32b9e-1a1a-40ba-98a7-6c785b7c5edf" />

- TC-FR01-209: `HW02/A_FR01/evidence/TC-FR01-209_req.json`, `HW02/A_FR01/evidence/TC-FR01-209_res.json`, `HW02/A_FR01/evidence/TC-FR01-209_api.png`

## TC liên quan

- Fail (1): TC-FR01-209
- Nhóm dữ kiện: G8 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.4:** Email phải là duy nhất trong hệ thống.
- **A9** (giả định, SRS im lặng): A9 (Kiểm ở tầng API): FR-01 là yêu cầu của hệ thống, không riêng giao diện → giả định API POST /api/register cũng phải từ chối dữ liệu vi phạm FR-01 khi gọi trực tiếp (bỏ qua UI).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- SV ghi chú: liên quan BUG-05.
- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G8): `backend/server.js dòng 20–29`; `backend/database.js dòng 50–54`
- TC-FR01-209 chạy lại 3 lần (`--repeat-each=3`, `HW02/tests/results/isolate_209.json`): 3/3 failed; mỗi lần cả 2 request HTTP 200 và tạo 2 user cùng email.

### Nhận định

- Thiếu Constraint ở DB: Bảng users trong database.js hoàn toàn không có ràng buộc UNIQUE cho cột email. Do đó SQLite không hề có cơ chế tự động reject khi có 2 dòng dữ liệu trùng email nạp vô cùng lúc.

- Không có Check-Then-Act hay Transaction: Kể cả backend sau này có viết thêm câu lệnh SELECT kiểm tra email trước khi INSERT, nếu không dùng Transaction/Lock DB hoặc UNIQUE constraint ở tầng database thì khi 2 request tới cùng thời điểm, cả 2 đều SELECT ra "chưa tồn tại" rồi cùng INSERT xuống.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#24 — body trước</summary>

````markdown
# BUG-08

- **ID:** BUG-08
- **Tiêu đề:** Backend API POST /api/register không Trim khoảng trắng thừa ở hai đầu Email trước khi lưu vào CSDL
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch. Họ Tên và Mật khẩu trong payload hợp lệ theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi email có chứa khoảng trắng ở hai đầu:
   `{"name": "Nguyen Van A", "email": "  api30_1792424692167@domain.com  ", "password": "Abcd1234!"}`

## Expected (trích SRS)

Theo quy chuẩn xử lý dữ liệu chuẩn (A3) và nguyên tắc duy nhất của Email (FR-01.4), khoảng trắng thừa ở hai đầu email phải được tự động cắt chuẩn hóa (`.trim()`) trước khi lưu vào CSDL. Phản hồi API trả **HTTP 200** và email lưu trong CSDL phải là `api30_1792424692167@domain.com` (đã cắt hết dấu cách thừa).

## Actual

API trả về **HTTP 200** `{"message":"User registered successfully","id": 5}`, nhưng email trong CSDL bị lưu nguyên văn cả các khoảng trắng hai đầu: `"  api30_1792424692167@domain.com  "`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-30_api.png`

<img width="1280" height="720" alt="TC-FR01-30_api" src="https://github.com/user-attachments/assets/ebb3af8d-fb0b-483f-af5c-580d17fde4fd" />

- TC-FR01-30: `HW02/A_FR01/evidence/TC-FR01-30_req.json`, `HW02/A_FR01/evidence/TC-FR01-30_res.json`, `HW02/A_FR01/evidence/TC-FR01-30_api.png`

## TC liên quan

- Fail (1): TC-FR01-30
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **A3** (giả định, SRS im lặng): A3 (Email – duy nhất): Email so sánh sau khi cắt khoảng trắng đầu/cuối; phần local phân biệt hoa/thường, phần domain không phân biệt (RFC 5321 §2.4). SV sửa ở bước 5.
- **FR-01.4:** Email phải là duy nhất trong hệ thống.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G7): `backend/server.js dòng 20–29`

### Nhận định

- Người dùng khi đăng nhập lại bằng email chính xác (không gõ khoảng trắng) sẽ bị báo sai tài khoản/mật khẩu vì chuỗi so sánh không khớp với giá trị lưu trong CSDL (chưa kiểm chứng).

- Tạo kẽ hở cho phép đăng ký trùng email ảo (một email có khoảng trắng và một email không có khoảng trắng được coi là 2 bản ghi khác nhau) (xem TC-FR01-42, BUG-05).

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#24 — body sau</summary>

````markdown
# BUG-08

- **ID:** BUG-08
- **Tiêu đề:** Backend API POST /api/register không Trim khoảng trắng thừa ở hai đầu Email trước khi lưu vào CSDL
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch. Họ Tên và Mật khẩu trong payload hợp lệ theo SRS.

## Các bước tái hiện

1. Gửi request `POST http://localhost:3000/api/register` (Header `Content-Type: application/json`).
2. Trong body JSON, gửi email có chứa khoảng trắng ở hai đầu:
   `{"name": "Nguyen Van A", "email": "  api30_1792424692167@domain.com  ", "password": "Abcd1234!"}`

## Expected (trích SRS)

Theo quy chuẩn xử lý dữ liệu chuẩn (A3) và nguyên tắc duy nhất của Email (FR-01.4), khoảng trắng thừa ở hai đầu email phải được tự động cắt chuẩn hóa (`.trim()`) trước khi lưu vào CSDL. Phản hồi API trả **HTTP 200** và email lưu trong CSDL phải là `api30_1792424692167@domain.com` (đã cắt hết dấu cách thừa).

## Actual

API trả về **HTTP 200** `{"message":"User registered successfully","id": 5}`, nhưng email trong CSDL bị lưu nguyên văn cả các khoảng trắng hai đầu: `"  api30_1792424692167@domain.com  "`.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-30_api.png`

<img width="1280" height="720" alt="TC-FR01-30_api" src="https://github.com/user-attachments/assets/ebb3af8d-fb0b-483f-af5c-580d17fde4fd" />

- TC-FR01-30: `HW02/A_FR01/evidence/TC-FR01-30_req.json`, `HW02/A_FR01/evidence/TC-FR01-30_res.json`, `HW02/A_FR01/evidence/TC-FR01-30_api.png`

## TC liên quan

- Fail (1): TC-FR01-30
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **A3** (giả định, SRS im lặng): A3 (Email – duy nhất): Email so sánh sau khi cắt khoảng trắng đầu/cuối; phần local phân biệt hoa/thường, phần domain không phân biệt (RFC 5321 §2.4). SV sửa ở bước 5.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G7): `backend/server.js dòng 20–29`

### Nhận định

- Người dùng khi đăng nhập lại bằng email chính xác (không gõ khoảng trắng) sẽ bị báo sai tài khoản/mật khẩu vì chuỗi so sánh không khớp với giá trị lưu trong CSDL (chưa kiểm chứng).

- Tạo kẽ hở cho phép đăng ký trùng email ảo (một email có khoảng trắng và một email không có khoảng trắng được coi là 2 bản ghi khác nhau) (xem TC-FR01-42, BUG-05).

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#25 — body trước</summary>

````markdown
# BUG-09

- **ID:** BUG-09
- **Tiêu đề:** Gửi mật khẩu hợp lệ dài 200.000 ký tự qua API làm backend trả về trang lỗi HTML HTTP 413 PayloadTooLargeError
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa mới khởi động lại xong, CSDL seed sạch sẽ. Họ Tên với Email trong payload là chuẩn theo SRS.

## Các bước tái hiện

1. Chuẩn bị payload `POST /api/register` có chứa trường mật khẩu siêu dài:
   - Header `Content-Type: application/json`
   - `name` = `"Lê Tấn Hiệp"`
   - `email` = `"hiep.sv13@domain.com"`
   - `password` = chuỗi hợp lệ dài 200.000 ký tự (ví dụ bắt đầu bằng `"Hiep123$"` rồi cộng thêm 199.992 ký tự `'a'`).
2. Gửi request `POST http://localhost:3000/api/register` tới server backend.

## Expected (trích SRS)

FR-01.6 và giả định A4 chỉ đặt ra độ dài tối thiểu là 8 ký tự cho mật khẩu chứ hoàn toàn không có đặt ra giới hạn cận trên (UB). Mật khẩu 200.000 ký tự vẫn có đủ chữ hoa, chữ thường, số và ký tự đặc biệt nên hoàn toàn hợp lệ. Backend phải xử lý nhận request thành công, trả về **HTTP 200** và tạo tài khoản user mới trong CSDL.

## Actual

Backend văng ra lỗi **HTTP 413** kèm trả về nguyên cục trang web HTML lỗi: `PayloadTooLargeError: request entity too large`. Đương nhiên là không có user mới nào được tạo ra trong CSDL cả.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-212_api.png`

<img width="1280" height="720" alt="TC-FR01-212_api" src="https://github.com/user-attachments/assets/027bef13-f7ea-4b41-8c97-8f8a23c8ab2b" />

- TC-FR01-212: `HW02/A_FR01/evidence/TC-FR01-212_req.json`, `HW02/A_FR01/evidence/TC-FR01-212_res.json`, `HW02/A_FR01/evidence/TC-FR01-212_api.png`

## TC liên quan

- Fail (1): TC-FR01-212
- Nhóm dữ kiện: G9 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **FR-01.6:** Mật khẩu tối thiểu 8 ký tự.
- **A4** (giả định, SRS im lặng): A4 (Mật khẩu – độ dài): chỉ có cận dưới 8 ký tự. SRS không có cận trên → không có UB; BVA độ dài chỉ quanh LB = 8 (7, 8, 9) và NOM.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G9): `backend/server.js dòng 3–12`
- `TC-FR01-212_req.json` ghi `password` dạng rút gọn (`Hiep123$aaa… (200000 ký tự)`); chuỗi gửi thật được script dựng và kiểm độ dài = 200.000 (`tests/A_FR01/lib.ts` dòng 32–37).
- Body 413 (`TC-FR01-212_res.json`) có stack trace: 10 dòng `at ...` (raw-body, body-parser, router, cors), kèm đường dẫn tuyệt đối trên máy chạy.
- Sau TC-FR01-212, test kế tiếp trong lượt chạy (TC-FR01-213, tầng API, Fail) vẫn nhận phản hồi từ backend (HTTP 200, id 58) → tiến trình backend không dừng.

### Nhận định

- SRS không hề quy định độ dài tối đa của mật khẩu (A4) nên hệ thống lý thuyết phải chấp nhận mọi chuỗi dài.

- Tuy nhiên trong server.js, dòng 12 dùng app.use(bodyParser.json()) nguyên bản không hề cấu hình limit độ lớn payload. Thư viện body-parser mặc định sẽ chặn và văng lỗi 413 nếu body JSON vượt quá ~100 KB.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#25 — body sau</summary>

````markdown
# BUG-09

- **ID:** BUG-09
- **Tiêu đề:** Gửi mật khẩu hợp lệ dài 200.000 ký tự qua API làm backend trả về trang lỗi HTML HTTP 413 PayloadTooLargeError
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa mới khởi động lại xong, CSDL seed sạch sẽ. Họ Tên với Email trong payload là chuẩn theo SRS.

## Các bước tái hiện

1. Chuẩn bị payload `POST /api/register` có chứa trường mật khẩu siêu dài:
   - Header `Content-Type: application/json`
   - `name` = `"Lê Tấn Hiệp"`
   - `email` = `"hiep.sv13@domain.com"`
   - `password` = chuỗi hợp lệ dài 200.000 ký tự (ví dụ bắt đầu bằng `"Hiep123$"` rồi cộng thêm 199.992 ký tự `'a'`).
2. Gửi request `POST http://localhost:3000/api/register` tới server backend.

## Expected (trích SRS)

FR-01.6 và giả định A4 chỉ đặt ra độ dài tối thiểu là 8 ký tự cho mật khẩu chứ hoàn toàn không có đặt ra giới hạn cận trên (UB). Mật khẩu 200.000 ký tự vẫn có đủ chữ hoa, chữ thường, số và ký tự đặc biệt nên hoàn toàn hợp lệ. Backend phải xử lý nhận request thành công, trả về **HTTP 200** và tạo tài khoản user mới trong CSDL.

## Actual

Backend văng ra lỗi **HTTP 413** kèm trả về nguyên cục trang web HTML lỗi: `PayloadTooLargeError: request entity too large`. Đương nhiên là không có user mới nào được tạo ra trong CSDL cả.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-212_api.png`

<img width="1280" height="720" alt="TC-FR01-212_api" src="https://github.com/user-attachments/assets/027bef13-f7ea-4b41-8c97-8f8a23c8ab2b" />

- TC-FR01-212: `HW02/A_FR01/evidence/TC-FR01-212_req.json`, `HW02/A_FR01/evidence/TC-FR01-212_res.json`, `HW02/A_FR01/evidence/TC-FR01-212_api.png`

## TC liên quan

- Fail (1): TC-FR01-212
- Nhóm dữ kiện: G9 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **A4** (giả định, SRS im lặng): A4 (Mật khẩu – độ dài): chỉ có cận dưới 8 ký tự. SRS không có cận trên → không có UB; BVA độ dài chỉ quanh LB = 8 (7, 8, 9) và NOM.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G9): `backend/server.js dòng 3–12`
- `TC-FR01-212_req.json` ghi `password` dạng rút gọn (`Hiep123$aaa… (200000 ký tự)`); chuỗi gửi thật được script dựng và kiểm độ dài = 200.000 (`tests/A_FR01/lib.ts` dòng 32–37).
- Body 413 (`TC-FR01-212_res.json`) có stack trace: 10 dòng `at ...` (raw-body, body-parser, router, cors), kèm đường dẫn tuyệt đối trên máy chạy.
- Sau TC-FR01-212, test kế tiếp trong lượt chạy (TC-FR01-213, tầng API, Fail) vẫn nhận phản hồi từ backend (HTTP 200, id 58) → tiến trình backend không dừng.

### Nhận định

- SRS không hề quy định độ dài tối đa của mật khẩu (A4) nên hệ thống lý thuyết phải chấp nhận mọi chuỗi dài.

- Tuy nhiên trong server.js, dòng 12 dùng app.use(bodyParser.json()) nguyên bản không hề cấu hình limit độ lớn payload. Thư viện body-parser mặc định sẽ chặn và văng lỗi 413 nếu body JSON vượt quá ~100 KB.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#26 — body trước</summary>

````markdown
# BUG-10

- **ID:** BUG-10
- **Tiêu đề:** Gửi request POST /api/register với Content-Type: text/plain, văng lỗi HTTP 500 kèm trang HTML stack trace
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch sẽ. Payload chứa các thông tin name, email, password hợp lệ theo SRS.

## Các bước tái hiện

1. Chuẩn bị payload JSON hợp lệ:
   `{"name": "Lê Tấn Hiệp", "email": "hiep.sv15@domain.com", "password": "Hiep123$"}`
2. Gửi request `POST http://localhost:3000/api/register` nhưng cố tình chỉnh Header `Content-Type: text/plain` (thay vì `application/json`).

## Expected (trích SRS)

Theo spec `API-REG` và giả định A11, API chỉ nhận body định dạng JSON (`application/json`). Khi client gửi Header `Content-Type` không đúng kiểu (như `text/plain`), backend phải xử lý từ chối an toàn bằng mã lỗi client **HTTP 4xx** (ví dụ 400 Bad Request hoặc 415 Unsupported Media Type) kèm body JSON chứa trường `error`, tuyệt đối không được để sập server hay trả về lỗi 5xx.

## Actual

Server backend, trả về mã **HTTP 500 Internal Server Error** cùng nguyên cục trang HTML chứa lỗi code:
`<pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<br>…</pre>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-214_api.png` 

<img width="1280" height="720" alt="TC-FR01-214_api" src="https://github.com/user-attachments/assets/db38c7ac-56f0-44eb-94a8-954794a2f7a8" />

- TC-FR01-214: `HW02/A_FR01/evidence/TC-FR01-214_req.json`, `HW02/A_FR01/evidence/TC-FR01-214_res.json`, `HW02/A_FR01/evidence/TC-FR01-214_api.png`

## TC liên quan

- Fail (1): TC-FR01-214
- Nhóm dữ kiện: G10 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **API-REG:** POST /api/register nhận body JSON {name, email, password}; thành công trả 200 {"message": "User registered successfully", "id": n} (api_specification.md dòng 14–21).
- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G10): `backend/server.js dòng 3–12`; `backend/server.js dòng 20–29`
- Body 500 (`TC-FR01-214_res.json`) có stack trace: 10 dòng `at ...`, dòng đầu `at D:\…\eshop-sut\backend\server.js:21:11`, kèm đường dẫn tuyệt đối trên máy chạy.
- Sau TC-FR01-214, test kế tiếp trong lượt chạy (TC-FR01-215, tầng UI, verdict Blocked theo A20, auto_status Fail) vẫn nhận phản hồi từ backend (fixture đăng nhập admin `POST /api/login` + `GET /api/admin/users` thành công, actual ghi `user mới=0`) → tiến trình backend không dừng.

### Nhận định

Có lẽ thiếu do middleware catch lỗi hoặc validate Content-Type:
- bodyParser.json() chỉ parse body khi Header là application/json. Khi gửi text/plain, middleware bỏ qua làm cho req.body bị undefined.

- Ở route handler dòng 21, code lại viết const { name, email, password } = req.body; (destructuring trực tiếp từ req.body).

- Vì req.body bị undefined nên JS quăng ra TypeError và do không có try-catch bọc lại nên Express tự động trả về trang lỗi HTML 500 mặc định.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

<details>
<summary>#26 — body sau</summary>

````markdown
# BUG-10

- **ID:** BUG-10
- **Tiêu đề:** Gửi request POST /api/register với Content-Type: text/plain, văng lỗi HTTP 500 kèm trang HTML stack trace
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/register (backend)
- Ngày chạy: 2026-10-19 (lượt tự động bắt đầu 22:42, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`

## Tiền điều kiện

Backend vừa khởi động lại, CSDL seed sạch sẽ. Payload chứa các thông tin name, email, password hợp lệ theo SRS.

## Các bước tái hiện

1. Chuẩn bị payload JSON hợp lệ:
   `{"name": "Lê Tấn Hiệp", "email": "hiep.sv15@domain.com", "password": "Hiep123$"}`
2. Gửi request `POST http://localhost:3000/api/register` nhưng cố tình chỉnh Header `Content-Type: text/plain` (thay vì `application/json`).

## Expected (trích SRS)

Theo spec `API-REG` và giả định A11, API chỉ nhận body định dạng JSON (`application/json`). Khi client gửi Header `Content-Type` không đúng kiểu (như `text/plain`), backend phải xử lý từ chối an toàn bằng mã lỗi client **HTTP 4xx** (ví dụ 400 Bad Request hoặc 415 Unsupported Media Type) kèm body JSON chứa trường `error`, tuyệt đối không được để sập server hay trả về lỗi 5xx.

## Actual

Server backend, trả về mã **HTTP 500 Internal Server Error** cùng nguyên cục trang HTML chứa lỗi code:
`<pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<br>…</pre>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR01-214_api.png` 

<img width="1280" height="720" alt="TC-FR01-214_api" src="https://github.com/user-attachments/assets/db38c7ac-56f0-44eb-94a8-954794a2f7a8" />

- TC-FR01-214: `HW02/A_FR01/evidence/TC-FR01-214_req.json`, `HW02/A_FR01/evidence/TC-FR01-214_res.json`, `HW02/A_FR01/evidence/TC-FR01-214_api.png`

## TC liên quan

- Fail (1): TC-FR01-214
- Nhóm dữ kiện: G10 trong `HW02/bugs/_groups_A_FR01.md`

## Yêu cầu

- **A11** (giả định, SRS im lặng): A11 (Mã lỗi API): api_specification.md chỉ mô tả phản hồi thành công 200. Giả định dữ liệu không hợp lệ phải nhận mã 4xx (không phải 2xx, không phải 5xx) kèm trường error; không cố định mã cụ thể (400/409/422).

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Đoạn code trích nguyên văn (xem `_groups_A_FR01.md`, nhóm G10): `backend/server.js dòng 3–12`; `backend/server.js dòng 20–29`
- Body 500 (`TC-FR01-214_res.json`) có stack trace: 10 dòng `at ...`, dòng đầu `at D:\…\eshop-sut\backend\server.js:21:11`, kèm đường dẫn tuyệt đối trên máy chạy.
- Sau TC-FR01-214, test kế tiếp trong lượt chạy (TC-FR01-215, tầng UI, verdict Blocked theo A20, auto_status Fail) vẫn nhận phản hồi từ backend (fixture đăng nhập admin `POST /api/login` + `GET /api/admin/users` thành công, actual ghi `user mới=0`) → tiến trình backend không dừng.

### Nhận định

Có lẽ thiếu do middleware catch lỗi hoặc validate Content-Type:
- bodyParser.json() chỉ parse body khi Header là application/json. Khi gửi text/plain, middleware bỏ qua làm cho req.body bị undefined.

- Ở route handler dòng 21, code lại viết const { name, email, password } = req.body; (destructuring trực tiếp từ req.body).

- Vì req.body bị undefined nên JS quăng ra TypeError và do không có try-catch bọc lại nên Express tự động trả về trang lỗi HTML 500 mặc định.

## Link GitHub Issue

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
````
</details>

