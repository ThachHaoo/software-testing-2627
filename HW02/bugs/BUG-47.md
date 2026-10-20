# BUG-47

- **ID:** BUG-47
- **Tiêu đề:** <SV viết>
- **Severity:** <SV viết>
- **Priority:** <SV viết>

## Môi trường

Chép nguyên văn từ `HW02/env/environment.md`:

| Mục | Giá trị |
|---|---|
| SUT | EShop, fork nhóm `tkob-team/eshop-sut` @ `de0f48f` (= `ttbhanh/eshop-sut` `85af3ba` + `.gitignore`, không đổi mã) |
| Máy | [...] (OS, CPU/RAM) |
| Node.js | [...] (`node -v`) |
| Trình duyệt | [...] (tên + phiên bản) |
| Backend / Web / Admin | http://localhost:3000 · :5173 · :5174 |
| Điện thoại | [...] (model, Android/iOS + phiên bản) |
| Expo Go | [...] (bản cho SDK 54) |
| Thay đổi SUT | `frontend-mobile/App.js` dòng 16 `API_URL` → IP LAN `[...]` (xem `mobile_api_url.patch`) |
| Playwright | [...] (`npx playwright --version`) |

**Đặc điểm môi trường ảnh hưởng thiết kế test**
- Backend xoá và seed lại CSDL mỗi lần khởi động; giỏ hàng lưu trong RAM.
- Tài khoản seed: admin `admin@eshop.com` / `Admin123!`, user `test@eshop.com` / `Test1234!` (setup_guide ghi `admin123`, không khớp seed).

- Commit SUT: `de0f48f`

## Tiền điều kiện

<SV viết>

## Các bước tái hiện

<SV viết>

## Expected (trích SRS)

<SV viết>

## Actual

<SV viết>

## Bằng chứng

- Ảnh tiêu biểu: `HW02/C_FR15/evidence/TC-FR15-50_api.png`

## TC liên quan

- Fail (9): TC-FR15-50, TC-FR15-51, TC-FR15-52, TC-FR15-53, TC-FR15-54, TC-FR15-55, TC-FR15-56, TC-FR15-57, TC-FR15-58
- Nhóm dữ kiện: G11 trong `HW02/bugs/_groups_C_FR15.md`

## Yêu cầu

<SV viết>

## Ghi chú cô lập

### Dữ kiện (AI chép)

Expected / Actual chép nguyên văn từ `HW02/C_FR15/testcases.json` (lượt chính thức = lượt 6; case manual theo ảnh SV).

#### TC-FR15-50 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":34}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 34, name "SP API50 1792497298877", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-50_req.json`, `HW02/C_FR15/evidence/TC-FR15-50_res.json`, `HW02/C_FR15/evidence/TC-FR15-50_api.png`

#### TC-FR15-51 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":35}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 35, name "SP API51 1792497299774", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-51_req.json`, `HW02/C_FR15/evidence/TC-FR15-51_res.json`, `HW02/C_FR15/evidence/TC-FR15-51_api.png`

#### TC-FR15-52 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product created","id":36}; bản ghi TRƯỚC → SAU: 5 → 6; bản ghi mới: {id 36, name "SP API52 1792497300678", price 1500000, category_id 2}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-52_req.json`, `HW02/C_FR15/evidence/TC-FR15-52_res.json`, `HW02/C_FR15/evidence/TC-FR15-52_api.png`

#### TC-FR15-53 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 51, name "Muc tieu 53 1792497314256", price 1000000, category_id 1} → M_SAU {id 51, name "Sua API53 1792497314256", price 2500000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-53_req.json`, `HW02/C_FR15/evidence/TC-FR15-53_res.json`, `HW02/C_FR15/evidence/TC-FR15-53_api.png`

#### TC-FR15-54 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 52, name "Muc tieu 54 1792497315170", price "1000000", category_id 1} → M_SAU {id 52, name "Sua API54 1792497315170", price "2500000", category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-54_req.json`, `HW02/C_FR15/evidence/TC-FR15-54_res.json`, `HW02/C_FR15/evidence/TC-FR15-54_api.png`

#### TC-FR15-55 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: M_SAU = M_TRƯỚC; GET /api/products SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product updated"}; bản ghi TRƯỚC → SAU: 6 → 6; M_TRƯỚC {id 53, name "Muc tieu 55 1792497316069", price 1000000, category_id 1} → M_SAU {id 53, name "Sua API55 1792497316069", price 2500000, category_id 3}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-55_req.json`, `HW02/C_FR15/evidence/TC-FR15-55_res.json`, `HW02/C_FR15/evidence/TC-FR15-55_api.png`

#### TC-FR15-56 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU vẫn có id M; SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 55, name "Muc tieu 56 1792497320087", price 1000000, category_id 1} → M_SAU HTTP 200 {}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-56_req.json`, `HW02/C_FR15/evidence/TC-FR15-56_res.json`, `HW02/C_FR15/evidence/TC-FR15-56_api.png`

#### TC-FR15-57 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU vẫn có id M; SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 56, name "Muc tieu 57 1792497320980", price "1000000", category_id 1} → M_SAU HTTP 200 {}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-57_req.json`, `HW02/C_FR15/evidence/TC-FR15-57_res.json`, `HW02/C_FR15/evidence/TC-FR15-57_api.png`

#### TC-FR15-58 (Fail)

- **Expected:** HTTP 4xx (không 2xx, không 5xx) (FR-12.2). Dữ liệu: GET /api/products SAU vẫn có id M; SAU = TRƯỚC.
- **Actual:** HTTP 200 {"message":"Product deleted"}; bản ghi TRƯỚC → SAU: 6 → 5; M_TRƯỚC {id 57, name "Muc tieu 58 1792497321894", price 1000000, category_id 1} → M_SAU HTTP 200 {}
- **Evidence:** `HW02/C_FR15/evidence/TC-FR15-58_req.json`, `HW02/C_FR15/evidence/TC-FR15-58_res.json`, `HW02/C_FR15/evidence/TC-FR15-58_api.png`

### Nhận định

<SV viết>

## Link GitHub Issue

(điền sau khi tạo issue)

---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
