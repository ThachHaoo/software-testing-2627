# Kiểm tái hiện 18 bug (lệnh #21 bước 1)

Claude Code chạy lại bước tái hiện SV viết trong `BUG-86…103` bằng script Playwright tạm (không commit), Chrome 157, 2026-11-17. Mỗi bug chạy trên CSDL vừa seed lại (restart backend trước từng bug), vào giỏ bằng link navbar. Không sửa chữ SV. Chỉ ghi dữ kiện.

| Bug | Tái hiện được hành vi? | Chỗ bước/giá trị lệch thực tế |
|---|---|---|
| BUG-86 | Có: ở lại `/register`, hộp lỗi "Mật khẩu quá yếu!…", API login 401 | – |
| BUG-87 | Có: không hộp lỗi, chuyển `/login`, API login `hiep.sv03@domain.com` = 200 | Bước 4 không ghi mật khẩu cụ thể; script dùng `Abcd 1234` (data TC-202) |
| BUG-88 | Có: đăng ký bị từ chối "Mật khẩu quá yếu!…"; đăng nhập lại: lỗi "Đăng nhập thất bại…", URL `/login`, token null | – |
| BUG-89 | Có: không phản hồi trong 2 s; giỏ trống, Tổng null | Bước 4 ghi URL `/cart`; gõ URL = tải lại trang → giỏ (state React) mất dù bug có hay không. Script dùng link navbar |
| BUG-90 | Có: chỉ "Giỏ hàng của bạn đang trống" + "Tiếp tục mua sắm"; img/svg trong khối = 0 | (như BUG-89, bước 2 ghi URL `/cart`) |
| BUG-91 | Có: không phản hồi trong 2 s; giỏ trống | (như BUG-89, bước 5) |
| BUG-92 | Có: badge null (link chỉ "Giỏ hàng"); AirPods SL 1, 6000000; Tổng 36000000 | (như BUG-89, bước 4) |
| BUG-93 | Có: 0 hộp thoại trong 2 s; xoá ngay, còn Keychron, Tổng 4000000 | (như BUG-89, bước 1: "truy cập trang Giỏ hàng (URL)") |
| BUG-94 | Có: lần 1 không phản hồi, giỏ trống; lần 2 giỏ vẫn trống | (như BUG-89, bước 2 và 4) |
| BUG-95 | Có: hộp thoại "Cập nhật thành công!"; mọi dòng 'Tên SP' = `Sửa UI03 1794903107473`; dòng M Giá `1000000 ₫`; GET M price "2500000", category_id 3 | Bước 3 ghi "danh mục có `category_id = 3`"; ô chọn hiện tên (`Phụ kiện`) |
| BUG-96 | Có: không thông báo; dòng `-1000 ₫`; bản ghi mới price -1000 | **Actual ghi `id = 7`; thực tế trên CSDL vừa seed: `id = 6`** (id phụ thuộc số bản ghi đã tạo trước đó) |
| BUG-97 | Có: không thông báo; dòng Giá `₫`; bản ghi mới price `""` | Actual ghi UI "`price: null`" — đó là giá trị script đọc ra, UI hiện `₫` |
| BUG-98 | Có: "Cập nhật thành công!"; GET list price -1000, GET /6 price "-1000"; mọi dòng 'Tên SP' = tên M | – (M id 6 khớp khi CSDL vừa seed) |
| BUG-99 | Có: không thông báo, không hộp thoại `1`; bản ghi được lưu (`id 6`, tên `<script>alert(1)</script>`) | – |
| BUG-100 | Có: không chặn; bản ghi mới price 100000; bảng `100000 ₫` | – |
| BUG-101 | Có: không thông báo; dòng tên 256 'x'; bản ghi mới price 1500000 | **Actual ghi `id = 7`; thực tế trên CSDL vừa seed: `id = 6`** |
| BUG-102 | Có: không thông báo; dòng `0 ₫`; bản ghi mới price 0 | – |
| BUG-103 | Có: "Cập nhật thành công!"; GET list và GET /:id name 256 'x'; mọi dòng 'Tên SP' = 256 'x' | **Tiền điều kiện, bước 5 và Actual ghi M `id = 8` (`GET /api/products/8`); thực tế trên CSDL vừa seed: M `id = 6`** |

Tổng: 18/18 tái hiện được hành vi. Lệch giá trị: BUG-96, 101, 103 (id). Lệch cách ghi bước: BUG-87 (thiếu mật khẩu cụ thể), BUG-89–94 (URL `/cart` thay vì link navbar), BUG-95 (category_id thay vì tên danh mục), BUG-97 (`price: null`).

## Lần 2 – sau khi SV sửa (commit `b264556`)

Chạy lại chỉ các bug SV vừa sửa: BUG-87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 101, 103 (cùng script, Chrome 157, CSDL seed lại trước từng bug, vào giỏ bằng link navbar).

| Bug | Tái hiện được? | Còn lệch? |
|---|---|---|
| BUG-87 | Có: mật khẩu `Abcd 1234` → không hộp lỗi, chuyển `/login`, API login 200 | Không |
| BUG-89 | Có: không phản hồi 2 s; giỏ trống | Không |
| BUG-90 | Có: chỉ chữ + link; img/svg = 0 | Không |
| BUG-91 | Có: không phản hồi 2 s; giỏ trống | Không |
| BUG-92 | Có: badge null; AirPods SL 1; Tổng 36000000 | Không |
| BUG-93 | Có: 0 hộp thoại trong 2 s; còn Keychron, Tổng 4000000 | Không |
| BUG-94 | Có: lần 1 và lần 2 giỏ trống | Không |
| BUG-95 | Có: chọn `Phụ kiện`; mọi dòng 'Tên SP' = tên mới; Giá M `1000000 ₫` | Không |
| BUG-96 | Có: bản ghi mới id 6 (bug ghi "id tiếp theo; ở lượt chính thức là 7") | Không |
| BUG-97 | Có: cột Giá `₫` | Không |
| BUG-101 | Có: bản ghi mới id 6 (bug ghi "id tiếp theo") | Không |
| BUG-103 | Có: M id 6 (bug ghi "<id của M>", lượt chính thức 8) | Không |

Kết luận dữ kiện: không còn lệch → tạo issue (lệnh #22).
