# BUG-49

- **ID:** BUG-49
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: `<SV điền>` (chạy tay, cửa sổ ẩn danh), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', form 'Thêm sản phẩm mới' (frontend-admin)
- Ngày chạy: 2026-10-20 (chạy tay, bắt đầu 18:33, Asia/Saigon)
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

- Ảnh tiêu biểu: `TC-FR15-90_manual.png`
- TC-FR15-90: `HW02/C_FR15/evidence/TC-FR15-90_manual.png`

## TC liên quan

- Fail (1): TC-FR15-90
- Nhóm dữ kiện: G15 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-22.1:** (GUI, C12) Tất cả trường bắt buộc phải có ký hiệu * bên cạnh nhãn — áp cho Tên, Giá, Danh mục.
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-90): `Manual – 20/10/2026 18:33. Form 'Thêm sản phẩm mới' chỉ có placeholder 'Tên sản phẩm', 'Giá tiền', 'URL Ảnh', 'Mô tả' và ô chọn danh mục; không có nhãn, không có ký hiệu '*'.`
- Lặp lại: chỉ có kết quả chạy tay (ảnh SV), không có lượt tự động.
- Đoạn code trích nguyên văn: `frontend-admin/src/App.jsx` dòng 490–507

  ```jsx
   490                <div className="grid grid-cols-2 gap-4">
   491                  <input
   492                    placeholder="Tên sản phẩm"
   493                    className="border p-2 rounded"
   494                    value={productForm.name}
   495                    onChange={(e) =>
   496                      setProductForm({ ...productForm, name: e.target.value })
   497                    }
   498                    required
   499                  />
   500                  <input
   501                    placeholder="Giá tiền"
   502                    type="number"
   503                    className="border p-2 rounded"
   504                    value={productForm.price}
   505                    onChange={(e) =>
   506                      setProductForm({ ...productForm, price: e.target.value })
   507                    }
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
