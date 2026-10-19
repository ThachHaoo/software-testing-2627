# Xuất commit log UTF-8 cho một bài (chạy ở gốc repo, SAU commit cuối cùng).
# Dùng: powershell -ExecutionPolicy Bypass -File tools\export_commit_log.ps1 HW02
param([string]$Hw = "HW02")
$out = "$Hw/appendix/commit_log.txt"
git -c i18n.logOutputEncoding=utf-8 log --reverse --name-status --date=format:"%H:%M %d/%m/%Y" `
    --pretty=format:"%h | %ad | %an | %s" -- $Hw | Out-File -Encoding utf8 $out
Write-Host "Đã ghi $out ($((Get-Content $out).Count) dòng). Nhớ commit file này rồi mới zip."
