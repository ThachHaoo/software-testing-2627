[Console]::OutputEncoding = [Text.Encoding]::UTF8
# 7c2 — sập backend: POST price null (id chẵn) rồi GET /api/products/:id; backend chạy với stderr ghi ra file để lấy stack trace
$err = Join-Path $env:TEMP 'eshop_backend_err.txt'
Get-CimInstance Win32_Process -Filter "Name='node.exe'" | Where-Object { $_.CommandLine -match 'server\.js' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
Start-Sleep -Milliseconds 500
$p = Start-Process -FilePath node -ArgumentList 'server.js' -WorkingDirectory 'D:\HK7\Testing\Exercise\HW\eshop-sut\backend' -RedirectStandardOutput "$err.out" -RedirectStandardError $err -PassThru -WindowStyle Hidden
for ($i = 0; $i -lt 40; $i++) { Start-Sleep -Milliseconds 250; try { if ((ConvertFrom-Json (Invoke-WebRequest -UseBasicParsing http://localhost:3000/api/products).Content).Count -ge 5) { break } } catch {} }
$body = '{"name": "SP 7c null", "price": null, "category_id": 2, "description": "Mô tả 7c", "imageUrl": "https://placehold.co/300"}'
"POST /api/products body: $body"
$r = Invoke-WebRequest -UseBasicParsing -Method Post -Uri http://localhost:3000/api/products -ContentType 'application/json' -Body ([Text.Encoding]::UTF8.GetBytes($body)); "-> HTTP $($r.StatusCode) $($r.Content)"
$id = (ConvertFrom-Json $r.Content).id
try { $g = Invoke-WebRequest -UseBasicParsing -Uri "http://localhost:3000/api/products/$id"; "GET /api/products/$id -> HTTP $($g.StatusCode) $($g.Content)" } catch { "GET /api/products/$id -> lỗi: $($_.Exception.Message)" }
Start-Sleep 1; $p.Refresh(); "tiến trình đã dừng: $($p.HasExited); mã thoát: $($p.ExitCode)"
"--- stderr ---"; Get-Content $err -Encoding UTF8
powershell -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'restart_backend.ps1')
