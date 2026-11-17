# B_FR07 – phần không tự động hoá được

| TC | Phần expected không tự động | Lý do | Script làm gì thay | Cách kiểm |
|---|---|---|---|---|
| TC-FR07-08 | "dòng chưa bị xoá khi dialog đang mở" | Dialog xác nhận nếu là dialog native (`window.confirm`) thì khoá luồng JS của trang: khi dialog đang mở, Playwright không đọc được DOM (mọi lệnh đọc trang chờ tới khi dialog đóng); handler `page.on('dialog')` chỉ nhận loại + nội dung rồi phải `accept()`/`dismiss()` thì trang mới chạy tiếp → không quan sát được trạng thái bảng giỏ **trong lúc** dialog mở. | Ghi annotation `oracle không tự động`; vẫn kiểm có đúng 1 dialog loại `confirm` sau khi bấm Xóa (chờ tối đa 2 s) và trạng thái giỏ SAU khi xác nhận. | Kiểm tay: bấm Xóa, khi dialog đang hiện nhìn bảng giỏ (dòng 'Tai nghe AirPods Pro 2' còn hay mất), rồi mới bấm xác nhận. |

Ghi chú: ở SUT hiện tại (lượt thử 1) bấm Xóa không hiện dialog nào (`dialog sau khi bấm xoá = []`), nên phần này hiện cũng không có trạng thái "dialog đang mở" để kiểm.
