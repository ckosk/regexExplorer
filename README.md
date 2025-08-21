# RegexExplorer

A modern, user-friendly desktop application built with Python and PySide6 for searching files using regular expressions. Perfect for developers, system administrators, and anyone who needs to find files based on complex naming patterns.

## 🚀 Features

- **Intuitive GUI Interface**: Clean, modern interface built with PySide6 (Qt6)
- **Regex File Search**: Powerful regular expression search capabilities
- **Folder Browsing**: Easy folder selection with built-in directory browser
- **Results Table**: Organized display of search results with filename and full path
- **File Integration**: Double-click to open files directly from search results

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **PySide6**: Modern Qt6 bindings for Python
- **Regular Expressions**: Built-in Python `re` module

## 📋 Requirements

### For Running the Executable
- Windows 10/11 (64-bit)

### For Building from Source
- Python 3.8 or higher
- PySide6
- PyInstaller (for building executables)

## 🚀 Installation

### Option 1: Download Executable (Recommended for Windows users)

1. **Download the latest release**
   - Go to [Releases](https://github.com/ckosk/regexExplorer/releases)
   - Download `RegexExplorer.exe` from the latest release
   - Run the executable directly - no installation required

### Option 2: Build from Source

1. **Clone the repository**
   ```bash
   git clone https://github.com/ckosk/regexExplorer.git
   cd regexExplorer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python regexExplorer.py
   ```

4. **Build executable (optional)**
   ```bash
   python build_exe.py
   ```

## 🚀 Quick Start

1. **Download and run** `RegexExplorer.exe` from the [Releases](https://github.com/ckosk/regexExplorer/releases) page
2. **Select a folder** - Click "Browse" to choose the directory to search
3. **Enter regex pattern** - Type your regular expression in the "Regex" field
4. **Search** - Click "Search" to find matching files
5. **View results** - Results appear in the table below
6. **Open files** - Double-click any result to open the file with your default application

## 💻 Usage (Source Code)

1. **Launch the application** - Run `python regexExplorer.py`
2. **Select a folder** - Click "Browse" to choose the directory to search
3. **Enter regex pattern** - Type your regular expression in the "Regex" field
4. **Search** - Click "Search" to find matching files
5. **View results** - Results appear in the table below
6. **Open files** - Double-click any result to open the file with your default application

## 🔍 Regex Examples

| Pattern | Description | Example Matches |
|---------|-------------|-----------------|
| `\.py$` | Python files | `script.py`, `main.py` |
| `^test.*` | Files starting with "test" | `test_file.txt`, `test123.py` |
| `.*\.(jpg\|png\|gif)$` | Image files | `photo.jpg`, `icon.png` |
| `[0-9]{4}` | Files with 4 digits | `2023_report.pdf`, `data_1234.csv` |

## 🏗️ Project Structure

```
regexExplorer/
├── regexExplorer.py    # Main application file
├── test_gui.py         # GUI testing utilities
├── build_exe.py        # Build script for creating executable
├── requirements.txt    # Python dependencies
├── releases/           # Compiled executables
└── README.md           # This file
```

## 🤝 Contributing

Contributions are welcome. Feel free to submit a Pull Request.
