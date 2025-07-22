#!/usr/bin/env python3
"""
YouTube Subtitle Extractor
A GUI application for extracting and saving YouTube video subtitles in SRT or TXT format.
"""

import tkinter as tk
import sys
import os
from gui_app import YouTubeSubtitleExtractorGUI

def hide_console():
    """Hide the console window on Windows."""
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except Exception:
            pass  # If hiding fails, continue anyway

def main():
    """Main entry point of the application."""
    try:
        # Hide console window on Windows
        hide_console()
        
        root = tk.Tk()
        app = YouTubeSubtitleExtractorGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Application error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
