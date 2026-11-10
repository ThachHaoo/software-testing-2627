# Kiểm trùng issue – T1 checklist C2 (AI liệt kê, SV quyết 🔒)

Nguồn: `HW03/bugs/issues.json` lấy lại 10/11/2026 bằng `gh issue list -R tkob-team/eshop-sut --state all --limit 1000 --json number,title,author,state,createdAt,labels,body` (tài khoản ThachHaoo): **179 issue, tới #224**; snapshot cũ 158 issue tới #203 → **21 issue mới (#204–#224), đều của nphoang-itus**. henry-banana không có issue nào > #203.

Phạm vi so: 28 nhóm MỚI (G-01…G-28), 4 item trùng một phần, 14 item trùng (`failed_list.md`) với **mọi** issue (mọi tác giả, mọi trạng thái), theo tiêu đề + màn/ứng dụng + nội dung. Mức: trùng / một phần / liên quan / không. Cột mức là đề xuất của AI; SV chốt.

## 1. Tiền tố tiêu đề bạn nhóm dùng

| Tác giả | Tiền tố | Số issue | Khoảng | Bài |
|---|---|---|---|---|
| nphoang-itus | `[BUG-FRxx-xx]` | 37 | #1–#69 | HW02 |
| ThachHaoo | `[FR-xx]` | 57 | #17–#203 | HW02 (của em) |
| henry-banana | `[FRxx-xx]` | 64 | #97–#160 | HW02 |
| nphoang-itus | `[HW03-C3-xx]` | 21 | #204–#224 | **HW03** (C3 – admin) |

