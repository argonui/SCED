param(
    [string]$JsonFile
)

if (-Not (Test-Path $JsonFile)) {
    Write-Host "Error: File not found: $JsonFile"
    exit 1
}

# Get the folder where the script is being run
$scriptFolder = Get-Location

# Get the base name without extension
$baseName = [System.IO.Path]::GetFileNameWithoutExtension($JsonFile)

# Create new filename
$newFileName = "LUAcoding$baseName.txt"
$outFile = Join-Path $scriptFolder $newFileName

# Extract LuaScript string (keeps escaped sequences)
$rawContent = Get-Content $JsonFile | ForEach-Object {
    if ($_ -match '"LuaScript"\s*:\s*"((?:\\.|[^"])*)"' ) {
        $matches[1]
    }
}

# Decode escaped sequences into real characters
$decoded = $rawContent -replace '\\n', "`r`n"
$decoded = $decoded -replace '\\t', "`t"
$decoded = $decoded -replace '\\r', "`r"
$decoded = $decoded -replace '\\"', '"'
$decoded = $decoded -replace '\\\\', '\'

# Save to new filename
$decoded | Set-Content $outFile -Encoding UTF8

Write-Host "Readable LuaScript saved to $outFile"

# Para usarlo hacer powershell ./get-lua-code.ps1 -JsonFile objects\PhaseTracker.d0c8fa.json desde cmd