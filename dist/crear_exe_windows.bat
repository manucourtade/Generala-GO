@echo off
setlocal

cd /d "%~dp0.."

if not exist ".venv" (
    py -3 -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
pyinstaller main.spec

echo.
echo Ejecutable de Windows generado en: dist\main.exe
echo Ejecutable de Linux existente: dist\main
pause
