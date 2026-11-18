param([string]$Hw = "")
# Xuất commit log UTF-8 cho một bài (chạy ở gốc repo, SAU commit cuối cùng).
# Dùng: powershell -ExecutionPolicy Bypass -File tools\export_commit_log.ps1          # bài hiện tại theo tools/hw.toml (khoá hw)
#       powershell -ExecutionPolicy Bypass -File tools\export_commit_log.ps1 HW04     # ghi đè: chỉ định bài
# Chỉ ghi <Hw>/appendix/commit_log.txt — không đụng bài khác.
if (-not $Hw) {
    $line = Get-Content -Encoding UTF8 "tools/hw.toml" | Where-Object { $_ -match '^\s*hw\s*=\s*"([^"]+)"' } | Select-Object -First 1
    if (-not $line) { Write-Error "Không đọc được khoá hw trong tools/hw.toml; truyền tên bài làm tham số."; exit 1 }
    $Hw = [regex]::Match($line, '"([^"]+)"').Groups[1].Value
}
if (-not (Test-Path "$Hw/appendix")) { Write-Error "Không có thư mục $Hw/appendix"; exit 1 }
$out = "$Hw/appendix/commit_log.txt"
git -c i18n.logOutputEncoding=utf-8 log --reverse --name-status --date=format:"%H:%M %d/%m/%Y" `
    --pretty=format:"%h | %ad | %an | %s" -- $Hw | Out-File -Encoding utf8 $out
Write-Host "Đã ghi $out ($((Get-Content $out).Count) dòng). Nhớ commit file này rồi mới zip."
