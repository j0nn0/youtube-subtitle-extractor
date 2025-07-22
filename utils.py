"""
Utility functions for the YouTube Subtitle Extractor application.
"""

import re
import os

def validate_youtube_url(url: str) -> bool:
    """
    Validate if the provided URL is a valid YouTube URL.
    
    Args:
        url (str): The URL to validate
        
    Returns:
        bool: True if valid YouTube URL, False otherwise
    """
    youtube_patterns = [
        r'^https?://(www\.)?youtube\.com/watch\?v=[\w-]+',
        r'^https?://(www\.)?youtube\.com/embed/[\w-]+',
        r'^https?://(www\.)?youtube\.com/v/[\w-]+',
        r'^https?://youtu\.be/[\w-]+',
        r'^https?://(www\.)?youtube\.com/watch\?.*v=[\w-]+',
        r'^https?://m\.youtube\.com/watch\?v=[\w-]+',
    ]
    
    for pattern in youtube_patterns:
        if re.match(pattern, url):
            return True
    
    return False

def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename by removing or replacing invalid characters.
    
    Args:
        filename (str): The filename to sanitize
        
    Returns:
        str: Sanitized filename safe for file system
    """
    if not filename:
        return "untitled"
    
    # Remove or replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove control characters
    filename = ''.join(char for char in filename if ord(char) >= 32)
    
    # Trim and remove multiple spaces
    filename = re.sub(r'\s+', ' ', filename.strip())
    
    # Limit length
    if len(filename) > 100:
        filename = filename[:100]
    
    # Ensure it's not empty after sanitization
    if not filename.strip():
        filename = "untitled"
    
    return filename

def format_duration(seconds: int) -> str:
    """
    Format duration in seconds to HH:MM:SS format.
    
    Args:
        seconds (int): Duration in seconds
        
    Returns:
        str: Formatted duration string
    """
    if seconds <= 0:
        return "00:00:00"
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def clean_subtitle_text(text: str) -> str:
    """
    Clean subtitle text by removing HTML tags and formatting.
    
    Args:
        text (str): Raw subtitle text
        
    Returns:
        str: Cleaned subtitle text
    """
    if not text:
        return ""
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove HTML entities
    html_entities = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&apos;': "'",
        '&nbsp;': ' ',
    }
    
    for entity, replacement in html_entities.items():
        text = text.replace(entity, replacement)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    
    return text

def is_valid_subtitle_format(content: str) -> bool:
    """
    Check if the content appears to be valid subtitle format.
    
    Args:
        content (str): Subtitle content to check
        
    Returns:
        bool: True if content appears to be valid subtitle format
    """
    if not content or len(content.strip()) < 10:
        return False
    
    # Check for common subtitle format indicators
    indicators = [
        'WEBVTT',  # WebVTT format
        '-->',     # Timestamp separator
        r'\d{2}:\d{2}:\d{2}',  # Time format
        r'\d+\n\d{2}:\d{2}:\d{2}',  # SRT format
    ]
    
    for indicator in indicators:
        if re.search(indicator, content):
            return True
    
    return False

def extract_video_id_from_url(url: str) -> str:
    """
    Extract video ID from YouTube URL.
    
    Args:
        url (str): YouTube URL
        
    Returns:
        str: Video ID or empty string if not found
    """
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return ""
