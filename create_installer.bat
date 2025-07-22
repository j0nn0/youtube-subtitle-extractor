@echo off
echo Creating Windows Installer for YouTube Subtitle Extractor...
echo.

REM Check if NSIS is installed
"C:\Program Files (x86)\NSIS\makensis.exe" /VERSION >nul 2>&1
if errorlevel 1 (
    echo ERROR: NSIS is not installed
    echo.
    echo Please download and install NSIS from:
    echo https://nsis.sourceforge.io/Download
    echo.
    echo After installation, run this script again.
    pause
    exit /b 1
)

REM Check if executable exists
if not exist "dist\YouTube_Subtitle_Extractor.exe" (
    echo ERROR: Executable not found!
    echo.
    echo Please build the executable first by running:
    echo   build.bat
    echo.
    echo Or manually with:
    echo   pyinstaller --onefile --windowed --name=YouTube_Subtitle_Extractor main.py
    pause
    exit /b 1
)

REM Create icon file if it doesn't exist
if not exist "icon.ico" (
    echo WARNING: icon.ico not found
    echo The installer will be created without a custom icon
    echo.
)

echo Building installer...
"C:\Program Files (x86)\NSIS\makensis.exe" installer.nsi

if exist "YouTube Subtitle Extractor_Setup.exe" (
    echo.
    echo ================================
    echo Installer created successfully!
    echo ================================
    echo File: YouTube Subtitle Extractor_Setup.exe
    echo.
    for %%A in ("YouTube Subtitle Extractor_Setup.exe") do echo Installer size: %%~zA bytes
    echo.
    echo Features:
    echo - Installs to Program Files
    echo - Creates Start Menu shortcuts
    echo - Creates Desktop shortcut
    echo - Includes uninstaller
    echo - Shows in Add/Remove Programs
) else (
    echo.
    echo ================================
    echo Installer creation failed!
    echo ================================
    echo Check the output above for errors.
)

pause