"""
YouTube Subtitle Extractor Module
Handles the extraction and processing of YouTube video subtitles.
"""

import os
import re
import yt_dlp
from typing import Optional, Dict, List, Tuple

class YouTubeSubtitleExtractor:
    """Class to handle YouTube subtitle extraction using yt-dlp."""
    
    def __init__(self):
        """Initialize the subtitle extractor."""
        self.ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en', 'en-US', 'en-GB'],
            'skip_download': True,
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'socket_timeout': 30,
        }
    
    def extract_video_info(self, url: str) -> Dict:
        """Extract video information from YouTube URL."""
        try:
            # Use minimal options for fast video info extraction
            simple_opts = {
                'quiet': True,
                'no_warnings': True,
                'skip_download': True,
                'extract_flat': False,
            }
            
            with yt_dlp.YoutubeDL(simple_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title', 'Unknown Title'),
                    'duration': info.get('duration', 0),
                    'subtitles': info.get('subtitles', {}),
                    'automatic_captions': info.get('automatic_captions', {})
                }
        except Exception as e:
            raise Exception(f"Failed to extract video info: {str(e)}")
    
    def get_subtitle_content(self, url: str) -> Optional[str]:
        """Extract subtitle content from YouTube video."""
        try:
            # Use the original working configuration
            opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitleslangs': ['en', 'en-US', 'en-GB'],
                'skip_download': True,
                'quiet': True,
                'no_warnings': True,
                'outtmpl': '%(title)s.%(ext)s'
            }
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Try to get manual subtitles first, then automatic
                subtitles = info.get('subtitles', {})
                automatic_captions = info.get('automatic_captions', {})
                
                # Look for English subtitles
                subtitle_langs = ['en', 'en-US', 'en-GB']
                subtitle_data = None
                
                for lang in subtitle_langs:
                    if lang in subtitles:
                        subtitle_data = subtitles[lang]
                        break
                    elif lang in automatic_captions:
                        subtitle_data = automatic_captions[lang]
                        break
                
                if not subtitle_data:
                    # Try any available language
                    if subtitles:
                        subtitle_data = list(subtitles.values())[0]
                    elif automatic_captions:
                        subtitle_data = list(automatic_captions.values())[0]
                
                if not subtitle_data:
                    raise Exception("No subtitles available for this video")
                
                # Find the best format (prefer vtt, then srv3, then others)
                best_format = None
                for fmt in subtitle_data:
                    if fmt.get('ext') == 'vtt':
                        best_format = fmt
                        break
                    elif fmt.get('ext') == 'srv3':
                        best_format = fmt
                    elif best_format is None:
                        best_format = fmt
                
                if not best_format:
                    raise Exception("No suitable subtitle format found")
                
                # Download subtitle content
                subtitle_url = best_format['url']
                
                import urllib.request
                import socket
                
                # Set a reasonable timeout
                original_timeout = socket.getdefaulttimeout()
                socket.setdefaulttimeout(60)  # 60 seconds for large files
                
                try:
                    with urllib.request.urlopen(subtitle_url) as response:
                        content = response.read().decode('utf-8')
                    return content
                finally:
                    # Restore original timeout
                    socket.setdefaulttimeout(original_timeout)
                
        except Exception as e:
            raise Exception(f"Failed to extract subtitles: {str(e)}")
    
    def convert_to_srt(self, content: str) -> str:
        """Convert subtitle content to SRT format."""
        try:
            # If content is already SRT, return as is
            if self._is_srt_format(content):
                return content
            
            # Parse VTT format
            if 'WEBVTT' in content:
                return self._convert_vtt_to_srt(content)
            
            # Parse other formats (srv3, etc.)
            return self._parse_generic_subtitle_format(content)
            
        except Exception as e:
            raise Exception(f"Failed to convert to SRT: {str(e)}")
    
    def convert_to_txt(self, content: str) -> str:
        """Convert subtitle content to clean TXT format."""
        try:
            # For very large content, process in chunks to avoid memory issues
            if len(content) > 100000:  # 100KB threshold
                return self._convert_large_txt(content)
            
            # First convert to SRT to normalize format
            srt_content = self.convert_to_srt(content)
            
            # Extract text from SRT
            lines = srt_content.split('\n')
            text_lines = []
            seen_lines = set()  # Track seen lines to avoid duplicates
            
            for line in lines:
                line = line.strip()
                # Skip empty lines, subtitle numbers, and timestamp lines
                if (line and 
                    not line.isdigit() and 
                    not '-->' in line and
                    not re.match(r'^\d+:\d+:', line)):
                    
                    # Clean HTML tags and formatting
                    clean_line = re.sub(r'<[^>]+>', '', line)
                    clean_line = re.sub(r'&[a-zA-Z]+;', '', clean_line)
                    clean_line = clean_line.strip()
                    
                    if clean_line:
                        # Only add if we haven't seen this exact line before
                        if clean_line not in seen_lines:
                            text_lines.append(clean_line)
                            seen_lines.add(clean_line)
            
            # Join lines and then split into sentences for better readability
            full_text = ' '.join(text_lines)
            
            # Split into sentences and rejoin with proper line breaks
            # Enhanced regex to handle more sentence endings including ellipsis
            sentences = re.split(r'(?<=[.!?…])\s+', full_text)
            final_lines = []
            
            for sentence in sentences:
                sentence = sentence.strip()
                if sentence:
                    # Ensure sentence ends with punctuation for clean formatting
                    final_lines.append(sentence)
            
            return '\n'.join(final_lines)
            
        except Exception as e:
            raise Exception(f"Failed to convert to TXT: {str(e)}")
    
    def _convert_large_txt(self, content: str) -> str:
        """Convert large subtitle content to TXT format efficiently."""
        # For large files, use a simpler approach to avoid performance issues
        lines = content.split('\n')
        text_lines = []
        seen_lines = set()
        
        for line in lines:
            line = line.strip()
            # Skip VTT headers, timestamps, and empty lines
            if (line and 
                not line.startswith('WEBVTT') and
                not line.startswith('NOTE') and
                not '-->' in line and
                not re.match(r'^\d{2}:\d{2}:\d{2}', line)):
                
                # Clean HTML tags and formatting
                clean_line = re.sub(r'<[^>]+>', '', line)
                clean_line = re.sub(r'&[a-zA-Z]+;', '', clean_line)
                clean_line = clean_line.strip()
                
                if clean_line and clean_line not in seen_lines:
                    text_lines.append(clean_line)
                    seen_lines.add(clean_line)
        
        # Apply same sentence-based formatting as regular method
        full_text = ' '.join(text_lines)
        
        # Split into sentences and rejoin with proper line breaks
        sentences = re.split(r'(?<=[.!?…])\s+', full_text)
        final_lines = []
        
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                final_lines.append(sentence)
        
        return '\n'.join(final_lines)
    
    def _is_srt_format(self, content: str) -> bool:
        """Check if content is already in SRT format."""
        lines = content.strip().split('\n')
        if len(lines) < 3:
            return False
        
        # Check if first line is a number
        if not lines[0].strip().isdigit():
            return False
        
        # Check if second line contains timestamp
        if '-->' not in lines[1]:
            return False
        
        return True
    
    def _convert_vtt_to_srt(self, vtt_content: str) -> str:
        """Convert VTT format to SRT format."""
        lines = vtt_content.split('\n')
        srt_lines = []
        subtitle_count = 0
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip WEBVTT header and empty lines
            if line.startswith('WEBVTT') or line.startswith('NOTE') or not line:
                i += 1
                continue
            
            # Look for timestamp lines
            if '-->' in line:
                subtitle_count += 1
                
                # Convert VTT timestamp to SRT timestamp
                timestamp_line = line.replace('.', ',')
                
                # Add subtitle number
                srt_lines.append(str(subtitle_count))
                srt_lines.append(timestamp_line)
                
                # Add subtitle text
                i += 1
                while i < len(lines) and lines[i].strip():
                    text_line = lines[i].strip()
                    if text_line:
                        srt_lines.append(text_line)
                    i += 1
                
                # Add empty line
                srt_lines.append('')
            else:
                i += 1
        
        return '\n'.join(srt_lines)
    
    def _parse_generic_subtitle_format(self, content: str) -> str:
        """Parse generic subtitle formats and convert to SRT."""
        # This is a fallback for other subtitle formats
        # Try to extract timestamps and text using regex
        
        # Look for timestamp patterns
        timestamp_pattern = r'(\d{1,2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{1,2}:\d{2}:\d{2}[.,]\d{3})'
        matches = re.findall(timestamp_pattern, content)
        
        if matches:
            # Already has timestamps, try to format as SRT
            lines = content.split('\n')
            srt_lines = []
            subtitle_count = 0
            
            for i, line in enumerate(lines):
                if re.search(timestamp_pattern, line):
                    subtitle_count += 1
                    srt_lines.append(str(subtitle_count))
                    srt_lines.append(line.replace('.', ','))
                    
                    # Look for text in following lines
                    j = i + 1
                    while j < len(lines) and lines[j].strip():
                        text_line = lines[j].strip()
                        if not re.search(timestamp_pattern, text_line):
                            srt_lines.append(text_line)
                        j += 1
                    
                    srt_lines.append('')
            
            return '\n'.join(srt_lines)
        
        # If no clear format found, return content as plain text
        return content
