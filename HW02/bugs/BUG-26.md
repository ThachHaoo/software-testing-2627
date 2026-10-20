# BUG-26

- **ID:** BUG-26
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173/cart (frontend-web)
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

- Ảnh tiêu biểu: `TC-FR07-95_ui.png`
- TC-FR07-95: `HW02/B_FR07/evidence/TC-FR07-95_ui.png`

## TC liên quan

- Fail (1): TC-FR07-95
- Nhóm dữ kiện: G12 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **FR-07.1:** Giỏ hàng hiển thị danh sách sản phẩm với các cột: Sản phẩm, Đơn giá, Số lượng, Thành tiền, Thao tác.
- **B12 (giả định SV chốt):** (nhãn chính xác) (SV chốt 2026-10-20): các cụm in đậm trong FR-07 là nhãn — 'Sản phẩm', 'Đơn giá', 'Số lượng', 'Thành tiền', 'Thao tác', 'Xóa sản phẩm', 'Tiếp tục mua sắm', 'Tổng cộng'. So khớp đúng chữ, PHÂN BIỆT hoa/thường, chuẩn hoá Unicode NFC trước khi so; coi hai cách đặt dấu 'óa'/'oá' là như nhau (vd 'Xóa' = 'Xoá'). Chỉ kiểm ở TC-FR07-95…98; case chức năng định vị nút/link không dựa vào chữ.
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-95): `nhãn đọc được=["Sản phẩm","Giá","Số lượng","Thành tiền","Thao tác"]`
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Cart.jsx` dòng 34–40

  ```jsx
    34            <tr className="border-b">
    35              <th className="py-2">Sản phẩm</th>
    36              <th className="py-2">Giá</th>
    37              <th className="py-2">Số lượng</th>
    38              <th className="py-2">Thành tiền</th>
    39              <th className="py-2">Thao tác</th>
    40            </tr>
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
