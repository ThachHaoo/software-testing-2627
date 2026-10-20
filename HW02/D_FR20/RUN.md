# D_FR20 – Hướng dẫn chạy tay (Android thật, Expo Go)

SV chạy; AI không chạy app. Căn cứ: D0 (trạng thái ban đầu, dữ liệu), D10/D11 (oracle), D14 (verdict), D15 (thiết bị). Expected ở `testcases.md`; file này chỉ là trình tự chạy.

Tổng: 33 case (AI 27, SV 6). Ảnh điện thoại tối đa **20** (11 bắt buộc + tối đa 9 'chỉ khi khác Expected'); ảnh trang admin trên PC tính riêng. Ước tính ≈ 1,5–2 giờ.

## Môi trường, trước mỗi lượt

1. **Khởi động lại backend** (CSDL seed lại; mọi tài khoản tạo ở lượt trước mất — D0):

   ```powershell
   cd ..\eshop-sut\backend; node server.js
   ```

2. Web admin (cửa sổ khác): `cd ..\eshop-sut\frontend-admin; npm run dev` → http://localhost:5174, đăng nhập `admin@eshop.com` / `Admin123!`, tab 'Người dùng'.
3. **Ảnh admin TRƯỚC** (ngay sau restart backend, trước case đầu tiên): chụp trang 'Quản lý Người dùng', cuộn đủ trang → `D_admin_truoc_1.png`, `_2.png`… (D11).
4. Áp patch API_URL nếu SUT chưa có (`git -C ..\eshop-sut apply --ignore-whitespace ..\software-testing-2627\HW02\env\mobile_api_url.patch`). Cần `--ignore-whitespace` vì git chuyển patch sang CRLF khi checkout trên Windows, còn App.js dùng LF. ~~Kiểm `ipconfig` vẫn là `172.21.0.137`~~ (đã thay: IP đổi trước lượt 1, App.js sửa 2026-10-20 23:51) → kiểm `ipconfig` vẫn là `192.168.2.12`; khác → sửa App.js dòng 16, tạo lại patch, ghi nhật ký.
5. Expo (cửa sổ khác): `cd ..\eshop-sut\frontend-mobile; npx expo start` → quét QR bằng Expo Go (SDK 54). Điện thoại và máy cùng Wi-Fi/hotspot.
6. Chuẩn bị sẵn trên điện thoại (vd một ghi chú) các chuỗi cần dán: mật khẩu 64 ký tự của TC-FR20-64, chuỗi của TC-FR20-200, 201, 205, 206 (D12).
7. Chép `HW02/D_FR20/results/D_FR20_manual_TEMPLATE.json` thành `HW02/D_FR20/results/D_FR20_manual_<yyyyMMdd-HHmmss>.json`.

## Sau lượt

1. **Ảnh admin SAU** (sau case cuối): tải lại trang 'Quản lý Người dùng', cuộn đủ trang → `D_admin_sau_1.png`, `_2.png`…; đối chiếu cột 'Kiểm ở ảnh admin SAU' của từng case.
2. Chép ảnh điện thoại vào `HW02/D_FR20/manual_raw/`, ảnh admin vào `HW02/D_FR20/evidence/`.
3. Nén: `py -3.12 tools/compress_manual.py` (Pillow; chỉ đụng `*_manual_*.png`, `D_admin_*.png` của D; in kích thước trước/sau).
4. Gộp: `py -3.12 .claude/skills/domain-bva-testing/scripts/merge_results.py HW02/D_FR20/testcases.json HW02/D_FR20/results/D_FR20_manual_<ts>.json` (status = verdict SV, không ghi auto_status — D14).

## {ts} và email

- `{ts}` = HHmm lúc **bắt đầu** case. Vd TC-FR20-01 → `m01_2231@domain.com`; TC-FR20-204 → `m204_2231 @domain.com` (có dấu cách). Ghi HHmm đã dùng vào Actual để đối chiếu ảnh admin SAU.
- Email chỉ có thể trùng trong cùng một lượt. Chạy lại một case trong cùng lượt → chờ sang phút mới.
- TC-FR20-06 dùng `test@eshop.com` (tài khoản seed).

