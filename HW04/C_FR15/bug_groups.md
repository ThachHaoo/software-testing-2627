# C_FR15 – nhóm TC Fail (dữ kiện, SV viết bug)

Nhóm = cùng tập assertion lỗi và cùng giá trị nhận được (triệu chứng giống hệt; số dài `{ts}` chuẩn hoá).
Không đặt tên bug, không severity/priority, không kết luận nguyên nhân, không đề xuất gộp/tách.
Ảnh lúc kết thúc = screenshot Playwright chụp lúc test KẾT THÚC (screenshot: 'only-on-failure'), không phải lúc assertion đầu tiên lỗi.
Ảnh ngay sau thao tác chính = ảnh spec tự đính (`<TC>_after-submit` / `<TC>_after-action[-k]`) ngay sau bấm Đăng Ký / Thêm / Xoá.

## G1 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: dòng của M: 'Giá' (so giá trị số) | expect(received).toBe(expected) // Object.is equality | Received: 1000000`
- `Error: mọi dòng khác SAU_UI = TRƯỚC_UI | expect(received).toEqual(expected) // deep equality | +     "name": "Sửa UI03 {ts}", | +     "name": "Sửa UI03 {ts}", | +     "name": "Sửa UI03 {ts}", | +     "name": "Sửa UI03 {ts}", | +     "name": "Sửa UI03 {ts}",`

### TC-FR15-03 – Kiểm tra sửa tên, giá, danh mục của một sản phẩm qua form khi giá mới là số nguyên

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Positive / EP
- HW02: Fail · BUG-45
- Expected (HW02, nguyên văn): Không đánh giá thông báo. Bảng: dòng của M hiển thị 'Tên SP' = 'Sửa UI03 {ts}', 'Giá' = 2500000 (so giá trị số); mọi dòng khác SAU_UI = TRƯỚC_UI; số dòng không đổi. Dữ liệu: M_SAU có name = 'Sửa UI03 {ts}', price = 2500000, category_id = 3 (so giá trị số).
- Ảnh lúc kết thúc: `evidence/TC-FR15-03_chrome.png`, `evidence/TC-FR15-03_edge.png`, `evidence/TC-FR15-03_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-03_after-save_chrome.png`, `evidence/TC-FR15-03_after-save_edge.png`, `evidence/TC-FR15-03_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: dòng của M: 'Giá' (so giá trị số)

expect(received).toBe(expected) // Object.is equality

Expected: 2500000
Received: 1000000

Error: mọi dòng khác SAU_UI = TRƯỚC_UI

expect(received).toEqual(expected) // deep equality

- Expected  - 5
+ Received  + 5

  Array [
    Object {
-     "name": "iPhone 15 Pro Max",
+     "name": "Sửa UI03 1794903107473",
      "price": 30000000,
      "priceRaw": "30000000 ₫",
    },
    Object {
-     "name": "Samsung Galaxy S24 Ultra",
+     "name": "Sửa UI03 1794903107473",
      "price": 28000000,
      "priceRaw": "28000000 ₫",
    },
    Object {
-     "name": "MacBook Pro M3",
+     "name": "Sửa UI03 1794903107473",
      "price": 45000000,
      "priceRaw": "45000000 ₫",
    },
    Object {
-     "name": "Tai nghe AirPods Pro 2",
+     "name": "Sửa UI03 1794903107473",
      "price": 6000000,
      "priceRaw": "6000000 ₫",
    },
    Object {
-     "name": "Bàn phím cơ Keychron Q1",
+     "name": "Sửa UI03 1794903107473",
      "price": 4000000,
      "priceRaw": "4000000 ₫",
    },
  ]
```

## G2 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: GET /api/products SAU = TRƯỚC | expect(received).toEqual(expected) // deep equality | +   Object { | +     "category_id": 2, | +     "description": "Mô tả NN {ts}", | +     "id": 7, | +     "imageUrl": "https://placehold.co/300", | +     "name": "Tai nghe UI10 {ts}", | +     "price": -1000, | +   },`
- `Error: bảng SAU_UI = TRƯỚC_UI | expect(received).toEqual(expected) // deep equality | +   Object { | +     "name": "Tai nghe UI10 {ts}", | +     "price": -1000, | +     "priceRaw": "-1000 ₫", | +   },`
- `Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16) | expect(received).toBe(expected) // Object.is equality | Received: false`

