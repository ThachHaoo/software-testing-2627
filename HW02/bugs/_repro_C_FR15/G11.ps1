. "$PSScriptRoot\prelude.ps1"
$lu = Invoke-WebRequest -UseBasicParsing -Method Post -Uri "$base/api/login" -ContentType 'application/json' -Body ([Text.Encoding]::UTF8.GetBytes('{"email":"test@eshop.com","password":"Test1234!"}'))
$TU = ($lu.Content | ConvertFrom-Json).token
# 1) POST không có header Authorization
$p = Send 'POST' "$base/api/products" '{"name": "repro G11 no token", "price": 1500000, "category_id": 2, "description": "repro", "imageUrl": "https://placehold.co/300"}' @{}
"1) POST không token -> $p"
$P = ([regex]'"id":(\d+)').Match($p).Groups[1].Value
# Dựng M bằng token admin
$m = Send 'POST' "$base/api/products" '{"name": "repro G11 M", "price": 1000000, "category_id": 1, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers
$M = ([regex]'"id":(\d+)').Match($m).Groups[1].Value
# 2) PUT với token không hợp lệ
"2) PUT token sai -> $(Send 'PUT' "$base/api/products/$M" '{"name": "repro G11 sua bang token sai", "price": 2500000, "category_id": 3, "description": "repro", "imageUrl": "https://placehold.co/300"}' @{ Authorization = 'Bearer abc.def.ghi' })"
"   M SAU -> $(Send 'GET' "$base/api/products/$M" $null @{})"
# 3) DELETE với token role user (test@eshop.com)
"3) DELETE token user -> $(Send 'DELETE' "$base/api/products/$M" $null @{ Authorization = "Bearer $TU" })"
"   M SAU -> $(Send 'GET' "$base/api/products/$M" $null @{})"
if ($P) { $null = Send 'DELETE' "$base/api/products/$P" $null $headers }
