@echo off
chcp 65001 >nul
echo 正在啟動法輪大法書籍閱讀器...
echo.

:: 嘗試找 Python
where python >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=python
    goto :found
)

if exist "C:\Users\adminininin\AppData\Local\Programs\Python\Python311\python.exe" (
    set PYTHON=C:\Users\adminininin\AppData\Local\Programs\Python\Python311\python.exe
    goto :found
)

echo [錯誤] 找不到 Python，請安裝 Python 3 後再試。
echo 下載地址: https://www.python.org/downloads/
pause
exit /b 1

:found
echo 使用 Python: %PYTHON%
echo 伺服器地址: http://localhost:8080
echo 按 Ctrl+C 可停止伺服器
echo.

:: 開啟瀏覽器
start "" "http://localhost:8080"

:: 啟動伺服器
"%PYTHON%" -m http.server 8080 --directory "%~dp0"
