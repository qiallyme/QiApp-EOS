@echo off
setlocal
IF NOT EXIST .venv (
  echo [QiMini] Creating venv...
  py -3 -m venv .venv
  call .venv\Scripts\pip install -r requirements.txt
)
call .venv\Scripts\python main.py
pause
