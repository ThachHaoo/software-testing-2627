# Dữ kiện Fail — FR-07 Giỏ hàng (B_FR07)

> Dữ kiện do AI gom, chưa phải bug report; SV quyết định gộp/tách.
> Nhãn nhóm chỉ mô tả triệu chứng quan sát được (tầng + quan sát). Không có tên bug, severity, priority hay nguyên nhân.
> Nguồn: `HW02/B_FR07/testcases.json` sau commit 6/7b (lượt chính thức = lượt 2). Đoạn code chỉ trích nguyên văn để SV đối chiếu, không bình luận.

**Trước khi tái hiện:** khởi động lại backend (`node server.js`); giỏ web là state React — không tải lại trang giữa các bước.

## Tổng hợp

| Nhóm | Khung | Số Fail | Số Blocked ghi case gốc | Yêu cầu / giả định |
|---|---|---|---|---|
| G1 | BUG-15 | 6 | 5 | FR-06.2, FR-07.1, FR-08.1, FR-07.5, FR-06.3, FR-24.1, B1, FR-07.3, B21 |
| G2 | BUG-16 | 1 | 0 | FR-06.3, FR-24.1 |
| G3 | BUG-17 | 1 | 0 | FR-07.3, B4 |
| G4 | BUG-18 | 1 | 4 | FR-07.2 |
| G5 | BUG-19 | 1 | 1 | FR-07.4, FR-24.2, FR-07.1 |
| G6 | BUG-20 | 1 | 0 | FR-07.3, FR-07.1, FR-23.2 |
| G7 | BUG-21 | 1 | 0 | FR-07.7, FR-07.5, FR-23.2, FR-24.3 |
| G8 | BUG-22 | 1 | 0 | FR-23.4 |
| G9 | BUG-23 | 1 | 0 | FR-23.1 |
| G10 | BUG-24 | 1 | 0 | FR-21.3, B13 |
| G11 | BUG-25 | 1 | 0 | FR-24.4 |
| G12 | BUG-26 | 1 | 0 | FR-07.1 |
| G13 | BUG-27 | 1 | 0 | FR-07.4, B12 |
| G14 | BUG-28 | 1 | 0 | FR-07.5, B12 |
| G15 | BUG-29 | 1 | 0 | FR-07.6 |
| G16 | BUG-30 | 1 | 1 | FR-07.3, API-CART |
| G17 | BUG-31 | 2 | 0 | FR-08.2, API-CART, B8 |
| G18 | BUG-32 | 8 | 0 | FR-06.2, API-CART |
| G19 | BUG-33 | 5 | 0 | API-CART |
| G20 | BUG-34 | 1 | 0 | API-CART |
| G21 | BUG-35 | 1 | 0 | API-CART |
| G22 | BUG-36 | 1 | 0 | FR-06.2, API-CART, B1 |

Tổng Fail: 39 (đủ, mỗi Fail đúng một nhóm). Blocked: TC-FR07-06 và 65 có hai case gốc (TC-61, TC-90) nên ghi ở G1 và G4.

## Kiểm trùng issue

`gh issue list -R tkob-team/eshop-sut --state all` (69 issue, mọi tác giả, gồm đã đóng) và BUG-01…14 (A_FR01). Tìm theo: giỏ/cart, /api/cart, CartContext/Cart.jsx, trang chi tiết/ProductDetail, badge, alt, ₫/VND, breadcrumb.

| Nhóm | Issue có thể liên quan | Dữ kiện |
|---|---|---|
| G18 (quantity API), G17 (price API) | #14 [BUG-FR08-05] | Bước 1 của #14 gọi `POST /api/cart` với quantity -1 (lặp 0, 1.5, "abc"; price 0, -4000000, "abc"); kết luận của #14 nói về `POST /api/checkout` tạo đơn. |
| G17 (price API) | #10 [BUG-FR08-01] | #10 nói về `total_amount` client gửi ở checkout, không phải price trong giỏ. |
| G1, G18 | #47 [BUG-D01] | Mobile (productDetail) nhận quantity không hợp lệ khi Add — nền tảng khác (frontend-mobile). |
| G20, G21 | #25, #26 (BUG-09, BUG-10 của A_FR01) | Cùng dạng 'lỗi trả trang HTML' nhưng endpoint `/api/register`; #26 là text/plain → 500, G21 là text/plain → 200. |