## Quy trình mỗi case nhập liệu (rút gọn cho chạy tay, oracle dữ liệu theo ảnh admin của lượt)

1. Tải lại app (Reload) → màn hình chủ, header 'Đăng nhập'.
2. 'Đăng nhập' → 'Đăng ký ngay' → màn 'Đăng Ký Tài Khoản', ba ô trống, không có chữ lỗi.
3. Nhập Họ Tên → Email → Mật khẩu theo bảng (`''` = không chạm ô; ␣ = phím cách đúng số lần; bàn phím tự sửa → xoá, gõ lại — D12). Không có ô Xác nhận mật khẩu → bỏ (D9).
4. Ẩn bàn phím, bấm 'Đăng Ký' (đúng số lần ghi trong case, mặc định 1).
5. Ghi Actual nguyên văn: mọi kênh thông báo (hộp thoại: tiêu đề + nội dung trước khi đóng; chữ trên màn hình; toast) và tiêu đề màn hình sau đó. Chụp theo cột 'Ảnh điện thoại'.
6. Case hợp lệ: ở màn 'Đăng Nhập', bảo đảm ô Email đúng email case, nhập mật khẩu, bấm 'Sign In'; ghi nguyên văn header.

## Ảnh điện thoại (tối đa 20)

- Tên `TC-FR20-xx_manual_<n>.png`, n đánh từ 1 trong mỗi case.
- **bắt buộc**: chụp đúng nội dung ghi trong bảng dưới.
- **chỉ khi khác Expected**: chụp 1 ảnh `_manual_1` màn hình lúc lệch; hết ngân sách → không chụp, ghi Actual nguyên văn chữ trên màn hình.
- **không chụp**: chỉ ghi Actual nguyên văn.
- Case Pass không có ảnh riêng: bằng chứng = Actual + ảnh admin SAU.

| Ảnh bắt buộc | Nội dung |
|---|---|
| `TC-FR20-94_manual_1.png` | màn hình theo bước của case (GUI) |
| `TC-FR20-90_manual_1.png` | màn hình theo bước của case (GUI) |
| `TC-FR20-91_manual_1.png` | màn hình theo bước của case (GUI) |
| `TC-FR20-92_manual_1.png` | màn hình theo bước của case (GUI) |
| `TC-FR20-93_manual_1.png` | thông báo lỗi + nút 'Đăng Ký' (đại diện kiểu thông báo lỗi do mật khẩu yếu) |
| `TC-FR20-01_manual_1.png` | kết quả ngay sau khi bấm (hộp thoại/thông báo nếu có) — đại diện kiểu đăng ký thành công |
| `TC-FR20-01_manual_2.png` | màn hình sau khi đóng hộp thoại (đại diện màn 'Đăng Nhập') |
| `TC-FR20-01_manual_3.png` | header sau khi đăng nhập thử (đại diện 'Chào, <Họ Tên>') |
| `TC-FR20-06_manual_1.png` | thông báo sau khi bấm — đại diện kiểu từ chối do server (email đã tồn tại) |
| `TC-FR20-200_manual_1.png` | header sau khi đăng nhập thử: chuỗi <script> hiển thị dạng chữ (SEC-04) |
| `TC-FR20-201_manual_1.png` | header sau khi đăng nhập thử: emoji hiển thị |

**Đếm ảnh đã dùng:** bắt buộc ___ / 11 · chỉ khi khác Expected ___ / 9 · tổng ___ / 20

