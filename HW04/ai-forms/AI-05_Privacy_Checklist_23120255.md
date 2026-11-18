**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**
**CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**
**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# Bảng Kiểm Quyền Riêng tư & Sử dụng AI Có Trách nhiệm

**Bài tập:** HW04-AI – Automation Testing on EShop
**Công cụ AI:** Claude (không rõ model) 37 lượt; Claude Opus 5.5 49 lượt (tổng 86 lượt theo dòng Tổng của `appendix/A_prompt_log.md`, khớp AI-03 mục 1; lượt claude.ai: Claude Opus 5.5 theo em xác nhận)

*Chỉ tick mục có bằng chứng trong repo (ghi ở cuối dòng). Mục cam kết cá nhân để trống "(em tự xác nhận)".*

## 1. Trước khi dùng AI

- [x] Đã xác nhận Cấp độ AI cho bài tập này. — *report dòng đầu: Cấp 4; AI-03 mục 1*
- [x] Dùng tài khoản Claude tự chọn. 
- [x] Đã đọc Thoả thuận AI của môn học. 
- [x] Hiểu rõ artifact nào KHÔNG được sinh bằng AI. — *AI-03 mục 4 "Danh mục AI không được làm"; `CLAUDE.md` §3, `HW04/CLAUDE.md` §6*

## 2. Trong khi dùng AI

- [x] Không nhập dữ liệu cá nhân của bạn, khách hàng, bệnh nhân. 
  - **Minh bạch:** log Code Integrity em xuất (`env/firefox_blocked_20261117.txt`) có đường dẫn chứa tên người dùng Windows; tài khoản thử nghiệm dùng tài khoản seed của SUT (`admin@eshop.com`, `test@eshop.com`) và email sinh theo `{ts}`.
- [x] Không paste nguyên si tài liệu có bản quyền lên AI. 
- [x] Không paste code công ty / code open-source giới hạn license. 
- [x] Đã ghi mọi prompt + phản hồi AI vào prompt log có timestamp. — *`appendix/A_prompt_log.md` (86 lượt, trích tự động, giờ Asia/Saigon; lượt claude.ai sau lần xuất dữ liệu cuối chưa có – AI-03 mục 1)*

## 3. Trước khi nộp bài

- [x] Mọi artifact AI sinh đã được gắn tag trong AI Audit Report. — *AI-02 mục 3.1 (theo commit), 3.3 (theo file), report §9*
- [x] Mọi trích dẫn AI đã được xác minh (nguồn thực sự tồn tại). 
- [x] Mọi code AI sinh đã được thực thi và test. — *9 lượt chính thức (3 feature × 3 trình duyệt) `reports/`; `tsc --noEmit` + `--list`; tái hiện bug `bugs/repro_check.md`*
- [x] AI Critique 200–300 chữ đã có trong báo cáo. — *report §8*
- [x] Đoạn Mandatory Disclosure ở cuối báo cáo. — *report §10*
- [x] Đính kèm AI Use Disclosure Form. — *`ai-forms/AI-03_Disclosure_Form_23120255.md`*
- [x] Sẵn sàng cho vấn đáp ngẫu nhiên 5–7 phút tuần kế nộp bài. 

## 4. Cam đoan Cuối cùng

*Em xác nhận đã rà soát danh sách trên; các mục chưa tick do em tự xác nhận trước khi ký.*

## Chữ ký

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |
| MSSV: | 23120255 |
| Lớp / Khoá: | Software Testing - 23_3 |
| Môn học: | CSC13003 – Kiểm chứng Phần mềm |
| Giảng viên: | Thầy Lâm Quang Vũ, Thầy Trần Duy Hoàng, Cô Trần Thị Bích Hạnh, Thầy Trương Phước Lộc, Thầy Hồ Tuấn Thanh |
| Ngày: | 18/11/2026 |
| Chữ ký: | ![Chữ ký](signature.png)  |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Hardman, P. (2025). A Post-AI Learning Taxonomy.
- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.
