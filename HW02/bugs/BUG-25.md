# BUG-25

- **ID:** BUG-25
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

- TC-FR07-94: `HW02/B_FR07/evidence/TC-FR07-94_ui.png`
</details>

## TC liên quan

- Fail (1): TC-FR07-94
- Nhóm dữ kiện: G11 trong `HW02/B_FR07/bugs_facts.md`

## Yêu cầu

- **FR-24.4:** (GUI, B16) Tất cả ảnh sản phẩm phải có thuộc tính alt mô tả nội dung (không rỗng). — vi phạm ở: trang chủ: 5/5 alt rỗng

- Đạt trong cùng case: FR-24.4 ở trang chi tiết (alt = tên sản phẩm)
- Chưa đánh giá được trong cùng case: —

## Ghi chú cô lập

### Dữ kiện (AI chép)

- Triệu chứng nhóm G11: UI · trang chủ: ảnh sản phẩm có alt rỗng (5/5 ảnh)
- Lặp lại: auto_status giống nhau ở lượt 1 và lượt 2 (restart backend trước mỗi lượt).
- Actual tiêu biểu (TC-FR07-94, nguyên văn): alt trang chủ=["","","","",""]; alt trang chi tiết=["Tai nghe AirPods Pro 2"]; trang giỏ không có ảnh sản phẩm (notes, không tính Fail); [kiểm tay] alt "mô tả nội dung ảnh": SV đối chiếu chữ alt với ảnh
- Cùng case: trang chi tiết alt = tên sản phẩm (đạt); trang giỏ không có ảnh.
- Notes SV: evidence kiểm tay cần chụp lại trong cửa sổ ẩn danh không tiện ích.
- Đoạn code trích nguyên văn: `frontend-web/src/pages/Home.jsx` dòng 80–84 (xem `bugs_facts.md`, G11)

### Nhận định


## Link GitHub Issue


---

Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện.
