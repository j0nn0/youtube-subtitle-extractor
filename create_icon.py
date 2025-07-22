#!/usr/bin/env python3
"""
Create a professional icon for the YouTube Subtitle Extractor application.
This script generates an ICO file that can be used as the window icon.
"""

def create_svg_icon():
    """Create a professional SVG icon for the YouTube Subtitle Extractor."""
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="64" height="64" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <!-- Background circle -->
  <circle cx="32" cy="32" r="30" fill="#FF0000" stroke="#CC0000" stroke-width="2"/>
  
  <!-- Play button triangle -->
  <path d="M25 20 L25 44 L45 32 Z" fill="white"/>
  
  <!-- Subtitle lines -->
  <rect x="12" y="48" width="40" height="2" fill="white" rx="1"/>
  <rect x="16" y="52" width="32" height="2" fill="white" rx="1"/>
  <rect x="20" y="56" width="24" height="2" fill="white" rx="1"/>
</svg>'''
    
    with open('icon.svg', 'w') as f:
        f.write(svg_content)
    print("Created icon.svg")

def create_ico_from_svg():
    """Convert SVG to ICO format using system tools if available."""
    try:
        import subprocess
        
        # Try to use ImageMagick to convert SVG to ICO
        result = subprocess.run(['convert', 'icon.svg', '-resize', '32x32', 'icon.ico'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Successfully created icon.ico using ImageMagick")
            return True
        else:
            print("ImageMagick not available")
            return False
            
    except (FileNotFoundError, subprocess.SubprocessError):
        print("ImageMagick not available")
        return False

def create_instructions():
    """Create instructions for the user on how to create an icon."""
    instructions = """
# How to Add a Custom Icon to Your YouTube Subtitle Extractor

## Option 1: Use the provided SVG icon
1. I've created an 'icon.svg' file with a professional YouTube-style icon
2. Convert it to ICO format using an online converter like:
   - convertio.co
   - cloudconvert.com
   - Any "SVG to ICO" converter

## Option 2: Create your own icon
Create a 32x32 pixel ICO file with your preferred design and name it 'icon.ico'

## Option 3: Use any existing ICO file
Simply rename your ICO file to 'icon.ico' and place it in the same folder as your Python files

## What the icon should look like:
- Size: 32x32 pixels (standard Windows icon size)
- Format: .ICO (Windows) or .PNG (cross-platform)
- Design: Something related to YouTube/video/subtitles
- Colors: Professional looking (red, white, blue themes work well)

## Icon Design Recommendations:
- Red background (YouTube brand color: #FF0000)
- White play button triangle
- Small subtitle lines at the bottom
- Simple, clean design that's visible at small sizes

Once you have your 'icon.ico' file in the same folder as your Python files, 
the application will automatically use it as the window icon!
"""
    
    with open('icon_instructions.txt', 'w') as f:
        f.write(instructions)
    print("Created icon_instructions.txt with detailed instructions")

if __name__ == "__main__":
    print("Creating professional icon for YouTube Subtitle Extractor...")
    
    # Create SVG icon
    create_svg_icon()
    
    # Try to create ICO file
    if not create_ico_from_svg():
        print("Could not create ICO file automatically")
    
    # Create instructions
    create_instructions()
    
    print("\nIcon creation complete!")
    print("Check the 'icon_instructions.txt' file for detailed setup instructions.")