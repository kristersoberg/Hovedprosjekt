# Start MCPO Server for Open WebUI Integration
# This script activates the venv and starts the MCPO proxy

Write-Host "Starting MCPO Server..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan

# Activate virtual environment
$venvPath = ".\venv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & $venvPath
} else {
    Write-Host "ERROR: Virtual environment not found at $venvPath" -ForegroundColor Red
    Write-Host "Please create a venv first: python -m venv venv" -ForegroundColor Yellow
    exit 1
}

# Check if mcpo is installed
Write-Host "Checking if mcpo is installed..." -ForegroundColor Yellow
$mcpoCheck = & python -m pip show mcpo 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: mcpo not found in venv" -ForegroundColor Red
    Write-Host "Installing mcpo..." -ForegroundColor Yellow
    & python -m pip install mcpo
}

# Start MCPO server
Write-Host "`nStarting MCPO proxy server on port 8001..." -ForegroundColor Green
Write-Host "API Key: cisco-mcp-secret" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "========================================`n" -ForegroundColor Cyan

# Run MCPO (call the executable directly)
& .\venv\Scripts\mcpo.exe --port 8001 --api-key "cisco-mcp-secret" -- python mcp_server\server.py
