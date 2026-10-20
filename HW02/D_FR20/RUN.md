# D_FR20 – Hướng dẫn chạy tay (Android thật, Expo Go)

SV chạy; AI không chạy app. Căn cứ: D0 (trạng thái ban đầu, dữ liệu), D10/D11 (oracle), D14 (verdict), D15 (thiết bị). Expected ở `testcases.md`; bảng này chỉ là trình tự chạy.

Tổng: 33 case (AI 27, SV 6). Ảnh: tối đa 128 ảnh. Ước tính ≈ 2 giờ (≈ 3,5 phút/case nhập liệu, ≈ 1,5 phút/case GUI; chưa tính chuẩn bị).

## Trước mỗi lượt

1. **Khởi động lại backend** (CSDL seed lại; mọi tài khoản tạo ở lượt trước mất — D0):

   ```powershell
   cd ..\eshop-sut\backend; node server.js
   ```

2. Web admin (cửa sổ khác): `cd ..\eshop-sut\frontend-admin; npm run dev` → http://localhost:5174, đăng nhập `admin@eshop.com` / `Admin123!`, mở tab 'Người dùng'.
3. Kiểm IP LAN của máy (`ipconfig`) vẫn là `172.21.0.137` (App.js dòng 16, `HW02/env/mobile_api_url.patch`). Khác → sửa App.js, tạo lại patch, ghi vào nhật ký lượt.
4. Expo (cửa sổ khác): `cd ..\eshop-sut\frontend-mobile; npx expo start` → quét QR bằng Expo Go (SDK 54). Điện thoại và máy cùng Wi-Fi/hotspot.
5. Chuẩn bị sẵn trên điện thoại (vd một ghi chú) các chuỗi cần dán: mật khẩu 64 ký tự của TC-FR20-64, chuỗi của TC-FR20-200, 201, 205, 206 (D12: dán và gõ cùng lớp).
6. Chép `HW02/D_FR20/results/D_FR20_manual_TEMPLATE.json` thành `HW02/D_FR20/results/D_FR20_manual_<yyyyMMdd-HHmmss>.json` cho lượt này.

## {ts} và email

- `{ts}` = 4 chữ số giờ-phút lúc **bắt đầu** case (HHmm, vd 2231). Email của case = thay `{ts}` trong cột Email, vd TC-FR20-01 → `m01_2231@domain.com`, TC-FR20-204 → `m204_2231 @domain.com` (có dấu cách).
- Email chỉ có thể trùng trong cùng một lượt (restart backend xoá dữ liệu). Chạy lại một case trong cùng lượt → chờ sang phút mới để HHmm khác; nếu không, email rơi vào EC7 (đã tồn tại).
- TC-FR20-06 dùng `test@eshop.com` (tài khoản seed).

## Quy trình chung mỗi case nhập liệu (TS-DOM, TS-BVA, TS-SV)

