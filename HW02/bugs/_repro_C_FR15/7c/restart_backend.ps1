[Console]::OutputEncoding = [Text.Encoding]::UTF8
# Restart backend SUT (CSDL bị xoá và seed lại mỗi lần node server.js khởi động) — dùng trước/sau mỗi lần tái hiện 7c
$backend = 'D:\HK7\Testing\Exercise\HW\eshop-sut\backend'
Get-CimInstance Win32_Process -Filter "Name='node.exe'" | Where-Object { $_.CommandLine -match 'server\.js' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
Start-Sleep -Milliseconds 500
Start-Process -FilePath node -ArgumentList 'server.js' -WorkingDirectory $backend -WindowStyle Minimized
for ($i = 0; $i -lt 40; $i++) {
  Start-Sleep -Milliseconds 250
  try { $r = Invoke-WebRequest -UseBasicParsing -Uri 'http://localhost:3000/api/products'; $n = (ConvertFrom-Json $r.Content).Count; if ($n -ge 5) { "backend restart xong: $n sản phẩm"; exit 0 } } catch {}
}
"backend restart THẤT BẠI"; exit 1
