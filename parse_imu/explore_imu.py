'''
    In-Depth analysis of a1 IMU data collected over 10m of walking
    front and back.

    Graphical analysis of the gyrosocpic and accelerometer data 
    and their relationship

    @author Aditya Varun Pratap
    @versoin 1.0
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Exploration
imu_data_frame = pd.read_csv(
    "parse_imu\walkfrontandback10mlcm_high_state_data.csv")
# All column headers for reference
column_headers = imu_data_frame.columns.tolist()

# Get a general description of the gyroscope data
imu_data_frame['.imu.gyroscope'].describe()
sns.displot(imu_data_frame['.imu.gyroscope'])

# Get a general description of the accelerometer data
imu_data_frame['.imu.accelerometer'].describe()
sns.displot(imu_data_frame['.imu.accelerometer'])

# See how the forward speed is related to the gyroscope
var = '.imu.gyroscope'
data = pd.concat([imu_data_frame['.forwardSpeed'],
                  imu_data_frame[var]], axis=1)
data.plot.scatter(x=var, y='.forwardSpeed', ylim=(0, 800000))

# See how the forward speed is related to the accelerometer
var = '.imu.accelerometer'
data = pd.concat([imu_data_frame['.forwardSpeed'],
                  imu_data_frame[var]], axis=1)
data.plot.scatter(x=var, y='.forwardSpeed', ylim=(0, 800000))


# Box plot analysis of relation ship between the gyroscope, accel, and position
var = '.imu.gyroscope'
data = pd.concat([imu_data_frame['.forwardPosition'],
                  imu_data_frame[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y=".forwardPosition", data=data)
fig.axis(ymin=0, ymax=800000)

var = '.imu.accelerometer'
data = pd.concat([imu_data_frame['.forwardPosition'],
                  imu_data_frame[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y=".forwardPosition", data=data)
fig.axis(ymin=0, ymax=800000)