1. Trên máy tính: tải lại trang admin (F5), mở tab 'Người dùng'; đếm số dòng, chụp ảnh TC-FR20-xx_manual_admin_before.png. → *Bảng 'Quản lý Người dùng' hiển thị, có admin@eshop.com và test@eshop.com.*
2. Trên điện thoại: tải lại app trong Expo Go (Reload). → *Màn hình chủ; header hiển thị 'Đăng nhập'.*
3. Bấm 'Đăng nhập' trên header, rồi bấm 'Đăng ký ngay'. → *Màn 'Đăng Ký Tài Khoản' hiển thị; ba ô Họ Tên, Email, Mật khẩu trống; không có chữ lỗi.*
4. Nhập lần lượt Họ Tên → Email → Mật khẩu → Xác nhận mật khẩu (nếu có) bằng bàn phím ảo, gõ đúng chuỗi trong cột. Ô có giá trị `''` (rỗng): không chạm vào ô, giữ trống. Giá trị có ␣: bấm phím cách đúng số lần đó. Bàn phím tự viết hoa/tự sửa/chèn gợi ý làm đổi chuỗi → xoá và gõ lại cho đúng, ghi notes (D12). Không có ô Xác nhận mật khẩu → làm theo notes của case (D9). → *Ô Họ Tên và Email hiển thị đúng chuỗi trong cột; ô Mật khẩu hiển thị dạng che với số ký tự che bằng độ dài chuỗi trong cột. Chụp TC-FR20-xx_manual_input.png.*
5. Ẩn bàn phím, bấm nút 'Đăng Ký' đúng một lần. → *App phản hồi (chữ lỗi, hộp thoại, toast hoặc chuyển màn hình).*
6. Quan sát và chụp TC-FR20-xx_manual_result.png: mọi kênh thông báo (hộp thoại: ghi tiêu đề + nội dung rồi mới đóng; chữ trên màn hình; toast) và tiêu đề màn hình sau khi đóng hộp thoại. → *Khớp phần app của cột Expected.*
7. Trên máy tính: tải lại trang admin, mở tab 'Người dùng'; so với ảnh ở bước 1, chụp TC-FR20-xx_manual_admin_after.png. → *Số dòng và Email như cột Expected (oracle tương đối).*
8. Chỉ case hợp lệ: trên màn 'Đăng Nhập' của app, bảo đảm ô Email chứa đúng email của case (xoá và gõ lại nếu khác), nhập Mật khẩu của case, bấm 'Sign In'; chụp TC-FR20-xx_manual_login.png. → *Header hiển thị 'Chào, <Họ Tên của case>' như cột Expected.*

TS-SV: bấm 'Đăng Ký' đúng số lần ghi trong case (mặc định 1 lần; TC-FR20-203: 10 lần liên tục).

## Ảnh

- Chụp trên điện thoại / máy, đặt tên `TC-FR20-xx_manual_<n>.png`, lưu vào `HW02/D_FR20/manual_raw/` (bản gốc, không che).
- n: 1 = admin TRƯỚC · 2 = ô sau khi nhập · 3 = kết quả sau khi bấm · 4 = admin SAU · 5 = header sau khi đăng nhập thử (chỉ case hợp lệ). Case GUI: 1 (và 2 cho TC-93).
- Hộp thoại: ghi tiêu đề + nội dung nguyên văn **trước** khi đóng.

## Ghi kết quả

- File lượt (`results/D_FR20_manual_<ts>.json`): với mỗi case, điền annotation `actual` (Actual nguyên văn: mọi kênh thông báo, tiêu đề màn hình, số dòng admin TRƯỚC → SAU, email dòng mới, header sau đăng nhập) và annotation `verdict` (`Pass` / `Fail` / `Blocked` / `Not run`). Không sửa `expected_result`.
- Case Blocked/Pass hộp đen: ghi case gốc vào `notes` của case trong `testcases.json` sau khi gộp (D14).
- Gộp: `python .claude/skills/domain-bva-testing/scripts/merge_results.py HW02/D_FR20/testcases.json HW02/D_FR20/results/D_FR20_manual_<ts>.json` (chạy từ thư mục repo).

## Thứ tự case

### Nhóm 1 — GUI, không cần trang admin (chạy TC-FR20-94 đầu tiên: quyết định TC-16, TC-17)

| TC | Suite | Họ Tên | Email | Mật khẩu | Xác nhận MK | Ảnh | Quan sát chính | Actual / verdict |
|---|---|---|---|---|---|---|---|---|
| TC-FR20-94 | TS-GUI | — | — | — | — | `_1` | Màn 'Đăng Ký Tài Khoản' có trường Xác nhận mật khẩu (FR-01.9). | file lượt, test `TC-FR20-94` |
| TC-FR20-90 | TS-GUI | — | — | — | — | `_1` | Mỗi nhãn trường bắt buộc theo FR-01 có ký hiệu '*' bên cạnh. | file lượt, test `TC-FR20-90` |
| TC-FR20-91 | TS-GUI | — | — | — | — | `_1` | Chạm vào ô Email hiện bàn phím email (keyboardType email-address theo D13). | file lượt, test `TC-FR20-91` |
| TC-FR20-92 | TS-GUI | — | — | — | — | `_1` | Ô Mật khẩu (và ô Xác nhận mật khẩu nếu có) che ký tự đã nhập. | file lượt, test `TC-FR20-92` |
| TC-FR20-93 | TS-GUI | — | — | — | — | `_1` · `_2` | Thông báo lỗi nằm phía trên nút 'Đăng Ký' (không nằm bên dưới). | file lượt, test `TC-FR20-93` |

