import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.spatial.transform import Rotation as R
from scipy.signal import find_peaks, peak_prominences

# read the csv file
refframe = pd.read_csv('TestDATA/Bregje-Lsnapshot.csv')

# Snapshot Counter,Time,w1,x1,y1,z1,loc1_x,loc1_y,loc1_z,time2,w2,x2,y2,z2,loc2_x,loc2_y,loc2_z,stylus_x,stylus_y,stylus_z

# Extract the data
snapshot_counter = refframe['Snapshot Counter']
time = refframe['Time']
w1 = refframe['w1']
x1 = refframe['x1']
y1 = refframe['y1']
z1 = refframe['z1']
loc1_x = refframe['loc1_x']
loc1_y = refframe['loc1_y']
loc1_z = refframe['loc1_z']
time2 = refframe['time2']
w2 = refframe['w2']
x2 = refframe['x2']
y2 = refframe['y2']
z2 = refframe['z2']
loc2_x = refframe['loc2_x']
loc2_y = refframe['loc2_y']
loc2_z = refframe['loc2_z']
stylus_x = refframe['stylus_x']
stylus_y = refframe['stylus_y']
stylus_z = refframe['stylus_z']

print(snapshot_counter)


point_1 = np.array([-stylus_x[0], -stylus_y[0], -stylus_z[0]])
point_2 = np.array([-stylus_x[1], -stylus_y[1], -stylus_z[1]])
point_3 = np.array([-stylus_x[2], -stylus_y[2], -stylus_z[2]])
point_4 = np.array([-stylus_x[3], -stylus_y[3], -stylus_z[3]])
point_5 = np.array([stylus_x[4], stylus_y[4], stylus_z[4]])
point_6 = np.array([stylus_x[5], stylus_y[5], stylus_z[5]])

sensor_1 = np.array([-loc1_x[0], -loc1_y[0], -loc1_z[0]])
sensor_2 = np.array([-loc2_x[0], -loc2_y[0], -loc2_z[0]])


# plot the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# set the limits
ax.set_xlim([-75, 75])
ax.set_ylim([-75, 75])
ax.set_zlim([-75, 75])
ax.scatter(point_1[0], point_1[1], point_1[2], c='r', marker='o')
ax.text(point_1[0], point_1[1], point_1[2], 'point_1')
ax.scatter(point_2[0], point_2[1], point_2[2], c='r', marker='o')
ax.text(point_2[0], point_2[1], point_2[2], 'point_2')
ax.scatter(point_3[0], point_3[1], point_3[2], c='r', marker='o')
ax.text(point_3[0], point_3[1], point_3[2], 'point_3')
ax.scatter(point_4[0], point_4[1], point_4[2], c='r', marker='o')
ax.text(point_4[0], point_4[1], point_4[2], 'point_4')
ax.scatter(point_5[0], point_5[1], point_5[2], c='r', marker='o')
ax.text(point_5[0], point_5[1], point_5[2], 'point_5')
ax.scatter(point_6[0], point_6[1], point_6[2], c='r', marker='o')
ax.text(point_6[0], point_6[1], point_6[2], 'point_6')

ax.scatter(sensor_1[0], sensor_1[1], sensor_1[2], c='g', marker='o')
ax.text(sensor_1[0], sensor_1[1], sensor_1[2], 'sensor_1')
ax.scatter(sensor_2[0], sensor_2[1], sensor_2[2], c='g', marker='o')
ax.text(sensor_2[0], sensor_2[1], sensor_2[2], 'sensor_2')

# center of frame
ax.scatter(0, 0, 0, c='b', marker='d')

# plot line between point 1 and 2

ax.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], [point_1[2], point_2[2]], c='b')

# plot line between point 4 and 5
ax.plot([point_4[0], point_5[0]], [point_4[1], point_5[1]], [point_4[2], point_5[2]], c='b')

# plot line between point 1 and 3
ax.plot([point_1[0], point_3[0]], [point_1[1], point_3[1]], [point_1[2], point_3[2]], c='b')

# plot line between point 4 and 6
ax.plot([point_4[0], point_6[0]], [point_4[1], point_6[1]], [point_4[2], point_6[2]], c='b')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()



print(point_1)


