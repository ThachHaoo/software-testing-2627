# B_FR07 – nhóm TC Fail (dữ kiện, SV viết bug)

Nhóm = cùng tập assertion lỗi và cùng giá trị nhận được (triệu chứng giống hệt; số dài `{ts}` chuẩn hoá).
Không đặt tên bug, không severity/priority, không kết luận nguyên nhân, không đề xuất gộp/tách.
Ảnh lúc kết thúc = screenshot Playwright chụp lúc test KẾT THÚC (screenshot: 'only-on-failure'), không phải lúc assertion đầu tiên lỗi.
Ảnh ngay sau thao tác chính = ảnh spec tự đính (`<TC>_after-submit` / `<TC>_after-action[-k]`) ngay sau bấm Đăng Ký / Thêm / Xoá.

## G1 – 4 TC × 3 trình duyệt (12 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: Tổng SAU | expect(received).toBe(expected) // Object.is equality | Received: null`
- `Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền) | expect(received).toEqual(expected) // deep equality | + Array []`
- `Error: số dòng SAU | expect(received).toBe(expected) // Object.is equality | Received: 0`

### TC-FR07-61 – Kiểm tra thêm từ trang chi tiết khi số lượng bằng 1 và giỏ rỗng

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / BVA LB
- HW02: Fail · BUG-15
- Expected (HW02, nguyên văn): TRƯỚC → SAU: 0 → 1 dòng 'Bàn phím cơ Keychron Q1', Số lượng 1, Thành tiền 4000000; Tổng 4000000.
- Ảnh lúc kết thúc: `evidence/TC-FR07-61_chrome.png`, `evidence/TC-FR07-61_edge.png`, `evidence/TC-FR07-61_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-61_after-action_chrome.png`, `evidence/TC-FR07-61_after-action_edge.png`, `evidence/TC-FR07-61_after-action_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)

expect(received).toEqual(expected) // deep equality

- Expected  - 8
+ Received  + 1

- Array [
-   Object {
-     "name": "Bàn phím cơ Keychron Q1",
-     "price": 4000000,
-     "qty": "1",
-     "subtotal": 4000000,
-   },
- ]
+ Array []

Error: số dòng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 1
Received: 0

Error: Tổng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 4000000
Received: null
```

### TC-FR07-62 – Kiểm tra thêm từ trang chi tiết khi số lượng bằng 2 và giỏ rỗng

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / BVA LB+1
- HW02: Fail · BUG-15
- Expected (HW02, nguyên văn): TRƯỚC → SAU: 0 → 1 dòng 'Bàn phím cơ Keychron Q1', Số lượng 2, Thành tiền 8000000; Tổng 8000000.
- Ảnh lúc kết thúc: `evidence/TC-FR07-62_chrome.png`, `evidence/TC-FR07-62_edge.png`, `evidence/TC-FR07-62_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-62_after-action_chrome.png`, `evidence/TC-FR07-62_after-action_edge.png`, `evidence/TC-FR07-62_after-action_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)

expect(received).toEqual(expected) // deep equality

- Expected  - 8
+ Received  + 1

- Array [
-   Object {
-     "name": "Bàn phím cơ Keychron Q1",
-     "price": 4000000,
-     "qty": "2",
-     "subtotal": 8000000,
-   },
- ]
+ Array []

Error: số dòng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 1
Received: 0

Error: Tổng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 8000000
Received: null
```

### TC-FR07-63 – Kiểm tra thêm từ trang chi tiết khi số lượng ở giá trị danh nghĩa 5

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / BVA NOM
- HW02: Fail · BUG-15
- Expected (HW02, nguyên văn): TRƯỚC → SAU: 0 → 1 dòng 'Bàn phím cơ Keychron Q1', Số lượng 5, Thành tiền 20000000; Tổng 20000000.
- Ảnh lúc kết thúc: `evidence/TC-FR07-63_chrome.png`, `evidence/TC-FR07-63_edge.png`, `evidence/TC-FR07-63_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-63_after-action_chrome.png`, `evidence/TC-FR07-63_after-action_edge.png`, `evidence/TC-FR07-63_after-action_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)

expect(received).toEqual(expected) // deep equality

- Expected  - 8
+ Received  + 1

- Array [
-   Object {
-     "name": "Bàn phím cơ Keychron Q1",
-     "price": 4000000,
-     "qty": "5",
-     "subtotal": 20000000,
-   },
- ]
+ Array []

Error: số dòng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 1
Received: 0

Error: Tổng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 20000000
Received: null
```

### TC-FR07-64 – Kiểm tra thêm từ trang chi tiết khi số lượng là giá trị lớn 1000

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / BVA LARGE
- HW02: Fail · BUG-15
- Expected (HW02, nguyên văn): TRƯỚC → SAU: 0 → 1 dòng 'Bàn phím cơ Keychron Q1', Số lượng 1000, Thành tiền 4000000000; Tổng 4000000000 (B1: hợp lệ).
- Ảnh lúc kết thúc: `evidence/TC-FR07-64_chrome.png`, `evidence/TC-FR07-64_edge.png`, `evidence/TC-FR07-64_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-64_after-action_chrome.png`, `evidence/TC-FR07-64_after-action_edge.png`, `evidence/TC-FR07-64_after-action_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)

expect(received).toEqual(expected) // deep equality

- Expected  - 8
+ Received  + 1

- Array [
-   Object {
-     "name": "Bàn phím cơ Keychron Q1",
-     "price": 4000000,
-     "qty": "1000",
-     "subtotal": 4000000000,
-   },
- ]
+ Array []

Error: số dòng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 1
Received: 0

Error: Tổng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 4000000000
Received: null
```

