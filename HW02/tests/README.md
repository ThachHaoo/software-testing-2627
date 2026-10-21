# Test tự động HW02 (Playwright)

Cài một lần: `npm install` rồi `npx playwright install chromium`.

- A_FR01: spec ở `A_FR01/` (`A_FR01.spec.ts` + `lib.ts`), đọc trực tiếp `../A_FR01/testcases.json`; mỗi suite một describe, cả UI và API trong một project `A_FR01`.
- B_FR07, C_FR15: spec ở `B_FR07/` (`B_FR07.spec.ts` + `lib.ts`) và `C_FR15/` (`C_FR15.spec.ts` + `lib.ts` + `oracle.ts`), đọc `../<feature>/testcases.json`; project `B_FR07`, `C_FR15` trong `playwright.config.ts`. Thư mục `specs/` hiện để trống.
- D_FR20 chạy tay (không có spec), xem `../D_FR20/RUN.md`.
- Kết quả lượt chính thức đã commit (thư mục `results/` bị gitignore, thêm bằng `git add -f`): `results/A_FR01.json` (A, 19/10 22:42), `results/B_FR07.json` + `results/B_FR07_rerun.json` (B), `results/C_FR15_20261020-185355.json` (C, lượt 6).
- `global-setup.ts` kiểm backend/web, đăng nhập admin, tài khoản seed trước mỗi lượt chạy; thiếu thì dừng và nhắc khởi động lại backend.
- Quy ước tiêu đề, annotation `actual`, ảnh chụp: xem `.claude/skills/domain-bva-testing/references/automation.md`.
- Chạy (PowerShell): `$env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/A_FR01.json"; npx playwright test A_FR01`
- Gộp kết quả: `python ../../.claude/skills/domain-bva-testing/scripts/merge_results.py ../A_FR01/testcases.json results/A_FR01.json`

Chạy trên máy của em để kết quả và ảnh chụp là bằng chứng thật; trước mỗi lượt chạy, khởi động lại backend để có CSDL sạch.
