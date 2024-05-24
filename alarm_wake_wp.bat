@echo off
:: This will create a wake timer to wake up the PC at a specific time
:: Replace 'time' with the time you want to wake up, for example, 07:00

echo Setting wake timer for the specified time
powercfg /waketimer
pause
