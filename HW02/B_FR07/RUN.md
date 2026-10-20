# B_FR07 – Lệnh chạy test (SV chạy trên máy mình, PowerShell)

1. Khởi động lại backend (CSDL seed sạch, giỏ RAM rỗng):

   ```powershell
   cd ..\eshop-sut\backend; node server.js
   ```

2. Chạy web (cửa sổ PowerShell khác):

   ```powershell
   cd ..\eshop-sut\frontend-web; npm run dev
   ```

3. Chạy test (cửa sổ PowerShell khác, từ thư mục repo):

   ```powershell
   cd HW02/tests; $env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/B_FR07.json"; npx playwright test --project=B_FR07 --reporter=list,json; cd ../..
   ```

4. Gộp kết quả vào testcases.json:

   ```powershell
   python .claude/skills/domain-bva-testing/scripts/merge_results.py HW02/B_FR07/testcases.json HW02/tests/results/B_FR07.json
   ```
