# Windows Setup Guide for Building Executable

## Step-by-Step Instructions

### 1. Install Python (if not already installed)
- Download Python from: https://python.org/downloads/
- **Important**: Check "Add Python to PATH" during installation
- Verify installation: Open Command Prompt and type `python --version`

### 2. Open Command Prompt or PowerShell
- Press `Windows + R`, type `cmd`, press Enter
- Or search "Command Prompt" in Start Menu
- Navigate to your project folder: `cd C:\path\to\your\project`

### 3. Install Required Packages
```cmd
pip install pyinstaller yt-dlp
```

If you get permission errors, try:
```cmd
pip install --user pyinstaller yt-dlp
```

### 4. Build the Executable
Simply run:
```cmd
build.bat
```

Or manually:
```cmd
pyinstaller --onefile --windowed --name=YouTube_Subtitle_Extractor main.py
```

### 5. Find Your Executable
- Location: `dist\YouTube_Subtitle_Extractor.exe`
- This file is completely standalone!

## Troubleshooting

### "pyinstaller is not recognized"
**Solution 1**: Install with user flag
```cmd
pip install --user pyinstaller
```

**Solution 2**: Add Python Scripts to PATH
- Find your Python installation (usually `C:\Users\YourName\AppData\Local\Programs\Python\PythonXX\`)
- Add `Scripts` folder to system PATH
- Restart Command Prompt

**Solution 3**: Use full path
```cmd
python -m PyInstaller --onefile --windowed --name=YouTube_Subtitle_Extractor main.py
```

### "'pip' is not recognized"
- Reinstall Python with "Add to PATH" checked
- Or download get-pip.py and run: `python get-pip.py`

### "Permission denied" errors
- Run Command Prompt as Administrator
- Or use `--user` flag with pip install

### Build fails with module errors
Add missing modules to the spec file:
```python
hiddenimports=['yt_dlp', 'urllib.request', 'tkinter.filedialog']
```

## Alternative Methods

### Method 1: Using Python directly
```cmd
python -m PyInstaller --onefile --windowed main.py
```

### Method 2: Using the spec file
```cmd
pyinstaller youtube_subtitle_extractor.spec
```

### Method 3: Using the Python build script
```cmd
python build_exe.py
```

## Final Result
- Single `.exe` file (~25-35 MB)
- No Python required on target computers
- Works on Windows 10/11
- Can be shared via email, USB, or download