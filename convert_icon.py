#!/usr/bin/env python3
"""
Convert SVG icon to ICO format for Windows installer
Requires Pillow (PIL) library: pip install Pillow
"""

import os
from PIL import Image
import io

def svg_to_ico():
    """Convert icon.svg to icon.ico"""
    
    # Check if SVG file exists
    if not os.path.exists('icon.svg'):
        print("ERROR: icon.svg not found")
        print("Please create an icon.svg file first")
        return False
    
    try:
        # Try to import cairosvg for SVG conversion
        import cairosvg
        
        # Convert SVG to PNG in memory
        png_data = cairosvg.svg2png(url='icon.svg', output_width=256, output_height=256)
        
        # Open PNG data with PIL
        img = Image.open(io.BytesIO(png_data))
        
        # Create ICO file with multiple sizes
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # Save as ICO
        img.save('icon.ico', format='ICO', sizes=icon_sizes)
        
        print("✓ Successfully converted icon.svg to icon.ico")
        print(f"✓ ICO file size: {os.path.getsize('icon.ico')} bytes")
        return True
        
    except ImportError:
        print("WARNING: cairosvg not found")
        print("Install with: pip install cairosvg")
        print("Alternatively, convert icon.svg to icon.ico manually using:")
        print("- Online converter (e.g., convertio.co)")
        print("- GIMP or Photoshop")
        print("- Inkscape: File > Export > Select ICO format")
        return False
        
    except Exception as e:
        print(f"ERROR: Failed to convert icon: {e}")
        return False

def create_simple_ico():
    """Create a simple text-based ICO if SVG conversion fails"""
    try:
        # Create a simple colored square as fallback
        img = Image.new('RGBA', (256, 256), (255, 0, 0, 255))  # Red background
        
        # Add some simple graphics (optional)
        from PIL import ImageDraw
        draw = ImageDraw.Draw(img)
        
        # Draw a simple play button triangle
        triangle = [(80, 80), (80, 176), (176, 128)]
        draw.polygon(triangle, fill=(255, 255, 255, 255))
        
        # Save as ICO
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save('icon.ico', format='ICO', sizes=icon_sizes)
        
        print("✓ Created simple fallback icon.ico")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to create fallback icon: {e}")
        return False

if __name__ == "__main__":
    print("Converting icon for Windows installer...")
    
    # First try SVG conversion
    if not svg_to_ico():
        print("\nTrying to create simple fallback icon...")
        create_simple_ico()
    
    if os.path.exists('icon.ico'):
        print("\n✓ icon.ico is ready for the installer")
    else:
        print("\n✗ Could not create icon.ico")
        print("The installer will work without a custom icon")