@echo off
title MAR Toolchain Manager

:menu
cls
echo ==============================
echo        MAR SYSTEM MENU
echo ==============================
echo.
echo 1 - Run Setup
echo 2 - Test AVR Tools
echo 3 - Run Programmer
echo 4 - Run FULL Pipeline
echo 0 - Exit
echo.
set /p choice=Choose an option: 

if "%choice%"=="1" goto setup
if "%choice%"=="2" goto test
if "%choice%"=="3" goto programmer
if "%choice%"=="4" goto full
if "%choice%"=="0" exit

goto menu

:setup
cls
echo Running MAR_setup...
start "" cmd /c "python MAR_setup.py && pause"
goto menu

:test
cls
echo Testing AVR tools...
start "" cmd /k ^
"echo === TESTING === && ^
where avr-gcc && ^
avr-gcc --version && ^
echo. && ^
where avrdude && ^
avrdude -? && ^
echo. && echo Done && pause"
goto menu

:programmer
cls
echo Running MAR_programmer...
start "" cmd /k "python MAR_programmer.py"
goto menu

:full
cls
echo Running FULL pipeline...

echo Step 1: Setup
start "" cmd /c "python MAR_setup.py && pause"

echo Aguarde o setup terminar...
pause

echo Step 2: Testing
start "" cmd /k ^
"echo === TESTING === && ^
avr-gcc --version && ^
avrdude -? && ^
pause"

echo Step 3: Programmer
start "" cmd /k "python MAR_programmer.py"

goto menu