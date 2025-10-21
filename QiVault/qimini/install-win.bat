@echo off
py -3 -m venv .venv
call .venv\Scripts\pip install -r requirements.txt
echo [QiMini] Installed.
pause