→ Bạn nhóm dùng `[HW03-C3-xx]` cho HW03 (ví dụ #204 · nphoang-itus · OPEN · [HW03-C3-01] Giao diện Login và Dashboard còn nhãn tiếng Anh). **Khác** `[FR-xx]` SV đã chốt → AI dừng trước bước dựng khung bug, chờ SV chọn tiền tố.

## 2. Issue mới #204–#224: phạm vi

Cả 21 issue là ứng dụng **admin** (frontend-admin), không phải web người dùng (frontend-web :5173) của C2. Câu chứng cứ (body #204): "Admin cô lập http://localhost:5175 / API http://localhost:3001.". #224: "Môi trường và baseline như các bug HW03-C3 khác (frontend-admin)".

## 3. Nhóm MỚI có issue nghi trùng

| Nhóm | Khung | Dữ kiện | Item | Issue nghi trùng (số · tác giả · trạng thái · tiêu đề) | Mức (AI đề xuất) | Chứng cứ / ghi chú |
|---|---|---|---|---|---|---|
| G-01 | `BUG-58.md` | Thứ tự Tab không theo vị trí hiển thị | CL-10, CL-12 | #221 · nphoang-itus · OPEN · [HW03-C3-18] Sidebar không điều hướng được bằng bàn phím | không | admin sidebar không Tab tới được; C2 là thứ tự Tab ở web /login, Quên MK B2 |
| G-04 | `BUG-61.md` | Trang không có <h1> | CL-02 | #206 · nphoang-itus · OPEN · [HW03-C3-03] h1 không mô tả phân vùng Dashboard hiện tại | không | admin có h1 'EShop Admin' nhưng không đổi theo tab; C2 web không có h1 |
| G-05 | `BUG-62.md` | Ô Email Quên MK B1 type=text, không chặn sai định dạng | CL-17, CL-66 | #4 · nphoang-itus · OPEN · [BUG-FR02-04] Ô email form đăng nhập Web là `type="text"`, không kiểm tra định dạng | một phần (giữ như cũ) | đã ghi: #4 phủ /login web |
| G-05 | `BUG-62.md` | Ô Email Quên MK B1 type=text, không chặn sai định dạng | CL-17, CL-66 | #209 · nphoang-itus · OPEN · [HW03-C3-06] Trường Email đăng nhập không dùng type=email | không | ô Email đăng nhập của admin |
| G-05 | `BUG-62.md` | Ô Email Quên MK B1 type=text, không chặn sai định dạng | CL-17, CL-66 | #121 · henry-banana · OPEN · [FR04-25] Disabled Web profile email uses text instead of email input type | không | ô Email (disabled) ở Hồ sơ web, không phải Đăng nhập/Quên MK |
| G-06 | `BUG-63.md` | Thiếu '*' trên nhãn bắt buộc (Quên MK B1/B2, Hồ sơ) | CL-20, CL-21 | #7 · nphoang-itus · OPEN · [BUG-FR02-07] Trường bắt buộc của form đăng nhập không có ký hiệu `*` | một phần (giữ như cũ) | đã ghi: #7 phủ /login web |
| G-06 | `BUG-63.md` | Thiếu '*' trên nhãn bắt buộc (Quên MK B1/B2, Hồ sơ) | CL-20, CL-21 | #205 · nphoang-itus · OPEN · [HW03-C3-02] Các form thiếu nhãn và dấu bắt buộc, trường Coupon chỉ có giá trị không nhãn | không | form admin (sản phẩm, danh mục, coupon) |
| G-06 | `BUG-63.md` | Thiếu '*' trên nhãn bắt buộc (Quên MK B1/B2, Hồ sơ) | CL-20, CL-21 | #195 · ThachHaoo · OPEN · [FR-15] Form Thêm sản phẩm (UI Admin) thiếu nhãn (label) và dấu sao bắt buộc (*) bên cạnh  | không | form Thêm sản phẩm admin |
| G-07 | `BUG-64.md` | Lỗi validate chỉ hiện ở hộp thoại trình duyệt | CL-23 | #210 · nphoang-itus · OPEN · [HW03-C3-07] Lỗi đăng nhập dùng alert chung, không chỉ ra trường bắt buộc hoặc đặt trên su | không | alert lỗi đăng nhập của admin; C2 là Quên MK B2, Hồ sơ web |
| G-15 | `BUG-72.md` | Hồ sơ: SĐT 9 số được lưu, thông báo không nêu quy tắc | CL-32 | #97 · henry-banana · OPEN · [FR04-01] Profile API accepts and persists a 9-digit phone | một phần (giữ như cũ) | đã ghi |
| G-15 | `BUG-72.md` | Hồ sơ: SĐT 9 số được lưu, thông báo không nêu quy tắc | CL-32 | #113 · henry-banana · OPEN · [FR04-17] Web accepts a 10-digit phone with an invalid nonzero prefix | một phần (giữ như cũ) | đã ghi |
| G-16 | `BUG-73.md` | Hồ sơ: Cập nhật + F5 quay về giá trị cũ | CL-37 | #123 · henry-banana · OPEN · [FR04-27] SPA profile re-entry shows stale data after a successful save | liên quan (giữ như cũ) | #123: vào lại Hồ sơ (SPA) thấy dữ liệu cũ sau khi lưu; C2: sau F5. SV xét có cùng hành vi không |
| G-21 | `BUG-78.md` | Nút submit không khoá / không chỉ báo khi bấm nhiều lần | CL-53, SV-06 | #222 · nphoang-itus · OPEN · [HW03-C3-19] Thiếu chỉ báo loading khi request API đang pending | không | thiếu loading khi request pending ở admin |
| G-22 | `BUG-79.md` | Lịch sử đơn: không có trạng thái đang tải | CL-63 | #222 · nphoang-itus · OPEN · [HW03-C3-19] Thiếu chỉ báo loading khi request API đang pending | không | cùng loại (thiếu loading) nhưng ở admin, không phải Lịch sử đơn web |
| G-24 | `BUG-81.md` | Lịch sử đơn: 'Hủy đơn' dùng được ở đơn đang giao | CL-59 | #219 · nphoang-itus · OPEN · [HW03-C3-16] Đơn canceled vẫn được chuyển sang delivered qua GUI | không | admin chuyển đơn canceled → delivered; C2 là người dùng huỷ đơn shipping trên web |

Nhóm không tìm thấy issue nghi trùng (quét tiêu đề cả 179 issue theo từ khoá của dữ kiện): G-02, G-03, G-08, G-09, G-10, G-11, G-12, G-13, G-14, G-17, G-18, G-19, G-20, G-23, G-25, G-26, G-27, G-28. G-11 (liên quan #30), G-13 (liên quan #17) giữ như cũ: cả hai issue là form Đăng ký, C2 là Quên MK B2.

## 4. Item trùng / một phần (failed_list) – đối chiếu lại

Mọi issue đã dùng làm căn cứ trùng vẫn **OPEN**: #1, #2, #3, #4, #5, #6, #7, #9, #97, #111, #112, #113, #122, #160, #165, #166, #167, #169, #170. Không đổi mức.

Issue mới cùng loại với item đã trùng (chỉ để SV biết, khác ứng dụng nên không đổi căn cứ trùng):

| Item | Căn cứ trùng hiện tại | Issue mới cùng loại (admin) | Mức (AI đề xuất) |
|---|---|---|---|
| CL-01 | #9 · nphoang-itus · OPEN · [BUG-FR02-09] Form đăng nhập: tiêu đề "Đăng Ký", nhãn "Username", nút "Sign In" | #204 · nphoang-itus · OPEN · [HW03-C3-01] Giao diện Login và Dashboard còn nhãn tiếng Anh | không (khác ứng dụng) |
| CL-04 | #160 · henry-banana · OPEN · [FR20-08] Mobile positive Add to Cart action is green instead of blue | #207 · nphoang-itus · OPEN · [HW03-C3-04] Nút lưu sản phẩm và tạo coupon sai màu hành động tích cực theo FR-21 | không (khác ứng dụng) |
| CL-08 | #170 · ThachHaoo · OPEN · [FR-07] Giá sản phẩm ở thẻ sản phẩm trang chủ hiển thị đơn vị tiền tệ là 'VND' thay vì '₫' | #208 · nphoang-itus · OPEN · [HW03-C3-05] Giá sản phẩm không có phân cách hàng nghìn | không (khác ứng dụng) |
| CL-62 | #167 · ThachHaoo · OPEN · [FR-07] Trang giỏ hàng trống chỉ có thông báo chữ, thiếu hoàn toàn hình minh họa/icon theo | #216 · nphoang-itus · OPEN · [HW03-C3-13] Đơn hàng trống chỉ có header bảng, thiếu empty state | không (khác ứng dụng) |
| CL-22 | #6 · nphoang-itus · OPEN · [BUG-FR02-06] Thông báo lỗi đăng nhập nằm dưới nút submit | #210 · nphoang-itus · OPEN · [HW03-C3-07] Lỗi đăng nhập dùng alert chung, không chỉ ra trường bắt buộc hoặc đặt trên su | không (khác ứng dụng) |

## 5. Kết luận cho SV quyết

- G nào đổi mức trùng so với `failed_list.md`: **không** (AI đề xuất). 28 nhóm vẫn MỚI, 4 một phần, 14 trùng.
- Chờ SV: tiền tố tiêu đề GitHub (`[FR-xx]` như HW02 của em, hay theo bạn nhóm `[HW03-C2-xx]`).