### TC-FR15-10 – Kiểm tra thêm sản phẩm qua form khi giá âm

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative / EP
- HW02: Fail · BUG-36
- Expected (HW02, nguyên văn): Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- Ảnh lúc kết thúc: `evidence/TC-FR15-10_chrome.png`, `evidence/TC-FR15-10_edge.png`, `evidence/TC-FR15-10_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-10_after-save_chrome.png`, `evidence/TC-FR15-10_after-save_edge.png`, `evidence/TC-FR15-10_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)

expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false

Error: bảng SAU_UI = TRƯỚC_UI

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 5

@@ -22,6 +22,11 @@
    Object {
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
      "priceRaw": "4000000 ₫",
    },
+   Object {
+     "name": "Tai nghe UI10 1794903113968",
+     "price": -1000,
+     "priceRaw": "-1000 ₫",
+   },
  ]

Error: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 8

@@ -37,6 +37,14 @@
      "id": 5,
      "imageUrl": "https://placehold.co/300x300/png?text=Keychron+Q1",
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
    },
+   Object {
+     "category_id": 2,
+     "description": "Mô tả NN 1794903113968",
+     "id": 7,
+     "imageUrl": "https://placehold.co/300",
+     "name": "Tai nghe UI10 1794903113968",
+     "price": -1000,
+   },
  ]
```

## G3 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: GET /api/products SAU = TRƯỚC | expect(received).toEqual(expected) // deep equality | +   Object { | +     "category_id": 2, | +     "description": "Mô tả NN {ts}", | +     "id": 6, | +     "imageUrl": "https://placehold.co/300", | +     "name": "Tai nghe UI11 {ts}", | +     "price": "", | +   },`
- `Error: bảng SAU_UI = TRƯỚC_UI | expect(received).toEqual(expected) // deep equality | +   Object { | +     "name": "Tai nghe UI11 {ts}", | +     "price": null, | +     "priceRaw": "₫", | +   },`
- `Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16) | expect(received).toBe(expected) // Object.is equality | Received: false`

### TC-FR15-11 – Kiểm tra thêm sản phẩm qua form khi ô 'Giá tiền' để trống

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative / EP
- HW02: Fail · BUG-36
- Expected (HW02, nguyên văn): Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- Ảnh lúc kết thúc: `evidence/TC-FR15-11_chrome.png`, `evidence/TC-FR15-11_edge.png`, `evidence/TC-FR15-11_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-11_after-save_chrome.png`, `evidence/TC-FR15-11_after-save_edge.png`, `evidence/TC-FR15-11_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)

expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false

Error: bảng SAU_UI = TRƯỚC_UI

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 5

@@ -22,6 +22,11 @@
    Object {
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
      "priceRaw": "4000000 ₫",
    },
+   Object {
+     "name": "Tai nghe UI11 1794903118181",
+     "price": null,
+     "priceRaw": "₫",
+   },
  ]

Error: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 8

@@ -37,6 +37,14 @@
      "id": 5,
      "imageUrl": "https://placehold.co/300x300/png?text=Keychron+Q1",
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
    },
+   Object {
+     "category_id": 2,
+     "description": "Mô tả NN 1794903118181",
+     "id": 6,
+     "imageUrl": "https://placehold.co/300",
+     "name": "Tai nghe UI11 1794903118181",
+     "price": "",
+   },
  ]
```

## G4 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: GET /api/products SAU = TRƯỚC | expect(received).toEqual(expected) // deep equality | +     "price": -1000,`
- `Error: M_SAU = M_TRƯỚC | expect(received).toEqual(expected) // deep equality | +   "price": "-1000",`
- `Error: bảng SAU_UI = TRƯỚC_UI | expect(received).toEqual(expected) // deep equality | +     "name": "Muc tieu 15 {ts}", | +     "name": "Muc tieu 15 {ts}", | +     "name": "Muc tieu 15 {ts}", | +     "name": "Muc tieu 15 {ts}", | +     "name": "Muc tieu 15 {ts}",`

