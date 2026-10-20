# BUG-40

- **ID:** BUG-40
- **Tiêu đề:** Form Thêm sản phẩm (UI Admin) cho phép nhập Giá tiền dưới dạng ký hiệu khoa học (E-notation như 1e5) mà không chặn hoặc báo lỗi
- **Severity:** Medium
- **Priority:** Medium

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', form 'Thêm sản phẩm mới' (frontend-admin)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.

- Backend node server.js đang chạy bình thường ở trang http://localhost:3000.

- Frontend Admin frontend-admin đang chạy ở trang http://localhost:5174.

- Đã đăng nhập trang Admin bằng tài khoản `admin@eshop.com` / `Admin123!`.

- Đã truy cập vào trang Admin tại http://localhost:5174 và chuyển sang mục "Sản phẩm" để mở form "Thêm sản phẩm mới"

## Các bước tái hiện

1. Mở giao diện Admin ở link http://localhost:5174 rồi bấm chọn mục "Sản phẩm".

2. Nhập Tên sản phẩm hợp lệ (ví dụ: Sản phẩm E-Notation).

3. Nhập giá tiền dạng ký hiệu khoa học vào ô "Giá tiền": 1e5 (TC-FR15-201).

4. Chọn Danh mục hợp lệ rồi bấm nút "Lưu sản phẩm".

5. Quan sát phản hồi trên giao diện (xem ô input có chặn/báo lỗi không) và kiểm tra lại danh sách sản phẩm hiển thị trên bảng UI cũng như dữ liệu chèn vào CSDL qua API GET /api/products.

## Expected (trích SRS)

- Theo quy định C24, ô "Giá tiền" trên giao diện UI phải chặn và không cho phép nhập hay gửi dữ liệu giá tiền viết dưới dạng ký hiệu khoa học (E-notation).

- Hệ thống phải hiển thị thông báo lỗi hoặc không cho submit khi phát hiện định dạng ký hiệu khoa học.

- Dữ liệu trong CSDL và trên bảng UI không được thay đổi.

## Actual

- Giao diện UI không hề chặn hay hiển thị bất kỳ thông báo lỗi nào (không alert, không bong bóng HTML5).

- Form vẫn gửi request thành công và CSDL tự động chuyển đổi 1e5 thành số 100000 để lưu vào bản ghi mới: {id: 106, name: "Sản phẩm E-Notation...", price: 100000, category_id: 2}.

- Bảng danh sách sản phẩm trên UI tự động thêm 1 dòng mới hiển thị giá 100000 ₫.

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-201_ui.png`
- TC-FR15-201: `HW02/C_FR15/evidence/TC-FR15-201_ui.png`

## TC liên quan

- Fail (1): TC-FR15-201
- Nhóm dữ kiện: G7 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **C24 (giả định SV chốt):** (cách viết giá dạng ký hiệu khoa học ở UI — TC-FR15-201) ô 'Giá tiền' trên UI chặn giá trị viết dạng ký hiệu khoa học. Dùng ở TC-FR15-201. — (SV chốt)
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-201): `giá trị ô Giá tiền trước khi lưu: "1e5"; hộp thoại: không có; ô không hợp lệ HTML5 lúc bấm: không có; thông báo mới trên trang: không có; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 106, name "Sản phẩm E-Notation 1792497408679", price 100000, category_id 2}; bảng TRƯỚC → SAU: 5 → 6 dòng; dòng mới/đổi trên bảng: [Sản phẩm E-Notation 1792497408679 | 100000 ₫]`
- Lặp lại: auto_status giống nhau ở lượt 3 và lượt 5 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `frontend-admin/src/App.jsx` dòng 500–507

  ```jsx
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

- Ở Frontend (frontend-admin/src/App.jsx, dòng 500–507): Ô nhập Giá tiền sử dụng thẻ <input type="number">. Theo chuẩn mặc định của HTML5, type="number" vẫn chấp nhận ký tự e / E để đại diện cho số mũ/ký hiệu khoa học (E-notation). Code frontend chưa xử lý chặn phím e (sự kiện onKeyDown) hoặc chưa thêm thuộc tính/regex validation để ngăn người dùng nhập dạng 1e5.

- Do không có cơ chế chặn định dạng E-notation ở UI theo đúng quy định C24, người dùng có thể vô tình hoặc cố ý nhập các chuỗi dạng 1e5, 2e6 làm sai lệch trải nghiệm nhập liệu tiêu chuẩn trên trang quản trị.

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