### Nhóm 2 — case bị từ chối (trang admin TRƯỚC/SAU)

| TC | Suite | Họ Tên | Email | Mật khẩu | Xác nhận MK | Ảnh | Quan sát chính | Actual / verdict |
|---|---|---|---|---|---|---|---|---|
| TC-FR20-03 | TS-DOM | `''` (không chạm vào ô) | `m03_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-03` |
| TC-FR20-04 | TS-DOM | `Nguyễn Văn Ánh` | `''` (không chạm vào ô) | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-04` |
| TC-FR20-05 | TS-DOM | `Nguyễn Văn Ánh` | `m05_{ts}domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-05` |
| TC-FR20-06 | TS-DOM | `Nguyễn Văn Ánh` | `test@eshop.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-06` |
| TC-FR20-07 | TS-DOM | `Nguyễn Văn Ánh` | `m07_{ts}@domain.com` | `Abc123!` | `Abc123!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-07` |
| TC-FR20-08 | TS-DOM | `Nguyễn Văn Ánh` | `m08_{ts}@domain.com` | `''` (không chạm vào ô) | `''` (không chạm vào ô) | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-08` |
| TC-FR20-09 | TS-DOM | `Nguyễn Văn Ánh` | `m09_{ts}@domain.com` | `abcd1234!` | `abcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-09` |
| TC-FR20-10 | TS-DOM | `Nguyễn Văn Ánh` | `m10_{ts}@domain.com` | `Êbcd1234!` | `Êbcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-10` |
| TC-FR20-11 | TS-DOM | `Nguyễn Văn Ánh` | `m11_{ts}@domain.com` | `ABCD1234!` | `ABCD1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-11` |
| TC-FR20-12 | TS-DOM | `Nguyễn Văn Ánh` | `m12_{ts}@domain.com` | `ABCê1234!` | `ABCê1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-12` |
| TC-FR20-13 | TS-DOM | `Nguyễn Văn Ánh` | `m13_{ts}@domain.com` | `Abcdefgh!` | `Abcdefgh!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-13` |
| TC-FR20-14 | TS-DOM | `Nguyễn Văn Ánh` | `m14_{ts}@domain.com` | `Abcd12345` | `Abcd12345` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-14` |
| TC-FR20-15 | TS-DOM | `Nguyễn Văn Ánh` | `m15_{ts}@domain.com` | `Abcd1234#` | `Abcd1234#` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-15` |
| TC-FR20-60 | TS-BVA | `Nguyễn Văn Ánh` | `m60_{ts}@domain.com` | `Abc12!x` | `Abc12!x` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-60` |
| TC-FR20-204 | TS-SV | `Nguyễn Văn Ánh` | `m204_{ts} @domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-204` |
| TC-FR20-205 | TS-SV | `Nguyễn Văn Ánh` | `m205_{ts}@domain.com` | `Abcd１２３４５６!` | `Abcd１２３４５６!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC | file lượt, test `TC-FR20-205` |

### Nhóm 3 — case hợp lệ (trang admin TRƯỚC/SAU + đăng nhập thử)

