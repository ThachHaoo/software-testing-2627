# B_FR07 – chọn TC tự động hoá (bước 1)

Nguồn: `HW02/B_FR07/testcases.json` @ `352a34d` · 25 TC UI có inputs → chọn **15**.
Dữ liệu: `HW04/data/B_FR07.json` (expected chép nguyên văn + sha1).

Loại: Negative 5, Positive 10 · HW02 status: Fail 9, Pass 6

| # | tc_id | loại | kỹ thuật | BVA | HW02 auto / status | bug | lý do chọn |
|---|---|---|---|---|---|---|---|
| 1 | TC-FR07-01 | Positive | EP |  | Fail / Fail | BUG-21 | Positive giỏ trống (trạng thái rỗng + link về trang chủ); HW02 Fail BUG-21 |
| 2 | TC-FR07-02 | Positive | EP |  | Fail / Fail | BUG-15 | Positive thêm từ trang chi tiết SL 2, user đăng nhập; HW02 Fail BUG-15; có oracle phản hồi ≤ 2 s (B21) |
| 3 | TC-FR07-04 | Positive | EP |  | Fail / Fail | BUG-20 | Positive thêm lại sản phẩm đã có (cộng dồn) + badge, giỏ 2 dòng; HW02 Fail (badge – BUG-20; thêm từ chi tiết – BUG-15) |
| 4 | TC-FR07-08 | Positive | EP |  | Fail / Fail | BUG-19 | Positive xoá dòng + dialog xác nhận; HW02 Fail BUG-19 |
| 5 | TC-FR07-10 | Negative | EP |  | Pass / Pass |  | Negative số lượng âm; HW02 Pass (hộp đen, case gốc TC-61) – đối chứng |
| 6 | TC-FR07-11 | Negative | EP |  | Pass / Pass |  | Negative số lượng thập phân 1.5; HW02 Pass (hộp đen, case gốc TC-61) – thay TC-201 ở 1/6b |
| 7 | TC-FR07-13 | Negative | EP |  | Pass / Pass |  | Negative số lượng không phải số (ô type=number); HW02 Pass (hộp đen) – đối chứng kiểu khác TC-10 |
| 8 | TC-FR07-60 | Negative | BVA | LB-1 | Pass / Pass |  | Boundary LB-1 số lượng 0; HW02 Pass (hộp đen) – cặp với TC-61 |
| 9 | TC-FR07-61 | Positive | BVA | LB | Fail / Fail | BUG-15 | Boundary LB số lượng 1, giỏ rỗng; HW02 Fail BUG-15 (case gốc của nhiều Blocked) |
| 10 | TC-FR07-62 | Positive | BVA | LB+1 | Fail / Fail | BUG-15 | Boundary LB+1 số lượng 2; HW02 Fail BUG-15 |
| 11 | TC-FR07-63 | Positive | BVA | NOM | Fail / Fail | BUG-15 | Boundary NOM số lượng 5; HW02 Fail BUG-15 |
| 12 | TC-FR07-64 | Positive | BVA | LARGE | Fail / Fail | BUG-15 | Boundary LARGE 1000 (thay UB vì SRS không có cận trên, B1); HW02 Fail BUG-15; kiểm định dạng tổng tiền lớn |
| 13 | TC-FR07-66 | Positive | BVA | LB | Pass / Pass |  | Boundary xoá dòng cuối (1 → 0 dòng, chuyển trạng thái giỏ trống); HW02 Pass – đối chứng |
| 14 | TC-FR07-200 | Negative (AI suy ra, SV duyệt) | EG |  | Pass / Pass |  | Negative (EG, SV) payload XSS vào ô Số lượng; HW02 Pass – kiểm không bật alert |
| 15 | TC-FR07-205 | Positive (AI suy ra, SV duyệt) | EG |  | Fail / Fail | BUG-15 | Positive (EG, SV) đổi Số lượng giữa 2 lần thêm ở trang chi tiết; HW02 Fail BUG-15 |

## Không chọn

| TC / nhóm | lý do |
|---|---|
| TS-DOM-API, TS-BVA-API, TS-SV-API | tầng API (POST /api/cart) – HW04 tự động hoá web frontend; giỏ web không gọi API này |
| TS-GUI TC-FR07-90…99 | checklist thuộc tính tĩnh, không có inputs → không data-driven |
| TC-FR07-03, 06, 65 (Blocked) | HW02 Blocked, bug gốc BUG-15 (dựng giỏ từ trang chi tiết không thêm được) – cùng bug với 61/62/63 đã chọn |
| TC-FR07-05, 07 (Blocked) | HW02 Blocked, bug gốc BUG-18 (trang giỏ không có nút '+'/'-'); sẽ Blocked lại vì thiếu control |
| TC-FR07-09 (Blocked) | HW02 Blocked, bug gốc BUG-19 (không có dialog nên không có lựa chọn Huỷ) – cùng bug với TC-08 đã chọn |
| TC-FR07-203, 206 (Blocked) | HW02 Blocked, bug gốc BUG-15 (sản phẩm không được thêm từ trang chi tiết) |
| Case cần tải lại trang | không có trong 25 ứng viên: mọi case điều hướng bằng link navbar (quy trình HW02 B0d); không Expected nào phụ thuộc lưu trữ giỏ |
| TC-FR07-12 | cùng nhóm số lượng không hợp lệ với TC-10/11/13/60, HW02 Pass hộp đen (case gốc TC-61) |
| TC-FR07-201 (bỏ ở 1/6b) | nhạy thời gian (20 lần bấm trong 0,4 s; HW02 notes ghi lượt 1 chưa chốt verdict) → dễ flaky (B2) |

## Oracle dữ liệu của giỏ (SUT)

- Giỏ web là state React: `../eshop-sut/frontend-web/src/context/CartContext.jsx` dòng 6 `useState([])`; file không gọi axios/API, không dùng localStorage → giỏ web không đọc được qua API (GET /api/cart là giỏ phía server, web không dùng).
- Oracle dữ liệu qua API (toEqual danh sách trước/sau) KHÔNG áp dụng cho giỏ. Thay bằng trạng thái giỏ trên UI ở trang /cart: số dòng, tên/Đơn giá/Số lượng/Thành tiền từng dòng, Tổng, badge — chụp TRƯỚC và SAU thao tác rồi so (quy trình HW02 bước 3–6).
- Không tải lại trang, không gõ URL sau lần mở đầu tiên của case (mất state). API chỉ dùng để tạo user (POST /api/register) và dọn dẹp (DELETE /api/admin/users/:id).
- Giá sản phẩm lấy theo bảng seed trong tiền điều kiện HW02 (database.js dòng 98–102), không đọc qua API.

## Quyết định của SV

- B1: loại TC-200 = Negative, TC-205 = Positive (AI suy ra, SV duyệt); TC-201 bỏ nên không còn cần loại.
- B2: thay TC-201 (nhạy thời gian) bằng TC-11.

## Tiêu chí

- 15 TC tầng UI, nguồn HW02/B_FR07/testcases.json; Blocked theo HW02 tối đa 2 → chọn 0
- đủ loại: Positive (EP, BVA, EG), Negative (EP, BVA, EG), Boundary qua điểm BVA LB-1/LB/LB+1/NOM/LARGE
- ưu tiên TC từng Fail ở HW02 (9 TC); giữ 6 TC Pass làm đối chứng (10, 11, 13, 60, 66, 200)
- phủ bug HW02: BUG-15, 19, 20, 21 (bug_id lấy từ mục TC liên quan của HW02/bugs/BUG-xx.md vì testcases.json không ghi)
