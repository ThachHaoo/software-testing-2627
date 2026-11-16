# A_FR01 – chọn TC tự động hoá (bước 1)

Nguồn: `HW02/A_FR01/testcases.json` @ `af48958` · 59 TC UI có inputs → chọn **15**.
Dữ liệu: `HW04/data/A_FR01.json` (expected chép nguyên văn + sha1).

Loại: Boundary 3, Negative 8, Positive 4 · HW02 status: Blocked 5, Fail 5, Pass 5

| # | tc_id | loại | kỹ thuật | BVA | HW02 auto / status | bug | lý do chọn |
|---|---|---|---|---|---|---|---|
| 1 | TC-FR01-01 | Positive | EP |  | Fail / Fail | BUG-01 | Positive danh nghĩa (tên không dấu, mật khẩu mạnh); HW02 Fail BUG-01 → kiểm hồi quy lỗi chính của form |
| 2 | TC-FR01-02 | Positive | EP |  | Fail / Fail | BUG-01 | Positive tên có dấu + mật khẩu 2 ký tự đặc biệt; HW02 Fail BUG-01; thêm lớp EC2 (tiếng Việt có dấu) |
| 3 | TC-FR01-03 | Positive | EP |  | Fail / Blocked | BUG-01 | Positive biên định dạng: email có khoảng trắng đầu/cuối (A3 – lưu đã cắt); HW02 auto Fail, chốt Blocked bởi TC-01 |
| 4 | TC-FR01-05 | Negative | EP |  | Pass / Pass |  | Negative Họ Tên rỗng (ô bắt buộc); HW02 Pass → đối chứng, oracle validationMessage (A16) |
| 5 | TC-FR01-07 | Negative | EP |  | Pass / Pass |  | Negative Email rỗng; HW02 Pass → đối chứng ô bắt buộc thứ hai |
| 6 | TC-FR01-08 | Negative | EP |  | Pass / Blocked | BUG-01 | Negative Email thiếu '@' (đại diện nhóm sai định dạng 08–13); HW02 chốt Blocked bởi TC-01 |
| 7 | TC-FR01-14 | Negative | EP |  | Pass / Blocked | BUG-01 | Negative email trùng tài khoản seed (luật duy nhất FR-01); cần oracle API trước/sau; HW02 Blocked bởi TC-01 |
| 8 | TC-FR01-17 | Negative | EP |  | Pass / Pass |  | Negative Mật khẩu rỗng; HW02 Pass → đối chứng ô bắt buộc thứ ba |
| 9 | TC-FR01-18 | Negative | EP |  | Pass / Pass |  | Negative mật khẩu thiếu chữ hoa (đại diện nhóm luật độ mạnh 18–24); HW02 Pass hộp đen |
| 10 | TC-FR01-26 | Negative | EP |  | Blocked / Blocked | BUG-14 | Negative Xác nhận mật khẩu khác Mật khẩu; HW02 Blocked BUG-14 (form không có ô) → kiểm cách script xử lý trường vắng mặt |
| 11 | TC-FR01-61 | Boundary | BVA | LB | Fail / Blocked | BUG-01 | Boundary Họ Tên 1 ký tự (LB); HW02 auto Fail, chốt Blocked bởi TC-01 |
| 12 | TC-FR01-63 | Boundary | BVA | LB-1 | Pass / Pass |  | Boundary mật khẩu 7 ký tự (LB-1, phía từ chối); HW02 Pass → cặp với TC-64 |
| 13 | TC-FR01-64 | Boundary | BVA | LB | Fail / Fail | BUG-01 | Boundary mật khẩu 8 ký tự (LB, phía chấp nhận); HW02 Fail BUG-01; đại diện nhóm BVA mật khẩu 64–78 (cùng triệu chứng) |
| 14 | TC-FR01-202 | Negative (suy ra) | EG |  | Fail / Fail | BUG-02 | Negative (EG, SV) mật khẩu có khoảng trắng thay ký tự đặc biệt bị chấp nhận; HW02 Fail BUG-02 – lỗi khác BUG-01 |
| 15 | TC-FR01-211 | Positive (suy ra) | EG |  | Fail / Fail | BUG-01 | Positive (EG, SV) mật khẩu có khoảng trắng đầu + đăng nhập lại; HW02 Fail BUG-01; có bước đăng nhập lại (luồng 2 màn hình) |

## Không chọn

| TC / nhóm | lý do |
|---|---|
| TS-DOM-API, TS-BVA-API, TC-FR01-201/206/207/209/212–214/219–222/224–232 (API) | tầng API – HW04 tự động hoá web frontend |
| TS-GUI TC-FR01-90…94 | checklist thuộc tính tĩnh, không có inputs → không data-driven |
| TC-FR01-216 | cần tạo user qua API rồi quan sát nơi hiển thị Họ Tên – case thăm dò (EXP), đã chạy tay ở HW02 |
| TC-FR01-223 | case quan sát, SRS không có Expected |
| TC-FR01-04, 06, 09–13, 15 | cùng nhóm với TC đã chọn (email sai định dạng / trùng email / Họ Tên khoảng trắng), HW02 cùng bị chặn bởi TC-01 |
| TC-FR01-19–24 | cùng nhóm luật độ mạnh mật khẩu với TC-18, HW02 Pass hộp đen |
| TC-FR01-25, 27 | cùng nguyên nhân Blocked BUG-14 với TC-26 |
| TC-FR01-60 | trùng giá trị với TC-05 |
| TC-FR01-62, 65–78 | cùng triệu chứng BUG-01 với TC-61/64; giữ 1 cặp biên độ dài mật khẩu (63/64) + 1 điểm Họ Tên (61) |
| TC-FR01-200, 203–205, 208, 210, 215, 217, 218 | TC của SV cùng bị chặn bởi BUG-01 hoặc trùng lớp đã chọn |

## Tiêu chí

- 15 TC tầng UI (đề ≥ 12; dư 3 để bù case không tự động được), nguồn HW02/A_FR01/testcases.json
- đủ loại: Positive (EP + EG), Negative (EP + EG), Boundary (BVA)
- ưu tiên TC từng Fail ở HW02 (status hoặc auto_status); mỗi nhóm triệu chứng/bug giữ 1–3 đại diện
- giữ 4 TC Pass ở HW02 (05, 07, 17, 63) làm đối chứng – phát hiện hồi quy và kiểm script không Fail giả
- phủ 3 bug HW02: BUG-01 (01, 02, 64, 211…), BUG-02 (202), BUG-14 (26)
- loại của TC-202/211 (HW02 không ghi type) do AI suy ra từ Expected – SV kiểm lại
