# BUG-34

- **ID:** BUG-34
- **Tiêu đề:** `<SV viết>`
- **Severity:** `<SV viết>`
- **Priority:** `<SV viết>`

## Môi trường

- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `de0f48f` = 85af3ba + .gitignore, không đổi mã)
- Máy: Windows (PowerShell), backend `node server.js` (CSDL seed lại mỗi lần khởi động; giỏ API nằm trong RAM)
- Công cụ gửi request: Playwright 1.48.2 (APIRequestContext)
- API http://localhost:3000/api/cart (backend)
- Ngày chạy: 2026-10-20 (lượt chính thức = lượt 2, bắt đầu 13:14, Asia/Saigon); TC-FR07-209 lấy từ lượt 3 (13:17), kết quả trùng lượt 2
- Chi tiết: `HW02/env/environment.md`, nhật ký lượt chạy `HW02/B_FR07/RUN.md`

## Tiền điều kiện

`<SV viết>`

## Các bước tái hiện

`<SV viết>`

## Expected (trích SRS)

`<SV viết>`

## Actual

`<SV viết>`

## Bằng chứng

- Ảnh tiêu biểu: `TC-FR07-209_api.png`
- TC-FR07-209: `HW02/B_FR07/evidence/TC-FR07-209_api.png`, `HW02/B_FR07/evidence/TC-FR07-209_req.json`, `HW02/B_FR07/evidence/TC-FR07-209_res.json`
- Bản che dùng cho issue: `HW02/bugs/_issue_redacted/BUG-34.txt`

## TC liên quan

- Fail (1): TC-FR07-209
- Nhóm dữ kiện: G20 trong `HW02/bugs/_groups_B_FR07.md`

## Yêu cầu

- **B17 (giả định SV chốt):** (mã lỗi API) (SV chốt 2026-10-20, theo đề xuất AI): api_specification §4 không mô tả lỗi. Đề xuất như A11: dữ liệu không hợp lệ → 4xx (không 2xx, không 5xx) kèm trường error; không cố định mã. Quan sát code: thiếu token → 401, token sai → 403 (server.js dòng 103, 106). — vi phạm ở: 4xx nhưng body là trang HTML, không có trường error
- Đạt trong cùng case: API-CART (body không phải JSON bị từ chối (400), giỏ không đổi)
- Chưa đánh giá được: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Actual nguyên văn (TC-FR07-209): `POST HTTP 400 <!DOCTYPE html> ↵ <html lang="en"> ↵ <head> ↵ <meta charset="utf-8"> ↵ <title>Error</title> ↵ </head> ↵ <body> ↵ <pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot;uant; TRƯỚC: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]; SAU: [{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]`
- Payload (`TC-FR07-209_req.json`): headers `{"Content-Type": "application/json", "Authorization": "Bearer <T>"}`, body thô `{"id": 5, "name": "Bàn phím cơ Keychron Q1", "price": 4000000, "quantity": Infinity}`; GET /api/cart TRƯỚC `[{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}]`
- Phản hồi (`TC-FR07-209_res.json`): HTTP 400, body `<!DOCTYPE html> ↵ <html lang="en"> ↵ <head> ↵ <meta charset="utf-8"> ↵ <title>Error</title> ↵ </head> ↵ <body> ↵ <pre>SyntaxError: Unexpected token &#39;I&#39;, ...&quot;uantity&quot;: Infinity}&quot; is not valid JSON<br> &nbsp; &nbsp;at JSON.parse (&lt;anonymous&gt;)<br> &nbsp; &nbsp;at parse (<SU… (rút gọn)`
- GET /api/cart SAU (`TC-FR07-209_res.json`): HTTP 200, body `[{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}]`
- Lượt 1 gửi sai body do script (Playwright tự JSON.stringify); lượt 2, 3 gửi đúng chuỗi thô — kết quả trùng nhau.
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt); lượt 3 cũng giống.
- Đoạn code trích nguyên văn: `backend/server.js` dòng 12

  ```js
    12  app.use(bodyParser.json());
  ```

### Nhận định

`<SV viết>`

## Link GitHub Issue

`<sau khi tạo issue>`

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
