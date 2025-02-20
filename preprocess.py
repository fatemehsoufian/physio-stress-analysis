import os
import pandas as pd
from add_attributes import add_timestamp_and_id_to_csv
from extract import extract 
from remove import remove_subfolders
from integrating import integrate_data

base_path = "dmp-dataset\\Stress_dataset"
nurses_id = ["5C","6B","6D","7A","7E","8B","15","83","94","BG","CE","DF","E4","EG","F5"]

def merge_all():
    for nurse in nurses_id:
         cur_path = os.path.join(base_path, nurse)
         for folder in os.scandir(cur_path):
            id, time = folder.name.split("_")
            folder_path = folder.path
            
            for file in os.scandir(folder_path):
                if file.is_file() and file.name.endswith('.csv'):
                    if file.name != "tags.csv":
                        csv_file = file.path
                        add_timestamp_and_id_to_csv(csv_file,nurse)

extract(".")
merge_all()
remove_subfolders()
integrate_data()
