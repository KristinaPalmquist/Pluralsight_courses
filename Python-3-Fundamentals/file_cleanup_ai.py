import os
import shutil

# Define the source directory (Desktop) and target directories
desktop_path = os.path.expanduser("~/Desktop")
images_folder = os.path.join(desktop_path, "Images")
documents_folder = os.path.join(desktop_path, "Documents")
archives_folder = os.path.join(desktop_path, "Archives")

# Create target directories if they don't exist
os.makedirs(images_folder, exist_ok=True)
os.makedirs(documents_folder, exist_ok=True)
os.makedirs(archives_folder, exist_ok=True)

# File type mappings
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
document_extensions = {".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"}
archive_extensions = {".zip", ".rar", ".tar", ".gz", ".7z"}

# Iterate through files on the desktop
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    _, file_extension = os.path.splitext(filename)

  
    # Move files based on their extensions
    if file_extension.lower() in image_extensions:
        shutil.move(file_path, os.path.join(images_folder, filename))
    elif file_extension.lower() in document_extensions:
        shutil.move(file_path, os.path.join(documents_folder, filename))
    elif file_extension.lower() in archive_extensions:
        shutil.move(file_path, os.path.join(archives_folder, filename))

print("Files have been organized into Images, Documents, and Archives folders.")


