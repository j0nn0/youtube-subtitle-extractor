# Complete Guide: Creating Windows Installer for YouTube Subtitle Extractor

This guide provides step-by-step instructions to create both a standalone executable and a professional Windows installer.

## Option 1: Standalone Executable (.exe) - Recommended for Quick Distribution

### Step 1: Prepare Environment
On a Windows machine with Python installed:

```cmd
# Install required packages
pip install -r requirements_build.txt

# Or install manually:
pip install pyinstaller yt-dlp
```

### Step 2: Build Executable

**Method A: Using batch file (easiest)**
```cmd
# Simply double-click build.bat or run:
build.bat
```

**Method B: Using PyInstaller directly**
```cmd
pyinstaller --onefile --windowed --name=YouTube_Subtitle_Extractor main.py
```

**Method C: Using spec file for advanced options**
```cmd
pyinstaller youtube_subtitle_extractor.spec
```

### Step 3: Find Your Executable
- Location: `dist/YouTube_Subtitle_Extractor.exe`
- Size: ~25-35 MB
- Ready to distribute - no installation needed!

## Option 2: Windows Installer (.msi) - Professional Distribution

For a more professional distribution, you can create a Windows installer:

### Using NSIS (Nullsoft Scriptable Install System)

1. **Download NSIS**: https://nsis.sourceforge.io/
2. **Create installer script** (`installer.nsi`):

```nsis
!define APPNAME "YouTube Subtitle Extractor"
!define COMPANYNAME "Your Name"
!define DESCRIPTION "Extract subtitles from YouTube videos"
!define VERSIONMAJOR 1
!define VERSIONMINOR 0
!define VERSIONBUILD 0

Name "${APPNAME}"
Icon "icon.ico"
OutFile "${APPNAME}_Setup.exe"
InstallDir "$PROGRAMFILES\${APPNAME}"

Page directory
Page instfiles

Section "install"
    SetOutPath $INSTDIR
    File "dist\YouTube_Subtitle_Extractor.exe"
    File /nonfatal "icon.ico"
    
    # Create uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
    
    # Start Menu
    CreateDirectory "$SMPROGRAMS\${APPNAME}"
    CreateShortCut "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\YouTube_Subtitle_Extractor.exe"
    CreateShortCut "$SMPROGRAMS\${APPNAME}\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    
    # Desktop shortcut
    CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\YouTube_Subtitle_Extractor.exe"
    
    # Registry info for Add/Remove Programs
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$INSTDIR\uninstall.exe"
SectionEnd

Section "uninstall"
    Delete "$INSTDIR\YouTube_Subtitle_Extractor.exe"
    Delete "$INSTDIR\icon.ico"
    Delete "$INSTDIR\uninstall.exe"
    
    Delete "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk"
    Delete "$SMPROGRAMS\${APPNAME}\Uninstall.lnk"
    RMDir "$SMPROGRAMS\${APPNAME}"
    
    Delete "$DESKTOP\${APPNAME}.lnk"
    
    RMDir "$INSTDIR"
    
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
SectionEnd
```

3. **Compile installer**: Right-click `installer.nsi` → "Compile NSIS Script"

## File Structure for Distribution

```
YouTube-Subtitle-Extractor/
├── main.py                          # Main application
├── gui_app.py                       # GUI components  
├── subtitle_extractor.py            # Core logic
├── utils.py                         # Utilities
├── build.bat                        # Windows build script
├── build_exe.py                     # Cross-platform build script
├── youtube_subtitle_extractor.spec  # PyInstaller config
├── requirements_build.txt           # Build dependencies
├── icon.ico                         # Application icon (optional)
├── README_BUILD.md                  # Build instructions
└── PACKAGING_GUIDE.md               # This guide
```

## Testing Your Executable

1. **Test on build machine**: Run the `.exe` file to ensure it works
2. **Test on clean machine**: Test on a Windows computer without Python installed
3. **Test different Windows versions**: Ensure compatibility across Windows 10/11
4. **Test with different YouTube videos**: Verify subtitle extraction works correctly

## Troubleshooting

### Common Build Issues

**"Module not found" errors:**
```cmd
# Add hidden imports to spec file:
hiddenimports=['yt_dlp', 'urllib.request', 'tkinter.filedialog']
```

**Large file size:**
- Expected: 25-35 MB (includes Python runtime)
- To reduce: Use `--exclude-module` for unused packages

**Antivirus false positives:**
- Common with PyInstaller executables
- Submit to antivirus vendor for whitelisting
- Sign the executable with a code signing certificate (for commercial use)

### Runtime Issues

**"Failed to execute script main":**
- Build without `--windowed` to see error messages
- Check all dependencies are included

**Missing DLL errors:**
- Usually resolved by rebuilding on target Windows version
- Consider using `--add-binary` for specific DLLs

## Distribution Options

1. **Direct Download**: Share the `.exe` file directly
2. **ZIP Archive**: Package with readme and license files
3. **Windows Installer**: Professional `.msi` or `.exe` installer
4. **Microsoft Store**: Publish through Windows Store (requires certification)
5. **GitHub Releases**: Automated builds with GitHub Actions

## Code Signing (Optional but Recommended)

For professional distribution:
1. Purchase code signing certificate
2. Sign the executable: `signtool sign /f cert.pfx /p password YouTube_Subtitle_Extractor.exe`
3. Prevents Windows SmartScreen warnings

## Automated Building with GitHub Actions

Create `.github/workflows/build-windows.yml` for automatic builds on code changes.