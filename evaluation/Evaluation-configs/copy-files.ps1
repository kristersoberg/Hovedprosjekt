param(
    [string]$SourceDir = "."
)

for ($switch = 1; $switch -le 10; $switch++) {
    $switchNum = "{0:D2}" -f $switch
    $original = Join-Path $SourceDir "switch-${switchNum}.txt"

    if (-not (Test-Path $original)) {
        Write-Warning "$original not found, skipping."
        continue
    }

    for ($copy = 1; $copy -le 10; $copy++) {
        $dest = Join-Path $SourceDir "switch-${switchNum}-${copy}.txt"
        Copy-Item $original $dest
        Write-Host "Created $dest"
    }
}

Write-Host "Done. 100 files created."