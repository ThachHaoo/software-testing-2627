. "$PSScriptRoot\prelude.ps1"
# POST /api/products với dữ liệu vi phạm FR-15.2 / FR-15.3 / FR-15.4 (token admin)
$r1 = Send 'POST' "$base/api/products" '{"name": "", "price": 1500000, "category_id": 2, "description": "repro G8", "imageUrl": "https://placehold.co/300"}' $headers; "1) name rỗng      -> $r1"
$r2 = Send 'POST' "$base/api/products" '{"name": "repro G8 gia am", "price": -1000, "category_id": 2, "description": "repro G8", "imageUrl": "https://placehold.co/300"}' $headers; "2) price -1000    -> $r2"
$r3 = Send 'POST' "$base/api/products" '{"name": "repro G8 dm 999", "price": 1500000, "category_id": 999, "description": "repro G8", "imageUrl": "https://placehold.co/300"}' $headers; "3) category 999   -> $r3"
foreach ($r in @($r1, $r2, $r3)) { $id = ([regex]'"id":(\d+)').Match($r).Groups[1].Value; if ($id) { "   GET /api/products/$id -> $(Send 'GET' "$base/api/products/$id" $null @{})"; $null = Send 'DELETE' "$base/api/products/$id" $null $headers } }
