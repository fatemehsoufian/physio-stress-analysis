import zipfile
import os
import pandas as pd

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
                        add_timestamp_to_csv(csv_file)

def add_timestamp_to_csv(input_csv):
    print(input_csv)

    csv_name = os.path.splitext(os.path.basename(input_csv))[0]

    try:
        # Read the CSV
        df = pd.read_csv(input_csv, header=None)
    except pd.errors.EmptyDataError:
        print(f"⚠️ Skipped: {input_csv} (No data to parse)")
        return
    
    if("IBI.csv" not in input_csv):
        initial_time = float(df.iloc[0, 0])  # Unix timestamp (UTC)
        sample_rate = float(df.iloc[1, 0])  # Sample rate (Hz)
        measurement_data = df.iloc[2:].reset_index(drop=True)
        time_intervals = pd.Series([initial_time + i * (1/sample_rate) for i in range(len(measurement_data))])
        if measurement_data.shape[1] == 3:
            measurement_data.columns = ['X', 'Y', 'Z']
        else:
            measurement_data = measurement_data.iloc[:, [0]]  # Ensures it's a DataFrame
            measurement_data.columns = [csv_name] 
        
        measurement_data['Timestamp'] = time_intervals
        measurement_data.to_csv(input_csv, index=False)
    
    else:
        timestamp_value = df.iloc[0,0]

        measurement_data = df.iloc[1:].reset_index(drop=True)

        measurement_data.columns = ["Timestamp", "IBI"]

        measurement_data["Timestamp"] = measurement_data["Timestamp"] + timestamp_value
        
        measurement_data.to_csv(input_csv, index=False)

extract(".")
merge_all()





  