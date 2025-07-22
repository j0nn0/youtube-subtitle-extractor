# Windows Installer Creation Guide

This guide shows you how to create a professional Windows installer that installs your app to Program Files and creates Start Menu shortcuts.

## Prerequisites

1. **NSIS (Nullsoft Scriptable Install System)**
   - Download from: https://nsis.sourceforge.io/Download
   - Install the program (it's free)
   - Default installation path: `C:\Program Files (x86)\NSIS\`

2. **Built Executable**
   - Must have `dist\YouTube_Subtitle_Extractor.exe` ready
   - Run `build.bat` first if you haven't

3. **Icon File (Optional)**
   - `icon.ico` file for professional appearance
   - Can convert from SVG using `convert_icon.py`

## Quick Start

### Step 1: Install NSIS
Download and install NSIS from the official website.

### Step 2: Create Icon (Optional)
```cmd
# If you have an SVG icon, convert it:
pip install Pillow cairosvg
python convert_icon.py

# Or create icon.ico manually using:
# - Online converters (convertio.co, etc.)
# - GIMP, Photoshop, or Inkscape
```

### Step 3: Build Executable
```cmd
build.bat
```

### Step 4: Create Installer
```cmd
create_installer.bat
```

Your installer will be created as: `YouTube Subtitle Extractor_Setup.exe`

## Manual Creation

If the batch file doesn't work, you can create the installer manually:

```cmd
"C:\Program Files (x86)\NSIS\makensis.exe" installer.nsi
```

## What the Installer Does

### Installation Features
- ✅ Installs to `C:\Program Files\YouTube Subtitle Extractor\`
- ✅ Creates Start Menu folder with shortcuts
- ✅ Optional Desktop shortcut
- ✅ Registers with Windows Add/Remove Programs
- ✅ Creates uninstaller
- ✅ Uses your custom icon
- ✅ Professional license agreement

### User Experience
1. User runs `YouTube Subtitle Extractor_Setup.exe`
2. Welcome screen with your app icon
3. License agreement (MIT license included)
4. Component selection (main app, shortcuts)
5. Installation directory selection
6. Progress bar during installation
7. Completion screen

### File Structure After Installation
```
C:\Program Files\YouTube Subtitle Extractor\
├── YouTube_Subtitle_Extractor.exe
├── icon.ico
├── README.md
└── uninstall.exe

Start Menu\Programs\YouTube Subtitle Extractor\
├── YouTube Subtitle Extractor.lnk
└── Uninstall YouTube Subtitle Extractor.lnk

Desktop\
└── YouTube Subtitle Extractor.lnk (if selected)
```

## Customization

### Changing App Information
Edit `installer.nsi` and modify:
```nsis
!define APPNAME "Your App Name"
!define COMPANYNAME "Your Company"
!define DESCRIPTION "Your Description"
```

### Adding Files to Installation
Add files in the install section:
```nsis
File "your-file.txt"
File "docs\manual.pdf"
```

### Custom Icon Requirements
- Format: ICO file
- Recommended sizes: 16x16, 32x32, 48x48, 64x64, 128x128, 256x256
- Transparent background supported
- Maximum file size: ~1MB for reasonable installer size

## Troubleshooting

### NSIS Not Found Error
- Install NSIS from official website
- Check installation path: `C:\Program Files (x86)\NSIS\makensis.exe`
- Restart Command Prompt after installation

### Executable Not Found
- Run `build.bat` first to create the executable
- Ensure `dist\YouTube_Subtitle_Extractor.exe` exists

### Icon Issues
- ICO format required (not PNG, JPG, or SVG)
- Use `convert_icon.py` or online converters
- Installer works without icon if needed

### Permission Errors
- Run Command Prompt as Administrator
- Ensure antivirus isn't blocking the installer creation

### Large Installer Size
- Normal size: 25-35 MB (includes Python runtime)
- ICO file adds ~100KB
- Consider compressing with UPX if needed

## Distribution

### Sharing Your Installer
- Single file: `YouTube Subtitle Extractor_Setup.exe`
- No dependencies required
- Works on Windows 10/11
- Can be shared via email, download, or USB

### Professional Touches
- Code signing certificate (prevents Windows warnings)
- Custom graphics and branding
- Multi-language support
- Auto-update functionality

## Advanced Features

The installer script supports additional features:
- File associations
- Registry entries
- Services installation
- Multiple languages
- Custom pages and dialogs

Edit `installer.nsi` to add these features as needed.