Lượt 1 (AI đếm theo ảnh, 6/7b): 31 ảnh, mỗi case đã chạy 1 ảnh `_manual_1`, vượt mức 20 (giữ hết, không bỏ ảnh nào).
- Bắt buộc: 7/11 đúng nội dung (94, 90, 91, 92, 93, 01_1, 06_1). Thiếu `01_2` (ảnh 01_1 là hộp thoại trên nền màn 'Đăng Nhập') và `01_3`. Ảnh 200 và 201 có, nhưng chụp hộp thoại 'Thành công' chứ không chụp header.
- Chỉ khi khác Expected: 6 ảnh của case lệch Expected (03, 04, 05, 15, 204, 203).
- Ngoài phân bổ: 16 ảnh của case không lệch (02, 07–14, 60, 61–64, 205, 206).
- Bổ sung sau lượt (đăng nhập thử, cùng lượt, chưa restart backend): 9 ảnh `_manual_2` (header sau đăng nhập) của 01, 02, 61–64, 200, 201, 206 → tổng **40/20**. Bắt buộc thành 10/11: header của 01 nằm ở `01_manual_2` (phân bổ ghi `01_3`), header của 200/201 nằm ở `_manual_2` (phân bổ ghi `_1`); còn thiếu ảnh 'màn hình sau khi đóng hộp thoại' của 01.

## Thứ tự case

### Nhóm 1 — GUI (chạy TC-FR20-94 đầu tiên: quyết định TC-16, TC-17)

| TC | Suite | Họ Tên | Email | Mật khẩu | Ảnh điện thoại | Kiểm ở ảnh admin SAU | Actual / verdict |
|---|---|---|---|---|---|---|---|
| TC-FR20-94 | TS-GUI | — | — | — | bắt buộc | — | file lượt, test `TC-FR20-94` |
| TC-FR20-90 | TS-GUI | — | — | — | bắt buộc | — | file lượt, test `TC-FR20-90` |
| TC-FR20-91 | TS-GUI | — | — | — | bắt buộc | — | file lượt, test `TC-FR20-91` |
| TC-FR20-92 | TS-GUI | — | — | — | bắt buộc | — | file lượt, test `TC-FR20-92` |
| TC-FR20-93 | TS-GUI | — | — | — | bắt buộc | không có dòng `m93_…` | file lượt, test `TC-FR20-93` |

### Nhóm 2 — case bị từ chối

