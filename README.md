# YouTube Subtitle Extractor

A user-friendly desktop application for extracting and saving subtitles from YouTube videos.

## Features

- **Simple GUI Interface** - Easy-to-use desktop application built with Python tkinter
- **Multiple Output Formats** - Save subtitles as SRT or clean TXT files
- **Smart Text Formatting** - Automatic sentence formatting with proper line breaks
- **Fast Extraction** - Powered by yt-dlp for reliable video processing
- **Custom Save Locations** - Choose where to save your subtitle files
- **Progress Tracking** - Visual feedback during extraction process
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Professional Windows Installer** - Program Files installation with Start Menu shortcuts

## Screenshots

*(Add screenshots of your application here when you upload to GitHub)*

## Installation

### Option 1: Windows Installer (Recommended for Windows users)
1. Download the latest `YouTube_Subtitle_Extractor_Setup.exe` from the [Releases](https://github.com/your-username/youtube-subtitle-extractor/releases) page
2. Run the installer - it will install to Program Files and create Start Menu shortcuts
3. Launch from Start Menu or Desktop shortcut

### Option 2: Standalone Executable (Windows)
1. Download `YouTube_Subtitle_Extractor.exe` from the [Releases](https://github.com/your-username/youtube-subtitle-extractor/releases) page
2. Run directly - no installation required

### Option 3: Run from Source (All platforms)
```bash
# Install Python 3.7+ and pip, then:
pip install yt-dlp
git clone https://github.com/your-username/youtube-subtitle-extractor.git
cd youtube-subtitle-extractor
python main.py
```

## Usage

1. **Launch the application**
2. **Paste a YouTube URL** into the input field
3. **Click "Extract Subtitles"** and wait for processing
4. **Choose save format** (SRT or TXT) and location
5. **Done!** Your subtitle file is ready

### Supported URL formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`

## Building from Source

### Requirements
- Python 3.7 or higher
- yt-dlp library
- tkinter (usually included with Python)

### Building Windows Executable
```cmd
pip install pyinstaller yt-dlp
build.bat
```

### Creating Windows Installer
1. Install NSIS from https://nsis.sourceforge.io/
2. Run: `create_installer.bat`

## Technical Details

- **GUI Framework**: tkinter (cross-platform, no external dependencies)
- **Video Processing**: yt-dlp (reliable YouTube extraction)
- **Architecture**: Modular design with separate GUI, extraction, and utility components
- **Threading**: Background processing prevents UI freezing
- **Error Handling**: Comprehensive error messages and recovery

## File Structure

```
├── main.py                    # Application entry point
├── gui_app.py                 # GUI components and interface
├── subtitle_extractor.py      # Core subtitle extraction logic
├── utils.py                   # Utility functions
├── build.bat                  # Windows build script
├── create_installer.bat       # Windows installer creation
├── installer.nsi              # NSIS installer configuration
└── README.md                  # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/your-username/youtube-subtitle-extractor.git
cd youtube-subtitle-extractor
pip install -r requirements_build.txt
python main.py
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

This is free software: you can redistribute it and/or modify it under the terms of the GNU GPL v3.0. 
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.

**Key points of GPL v3.0:**
- ✅ Use for any purpose (commercial or non-commercial)
- ✅ Modify the source code
- ✅ Distribute copies
- ✅ Distribute modified versions
- ⚠️ Must provide source code when distributing
- ⚠️ Must keep the same GPL v3.0 license
- ⚠️ Must state changes made to the original

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful YouTube downloader that makes this project possible
- Python tkinter - For the cross-platform GUI framework
- NSIS - For the professional Windows installer system

## Support

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information about your problem
3. Include your operating system, Python version, and error messages

## Changelog

### Version 1.0.0
- Initial release
- Basic subtitle extraction functionality
- SRT and TXT output formats
- Windows installer support
- Enhanced text formatting with proper sentence breaks