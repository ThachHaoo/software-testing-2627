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
    2. typeperf ghi CPU/RAM tiến trình node (PID backend) + CPU tổng + RAM trống ra typeperf_node.csv mỗi -SampleSec giây
    3. java -jar ApacheJMeter.jar -n -t <jmx> -l <plan>.jtl -e -o html -j jmeter.log -Jlistener.dir=<run>
    4. dừng typeperf, ghi RUN.md (giờ ISO, hostname, commit repo + SUT, sha256 jmx, lệnh, exit code, số dòng jtl)
  Gọi java trực tiếp (không qua jmeter.bat) để không bị lệnh "pause" của jmeter.bat treo khi JMeter lỗi.
  "% Processor Time" của tiến trình là tổng trên mọi lõi (có thể > 100) – chia cho số luồng logic khi báo cáo.

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

# 2. typeperf theo PID
$inst = (Get-Counter '\Process(node*)\ID Process' -ErrorAction SilentlyContinue).CounterSamples |
          Where-Object { [int]$_.CookedValue -eq $nodePid } | Select-Object -First 1 -ExpandProperty InstanceName
$tpCsv = Join-Path $run 'typeperf_node.csv'
$tp = $null
if ($inst) {
  $ctr = @("\Process($inst)\% Processor Time", "\Process($inst)\Working Set - Private", "\Process($inst)\Private Bytes",
           '\Processor(_Total)\% Processor Time', '\Memory\Available MBytes') | ForEach-Object { '"' + $_ + '"' }
  $tp = Start-Process -FilePath 'typeperf' -ArgumentList ($ctr + @('-si', $SampleSec, '-f', 'CSV', '-o', "`"$tpCsv`"", '-y')) `
          -WindowStyle Hidden -PassThru
} else { Write-Warning "Không tìm được instance counter cho PID $nodePid – bỏ typeperf" }

# 3. JMeter non-GUI
$jtl = Join-Path $run "$plan.jtl"
$html = Join-Path $run 'html'
$jargs = @($Heap -split ' ' | Where-Object { $_ }) + @('-jar', $jar, '-n', '-t', $Jmx, '-l', $jtl, '-e', '-o', $html,
          '-j', (Join-Path $run 'jmeter.log'), "-Jlistener.dir=$run", '-Jjmeter.save.saveservice.output_format=csv')
$start = (Get-Date).ToString('o')
$ErrorActionPreference = 'Continue'   # JMeter/log4j ghi cảnh báo ra stderr – PS 5.1 không được coi là lỗi
$console = & java @jargs 2>&1 | ForEach-Object { $line = "$_"; Write-Host $line; $line }
$exit = $LASTEXITCODE
# Tee-Object của PS 5.1 ghi UTF-16 → tự ghi UTF-8 không BOM
[IO.File]::WriteAllLines((Join-Path $run 'jmeter.console.txt'), [string[]]@($console), (New-Object Text.UTF8Encoding $false))
$end = (Get-Date).ToString('o')

# 4. dừng typeperf, RUN.md
if ($tp) { Start-Sleep -Seconds ([Math]::Max(1, $SampleSec)); Stop-Process -Id $tp.Id -Force -ErrorAction SilentlyContinue }
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
| PID node / instance counter | $nodePid / $inst |
| Test plan | ``$Jmx`` |
| sha256 test plan | ``$sha`` |
| Commit repo / SUT | ``$gitRepo`` / ``$gitSut`` |
| JMeter / Java | $JmeterHome / $java |
| Heap JMeter | ``$Heap`` |
| Exit code JMeter | $exit |
| jtl | ``$plan.jtl`` – $rows dòng, $jtlBytes byte |
| HTML report | ``html/index.html`` (số liệu: ``html/statistics.json``) |
| typeperf | ``typeperf_node.csv`` (mỗi $SampleSec s; % Processor Time của tiến trình = tổng các lõi) |

Lệnh JMeter:

``````
java $($jargs -join ' ')
``````

Các bước reset trước lượt: $(if ($NoRestart) { 'không reset' } else { "dừng tiến trình nghe cổng $Port → ``node server.js`` (CSDL DROP + seed lại, mất user đăng ký thêm và trạng thái khoá) → chờ ``GET /api/products`` = 200" }).
"@
Set-Content -Path (Join-Path $run 'RUN.md') -Value $md -Encoding UTF8
Write-Host "Xong: $run (exit $exit, $rows dòng jtl)"
exit $exit
