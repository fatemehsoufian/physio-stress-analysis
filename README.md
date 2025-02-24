# README 📂

## Branch Overview
In this branch, we merged CSV files without applying any resampling strategy. The following Python files are included:

### **Python Files and Their Functions** 🗂️

1. **extract.py**
   - Contains the `extract` function, which iterates over files to unzip all ZIP archives.

2. **add_attributes.py**
   - Includes the `add_timestamp_and_id_to_csv` function, which iterates over all CSV files and adds:
     - `nurse_id`
     - `timestamp` (calculated based on the initial timestamp and sampling frequency)

3. **remove.py**
   - Contains the `remove_subfolders` function, which cleans up the file and folder hierarchy by:
     - Moving all CSV files to the root directory 📁
     - Deleting subfolders that do not contain CSV files ❌

4. **integrating.py**
   - Includes the `concat_data` function, which concatenates all CSV measurements for specific physiological factors.
   - Final result: Six CSV files are generated 📊:
     - `HR.csv`
     - `IBI.csv`
     - `BVP.csv`
     - `EDA.csv`
     - `ACC.csv`
     - `TEMP.csv`

5. **preprocess.py**
   - The main script that iterates and calls other functions to execute the full pipeline.

---
## Challenges 🚧
### **1. Data Integrity Issues**
   - Some of the `IBI.csv` files are empty ⚠️

### **2. Large File Sizes**
   - The final six CSV files have a **large volume**, especially:
     - `BVP.csv` is over **7GB** 💾
     
   **Potential Solutions:**
   - Apply resampling strategies (downsampling, aggregations, etc.)

---
## Unifying Sampling Rates ⏳

- **Downsampling:** Calculate the Greatest Common Divisor (GCD) for a new sampling rate.
  - **Issue:** Reduces data size, leading to loss of information.
- **Oversampling:** Calculate the Least Common Multiple (LCM) for a new sampling rate.
  - **Issue:** Increases data size, requiring more processing time.


| Signal      | Signal_code | Frequecy(Hz)|
| ----------- | ----------- | ----------- |
| Heart Rate  | HR | 1.0 |
| Electrodermal Activity   | EDA | 4.0 |
| Skin Temperature   | TEMP | 4.0 |
| Accelerometer   | ACC | 32.0 |
| Inter-Beat Interval   | IBI | 64.0 |
| Blood Volume Pulse   | BVP | 64.0 |

---
##  Next Steps 🚀
- Need an optimal resampling strategy to reduce data volume while preserving meaningful information. 
- Determining appropriate sampling intervals for different physiological signals. ⏲️
