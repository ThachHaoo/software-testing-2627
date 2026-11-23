# Prompt Log – HW05
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude Opus 5.5

> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script `tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.

---

## #1 | 12:51 23/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
NHIỆM VỤ: (A) Chuyển hook prompt log sang HW05 + dọn log thừa HW04; (B) khảo sát SUT + môi trường HW05 (JMeter). CHƯA viết test plan.
Quyết định: HW05 bắt đầu 2026-11-23 12:39 (giờ VN). Workflow dự kiến = C (login → GET /api/products → POST /api/checkout → GET /api/orders/my-orders).

A. Prompt log
1. git diff HW04/appendix/A_prompt_log.md: phần thêm chỉ là lượt sau khi nộp HW04 → git restore. Khác → DỪNG, báo.
2. Sửa cấu hình hook/script trích (không sửa output tay): đích HW05/appendix/A_prompt_log.md; notes/extra HW05/prompt_log_notes.toml, HW05/prompt_log_extra.toml; chỉ lấy lượt từ mốc trên; HW04 không bị ghi thêm.
3. Transcript cũ trong .transcripts/: KHÔNG xoá, chuyển vào .transcripts/<HW>/ (vẫn gitignore); script HW05 chỉ đọc gốc .transcripts/ hoặc lọc theo mốc.
4. on_stop.py --manual: log HW05 chỉ có lượt từ 12:39 hôm nay; HW04 sạch.
Commit `HW05: chuyển hook prompt log sang HW05`.

B. Khảo sát (ghi HW05/notes/sut_recon.md, kèm file:dòng)
5. Kiểm thư mục SUT đã add-dir còn đọc được; git status + git pull (ghi commit trước/sau).
6. Cách chạy backend, port, base URL; DB loại gì (SQLite? WAL? index).
7. 4 endpoint C: method, path, auth, body/response mẫu. QUAN TRỌNG: checkout nhận items trong body hay bắt buộc cart?
8. Lockout: ngưỡng, thời gian khoá, lưu ở đâu, cách reset.
9. Tồn kho: checkout có trừ stock? seed bao nhiêu; cách reset DB về seed.
10. Tài khoản seed: số lượng + cách tạo thêm user cho CSV (không in mật khẩu thật vào chat). Rate limit/middleware có thể chặn tải.
11. Môi trường: hostname, OS, CPU/RAM, java -version, JMeter (bản, đường dẫn). Chưa có thì ghi, KHÔNG tự cài.
Commit `HW05: khảo sát SUT và môi trường`.

Không amend, không push.
Báo cáo ≤ 18 dòng: diff HW04 có gì, số lượt log HW05 + giờ đầu/cuối, C khả thi không (checkout+items), lockout/reset, stock/reset, DB, JMeter/Java, hostname, 2 hash.
```

**Output:**
```
Login expired · Please run /login

Đang cập nhật hw.toml sang HW05 (hook đã sửa xong, transcript cũ đã chuyển vào thư mục con).
```

**Xử lý:** [...]

---

**Tổng:** 1 lượt; Claude Opus 5.5 1 lượt (#1).
