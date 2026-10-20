# HW02 – Domain Testing on EShop

**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Cấp độ AI:** Cấp 4 | **Công cụ AI:** [...]

## Tự đánh giá

| No. | Tiêu chí | Điểm | Tự đánh giá | Căn cứ |
|---|---|---|---|---|
| 1 | Feature A – FR-01 Đăng ký (Domain + Boundary) | 25 | [...] | [...] |
| 2 | Feature B – FR-07 Giỏ hàng (Domain + Boundary) | 25 | [...] | [...] |
| 3 | Feature C – FR-15 Product CRUD (Domain + Boundary) | 25 | [...] | [...] |
| 4 | Feature D – FR-20 Đăng ký trên Mobile (Domain + Boundary) | 15 | [...] | [...] |
| 5 | Agent Skills (`skills/domain-bva-testing`) | 10 | [...] | [...] |
|  | **Tổng** | **100** | **[...]** | |

## Test summary

<!-- SUMMARY:START -->
| Feature | Chức năng | Thiết kế | Đã chạy | Pass | Fail | Blocked | Chưa chạy | TC từ AI | TC AI + SV sửa | TC SV thêm | Bug |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A_FR01 | FR-01 Đăng ký tài khoản (web frontend-web + API POST /api/register) | 133 | 108 | 43 | 65 | 25 | 0 | 98 | 10 | 25 | 14 |
| B_FR07 | FR-07 Giỏ hàng (web frontend-web: /product/:id, /, /cart + API GET/POST /api/cart) | 62 | 53 | 14 | 39 | 9 | 0 | 49 | 0 | 13 | 20 |
| C_FR15 | FR-15 Quản lý Sản phẩm (web admin frontend-admin: tab 'Sản phẩm' + API POST/GET/PUT/DELETE /api/products) | 122 | 117 | 51 | 66 | 5 | 0 | 111 | 0 | 11 | 16 |
| D_FR20 | FR-20 Tính năng Mobile — chức năng Đăng ký (frontend-mobile, Expo SDK 54, màn hình 'Đăng Ký Tài Khoản'), áp dụng FR-01 | 33 | 31 | 21 | 10 | 2 | 0 | 27 | 0 | 6 | 7 |
| **Tổng** | **4 feature** | **350** | **309** | **129** | **180** | **41** | **0** | **285** | **10** | **55** | **57** |

Bug theo severity: Critical 11, High 20, Medium 12, Low 14 (tổng 57 file trong `bugs/`).
<!-- SUMMARY:END -->

## Video demo (YouTube)

| Nội dung | Link | Thời lượng |
|---|---|---|
| Agent Skill `domain-bva-testing` chạy end-to-end trên một feature | [...] | [...] |

## Tài liệu trong bài nộp

| File | Nội dung |
|---|---|
| `23120255_HW02_Report.md` / `.pdf` | Report chính (Domain + BVA, gap analysis) |
| `bugs/` | Bug report + ảnh trang GitHub Issues |
| `ai-forms/` | AI-02 Audit Report, AI-03 Disclosure, AI-05 Checklist (.md + PDF đã ký) |
| `appendix/A_prompt_log.md` | Prompt log (trích tự động) |
| `appendix/commit_log.txt` | Git commit log |
| `skills/` | Agent Skill |