### TC-FR15-15 – Kiểm tra sửa sản phẩm qua form khi giá mới âm

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative / EP
- HW02: Fail · BUG-38
- Expected (HW02, nguyên văn): Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- Ảnh lúc kết thúc: `evidence/TC-FR15-15_chrome.png`, `evidence/TC-FR15-15_edge.png`, `evidence/TC-FR15-15_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-15_after-save_chrome.png`, `evidence/TC-FR15-15_after-save_edge.png`, `evidence/TC-FR15-15_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: bảng SAU_UI = TRƯỚC_UI

expect(received).toEqual(expected) // deep equality

- Expected  - 5
+ Received  + 5

@@ -1,28 +1,28 @@
  Array [
    Object {
-     "name": "iPhone 15 Pro Max",
+     "name": "Muc tieu 15 1794903121716",
      "price": 30000000,
      "priceRaw": "30000000 ₫",
    },
    Object {
-     "name": "Samsung Galaxy S24 Ultra",
+     "name": "Muc tieu 15 1794903121716",
      "price": 28000000,
      "priceRaw": "28000000 ₫",
    },
    Object {
-     "name": "MacBook Pro M3",
+     "name": "Muc tieu 15 1794903121716",
      "price": 45000000,
      "priceRaw": "45000000 ₫",
    },
    Object {
-     "name": "Tai nghe AirPods Pro 2",
+     "name": "Muc tieu 15 1794903121716",
      "price": 6000000,
      "priceRaw": "6000000 ₫",
    },
    Object {
-     "name": "Bàn phím cơ Keychron Q1",
+     "name": "Muc tieu 15 1794903121716",
      "price": 4000000,
      "priceRaw": "4000000 ₫",
    },
    Object {
      "name": "Muc tieu 15 1794903121716",

Error: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 1
+ Received  + 1

@@ -43,8 +43,8 @@
      "category_id": 1,
      "description": "Mô tả mục tiêu 1794903121716",
      "id": 6,
      "imageUrl": "https://placehold.co/300",
      "name": "Muc tieu 15 1794903121716",
-     "price": 1000000,
+     "price": -1000,
    },
  ]

Error: M_SAU = M_TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 1
+ Received  + 1

@@ -2,7 +2,7 @@
    "category_id": 1,
    "description": "Mô tả mục tiêu 1794903121716",
    "id": 6,
    "imageUrl": "https://placehold.co/300",
    "name": "Muc tieu 15 1794903121716",
-   "price": "1000000",
+   "price": "-1000",
  }
```

## G5 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16) | expect(received).toBe(expected) // Object.is equality | Received: false`

### TC-FR15-200 – Kiểm tra chèn XSS `<script>alert(1)</script>` vào ô 'Tên sản phẩm' ở form Thêm

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative (AI suy ra, SV duyệt) / Security (XSS)
- HW02: Fail · BUG-39
- Expected (HW02, nguyên văn): Báo lỗi; tuyệt đối không kích hoạt alert XSS (SEC-04, C21).
- Ảnh lúc kết thúc: `evidence/TC-FR15-200_chrome.png`, `evidence/TC-FR15-200_edge.png`, `evidence/TC-FR15-200_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-200_after-save_chrome.png`, `evidence/TC-FR15-200_after-save_edge.png`, `evidence/TC-FR15-200_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)

expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false
```

## G6 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: form chặn: GET /api/products SAU = TRƯỚC | expect(received).toEqual(expected) // deep equality | +   Object { | +     "category_id": 2, | +     "description": "Mô tả SV201 {ts}", | +     "id": 6, | +     "imageUrl": "https://placehold.co/300", | +     "name": "Sản phẩm E-Notation {ts}", | +     "price": 100000, | +   },`

