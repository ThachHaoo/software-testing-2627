# Bug report HW02 — quy ước

Bug report do SV tự viết (AI-01 §11). Thư mục này chỉ ghi thang đo, quy ước tên file và các trường bắt buộc.

## Severity — mức ảnh hưởng của lỗi tới hệ thống (ISTQB: *degree of impact*)

| Mức | Định nghĩa chung |
|---|---|
| Critical | Chức năng chính không dùng được hoặc gây mất/hỏng dữ liệu, sập hệ thống, lỗ hổng bảo mật nghiêm trọng; không có cách làm vòng. |
| High | Chức năng chạy sai so với đặc tả ở phần quan trọng; có cách làm vòng nhưng khó hoặc không chấp nhận được với người dùng. |
| Medium | Chức năng chạy sai ở phần ít quan trọng; có cách làm vòng dễ, ảnh hưởng hạn chế. |
| Low | Sai lệch thẩm mỹ, chính tả, bố cục; không ảnh hưởng tới chức năng. |

## Priority — mức khẩn cấp phải sửa (ISTQB: *level of business importance*)

| Mức | Định nghĩa chung |
|---|---|
| High | Phải sửa ngay, trước bản phát hành tiếp theo. |
| Medium | Sửa trong kế hoạch bình thường, sau các lỗi High. |
| Low | Sửa khi có thời gian; có thể hoãn sang phiên bản sau. |

Severity và Priority độc lập với nhau.

## Tên file

- `BUG-xx.md`, `xx` là số thứ tự hai chữ số, đánh liên tục cho cả HW02 (không theo feature): `BUG-01.md`, `BUG-02.md`, …
- Ảnh đính kèm đặt cạnh file: `BUG-xx_<mô tả ngắn>.png`. Ảnh trang GitHub Issues: `issues_page.png`.

## Trường bắt buộc

| Trường | Ghi chú |
|---|---|
| ID | `BUG-xx` |
| Tiêu đề | |
| Severity | theo thang ở trên |
| Priority | theo thang ở trên |
| Môi trường | SUT + commit, OS, trình duyệt, URL; xem `HW02/env/environment.md` |
| Tiền điều kiện | |
| Các bước tái hiện | |
| Expected (trích SRS) | trích nguyên văn mục SRS/giả định làm căn cứ |
| Actual | |
| Bằng chứng | đường dẫn ảnh/JSON trong `HW02/<feature>/evidence/` |
| TC liên quan | mã `TC-…` |
| Yêu cầu | mã yêu cầu (`FR-…`, `SEC-…`) |
| Ghi chú cô lập | đã chạy lại, reset dữ liệu, so UI với API… |
| Link GitHub Issue | `tkob-team/eshop-sut` |
