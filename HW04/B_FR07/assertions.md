# B_FR07 – bảng assertion (bước 3, AI sinh)

Spec: `HW04/tests/B_FR07.spec.ts`; thao tác + oracle đọc từ cột `Thao tác` / `expected` của `HW04/data/B_FR07.json` bằng `HW04/tests/oracles/b_fr07.oracle.ts` (cú pháp lạ → ném lỗi; cụm expected không ánh xạ được → annotation `oracle không tự động`). Mọi assertion là `expect.soft`.

## Kiểu assertion

| # | Kiểu | Matcher | Dùng cho | TC |
|---|---|---|---|---|
| 1 | Trạng thái UI | `toHaveURL` | URL sau khi bấm link về trang chủ ở trang giỏ | 01, 02 |
| 1 | Trạng thái UI | `toBeVisible` | img/svg minh hoạ giỏ trống | 01 |
| 2 | Nội dung | `toHaveText` | tiêu đề trang chi tiết = tên sản phẩm (seed) | mọi TC có `CT:` |
| 2 | Nội dung | `toContainText` | dòng chữ báo giỏ trống (chứa "trống"; kèm annotation `oracle thông báo yếu`) | 01 |
| 3 | Oracle trạng thái giỏ (object) | `toEqual` | danh sách dòng SAU {tên, Đơn giá, Số lượng, Thành tiền} = TRƯỚC + thay đổi expected nêu (không phụ thuộc thứ tự); dòng "không đổi" = TRƯỚC; dialog là `confirm`; không có alert | 02, 04, 08, 10, 11, 13, 60–64, 66, 200, 205 |
| 4 | Đếm | `toHaveCount` | số dòng TRƯỚC/SAU lần k; không còn bảng; link về trang chủ trong main; dòng id ở lần k | 01, 02, 61–64, 66, 205 |
| 5 | Giá trị | `toBe` / `toContain` / `not.toContain` | Tổng SAU, Tổng = Σ Thành tiền, badge SAU, badge ẩn hoặc 0, số dòng SAU, không có dòng X | 01, 04, 08, 10–13, 60–64 |
| 6 | Phản hồi (B21) | `not.toBeNull` / `toBeNull` | thay đổi nhìn thấy được trong ≤ 2 s sau khi bấm thêm (toast, navbar/badge, chữ nút, nội dung main) | 02, 205 (có); 10, 11, 13, 60 (không) |
| 7 | Dialog | `expect.poll(...).toBe(1)` | có đúng 1 dialog sau khi bấm Xóa (chờ tối đa 2 s) | 08 |

## Quy ước

- Procedure HW02 bước 3: giỏ TRƯỚC không khớp cột `Giỏ ban đầu` → **Blocked** (B20), không Fail.
- Bước điều hướng/chuẩn bị (mở trang, dựng giỏ, mở /cart, mở chi tiết) quá hạn → **Blocked** (`step()`); assertion không bị đổi thành Blocked.
- Bấm `Thêm vào giỏ hàng` / `Xóa` **đúng 1 lần** như procedure; không bấm thêm để lách "lần bấm đầu không thêm" (ProductDetail.jsx:21–25).
- Dialog native được ghi lại (loại + nội dung) rồi chấp nhận/huỷ theo cột Thao tác (fixture `dialogAction`).
- Cửa sổ 2 s của B21 là cửa sổ quan sát do oracle quy định (`waitForFunction` timeout → "không có phản hồi"), không phải chờ cứng để đồng bộ.
- Annotation mỗi TC: `expected`, `hw02`, `TRƯỚC`, `SAU`, `ô Số lượng sau khi gõ`, `phản hồi sau khi bấm thêm`, `dialog sau khi bấm xoá`.

## Không tự động được (annotation `oracle không tự động`)

| TC | Cụm expected | Lý do |
|---|---|---|
| TC-FR07-08 | "dòng chưa bị xoá khi dialog đang mở" | SUT hiện không hiện dialog nào khi bấm Xóa (lượt chính thức: `dialog sau khi bấm xoá = []`, BUG-93) → không có trạng thái "dialog đang mở" để kiểm. Nếu SUT có dialog native (`window.confirm`): dialog khoá trang, script không đọc DOM khi dialog đang mở → kiểm tay |