| TC | Suite | Họ Tên | Email | Mật khẩu | Ảnh điện thoại | Kiểm ở ảnh admin SAU | Actual / verdict |
|---|---|---|---|---|---|---|---|
| TC-FR20-03 | TS-DOM | `''` (không chạm) | `m03_{ts}@domain.com` | `Abcd1234!` | chỉ khi khác Expected | không có dòng `m03_<HHmm>@domain.com` | file lượt, test `TC-FR20-03` |
| TC-FR20-04 | TS-DOM | `Nguyễn Văn Ánh` | `''` (không chạm) | `Abcd1234!` | chỉ khi khác Expected | không có dòng `''` | file lượt, test `TC-FR20-04` |
| TC-FR20-05 | TS-DOM | `Nguyễn Văn Ánh` | `m05_{ts}domain.com` | `Abcd1234!` | chỉ khi khác Expected | không có dòng `m05_<HHmm>domain.com` | file lượt, test `TC-FR20-05` |
| TC-FR20-06 | TS-DOM | `Nguyễn Văn Ánh` | `test@eshop.com` | `Abcd1234!` | bắt buộc | `test@eshop.com` có đúng 1 dòng | file lượt, test `TC-FR20-06` |
| TC-FR20-07 | TS-DOM | `Nguyễn Văn Ánh` | `m07_{ts}@domain.com` | `Abc123!` | chỉ khi khác Expected | không có dòng `m07_<HHmm>@domain.com` | file lượt, test `TC-FR20-07` |
| TC-FR20-08 | TS-DOM | `Nguyễn Văn Ánh` | `m08_{ts}@domain.com` | `''` (không chạm) | chỉ khi khác Expected | không có dòng `m08_<HHmm>@domain.com` | file lượt, test `TC-FR20-08` |
| TC-FR20-09 | TS-DOM | `Nguyễn Văn Ánh` | `m09_{ts}@domain.com` | `abcd1234!` | chỉ khi khác Expected | không có dòng `m09_<HHmm>@domain.com` | file lượt, test `TC-FR20-09` |
| TC-FR20-10 | TS-DOM | `Nguyễn Văn Ánh` | `m10_{ts}@domain.com` | `Êbcd1234!` | chỉ khi khác Expected | không có dòng `m10_<HHmm>@domain.com` | file lượt, test `TC-FR20-10` |
| TC-FR20-11 | TS-DOM | `Nguyễn Văn Ánh` | `m11_{ts}@domain.com` | `ABCD1234!` | chỉ khi khác Expected | không có dòng `m11_<HHmm>@domain.com` | file lượt, test `TC-FR20-11` |
| TC-FR20-12 | TS-DOM | `Nguyễn Văn Ánh` | `m12_{ts}@domain.com` | `ABCê1234!` | chỉ khi khác Expected | không có dòng `m12_<HHmm>@domain.com` | file lượt, test `TC-FR20-12` |
| TC-FR20-13 | TS-DOM | `Nguyễn Văn Ánh` | `m13_{ts}@domain.com` | `Abcdefgh!` | chỉ khi khác Expected | không có dòng `m13_<HHmm>@domain.com` | file lượt, test `TC-FR20-13` |
| TC-FR20-14 | TS-DOM | `Nguyễn Văn Ánh` | `m14_{ts}@domain.com` | `Abcd12345` | chỉ khi khác Expected | không có dòng `m14_<HHmm>@domain.com` | file lượt, test `TC-FR20-14` |
| TC-FR20-15 | TS-DOM | `Nguyễn Văn Ánh` | `m15_{ts}@domain.com` | `Abcd1234#` | chỉ khi khác Expected | không có dòng `m15_<HHmm>@domain.com` | file lượt, test `TC-FR20-15` |
| TC-FR20-60 | TS-BVA | `Nguyễn Văn Ánh` | `m60_{ts}@domain.com` | `Abc12!x` | chỉ khi khác Expected | không có dòng `m60_<HHmm>@domain.com` | file lượt, test `TC-FR20-60` |
| TC-FR20-204 | TS-SV | `Nguyễn Văn Ánh` | `m204_{ts} @domain.com` | `Abcd1234!` | chỉ khi khác Expected | không có dòng `m204_<HHmm> @domain.com` | file lượt, test `TC-FR20-204` |
| TC-FR20-205 | TS-SV | `Nguyễn Văn Ánh` | `m205_{ts}@domain.com` | `Abcd１２３４５６!` | chỉ khi khác Expected | không có dòng `m205_<HHmm>@domain.com` | file lượt, test `TC-FR20-205` |

### Nhóm 3 — case hợp lệ (đăng nhập thử)

