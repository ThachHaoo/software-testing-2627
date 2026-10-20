# BUG-42

- **ID:** BUG-42
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Client: Playwright 1.48.2 APIRequestContext (lượt 6); kiểm tái hiện bằng PowerShell 5.1 Invoke-WebRequest (7/7a)
- API PUT http://localhost:3000/api/products/:id
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 6, bắt đầu 18:53, Asia/Saigon)
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/C_FR15/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR15-35_api.png`
- TC-FR15-35: `HW02/C_FR15/evidence/TC-FR15-35_req.json`, `HW02/C_FR15/evidence/TC-FR15-35_res.json`, `HW02/C_FR15/evidence/TC-FR15-35_api.png`
- TC-FR15-36: `HW02/C_FR15/evidence/TC-FR15-36_req.json`, `HW02/C_FR15/evidence/TC-FR15-36_res.json`, `HW02/C_FR15/evidence/TC-FR15-36_api.png`, `HW02/C_FR15/evidence/TC-FR15-36_failed.png`
- TC-FR15-37: `HW02/C_FR15/evidence/TC-FR15-37_req.json`, `HW02/C_FR15/evidence/TC-FR15-37_res.json`, `HW02/C_FR15/evidence/TC-FR15-37_api.png`
- TC-FR15-38: `HW02/C_FR15/evidence/TC-FR15-38_req.json`, `HW02/C_FR15/evidence/TC-FR15-38_res.json`, `HW02/C_FR15/evidence/TC-FR15-38_api.png`
- TC-FR15-39: `HW02/C_FR15/evidence/TC-FR15-39_req.json`, `HW02/C_FR15/evidence/TC-FR15-39_res.json`, `HW02/C_FR15/evidence/TC-FR15-39_api.png`
- TC-FR15-106: `HW02/C_FR15/evidence/TC-FR15-106_req.json`, `HW02/C_FR15/evidence/TC-FR15-106_res.json`, `HW02/C_FR15/evidence/TC-FR15-106_api.png`
- TC-FR15-112: `HW02/C_FR15/evidence/TC-FR15-112_req.json`, `HW02/C_FR15/evidence/TC-FR15-112_res.json`, `HW02/C_FR15/evidence/TC-FR15-112_api.png`, `HW02/C_FR15/evidence/TC-FR15-112_failed.png`
- TC-FR15-40: `HW02/C_FR15/evidence/TC-FR15-40_req.json`, `HW02/C_FR15/evidence/TC-FR15-40_res.json`, `HW02/C_FR15/evidence/TC-FR15-40_api.png`
- TC-FR15-41: `HW02/C_FR15/evidence/TC-FR15-41_req.json`, `HW02/C_FR15/evidence/TC-FR15-41_res.json`, `HW02/C_FR15/evidence/TC-FR15-41_api.png`
- TC-FR15-42: `HW02/C_FR15/evidence/TC-FR15-42_req.json`, `HW02/C_FR15/evidence/TC-FR15-42_res.json`, `HW02/C_FR15/evidence/TC-FR15-42_api.png`
- TC-FR15-43: `HW02/C_FR15/evidence/TC-FR15-43_req.json`, `HW02/C_FR15/evidence/TC-FR15-43_res.json`, `HW02/C_FR15/evidence/TC-FR15-43_api.png`
- TC-FR15-113: `HW02/C_FR15/evidence/TC-FR15-113_req.json`, `HW02/C_FR15/evidence/TC-FR15-113_res.json`, `HW02/C_FR15/evidence/TC-FR15-113_api.png`
- TC-FR15-44: `HW02/C_FR15/evidence/TC-FR15-44_req.json`, `HW02/C_FR15/evidence/TC-FR15-44_res.json`, `HW02/C_FR15/evidence/TC-FR15-44_api.png`
- TC-FR15-45: `HW02/C_FR15/evidence/TC-FR15-45_req.json`, `HW02/C_FR15/evidence/TC-FR15-45_res.json`, `HW02/C_FR15/evidence/TC-FR15-45_api.png`
- TC-FR15-46: `HW02/C_FR15/evidence/TC-FR15-46_req.json`, `HW02/C_FR15/evidence/TC-FR15-46_res.json`, `HW02/C_FR15/evidence/TC-FR15-46_api.png`

## TC liên quan

- Fail (15): TC-FR15-35, TC-FR15-36, TC-FR15-37, TC-FR15-38, TC-FR15-39, TC-FR15-106, TC-FR15-112, TC-FR15-40, TC-FR15-41, TC-FR15-42, TC-FR15-43, TC-FR15-113, TC-FR15-44, TC-FR15-45, TC-FR15-46
- Nhóm dữ kiện: G9 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **FR-15.2:** (SRS) Tên sản phẩm: bắt buộc, tối đa 255 ký tự. — (35–39, 106, 112)
- **FR-15.3:** (SRS) Giá: bắt buộc, phải là số dương (> 0). — (40–43, 113)
- **FR-15.4:** (SRS) Danh mục: bắt buộc, phải chọn từ danh sách có sẵn. — (44–46)
- **C6 (giả định SV chốt):** (tầng API áp FR-15) API là tầng riêng, suite riêng: POST/PUT gọi trực tiếp với dữ liệu vi phạm FR-15.2–15.4 → 4xx (không 2xx, không 5xx) kèm trường error, không tạo/không đổi bản ghi; không cố định mã cụ thể.
- **C9 (giả định SV chốt):** (thiếu trường / sai kiểu ở API) name/price/category_id thiếu, null hoặc sai kiểu JSON (name là số; price là chuỗi — kể cả chuỗi số như "100000"; category_id là chuỗi chữ) → 4xx, không tạo/không đổi bản ghi. — (38, 39, 41, 42, 43, 45, 46)
- **C3 (giả định SV chốt):** (Tên – chuỗi chỉ gồm khoảng trắng) chuỗi chỉ gồm khoảng trắng coi như trống → bị từ chối; tách lớp riêng với chuỗi rỗng. — (37)
- **C11 (giả định SV chốt):** (Danh mục – 'danh sách có sẵn') danh sách có sẵn = các danh mục tồn tại trong bảng categories (GET /api/categories) tại thời điểm lưu. category_id không có trong danh sách hoặc thiếu → không hợp lệ. Quan sát (gray-box): ô chọn danh mục trên UI luôn có … — (44)
- Đạt trong cùng case: —
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-35): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 39, name "Muc tieu 35 1792497302093", price 1000000, category_id 1} → M_SAU {id 39, name "", price 2500000, category_id 3}`
- Actual nguyên văn (TC-FR15-36): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 40, name "Muc tieu 36 1792497303069", price "1000000", category_id 1} → M_SAU {id 40, name ""x"×300", price "2500000", category_id 3}` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
- Actual nguyên văn (TC-FR15-37): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 41, name "Muc tieu 37 1792497304008", price 1000000, category_id 1} → M_SAU {id 41, name "   ", price 2500000, category_id 3}`
- Actual nguyên văn (TC-FR15-38): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 42, name "Muc tieu 38 1792497304945", price "1000000", category_id 1} → M_SAU {id 42, name null, price "2500000", category_id 3}`
- Actual nguyên văn (TC-FR15-39): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 43, name "Muc tieu 39 1792497305863", price 1000000, category_id 1} → M_SAU {id 43, name "123", price 2500000, category_id 3}`
- Actual nguyên văn (TC-FR15-106): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 93, name "Muc tieu 106 1792497399830", price 1000000, category_id 1} → M_SAU {id 93, name "", price 2500000, category_id 3}`
- Actual nguyên văn (TC-FR15-112): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 99, name "Muc tieu 112 1792497402085", price 1000000, category_id 1} → M_SAU {id 99, name ""x"×256", price 2500000, category_id 3}` (rút gọn ký tự lặp; nguyên văn ở testcases.json)
- Actual nguyên văn (TC-FR15-40): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 44, name "Muc tieu 40 1792497306783", price "1000000", category_id 1} → M_SAU {id 44, name "Sua API40 1792497306783", price "-1000", category_id 3}`
- Actual nguyên văn (TC-FR15-41): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 45, name "Muc tieu 41 1792497307693", price 1000000, category_id 1} → M_SAU {id 45, name "Sua API41 1792497307693", price null, category_id 3}`
- Actual nguyên văn (TC-FR15-42): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 46, name "Muc tieu 42 1792497308626", price "1000000", category_id 1} → M_SAU {id 46, name "Sua API42 1792497308626", price "abc", category_id 3}`
- Actual nguyên văn (TC-FR15-43): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 47, name "Muc tieu 43 1792497309603", price 1000000, category_id 1} → M_SAU {id 47, name "Sua API43 1792497309603", price 100000, category_id 3}`
- Actual nguyên văn (TC-FR15-113): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 100, name "Muc tieu 113 1792497402983", price "1000000", category_id 1} → M_SAU {id 100, name "Sua BVA 113 1792497402983", price "0", category_id 3}`
- Actual nguyên văn (TC-FR15-44): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 48, name "Muc tieu 44 1792497310540", price "1000000", category_id 1} → M_SAU {id 48, name "Sua API44 1792497310540", price "2500000", category_id 999}`
- Actual nguyên văn (TC-FR15-45): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 49, name "Muc tieu 45 1792497311464", price 1000000, category_id 1} → M_SAU {id 49, name "Sua API45 1792497311464", price 2500000, category_id null}`
- Actual nguyên văn (TC-FR15-46): `HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 50, name "Muc tieu 46 1792497312379", price "1000000", category_id 1} → M_SAU {id 50, name "Sua API46 1792497312379", price "2500000", category_id "abc"}`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 179–189

  ```js
   179  app.put("/api/products/:id", (req, res) => {
   180    const { name, price, description, imageUrl, category_id } = req.body;
   181    db.run(
   182      "UPDATE products SET name = ?, price = ?, description = ?, imageUrl = ?, category_id = ? WHERE id = ?",
   183      [name, price, description, imageUrl, category_id, req.params.id],
   184      function (err) {
   185        if (err) return res.status(500).json({ error: err.message });
   186        res.json({ message: "Product updated" });
   187      },
   188    );
   189  });
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
