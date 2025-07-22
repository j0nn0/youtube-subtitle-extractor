"""
GUI Application for YouTube Subtitle Extractor
Provides a user-friendly interface for extracting and saving YouTube subtitles.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import os
from subtitle_extractor import YouTubeSubtitleExtractor
from utils import validate_youtube_url, sanitize_filename

class YouTubeSubtitleExtractorGUI:
    """Main GUI application class."""
    
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.extractor = YouTubeSubtitleExtractor()
        self.current_subtitles = None
        self.current_video_title = None
        
        self.setup_gui()
    
    def setup_gui(self):
        """Set up the GUI components."""
        self.root.title("YouTube Subtitle Extractor")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Set window icon
        self.set_window_icon()
        
        # Configure grid weights for responsive design
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="YouTube Subtitle Extractor", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, pady=(0, 20))
        
        # URL input section
        url_frame = ttk.LabelFrame(main_frame, text="YouTube Video URL", padding="10")
        url_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        url_frame.grid_columnconfigure(0, weight=1)
        
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(url_frame, textvariable=self.url_var, font=("Arial", 10))
        url_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Buttons frame
        button_frame = ttk.Frame(url_frame)
        button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        button_frame.grid_columnconfigure(0, weight=1)
        
        self.extract_button = ttk.Button(button_frame, text="Extract Subtitles", 
                                        command=self.extract_subtitles)
        self.extract_button.grid(row=0, column=0, padx=(0, 10))
        
        self.clear_button = ttk.Button(button_frame, text="Clear URL", 
                                      command=self.clear_url)
        self.clear_button.grid(row=0, column=1)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to extract subtitles")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, 
                                font=("Arial", 9))
        status_label.grid(row=3, column=0, pady=(0, 10))
        
        # Video info frame
        self.info_frame = ttk.LabelFrame(main_frame, text="Video Information", 
                                        padding="10")
        self.info_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.info_frame.grid_remove()  # Hide initially
        
        # Video title
        ttk.Label(self.info_frame, text="Title:").grid(row=0, column=0, sticky=tk.W)
        self.title_var = tk.StringVar()
        title_info = ttk.Label(self.info_frame, textvariable=self.title_var, 
                              font=("Arial", 9), wraplength=400)
        title_info.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        
        # Save options frame
        self.save_frame = ttk.LabelFrame(main_frame, text="Save Options", 
                                        padding="10")
        self.save_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.save_frame.grid_columnconfigure(0, weight=1)
        self.save_frame.grid_remove()  # Hide initially
        
        # Save buttons
        save_button_frame = ttk.Frame(self.save_frame)
        save_button_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        save_button_frame.grid_columnconfigure(0, weight=1)
        save_button_frame.grid_columnconfigure(1, weight=1)
        
        self.save_srt_button = ttk.Button(save_button_frame, text="Save as SRT", 
                                         command=self.save_as_srt)
        self.save_srt_button.grid(row=0, column=0, padx=(0, 5), sticky=(tk.W, tk.E))
        
        self.save_txt_button = ttk.Button(save_button_frame, text="Save as TXT", 
                                         command=self.save_as_txt)
        self.save_txt_button.grid(row=0, column=1, padx=(5, 0), sticky=(tk.W, tk.E))
        
        # Process another button
        self.process_another_button = ttk.Button(main_frame, text="Process Another Video", 
                                                command=self.process_another)
        self.process_another_button.grid(row=6, column=0, pady=(20, 0))
        self.process_another_button.grid_remove()  # Hide initially
        
        # Configure scrollable text widget for subtitle preview (optional)
        self.create_preview_section(main_frame)
        
    def create_preview_section(self, parent):
        """Create subtitle preview section."""
        self.preview_frame = ttk.LabelFrame(parent, text="Subtitle Preview", 
                                           padding="10")
        self.preview_frame.grid(row=7, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), 
                               pady=(10, 0))
        self.preview_frame.grid_columnconfigure(0, weight=1)
        self.preview_frame.grid_rowconfigure(0, weight=1)
        self.preview_frame.grid_remove()  # Hide initially
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(self.preview_frame)
        text_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        text_frame.grid_columnconfigure(0, weight=1)
        text_frame.grid_rowconfigure(0, weight=1)
        
        self.preview_text = tk.Text(text_frame, height=10, wrap=tk.WORD, 
                                   font=("Courier", 9))
        self.preview_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, 
                                 command=self.preview_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.preview_text.config(yscrollcommand=scrollbar.set)
        
        # Configure main frame to expand preview
        parent.grid_rowconfigure(7, weight=1)
    
    def set_window_icon(self):
        """Set the window icon."""
        try:
            # Try to load icon.ico if it exists
            if os.path.exists('icon.ico'):
                self.root.iconbitmap('icon.ico')
            else:
                # Use a simple default approach for cross-platform compatibility
                pass
        except Exception:
            # If icon loading fails, continue without icon
            pass
    
    def clear_url(self):
        """Clear the URL input field."""
        self.url_var.set("")
        self.hide_results()
        self.status_var.set("Ready to extract subtitles")
    
    def hide_results(self):
        """Hide result frames."""
        self.info_frame.grid_remove()
        self.save_frame.grid_remove()
        self.preview_frame.grid_remove()
        self.process_another_button.grid_remove()
    
    def show_results(self):
        """Show result frames."""
        self.info_frame.grid()
        self.save_frame.grid()
        self.preview_frame.grid()
        self.process_another_button.grid()
    
    def extract_subtitles(self):
        """Extract subtitles from the YouTube video."""
        url = self.url_var.get().strip()
        
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
        
        if not validate_youtube_url(url):
            messagebox.showerror("Error", "Please enter a valid YouTube URL")
            return
        
        # Disable extract button and start progress
        self.extract_button.config(state='disabled')
        self.progress.start()
        self.status_var.set("Extracting subtitles...")
        
        # Run extraction in separate thread
        thread = threading.Thread(target=self._extract_subtitles_thread, args=(url,))
        thread.daemon = True
        thread.start()
    
    def _extract_subtitles_thread(self, url):
        """Extract subtitles in a separate thread."""
        try:
            # Extract video info
            self.root.after(0, lambda: self.status_var.set("Getting video information..."))
            info = self.extractor.extract_video_info(url)
            
            # Extract subtitles
            self.root.after(0, lambda: self.status_var.set("Downloading subtitles..."))
            subtitle_content = self.extractor.get_subtitle_content(url)
            
            # Store results
            self.current_subtitles = subtitle_content
            self.current_video_title = info['title']
            
            # Update GUI in main thread
            self.root.after(0, self._extraction_complete)
            
        except Exception as e:
            self.root.after(0, self._extraction_error, str(e))
    
    def _extraction_complete(self):
        """Handle successful subtitle extraction."""
        self.progress.stop()
        self.extract_button.config(state='normal')
        self.status_var.set("Subtitles extracted successfully!")
        
        # Update video info
        self.title_var.set(self.current_video_title)
        
        # Show preview
        try:
            txt_content = self.extractor.convert_to_txt(self.current_subtitles)
            self.preview_text.delete(1.0, tk.END)
            self.preview_text.insert(1.0, txt_content[:1000] + "..." if len(txt_content) > 1000 else txt_content)
        except Exception as e:
            self.preview_text.delete(1.0, tk.END)
            self.preview_text.insert(1.0, f"Preview unavailable: {str(e)}")
        
        # Show results
        self.show_results()
    
    def _extraction_error(self, error_message):
        """Handle subtitle extraction error."""
        self.progress.stop()
        self.extract_button.config(state='normal')
        self.status_var.set("Extraction failed")
        messagebox.showerror("Extraction Error", f"Failed to extract subtitles:\n{error_message}")
    
    def save_as_srt(self):
        """Save subtitles as SRT file."""
        if not self.current_subtitles:
            messagebox.showerror("Error", "No subtitles to save")
            return
        
        try:
            # Convert to SRT format
            srt_content = self.extractor.convert_to_srt(self.current_subtitles)
            
            # Get save location
            filename = sanitize_filename(self.current_video_title) + ".srt"
            file_path = filedialog.asksaveasfilename(
                defaultextension=".srt",
                filetypes=[("SRT files", "*.srt"), ("All files", "*.*")],
                initialfile=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(srt_content)
                messagebox.showinfo("Success", f"SRT file saved successfully:\n{file_path}")
                
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save SRT file:\n{str(e)}")
    
    def save_as_txt(self):
        """Save subtitles as TXT file."""
        if not self.current_subtitles:
            messagebox.showerror("Error", "No subtitles to save")
            return
        
        try:
            # Convert to TXT format
            txt_content = self.extractor.convert_to_txt(self.current_subtitles)
            
            # Get save location
            filename = sanitize_filename(self.current_video_title) + ".txt"
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                initialfile=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(txt_content)
                messagebox.showinfo("Success", f"TXT file saved successfully:\n{file_path}")
                
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save TXT file:\n{str(e)}")
    
    def process_another(self):
        """Reset the application for processing another video."""
        self.url_var.set("")
        self.current_subtitles = None
        self.current_video_title = None
        self.hide_results()
        self.status_var.set("Ready to extract subtitles")
        self.preview_text.delete(1.0, tk.END)
