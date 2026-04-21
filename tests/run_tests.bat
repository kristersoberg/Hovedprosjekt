@echo off
REM Test runner for Cisco Documentation System

echo Running all tests...
echo.

call venv\Scripts\activate.bat

python tests\run_tests.py

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
