# Contributing to YouTube Subtitle Extractor

Thank you for your interest in contributing to YouTube Subtitle Extractor! This document provides guidelines for contributing to the project.

## Ways to Contribute

- 🐛 **Report Bugs** - Help us identify and fix issues
- 💡 **Suggest Features** - Propose new functionality or improvements
- 🔧 **Submit Code** - Fix bugs or implement new features
- 📖 **Improve Documentation** - Help make the project more accessible
- 🧪 **Test** - Try the application on different systems and report results

## Getting Started

### Development Environment Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/youtube-subtitle-extractor.git
   cd youtube-subtitle-extractor
   ```
3. **Install dependencies**:
   ```bash
   pip install yt-dlp pyinstaller
   ```
4. **Run the application**:
   ```bash
   python main.py
   ```

### Project Structure

- `main.py` - Application entry point
- `gui_app.py` - GUI components and user interface
- `subtitle_extractor.py` - Core subtitle extraction logic
- `utils.py` - Utility functions and helpers
- `build/` - Build scripts and configuration files

## Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

### Testing
- Test your changes on multiple operating systems when possible
- Verify that both SRT and TXT output formats work correctly
- Test with various YouTube video types (different languages, long videos, etc.)
- Ensure the GUI remains responsive during extraction

### Commit Messages
Use clear, descriptive commit messages:
- `feat: add support for playlist URLs`
- `fix: resolve GUI freezing during long extractions`
- `docs: update installation instructions`
- `style: improve error message formatting`

## Types of Contributions

### Bug Reports
When reporting bugs, please include:
- **Operating System** and version
- **Python version**
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Error messages** or screenshots
- **YouTube URL** that caused the issue (if applicable)

### Feature Requests
For new features, please provide:
- **Clear description** of the feature
- **Use case** - why would this be useful?
- **Implementation ideas** (if you have any)
- **Examples** of how it would work

### Code Contributions

#### Before Submitting Code
1. **Create an issue** to discuss major changes
2. **Check existing issues** to avoid duplicating work
3. **Follow the coding standards** outlined above
4. **Test your changes** thoroughly

#### Pull Request Process
1. **Create a feature branch** from main:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** with clear, focused commits
3. **Test thoroughly** on your local machine
4. **Update documentation** if needed
5. **Submit a pull request** with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots (for UI changes)
   - Testing details

## Areas for Contribution

### High Priority
- 🌐 **Internationalization** - Multi-language support
- 🎨 **UI Improvements** - Better styling and user experience
- 🔍 **Error Handling** - More specific error messages and recovery
- 📱 **Accessibility** - Screen reader support, keyboard navigation

### Medium Priority
- 🎵 **Audio Track Support** - Extract audio descriptions
- 📂 **Batch Processing** - Multiple URLs at once
- ⚡ **Performance** - Faster extraction for long videos
- 🔧 **Configuration** - User preferences and settings

### Ideas Welcome
- 📊 **Statistics** - Show extraction time, file sizes
- 🔗 **Browser Integration** - Browser extension support
- 📱 **Mobile Support** - Android/iOS versions
- 🌙 **Dark Mode** - Theme options

## Code Review Process

1. **All submissions** go through code review
2. **Maintainers** will review your pull request
3. **Feedback** will be provided for improvements
4. **Approval** and merge once review is complete

## Questions?

- 💬 **Discussions** - Use GitHub Discussions for questions
- 🐛 **Issues** - Use GitHub Issues for bugs and features
- 📧 **Email** - Contact maintainers for sensitive matters

## Recognition

Contributors are recognized in:
- README.md acknowledgments
- Release notes for significant contributions
- GitHub contributors list

Thank you for helping make YouTube Subtitle Extractor better for everyone! 🎉