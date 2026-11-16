# Prompt Log – HW04
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude Opus 5.5

> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script `tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.

---

## #1 | 22:20 16/11/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
HW04 – bước 0: dựng môi trường. Repo hiện tại.
1. git pull; git status phải sạch.
2. Em đặt đề vào context/HW04_assignment.pdf → chuyển thành context/HW04_assignment.md (giữ nguyên chữ).
3. tools/hw.toml: chuyển sang HW04 (since = "2026-11-12 18:51", log/notes/extra trong HW04/appendix/), giữ cấu hình HW03 dạng comment.
4. Tạo HW04/CLAUDE.md: chép quy ước còn đúng từ HW03/CLAUDE.md (AI-01, không amend, bug do SV viết, prompt log), thêm yêu cầu HW04 từ đề.
5. Tạo HW04/tests/: @playwright/test bản mới nhất, 3 project chromium/firefox/webkit, workers 1, retries 0, globalSetup kiểm SUT (lấy từ HW02), HTML reporter: title + metadata "Run by: 23120255 · <ISO timestamp lúc chạy>", outputFolder HW04/reports/<project>_<timestamp>. Cài 3 trình duyệt.
6. Tạo 1 spec smoke tạm (mở trang chủ), chạy trên 3 trình duyệt để kiểm report hiện đúng "Run by" + timestamp; xong XOÁ spec smoke và report smoke (không commit chúng).
7. Commit "HW04: bước 0 – môi trường" (không push).
Báo cáo ≤ 12 dòng: phiên bản Playwright, "Run by" hiện ở đâu trong report, lỗi nếu có.


 Đồng thời, tạm dừng ghi các prompt log cho HW03, vì giờ đã bắt đầu sang HW04
```

**Output:**
```
Đã có đề + hw.toml chuyển HW04. Giờ tạo HW04/CLAUDE.md, settings deny, khung notes, rồi dựng Playwright.

Now writing files.

Root CLAUDE.md table update + Playwright files.

Browsers tải xong; WebKit báo thiếu DLL (cảnh báo). Bật SUT rồi chạy smoke để xem WebKit có chạy không.

Smoke spec + run 3 browsers.

WebKit bị Windows Application Control (Smart App Control) chặn `Playwright.exe`, nên không chạy được. Em kiểm report của Chromium/Firefox trước.

Report đúng. Giờ xoá smoke, sinh log HW04, commit.
```
*File AI ghi/gửi trong lượt này:* `hw.toml`, `CLAUDE.md`, `package.json`, `playwright.config.ts`, `global-setup.ts`

**Xử lý:** [...]

---

**Tổng:** 1 lượt; Claude Opus 5.5 1 lượt (#1).
