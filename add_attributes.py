import os
import pandas as pd

def add_timestamp_and_id_to_csv(input_csv,id_number):
    print(f"Adding timestamp and id to {input_csv}")

    csv_name = os.path.splitext(os.path.basename(input_csv))[0]

    df = pd.read_csv(input_csv, header=None)

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