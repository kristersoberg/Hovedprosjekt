@echo off
REM Quick test runner for MCP integration

echo Running MCP Integration Tests...
echo.

call venv\Scripts\activate.bat

python tests\test_mcp_integration.py

if errorlevel 1 (
    echo.
    echo [X] Tests FAILED
    pause
    exit /b 1
) else (
    echo.
    echo [OK] Tests PASSED
    pause
    exit /b 0
)
