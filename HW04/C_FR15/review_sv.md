# C_FR15 – SV review spec AI (bước 5)

Spec soi: `HW04/tests/C_FR15.spec.ts` @ `370c9cd` (bản AI, đông lạnh ở `HW04/appendix/ai-outputs/C_FR15/step3/`). Lượt thử 1: `HW04/C_FR15/RUN.md`.

## Bản 1 – SV tự soi (chép nguyên văn)

| # | Ý của SV (nguyên văn) | Đối chiếu code (phiên thảo luận) |
|---|---|---|
| 1 | Lỗi render toàn bảng khi Sửa: như khi sửa 1 sản phẩm, thì frontend ghi đè tên mới lên toàn bộ các dòng sản phẩm trong bảng, nhưng cột giá thì lại không cập nhật. | Bug SUT, script phát hiện (dòng 210–211 → TC-03 Fail). |
| 2 | Thiếu phản hồi trực quan sau thao tác: Thao tác Thêm và Xoá không có thông báo thành công, còn thao tác Sửa thì lại dùng alert() của trình duyệt và báo thành công giả ngay cả khi UI render lỗi. | Theo Expected (TC-01 C13, TC-03 "Không đánh giá thông báo"). |
| 3 | Lệch ngôn ngữ thông báo validation: Dùng validation mặc định của trình duyệt nên câu báo lỗi hiển thị tiếng Anh dù hệ thống cấu hình tiếng Việt. | Theo Expected/H4 (dòng 130). |
| 4 | Bỏ qua kiểm tra thông báo thành công: kịch bản hiện đang bỏ qua việc đánh giá thông báo phản hồi ở luồng Thêm và Sửa, nên test sẽ không bắt được lỗi UX hoặc thông báo sai ngữ cảnh. | Theo Expected (TC-01 C13, TC-03 "Không đánh giá thông báo"). |
| 5 | Phụ thuộc backend restart để reset dữ liệu: Mỗi lần chạy đều khởi động lại backend để đưa DB về trạng thái 5 sản phẩm, nên gây chậm thời gian thực thi và bỏ qua các lỗi khi mà data nó nhiều. | Restart sau mỗi Fail đúng; nhiều dữ liệu = phạm vi. |

## Bản 2 – sau đối chiếu (chép nguyên văn)

| # | Ý (nguyên văn) | Nguồn | Xử lý |
|---|---|---|---|
| 1 | Coi hộp thoại thành công là "có thông báo lỗi": Biến "errShown = invalid \|\| newDialogs.length > 0 \|\| pageMsgs" đếm mọi hộp thoại xuất hiện mà không phân biệt nó là gì. | Phiên thảo luận | R3=a: giữ errShown theo H4 (HW02), ghi là điểm yếu; không sửa spec. |
| 2 | Phụ thuộc backend restart để reset dữ liệu: Mỗi lần chạy đều khởi động lại backend để đưa DB về trạng thái 5 sản phẩm, nên gây chậm thời gian thực thi và bỏ qua các lỗi khi mà data nó nhiều. | SV | Không sửa (xem Bản 1 ý 5). |
| 3 | Ô nhập liệu không hợp lệ bị ghi nhận 2 lần: Khi kiểm tra validation, gọi checkValidity() trước khi ấn submit sẽ kích hoạt sự kiện invalid. | Claude Code (báo cáo lệnh #17) | Sửa ở 5/6a: chỉ ghi sự kiện sau khi bấm 'Lưu sản phẩm'. |
