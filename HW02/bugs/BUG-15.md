# BUG-15

- **ID:** BUG-15
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
<summary>Evidence từng TC (6)</summary>

- TC-FR07-02: `HW02/B_FR07/evidence/TC-FR07-02_failed.png`, `HW02/B_FR07/evidence/TC-FR07-02_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-02_ui.png`
- TC-FR07-61: `HW02/B_FR07/evidence/TC-FR07-61_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-61_ui.png`
- TC-FR07-62: `HW02/B_FR07/evidence/TC-FR07-62_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-62_ui.png`
- TC-FR07-63: `HW02/B_FR07/evidence/TC-FR07-63_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-63_ui.png`
- TC-FR07-64: `HW02/B_FR07/evidence/TC-FR07-64_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-64_ui.png`
- TC-FR07-205: `HW02/B_FR07/evidence/TC-FR07-205_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-205_ui-lan1.png`
</details>

## TC liên quan

- Fail (6): TC-FR07-02, TC-FR07-61, TC-FR07-62, TC-FR07-63, TC-FR07-64, TC-FR07-205
- Blocked ghi case gốc (5): TC-FR07-03, TC-FR07-06, TC-FR07-65, TC-FR07-203, TC-FR07-206
- Nhóm dữ kiện: G1 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-06.2:** (B6 SV chốt) Trang chi tiết có ô nhập Số lượng, chỉ nhận số nguyên dương, tối thiểu là 1.
- **FR-07.1:** Giỏ hàng hiển thị danh sách sản phẩm với các cột: Sản phẩm, Đơn giá, Số lượng, Thành tiền, Thao tác.
- **FR-08.1:** (liên quan) Chỉ người dùng đã đăng nhập mới tiến hành thanh toán được — dùng để suy ra B11.
- **FR-07.5:** Có nút Tiếp tục mua sắm để quay về trang chủ.
- **FR-06.3:** (B6 SV chốt) Nút Thêm vào giỏ hàng — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).
- **FR-24.1:** (GUI, B16) Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- **B1 (giả định):** B1 (cận trên Số lượng) (SV chốt 2026-10-20): KHÔNG có cận trên. Lý do: SRS chỉ quy định ≥ 1 (FR-06). BVA phía trên dùng 1 đại diện 'giá trị lớn' hợp lệ thay cho UB/UB±1.
- **FR-07.3:** Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.
- **B21 (giả định):** B21 (phản hồi trực quan khi thêm) (SV chốt 2026-10-20): hiểu theo nghĩa rộng — lý do: FR-06.3/FR-24.1 ghi '(toast notification hoặc badge cập nhật)' như ví dụ minh hoạ, không phải danh sách đóng. Oracle: trong ≤ 2 giây sau khi bấm, có ít nhất một thay đổi nhìn thấy được gắn với lần thêm (toast; badge đổi; chữ/trạng thái nút thêm đổi; thông báo trên trang); ghi rõ loại phản hồi quan sát được vào Actual.

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G1: UI · trang chi tiết: bấm 'Thêm vào giỏ hàng' một lần với Số lượng hợp lệ → giỏ không có dòng mới; không có phản hồi nhìn thấy được trong 2 s
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-02, nguyên văn): đăng nhập cart02_1792476866046@domain.com: navbar có tên user; TRƯỚC: không có bảng (giỏ trống); ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: không có bảng (giỏ trống); URL sau khi bấm link về trang chủ=http://localhost:5173/
- Pass hộp đen ghi case gốc TC-FR07-61 (notes 6b): TC-FR07-10, 11, 12, 13, 60, 200.
- TC-FR07-04 (xếp ở nhóm badge) cũng ghi SAU = TRƯỚC sau khi thêm từ trang chi tiết; notes: EC10 chưa đánh giá được, case gốc TC-FR07-61.
- TC-FR07-205 notes (SV): lần 1 không thêm, khớp giả thuyết gray-box ProductDetail.jsx:21–31.
- Đoạn code trích nguyên văn: `frontend-web/src/pages/ProductDetail.jsx` dòng 21–31 (xem `bugs_facts.md`, G1)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
