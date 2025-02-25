import pandas as pd
from pathlib import Path
import os

def resample_dataframe(data_file):
    """
    Resample sensor data to a common frequency of 4 Hz (250ms interval).

    Parameters:
        data_file (str): Path to the CSV file containing sensor data.

    Returns:
        pd.DataFrame: Resampled DataFrame with datetime index.
    """
    data_df = pd.read_csv(data_file)
    # Extract filename
    file_name = os.path.basename(data_file)
    data_df['datetime'] = pd.to_datetime(data_df['Timestamp'], unit='s')

    # Set the datetime column as the index for resampling
    data_df.set_index('datetime', inplace=True)

    # Define common resampling interval for 4 Hz (every 250ms)
    resample_interval = '250ms'

    match file_name:
        case _ if file_name.startswith("HR"):
            nurse_id = data_df["Nurse ID"].iloc[0]
            # HR (Heart Rate) is originally at 1 Hz -> upsample to 4 Hz using interpolation
            resampled_df = data_df.resample(resample_interval).interpolate(method='time')
            resampled_df["Nurse ID"] = nurse_id  # Assign back the original ID
        
        case _ if file_name.startswith("ACC") or file_name.startswith("BVP"):
            nurse_id = data_df["Nurse ID"].iloc[0]
            # ACC (32 Hz) and BVP (64 Hz) -> downsample to 4 Hz using mean aggregation
            resampled_df =  data_df.resample(resample_interval).asfreq()
            resampled_df["Nurse ID"] = nurse_id  # Assign back the original ID
        
        case _ if file_name.startswith("TEMP") or file_name.startswith("EDA"):
            nurse_id = data_df["Nurse ID"].iloc[0]
            # TEMP (4 Hz) and EDA (4 Hz) -> Do nothing, return the original DataFrame unchanged
            resampled_df = data_df
            resampled_df["Nurse ID"] = nurse_id  # Assign back the original ID

        case _:
            return "Invalid data file"

    return resampled_df
        
def resampling(sensor_data_dir):
    resampled_data_dir = "dmp-dataset\Resampled"
    os.makedirs(resampled_data_dir, exist_ok=True)

    for file_path in Path(sensor_data_dir).glob("*.csv"):  
        file_path_str = str(file_path)
        print(f"Resampling: {file_path_str}")

        resampled_df = resample_dataframe(file_path_str)

        output_path = Path(resampled_data_dir) / f"resampled_{file_path.name}"
        resampled_df.to_csv(output_path)

        print(f"Resampled CSV Saved: {output_path}")

    print("Resampling complete for all files!")