### TC-FR15-201 – Kiểm tra nhập giá tiền dạng E-notation `1e5` vào ô 'Giá tiền'

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative (AI suy ra, SV duyệt) / Type / JS Math
- HW02: Fail · BUG-40
- Expected (HW02, nguyên văn): Form chặn do type=number.
- Ảnh lúc kết thúc: `evidence/TC-FR15-201_chrome.png`, `evidence/TC-FR15-201_edge.png`, `evidence/TC-FR15-201_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-201_after-save_chrome.png`, `evidence/TC-FR15-201_after-save_edge.png`, `evidence/TC-FR15-201_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: form chặn: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 8

@@ -37,6 +37,14 @@
      "id": 5,
      "imageUrl": "https://placehold.co/300x300/png?text=Keychron+Q1",
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
    },
+   Object {
+     "category_id": 2,
+     "description": "Mô tả SV201 1794903142316",
+     "id": 6,
+     "imageUrl": "https://placehold.co/300",
+     "name": "Sản phẩm E-Notation 1794903142316",
+     "price": 100000,
+   },
  ]
```

## G7 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: GET /api/products SAU = TRƯỚC | expect(received).toEqual(expected) // deep equality | +   Object { | +     "category_id": 2, | +     "description": "Mô tả NN {ts}", | +     "id": 7, | +     "imageUrl": "https://placehold.co/300", | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", | +     "price": 1500000, | +   },`
- `Error: bảng SAU_UI = TRƯỚC_UI | expect(received).toEqual(expected) // deep equality | +   Object { | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", | +     "price": 1500000, | +     "priceRaw": "1500000 ₫", | +   },`
- `Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16) | expect(received).toBe(expected) // Object.is equality | Received: false`

### TC-FR15-66 – Kiểm tra thêm sản phẩm qua form khi tên dài 256 ký tự (điểm UB+1)

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative / BVA UB+1
- HW02: Fail · BUG-35
- Expected (HW02, nguyên văn): Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- Ảnh lúc kết thúc: `evidence/TC-FR15-66_chrome.png`, `evidence/TC-FR15-66_edge.png`, `evidence/TC-FR15-66_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-66_after-save_chrome.png`, `evidence/TC-FR15-66_after-save_edge.png`, `evidence/TC-FR15-66_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)

expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false

Error: bảng SAU_UI = TRƯỚC_UI

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 5

@@ -22,6 +22,11 @@
    Object {
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
      "priceRaw": "4000000 ₫",
    },
+   Object {
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
+     "price": 1500000,
+     "priceRaw": "1500000 ₫",
+   },
  ]

Error: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 8

@@ -37,6 +37,14 @@
      "id": 5,
      "imageUrl": "https://placehold.co/300x300/png?text=Keychron+Q1",
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
    },
+   Object {
+     "category_id": 2,
+     "description": "Mô tả NN 1794903126004",
+     "id": 7,
+     "imageUrl": "https://placehold.co/300",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
+     "price": 1500000,
+   },
  ]
```

## G8 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: GET /api/products SAU = TRƯỚC | expect(received).toEqual(expected) // deep equality | +   Object { | +     "category_id": 2, | +     "description": "Mô tả NN {ts}", | +     "id": 6, | +     "imageUrl": "https://placehold.co/300", | +     "name": "Tai nghe BVA 67 {ts}", | +     "price": 0, | +   },`
- `Error: bảng SAU_UI = TRƯỚC_UI | expect(received).toEqual(expected) // deep equality | +   Object { | +     "name": "Tai nghe BVA 67 {ts}", | +     "price": 0, | +     "priceRaw": "0 ₫", | +   },`
- `Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16) | expect(received).toBe(expected) // Object.is equality | Received: false`

### TC-FR15-67 – Kiểm tra thêm sản phẩm qua form khi giá = 0 (điểm LB-1)

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative / BVA LB-1
- HW02: Fail · BUG-36
- Expected (HW02, nguyên văn): Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: GET /api/products SAU = TRƯỚC.
- Ảnh lúc kết thúc: `evidence/TC-FR15-67_chrome.png`, `evidence/TC-FR15-67_edge.png`, `evidence/TC-FR15-67_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-67_after-save_chrome.png`, `evidence/TC-FR15-67_after-save_edge.png`, `evidence/TC-FR15-67_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: có thông báo lỗi (bong bóng HTML5 / hộp thoại / thông báo trên trang) (C7, C16)

expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false

Error: bảng SAU_UI = TRƯỚC_UI

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 5

@@ -22,6 +22,11 @@
    Object {
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
      "priceRaw": "4000000 ₫",
    },
+   Object {
+     "name": "Tai nghe BVA 67 1794903129393",
+     "price": 0,
+     "priceRaw": "0 ₫",
+   },
  ]

Error: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 0
+ Received  + 8

@@ -37,6 +37,14 @@
      "id": 5,
      "imageUrl": "https://placehold.co/300x300/png?text=Keychron+Q1",
      "name": "Bàn phím cơ Keychron Q1",
      "price": 4000000,
    },
+   Object {
+     "category_id": 2,
+     "description": "Mô tả NN 1794903129393",
+     "id": 6,
+     "imageUrl": "https://placehold.co/300",
+     "name": "Tai nghe BVA 67 1794903129393",
+     "price": 0,
+   },
  ]
```

