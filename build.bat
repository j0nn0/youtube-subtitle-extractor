@echo off
echo Building YouTube Subtitle Extractor...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip is not available
    echo Please reinstall Python with pip included
    pause
    exit /b 1
)

echo Installing required packages...
pip install pyinstaller yt-dlp

REM Verify PyInstaller installation
pyinstaller --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: PyInstaller installation failed
    echo Try running: pip install --user pyinstaller
    pause
    exit /b 1
)

echo Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo Building executable...
pyinstaller --onefile --windowed --name=YouTube_Subtitle_Extractor main.py

if exist "dist\YouTube_Subtitle_Extractor.exe" (
    echo.
    echo ================================
    echo Build completed successfully!
    echo ================================
    echo Executable location: dist\YouTube_Subtitle_Extractor.exe
    echo.
    for %%A in ("dist\YouTube_Subtitle_Extractor.exe") do echo File size: %%~zA bytes
    echo.
    echo You can now distribute this .exe file to other Windows computers
    echo No Python installation required on target machines
) else (
    echo.
    echo ================================
    echo Build failed!
    echo ================================
    echo Check the output above for errors.
    echo.
    echo Common solutions:
    echo 1. Make sure you're in the correct directory
    echo 2. Try: pip install --user pyinstaller
    echo 3. Restart Command Prompt as Administrator
)
pause