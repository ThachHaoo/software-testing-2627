. "$PSScriptRoot\prelude.ps1"
"POST text/plain -> $(Send 'POST' "$base/api/products" '{"name": "repro G14", "price": 1500000, "category_id": 2, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers 'text/plain')"
