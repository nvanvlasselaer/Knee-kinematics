# Screw Home Mechanism Analysis

This Python script is designed to analyze the Screw Home mechanism in knee kinematics using quaternion data from sensors attached to the femur and tibia. The script performs several steps to process the data and visualize the angular differences between the sensors.

## Prerequisites
- Python 3.x
- Ensure you have the necessary Python libraries installed, including numpy, pandas, matplotlib, and scipy

## Usage
1. Make sure you have the required libraries installed.
2. Update the script with your specific data or file paths.
3. Run the script.

## Steps Involved

### 1. Data Preparation
- The script starts by defining necessary functions for converting quaternion data to Euler angles and calculating angular differences.
- Quaternion data and timestamps are iterated through to calculate angular differences between the femur and tibia sensors.
- Data is processed and stored in DataFrames for further analysis.

### 2. Analysis
- The script plots the angular differences over time and identifies rapid changes in knee movement.
- Peaks and valleys in the angular data are detected to mark key points in the motion.
- Data is segmented into flexion and extension phases based on the identified peaks and valleys.
- Averaged dataframes are created for each phase to smooth out variations.

### 3. Visualization
- The script generates visualizations to display the angular differences and segmented data.
- Plots show the angular differences over time, highlighting peaks and valleys.

## Output
- The script provides insights into the Screw Home mechanism by analyzing knee kinematics and visualizing angular differences between sensors.

## Note
- Ensure that the data format matches the expected format in the script.
- Adjust parameters such as thresholds and distances according to your specific dataset.

By following the steps outlined in this script, you can analyze and visualize the Screw Home mechanism in knee kinematics efficiently.

## Steps in more detail

1. **Quaternion to Euler Conversion Functions:**
   - `quaternion_to_euler1` and `quaternion_to_euler2` convert quaternions to Euler angles for two sensors.
   - `calculate_angular_difference` and `calculate_angular_difference_inv` compute angular differences between quaternions.

2. **Data Processing:**
   - The `interate_cvs` function processes quaternion data from a DataFrame (`df`) and stores the results in `converted_data`.
   - The `interate_snapshot_cvs` function processes snapshot quaternion data from a different DataFrame (`df_snapshot`) and stores the results in `converted_snapshot`.

3. **Data Visualization:**
   - Visualizes the angular differences over time using `matplotlib`.

4. **Calibration:**
   - Calculates the mean of all columns in the snapshot data (`extension_baseline`).
   - Subtracts the mean from the data to calibrate (`calibrated_data`).

5. **Rapid Change Detection:**
   - Identifies rapid changes in the derivative of `Degrees_x` and sets a threshold.
   - Determines reference timestamps for further analysis.

6. **Data Trimming:**
   - Trims data based on rapid changes in both directions, ensuring accurate analysis.

7. **Peak and Valley Detection:**
   - Uses `find_peaks` and `peak_prominences` to identify peaks and valleys in the angular differences.

8. **Data Segmentation:**
   - Segments the data based on peaks and valleys, creating cut_dataframes.

9. **Data Averaging:**
   - Rounds the angular difference values in each cut dataframe.
   - Averages dataframes in `cut_dataframes` and plots the results.

10. **Extension and Flexion Dataframes:**
    - Creates extension and flexion dataframes for both Open Kinetic Chain (OKC) and Closed Kinetic Chain (CKC) movements.

11. **Dataframe Merging:**
    - Merges averaged dataframes for extension and flexion for OKC and CKC movements.

12. **Average Calculation:**
    - Calculates average values for each column in the final dataframes.

13. **Dataframe Output:**
    - Outputs averaged dataframes for OKC extension, OKC flexion, CKC extension, and CKC flexion.