# BUG-25

- **ID:** BUG-25
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/ (frontend-web); đối chiếu /product/4, /cart
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

- Ảnh tiêu biểu: `TC-FR07-94_ui.png`
- TC-FR07-94: `HW02/B_FR07/evidence/TC-FR07-94_ui.png`

## TC liên quan

- Fail (1): TC-FR07-94
- Nhóm dữ kiện: G11 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-24.4:** (GUI, B16) Tất cả ảnh sản phẩm phải có thuộc tính alt mô tả nội dung (không rỗng). — vi phạm ở: trang chủ: 5/5 alt rỗng
- Đạt trong cùng case: FR-24.4 ở trang chi tiết (alt = tên sản phẩm)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-94): `alt trang chủ=["","","","",""]; alt trang chi tiết=["Tai nghe AirPods Pro 2"]; trang giỏ không có ảnh sản phẩm (notes, không tính Fail); [kiểm tay] alt "mô tả nội dung ảnh": SV đối chiếu chữ alt với ảnh`
- Cùng case: trang chi tiết alt = tên sản phẩm (đạt); trang giỏ không có ảnh.
- Notes SV: evidence kiểm tay cần chụp lại trong cửa sổ ẩn danh không tiện ích.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Home.jsx` dòng 80–84

  ```jsx
    80                <img
    81                  src={p.imageUrl}
    82                  alt=""
    83                  className="w-full h-48 object-cover mb-4 rounded"
    84                />
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
