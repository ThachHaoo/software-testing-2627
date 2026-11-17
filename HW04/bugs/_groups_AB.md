# A_FR01 + B_FR07 – dữ kiện nhóm Fail (để SV quyết G → BUG)

AI tổng hợp dữ kiện từ `HW04/A_FR01/bug_groups.md`, `HW04/B_FR07/bug_groups.md` (lượt chính thức), `HW02/bugs/BUG-xx.md` (mục Yêu cầu, đoạn code, link Issue) và mã SUT `../eshop-sut` @ de0f48f. **Không** đề xuất gộp/tách, **không** viết mô tả bug — SV quyết. Mọi G đều Fail ở cả chrome/edge/firefox.

## A_FR01 (lượt chính thức: chrome 13:47, edge 13:49, firefox 13:52 – spec 9f26855)

| G | TC | Triệu chứng (assertion lỗi) | Vị trí code SUT | Yêu cầu bị vi phạm (theo HW02) | Issue HW02 liên quan |
|---|---|---|---|---|---|
| A-G1 | TC-FR01-01, 02, 64, 68, 74, 77 | URL sau khi bấm Đăng Ký vẫn `/register` (toHaveURL); có thông báo lỗi (toHaveCount = 1); không có user mới (toEqual `[]`) | `frontend-web/src/pages/Register.jsx:15` regex mật khẩu `(?=.*\s)[A-Za-z\d\s]{8,}`; `Register.jsx:17-19` không khớp → setError, return trước POST | FR-01.10; chấp nhận mật khẩu hợp lệ theo FR-01.5–01.8 (ngầm định) | BUG-01 · #17 |
| A-G2 | TC-FR01-202 | không có hộp lỗi đỏ (toBeVisible), không có nội dung lỗi (toHaveText/toContainText "mật khẩu", "ký tự đặc biệt"); có user mới (toEqual) | `Register.jsx:15` (cùng regex) | FR-01.8 (ký tự đặc biệt thuộc @$!%*?&); A5 (HW02): khoảng trắng không phải ký tự đặc biệt | BUG-02 · #18 |
| A-G3 | TC-FR01-211 | không có user mới (toEqual `[]`); có thông báo lỗi; đăng nhập lại không về trang chủ (URL `/login`), không có token localStorage | `Register.jsx:15`, `Register.jsx:17-19` (như A-G1) | FR-01.10; FR-01.5–01.8 (ngầm định) | BUG-01 · #17 |

## B_FR07 (lượt chính thức: chrome 14:11, edge 14:12, firefox 14:13 – spec c8a2ce9)

| G | TC | Triệu chứng (assertion lỗi) | Vị trí code SUT | Yêu cầu bị vi phạm (theo HW02) | Issue HW02 liên quan |
|---|---|---|---|---|---|
| B-G1 | TC-FR07-61, 62, 63, 64 | sau 1 lần bấm 'Thêm vào giỏ hàng' ở trang chi tiết: giỏ 0 dòng (toBe), dòng giỏ `[]` (toEqual), Tổng null | `frontend-web/src/pages/ProductDetail.jsx:21-31` `handleAddToCart`: `clickCount === 0` → `setClickCount(1); return;` (lần bấm đầu không thêm) | chức năng thêm của nút (ngầm định FR-06); FR-06.3 / FR-24.1 + B21 | BUG-15 · #161 |
| B-G2 | TC-FR07-01 | giỏ trống: không có img/svg minh hoạ trong khối chữ giỏ trống (not.toHaveCount 0) | `frontend-web/src/pages/Cart.jsx:20-27` (chỉ `<h2>` + `<Link>`) | FR-07.7; FR-24.3 | BUG-21 · #167 |
| B-G3 | TC-FR07-02 | không có phản hồi ≤ 2 s sau khi bấm thêm (B21, not.toBeNull); giỏ 0 dòng, dòng `[]`, Tổng null | `ProductDetail.jsx:21-31` (như B-G1) | chức năng thêm (ngầm định FR-06); FR-06.3 / FR-24.1 + B21 | BUG-15 · #161 |
| B-G4 | TC-FR07-04 | badge SAU null (B9, toBe); Tổng SAU 36000000; dòng giỏ: Số lượng "1", Thành tiền 6000000 (toEqual lệch) | badge: `frontend-web/src/App.jsx:23` (`<Link to="/cart">Giỏ hàng</Link>` không có số); Số lượng/Tổng: `ProductDetail.jsx:21-31` | FR-23.2 + B9/B16 (badge); FR-07.3 (HW02 ghi "chưa đánh giá được" do thêm từ chi tiết không vào giỏ) | BUG-20 · #166 (HW02 gắn TC-04); BUG-15 · #161 (cùng code thêm từ chi tiết) |
| B-G5 | TC-FR07-08 | không hiện dialog xác nhận sau khi bấm Xóa (Received 0) | `frontend-web/src/pages/Cart.jsx:49-55` (`onClick={() => removeFromCart(index)}`); `frontend-web/src/context/CartContext.jsx:12-16` | FR-07.4; FR-24.2 | BUG-19 · #165 |
| B-G6 | TC-FR07-205 | không có phản hồi ≤ 2 s (B21); lần 1 và lần 2: không có dòng id 5 (toHaveCount 0), Số lượng `[]`; lần 2: số dòng 0 | `ProductDetail.jsx:21-31` (như B-G1) | chức năng thêm (ngầm định FR-06); FR-06.3 / FR-24.1 + B21; FR-07.3 | BUG-15 · #161 |

## G nào cùng vị trí code

| Vị trí code SUT | G |
|---|---|
| `Register.jsx:15` (regex mật khẩu) | A-G1, A-G2, A-G3 |
| `Register.jsx:17-19` | A-G1, A-G3 |
| `ProductDetail.jsx:21-31` (`handleAddToCart`, `clickCount`) | B-G1, B-G3, B-G4 (phần Số lượng/Tổng), B-G6 |
| `App.jsx:23` (link Giỏ hàng, không badge) | B-G4 (phần badge) |
| `Cart.jsx:20-27` (giỏ trống) | B-G2 |
| `Cart.jsx:49-55` + `CartContext.jsx:12-16` (xoá) | B-G5 |

## Ghi chú dữ kiện

- Issue HW02 đã có cho mọi G (#17, #18, #161, #165, #166, #167) → SV quyết: comment vào issue cũ hay tạo issue mới cho HW04.
- B-G4 có 2 vị trí code (badge `App.jsx:23`, thêm từ chi tiết `ProductDetail.jsx`); HW02 gắn TC-04 với BUG-20.
- Chi tiết assertion, ảnh `evidence/`: `HW04/A_FR01/bug_groups.md`, `HW04/B_FR07/bug_groups.md`.
