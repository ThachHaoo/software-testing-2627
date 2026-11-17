# B_FR07 – SV soi spec (bước 5)

Spec được soi: `HW04/tests/B_FR07.spec.ts` @ `7e75536` (bản AI bước 3, đóng băng ở `HW04/appendix/ai-outputs/B_FR07/step3/`). Lượt chạy tham chiếu: lượt thử 1 (`HW04/B_FR07/RUN.md`).

## Danh sách soi spec của SV (chép nguyên văn)

> Soi spec:
> - Chờ hardcode (waitForTimeout), có thể gây chậm suite cũng như dễ flaky: Giả sử nó chạy nhanh hơn thì gây chậm, còn nếu có khi mạng lag hoặc CPU lag thì gây ra flaky.
> - Selector phụ thuộc cấu trúc DOM và thẻ HTML chung chung: cảm giác script kiểm tra hình minh hoạ giỏ giống bằng selector main img, main svg không đủ tốt lắm.Vậy nên dễ nhầm nếu trong \<main\> có icon khác hoặc fail nếu UI dùng \<canvas\>
> - Assertion phụ thuộc chặt vào câu chữ tiếng Việt cụ thể: Các assertion đang khớp hardcode text. Nên nếu đổi thông báo thì lại fail.
> - Cách bắt sự kiện dialog: script gắn listener page.on('dialog', ...) và tự động accept() ngay lập tức. Nên cái này chỉ check có bật dialog hay không chứ không kiểm tra được trạng thái UI tạm dừng.

## Đối chiếu code (phiên thảo luận)

| # | Ý của SV (tóm tắt) | Đối chiếu code (phiên thảo luận) | Xử lý |
|---|---|---|---|
| 1 | Chờ hardcode `waitForTimeout` | Spec không có `waitForTimeout`; chỉ có ngưỡng 2 s của B21 (`FEEDBACK_WINDOW`, dòng 62–72 `waitForFunction` timeout 2 s; dòng 161 `expect.poll` dialog timeout 2 s) — là cửa sổ quan sát do oracle quy định | Không sửa |
| 2 | Selector `main img, main svg` chung chung | Selector bám Expected ("img hoặc svg"); yếu ở `.first()` + nhận mọi img/svg trong `main` (dòng 124, `shop.pages.ts` `emptyIllustration`) | R2 → 5/6b |
| 3 | Assertion khớp câu chữ cứng | `/trống/i` gõ cứng ở dòng 121; tên sản phẩm ở dòng 133 lấy từ data (bảng seed), không gõ cứng | R1=a → 5/6a |
| 4 | Dialog bị accept ngay | Fixture mặc định `dismiss`; thao tác xoá có "xác nhận" → `accept` (dòng 157). Phần "dòng chưa bị xoá khi dialog đang mở" (TC-08) không tự động hoá được (dialog native khoá trang) | Ghi `not_automated.md` |

## Phiên thảo luận bổ sung

- P1=a: chụp ảnh ngay sau thao tác chính (sau bấm Thêm/Xoá) bằng `testInfo.attach`, tên `<TC>_after-action` → 5/6c (áp cả A_FR01: ảnh sau bấm Đăng Ký, 5/6e).

## Các commit sửa

| Commit | Mục | Nội dung |
|---|---|---|
| 5/6a | R1=a | từ khoá giỏ trống chuyển vào `HW04/data/B_FR07.json` (giả định SV chốt), expected giữ nguyên |
| 5/6b | R2 | ảnh/icon minh hoạ phải nằm trong cùng khối chứa dòng chữ giỏ trống; bỏ `.first()` chung |
| 5/6c | P1=a | ảnh `<TC>_after-action` sau thao tác chính |
