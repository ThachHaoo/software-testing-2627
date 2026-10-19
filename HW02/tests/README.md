# Test tự động HW02 (Playwright)

Cài một lần: `npm install` rồi `npx playwright install chromium`.

- A_FR01: spec ở `A_FR01/` (`A_FR01.spec.ts` + `lib.ts`), đọc trực tiếp `../A_FR01/testcases.json`; mỗi suite một describe, cả UI và API trong một project `A_FR01`.
- Feature khác: spec đặt ở `specs/`, tên file `<feature>.spec.ts` (UI) hoặc `<feature>.api.spec.ts` (API), đọc dữ liệu từ `../<feature>/testcases.json`.
- `global-setup.ts` kiểm backend/web, đăng nhập admin, tài khoản seed trước mỗi lượt chạy; thiếu thì dừng và nhắc khởi động lại backend.
- Quy ước tiêu đề, annotation `actual`, ảnh chụp: xem `.claude/skills/domain-bva-testing/references/automation.md`.
- Chạy (PowerShell): `$env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/A_FR01.json"; npx playwright test A_FR01`
- Gộp kết quả: `python ../../.claude/skills/domain-bva-testing/scripts/merge_results.py ../A_FR01/testcases.json results/A_FR01.json`

Chạy trên máy của em để kết quả và ảnh chụp là bằng chứng thật; trước mỗi lượt chạy, khởi động lại backend để có CSDL sạch.
