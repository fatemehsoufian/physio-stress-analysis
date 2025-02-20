import os
import pandas as pd

def add_timestamp_and_id_to_csv(input_csv,id_number):
    print(input_csv)

    csv_name = os.path.splitext(os.path.basename(input_csv))[0]

    try:
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
        measurement_data['Nurse ID'] = id_number
        measurement_data.to_csv(input_csv, index=False)
    
    else:
        timestamp_value = df.iloc[0,0]

        measurement_data = df.iloc[1:].reset_index(drop=True)

        measurement_data.columns = ["Timestamp", "IBI"]

        measurement_data["Timestamp"] = measurement_data["Timestamp"] + timestamp_value
        measurement_data["Nurse ID"] = id_number
        
        measurement_data.to_csv(input_csv, index=False)
