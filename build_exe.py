#!/usr/bin/env python3
"""
Build script to create Windows executable for YouTube Subtitle Extractor
"""

import os
import subprocess
import sys
import shutil

def build_executable():
    """Build the Windows executable using PyInstaller"""
    
    print("Building YouTube Subtitle Extractor executable...")
    
    # Clean up previous builds
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",  # Single executable file
        "--windowed",  # No console window
        "--name=YouTube_Subtitle_Extractor",
        "--icon=icon.ico" if os.path.exists("icon.ico") else "",
        "--add-data=icon.ico;." if os.path.exists("icon.ico") else "",
        "main.py"
    ]
    
    # Remove empty icon parameter if no icon file exists
    cmd = [arg for arg in cmd if arg]
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build successful!")
        print(f"Executable created: dist/YouTube_Subtitle_Extractor.exe")
        
        # Show build info
        if os.path.exists("dist/YouTube_Subtitle_Extractor.exe"):
            size = os.path.getsize("dist/YouTube_Subtitle_Extractor.exe")
            print(f"File size: {size / (1024*1024):.1f} MB")
        
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("PyInstaller not found. Please install it with: pip install pyinstaller")
        sys.exit(1)

if __name__ == "__main__":
    build_executable()