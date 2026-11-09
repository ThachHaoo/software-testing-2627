# HW03 T2 – mở môi trường usability từ xa cho 1 phiên:
#   restart backend (CSDL seed lại) → Vite của nhánh usability-tunnel (127.0.0.1:5173) → Cloudflare quick tunnel → in link.
# Ctrl+C: tắt tunnel + Vite (backend để chạy; restart_backend.ps1 lần sau sẽ tự dừng nó).
# Quay SUT về main sau đợt usability: tools/sut_main.ps1
# Usage (gốc repo): powershell -ExecutionPolicy Bypass -File tools\usability_session.ps1
param([string]$Cloudflared = 'D:\Tools\cloudflared\cloudflared.exe')
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$ErrorActionPreference = 'Stop'
$sut = 'D:\HK7\Testing\Exercise\HW\eshop-sut'
$web = Join-Path $sut 'frontend-web'
if (-not (Test-Path $Cloudflared)) { $c = Get-Command cloudflared -ErrorAction SilentlyContinue; if ($c) { $Cloudflared = $c.Source } else { throw "Không thấy cloudflared ($Cloudflared)" } }

$branch = (git -C $sut branch --show-current).Trim()
if ($branch -ne 'usability-tunnel') {
  "SUT đang ở nhánh '$branch' → chuyển sang usability-tunnel"
  git -C $sut switch usability-tunnel | Out-Host
  if ($LASTEXITCODE -ne 0) { throw "Không chuyển được nhánh usability-tunnel" }
}

& (Join-Path $PSScriptRoot 'restart_backend.ps1')
if ($LASTEXITCODE -ne 0) { throw "backend không lên" }

# dừng Vite cũ trên :5173 (nếu có) rồi mở Vite mới
$old = Get-NetTCPConnection -State Listen -LocalPort 5173 -ErrorAction SilentlyContinue
if ($old) { $old.OwningProcess | Sort-Object -Unique | ForEach-Object { Stop-Process -Id $_ -Force } ; Start-Sleep -Milliseconds 500 }
$vite = Start-Process -FilePath 'cmd.exe' -ArgumentList '/c', 'npx vite --host 127.0.0.1 --port 5173 --strictPort' -WorkingDirectory $web -WindowStyle Minimized -PassThru
for ($i = 0; $i -lt 60; $i++) { Start-Sleep -Milliseconds 500; try { Invoke-WebRequest -UseBasicParsing 'http://127.0.0.1:5173/' | Out-Null; break } catch {} }
try { $n = (Invoke-RestMethod 'http://127.0.0.1:5173/api/products').Count; "vite :5173 xong; proxy /api → :3000: $n sản phẩm" } catch { throw "Vite/proxy /api không chạy: $_" }

$log = Join-Path $env:TEMP 'cloudflared_usability.log'
Remove-Item $log -ErrorAction SilentlyContinue
$cf = Start-Process -FilePath $Cloudflared -ArgumentList 'tunnel', '--no-autoupdate', '--url', 'http://localhost:5173', '--logfile', $log -WindowStyle Hidden -PassThru
$url = $null
for ($i = 0; $i -lt 60 -and -not $url; $i++) {
  Start-Sleep -Milliseconds 500
  if (Test-Path $log) { $m = Select-String -Path $log -Pattern 'https://[a-z0-9-]+\.trycloudflare\.com' | Select-Object -First 1; if ($m) { $url = $m.Matches[0].Value } }
}
if (-not $url) { Stop-Process -Id $cf.Id -Force -ErrorAction SilentlyContinue; throw "Không lấy được link tunnel (xem $log)" }
""
"LINK PHIÊN: $url"
"(link đổi mỗi lần chạy; gửi cho người tham gia ngay trước phiên)"
"Ctrl+C để tắt tunnel + Vite."
try {
  while (-not $cf.HasExited) { Start-Sleep -Seconds 1 }
  "cloudflared đã thoát (mã $($cf.ExitCode)) – xem $log"
} finally {
  Stop-Process -Id $cf.Id -Force -ErrorAction SilentlyContinue
  Get-NetTCPConnection -State Listen -LocalPort 5173 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
  Stop-Process -Id $vite.Id -Force -ErrorAction SilentlyContinue
  "đã tắt tunnel + Vite"
}
