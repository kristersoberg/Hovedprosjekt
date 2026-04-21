# Test runner for Cisco Documentation System

Write-Host "Running all tests..." -ForegroundColor Cyan
Write-Host ""

# Activate venv
& .\venv\Scripts\Activate.ps1

# Run tests
& python tests\run_tests.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[OK] Tests PASSED" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "[X] Tests FAILED" -ForegroundColor Red
    exit 1
}
