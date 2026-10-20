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

## Lượt chạy lại (bước 6b): TC-FR07-201, TC-FR07-209

1. Khởi động lại backend (bắt buộc trước lượt chạy lại) và chạy web như bước 1–2.
2. Chạy lại và gộp kết quả:

   ```powershell
   cd HW02/tests; $env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/B_FR07_rerun.json"; npx playwright test --project=B_FR07 -g "TC-FR07-(201|209) " --reporter=list,json; cd ../..
   python .claude/skills/domain-bva-testing/scripts/merge_results.py HW02/B_FR07/testcases.json HW02/tests/results/B_FR07_rerun.json
   ```

## Nhật ký lượt chạy

| Lượt | Thời điểm (20/10/2026) | Phạm vi | Script | Ghi chú |
|---|---|---|---|---|
| 1 | ≈ 12:56 | toàn bộ 62 case | 6/7a | Kết quả chính thức ban đầu. results/B_FR07.json và evidence bị lượt 2 ghi đè do chạy nhầm; số liệu còn trong notes "6b" và báo cáo 6b |
| 2 | 13:14 | toàn bộ 62 case | đã sửa ở 6b (TC-201 element.click(), body API dạng Buffer) | auto_status giống lượt 1 ở mọi case trừ TC-201, TC-209 (cả hai vẫn Fail) |
| 3 | 13:17 | TC-201, TC-209 | như lượt 2 | Kết quả giống lượt 2 |

**Lượt chính thức = lượt 2** (SV xác nhận đã restart backend trước mọi lượt). Lượt 3 = chạy lại TC-201, TC-209; evidence của hai case này lấy từ lượt 3, kết quả trùng lượt 2.

Evidence chỉ giữ của lượt mới nhất (merge chép đè cùng tên file); không vá do giới hạn 20 MB của bài nộp.

Từ nay mỗi lượt ghi results riêng có timestamp:

```powershell
cd HW02/tests; $ts = Get-Date -Format yyyyMMdd-HHmmss; $env:PLAYWRIGHT_JSON_OUTPUT_NAME="results/B_FR07_$ts.json"; npx playwright test --project=B_FR07 --reporter=list,json; cd ../..
python .claude/skills/domain-bva-testing/scripts/merge_results.py HW02/B_FR07/testcases.json HW02/tests/results/B_FR07_<ts>.json
```
