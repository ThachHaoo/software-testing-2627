# BUG-49

- **ID:** BUG-49
- **Tiêu đề:** Form Thêm sản phẩm (UI Admin) thiếu nhãn (label) và dấu sao bắt buộc (*) bên cạnh các trường nhập liệu bắt buộc (Tên sản phẩm, Giá tiền, Danh mục)
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Cốc Cốc / Chromium (chạy tay, cửa sổ ẩn danh), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', form 'Thêm sản phẩm mới' (frontend-admin)
- Ngày chạy: 2026-10-20 (chạy tay, bắt đầu 18:33, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.

- Backend node server.js đang chạy bình thường ở cổng http://localhost:3000.

- Frontend Admin frontend-admin đang chạy ở cổng http://localhost:5174.

- Đã đăng nhập trang Admin bằng tài khoản `admin@eshop.com` / `Admin123!`.

- Người dùng đã mở trang Admin tại http://localhost:5174 và chuyển sang mục "Sản phẩm" để hiển thị form "Thêm sản phẩm mới".

## Các bước tái hiện

1. Truy cập giao diện Admin tại link http://localhost:5174 và chọn mục "Sản phẩm".

2. Quan sát giao diện form "Thêm sản phẩm mới", đặc biệt chú ý quan sát phía trên hoặc bên cạnh các ô nhập liệu: Tên sản phẩm, Giá tiền, Danh mục.

3. Kiểm tra sự xuất hiện của các nhãn (label) mô tả trường và ký hiệu bắt buộc * đi kèm.

## Expected (trích SRS)

- Theo yêu cầu FR-22.1 (quy định thiết kế GUI, C12): Tất cả các trường thông tin bắt buộc phải có nhãn (label) tên trường và phải hiển thị dấu sao màu đỏ hoặc ký hiệu * ngay bên cạnh nhãn đó.

- Áp dụng cụ thể cho các trường bắt buộc của sản phẩm gồm: Tên sản phẩm (*), Giá tiền (*), Danh mục (*).

## Actual

- Trên giao diện form "Thêm sản phẩm mới", các ô nhập liệu chỉ có thuộc tính placeholder (như "Tên sản phẩm", "Giá tiền", "URL Ảnh", "Mô tả") và ô chọn Danh mục.

- Form hoàn toàn không có thẻ nhãn (label) hiển thị tên trường và hoàn toàn thiếu ký hiệu * bên cạnh để đánh dấu các trường bắt buộc nhập theo đúng chuẩn GUI.

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

- Ở Frontend (frontend-admin/src/App.jsx, dòng 490–507): Giao diện chỉ đặt trực tiếp các thẻ <input> có placeholder nằm trong grid layout mà không thiết kế thẻ <label> bọc bên ngoài hoặc đứng trước input để hiển thị ký hiệu *.

- Mặc dù đây là lỗi giao diện UI/UX ở mức độ nhẹ, việc thiếu nhãn và ký hiệu * đánh dấu trường bắt buộc vi phạm tiêu chuẩn thiết kế GUI (FR-22.1), làm giảm trải nghiệm người dùng và khiến người quản trị khó nhận biết trường nào là bắt buộc phải điền.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
