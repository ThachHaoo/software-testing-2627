# BUG-34

- **ID:** BUG-34
- **Tiêu đề:** 
- **Severity:** 
- **Priority:** 

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API trong RAM)
- Trình duyệt: Chromium 130.0.6723.31 (Playwright 1.48.2), locale vi-VN
- Web http://localhost:5173 (frontend-web), API http://localhost:3000
- Lượt chính thức: lượt 2, 2026-10-20 13:14 (Asia/Saigon); TC-FR07-201, 209 từ lượt 3 (13:17), kết quả trùng lượt 2
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện


## Các bước tái hiện


## Expected (trích SRS)


## Actual


## Bằng chứng

<details>
<summary>Evidence từng TC (1)</summary>

- TC-FR07-209: `HW02/B_FR07/evidence/TC-FR07-209_api.png`, `HW02/B_FR07/evidence/TC-FR07-209_req.json`, `HW02/B_FR07/evidence/TC-FR07-209_res.json`
</details>

## TC liên quan

- Fail (1): TC-FR07-209
- Nhóm dữ kiện: G20 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **B17 (giả định):** B17 (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106). — vi phạm ở: 4xx nhưng body là trang HTML, không có trường error

- Đạt trong cùng case: API-CART (body không phải JSON bị từ chối (400), giỏ không đổi)
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G20: API · POST /api/cart body không phải JSON hợp lệ (quantity: Infinity) → HTTP 400 trả trang HTML (stack trace), không có trường error; giỏ không đổi
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt); lượt 3 cũng giống.
- Actual tiêu biểu (TC-FR07-209, nguyên văn): POST HTTP 400 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot;uant; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]
- Lượt 1 gửi sai body do script (Playwright tự JSON.stringify); lượt 2, 3 gửi đúng chuỗi thô — kết quả trùng nhau.
- Body HTML có đường dẫn tuyệt đối trên máy chạy (node_modules\body-parser) — evidence gốc giữ nguyên (quy ước: bản dán issue che đặt ở `HW02/bugs/_issue_redacted/`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 12 (xem `bugs_facts.md`, G20)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
