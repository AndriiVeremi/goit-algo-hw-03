import os
import sys
from pathlib import Path

source_folder = Path(sys.argv[1])

try:
    if not source_folder.exists() or not source_folder.is_dir():
        raise FileNotFoundError(f"Error: The folder 📂 '{source_folder}' does not exist or is not a directory.")
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

os.makedirs('dist', exist_ok=True)
dist = Path('path_to_save_files') if Path('path_to_save_files').exists() else Path('dist')

def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse: 📂 This is folder - {element.name}")
            parse_folder(element)
        elif element.is_file():
            print(f"Parse: 📄 This is file - {element.name}")
            sort_and_copy(element)

def sort_and_copy(file_path):
    try:
        file_ext = file_path.suffix[1:].lower() if file_path.suffix else "unknown"
        ext_dir = dist / file_ext
        ext_dir.mkdir(parents=True, exist_ok=True)
        destination = ext_dir / file_path.name
        file_path.replace(destination)
        print(f"File {file_path.name} moved to {destination}")

    except Exception as e:
        print(f"Error while processing file {file_path.name}: {e}")

parse_folder(source_folder)
