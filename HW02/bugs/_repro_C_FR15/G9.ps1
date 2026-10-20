. "$PSScriptRoot\prelude.ps1"
# Dựng M
$m = Send 'POST' "$base/api/products" '{"name": "repro G9 M", "price": 1000000, "category_id": 1, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers
$M = ([regex]'"id":(\d+)').Match($m).Groups[1].Value
"Dựng M -> $m"
"M TRƯỚC -> $(Send 'GET' "$base/api/products/$M" $null @{})"
$r = Send 'PUT' "$base/api/products/$M" '{"name": "", "price": 2500000, "category_id": 3, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers
"PUT name rỗng -> $r"
"M SAU -> $(Send 'GET' "$base/api/products/$M" $null @{})"
$null = Send 'DELETE' "$base/api/products/$M" $null $headers
