@echo off
:loop
python textbaseapp.py
timeout /t 3 >nul
cls
goto loop
pause