| TC | Suite | Họ Tên | Email | Mật khẩu | Xác nhận MK | Ảnh | Quan sát chính | Actual / verdict |
|---|---|---|---|---|---|---|---|---|
| TC-FR20-01 | TS-DOM | `Nguyễn Văn Ánh` | `m01_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-01` |
| TC-FR20-02 | TS-DOM | `Trần Thị Bình` | `m02_{ts}@domain.com` | `Abcd1234!#` | `Abcd1234!#` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-02` |
| TC-FR20-61 | TS-BVA | `Nguyễn Văn Ánh` | `m61_{ts}@domain.com` | `Abc12!xy` | `Abc12!xy` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-61` |
| TC-FR20-62 | TS-BVA | `Nguyễn Văn Ánh` | `m62_{ts}@domain.com` | `Abc12!xyz` | `Abc12!xyz` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-62` |
| TC-FR20-63 | TS-BVA | `Nguyễn Văn Ánh` | `m63_{ts}@domain.com` | `Abc12!xyz345` | `Abc12!xyz345` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-63` |
| TC-FR20-64 | TS-BVA | `Nguyễn Văn Ánh` | `m64_{ts}@domain.com` | `Abc12!xxxxxxxxxxxxxx…` (64 ký tự) | `Abc12!xxxxxxxxxxxxxx…` (64 ký tự) | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-64` |
| TC-FR20-200 | TS-SV | `<script>alert(1)</script>` | `m200_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-200` |
| TC-FR20-201 | TS-SV | `Lê 🐻 Hiệp` | `m201_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-201` |
| TC-FR20-203 | TS-SV | `Nguyễn Văn Ánh` | `m203_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' · bấm 10 lần | file lượt, test `TC-FR20-203` |
| TC-FR20-206 | TS-SV | `10.000 chữ 'a'` | `m206_{ts}@domain.com` | `Abcd1234!` | `Abcd1234!` | `_1` · `_2` · `_3` · `_4` · `_5` | màn 'Đăng Nhập' + đúng 1 dòng admin mới + header 'Chào, …' | file lượt, test `TC-FR20-206` |

### Nhóm 4 — phụ thuộc ô Xác nhận mật khẩu

| TC | Suite | Họ Tên | Email | Mật khẩu | Xác nhận MK | Ảnh | Quan sát chính | Actual / verdict |
|---|---|---|---|---|---|---|---|---|
| TC-FR20-16 | TS-DOM | `Nguyễn Văn Ánh` | `m16_{ts}@domain.com` | `Abcd1234!` | `Abcd1234?` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC · **không chạy, đánh dấu Blocked nếu TC-94 Fail** (case gốc TC-FR20-94, D9) | file lượt, test `TC-FR20-16` |
| TC-FR20-17 | TS-DOM | `Nguyễn Văn Ánh` | `m17_{ts}@domain.com` | `Abcd1234!` | `abcd1234!` | `_1` · `_2` · `_3` · `_4` | thông báo lỗi (mọi kênh) + ở lại màn Đăng ký + admin SAU = TRƯỚC · **không chạy, đánh dấu Blocked nếu TC-94 Fail** (case gốc TC-FR20-94, D9) | file lượt, test `TC-FR20-17` |

Ô 'Xác nhận mật khẩu' không có trên màn hình → mọi case trừ TC-16, TC-17 bỏ bước nhập ô này và ghi notes (D9).

## Nhật ký lượt

| Lượt | Ngày giờ bắt đầu | Máy (OS) | Điện thoại (model, Android) | Expo Go | Locale / bàn phím | IP API_URL | Phạm vi | File kết quả | Chính thức? | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | |

Lượt chính thức = lượt chạy toàn bộ sau khi restart backend. Evidence chỉ giữ lượt mới nhất.
## Hạn chế harness khi gộp kết quả chạy tay (chưa vá, chờ SV quyết)

- `merge_results.py` đổi tên ảnh theo tên attachment qua `slug()`: `TC-FR20-xx_manual_1` → `evidence/TC-FR20-xx_manual-1.png` (gạch ngang thay gạch dưới).
- `merge_results.py` ghi `auto_status` = verdict SV điền trong file lượt, trong khi D14 ghi "auto_status để trống" khi chạy tay.
