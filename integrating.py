import pandas as pd
import glob

prefixes = ["EDA", "HR", "IBI", "BVP", "ACC", "TEMP"]

def concat_data(metric):

    output_file = f"{metric}.csv"

    # Initialize an empty file
    with open(output_file, "w",newline='') as outfile:
        header_written = False  # Track if the header is written

        csv_files = glob.glob(f"dmp-dataset\Stress_dataset\{metric}_*.csv")

        if csv_files:
            for file in csv_files:
                print(f"Processing: {file}")
                try:
                    input_file = pd.read_csv(file, chunksize=50000)
                except pd.errors.EmptyDataError:
                    continue
                # Read file in chunks
                for chunk in input_file:
                    chunk.to_csv(outfile, mode="a", index=False, header=not header_written)
                    header_written = True  # Ensure header is written only once

    print(f"Merged file saved as '{output_file}'")

def integrate_data():
    for prefix in prefixes:
        concat_data(prefix)