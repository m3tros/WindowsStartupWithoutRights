@echo off
chcp 1251>nul
color 0f
echo Metros Software (script type: Windows Startup Without Permission). (version 1.0 2022).
echo.
echo Current path: %cd%
set /p mswswp_filename=Enter the full path to the program to run it: 
cmd /min /C "set __COMPAT_LAYE 	R=RunAsInVoker && start %mswswp_filename%
