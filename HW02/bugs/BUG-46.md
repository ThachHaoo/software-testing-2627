# BUG-46

- **ID:** BUG-46
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

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-47_api.png`

## TC liên quan

- Fail (3): TC-FR15-47, TC-FR15-48, TC-FR15-49
- Nhóm dữ kiện: G10 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-47 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (C10). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {}; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-47_req.json`, `HW02/C_FR15/evidence/TC-FR15-47_res.json`, `HW02/C_FR15/evidence/TC-FR15-47_api.png`

#### TC-FR15-48 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (C10). Dữ liệu: GET /api/products SAU = TRƯỚC (không có bản ghi mới, không bản ghi nào đổi).
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-48_req.json`, `HW02/C_FR15/evidence/TC-FR15-48_res.json`, `HW02/C_FR15/evidence/TC-FR15-48_api.png`

#### TC-FR15-49 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (C10). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-49_req.json`, `HW02/C_FR15/evidence/TC-FR15-49_res.json`, `HW02/C_FR15/evidence/TC-FR15-49_api.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
