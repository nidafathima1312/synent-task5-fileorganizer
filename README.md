# Synent Task 5: Automated File Organizer CLI

A smart Python automation script that categorizes and organizes messy directories into structured folders for the Synent Technologies Internship Program.

## 📌 Project Overview
This CLI application automates file management using standard Python OS libraries. It scans a specified directory, identifies file extensions, creates category folders automatically, safely handles duplicate filenames without overwriting, generates execution logs, and includes a Preview/Dry-Run mode prior to file movements.

## ✨ Key Features
- **📂 Automatic Folder Generation**: Dynamically creates subfolders (`Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Others`) if they do not exist.
- **🔍 Preview (Dry Run) Mode**: Displays planned file movements before altering the file system, letting the user confirm or cancel.
- **🛡️ Duplicate Name Safety**: Automatically renames duplicate files (`filename_1.ext`, `filename_2.ext`) to avoid accidental overwrites.
- **🚫 Safe Directory Handling**: Skips existing subdirectories and operates strictly on loose files.
- **📝 Audit Logging**: Saves detailed execution logs (`organization_log.txt`) inside the target directory.
- **🎨 Styled Terminal Output**: Utilizes ANSI color formatting for clear, readable output summaries.

## 🛠️ Supported File Types
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.csv`
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.wmv`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`, `.m4a`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Others**: Unrecognized extensions or files without extension formats.

## 🚀 How to Run

1. **Prerequisites**: Ensure Python 3.x is installed on your system.
2. **Execution**:
   Open terminal inside the project directory and run:
   ```bash
   python file_organizer.py