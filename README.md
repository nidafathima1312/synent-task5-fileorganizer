# Synent Task 5: Automated File Organizer CLI

A smart Python automation script that categorizes and organizes messy directories into structured folders for the Synent Technologies Internship Program.

## 📌 Project Overview
This CLI application automates file management using standard Python OS libraries. It scans a specified directory, identifies file extensions, creates category folders automatically, safely handles duplicate filenames without overwriting, generates execution logs, and includes a Preview/Dry-Run mode prior to file movements.

## 🛠️ Methodology & Logic
- **Directory Traversal:** Employs `os.listdir()` and `os.path.isfile()` to target and isolate loose files while skipping existing subdirectories.
- **Extension Mapping:** Maps file extensions against predefined categories (`Images`, `Documents`, `Videos`, `Audio`, `Archives`) using `os.path.splitext()`.
- **Dry-Run Safeguard:** Pre-views planned file destinations and requests explicit user confirmation (`y/n`) before executing any file operations.
- **Duplicate Protection:** Generates unique target filepaths using incremental counters (`_1`, `_2`) via `os.path.exists()` to prevent accidental overwrites.
- **Audit Logging:** Logs all operational activity with timestamps into `organization_log.txt` using Python standard file handling (`open()`).

## ✨ Key Features
- **📂 Automatic Folder Generation:** Dynamically creates subfolders (`Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Others`).
- **🔍 Preview (Dry Run) Mode:** Displays planned file movements before altering the file system.
- **🛡️ Duplicate Name Safety:** Automatically renames duplicate files (`filename_1.ext`).
- **🚫 Safe Directory Handling:** Skips existing subdirectories and operates strictly on loose files.
- **📝 Audit Logging:** Saves detailed execution logs (`organization_log.txt`) inside target directories.
- **🎨 Styled Terminal Output:** Utilizes ANSI color formatting for clear output summaries.

## 🛠️ Supported File Types
- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`
- **Documents:** `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.csv`
- **Videos:** `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.wmv`
- **Audio:** `.mp3`, `.wav`, `.aac`, `.flac`, `.m4a`
- **Archives:** `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Others:** Unrecognized extensions or files without extension formats.

## 📷 Screenshots & Execution Walkthrough

### 1. Preview / Dry-Run Mode
![Dry Run Preview](screenshot%201.png)

### 2. Organization Completion
![Organization Complete](screenshot%202.png)

### 3. Generated Audit Log File
![Audit Log File](screenshot%203.png)

## 💻 Example Output
```text
=============================================
      📂 AUTOMATED FILE ORGANIZER 📂         
=============================================

Enter target folder path to organize: "C:\Users\nidaf\OneDrive\Desktop\Test-Files"

Found 3 file(s) to process.

--- PREVIEW MODE (Dry Run) ---
📄 notes.txt.txt                  ➔  📁 Documents/
📄 photo.jpg.doc                  ➔  📁 Documents/
📄 resume.pdf.txt                 ➔  📁 Documents/

Proceed with organizing these files? (y/n): y

=============================================
      ✓ ORGANIZATION COMPLETE!             
=============================================
 • Documents    : 3

Total files moved: 3
📄 Log saved to: C:\Users\nidaf\OneDrive\Desktop\Test-Files\organization_log.txt
