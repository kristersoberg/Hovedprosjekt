@echo off
REM Start MCPO Server for Open WebUI Integration
REM This batch file activates venv and starts MCPO

echo Starting MCPO Server...
echo ========================================

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if activation worked
if errorlevel 1 (
    echo ERROR: Could not activate virtual environment
    echo Please ensure venv exists: python -m venv venv
    pause
    exit /b 1
)

echo Virtual environment activated!

REM Install mcpo if not present
pip show mcpo >nul 2>&1
if errorlevel 1 (
    echo Installing mcpo...
    pip install mcpo
)

echo.
echo Starting MCPO proxy server on port 8001...
echo API Key: cisco-mcp-secret
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Run MCPO (call the executable directly)
venv\Scripts\mcpo.exe --port 8001 --api-key "cisco-mcp-secret" -- python mcp_server\server.py

pause