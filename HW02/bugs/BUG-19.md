# BUG-19

- **ID:** BUG-19
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

- TC-FR07-08: `HW02/B_FR07/evidence/TC-FR07-08_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-08
- Blocked ghi case gốc (1): TC-FR07-09
- Nhóm dữ kiện: G5 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.4:** Nút Xóa sản phẩm phải có dialog xác nhận trước khi thực hiện.
- **FR-24.2:** Khi xóa item khỏi giỏ phải có dialog xác nhận (trùng FR-07.4).

- Đạt trong cùng case: B4 (Tổng SAU 4000000 = Thành tiền dòng còn lại), xoá dòng (dòng AirPods bị xoá, dòng Keychron không đổi)
- Chưa đánh giá được trong cùng case: FR-07.1 (nhãn cột kiểm ở TC-95)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G5: UI · trang giỏ: bấm nút xoá → không có dialog xác nhận, dòng bị xoá ngay
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-08, nguyên văn): đăng nhập cart08_1792476880905@domain.com: navbar có tên user; TRƯỚC: 2 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Bàn phím cơ Keychron Q1 | Đơn giá 4000000 | SL 1 | Thành tiền 4000000]; Tổng 10000000; không có badge; không có dialog; SAU: 1 dòng: [Bàn phím cơ Keychron Q1 | Đơn giá 4000000 | SL 1 | Thành tiền 4000000]; Tổng 4000000; không có badge
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 49–55; `frontend-web/src/context/CartContext.jsx` dòng 12–16 (xem `_groups_B_FR07.md`, G5)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
