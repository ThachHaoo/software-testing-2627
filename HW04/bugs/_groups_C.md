# C_FR15 – dữ kiện nhóm Fail (để SV quyết G → BUG)

AI tổng hợp dữ kiện từ `HW04/C_FR15/bug_groups.md` (lượt chính thức chrome 15:11, edge 15:12, firefox 15:13 – spec 2e9e454), `HW02/bugs/BUG-xx.md` (mục Yêu cầu, đoạn code, link Issue) và mã SUT `../eshop-sut` @ de0f48f. **Không** đề xuất gộp/tách, **không** viết mô tả bug — SV quyết. Mọi G đều Fail ở cả chrome/edge/firefox. File SUT: admin = `frontend-admin/src/App.jsx`, backend = `backend/server.js`.

| G | TC | Triệu chứng (assertion lỗi) | Vị trí code SUT (theo HW02) | Yêu cầu bị vi phạm (theo HW02) | Issue HW02 liên quan |
|---|---|---|---|---|---|
| C-G1 | TC-FR15-03 (Sửa) | dòng của M: 'Giá' = 1000000 thay vì 2500000 (toBe); mọi dòng khác SAU_UI ≠ TRƯỚC_UI: 'Tên SP' của mọi dòng = tên mới (toEqual) | `App.jsx:105-116` | FR-15.5; FR-15.1 (Xem) | BUG-45 · #191 |
| C-G2 | TC-FR15-10 (Thêm, giá -1000) | không có thông báo lỗi (toBe false); bảng có thêm dòng giá -1000 (toEqual); GET SAU có thêm bản ghi (toEqual) | `App.jsx:500-507`; `server.js:167-177` | FR-15.3; C7, C16 | BUG-36 · #182 |
| C-G3 | TC-FR15-11 (Thêm, giá rỗng) | không có thông báo lỗi; bảng có thêm dòng giá rỗng (`₫`); GET SAU có thêm bản ghi | `App.jsx:500-507`; `server.js:167-177` | FR-15.3; C7, C16 | BUG-36 · #182 |
| C-G4 | TC-FR15-15 (Sửa, giá -1000) | bảng SAU_UI ≠ TRƯỚC_UI ('Tên SP' mọi dòng = tên M); M_SAU price "-1000" (toEqual); GET SAU price -1000 (toEqual) | `App.jsx:500-507`; `server.js:179-189` | FR-15.3; C7, C16 | BUG-38 · #184 |
| C-G5 | TC-FR15-200 (Thêm, tên `<script>alert(1)</script>`) | không có thông báo lỗi (toBe false); không có hộp thoại '1' (assertion XSS đạt) | `App.jsx:491-499`; `server.js:167-177` | C21; C7, C16 | BUG-39 · #185 |
| C-G6 | TC-FR15-201 (Thêm, giá `1e5`) | form chặn: GET SAU có thêm bản ghi (toEqual) | `App.jsx:500-507` | C24 | BUG-40 · #186 |
| C-G7 | TC-FR15-66 (Thêm, tên 256 ký tự) | không có thông báo lỗi; bảng có thêm dòng tên 256 ký tự; GET SAU có thêm bản ghi | `App.jsx:491-499`; `server.js:167-177` | FR-15.2; C7, C16 | BUG-35 · #181 |
| C-G8 | TC-FR15-67 (Thêm, giá 0) | không có thông báo lỗi; bảng có thêm dòng giá 0; GET SAU có thêm bản ghi | `App.jsx:500-507`; `server.js:167-177` | FR-15.3; C7, C16 | BUG-36 · #182 |
| C-G9 | TC-FR15-78 (Sửa, tên 256 ký tự) | bảng SAU_UI ≠ TRƯỚC_UI ('Tên SP' mọi dòng = tên 256 ký tự); M_SAU name 256 ký tự (toEqual); GET SAU khác TRƯỚC (toEqual) | `App.jsx:105-116`; `server.js:179-189` | FR-15.2; C7, C16 | BUG-37 · #183 |

## G nào cùng vị trí code

| Vị trí code SUT | G |
|---|---|
| `App.jsx:105-116` | C-G1, C-G9 |
| `App.jsx:491-499` (ô Tên) | C-G5, C-G7 |
| `App.jsx:500-507` (ô Giá tiền) | C-G2, C-G3, C-G4, C-G6, C-G8 |
| `server.js:167-177` (POST /api/products) | C-G2, C-G3, C-G5, C-G7, C-G8 |
| `server.js:179-189` (PUT /api/products/:id) | C-G4, C-G9 |

## Ghi chú dữ kiện

- C-G2, C-G3, C-G8 cùng issue HW02 BUG-36 (#182). C-G4 và C-G9 cũng có 'Tên SP' mọi dòng đổi trên bảng, giống triệu chứng của C-G1 (BUG-45).
- Annotation `price dạng chuỗi (BUG-48)` (`server.js:159-165`, dòng 162; issue #194): TC-05 (Pass), TC-15, TC-78 — không phải assertion lỗi, không tạo G.
- Annotation `oracle thông báo yếu`: TC-15, TC-78 (chỉ có hộp thoại "Cập nhật thành công!", vẫn đếm là có thông báo theo H4, R3=a).
- Mọi G đã có issue HW02 (#181–#186, #191) → SV quyết: comment vào issue cũ hay tạo issue mới cho HW04.
- Chi tiết assertion, ảnh: `HW04/C_FR15/bug_groups.md`, `HW04/C_FR15/evidence/`.
