@echo off
REM Run the Flask dashboard application
cd /d "%~dp0"
echo Starting SLA Dashboard...
echo.
py run_app.py
pause