| TC | Suite | Họ Tên | Email | Mật khẩu | Ảnh điện thoại | Kiểm ở ảnh admin SAU | Actual / verdict |
|---|---|---|---|---|---|---|---|
| TC-FR20-01 | TS-DOM | `Nguyễn Văn Ánh` | `m01_{ts}@domain.com` | `Abcd1234!` | bắt buộc | có đúng 1 dòng `m01_<HHmm>@domain.com` | file lượt, test `TC-FR20-01` |
| TC-FR20-02 | TS-DOM | `Trần Thị Bình` | `m02_{ts}@domain.com` | `Abcd1234!#` | chỉ khi khác Expected | có đúng 1 dòng `m02_<HHmm>@domain.com` | file lượt, test `TC-FR20-02` |
| TC-FR20-61 | TS-BVA | `Nguyễn Văn Ánh` | `m61_{ts}@domain.com` | `Abc12!xy` | chỉ khi khác Expected | có đúng 1 dòng `m61_<HHmm>@domain.com` | file lượt, test `TC-FR20-61` |
| TC-FR20-62 | TS-BVA | `Nguyễn Văn Ánh` | `m62_{ts}@domain.com` | `Abc12!xyz` | chỉ khi khác Expected | có đúng 1 dòng `m62_<HHmm>@domain.com` | file lượt, test `TC-FR20-62` |
| TC-FR20-63 | TS-BVA | `Nguyễn Văn Ánh` | `m63_{ts}@domain.com` | `Abc12!xyz345` | chỉ khi khác Expected | có đúng 1 dòng `m63_<HHmm>@domain.com` | file lượt, test `TC-FR20-63` |
| TC-FR20-64 | TS-BVA | `Nguyễn Văn Ánh` | `m64_{ts}@domain.com` | `Abc12!xxxxxxxxxx…` (64 ký tự) | chỉ khi khác Expected | có đúng 1 dòng `m64_<HHmm>@domain.com` | file lượt, test `TC-FR20-64` |
| TC-FR20-200 | TS-SV | `<script>alert(1)</script>` | `m200_{ts}@domain.com` | `Abcd1234!` | bắt buộc | có đúng 1 dòng `m200_<HHmm>@domain.com` | file lượt, test `TC-FR20-200` |
| TC-FR20-201 | TS-SV | `Lê 🐻 Hiệp` | `m201_{ts}@domain.com` | `Abcd1234!` | bắt buộc | có đúng 1 dòng `m201_<HHmm>@domain.com` | file lượt, test `TC-FR20-201` |
| TC-FR20-203 | TS-SV | `Nguyễn Văn Ánh` | `m203_{ts}@domain.com` | `Abcd1234!` | chỉ khi khác Expected · bấm 10 lần | có đúng 1 dòng `m203_<HHmm>@domain.com` | file lượt, test `TC-FR20-203` |
| TC-FR20-206 | TS-SV | 10.000 chữ 'a' | `m206_{ts}@domain.com` | `Abcd1234!` | chỉ khi khác Expected | có đúng 1 dòng `m206_<HHmm>@domain.com` | file lượt, test `TC-FR20-206` |

### Nhóm 4 — phụ thuộc ô Xác nhận mật khẩu

| TC | Suite | Họ Tên | Email | Mật khẩu | Ảnh điện thoại | Kiểm ở ảnh admin SAU | Actual / verdict |
|---|---|---|---|---|---|---|---|
| TC-FR20-16 | TS-DOM | `Nguyễn Văn Ánh` | `m16_{ts}@domain.com` | `Abcd1234!` | không chụp (Blocked nếu TC-94 Fail); TC-94 Pass → chỉ khi khác Expected | không có dòng `m16_<HHmm>@domain.com` | file lượt, test `TC-FR20-16` |
| TC-FR20-17 | TS-DOM | `Nguyễn Văn Ánh` | `m17_{ts}@domain.com` | `Abcd1234!` | không chụp (Blocked nếu TC-94 Fail); TC-94 Pass → chỉ khi khác Expected | không có dòng `m17_<HHmm>@domain.com` | file lượt, test `TC-FR20-17` |

Xác nhận mật khẩu: TC-16 `Abcd1234?`, TC-17 `abcd1234!`; các case khác = Mật khẩu (ô không có → bỏ, D9).

## Nhật ký lượt