## G2 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: giỏ trống: có img/svg minh hoạ trong khối chứa dòng chữ giỏ trống | expect(locator).not.toHaveCount(expected) failed | Received: 0`

### TC-FR07-01 – Kiểm tra trang giỏ trống và việc quay về trang chủ khi khách chưa đăng nhập mở giỏ rỗng

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / EP
- HW02: Fail · BUG-21
- Expected (HW02, nguyên văn): Bước 3: không có bảng sản phẩm; có hình minh hoạ/icon (img hoặc svg) và dòng chữ báo giỏ trống; badge ẩn hoặc 0. Sau thao tác: URL = http://localhost:5173/.
- Ảnh lúc kết thúc: `evidence/TC-FR07-01_chrome.png`, `evidence/TC-FR07-01_edge.png`, `evidence/TC-FR07-01_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: giỏ trống: có img/svg minh hoạ trong khối chứa dòng chữ giỏ trống

expect(locator).not.toHaveCount(expected) failed

Locator:  locator('main').getByText(/trống/i).locator('..').locator('img, svg').visible()
Expected: not 0
Received: 0
Timeout:  5000ms
```

## G3 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: B21: có phản hồi ≤ 2 s sau khi bấm thêm | expect(received).not.toBeNull() | Received: null`
- `Error: Tổng SAU | expect(received).toBe(expected) // Object.is equality | Received: null`
- `Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền) | expect(received).toEqual(expected) // deep equality | + Array []`
- `Error: số dòng SAU | expect(received).toBe(expected) // Object.is equality | Received: 0`

### TC-FR07-02 – Kiểm tra thêm sản phẩm mới với số lượng 2 từ trang chi tiết khi user đã đăng nhập và giỏ rỗng

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / EP
- HW02: Fail · BUG-15
- Expected (HW02, nguyên văn): Trong ≤ 2 giây sau khi bấm 'Thêm vào giỏ hàng': có ít nhất một phản hồi nhìn thấy được gắn với lần thêm (toast; badge đổi; chữ/trạng thái nút đổi; thông báo trên trang) — ghi loại phản hồi vào Actual (B21). TRƯỚC → SAU: 0 → 1 dòng 'Samsung Galaxy S24 Ultra', Đơn giá 28000000, Số lượng 2, Thành tiền 56000000; Tổng 56000000. Sau khi bấm link về trang chủ (giỏ có hàng): URL = http://localhost:5173/.
- Ảnh lúc kết thúc: `evidence/TC-FR07-02_chrome.png`, `evidence/TC-FR07-02_edge.png`, `evidence/TC-FR07-02_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-02_after-action_chrome.png`, `evidence/TC-FR07-02_after-action_edge.png`, `evidence/TC-FR07-02_after-action_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: B21: có phản hồi ≤ 2 s sau khi bấm thêm

expect(received).not.toBeNull()

Received: null

Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)

expect(received).toEqual(expected) // deep equality

- Expected  - 8
+ Received  + 1

- Array [
-   Object {
-     "name": "Samsung Galaxy S24 Ultra",
-     "price": 28000000,
-     "qty": "2",
-     "subtotal": 56000000,
-   },
- ]
+ Array []

Error: số dòng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 1
Received: 0

Error: Tổng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 56000000
Received: null
```

## G4 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: Tổng SAU | expect(received).toBe(expected) // Object.is equality | Received: 36000000`
- `Error: badge SAU (tổng Số lượng, B9) | expect(received).toBe(expected) // Object.is equality | Received: null`
- `Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền) | expect(received).toEqual(expected) // deep equality | +     "qty": "1", | +     "subtotal": 6000000,`

### TC-FR07-04 – Kiểm tra thêm lại sản phẩm từ trang chi tiết khi sản phẩm đã được thêm từ trang chủ và giỏ có 2 dòng

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / EP
- HW02: Fail · BUG-20
- Expected (HW02, nguyên văn): TRƯỚC → SAU: vẫn 2 dòng; 'Tai nghe AirPods Pro 2' Số lượng 1 → 3, Thành tiền SAU 18000000; dòng 'iPhone 15 Pro Max' không đổi (Số lượng, Thành tiền SAU = TRƯỚC); Tổng SAU 48000000; badge SAU 4 (tổng Số lượng, B9).
- Ảnh lúc kết thúc: `evidence/TC-FR07-04_chrome.png`, `evidence/TC-FR07-04_edge.png`, `evidence/TC-FR07-04_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-04_after-action_chrome.png`, `evidence/TC-FR07-04_after-action_edge.png`, `evidence/TC-FR07-04_after-action_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: các dòng giỏ SAU (tên, Đơn giá, Số lượng, Thành tiền)

expect(received).toEqual(expected) // deep equality

- Expected  - 2
+ Received  + 2

@@ -6,9 +6,9 @@
      "subtotal": 30000000,
    },
    Object {
      "name": "Tai nghe AirPods Pro 2",
      "price": 6000000,
-     "qty": "3",
-     "subtotal": 18000000,
+     "qty": "1",
+     "subtotal": 6000000,
    },
  ]

Error: Tổng SAU

expect(received).toBe(expected) // Object.is equality

Expected: 48000000
Received: 36000000

Error: badge SAU (tổng Số lượng, B9)

expect(received).toBe(expected) // Object.is equality

Expected: 4
Received: null
```

