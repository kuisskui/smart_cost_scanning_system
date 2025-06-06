@echo off
setlocal enabledelayedexpansion

echo Checking Python environment...
python --version > nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Warning: Failed to upgrade pip, continuing anyway...
)

echo Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install requirements
    pause
    exit /b 1
)

echo.
echo Building application...
python build.py
if errorlevel 1 (
    echo Error: Build process failed
    pause
    exit /b 1
)

echo.
echo Build process completed successfully!
echo The executable can be found in the 'dist' directory.

echo.
echo Deactivating virtual environment...
deactivate

pause 