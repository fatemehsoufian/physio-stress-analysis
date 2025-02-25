import os
import shutil

def remove_subfolders(root_dir):
    counter = 1  

    # Move and rename CSV files
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for file in filenames:
            if file.endswith(".csv"):
                new_filename = f"{os.path.splitext(file)[0]}_{counter}.csv"
                counter += 1 
                
                old_path = os.path.join(dirpath, file)
                new_path = os.path.join(root_dir, new_filename)
                
                shutil.move(old_path, new_path)

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        contains_csv = any(file.endswith(".csv") for file in filenames)
        
        # If folder is empty or does not contain CSV files, remove it
        if not contains_csv:
            shutil.rmtree(dirpath)

    print("CSV files moved and renamed, non-CSV folders deleted.")

def delete_ibi_and_tags_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith("IBI") or filename.startswith("tags"):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path) 
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")