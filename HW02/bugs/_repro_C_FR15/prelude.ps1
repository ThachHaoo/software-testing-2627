[Console]::OutputEncoding = [Text.Encoding]::UTF8
# Dùng chung cho các bước tái hiện API (Windows PowerShell 5.1)
$base = 'http://localhost:3000'
function Send($method, $uri, $body, $h, $ct = 'application/json') {
  try {
    if ($body -ne $null) {
      $r = Invoke-WebRequest -UseBasicParsing -Method $method -Uri $uri -Headers $h -ContentType $ct -Body ([Text.Encoding]::UTF8.GetBytes($body))
    } else {
      $r = Invoke-WebRequest -UseBasicParsing -Method $method -Uri $uri -Headers $h
    }
    "HTTP $($r.StatusCode) $($r.Content)"
  } catch {
    $resp = $_.Exception.Response
    $s = $resp.GetResponseStream(); $s.Position = 0
    $rd = New-Object IO.StreamReader($s)
    "HTTP $([int]$resp.StatusCode) $($rd.ReadToEnd())"
  }
}
$login = Invoke-WebRequest -UseBasicParsing -Method Post -Uri "$base/api/login" -ContentType 'application/json' -Body ([Text.Encoding]::UTF8.GetBytes('{"email":"admin@eshop.com","password":"Admin123!"}'))
$TA = ($login.Content | ConvertFrom-Json).token
$headers = @{ Authorization = "Bearer $TA" }
