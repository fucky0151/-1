@echo off
cd /d "%~dp0"
python build1.py
start "" "%~dp0index.html"
