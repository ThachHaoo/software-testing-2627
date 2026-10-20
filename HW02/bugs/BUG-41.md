# BUG-41

- **ID:** BUG-41
- **Tiêu đề:** <SV viết>
- **Severity:** <SV viết>
- **Priority:** <SV viết>

## Môi trường

<SV viết>

## Tiền điều kiện

<SV viết>

## Các bước tái hiện

<SV viết>

## Expected (trích SRS)

<SV viết>

## Actual

<SV viết>

## Bằng chứng

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-23_api.png`

## TC liên quan

- Fail (17): TC-FR15-23, TC-FR15-24, TC-FR15-25, TC-FR15-26, TC-FR15-27, TC-FR15-84, TC-FR15-100, TC-FR15-28, TC-FR15-29, TC-FR15-30, TC-FR15-31, TC-FR15-101, TC-FR15-208, TC-FR15-214, TC-FR15-32, TC-FR15-33, TC-FR15-34
- Nhóm dữ kiện: G8 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-23 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":22}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 22, name "", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-23_req.json`, `HW02/C_FR15/evidence/TC-FR15-23_res.json`, `HW02/C_FR15/evidence/TC-FR15-23_api.png`

#### TC-FR15-24 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":23}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 23, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-24_req.json`, `HW02/C_FR15/evidence/TC-FR15-24_res.json`, `HW02/C_FR15/evidence/TC-FR15-24_api.png`, `HW02/C_FR15/evidence/TC-FR15-24_failed.png`

#### TC-FR15-25 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":24}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 24, name "   ", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-25_req.json`, `HW02/C_FR15/evidence/TC-FR15-25_res.json`, `HW02/C_FR15/evidence/TC-FR15-25_api.png`

#### TC-FR15-26 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":25}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 25, name null, price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-26_req.json`, `HW02/C_FR15/evidence/TC-FR15-26_res.json`, `HW02/C_FR15/evidence/TC-FR15-26_api.png`

#### TC-FR15-27 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":26}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 26, name "123", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-27_req.json`, `HW02/C_FR15/evidence/TC-FR15-27_res.json`, `HW02/C_FR15/evidence/TC-FR15-27_api.png`

#### TC-FR15-84 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":81}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 81, name "", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-84_req.json`, `HW02/C_FR15/evidence/TC-FR15-84_res.json`, `HW02/C_FR15/evidence/TC-FR15-84_api.png`

#### TC-FR15-100 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":87}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 87, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-100_req.json`, `HW02/C_FR15/evidence/TC-FR15-100_res.json`, `HW02/C_FR15/evidence/TC-FR15-100_api.png`, `HW02/C_FR15/evidence/TC-FR15-100_failed.png`

#### TC-FR15-28 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":27}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 27, name "SP API28 1792497292506", price -1000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-28_req.json`, `HW02/C_FR15/evidence/TC-FR15-28_res.json`, `HW02/C_FR15/evidence/TC-FR15-28_api.png`

#### TC-FR15-29 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":28}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 28, name "SP API29 1792497293415", price null, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-29_req.json`, `HW02/C_FR15/evidence/TC-FR15-29_res.json`, `HW02/C_FR15/evidence/TC-FR15-29_api.png`

#### TC-FR15-30 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":29}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 29, name "SP API30 1792497294325", price "abc", category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-30_req.json`, `HW02/C_FR15/evidence/TC-FR15-30_res.json`, `HW02/C_FR15/evidence/TC-FR15-30_api.png`

#### TC-FR15-31 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":30}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 30, name "SP API31 1792497295222", price 100000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-31_req.json`, `HW02/C_FR15/evidence/TC-FR15-31_res.json`, `HW02/C_FR15/evidence/TC-FR15-31_api.png`

#### TC-FR15-101 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":88}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 88, name "SP BVA 101 1792497398040", price 0, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-101_req.json`, `HW02/C_FR15/evidence/TC-FR15-101_res.json`, `HW02/C_FR15/evidence/TC-FR15-101_api.png`

#### TC-FR15-208 (Fail)

- **Expected:** HTTP 4xx kèm trường error; CSDL không tạo sản phẩm mới.
- **Actual:** HTTP 200 {"message":"Product created","id":112}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 112, name "SP Giá Âm Cực Đại 1792497423262", price -999999999999, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-208_req.json`, `HW02/C_FR15/evidence/TC-FR15-208_res.json`, `HW02/C_FR15/evidence/TC-FR15-208_api.png`

#### TC-FR15-214 (Fail)

- **Expected:** HTTP 4xx kèm trường error (do JS parse `1e-324` ngầm thành `0`, vi phạm giá > 0); CSDL không đổi.
- **Actual:** HTTP 200 {"message":"Product created","id":114}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 114, name "SP Underflow Price 1792497426240", price 0, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-214_req.json`, `HW02/C_FR15/evidence/TC-FR15-214_res.json`, `HW02/C_FR15/evidence/TC-FR15-214_api.png`

#### TC-FR15-32 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":31}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 31, name "SP API32 1792497296103", price 1500000, category_id 999}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-32_req.json`, `HW02/C_FR15/evidence/TC-FR15-32_res.json`, `HW02/C_FR15/evidence/TC-FR15-32_api.png`

#### TC-FR15-33 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":32}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 32, name "SP API33 1792497297046", price 1500000, category_id null}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-33_req.json`, `HW02/C_FR15/evidence/TC-FR15-33_res.json`, `HW02/C_FR15/evidence/TC-FR15-33_api.png`

#### TC-FR15-34 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":33}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 33, name "SP API34 1792497297969", price 1500000, category_id "abc"}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-34_req.json`, `HW02/C_FR15/evidence/TC-FR15-34_res.json`, `HW02/C_FR15/evidence/TC-FR15-34_api.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
