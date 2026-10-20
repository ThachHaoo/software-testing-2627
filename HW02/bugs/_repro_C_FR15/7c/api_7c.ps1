[Console]::OutputEncoding = [Text.Encoding]::UTF8
# 7c — chạy bước tái hiện SV viết cho BUG-41…44, 46, 47, 48 (Windows PowerShell 5.1)
# Restart backend trước mỗi BUG và sau BUG cuối. Không gửi Authorization trừ BUG-47 (SV không ghi token ở các BUG khác).
$base = 'http://localhost:3000'
$restart = Join-Path $PSScriptRoot 'restart_backend.ps1'
function Restart { $o = powershell -ExecutionPolicy Bypass -File $restart; "   [$o]" }
function Send($method, $uri, $body, $h, $ct = 'application/json', [switch]$NoCt) {
  try {
    if ($body -eq $null) { $r = Invoke-WebRequest -UseBasicParsing -Method $method -Uri $uri -Headers $h }
    elseif ($NoCt) { $r = Invoke-WebRequest -UseBasicParsing -Method $method -Uri $uri -Headers $h -Body ([Text.Encoding]::UTF8.GetBytes($body)) }
    else { $r = Invoke-WebRequest -UseBasicParsing -Method $method -Uri $uri -Headers $h -ContentType $ct -Body ([Text.Encoding]::UTF8.GetBytes($body)) }
    $ctype = $r.Headers['Content-Type']; "HTTP $($r.StatusCode) [$ctype] $($r.Content)"
  } catch {
    $resp = $_.Exception.Response
    $s = $resp.GetResponseStream(); $s.Position = 0
    $rd = New-Object IO.StreamReader($s)
    "HTTP $([int]$resp.StatusCode) [$($resp.ContentType)] $($rd.ReadToEnd())"
  }
}
function Count { (ConvertFrom-Json (Invoke-WebRequest -UseBasicParsing -Uri "$base/api/products").Content).Count }
function Short($s) { $s = $s -replace '(x{20})x+', '$1…'; $s = $s -replace '\s*\r?\n\s*', ' '; if ($s.Length -gt 260) { $s.Substring(0, 260) + '…' } else { $s } }
function Post($label, $json, $h = @{}) {
  $n0 = Count; $r = Send 'POST' "$base/api/products" $json $h; $n1 = Count
  $id = ([regex]'"id":(\d+)').Match($r).Groups[1].Value
  # bản ghi mới đọc từ danh sách GET /api/products (đúng bước SV); không gọi GET /api/products/:id vì id chẵn + price null làm backend dừng (server.js:162)
  $rec = if ($id) { Short (ConvertTo-Json -Compress ((ConvertFrom-Json (Invoke-WebRequest -UseBasicParsing -Uri "$base/api/products").Content) | Where-Object { $_.id -eq [int]$id })) } else { '—' }
  "$label -> $(Short $r); bản ghi $n0 → $n1; bản ghi id $id trong GET /api/products: $rec"
}
function Put($label, $id, $json, $h = @{}) {
  $m0 = Short (Send 'GET' "$base/api/products/$id" $null @{}); $n0 = Count
  $r = Send 'PUT' "$base/api/products/$id" $json $h; $n1 = Count
  $m1 = Short (Send 'GET' "$base/api/products/$id" $null @{})
  "$label -> $(Short $r); bản ghi $n0 → $n1"; "      M TRƯỚC: $m0"; "      M SAU:   $m1"
}
$x256 = 'x' * 256; $x300 = 'x' * 300
function P($name, $price, $cat) { "{`"name`": $name, `"price`": $price, `"category_id`": $cat, `"description`": `"Mô tả 7c`", `"imageUrl`": `"https://placehold.co/300`"}" }

"===== BUG-41 (POST /api/products, các payload vi phạm; không gửi token)"; Restart
Post 'name ""          (TC-23/84)' (P '""' 1500000 2)
Post 'name 256×x       (TC-100)' (P "`"$x256`"" 1500000 2)
Post 'name 300×x       (TC-24)' (P "`"$x300`"" 1500000 2)
Post 'name "   "       (TC-25)' (P '"   "' 1500000 2)
Post 'name null        (TC-26)' (P 'null' 1500000 2)
Post 'name 123         (TC-27)' (P '123' 1500000 2)
Post 'price -1000      (TC-28)' (P '"SP 7c 28"' -1000 2)
Post 'price -999999999999 (TC-208)' (P '"SP 7c 208"' -999999999999 2)
Post 'price 0          (TC-101)' (P '"SP 7c 101"' 0 2)
Post 'price 1e-324     (TC-214)' (P '"SP 7c 214"' '1e-324' 2)
Post 'price null       (TC-29)' (P '"SP 7c 29"' 'null' 2)
Post 'price "abc"      (TC-30)' (P '"SP 7c 30"' '"abc"' 2)
Post 'price "100000"   (TC-31)' (P '"SP 7c 31"' '"100000"' 2)
Post 'category 999     (TC-32)' (P '"SP 7c 32"' 1500000 999)
Post 'category null    (TC-33)' (P '"SP 7c 33"' 1500000 'null')
Post 'category "abc"   (TC-34)' (P '"SP 7c 34"' 1500000 '"abc"')

"===== BUG-42 (PUT /api/products/1 — sản phẩm seed đang tồn tại; không gửi token)"; Restart
Put 'name ""          (TC-35/106)' 1 (P '""' 2500000 3)
Put 'name 256×x       (TC-112)' 1 (P "`"$x256`"" 2500000 3)
Put 'name 300×x       (TC-36)' 1 (P "`"$x300`"" 2500000 3)
Put 'name "   "       (TC-37)' 1 (P '"   "' 2500000 3)
Put 'name null        (TC-38)' 1 (P 'null' 2500000 3)
Put 'name 123         (TC-39)' 1 (P '123' 2500000 3)
Put 'price -1000      (TC-40)' 1 (P '"Sua 7c 40"' -1000 3)
Put 'price 0          (TC-113)' 1 (P '"Sua 7c 113"' 0 3)
Put 'price null       (TC-41)' 1 (P '"Sua 7c 41"' 'null' 3)
Put 'price "abc"      (TC-42)' 1 (P '"Sua 7c 42"' '"abc"' 3)
Put 'price "100000"   (TC-43)' 1 (P '"Sua 7c 43"' '"100000"' 3)
Put 'category 999     (TC-44)' 1 (P '"Sua 7c 44"' 2500000 999)
Put 'category null    (TC-45)' 1 (P '"Sua 7c 45"' 2500000 'null')
Put 'category "abc"   (TC-46)' 1 (P '"Sua 7c 46"' 2500000 '"abc"')

"===== BUG-43 (POST, price: Infinity thô, Content-Type application/json)"; Restart
Post 'price Infinity   (TC-209)' (P '"SP 7c 209"' 'Infinity' 2)

"===== BUG-44 (POST không có Content-Type: application/json)"; Restart
$n0 = Count; $r = Send 'POST' "$base/api/products" (P '"SP 7c 211a"' 1500000 2) @{} -NoCt; "a) không truyền -ContentType (PS 5.1 tự gửi application/x-www-form-urlencoded) -> $(Short $r); bản ghi $n0 → $(Count)"
$n0 = Count; $r = Send 'POST' "$base/api/products" (P '"SP 7c 211b"' 1500000 2) @{} 'text/plain'; "b) Content-Type: text/plain (như TC-211) -> $(Short $r); bản ghi $n0 → $(Count)"

"===== BUG-46 (id 999 không tồn tại)"; Restart
$n0 = Count; "GET    /api/products/999 -> $(Send 'GET' "$base/api/products/999" $null @{}); bản ghi $n0 → $(Count)"
$n0 = Count; "PUT    /api/products/999 -> $(Send 'PUT' "$base/api/products/999" (P '"Sua 7c 48"' 2500000 3) @{}); bản ghi $n0 → $(Count)"
$n0 = Count; "DELETE /api/products/999 -> $(Send 'DELETE' "$base/api/products/999" $null @{}); bản ghi $n0 → $(Count)"
"   GET /api/products (danh sách sau 3 request): $((ConvertFrom-Json (Invoke-WebRequest -UseBasicParsing -Uri "$base/api/products").Content | ForEach-Object { $_.id }) -join ',')"

"===== BUG-47 (không token / token sai / token hết hạn / token user)"; Restart
$tu = (ConvertFrom-Json (Invoke-WebRequest -UseBasicParsing -Method Post -Uri "$base/api/login" -ContentType 'application/json' -Body ([Text.Encoding]::UTF8.GetBytes('{"email":"test@eshop.com","password":"Test1234!"}'))).Content)
"   token user: role trong phản hồi login = $($tu.user.role)"
$texp = node -e "const jwt=require('D:/HK7/Testing/Exercise/HW/eshop-sut/backend/node_modules/jsonwebtoken');console.log(jwt.sign({id:1,email:'admin@eshop.com',role:'admin',exp:Math.floor(Date.now()/1000)-3600},'super_secret_key_that_should_not_be_here'))"
$cases = [ordered]@{ 'không token' = @{}; 'token sai abc.def.ghi' = @{ Authorization = 'Bearer abc.def.ghi' }; 'token hết hạn (exp = 1 giờ trước)' = @{ Authorization = "Bearer $texp" }; 'token user test@eshop.com' = @{ Authorization = "Bearer $($tu.token)" } }
$pid_ = 1; $did = 2
foreach ($k in $cases.Keys) {
  Post "POST   [$k]" (P "`"SP 7c 47 $k`"" 1500000 2) $cases[$k]
  Put "PUT    /$pid_ [$k]" $pid_ (P "`"Sua 7c 47 $k`"" 2500000 3) $cases[$k]
  $n0 = Count; $r = Send 'DELETE' "$base/api/products/$did" $null $cases[$k]; "DELETE /$did [$k] -> $r; bản ghi $n0 → $(Count); GET /api/products/$did -> $(Send 'GET' "$base/api/products/$did" $null @{})"
  $did++
}

"===== BUG-48 (GET /api/products/2)"; Restart
$r = Invoke-WebRequest -UseBasicParsing -Uri "$base/api/products/2"; "GET /api/products/2 -> HTTP $($r.StatusCode) $($r.Content)"
"   kiểu price trong JSON: $((ConvertFrom-Json $r.Content).price.GetType().Name)"

"===== kết thúc"; Restart
