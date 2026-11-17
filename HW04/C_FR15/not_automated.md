# C_FR15 – TC / phần expected không tự động hoá được

Dữ kiện lấy từ `C_FR15/selection.json` (mục `excluded`) và annotation trong report chính thức `reports/chrome_20261117T151143/` (giống edge/firefox).

## TC không đưa vào script

| TC | Lý do (nguồn) | Cách kiểm |
|---|---|---|
| TC-FR15-206 | Chuỗi 2 thao tác (Sửa SP1 → Sửa SP2 không Hủy) không biểu diễn được bằng cột 'Thao tác CRUD' một lần của procedure; HW02 Pass (selection.json) | Chạy tay (HW02) |
| TC-FR15-202 | HW02 ghi lỗi thiết kế TC: expected 7000000 ≠ giá trị số của 00700000 (= 700000) – không dùng expected sai (selection.json) | Sửa TC ở HW02 trước khi tự động |
| TS-GUI TC-FR15-90…94, TS-SV-GUI | Checklist thuộc tính tĩnh, không có `inputs` → không data-driven (selection.json) | Checklist GUI (HW03) |
| TS-DOM-API, TS-BVA-API-*, TS-SV-API | Tầng API – HW04 tự động hoá web admin; API chỉ dùng làm oracle dữ liệu và dựng/dọn dữ liệu (selection.json) | Bộ test API của HW02 |

## Phần expected kiểm yếu trong TC đã tự động

| TC | Phần kiểm yếu | Lý do | Script làm gì thay |
|---|---|---|---|
| TC-FR15-15, TC-FR15-78 | "có thông báo lỗi" | Sau khi bấm Lưu chỉ có hộp thoại "Cập nhật thành công!"; HW02 H4 không phân loại nội dung thông báo | Đếm là "có thông báo" như HW02, ghi annotation `oracle thông báo yếu` để SV xét (review_sv.md Bản 2 ý 1) |
