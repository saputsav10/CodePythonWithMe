@echo off
cd /d "D:\PYTHON IS ON\Python_Daily_Updates"

:: Add a timestamp to a file
echo Updated on %date% at %time% >> daily_log.txt

:: Git commands
git add .
git commit -m "Auto update on %date%"
git push origin main
