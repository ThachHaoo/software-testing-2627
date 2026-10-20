# BUG-43

- **ID:** BUG-43
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

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-209_api.png`

## TC liên quan

- Fail (1): TC-FR15-209
- Nhóm dữ kiện: G13 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-209 (Fail)

- **Expected:** HTTP 4xx kèm trường error (không trả về HTML 500 lộ stack trace); CSDL không đổi.
- **Actual:** HTTP 400 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot; &quot;price&quot;: Infinity, &quot;... is n; bản ghi TRƯỚC → SAU: 5 → 5
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-209_req.json`, `HW02/C_FR15/evidence/TC-FR15-209_res.json`, `HW02/C_FR15/evidence/TC-FR15-209_api.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