## G5 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: hiện dialog xác nhận sau khi bấm xoá | hiện dialog xác nhận sau khi bấm xoá | Received: 0`

### TC-FR07-08 – Kiểm tra xoá một dòng và xác nhận trong dialog khi giỏ có 2 dòng

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / EP
- HW02: Fail · BUG-19
- Expected (HW02, nguyên văn): Sau khi bấm nút xoá: hiện dialog xác nhận; dòng chưa bị xoá khi dialog đang mở. Sau khi xác nhận: TRƯỚC → SAU: 2 → 1 dòng; không còn 'Tai nghe AirPods Pro 2'; dòng 'Bàn phím cơ Keychron Q1' không đổi; Tổng SAU 4000000 (= Thành tiền dòng còn lại).
- Ảnh lúc kết thúc: `evidence/TC-FR07-08_chrome.png`, `evidence/TC-FR07-08_edge.png`, `evidence/TC-FR07-08_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-08_after-action_chrome.png`, `evidence/TC-FR07-08_after-action_edge.png`, `evidence/TC-FR07-08_after-action_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: hiện dialog xác nhận sau khi bấm xoá

hiện dialog xác nhận sau khi bấm xoá

expect(received).toBe(expected) // Object.is equality

Expected: 1
Received: 0

Call Log:
- Timeout 2000ms exceeded while waiting on the predicate
```

## G6 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: B21: có phản hồi ≤ 2 s sau khi bấm thêm | expect(received).not.toBeNull() | Received: null`
- `Error: lần 1: Số lượng id 5 | expect(received).toEqual(expected) // deep equality | + Array []`
- `Error: lần 1: có dòng id 5 | expect(locator).toHaveCount(expected) failed | Received: 0`
- `Error: lần 2: Số lượng id 5 | expect(received).toEqual(expected) // deep equality | + Array []`
- `Error: lần 2: có dòng id 5 | expect(locator).toHaveCount(expected) failed | Received: 0`
- `Error: lần 2: số dòng | expect(locator).toHaveCount(expected) failed | Received: 0`

### TC-FR07-205 – Kiểm tra đổi Số lượng giữa hai lần bấm 'Thêm vào giỏ hàng' ở trang chi tiết

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive (AI suy ra, SV duyệt) / EG
- HW02: Fail · BUG-15
- Expected (HW02, nguyên văn): Sau lần 1: id 5 × 2 và có phản hồi trong ≤ 2 s (B21). Sau lần 2: 1 dòng id 5 × 7 (FR-07.3).
- Ảnh lúc kết thúc: `evidence/TC-FR07-205_chrome.png`, `evidence/TC-FR07-205_edge.png`, `evidence/TC-FR07-205_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR07-205_after-action-1_chrome.png`, `evidence/TC-FR07-205_after-action-2_chrome.png`, `evidence/TC-FR07-205_after-action-1_edge.png`, `evidence/TC-FR07-205_after-action-2_edge.png`, `evidence/TC-FR07-205_after-action-1_firefox.png`, `evidence/TC-FR07-205_after-action-2_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: B21: có phản hồi ≤ 2 s sau khi bấm thêm

expect(received).not.toBeNull()

Received: null

Error: lần 1: có dòng id 5

expect(locator).toHaveCount(expected) failed

Locator:  locator('main table tbody tr').filter({ has: locator('td').filter({ hasText: 'Bàn phím cơ Keychron Q1' }) })
Expected: 1
Received: 0
Timeout:  5000ms

Error: lần 1: Số lượng id 5

expect(received).toEqual(expected) // deep equality

- Expected  - 3
+ Received  + 1

- Array [
-   "2",
- ]
+ Array []

Error: lần 2: có dòng id 5

expect(locator).toHaveCount(expected) failed

Locator:  locator('main table tbody tr').filter({ has: locator('td').filter({ hasText: 'Bàn phím cơ Keychron Q1' }) })
Expected: 1
Received: 0
Timeout:  5000ms

Error: lần 2: Số lượng id 5

expect(received).toEqual(expected) // deep equality

- Expected  - 3
+ Received  + 1

- Array [
-   "7",
- ]
+ Array []

Error: lần 2: số dòng

expect(locator).toHaveCount(expected) failed

Locator:  locator('main table tbody tr')
Expected: 1
Received: 0
Timeout:  5000ms
```

