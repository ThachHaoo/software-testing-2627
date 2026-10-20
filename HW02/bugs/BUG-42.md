# BUG-42

- **ID:** BUG-42
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

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-35_api.png`

## TC liên quan

- Fail (15): TC-FR15-35, TC-FR15-36, TC-FR15-37, TC-FR15-38, TC-FR15-39, TC-FR15-106, TC-FR15-112, TC-FR15-40, TC-FR15-41, TC-FR15-42, TC-FR15-43, TC-FR15-113, TC-FR15-44, TC-FR15-45, TC-FR15-46
- Nhóm dữ kiện: G9 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-35 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 39, name "Muc tieu 35 1792497302093", price 1000000, category_id 1} → M_SAU {id 39, name "", price 2500000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-35_req.json`, `HW02/C_FR15/evidence/TC-FR15-35_res.json`, `HW02/C_FR15/evidence/TC-FR15-35_api.png`

#### TC-FR15-36 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 40, name "Muc tieu 36 1792497303069", price "1000000", category_id 1} → M_SAU {id 40, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price "2500000", category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-36_req.json`, `HW02/C_FR15/evidence/TC-FR15-36_res.json`, `HW02/C_FR15/evidence/TC-FR15-36_api.png`, `HW02/C_FR15/evidence/TC-FR15-36_failed.png`

#### TC-FR15-37 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 41, name "Muc tieu 37 1792497304008", price 1000000, category_id 1} → M_SAU {id 41, name "   ", price 2500000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-37_req.json`, `HW02/C_FR15/evidence/TC-FR15-37_res.json`, `HW02/C_FR15/evidence/TC-FR15-37_api.png`

#### TC-FR15-38 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 42, name "Muc tieu 38 1792497304945", price "1000000", category_id 1} → M_SAU {id 42, name null, price "2500000", category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-38_req.json`, `HW02/C_FR15/evidence/TC-FR15-38_res.json`, `HW02/C_FR15/evidence/TC-FR15-38_api.png`

#### TC-FR15-39 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 43, name "Muc tieu 39 1792497305863", price 1000000, category_id 1} → M_SAU {id 43, name "123", price 2500000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-39_req.json`, `HW02/C_FR15/evidence/TC-FR15-39_res.json`, `HW02/C_FR15/evidence/TC-FR15-39_api.png`

#### TC-FR15-106 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 93, name "Muc tieu 106 1792497399830", price 1000000, category_id 1} → M_SAU {id 93, name "", price 2500000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-106_req.json`, `HW02/C_FR15/evidence/TC-FR15-106_res.json`, `HW02/C_FR15/evidence/TC-FR15-106_api.png`

#### TC-FR15-112 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 99, name "Muc tieu 112 1792497402085", price 1000000, category_id 1} → M_SAU {id 99, name "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", price 2500000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-112_req.json`, `HW02/C_FR15/evidence/TC-FR15-112_res.json`, `HW02/C_FR15/evidence/TC-FR15-112_api.png`, `HW02/C_FR15/evidence/TC-FR15-112_failed.png`

#### TC-FR15-40 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 44, name "Muc tieu 40 1792497306783", price "1000000", category_id 1} → M_SAU {id 44, name "Sua API40 1792497306783", price "-1000", category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-40_req.json`, `HW02/C_FR15/evidence/TC-FR15-40_res.json`, `HW02/C_FR15/evidence/TC-FR15-40_api.png`

#### TC-FR15-41 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 45, name "Muc tieu 41 1792497307693", price 1000000, category_id 1} → M_SAU {id 45, name "Sua API41 1792497307693", price null, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-41_req.json`, `HW02/C_FR15/evidence/TC-FR15-41_res.json`, `HW02/C_FR15/evidence/TC-FR15-41_api.png`

#### TC-FR15-42 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 46, name "Muc tieu 42 1792497308626", price "1000000", category_id 1} → M_SAU {id 46, name "Sua API42 1792497308626", price "abc", category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-42_req.json`, `HW02/C_FR15/evidence/TC-FR15-42_res.json`, `HW02/C_FR15/evidence/TC-FR15-42_api.png`

#### TC-FR15-43 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 47, name "Muc tieu 43 1792497309603", price 1000000, category_id 1} → M_SAU {id 47, name "Sua API43 1792497309603", price 100000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-43_req.json`, `HW02/C_FR15/evidence/TC-FR15-43_res.json`, `HW02/C_FR15/evidence/TC-FR15-43_api.png`

#### TC-FR15-113 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 100, name "Muc tieu 113 1792497402983", price "1000000", category_id 1} → M_SAU {id 100, name "Sua BVA 113 1792497402983", price "0", category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-113_req.json`, `HW02/C_FR15/evidence/TC-FR15-113_res.json`, `HW02/C_FR15/evidence/TC-FR15-113_api.png`

#### TC-FR15-44 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 48, name "Muc tieu 44 1792497310540", price "1000000", category_id 1} → M_SAU {id 48, name "Sua API44 1792497310540", price "2500000", category_id 999}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-44_req.json`, `HW02/C_FR15/evidence/TC-FR15-44_res.json`, `HW02/C_FR15/evidence/TC-FR15-44_api.png`

#### TC-FR15-45 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 49, name "Muc tieu 45 1792497311464", price 1000000, category_id 1} → M_SAU {id 49, name "Sua API45 1792497311464", price 2500000, category_id null}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-45_req.json`, `HW02/C_FR15/evidence/TC-FR15-45_res.json`, `HW02/C_FR15/evidence/TC-FR15-45_api.png`

#### TC-FR15-46 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx), body có trường error (C6). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 50, name "Muc tieu 46 1792497312379", price "1000000", category_id 1} → M_SAU {id 50, name "Sua API46 1792497312379", price "2500000", category_id "abc"}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-46_req.json`, `HW02/C_FR15/evidence/TC-FR15-46_res.json`, `HW02/C_FR15/evidence/TC-FR15-46_api.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
