# BUG-16

- **ID:** BUG-16
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/ (frontend-web)
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

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
