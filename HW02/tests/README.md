# Test tự động HW02 (Playwright)

Cài một lần: `npm install` rồi `npx playwright install chromium`.

- Spec đặt ở `specs/`, tên file `<feature>.spec.ts` (UI) hoặc `<feature>.api.spec.ts` (API), đọc dữ liệu từ `../<feature>/testcases.json`.
- Quy ước tiêu đề, annotation `actual`, ảnh chụp: xem `.claude/skills/domain-bva-testing/references/automation.md`.
- Chạy (PowerShell): `$env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/A_FR01.json"; npx playwright test A_FR01`
- Gộp kết quả: `python ../../.claude/skills/domain-bva-testing/scripts/merge_results.py ../A_FR01/testcases.json results/A_FR01.json`

Chạy trên máy của em để kết quả và ảnh chụp là bằng chứng thật; trước mỗi lượt chạy, khởi động lại backend để có CSDL sạch.
