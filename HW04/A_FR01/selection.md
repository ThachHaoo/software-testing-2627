# A_FR01 – chọn TC tự động hoá (bước 1)

Nguồn: `HW02/A_FR01/testcases.json` @ `af48958` · 59 TC UI có inputs → chọn **15**.
Dữ liệu: `HW04/data/A_FR01.json` (expected chép nguyên văn + sha1).

Loại: Boundary 5, Negative 7, Positive 3 · HW02 status: Fail 8, Pass 7

| # | tc_id | loại | kỹ thuật | BVA | HW02 auto / status | bug | lý do chọn |
|---|---|---|---|---|---|---|---|
| 1 | TC-FR01-01 | Positive | EP |  | Fail / Fail | BUG-01 | Positive danh nghĩa (tên không dấu, mật khẩu mạnh); HW02 Fail BUG-01 → kiểm hồi quy lỗi chính của form |
| 2 | TC-FR01-02 | Positive | EP |  | Fail / Fail | BUG-01 | Positive tên có dấu + mật khẩu 2 ký tự đặc biệt; HW02 Fail BUG-01; thêm lớp EC2 (tiếng Việt có dấu) |
| 3 | TC-FR01-05 | Negative | EP |  | Pass / Pass |  | Negative Họ Tên rỗng (ô bắt buộc); HW02 Pass → đối chứng, oracle validationMessage (A16) |
| 4 | TC-FR01-07 | Negative | EP |  | Pass / Pass |  | Negative Email rỗng; HW02 Pass → đối chứng ô bắt buộc thứ hai |
| 5 | TC-FR01-17 | Negative | EP |  | Pass / Pass |  | Negative Mật khẩu rỗng; HW02 Pass → đối chứng ô bắt buộc thứ ba |
| 6 | TC-FR01-18 | Negative | EP |  | Pass / Pass |  | Negative mật khẩu thiếu chữ hoa (đại diện nhóm luật độ mạnh 18–24); HW02 Pass hộp đen |
| 7 | TC-FR01-22 | Negative | EP |  | Pass / Pass |  | Negative mật khẩu thiếu chữ số; HW02 Pass (hộp đen) – bù sau 1/6b, chạy trọn luồng |
| 8 | TC-FR01-23 | Negative | EP |  | Pass / Pass |  | Negative mật khẩu thiếu ký tự đặc biệt; HW02 Pass (hộp đen) – bù sau 1/6b, chạy trọn luồng |
| 9 | TC-FR01-63 | Boundary | BVA | LB-1 | Pass / Pass |  | Boundary mật khẩu 7 ký tự (LB-1, phía từ chối); HW02 Pass → cặp với TC-64 |
| 10 | TC-FR01-64 | Boundary | BVA | LB | Fail / Fail | BUG-01 | Boundary mật khẩu 8 ký tự (LB, phía chấp nhận); HW02 Fail BUG-01 |
| 11 | TC-FR01-68 | Boundary | BVA | LB | Fail / Fail | BUG-01 | Boundary đúng 1 chữ hoa (LB); HW02 Fail BUG-01 – bù sau 1/6b, chạy trọn luồng tới oracle |
| 12 | TC-FR01-74 | Boundary | BVA | LB | Fail / Fail | BUG-01 | Boundary đúng 1 chữ số (LB); HW02 Fail BUG-01 – bù sau 1/6b |
| 13 | TC-FR01-77 | Boundary | BVA | LB | Fail / Fail | BUG-01 | Boundary đúng 1 ký tự đặc biệt (LB); HW02 Fail BUG-01 – bù sau 1/6b |
| 14 | TC-FR01-202 | Negative (AI suy ra, SV duyệt) | EG |  | Fail / Fail | BUG-02 | Negative (EG, SV) mật khẩu có khoảng trắng thay ký tự đặc biệt bị chấp nhận; HW02 Fail BUG-02 – lỗi khác BUG-01 |
| 15 | TC-FR01-211 | Positive (AI suy ra, SV duyệt) | EG |  | Fail / Fail | BUG-01 | Positive (EG, SV) mật khẩu có khoảng trắng đầu + đăng nhập lại; HW02 Fail BUG-01; có bước đăng nhập lại (luồng 2 màn hình) |

## Không chọn

| TC / nhóm | lý do |
|---|---|
| TS-DOM-API, TS-BVA-API, TC-FR01-201/206/207/209/212–214/219–222/224–232 (API) | tầng API – HW04 tự động hoá web frontend |
| TS-GUI TC-FR01-90…94 | checklist thuộc tính tĩnh, không có inputs → không data-driven |
| TC-FR01-216 | cần tạo user qua API rồi quan sát nơi hiển thị Họ Tên – case thăm dò (EXP), đã chạy tay ở HW02 |
| TC-FR01-223 | case quan sát, SRS không có Expected |
| TC-FR01-04, 06, 09–13, 15 | cùng nhóm / cùng bị chặn BUG-01 bởi TC-01 |
| TC-FR01-25, 27 | cùng nguyên nhân Blocked BUG-14 |
| TC-FR01-60 | trùng giá trị với TC-05 |
| TC-FR01-200, 203–205, 208, 210, 215, 217, 218 | TC của SV cùng bị chặn bởi BUG-01 hoặc trùng lớp đã chọn |
| TC-FR01-03, 08, 14, 61 (bỏ ở 1/6b) | HW02 Blocked, bug gốc BUG-01 – bị chặn bởi TC-FR01-01 (form từ chối bằng 'Mật khẩu quá yếu!' nên biến mục tiêu Email/Họ Tên không được kiểm); TC-01 đã chọn |
| TC-FR01-26 (bỏ ở 1/6b) | HW02 Blocked BUG-14 – form không có ô Xác nhận mật khẩu (S2) |
| UB / UB+1 | không có trong HW02: SRS không có cận trên độ dài Họ Tên/Mật khẩu/số ký tự mỗi loại (A1, A4) |
| TC-FR01-62, 65–67, 69–73, 75, 76, 78 | cùng nhóm BVA với TC đã chọn; giữ mỗi biến đếm ký tự 1 điểm LB (68, 74, 77) + cặp độ dài 63/64 |
| TC-FR01-19–21, 24 | cùng nhóm luật độ mạnh mật khẩu với TC-18, HW02 Pass hộp đen |

## Quyết định của SV

- S1: loại TC-202 = Negative, TC-211 = Positive (AI suy ra, SV duyệt).
- S2: bỏ TC-26 (Blocked BUG-14).
- Blocked tối đa 2: bỏ 03, 08, 14, 61 (cùng bug gốc BUG-01 với TC-01 đã chọn) → còn 0 TC Blocked theo HW02.
- Bù 5 TC: không có UB/UB+1 → BVA LB Fail 68, 74, 77 + EP Pass 22, 23.

## Tiêu chí

- 15 TC tầng UI (đề ≥ 12; dư 3 để bù case không tự động được), nguồn HW02/A_FR01/testcases.json
- đủ loại: Positive (EP + EG), Negative (EP + EG), Boundary (BVA)
- ưu tiên TC từng Fail ở HW02 (status hoặc auto_status); mỗi nhóm triệu chứng/bug giữ 1–3 đại diện
- giữ TC Pass ở HW02 (05, 07, 17, 18, 22, 23, 63) làm đối chứng – phát hiện hồi quy và kiểm script không Fail giả
- phủ bug HW02: BUG-01 (01, 02, 64, 68, 74, 77, 211), BUG-02 (202)
