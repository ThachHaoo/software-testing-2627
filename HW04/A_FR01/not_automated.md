# A_FR01 – TC / phần expected không tự động hoá được

Dữ kiện lấy từ `A_FR01/selection.json` (mục `excluded`) và annotation trong report chính thức `reports/chrome_20261117T134709/` (giống edge/firefox).

## TC không đưa vào script (không tự động hoá được ở tầng UI)

| TC | Lý do (nguồn) | Cách kiểm |
|---|---|---|
| TC-FR01-216 | Case thăm dò (EXP): tạo user qua API rồi quan sát nơi hiển thị Họ Tên – không có expected đóng (selection.json) | Đã chạy tay ở HW02 |
| TC-FR01-223 | Case quan sát, SRS không có Expected (selection.json) | Quan sát tay |
| TS-GUI TC-FR01-90…94 | Checklist thuộc tính tĩnh, không có `inputs` → không data-driven (selection.json) | Checklist GUI (HW03) |
| TS-DOM-API, TS-BVA-API, TC-FR01-201/206/207/209/212–214/219–222/224–232 | Tầng API – HW04 tự động hoá web frontend (selection.json) | Bộ test API của HW02 |

## Phần expected không kiểm được đầy đủ trong TC đã tự động

| TC | Phần không tự động / kiểm yếu | Lý do | Script làm gì thay |
|---|---|---|---|
| 13 TC có cột `Xác nhận mật khẩu` (01, 02, 05, 07, 17, 18, 22, 23, 63, 64, 68, 74, 77) | Bước nhập V5 'Xác nhận mật khẩu' | Form `/register` không có ô này (HW02 BUG-14, giả định A17) | Bỏ bước nhập, ghi annotation `A17` |
| TC-FR01-18, 22, 23, 63 | Nội dung thông báo lỗi | Expected không nêu ý của thông báo | Chỉ kiểm hộp lỗi hiện và có chữ; annotation `oracle thông báo yếu` |