Không thấy issue nào về: trang chi tiết không thêm vào giỏ, badge, highlight navbar, breadcrumb, alt, 'VND', nhãn trang giỏ, nút +/-, dialog xoá, cộng dồn.

## G1 — UI · trang chi tiết: bấm 'Thêm vào giỏ hàng' một lần với Số lượng hợp lệ → giỏ không có dòng mới; không có phản hồi nhìn thấy được trong 2 s

- **TC Fail (6):** 02, 61, 62, 63, 64, 205
- **Blocked ghi case gốc (5):** 03, 06, 65, 203, 206
- **Yêu cầu / giả định:** FR-06.2, FR-07.1, FR-08.1, FR-07.5, FR-06.3, FR-24.1, B1, FR-07.3, B21
- **Actual tiêu biểu (TC-FR07-02, nguyên văn):** đăng nhập cart02_1792476866046@domain.com: navbar có tên user; TRƯỚC: không có bảng (giỏ trống); ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: không có bảng (giỏ trống); URL sau khi bấm link về trang chủ=http://localhost:5173/
- **Actual các case còn lại (rút gọn 200 ký tự):**
  - TC-FR07-61: đăng nhập cart61_1792476918630@domain.com: navbar có tên user; TRƯỚC: không có bảng (giỏ trống); ô Số lượng sau khi gõ "1": value="1"; không có phản hồi nhìn thấy được trong 2 s; SAU: không có bảng (g
  - TC-FR07-62: đăng nhập cart62_1792476923019@domain.com: navbar có tên user; TRƯỚC: không có bảng (giỏ trống); ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: không có bảng (g
  - TC-FR07-63: đăng nhập cart63_1792476927256@domain.com: navbar có tên user; TRƯỚC: không có bảng (giỏ trống); ô Số lượng sau khi gõ "5": value="5"; không có phản hồi nhìn thấy được trong 2 s; SAU: không có bảng (g
  - TC-FR07-64: đăng nhập cart64_1792476931447@domain.com: navbar có tên user; TRƯỚC: không có bảng (giỏ trống); ô Số lượng sau khi gõ "1000": value="1000"; không có phản hồi nhìn thấy được trong 2 s; SAU: không có b
  - TC-FR07-205: TRƯỚC: không có bảng (giỏ trống); lần 1: value="2"; lần 1: không có phản hồi nhìn thấy được trong 2 s; sau lần 1: không có bảng (giỏ trống); lần 2: value="5"; sau lần 2: không có bảng (giỏ trống)
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-02_failed.png`, `HW02/B_FR07/evidence/TC-FR07-02_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-02_ui.png`, `HW02/B_FR07/evidence/TC-FR07-61_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-61_ui.png`, `HW02/B_FR07/evidence/TC-FR07-62_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-62_ui.png`, `HW02/B_FR07/evidence/TC-FR07-63_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-63_ui.png`, `HW02/B_FR07/evidence/TC-FR07-64_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-64_ui.png`, `HW02/B_FR07/evidence/TC-FR07-205_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-205_ui-lan1.png`
- Pass hộp đen ghi case gốc TC-FR07-61 (notes 6b): TC-FR07-10, 11, 12, 13, 60, 200.
- TC-FR07-04 (xếp ở nhóm badge) cũng ghi SAU = TRƯỚC sau khi thêm từ trang chi tiết; notes: EC10 chưa đánh giá được, case gốc TC-FR07-61.
- TC-FR07-205 notes (SV): lần 1 không thêm, khớp giả thuyết gray-box ProductDetail.jsx:21–31.

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/ProductDetail.jsx` dòng 21–31:

```jsx
  21    const handleAddToCart = () => {
  22      if (clickCount === 0) {
  23        setClickCount(1);
  24        return; // Không làm gì cả ở lần đầu tiên
  25      }
  26  
  27      addToCart(product, parseInt(quantity));
  28      setAdded(true);
  29      setClickCount(0); // Reset lại
  30      setTimeout(() => setAdded(false), 2000);
  31    };
```

## G2 — UI · trang chủ: bấm 'Thêm vào giỏ' trên thẻ sản phẩm → không có phản hồi nhìn thấy được trong 2 s (toast, badge, chữ/trạng thái nút, thông báo)

- **TC Fail (1):** 99
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-06.3, FR-24.1
- **Actual tiêu biểu (TC-FR07-99, nguyên văn):** không có phản hồi nhìn thấy được trong 2 s
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-99_failed.png`, `HW02/B_FR07/evidence/TC-FR07-99_feedback.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Home.jsx` dòng 97–102:

```jsx
  97                  <button
  98                    onClick={() => addToCart({ ...p, quantity: 1 }, 1)}
  99                    className="flex-1 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 text-sm"
 100                  >
 101                    Thêm vào giỏ
 102                  </button>
```

`frontend-web/src/App.jsx` dòng 23:

```jsx
  23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
```

## G3 — UI · trang chủ: bấm 'Thêm vào giỏ' cùng sản phẩm 20 lần → trang giỏ có 20 dòng riêng, mỗi dòng Số lượng 1 (không cộng dồn)

- **TC Fail (1):** 201
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-07.3, B4
- **Actual tiêu biểu (TC-FR07-201, nguyên văn):** TRƯỚC: không có bảng (giỏ trống); bấm 20 lần (element.click() trong trang) trong 410 ms [notes] thời gian thực tế 410 ms > 400 ms của cột Thao tác; SAU: 20 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Tai nghe Ai
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-201_failed.png`, `HW02/B_FR07/evidence/TC-FR07-201_ui.png`
- Thời gian bấm thực tế 405 ms (lượt 2), 410 ms (lượt 3) so với 400 ms của cột Thao tác; notes SV: không ảnh hưởng kết luận.
- Tầng API cùng dạng quan sát: nhóm API 'POST cùng id → phần tử mới' (TC-FR07-21).

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/context/CartContext.jsx` dòng 8–10:

```jsx
   8    const addToCart = (product, quantity) => {
   9      setCart([...cart, { ...product, quantity }]);
  10    };
```

## G4 — UI · trang giỏ: ô Số lượng của dòng không có nút '+' / '-'

- **TC Fail (1):** 90
- **Blocked ghi case gốc (4):** 05, 06, 07, 65
- **Yêu cầu / giả định:** FR-07.2
- **Actual tiêu biểu (TC-FR07-90, nguyên văn):** dòng: 1 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 6000000; không có badge; nút trong ô Số lượng: []
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-90_ui.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 47:

```jsx
  47                <td>{item.quantity}</td>
```

## G5 — UI · trang giỏ: bấm nút xoá → không có dialog xác nhận, dòng bị xoá ngay

- **TC Fail (1):** 08
- **Blocked ghi case gốc (1):** 09
- **Yêu cầu / giả định:** FR-07.4, FR-24.2, FR-07.1
- **Actual tiêu biểu (TC-FR07-08, nguyên văn):** đăng nhập cart08_1792476880905@domain.com: navbar có tên user; TRƯỚC: 2 dòng: [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000] [Bàn phím cơ Keychron Q1 | Đơn giá 4000000 | SL 1 | Thành tiền 4000000]; Tổng 10000000; không có badge; không có dialog; SAU: 1 dòng: [Bàn phím cơ Keychron Q1 | Đơn giá 4000000 | SL 1 | Thành tiền 4000000]; Tổng 4000000; không có badge
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-08_ui.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 49–55:

```jsx
  49                <td>
  50                  <button
  51                    onClick={() => removeFromCart(index)}
  52                    className="text-red-500 hover:text-red-700"
  53                  >
  54                    Xóa
  55                  </button>
```

`frontend-web/src/context/CartContext.jsx` dòng 12–16:

```jsx
  12    const removeFromCart = (index) => {
  13      const newCart = [...cart];
  14      newCart.splice(index, 1);
  15      setCart(newCart);
  16    };
```

## G6 — UI · navbar: không có badge số lượng trên/cạnh link tới /cart khi giỏ có hàng

- **TC Fail (1):** 04
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-07.3, FR-07.1, FR-23.2
- **Actual tiêu biểu (TC-FR07-04, nguyên văn):** đăng nhập cart04_1792476872458@domain.com: navbar có tên user; TRƯỚC: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge; ô Số lượng sau khi gõ "2": value="2"; không có phản hồi nhìn thấy được trong 2 s; SAU: 2 dòng: [iPhone 15 Pro Max | Đơn giá 30000000 | SL 1 | Thành tiền 30000000] [Tai nghe AirPods Pro 2 | Đơn giá 6000000 | SL 1 | Thành tiền 6000000]; Tổng 36000000; không có badge
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-04_feedback.png`, `HW02/B_FR07/evidence/TC-FR07-04_ui.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/App.jsx` dòng 23:

```jsx
  23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
```

## G7 — UI · trang giỏ trống: không có hình minh hoạ/icon (img/svg)

- **TC Fail (1):** 01
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-07.7, FR-07.5, FR-23.2, FR-24.3
- **Actual tiêu biểu (TC-FR07-01, nguyên văn):** TRƯỚC: không có bảng (giỏ trống); trạng thái trống: bảng=không, ảnh/icon=không, chữ="Giỏ hàng của bạn đang trốngTiếp tục mua sắm"; URL sau thao tác=http://localhost:5173/
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-01_failed.png`, `HW02/B_FR07/evidence/TC-FR07-01_ui.png`
- Cùng case: dòng chữ 'Giỏ hàng của bạn đang trống' có; link về trang chủ → URL '/' đạt.

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 20–27:

```jsx
  20    if (cart.length === 0) {
  21      return (
  22        <div className="text-center mt-10">
  23          <h2 className="text-2xl mb-4">Giỏ hàng của bạn đang trống</h2>
  24          <Link to="/" className="text-blue-600 hover:underline">Tiếp tục mua sắm</Link>
  25        </div>
  26      );
  27    }
```

## G8 — UI · trang giỏ: không có breadcrumb ở vùng nội dung chính

- **TC Fail (1):** 91
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-23.4
- **Actual tiêu biểu (TC-FR07-91, nguyên văn):** không tìm thấy breadcrumb ở vùng nội dung chính
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-91_ui.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 29–31:

```jsx
  29    return (
  30      <div className="bg-white p-6 border rounded shadow-sm">
  31        <h2 className="text-2xl font-bold mb-6">Giỏ Hàng</h2>
```

## G9 — UI · navbar: link tới /cart có kiểu hiển thị giống các link khác khi đang ở /cart (không highlight)

- **TC Fail (1):** 92
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-23.1
- **Actual tiêu biểu (TC-FR07-92, nguyên văn):** ở /cart: [{"href":"/cart","text":"Giỏ hàng","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/login","text":"Đăng nhập","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/register","text":"Đăng ký","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"}]; ở trang chủ: [{"href":"/cart","text":"Giỏ hàng","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/login","text":"Đăng nhập","style":"rgb(255, 255, 255) | none | rgba(0, 0, 0, 0) | 400 | 0px solid"},{"href":"/register","text":
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-92_failed.png`, `HW02/B_FR07/evidence/TC-FR07-92_ui-cart.png`, `HW02/B_FR07/evidence/TC-FR07-92_ui-home.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/App.jsx` dòng 21–24:

```jsx
  21        <Link to="/" className="text-2xl font-bold">EShop</Link>
  22        <nav className="flex gap-4 items-center">
  23          <Link to="/cart" className="hover:underline">Giỏ hàng</Link>
  24          {user ? (
```

## G10 — UI · trang chủ: giá trên thẻ sản phẩm hiển thị đơn vị 'VND' thay vì '₫'

- **TC Fail (1):** 93
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-21.3, B13
- **Actual tiêu biểu (TC-FR07-93, nguyên văn):** locale trình duyệt=vi-VN; trang chủ (thẻ)="6.000.000 VND"; trang chi tiết="6.000.000 ₫"; giỏ: Đơn giá="6.000.000 ₫"; giỏ: Thành tiền="6.000.000 ₫"; giỏ: Tổng="6.000.000 ₫"
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-93_ui.png`
- Cùng case: trang chi tiết và trang giỏ dùng '₫' (đạt).

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Home.jsx` dòng 86–88:

```jsx
  86                <p className="text-red-500 font-bold mb-2">
  87                  {Number(p.price).toLocaleString()} VND
  88                </p>
```

## G11 — UI · trang chủ: ảnh sản phẩm có alt rỗng (5/5 ảnh)

- **TC Fail (1):** 94
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-24.4
- **Actual tiêu biểu (TC-FR07-94, nguyên văn):** alt trang chủ=["","","","",""]; alt trang chi tiết=["Tai nghe AirPods Pro 2"]; trang giỏ không có ảnh sản phẩm (notes, không tính Fail); [kiểm tay] alt "mô tả nội dung ảnh": SV đối chiếu chữ alt với ảnh
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-94_ui.png`
- Cùng case: trang chi tiết alt = tên sản phẩm (đạt); trang giỏ không có ảnh.
- Notes SV: evidence kiểm tay cần chụp lại trong cửa sổ ẩn danh không tiện ích.

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Home.jsx` dòng 80–84:

```jsx
  80                <img
  81                  src={p.imageUrl}
  82                  alt=""
  83                  className="w-full h-48 object-cover mb-4 rounded"
  84                />
```

## G12 — UI · trang giỏ: tiêu đề cột thứ 2 là 'Giá' (SRS: 'Đơn giá')

- **TC Fail (1):** 95
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-07.1
- **Actual tiêu biểu (TC-FR07-95, nguyên văn):** nhãn đọc được=["Sản phẩm","Giá","Số lượng","Thành tiền","Thao tác"]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-95_ui.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 34–40:

```jsx
  34            <tr className="border-b">
  35              <th className="py-2">Sản phẩm</th>
  36              <th className="py-2">Giá</th>
  37              <th className="py-2">Số lượng</th>
  38              <th className="py-2">Thành tiền</th>
  39              <th className="py-2">Thao tác</th>
  40            </tr>
```

## G13 — UI · trang giỏ: nút xoá trên dòng có chữ 'Xóa' (SRS: 'Xóa sản phẩm')

- **TC Fail (1):** 96
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-07.4, B12
- **Actual tiêu biểu (TC-FR07-96, nguyên văn):** nhãn đọc được=["Xóa"]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-96_ui.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 50–55:

```jsx
  50                  <button
  51                    onClick={() => removeFromCart(index)}
  52                    className="text-red-500 hover:text-red-700"
  53                  >
  54                    Xóa
  55                  </button>
```

## G14 — UI · trang giỏ: link về trang chủ có chữ '← Mua tiếp' (SRS: 'Tiếp tục mua sắm')

- **TC Fail (1):** 97
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-07.5, B12
- **Actual tiêu biểu (TC-FR07-97, nguyên văn):** nhãn đọc được=["← Mua tiếp"]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-97_ui.png`
- Trang giỏ trống có link 'Tiếp tục mua sắm' (Cart.jsx dòng 24); TC-FR07-97 kiểm khi giỏ có 1 dòng.

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 65–68:

```jsx
  65          <div className="flex gap-3">
  66            <Link to="/" className="border px-4 py-2 rounded text-gray-600 hover:bg-gray-50">
  67              ← Mua tiếp
  68            </Link>
```

## G15 — UI · trang giỏ: nhãn dòng tổng là 'Tổng tạm tính:' (SRS: 'Tổng cộng')

- **TC Fail (1):** 98
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-07.6
- **Actual tiêu biểu (TC-FR07-98, nguyên văn):** nhãn đọc được=["Tổng tạm tính:"]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-98_ui.png`

**Đoạn code liên quan (trích nguyên văn):**

`frontend-web/src/pages/Cart.jsx` dòng 62–64:

```jsx
  62          <div className="text-xl font-bold">
  63            Tổng tạm tính: <span className="text-red-600">{cartTotal.toLocaleString()} ₫</span>
  64          </div>
```

## G16 — API · POST /api/cart cùng id đã có trong giỏ → HTTP 200, GET có thêm phần tử mới thay vì cộng quantity

- **TC Fail (1):** 21
- **Blocked ghi case gốc (1):** 213
- **Yêu cầu / giả định:** FR-07.3, API-CART
- **Actual tiêu biểu (TC-FR07-21, nguyên văn):** POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1}]; SAU: [{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":1},{"id":2,"name":"Samsung Galaxy S24 Ultra","price":28000000,"quantity":3}]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-21_api.png`, `HW02/B_FR07/evidence/TC-FR07-21_req.json`, `HW02/B_FR07/evidence/TC-FR07-21_res.json`
- TC-FR07-213: 50 POST song song → 50×HTTP 200, GET SAU 50 phần tử id 1 quantity 1 (Blocked, case gốc TC-FR07-21).
- Tầng UI cùng dạng quan sát: nhóm 'bấm 20 lần → 20 dòng' (TC-FR07-201).

**Đoạn code liên quan (trích nguyên văn):**

`backend/server.js` dòng 290–295:

```js
 290  app.post("/api/cart", authenticateToken, (req, res) => {
 291    const userId = req.user.id;
 292    if (!userCarts[userId]) userCarts[userId] = [];
 293    userCarts[userId].push(req.body);
 294    res.json({ message: "Added to cart" });
 295  });
```

## G17 — API · POST /api/cart với price khác giá CSDL → HTTP 200, GET lưu đúng price client gửi

- **TC Fail (2):** 22, 210
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-08.2, API-CART, B8
- **Actual tiêu biểu (TC-FR07-22, nguyên văn):** POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":1},{"id":4,"name":"Tai nghe AirPods Pro 2","price":1,"quantity":1}]
- **Actual các case còn lại (rút gọn 200 ký tự):**
  - TC-FR07-210: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":2,"
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-22_api.png`, `HW02/B_FR07/evidence/TC-FR07-22_req.json`, `HW02/B_FR07/evidence/TC-FR07-22_res.json`, `HW02/B_FR07/evidence/TC-FR07-210_api.png`, `HW02/B_FR07/evidence/TC-FR07-210_req.json`, `HW02/B_FR07/evidence/TC-FR07-210_res.json`

**Đoạn code liên quan (trích nguyên văn):**

`backend/server.js` dòng 290–295:

```js
 290  app.post("/api/cart", authenticateToken, (req, res) => {
 291    const userId = req.user.id;
 292    if (!userCarts[userId]) userCarts[userId] = [];
 293    userCarts[userId].push(req.body);
 294    res.json({ message: "Added to cart" });
 295  });
```

## G18 — API · POST /api/cart với quantity không hợp lệ (≤ 0, thập phân, chuỗi, thiếu) → HTTP 200, GET có phần tử mới mang quantity đó

- **TC Fail (8):** 30, 31, 32, 33, 34, 35, 70, 208
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-06.2, API-CART
- **Actual tiêu biểu (TC-FR07-30, nguyên văn):** POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":-3}]
- **Actual các case còn lại (rút gọn 200 ký tự):**
  - TC-FR07-31: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"
  - TC-FR07-32: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"
  - TC-FR07-33: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"
  - TC-FR07-34: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"
  - TC-FR07-35: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"
  - TC-FR07-70: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"
  - TC-FR07-208: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":5,"
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-30_api.png`, `HW02/B_FR07/evidence/TC-FR07-30_req.json`, `HW02/B_FR07/evidence/TC-FR07-30_res.json`, `HW02/B_FR07/evidence/TC-FR07-31_api.png`, `HW02/B_FR07/evidence/TC-FR07-31_req.json`, `HW02/B_FR07/evidence/TC-FR07-31_res.json`, `HW02/B_FR07/evidence/TC-FR07-32_api.png`, `HW02/B_FR07/evidence/TC-FR07-32_req.json`, `HW02/B_FR07/evidence/TC-FR07-32_res.json`, `HW02/B_FR07/evidence/TC-FR07-33_api.png`, `HW02/B_FR07/evidence/TC-FR07-33_req.json`, `HW02/B_FR07/evidence/TC-FR07-33_res.json`, `HW02/B_FR07/evidence/TC-FR07-34_api.png`, `HW02/B_FR07/evidence/TC-FR07-34_req.json`, `HW02/B_FR07/evidence/TC-FR07-34_res.json`, `HW02/B_FR07/evidence/TC-FR07-35_api.png`, `HW02/B_FR07/evidence/TC-FR07-35_req.json`, `HW02/B_FR07/evidence/TC-FR07-35_res.json`, `HW02/B_FR07/evidence/TC-FR07-70_api.png`, `HW02/B_FR07/evidence/TC-FR07-70_req.json`, `HW02/B_FR07/evidence/TC-FR07-70_res.json`, `HW02/B_FR07/evidence/TC-FR07-208_api.png`, `HW02/B_FR07/evidence/TC-FR07-208_req.json`, `HW02/B_FR07/evidence/TC-FR07-208_res.json`

**Đoạn code liên quan (trích nguyên văn):**

`backend/server.js` dòng 290–295:

```js
 290  app.post("/api/cart", authenticateToken, (req, res) => {
 291    const userId = req.user.id;
 292    if (!userCarts[userId]) userCarts[userId] = [];
 293    userCarts[userId].push(req.body);
 294    res.json({ message: "Added to cart" });
 295  });
```

## G19 — API · POST /api/cart với id không hợp lệ (không tồn tại, chuỗi, mảng, object, thiếu) → HTTP 200, GET có phần tử mới mang id đó

- **TC Fail (5):** 36, 37, 40, 211, 212
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** API-CART
- **Actual tiêu biểu (TC-FR07-36, nguyên văn):** POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":99999,"name":"Không tồn tại","price":1000,"quantity":1}]
- **Actual các case còn lại (rút gọn 200 ký tự):**
  - TC-FR07-37: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":"ab
  - TC-FR07-40: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"name":"
  - TC-FR07-211: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":[1,
  - TC-FR07-212: POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1},{"id":{"i
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-36_api.png`, `HW02/B_FR07/evidence/TC-FR07-36_req.json`, `HW02/B_FR07/evidence/TC-FR07-36_res.json`, `HW02/B_FR07/evidence/TC-FR07-37_api.png`, `HW02/B_FR07/evidence/TC-FR07-37_req.json`, `HW02/B_FR07/evidence/TC-FR07-37_res.json`, `HW02/B_FR07/evidence/TC-FR07-40_api.png`, `HW02/B_FR07/evidence/TC-FR07-40_req.json`, `HW02/B_FR07/evidence/TC-FR07-40_res.json`, `HW02/B_FR07/evidence/TC-FR07-211_api.png`, `HW02/B_FR07/evidence/TC-FR07-211_req.json`, `HW02/B_FR07/evidence/TC-FR07-211_res.json`, `HW02/B_FR07/evidence/TC-FR07-212_api.png`, `HW02/B_FR07/evidence/TC-FR07-212_req.json`, `HW02/B_FR07/evidence/TC-FR07-212_res.json`

**Đoạn code liên quan (trích nguyên văn):**

`backend/server.js` dòng 290–295:

```js
 290  app.post("/api/cart", authenticateToken, (req, res) => {
 291    const userId = req.user.id;
 292    if (!userCarts[userId]) userCarts[userId] = [];
 293    userCarts[userId].push(req.body);
 294    res.json({ message: "Added to cart" });
 295  });
```

## G20 — API · POST /api/cart body không phải JSON hợp lệ (quantity: Infinity) → HTTP 400 trả trang HTML (stack trace), không có trường error; giỏ không đổi

- **TC Fail (1):** 209
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** API-CART
- **Actual tiêu biểu (TC-FR07-209, nguyên văn):** POST HTTP 400 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot;uant; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-209_api.png`, `HW02/B_FR07/evidence/TC-FR07-209_req.json`, `HW02/B_FR07/evidence/TC-FR07-209_res.json`
- Lượt 1 gửi sai body do script (Playwright tự JSON.stringify); lượt 2, 3 gửi đúng chuỗi thô — kết quả trùng nhau.
- Body HTML có đường dẫn tuyệt đối trên máy chạy (node_modules\body-parser) — evidence gốc giữ nguyên (quy ước: bản dán issue che đặt ở `HW02/bugs/_issue_redacted/`).

**Đoạn code liên quan (trích nguyên văn):**

`backend/server.js` dòng 12:

```js
  12  app.use(bodyParser.json());
```

## G21 — API · POST /api/cart với Content-Type: text/plain (body JSON hợp lệ) → HTTP 200, GET có phần tử null

- **TC Fail (1):** 214
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** API-CART
- **Actual tiêu biểu (TC-FR07-214, nguyên văn):** POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: []; SAU: [null]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-214_api.png`, `HW02/B_FR07/evidence/TC-FR07-214_req.json`, `HW02/B_FR07/evidence/TC-FR07-214_res.json`

**Đoạn code liên quan (trích nguyên văn):**

`backend/server.js` dòng 12:

```js
  12  app.use(bodyParser.json());
```

`backend/server.js` dòng 290–295:

```js
 290  app.post("/api/cart", authenticateToken, (req, res) => {
 291    const userId = req.user.id;
 292    if (!userCarts[userId]) userCarts[userId] = [];
 293    userCarts[userId].push(req.body);
 294    res.json({ message: "Added to cart" });
 295  });
```

## G22 — API · POST /api/cart quantity 9007199254740993 → HTTP 200, GET trả quantity 9007199254740992

- **TC Fail (1):** 215
- **Blocked ghi case gốc (0):** —
- **Yêu cầu / giả định:** FR-06.2, API-CART, B1
- **Actual tiêu biểu (TC-FR07-215, nguyên văn):** POST HTTP 200 {"message":"Added to cart"}; TRƯỚC: []; SAU: [{"id":5,"name":"Bàn phím cơ Keychron Q1","price":4000000,"quantity":9007199254740992}]
- **Evidence:** `HW02/B_FR07/evidence/TC-FR07-215_api.png`, `HW02/B_FR07/evidence/TC-FR07-215_req.json`, `HW02/B_FR07/evidence/TC-FR07-215_res.json`
- SV ghi giả định B1 (không có cận trên) cho Expected của case.

**Đoạn code liên quan (trích nguyên văn):**

`backend/server.js` dòng 12:

```js
  12  app.use(bodyParser.json());
```

`backend/server.js` dòng 290–295:

```js
 290  app.post("/api/cart", authenticateToken, (req, res) => {
 291    const userId = req.user.id;
 292    if (!userCarts[userId]) userCarts[userId] = [];
 293    userCarts[userId].push(req.body);
 294    res.json({ message: "Added to cart" });
 295  });
```