| Lượt | Ngày giờ bắt đầu | Máy (OS) | Điện thoại (model, Android) | Expo Go | Locale / bàn phím | IP API_URL | Phạm vi | File kết quả | Ảnh admin TRƯỚC/SAU | Số ảnh điện thoại | Chính thức? | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-21 00:15 (giờ TC-FR20-94, cột Time của `results/Check.md`) | Windows 11 Home Single Language 10.0.26200 (AI lấy từ máy) | POCO F5 · OS 1.0.5.0.UMRTWXM · Android 14 (UKQ1.230804.001) | 54.0.8 | Tiếng Việt (Việt Nam) · QWERTY | `192.168.2.12` (App.js dòng 16, sửa lúc 2026-10-20 23:51, trước lượt; `HW02/env/mobile_api_url.patch` đã tạo lại theo IP này sau lượt) | 31/33 case (TC-16, TC-17 không chạy — Check.md dòng 35) | `results/D_FR20_manual_20261021-001500.json` (giây = 00: Check.md chỉ ghi HHmm) | `D_admin_truoc_1` / `D_admin_sau_1`, `_2` (+ `TC-FR20-203_admin_1`) | 31 | có (SV xác nhận đã restart backend trước lượt) | Bản ghi gốc của SV: `results/Check.md` (không sửa). Email gõ nguyên chuỗi `{ts}`, không thay HHmm (ảnh admin SAU, ảnh điện thoại) |

Lượt chính thức = lượt chạy toàn bộ sau khi restart backend. Evidence chỉ giữ lượt mới nhất.

## Đổi tên evidence (lượt 1, 6/7b)

AI đổi tên và định dạng ảnh của SV, không sửa nội dung. Ảnh gốc giữ ở `manual_raw/` (gitignore); bản nén .png (rộng 720, 256 màu) nằm ở `evidence/`, do `tools/compress_manual.py` tạo. Ảnh admin gốc SV đặt ở `evidence/` đã chép sang `manual_raw/` trước khi đổi tên. Không có cặp ảnh trùng.

| Tên gốc (SV) | Tên mới (evidence/) |
|---|---|
| `D_admin_truoc.png` | `D_admin_truoc_1.png` |
| `D_admin_sau_1.png` | `D_admin_sau_1.png` (chỉ nén) |
| `D_admin_sau_2.png` | `D_admin_sau_2.png` (chỉ nén) |
| `TC-FR20-203-admin_manual.png` | `TC-FR20-203_admin_1.png` |
| `TC-FR20-90-manual.jpg`, `TC-FR20-94-manual.jpg` | `TC-FR20-90_manual_1.png`, `TC-FR20-94_manual_1.png` |
| `TC-FR20-<xx>_manual.jpg` (29 ảnh: 01–15, 60–64, 91–93, 200, 201, 203–206) | `TC-FR20-<xx>_manual_1.png` |
| `TC-FR20-<xx>_manual_2.jpg` (9 ảnh đăng nhập thử: 01, 02, 61–64, 200, 201, 206) | `TC-FR20-<xx>_manual_2.png` (chỉ đổi định dạng) |

## Đồng bộ file lượt với status SV chốt (6/7b3)

Annotation `verdict` của `results/D_FR20_manual_20261021-001500.json` được đặt bằng status SV chốt ở f644140. Nhãn ghi ở annotation `label` (merge không đọc; notes trong `testcases.json` đã có sẵn). Sau khi đồng bộ, chạy `merge_results.py --dry-run` cho D ra status giống hệt 33/33 case, nên merge lại không còn làm mất status SV chốt. Actual của file lượt có thêm phần "Đăng nhập thử" cho 9 case (AI chép từ ảnh `_manual_2`); Check.md giữ nguyên.

| TC | verdict trước (Check.md) | verdict sau | label |
|---|---|---|---|
| TC-FR20-07…14, 60, 205 (10 case) | Pass | Pass | Pass hộp đen |
| TC-FR20-203 | Pass | Fail | Fail do lỗi thiết kế TC, không lập bug |
| TC-FR20-16 | (trống) | Blocked | — |
| TC-FR20-17 | (trống) | Blocked | — |

## Ghi chú harness

- Quy trình trong `testcases.json` (TS-DOM/TS-BVA/TS-SV bước 1 và 7) đã khớp D0 (SV chốt): so ảnh admin TRƯỚC/SAU của lượt (6/7a3). Chữ Expected 'so với TRƯỚC' giữ nguyên, đọc theo ảnh admin của lượt.
