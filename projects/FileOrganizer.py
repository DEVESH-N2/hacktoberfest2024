import os
import shutil

def organize_files(directory):
    file_types = {
        "Documents": [".pdf", ".docx", ".txt"],
        "Images": [".jpg", ".jpeg", ".png"],
        "Videos": [".mp4", ".mov"],
    }
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            for folder, extensions in file_types.items():
                if filename.endswith(tuple(extensions)):
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(filepath, folder_path)
                    print(f"Moved {filename} to {folder}")
                    break

# Example usage
organize_files("/path/to/your/folder")
