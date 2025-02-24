import os
from add_attributes import add_timestamp_and_id_to_csv
from extract import extract 
from remove import remove_subfolders, delete_ibi_and_tags_files
from integrating import integrate_data
from resampling import resampling
from comparison_visualization import compare_original_resampled
import pandas as pd

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
delete_ibi_and_tags_files("dmp-dataset\Stress_dataset")
resampling()
integrate_data()

# original = pd.read_csv("D:\dmp-dataset\Stress_dataset\ACC_1.csv")
# resample = pd.read_csv("D:/dmp-dataset/Resampled/resampled_ACC_1.csv")
# compare_original_resampled(original,resample,"ACC")

# original = pd.read_csv("D:\dmp-dataset\Stress_dataset\BVP_3705.csv")
# resample = pd.read_csv("D:/dmp-dataset/Resampled/resampled_BVP_3705.csv")
# compare_original_resampled(original,resample,"BVP")

# original = pd.read_csv("D:\dmp-dataset\Stress_dataset\HR_3770.csv")
# resample = pd.read_csv("D:/dmp-dataset/Resampled/resampled_HR_3770.csv")
# compare_original_resampled(original,resample,"HR")