# BUG-50

- **ID:** BUG-50
- **Tiêu đề:** Bảng danh sách sản phẩm (UI Admin) hiển thị Cột 'Giá' không có dấu phân cách hàng nghìn (hiển thị 30000000 ₫ thay vì 30.000.000 ₫)
- **Severity:** Low
- **Priority:** Low

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Trình duyệt: Cốc Cốc / Chromium (chạy tay, cửa sổ ẩn danh), locale en-US
- Admin http://localhost:5174 — mục 'Sản phẩm', bảng sản phẩm (frontend-admin)
- Ngày chạy: 2026-10-20 (chạy tay, bắt đầu 18:36, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

- CSDL đã khởi tạo lại dữ liệu gốc ban đầu thành công.

- Backend node server.js đang chạy bình thường ở cổng http://localhost:3000.

- Frontend Admin frontend-admin đang chạy ở cổng http://localhost:5174.

- Đã đăng nhập trang Admin bằng tài khoản `admin@eshop.com` / `Admin123!`.

- Người dùng đã mở trang Admin tại http://localhost:5174 và chọn mục "Sản phẩm" để hiển thị bảng danh sách sản phẩm.

## Các bước tái hiện

1. Truy cập giao diện Admin tại link http://localhost:5174 và chọn mục "Sản phẩm".

2. Quan sát cột "Giá" trên bảng danh sách sản phẩm (ví dụ dòng sản phẩm iPhone 15 Pro Max).

3. Kiểm tra định dạng hiển thị giá tiền xem có dấu phân cách hàng nghìn (dấu chấm hoặc dấu phẩy) hay không.

## Expected (trích SRS)

Theo yêu cầu FR-21.3 (quy định định dạng hiển thị GUI, C12): Cột giá tiền phải luôn có ký hiệu ₫ đi kèm định dạng phân cách hàng nghìn rõ ràng (ví dụ: 30.000.000 ₫ hoặc 30,000,000 ₫).

## Actual

- Cột "Giá" trên bảng sản phẩm hiển thị ký hiệu ₫ ở cuối nhưng chuỗi số giá tiền hoàn toàn không có dấu phân cách hàng nghìn.

- Ví dụ: Dòng sản phẩm iPhone 15 Pro Max hiển thị nguyên văn là 30000000 ₫ thay vì có dấu định dạng phân cách.

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

- Ở Frontend (frontend-admin/src/App.jsx, dòng 590): Giá tiền được render trực tiếp dạng chuỗi/số thô từ API mà không qua hàm định dạng số tiền: <td className="p-3">{p.price} ₫</td>.

- Code frontend thiếu bước format giá tiền (chưa dùng toLocaleString() hoặc hàm định dạng tiền tệ chuyên dụng), khiến chuỗi số giá tiền lớn bị dính liền nhau, vi phạm quy định thiết kế GUI FR-21.3 và làm người dùng khó đọc/dễ nhìn nhầm số lượng chữ số 0 của giá sản phẩm.

## Link GitHub Issue

https://github.com/tkob-team/eshop-sut/issues/196

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
