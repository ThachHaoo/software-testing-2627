# BUG-15

- **ID:** BUG-15
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/product/:id → /cart (frontend-web)
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

- Ảnh tiêu biểu: `TC-FR07-02_ui.png`
- TC-FR07-02: `HW02/B_FR07/evidence/TC-FR07-02_failed.png`, `HW02/B_FR07/evidence/TC-FR07-02_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-02_ui.png`
- TC-FR07-61: `HW02/B_FR07/evidence/TC-FR07-61_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-61_ui.png`
- TC-FR07-62: `HW02/B_FR07/evidence/TC-FR07-62_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-62_ui.png`
- TC-FR07-63: `HW02/B_FR07/evidence/TC-FR07-63_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-63_ui.png`
- TC-FR07-64: `HW02/B_FR07/evidence/TC-FR07-64_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-64_ui.png`
- TC-FR07-205: `HW02/B_FR07/evidence/TC-FR07-205_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-205_ui-lan1.png`

## TC liên quan

- Fail (6): TC-FR07-02, TC-FR07-61, TC-FR07-62, TC-FR07-63, TC-FR07-64, TC-FR07-205
- Blocked ghi case gốc (5): TC-FR07-03, TC-FR07-06, TC-FR07-65, TC-FR07-203, TC-FR07-206
- Pass hộp đen ghi case gốc (6): TC-FR07-10, TC-FR07-11, TC-FR07-12, TC-FR07-13, TC-FR07-60, TC-FR07-200
- Nhóm dữ kiện: G1 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **Chức năng thêm của nút 'Thêm vào giỏ hàng' (ngầm định):** ngầm định trong FR-06, không có câu SRS riêng
- **FR-06.3:** (B6 SV chốt) Nút Thêm vào giỏ hàng — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).
- **FR-24.1:** (GUI, B16) Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- **B21 (giả định SV chốt):** (phản hồi trực quan khi thêm) (SV chốt 2026-10-20): hiểu theo nghĩa rộng — lý do: FR-06.3/FR-24.1 ghi '(toast notification hoặc badge cập nhật)' như ví dụ minh hoạ, không phải danh sách đóng. Oracle: trong ≤ 2 giây sau khi bấm, có ít nhất một thay đổi nhìn thấy được gắn với lần thêm (toast; badge đổi; chữ/trạng thái nút thêm đổi; thông báo trên trang); ghi rõ loại phản hồi quan sát được vào Actual.
- **B1 (giả định SV chốt):** (cận trên Số lượng) (SV chốt 2026-10-20): KHÔNG có cận trên. Lý do: SRS chỉ quy định ≥ 1 (FR-06). BVA phía trên dùng 1 đại diện 'giá trị lớn' hợp lệ thay cho UB/UB±1. — vi phạm ở: TC-64: 1000 không được thêm
- Đạt trong cùng case: FR-07.5 (TC-02: link về trang chủ → URL '/')
- Chưa đánh giá được: FR-06.2 (Số lượng hợp lệ không được thêm nên chưa xét được ô nhận/chặn giá trị), FR-07.1 (không có bảng để xét cột), FR-07.3 (TC-205: lần 1 không thêm nên chưa xét cộng dồn), FR-08.1 (không liên quan tới quan sát)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-02): `đăng nhập cart02_1792476866046@domain.com: navbar có tên user; TRƯỚC: không có bảng (giỏ trống); ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: không có bảng (giỏ trống); URL sau khi bấm link về trang chủ=http://localhost:5173/`
- Các case Blocked ghi case gốc: TC-FR07-61 (A20).
- Các case Pass hộp đen ghi case gốc: TC-FR07-61 (notes 6b).
- Pass hộp đen ghi case gốc TC-FR07-61 (notes 6b): TC-FR07-10, 11, 12, 13, 60, 200.
- TC-FR07-04 (xếp ở nhóm badge) cũng ghi SAU = TRƯỚC sau khi thêm từ trang chi tiết; notes: EC10 chưa đánh giá được, case gốc TC-FR07-61.
- TC-FR07-205 notes (SV): lần 1 không thêm, khớp giả thuyết gray-box ProductDetail.jsx:21–31.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/ProductDetail.jsx` dòng 21–31

  ```jsx
    21    const handleAddToCart = () => {
    22      if (clickCount === 0) {
    23        setClickCount(1);
    24        return; // Không làm gì cả ở lần đầu tiên
    25      }
    26  
    27      addToCart(product, parseInt(quantity));
    28      setAdded(true);
    29      setClickCount(0); // Reset lại
    30      setTimeout(() => setAdded(false), 2000);
    31    };
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
