# Screw Home Mechanism Analysis

This Python script is designed to analyze the Screw Home mechanism in knee kinematics using quaternion data from sensors attached to the femur and tibia, using electromagnetic trackers or Inertial measurement unit sensors. The script performs several steps to process the data and visualize the angular differences between the sensors. The workflow involves using the "kneekinematics.ipynb" notebook first to process raw data, followed by the "Data-analysis.ipynb" notebook for detailed analysis. All data required for these notebooks is located in the Data folder.

## Prerequisites
Python 3.x
Jupyter Notebook
Required Python packages: 
- numpy
- pandas
- matplotlib
- scipy
- sklearn

## Usage
1. Make sure you have the required libraries installed.
2. Update the script with your specific data or file paths.
3. Run the script.

## kneekinematics.ipynb

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

## Data-analysis.ipynb

# Functional Data Analysis and Clustering Script

## Overview
This script performs functional data analysis and clustering on a dataset of subjects. The process involves preparing the data, performing functional principal component analysis (FPCA), and clustering the subjects based on the principal components. The clusters are then visualized and the results are printed.

## Steps

## Set limit for range of flexion/extension degrees

### 1. Define the List of Subjects and Data to Use
- Specify the list of subjects and the corresponding subject names to use in the analysis.
- The `subjects` variable can be set to `all_subjects_zero` or `subjects_zero_L`.
- The `subjects_name` variable should match the corresponding subjects list name.
- Define the data column to use from the dataset with `data_from_list`.

### 2. Prepare Functional Data
- Initialize empty lists `X`, `Xder`, and `subject_names` to store spline regression curves, their derivatives, and subject names, respectively.
- Iterate over each subject's data to:
  - Calculate the derivatives of the selected data column and append to `Xder`.
  - Append the original data values to `X`.
  - Append the subject names to `subject_names`.
- Convert the lists `X` and `Xder` to NumPy arrays.

### 3. Create FDataGrid Objects
- Create `FDataGrid` objects for the data matrix `X` and its derivatives `Xder`.

### 4. Apply Functional Principal Component Analysis (FPCA)
- Define the number of principal components `n_components` to retain.
- Perform FPCA on the `FDataGrid` objects to obtain the transformed FPCA scores for both the data and its derivatives.

### 5. Perform Clustering on the FPCA Scores
- Define the number of clusters `n_clusters`.
- Use the KMeans clustering algorithm to fit the FPCA scores of the derivatives and predict cluster assignments.
- Assign colors to the clusters for visualization.

### 6. Print the Clusters
- For each cluster, find the indices of subjects belonging to that cluster.
- Print the subject names grouped by their cluster assignments.

### 7. Visualize Clusters
- Create a plot to visualize the clusters.
- Plot the data points for each subject in their respective clusters with assigned colors.
- Add labels, title, and legend to the plot.
- Draw a horizontal line at y=0 for reference.

### 8. Create Subject-Cluster Mapping
- Create a dictionary mapping each subject name to their corresponding cluster number.
- Convert this dictionary to a DataFrame for easy viewing and export.

### 9. Display the DataFrame
- Print the DataFrame showing the subject names and their cluster assignments.

## Libraries and Dependencies
- `numpy` for numerical operations.
- `pandas` for handling data structures and data analysis.
- `matplotlib` for plotting and visualization.
- `FDataGrid` and `FPCA` from `skfda` for functional data analysis.
- `KMeans` from `sklearn.cluster` for clustering.


