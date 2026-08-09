import os
import shutil
from datetime import datetime

# ANSI Colors for Terminal Styling
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# File Extension Categories
CATEGORY_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def display_header():
    print(f"{CYAN}\n=============================================")
    print("      📂 AUTOMATED FILE ORGANIZER 📂         ")
    print(f"============================================={RESET}")

def get_category(file_extension):
    """Map file extension to corresponding category folder."""
    ext = file_extension.lower()
    for category, extensions in CATEGORY_MAPPING.items():
        if ext in extensions:
            return category
    return "Others"

def get_unique_filepath(destination_folder, filename):
    """Handle duplicate file names by appending _1, _2, etc."""
    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filepath = os.path.join(destination_folder, filename)

    while os.path.exists(new_filepath):
        new_filename = f"{base_name}_{counter}{extension}"
        new_filepath = os.path.join(destination_folder, new_filename)
        counter += 1

    return new_filepath

def organize_folder(target_path, dry_run=True):
    if not os.path.exists(target_path):
        print(f"{RED}⚠️ Error: The directory '{target_path}' does not exist!{RESET}")
        return

    # Filter out directories; only process actual files
    items = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]

    # Exclude log file from being organized
    items = [f for f in items if f != "organization_log.txt"]

    if not items:
        print(f"{YELLOW}⚠️ No loose files found in the directory to organize.{RESET}")
        return

    category_counts = {cat: 0 for cat in CATEGORY_MAPPING.keys()}
    category_counts["Others"] = 0

    print(f"\n{CYAN}Found {len(items)} file(s) to process.{RESET}")
    print("\n--- " + ("PREVIEW MODE (Dry Run)" if dry_run else "ORGANIZING FILES") + " ---")

    planned_moves = []

    for item in items:
        _, ext = os.path.splitext(item)
        if not ext:
            category = "Others"
        else:
            category = get_category(ext)

        dest_folder = os.path.join(target_path, category)
        planned_moves.append((item, category, dest_folder))
        print(f"📄 {item:<30} ➔  📁 {category}/")

    if dry_run:
        choice = input(f"\nProceed with organizing these files? (y/n): ").strip().lower()
        if choice != 'y':
            print(f"{YELLOW}\nOperation canceled. No files were moved.{RESET}")
            return
        # Execute actual move
        organize_folder(target_path, dry_run=False)
        return

    # Actual Execution
    log_entries = []
    log_entries.append(f"Organization Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" + "="*50 + "\n")

    for item, category, dest_folder in planned_moves:
        os.makedirs(dest_folder, exist_ok=True)
        src_file = os.path.join(target_path, item)
        dest_file = get_unique_filepath(dest_folder, item)

        shutil.move(src_file, dest_file)
        category_counts[category] += 1
        log_entries.append(f"Moved: '{item}' ➔ '{category}/{os.path.basename(dest_file)}'\n")

    # Save log file
    log_path = os.path.join(target_path, "organization_log.txt")
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.writelines(log_entries)

    print(f"{GREEN}\n=============================================")
    print("      ✓ ORGANIZATION COMPLETE!             ")
    print(f"============================================={RESET}")

    for cat, count in category_counts.items():
        if count > 0:
            print(f" • {cat:<12} : {count}")

    print(f"\n{GREEN}Total files moved: {len(items)}{RESET}")
    print(f"📄 Log saved to: {log_path}")

def main():
    display_header()
    target = input("\nEnter target folder path to organize: ").strip().strip('"').strip("'")
    if target:
        organize_folder(target, dry_run=True)
    else:
        print(f"{RED}⚠️ Invalid folder path provided.{RESET}")

if __name__ == "__main__":
    main()