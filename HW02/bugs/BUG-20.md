# BUG-20

- **ID:** BUG-20
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

- TC-FR07-04: `HW02/B_FR07/evidence/TC-FR07-04_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-04_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-04
- Nhóm dữ kiện: G6 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-07.3:** Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.
- **FR-07.1:** Giỏ hàng hiển thị danh sách sản phẩm với các cột: Sản phẩm, Đơn giá, Số lượng, Thành tiền, Thao tác.
- **FR-23.2:** (GUI, B16) Link "Giỏ hàng" phải hiển thị badge số lượng sản phẩm trong giỏ.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G6: UI · navbar: không có badge số lượng trên/cạnh link tới /cart khi giỏ có hàng
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-04, nguyên văn): đăng nhập cart04_1792476872458@domain.com: navbar có tên user; TRƯỚC: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge; ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge
- Đoạn code trích nguyên văn: `frontend-web/src/App.jsx` dòng 23 (xem `bugs_facts.md`, G6)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
