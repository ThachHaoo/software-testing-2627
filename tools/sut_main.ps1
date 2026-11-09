[Console]::OutputEncoding = [Text.Encoding]::UTF8
# HW03 T2 – sau đợt usability: tắt tunnel/Vite, quay SUT về nhánh main (bản kiểm thử chính thức de0f48f).
# Nhánh usability-tunnel giữ nguyên (local, không push). Usage: powershell -ExecutionPolicy Bypass -File tools\sut_main.ps1
$sut = 'D:\HK7\Testing\Exercise\HW\eshop-sut'
Get-Process cloudflared -ErrorAction SilentlyContinue | Stop-Process -Force
Get-NetTCPConnection -State Listen -LocalPort 5173 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
git -C $sut switch main | Out-Host
if ($LASTEXITCODE -ne 0) { "Không chuyển được về main (xem git status trong $sut)"; exit 1 }
"SUT: nhánh $((git -C $sut branch --show-current).Trim()) @ $((git -C $sut rev-parse --short HEAD).Trim())"
$n = (Select-String -Path (Join-Path $sut 'frontend-web\src\pages\Home.jsx') -Pattern 'localhost:3000' -SimpleMatch).Count
"frontend-web dùng lại http://localhost:3000 ($n chỗ trong Home.jsx). Mở web: cd $sut\frontend-web; npx vite --host 127.0.0.1 --port 5173"
