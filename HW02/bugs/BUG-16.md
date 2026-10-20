# BUG-16

- **ID:** BUG-16
- **Tiêu đề:** Trang chủ: Bấm 'Thêm vào giỏ' trên thẻ sản phẩm không có bất kỳ phản hồi trực quan nào trong vòng 2 giây
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/ (frontend-web)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

- Hệ thống frontend web và backend server đang chạy bình thường.
- Người dùng đang ở trang chủ `/` (chưa đăng nhập hoặc đã đăng nhập).

## Các bước tái hiện

1. Truy cập vào trang chủ `http://localhost:5173/`.
2. Tìm thẻ sản phẩm bất kỳ (ví dụ: `Tai nghe AirPods Pro 2`).
3. Bấm nút "Thêm vào giỏ" nằm trên thẻ sản phẩm đúng 1 lần.
4. Quan sát các phản hồi trên giao diện (toast, nút, badge giỏ hàng) trong vòng 2 giây.

## Expected (trích SRS)

Theo yêu cầu FR-24.1 (kèm giả định B21): Ngay sau khi người dùng bấm nút "Thêm vào giỏ" ở trang chủ, giao diện phải xuất hiện ít nhất một phản hồi trực quan trong vòng 2 giây (chẳng hạn như bật thông báo toast, thay đổi chữ/trạng thái nút, hoặc nhảy badge đếm số lượng trên link "Giỏ hàng" ở navbar).

## Actual

Giao diện hoàn toàn "im lặng". Nút bấm không thay đổi trạng thái, không xuất hiện thông báo toast, và link "Giỏ hàng" trên navbar cũng không hề xuất hiện badge cập nhật số lượng trong suốt 2 giây sau khi bấm (dù sản phẩm thực tế có được thêm vào giỏ khi mở `/cart`).

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-99_feedback.png`
- TC-FR07-99: `HW02/B_FR07/evidence/TC-FR07-99_failed.png`, `HW02/B_FR07/evidence/TC-FR07-99_feedback.png`

## TC liên quan

- Fail (1): TC-FR07-99
- Nhóm dữ kiện: G2 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-24.1:** (GUI, B16) Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
- **B21 (giả định SV chốt):** (phản hồi trực quan khi thêm) (SV chốt 2026-10-20): hiểu theo nghĩa rộng — lý do: FR-06.3/FR-24.1 ghi '(toast notification hoặc badge cập nhật)' như ví dụ minh hoạ, không phải danh sách đóng. Oracle: trong ≤ 2 giây sau khi bấm, có ít nhất một thay đổi nhìn thấy được gắn với lần thêm (toast; badge đổi; chữ/trạng thái nút thêm đổi; thông báo trên trang); ghi rõ loại phản hồi quan sát được vào Actual.
- Đạt trong cùng case: —
- Chưa đánh giá được: —
- Không áp dụng: FR-06.3 (nút ở trang chủ thuộc FR-24.1)

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-99): `không có phản hồi nhìn thấy được trong 2 s`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Home.jsx` dòng 97–102

  ```jsx
    97                  <button
    98                    onClick={() => addToCart({ ...p, quantity: 1 }, 1)}
    99                    className="flex-1 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 text-sm"
   100                  >
   101                    Thêm vào giỏ
   102                  </button>
  ```

- Đoạn code trích nguyên văn: `frontend-web/src/App.jsx` dòng 23

  ```jsx
    23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
  ```

### Nhận định

- Trong Home.jsx (dòng 98), sự kiện onClick của nút chỉ gọi đơn thuần hàm addToCart({ ...p, quantity: 1 }, 1) để cập nhật state giỏ hàng mà không hề gọi hàm hiển thị toast hay xử lý đổi trạng thái UI local nào cho nút.

- Ở phía Navbar (App.jsx dòng 23), phần tử <Link to="/cart">Giỏ hàng</Link> được viết dạng text tĩnh hoàn toàn, không hề bọc hay tính toán badge số lượng sản phẩm từ CartContext.

- Việc thiếu cả hiệu ứng phản hồi nút/toast lẫn badge trên Navbar khiến người dùng ở trang chủ không biết được thao tác bấm "Thêm vào giỏ" đã thành công hay chưa nếu không chủ động click sang trang /cart để kiểm tra.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/162

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
