# BUG-21

- **ID:** BUG-21
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart, giỏ trống (frontend-web)
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

- Ảnh tiêu biểu: `TC-FR07-01_ui.png`
- TC-FR07-01: `HW02/B_FR07/evidence/TC-FR07-01_failed.png`, `HW02/B_FR07/evidence/TC-FR07-01_ui.png`

## TC liên quan

- Fail (1): TC-FR07-01
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.7:** Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng. — vi phạm ở: thiếu hình minh hoạ; có thông báo 'Giỏ hàng của bạn đang trống'
- **FR-24.3:** Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện (bổ sung FR-07.7). — vi phạm ở: thiếu icon/hình minh hoạ
- Đạt trong cùng case: FR-07.5 (link về trang chủ → URL '/'), FR-23.2 (badge ẩn khi giỏ trống, chấp nhận theo B22)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-01): `TRƯỚC: không có bảng (giỏ trống); trạng thái trống: bảng=không, ảnh/icon=không, chữ="Giỏ hàng của bạn đang trốngTiếp tục mua sắm"; URL sau thao tác=http://localhost:5173/`
- Cùng case: dòng chữ 'Giỏ hàng của bạn đang trống' có; link về trang chủ → URL '/' đạt.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 20–27

  ```jsx
    20    if (cart.length === 0) {
    21      return (
    22        <div className="text-center mt-10">
    23          <h2 className="text-2xl mb-4">Giỏ hàng của bạn đang trống</h2>
    24          <Link to="/" className="text-blue-600 hover:underline">Tiếp tục mua sắm</Link>
    25        </div>
    26      );
    27    }
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
