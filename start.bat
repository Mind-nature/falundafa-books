@echo off
chcp 65001 >nul
cd /d "%~dp0"

:: Try to find Python
where python >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python
    goto :found
)

:: Fallback: common per-user Python install locations
for %%V in (313 312 311 310) do (
    if exist "%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe" (
        set "PYTHON=%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe"
        goto :found
    )
)

py --version >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=py
    goto :found
)

echo Cannot find Python. Please install Python 3.
pause
exit /b 1

:found
start "" "http://localhost:8000"
"%PYTHON%" -m http.server 8000
