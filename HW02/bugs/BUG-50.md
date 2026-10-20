# BUG-50

- **ID:** BUG-50
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: `<SV điền>` (chạy tay, cửa sổ ẩn danh), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', bảng sản phẩm (frontend-admin)
- Ngày chạy: 2026-10-20 (chạy tay, bắt đầu 18:36, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-92_manual.png`
- TC-FR15-92: `HW02/C_FR15/evidence/TC-FR15-92_manual.png`

## TC liên quan

- Fail (1): TC-FR15-92
- Nhóm dữ kiện: G16 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-21.3:** (GUI, C12) Luôn dùng ký hiệu ₫ với định dạng phân cách hàng nghìn — áp cho cột 'Giá' của bảng sản phẩm.
- Đạt trong cùng case: Có ký hiệu ₫
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-92): `Manual – 20/10/2026 18:36. Ô 'Giá' dòng 'iPhone 15 Pro Max' hiển thị '30000000 ₫' — có ₫, không có ký tự phân cách hàng nghìn.`
- Lặp lại: chỉ có kết quả chạy tay (ảnh SV), không có lượt tự động.
- Đoạn code trích nguyên văn: `frontend-admin/src/App.jsx` dòng 590

  ```jsx
   590                      <td className="p-3">{p.price} ₫</td>
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
