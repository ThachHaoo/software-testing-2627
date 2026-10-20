# C_FR15 – Lệnh chạy test (SV chạy trên máy mình, PowerShell)

Spec: `HW02/tests/C_FR15/C_FR15.spec.ts` (+ `lib.ts`, `oracle.ts`), project Playwright `C_FR15`. Có 117 test tự động: 106 case AI (TS-DOM-*, TS-BVA-*) và 11 case SV (TS-SV-UI, TS-SV-API). 5 case GUI (TS-GUI, TC-FR15-90…94) chạy tay, xem mục cuối.

## Mỗi lượt chạy

1. **Khởi động lại backend trước MỌI lượt**, kể cả lượt chạy lại vài case. CSDL được seed lại (5 sản phẩm id 1–5). `global-setup.ts` dừng lượt chạy nếu CSDL có sản phẩm khác id 1–5.

   ```powershell
   cd ..\eshop-sut\backend; node server.js
   ```

2. Chạy web admin :5174 (cửa sổ PowerShell khác; giữ chạy giữa các lượt):

   ```powershell
   cd ..\eshop-sut\frontend-admin; npm run dev
   ```

3. Chạy test (cửa sổ PowerShell khác, từ thư mục repo). Results ghi riêng theo timestamp:

   ```powershell
   cd HW02/tests; $ts = Get-Date -Format yyyyMMdd-HHmmss; $env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/C_FR15_$ts.json"; npx playwright test --project=C_FR15 --reporter=list,json; cd ../..; echo "results/C_FR15_$ts.json"
   ```

4. Gộp kết quả vào `testcases.json` (thay `<ts>` bằng giá trị in ra ở bước 3):

   ```powershell
   python .claude/skills/domain-bva-testing/scripts/merge_results.py HW02/C_FR15/testcases.json HW02/tests/results/C_FR15_<ts>.json
   ```

   - `merge_results.py` ghi `auto_status`, `actual_result`, `evidence`.
   - **Không ghi đè `status` mà SV đã chỉnh** (status khác auto_status, theo C14/A20). Muốn ghi đè thì thêm `--force`.
   - Evidence chép vào `HW02/C_FR15/evidence/`, tên theo dạng `TC-xx_ui.png`, `_api.png`, `_req.json`, `_res.json`, `_failed.png`. Evidence chỉ giữ của lượt mới nhất.

5. Chạy lại vài case (vẫn phải làm bước 1 trước), ví dụ TC-201 và TC-205:

   ```powershell
   cd HW02/tests; $ts = Get-Date -Format yyyyMMdd-HHmmss; $env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/C_FR15_$ts.json"; npx playwright test --project=C_FR15 -g "TC-FR15-(201|205) " --reporter=list,json; cd ../..
   ```

Lượt chính thức = lượt chạy **toàn bộ** ngay sau khi khởi động lại backend. Ghi mỗi lượt vào bảng nhật ký cuối file.

## Cách test quan sát và dọn dữ liệu

- **Độc lập:** mỗi case dùng `{ts}` = `Date.now()` lúc chạy; sản phẩm mục tiêu M được dựng qua API (procedure bước 1).
- **Cleanup lớp 1:** sau mỗi case, kể cả khi Fail, xoá mọi id mới xuất hiện so với lúc case bắt đầu.
- **Cleanup lớp 2:** cuối lượt, xoá mọi id không có lúc đầu lượt hoặc có tên chứa mốc `{ts}` của lượt. Không xoá được thì in cảnh báo; khi đó khởi động lại backend.
- **Oracle:**
  - Case AI lấy từ `oracle.ts`, case SV lấy từ `SV_ORACLE` trong spec. Cả hai khoá bằng sha1 của `expected_result`: Expected trong JSON đổi thì test báo "oracle cũ", không tự chạy theo bản cũ.
  - Case nhiều khẳng định dùng `expect.soft`; mọi chỗ lệch nằm trong Actual.
- **Body API:** gửi thô bằng `Buffer` đúng như cột (để `Infinity`, `1e-324`, khoá thiếu, chuỗi số giữ nguyên). Số nguyên vượt `Number.MAX_SAFE_INTEGER` được so trên chuỗi.
- **Thông báo lỗi trên UI (C7, C16):** test ghi lại hộp thoại trình duyệt (nội dung đủ trong Actual; ảnh không chụp được hộp thoại native) và ô HTML5 không hợp lệ (`validationMessage`).
  - Để tự động phân biệt hộp thoại báo lỗi với hộp thoại báo thành công, test dùng regex `lỗi|error|không hợp lệ|invalid|bắt buộc|required|please|vui lòng`.
  - **SV xem lại Actual** khi verdict phụ thuộc vào việc phân loại này.
- **Cách AI hiểu TC-206** (SV xem lại): dựng SP1 và SP2. Bấm 'Sửa' SP1, sửa ô Tên thành `SP1 tạm {ts}`, rồi bấm 'Sửa' SP2 (không bấm 'Hủy sửa'). Ghi giá trị form. Nhập các cột của case cho SP2 rồi bấm 'Lưu sản phẩm' một lần.
- **TC-205:** chữ số full-width được đưa vào ô bằng `keyboard.insertText`, mô phỏng thao tác dán.

## Case manual (TS-GUI: TC-FR15-90…94)

Chạy tay sau khi khởi động lại backend. Dùng **cửa sổ ẩn danh, tắt mọi tiện ích**, đăng nhập `admin@eshop.com` / `Admin123!`, mở mục 'Sản phẩm'. Làm đúng các bước và Expected của case trong `testcases.md` (mục TS-GUI).

- Ảnh lưu vào `HW02/C_FR15/evidence/`, tên `TC-FR15-9x_manual_<n>.png` (n = 1, 2…). Ảnh chụp cả cửa sổ trình duyệt; không chụp màn hình có tên người dùng/hostname của máy.
- Ghi `actual_result`, `status`, `evidence` của case vào `testcases.json` (hoặc gửi AI chép vào). Ghi `notes` "Manual – <ngày giờ>".

| Case | Cần chụp |
|---|---|
| TC-FR15-90 | Form 'Thêm sản phẩm mới' với 3 trường Tên, Giá, Danh mục (thấy có/không có nhãn và dấu '*') |
| TC-FR15-91 | Ngay sau khi bấm 'Lưu sản phẩm' với Tên để trống: thấy thông báo lỗi và nút 'Lưu sản phẩm' trong cùng ảnh. Thông báo là hộp thoại trình duyệt thì chụp hộp thoại và ghi nội dung (C16) |
| TC-FR15-92 | Ô 'Giá' của dòng 'iPhone 15 Pro Max'. Ghi locale trình duyệt vào notes (C17) |
| TC-FR15-93 | DevTools (Elements) chọn thẻ `<img>` của cột 'Ảnh', thấy thuộc tính `alt`. Mỗi ảnh một tấm, hoặc Console: `[...document.querySelectorAll('table img')].map(i => i.alt)` |
| TC-FR15-94 | Ô 'Tên SP' của dòng `<i>SEC04 {ts}</i>` và DevTools (Elements) của ô đó (có/không có phần tử `<i>`) |

## Nhật ký lượt chạy

| Lượt | Thời điểm | Phạm vi | Results | Ghi chú |
|---|---|---|---|---|
| | | | | |
