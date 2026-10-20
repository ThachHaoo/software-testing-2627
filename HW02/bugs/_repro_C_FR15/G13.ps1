. "$PSScriptRoot\prelude.ps1"
"POST price Infinity -> $(Send 'POST' "$base/api/products" '{"name": "repro G13", "price": Infinity, "category_id": 2, "description": "repro", "imageUrl": "https://placehold.co/300"}' $headers)"
