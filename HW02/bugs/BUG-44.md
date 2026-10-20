# BUG-44

- **ID:** BUG-44
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động)
- Client: Playwright 1.48.2 APIRequestContext (lượt 6); kiểm tái hiện bằng PowerShell 5.1 Invoke-WebRequest (7/7a)
- API POST http://localhost:3000/api/products
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

- Ảnh tiêu biểu: `TC-FR15-211_api.png`
- TC-FR15-211: `HW02/C_FR15/evidence/TC-FR15-211_req.json`, `HW02/C_FR15/evidence/TC-FR15-211_res.json`, `HW02/C_FR15/evidence/TC-FR15-211_api.png`

## TC liên quan

- Fail (1): TC-FR15-211
- Nhóm dữ kiện: G14 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

- **C6 (giả định SV chốt):** (tầng API áp FR-15) API là tầng riêng, suite riêng: POST/PUT gọi trực tiếp với dữ liệu vi phạm FR-15.2–15.4 → 4xx (không 2xx, không 5xx) kèm trường error, không tạo/không đổi bản ghi; không cố định mã cụ thể. — (không 5xx; SV ghi căn cứ C6, C9)
- Đạt trong cùng case: Không tạo sản phẩm
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR15-211): `HTTP 500 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>TypeError: Cannot destructure property &#39;name&#39; of &#39;req.body&#39; as it is undefined.<; bản ghi TRƯỚC → SAU: 5 → 5`
- Lặp lại: auto_status giống nhau ở lượt 3 (lượt thử, harness lỗi H1–H4) và lượt 6 (chính thức, restart backend trước lượt); tái hiện lại ở 7/7a (`_groups_C_FR15.md`).
- Đoạn code trích nguyên văn: `backend/server.js` dòng 11–12

  ```js
    11  app.use(cors());
    12  app.use(bodyParser.json());
  ```
- Đoạn code trích nguyên văn: `backend/server.js` dòng 167–168

  ```js
   167  app.post("/api/products", (req, res) => {
   168    const { name, price, description, imageUrl, category_id } = req.body;
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
