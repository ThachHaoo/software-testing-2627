. "$PSScriptRoot\prelude.ps1"
"GET /api/products/2 -> $(Send 'GET' "$base/api/products/2" $null @{})"
"GET /api/products/1 -> $(Send 'GET' "$base/api/products/1" $null @{})"
