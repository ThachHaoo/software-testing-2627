# C_FR15 – bảng assertion (bước 3, AI sinh)

Spec: `HW04/tests/C_FR15.spec.ts`; oracle đọc từ `expected` của `HW04/data/C_FR15.json` bằng `HW04/tests/oracles/c_fr15.oracle.ts` (không xác định được loại kết quả → ném lỗi; cụm dư → annotation `oracle không tự động` — hiện 0 cụm ở 15 TC). Mọi assertion là `expect.soft`.

## Kiểu assertion

| # | Kiểu | Matcher | Dùng cho | TC |
|---|---|---|---|---|
| 1 | Trạng thái UI | `toBeVisible` | form có nút 'Lưu sản phẩm' sau khi vào tab; dòng mới hiển thị trên bảng | mọi TC; 01, 65, 68 |
| 2 | Nội dung | `toHaveText` | ô 'Tên SP' của dòng M sau khi sửa | 03, 77 |
| 3 | Giá trị ô | `toHaveValue` | ô Tên/Mô tả/URL giữ đúng chuỗi đã nhập trước khi bấm Lưu (ô Giá chỉ ghi annotation) | mọi TC Thêm/Sửa có nhập |
| 4 | Đếm | `toHaveCount` | đúng 1 dòng 'Tên SP' = …; số dòng không đổi; không còn dòng M; số dòng SAU_UI = TRƯỚC_UI − 1 | 01, 65, 68; 03; 05 |
| 5 | Oracle dữ liệu GET trước/sau | `toEqual` | GET /api/products SAU = TRƯỚC (sắp theo id); M_SAU = M_TRƯỚC; bản ghi mới / M_SAU {name, price, category_id} (so giá trị số); trường giữ nguyên = M_TRƯỚC; bảng SAU_UI = TRƯỚC_UI; mọi dòng khác = TRƯỚC_UI; không có hộp thoại XSS | 07, 10, 11, 15, 66, 67, 78, 201; 15, 78; 01, 65, 68; 03, 77; 200 |
| 6 | Giá trị | `toBe` / `not.toContain` | số bản ghi SAU = TRƯỚC ± n; 'Giá' dòng mới/dòng M; có/không có thông báo lỗi; price `sameNumber` như HW02; id M không còn | 01, 03, 05, 65, 68, 77; 07…78, 200 |

## Quy ước

- So giá như HW02 (`HW02/tests/C_FR15/lib.ts` dòng 147 `sameNumber`): `Number(actual) === expected`, null/"" không khớp; `toEqual` dùng giá trị đã chuẩn hoá cùng nghĩa. Trường giữ nguyên so bằng `String()` như HW02 (dòng 141–143 spec HW02).
- GET /api/products/:id với id chẵn trả `price` dạng chuỗi (BUG-48) → annotation `price dạng chuỗi (BUG-48)` (M_TRƯỚC/M_SAU); không làm Fail vì so giá trị số.
- "Có thông báo" = ô không hợp lệ HTML5 (sự kiện `invalid` trong lần bấm) hoặc hộp thoại hoặc thông báo mới trên trang (selector ở `assumptions.page_message_selector`) — không phân loại nội dung (HW02 H4). Chỉ có hộp thoại → annotation `oracle thông báo yếu` kèm nội dung để SV xét.
- Bấm 'Lưu sản phẩm' / 'Xóa' đúng 1 lần. Chờ trạng thái rõ: phản hồi POST/PUT/DELETE trong log mạng → GET /api/products tải lại (Thêm/Xóa) hoặc hộp thoại (Sửa, lỗi) → 2 khung hình render. Quá 10 s → Blocked. Form không hợp lệ HTML5 → không có request, không chờ.
- Ảnh `<TC>_after-save` chụp SAU khi đo xong (không song song với việc chờ/đo).
- Giả định ngoài expected (chờ SV duyệt) nằm ở `assumptions` của file data: `page_message_selector` (HW02 H3), `xss_alert_text` = '1' (HW02 C21), `form_blocked_means` = dữ liệu SAU = TRƯỚC (HW02 C24).
- C2=a: fixture kiểm backend sau mỗi case; sập → annotation `backend sập`, resetDb, case Fail.
- Annotation mỗi TC: `expected`, `hw02`, `TRƯỚC`, `ô Giá tiền sau khi nhập`, `quan sát sau thao tác` (ô không hợp lệ, hộp thoại, thông báo, request), `SAU`.
