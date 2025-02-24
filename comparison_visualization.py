import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def compare_original_resampled(original_df, resampled_df, file_name):
    
    # Convert Timestamp to datetime for original dataset
    original_df['Timestamp'] = pd.to_datetime(original_df['Timestamp'], unit='s')

    plt.figure(figsize=(14, 6))

    # Determine metric type based on file name
    if file_name.startswith("HR"):
        metric_name = "HR"
    elif file_name.startswith("BVP"):
        metric_name = "BVP"
    elif file_name.startswith("ACC"):
        metric_name = "ACC"
    else:
        print(f"⚠ Unknown metric in file: {file_name}. Supported: 'HR', 'BVP', 'ACC'")
        return

    if metric_name == "HR":  
        df_filtered = filter_first_second(original_df, 'Timestamp',5)
        df_resampled_filtered = filter_first_second(resampled_df, 'datetime',5)

        # Resampled data
        plt.plot(df_resampled_filtered['datetime'], df_resampled_filtered[metric_name], linestyle='-', marker='s', color='red', alpha=0.7, label=f"Resampled {metric_name}")

        # Original data
        plt.plot(df_filtered['Timestamp'], df_filtered[metric_name], linestyle='-', marker='o', color='blue', alpha=0.5, label=f"Original {metric_name}")

    if metric_name == "BVP":  
        df_filtered = filter_first_second(original_df, 'Timestamp',1)
        df_resampled_filtered = filter_first_second(resampled_df, 'datetime',1)

        # Original data
        plt.plot(df_filtered['Timestamp'], df_filtered[metric_name], linestyle='-', marker='o', color='blue', alpha=0.5, label=f"Original {metric_name}")

         # Resampled data
        plt.plot(df_resampled_filtered['datetime'], df_resampled_filtered[metric_name], linestyle='-', marker='s', color='red', alpha=0.7, label=f"Resampled {metric_name}")

    elif metric_name == "ACC":  
        df_filtered = filter_first_second(original_df, 'Timestamp',1)
        df_resampled_filtered = filter_first_second(resampled_df, 'datetime',1)

        # Original Accelerometer Data
        plt.plot(df_filtered['Timestamp'], df_filtered['X'], linestyle='-', marker='o', markersize=5, color='red', alpha=0.6, label="Original X")
        plt.plot(df_filtered['Timestamp'], df_filtered['Y'], linestyle='-', marker='o', markersize=5, color='blue', alpha=0.6, label="Original Y")
        plt.plot(df_filtered['Timestamp'], df_filtered['Z'], linestyle='-', marker='o', markersize=5, color='green', alpha=0.6, label="Original Z")

        # Resampled Accelerometer Data
        plt.plot(df_resampled_filtered['datetime'], df_resampled_filtered['X'], linestyle='-', marker='s', markersize=5, color='red', alpha=0.9, label="Resampled X")
        plt.plot(df_resampled_filtered['datetime'], df_resampled_filtered['Y'], linestyle='-', marker='s', markersize=5, color='blue', alpha=0.9, label="Resampled Y")
        plt.plot(df_resampled_filtered['datetime'], df_resampled_filtered['Z'], linestyle='-', marker='s', markersize=5, color='green', alpha=0.9, label="Resampled Z")
    
    plt.xlabel("Timestamp")
    plt.ylabel(f"{metric_name}")
    plt.title(f"Comparison of Original and Resampled {metric_name}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
    

def filter_first_second(df, time_column,time_limit):
    df = df.dropna(subset=[time_column])  
    df[time_column] = pd.to_datetime(df[time_column], errors='coerce')
    df = df.sort_values(by=time_column)
    start_time = df[time_column].iloc[0]
    end_time = start_time + pd.Timedelta(seconds=time_limit)
    return df[(df[time_column] >= start_time) & (df[time_column] < end_time)]