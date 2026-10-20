# BUG-21

- **ID:** BUG-21
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

- TC-FR07-01: `HW02/B_FR07/evidence/TC-FR07-01_failed.png`, `HW02/B_FR07/evidence/TC-FR07-01_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-01
- Nhóm dữ kiện: G7 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-07.7:** Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng. — vi phạm ở: thiếu hình minh hoạ; có thông báo 'Giỏ hàng của bạn đang trống'
- **FR-24.3:** Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện (bổ sung FR-07.7). — vi phạm ở: thiếu icon/hình minh hoạ

- Đạt trong cùng case: FR-07.5 (link về trang chủ → URL '/'), FR-23.2 (badge ẩn khi giỏ trống, chấp nhận theo B22)
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G7: UI · trang giỏ trống: không có hình minh hoạ/icon (img/svg)
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-01, nguyên văn): TRƯỚC: không có bảng (giỏ trống); trạng thái trống: bảng=không, ảnh/icon=không, chữ="Giỏ hàng của bạn đang trốngTiếp tục mua sắm"; URL sau thao tác=http://localhost:5173/
- Cùng case: dòng chữ 'Giỏ hàng của bạn đang trống' có; link về trang chủ → URL '/' đạt.
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 20–27 (xem `bugs_facts.md`, G7)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
