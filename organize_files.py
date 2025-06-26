import os
import shutil
from pathlib import Path

# Define the categories and their associated extensions
FILE_CATEGORIES = {
    "images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    "pdfs": ['.pdf'],
    "word_docs": ['.doc', '.docx'],
    "code_files": ['.py', '.js', '.ts', '.html', '.css', '.php', '.cpp', '.c', '.java', '.json', '.xml', '.sh', '.rb', '.go', '.cs'],
}

def create_folder_if_not_exists(folder_path):
    """Ensure a directory exists."""
    os.makedirs(folder_path, exist_ok=True)

def get_category(file_extension):
    """Return the folder name based on file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return None  # Skip files that don't match any category

def move_file(file_path, destination_folder):
    """Move a file to a destination folder, handling name conflicts."""
    create_folder_if_not_exists(destination_folder)
    base_name = file_path.name
    target_path = destination_folder / base_name

    # Avoid overwriting files
    count = 1
    while target_path.exists():
        new_name = f"{file_path.stem}_{count}{file_path.suffix}"
        target_path = destination_folder / new_name
        count += 1

    shutil.move(str(file_path), str(target_path))

def organize_files(source_folder):
    """Organize files into categorized folders."""
    source = Path(source_folder)
    if not source.exists() or not source.is_dir():
        print(f"Source folder {source_folder} does not exist.")
        return

    for file_path in source.iterdir():
        if file_path.is_file():
            category = get_category(file_path.suffix)
            if category:
                destination_folder = source / category
                move_file(file_path, destination_folder)
                print(f"Moved: {file_path.name} -> {category}/")
            else:
                print(f"Skipped: {file_path.name}")

if __name__ == "__main__":
    # Set the path to the folder where your files are
    folder_to_organize = "./your-folder-path-here"
    organize_files(folder_to_organize)
