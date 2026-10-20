# BUG-20

- **ID:** BUG-20
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173 — navbar, trang /cart (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-04_ui.png`
- TC-FR07-04: `HW02/B_FR07/evidence/TC-FR07-04_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-04_ui.png`

## TC liên quan

- Fail (1): TC-FR07-04
- Nhóm dữ kiện: G6 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-23.2:** (GUI, B16) Link "Giỏ hàng" phải hiển thị badge số lượng sản phẩm trong giỏ.
- Đạt trong cùng case: —
- Chưa đánh giá được: FR-07.3 (EC10/EC37: thêm từ trang chi tiết không vào giỏ, case gốc TC-61), FR-07.1 (nhãn cột kiểm ở TC-95)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-04): `đăng nhập cart04_1792476872458@domain.com: navbar có tên user; TRƯỚC: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge; ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/App.jsx` dòng 23

  ```jsx
    23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
