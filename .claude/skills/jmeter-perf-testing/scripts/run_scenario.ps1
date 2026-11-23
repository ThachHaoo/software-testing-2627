param(
  [Parameter(Mandatory = $true)][string]$Jmx,
  [Parameter(Mandatory = $true)][string]$OutDir,
  [string]$BackendDir = '',
  [string]$JmeterHome = 'D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3',
  [string]$Heap = '-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m',
  [int]$SampleSec = 1,
  [int]$Port = 3000,
  [switch]$NoRestart,
  [switch]$StopBackend,
  [switch]$Official,
  [string]$Note = ''
)
<#
  Chạy MỘT scenario JMeter ở chế độ non-GUI (H2=a) và gom bằng chứng vào <OutDir>\<plan>_<yyyyMMddTHHmmss>\:
    1. restart backend EShop (CSDL seed lại, xoá trạng thái khoá) – trừ khi -NoRestart
    2. java -jar ApacheJMeter.jar -n -t <jmx> -l <plan>.jtl -e -o html -j jmeter.log (tiến trình riêng, biết PID)
    3. trong lúc JMeter chạy: mỗi -SampleSec giây lấy mẫu theo PID backend (node) + PID JMeter (java):
       CPU% (theo cả máy = Δ thời gian CPU / Δ thời gian thực / số luồng logic), WorkingSet, PrivateBytes, RAM trống
       → monitor.csv. Lấy theo PID (Get-Process -Id), không theo tên instance counter (node#1… đổi khi có nhiều node).
    4. ghi RUN.md (lượt chính thức?, giờ ISO, hostname, heap JMeter, RAM trống lúc bắt đầu, commit repo + SUT,
       sha256 jmx, lệnh, exit code, số dòng jtl)
  Gọi java trực tiếp (không qua jmeter.bat) để không bị lệnh "pause" của jmeter.bat treo khi JMeter lỗi.

  Ví dụ:
    powershell -ExecutionPolicy Bypass -File .claude\skills\jmeter-perf-testing\scripts\run_scenario.ps1 `
      -Jmx HW05\testplans\23120255_Load_20261125.jmx -OutDir HW05\runs
#>
$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
if (-not $BackendDir) { $BackendDir = Join-Path (Split-Path $repo -Parent) 'eshop-sut\backend' }
$Jmx = (Resolve-Path $Jmx).Path
if (-not (Test-Path (Join-Path $BackendDir 'server.js'))) { throw "Không thấy server.js trong $BackendDir" }
$jar = Join-Path $JmeterHome 'bin\ApacheJMeter.jar'
if (-not (Test-Path $jar)) { throw "Không thấy $jar (sửa -JmeterHome)" }
$env:JMETER_HOME = $JmeterHome

$plan = [IO.Path]::GetFileNameWithoutExtension($Jmx)
$stamp = Get-Date -Format 'yyyyMMddTHHmmss'
New-Item -ItemType Directory -Force $OutDir | Out-Null
$run = Join-Path (Resolve-Path $OutDir).Path "$($plan)_$stamp"
if (Test-Path $run) { throw "$run đã tồn tại" }
New-Item -ItemType Directory $run | Out-Null
$base = "http://localhost:$Port"

function Wait-Backend {
  for ($i = 0; $i -lt 60; $i++) {
    try { $r = Invoke-WebRequest -UseBasicParsing "$base/api/products" -TimeoutSec 2; if ($r.StatusCode -eq 200) { return $true } } catch {}
    Start-Sleep -Milliseconds 500
  }
  return $false
}

# 1. backend
$restartAt = $null
if (-not $NoRestart) {
  Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty OwningProcess -Unique | ForEach-Object { Stop-Process -Id $_ -Force }
  Start-Sleep -Milliseconds 800
  # Không dùng Start-Process -Redirect*: khi đó node kế thừa handle stdout/stderr của tiến trình gọi, lệnh gọi script
  # qua pipe (CI, Claude Code) treo tới khi backend tắt. cmd /c qua ShellExecute không kế thừa handle; log ghi bằng '>'.
  $outLog = Join-Path $run 'backend.out.log'; $errLog = Join-Path $run 'backend.err.log'
  Start-Process -FilePath 'cmd.exe' -ArgumentList "/c node server.js > `"$outLog`" 2> `"$errLog`"" `
    -WorkingDirectory $BackendDir -WindowStyle Hidden
  $restartAt = (Get-Date).ToString('o')
  if (-not (Wait-Backend)) { throw "Backend không lên sau 30 s (xem $errLog)" }
  $nodePid = (Get-NetTCPConnection -State Listen -LocalPort $Port | Select-Object -First 1).OwningProcess
} else {
  $c = Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue | Select-Object -First 1
  if (-not $c) { throw "Không có tiến trình nghe cổng $Port (bỏ -NoRestart để tự khởi động)" }
  $nodePid = $c.OwningProcess
}

# 2. JMeter non-GUI (tiến trình riêng để biết PID)
$jtl = Join-Path $run "$plan.jtl"
$html = Join-Path $run 'html'
$jargs = @($Heap -split ' ' | Where-Object { $_ }) + @('-jar', $jar, '-n', '-t', $Jmx, '-l', $jtl, '-e', '-o', $html,
          '-j', (Join-Path $run 'jmeter.log'), '-Jjmeter.save.saveservice.output_format=csv')
$quoted = $jargs | ForEach-Object { if ($_ -match '\s') { '"' + $_ + '"' } else { $_ } }
$os0 = Get-CimInstance Win32_OperatingSystem
$freeStartMB = [Math]::Round($os0.FreePhysicalMemory / 1024)
$totalMB = [Math]::Round($os0.TotalVisibleMemorySize / 1024)
$ncpu = [Environment]::ProcessorCount
$start = (Get-Date).ToString('o')
$jp = Start-Process -FilePath 'java' -ArgumentList $quoted -NoNewWindow -PassThru `
        -RedirectStandardOutput (Join-Path $run 'jmeter.console.txt') -RedirectStandardError (Join-Path $run 'jmeter.console.err.txt')
$null = $jp.Handle   # PS 5.1: giữ handle để đọc được ExitCode sau khi tiến trình kết thúc

# 3. lấy mẫu theo PID tới khi JMeter kết thúc
$mon = Join-Path $run 'monitor.csv'
$sw = New-Object IO.StreamWriter($mon, $false, (New-Object Text.UTF8Encoding $false))
$sw.WriteLine('time_iso,elapsed_s,role,pid,cpu_pct_machine,working_set_mb,private_mb,avail_mb')
$prev = @{}; $t0 = Get-Date
while (-not $jp.HasExited) {
  $now = Get-Date
  $avail = [Math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1024)
  foreach ($r in @(@('backend', $nodePid), @('jmeter', $jp.Id))) {
    $p = Get-Process -Id $r[1] -ErrorAction SilentlyContinue
    if (-not $p) { continue }
    $cpuT = $p.TotalProcessorTime.TotalMilliseconds
    $pct = ''
    if ($prev.ContainsKey($r[0])) {
      $dt = ($now - $prev[$r[0]][1]).TotalMilliseconds
      if ($dt -gt 0) { $pct = [Math]::Round(100 * ($cpuT - $prev[$r[0]][0]) / $dt / $ncpu, 2) }
    }
    $prev[$r[0]] = @($cpuT, $now)
    $sw.WriteLine(('{0},{1},{2},{3},{4},{5},{6},{7}' -f $now.ToString('o'), [Math]::Round(($now - $t0).TotalSeconds, 1),
      $r[0], $r[1], $pct, [Math]::Round($p.WorkingSet64 / 1MB, 1), [Math]::Round($p.PrivateMemorySize64 / 1MB, 1), $avail))
  }
  $sw.Flush()
  Start-Sleep -Seconds $SampleSec
}
$sw.Close()
$jp.WaitForExit()
$exit = $jp.ExitCode
$end = (Get-Date).ToString('o')
Get-Content (Join-Path $run 'jmeter.console.txt') -Tail 8 | ForEach-Object { Write-Host $_ }

# 4. RUN.md
$ErrorActionPreference = 'Continue'   # java -version/git ghi ra stderr – PS 5.1 không được coi là lỗi
if ($StopBackend) { Stop-Process -Id $nodePid -Force -ErrorAction SilentlyContinue }
$rows = if (Test-Path $jtl) { (Get-Content $jtl | Measure-Object -Line).Lines - 1 } else { 0 }
$jtlBytes = if (Test-Path $jtl) { (Get-Item $jtl).Length } else { 0 }
$sha = (Get-FileHash $Jmx -Algorithm SHA256).Hash.ToLower()
$gitRepo = (git -C $repo rev-parse --short HEAD) 2>$null
$gitSut = (git -C $BackendDir rev-parse --short HEAD) 2>$null
$java = ((& java -version 2>&1) | Select-Object -First 1 | ForEach-Object { "$_" })
$cpu = (Get-CimInstance Win32_Processor | Select-Object -First 1)
$md = @"
# RUN – $plan

| Mục | Giá trị |
|---|---|
| Lượt chính thức | $(if ($Official) { 'CÓ (-Official) – số liệu dùng trong report' } else { 'KHÔNG (lượt thử / smoke – export-ignore khi nộp)' }) |
| Ghi chú | $Note |
| Hostname | $env:COMPUTERNAME |
| CPU / luồng logic | $($cpu.Name) / $($cpu.NumberOfLogicalProcessors) |
| Bắt đầu JMeter (ISO) | $start |
| Kết thúc JMeter (ISO) | $end |
| Restart backend lúc | $(if ($restartAt) { $restartAt } else { 'không restart (-NoRestart)' }) |
| PID backend (node) / JMeter (java) | $nodePid / $($jp.Id) |
| Test plan | ``$Jmx`` |
| sha256 test plan | ``$sha`` |
| Commit repo / SUT | ``$gitRepo`` / ``$gitSut`` |
| JMeter / Java | $JmeterHome / $java |
| Heap JMeter | ``$Heap`` |
| RAM trống lúc bắt đầu / tổng | $freeStartMB MB / $totalMB MB |
| Exit code JMeter | $exit |
| jtl | ``$plan.jtl`` – $rows dòng, $jtlBytes byte |
| HTML report | ``html/index.html`` (số liệu: ``html/statistics.json``) |
| Giám sát tài nguyên | ``monitor.csv`` (mỗi $SampleSec s, theo PID; cpu_pct_machine = % của cả máy, $ncpu luồng logic) |

Lệnh JMeter:

``````
java $($jargs -join ' ')
``````

Các bước reset trước lượt: $(if ($NoRestart) { 'không reset' } else { "dừng tiến trình nghe cổng $Port → ``node server.js`` (CSDL DROP + seed lại, mất user đăng ký thêm và trạng thái khoá) → chờ ``GET /api/products`` = 200" }).
"@
Set-Content -Path (Join-Path $run 'RUN.md') -Value $md -Encoding UTF8
Write-Host "Xong: $run (exit $exit, $rows dòng jtl)"
exit $exit
