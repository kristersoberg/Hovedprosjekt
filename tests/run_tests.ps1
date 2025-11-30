# Quick test runner for MCP integration

Write-Host "Running MCP Integration Tests..." -ForegroundColor Cyan
Write-Host ""

# Activate venv
& .\venv\Scripts\Activate.ps1

# Run tests
& python tests\test_mcp_integration.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[OK] Tests PASSED" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "[X] Tests FAILED" -ForegroundColor Red
    exit 1
}
