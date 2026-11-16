# A_FR01 – review spec của SV (bước 5)

Spec được review: `HW04/tests/A_FR01.spec.ts` @ `6fc76b5` (bản AI bước 3 `9a5e558` + sửa 5/6a). Bản AI đóng băng: `HW04/appendix/ai-outputs/A_FR01/step3/A_FR01.spec.ts`.

## Danh sách của SV (nguyên văn)

Soi spec: 

Oracle phụ thuộc regex tiếng Việt cứng nhắc: vì dùng regex để phân tích câu văn tiếng việt, nên giả sử expected diễn đạt lệch 1 xíu thì regex phân tích sai --> bỏ sót kiểm tra thông báo lỗi hoặc crash.
Đồng bộ sau Submit dùng Promise.race cùng vboiws catch(() => {}) dễ gây flaky: submit xong thì đua giữa waitForURL và r.error.waitFor. Giả sử mạng lag quá 5s, timeout không bắt dực thì script hiểu nhầm trình duyệt chặn submit.
Làm dụng expect.soft: nếu bước submit thất bại ở ban đầu, mà vẫn chạy tiếp xuống gọi API users.list(), có thể race condition khi backend chưa ghi xong DB, rồi lại chạy tiếp relogin --> nhiều lỗi.
Dọn dữ liệu (cleanup) và resetDb() chưa an toàn khi chạy song song: có thể khi chạy nhiều trình duyệt cùng lúc thì các worker restart backend đè lên nhau.

## Phiên thảo luận bổ sung

- **Serial** – `test.describe.configure({ mode: 'serial' })` (bản AI, dòng 44): TC đầu Fail thì 14 TC còn lại không chạy. Đã sửa ở `HW04[A-FR01] 5/6a`.
- **`^` ở dòng 28** – `/^Không có thông báo lỗi|Đăng ký thành công/`: `^` chỉ neo nhánh thứ nhất; nhánh "Đăng ký thành công" khớp ở bất kỳ đâu trong câu. Sửa ở 5/6c.
- **RegExp không escape ở dòng 38** – `new RegExp(h[1])`, `new RegExp(h[2].trim())` dựng regex trực tiếp từ chữ trong expected; ký tự đặc biệt (`.`, `(`, `+`, `?`…) sẽ đổi nghĩa hoặc làm regex lỗi. Sửa ở 5/6c.
- **`users.list()` không chờ POST (dòng 103)** – oracle API gọi ngay sau khi race kết thúc, không chờ phản hồi `POST /api/register`; nếu request còn đang xử lý thì danh sách "sau" chưa có user mới. Sửa ở 5/6b.

## Sửa theo review

| Commit | Mục |
|---|---|
| 5/6a | bỏ mode serial |
| 5/6b | chờ phản hồi POST / xác nhận không có POST rồi mới gọi `users.list()`; bỏ `catch` rỗng, annotation nhánh phản hồi; timeout → Blocked |
| 5/6c | `oracleOf`: nhóm `^(…|…)`, escape chuỗi trước `new RegExp`; reject không đọc được ý thông báo → annotation "oracle thông báo yếu" |
| 5/6d | `beforeAll` dừng nếu workers > 1 |