## G9 – 1 TC × 3 trình duyệt (3 lượt Fail)

Assertion lỗi (chung của nhóm):

- `Error: GET /api/products SAU = TRƯỚC | expect(received).toEqual(expected) // deep equality | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",`
- `Error: M_SAU = M_TRƯỚC | expect(received).toEqual(expected) // deep equality | +   "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",`
- `Error: bảng SAU_UI = TRƯỚC_UI | expect(received).toEqual(expected) // deep equality | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", | +     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",`

### TC-FR15-78 – Kiểm tra sửa sản phẩm qua form khi tên mới dài 256 ký tự (điểm UB+1)

- Trình duyệt Fail: chrome, edge, firefox
- Loại / kỹ thuật: Negative / BVA UB+1
- HW02: Fail · BUG-37
- Expected (HW02, nguyên văn): Có thông báo lỗi (bong bóng HTML5, thông báo trên trang hoặc hộp thoại trình duyệt đều tính; nội dung ghi vào Actual) (C7, C16). Bảng: SAU_UI = TRƯỚC_UI. Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- Ảnh lúc kết thúc: `evidence/TC-FR15-78_chrome.png`, `evidence/TC-FR15-78_edge.png`, `evidence/TC-FR15-78_firefox.png`
- Ảnh ngay sau thao tác chính: `evidence/TC-FR15-78_after-save_chrome.png`, `evidence/TC-FR15-78_after-save_edge.png`, `evidence/TC-FR15-78_after-save_firefox.png`
- Actual (chrome, nguyên văn assertion lỗi):

```
Error: bảng SAU_UI = TRƯỚC_UI

expect(received).toEqual(expected) // deep equality

- Expected  - 6
+ Received  + 6

  Array [
    Object {
-     "name": "iPhone 15 Pro Max",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "price": 30000000,
      "priceRaw": "30000000 ₫",
    },
    Object {
-     "name": "Samsung Galaxy S24 Ultra",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "price": 28000000,
      "priceRaw": "28000000 ₫",
    },
    Object {
-     "name": "MacBook Pro M3",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "price": 45000000,
      "priceRaw": "45000000 ₫",
    },
    Object {
-     "name": "Tai nghe AirPods Pro 2",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "price": 6000000,
      "priceRaw": "6000000 ₫",
    },
    Object {
-     "name": "Bàn phím cơ Keychron Q1",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "price": 4000000,
      "priceRaw": "4000000 ₫",
    },
    Object {
-     "name": "Muc tieu 78 1794903135130",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "price": 1000000,
      "priceRaw": "1000000 ₫",
    },
  ]

Error: GET /api/products SAU = TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 1
+ Received  + 1

@@ -42,9 +42,9 @@
    Object {
      "category_id": 1,
      "description": "Mô tả mục tiêu 1794903135130",
      "id": 8,
      "imageUrl": "https://placehold.co/300",
-     "name": "Muc tieu 78 1794903135130",
+     "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "price": 1000000,
    },
  ]

Error: M_SAU = M_TRƯỚC

expect(received).toEqual(expected) // deep equality

- Expected  - 1
+ Received  + 1

  Object {
    "category_id": 1,
    "description": "Mô tả mục tiêu 1794903135130",
    "id": 8,
    "imageUrl": "https://placehold.co/300",
-   "name": "Muc tieu 78 1794903135130",
+   "name": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "price": "1000000",
  }
```

