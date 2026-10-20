# BUG-28

- **ID:** BUG-28
- **Tiêu đề:** 
- **Severity:** 
- **Priority:** 

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173 (frontend-web), API http://localhost:3000
- Lượt chính thức: lượt 2, 2026-10-20 13:14 (Asia/Saigon); TC-FR07-201, 209 từ lượt 3 (13:17), kết quả trùng lượt 2
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện


## Các bước tái hiện


## Expected (trích SRS)


## Actual


## Bằng chứng

<details>
<summary>Evidence từng TC (1)</summary>

- TC-FR07-97: `HW02/B_FR07/evidence/TC-FR07-97_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-97
- Nhóm dữ kiện: G14 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-07.5:** Có nút Tiếp tục mua sắm để quay về trang chủ.
- **B12 (giả định):** B12 (nhãn chính xác) (SV chốt 2026-10-20): các cụm in đậm trong FR-07 là nhãn — 'Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác', 'Xóa sản phẩm', 'Tiếp tục mua sắm', 'Tổng cộng'. So khớp đúng chữ, PHÂN BIỆT hoa/thường, chuẩn hoá Unicode NFC trước khi so; coi hai cách đặt dấu 'óa'/'oá' là như nhau (vd 'Xóa' = 'Xoá'). Chỉ kiểm ở TC-FR07-95…98; case chức năng định vị nút/link không dựa vào chữ.

- Đạt trong cùng case: —
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G14: UI · trang giỏ: link về trang chủ có chữ '← Mua tiếp' (SRS: 'Tiếp tục mua sắm')
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-97, nguyên văn): nhãn đọc được=["← Mua tiếp"]
- Trang giỏ trống có link 'Tiếp tục mua sắm' (Cart.jsx dòng 24); TC-FR07-97 kiểm khi giỏ có 1 dòng.
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 65–68 (xem `bugs_facts.md`, G14)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
