@echo off
chcp 65001 >nul

:: Try to find Python
where python >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python
    goto :found
)

if exist "C:\Users\adminininin\AppData\Local\Programs\Python\Python311\python.exe" (
    set "PYTHON=C:\Users\adminininin\AppData\Local\Programs\Python\Python311\python.exe"
    goto :found
)

echo Cannot find Python. Please install Python 3.
pause
exit /b 1

:found
start "" "http://localhost:8080"
"%PYTHON%" -m http.server 8080 --directory "%~dp0"
