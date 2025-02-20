import os
import zipfile

def extract(directory_path):
    for dir in os.scandir(directory_path):
        if dir.is_file() and dir.path.endswith(".zip"):
            extract_path = dir.path[:-4]
            with zipfile.ZipFile(dir.path, 'r') as zip_ref:
                print(f'extracting {dir.path}')
                zip_ref.extractall(extract_path)

            os.remove(dir.path)
            extract(extract_path)

        elif dir.is_dir():  # If it's a directory, go inside to check for zip files
            extract(dir.path)