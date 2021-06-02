import pandas as pd
import numpy as np
from process_imu import ParseIMU
from complementary_filter import ComplementaryFilter
import matplotlib.pyplot as plt

'''
    This is a controller file to run and test the complementary filter.
    All the data needed to run the filter is initialized here.

    @authors Aditya Pratap, Andrea Covre
'''

# Initialize Variables

imu = ParseIMU()
complementary_filter = ComplementaryFilter()
accelerometer_data = imu.get_accelerometer_data()

gyroscope_data = imu.get_gyroscope_data()
time_seconds = imu.get_time_seconds()

accel_lowpass_data = []
gyro_angles_list = []
gyro_highpass_data = []

# Initial values to use as the previous time step.
accel_lowpass_data.append((1, 1, 1, 1))
gyro_angles_list.append((1, 0, 0, 0))
gyro_highpass_data.append((0, 0, 0, 0))
gyro_angles = imu.get_quaternions()[0]

xPlot = []
yFPlot = []
yPlot = []

# Iterate for length of time steps.\
for i in range(1, len(time_seconds)):

    delta_t = time_seconds[i] - time_seconds[i - 1]

    # Accelerometer low pass and angle calculation
    accel_lowpass = complementary_filter.low_pass(
        accelerometer_data[i], delta_t, accel_lowpass_data[i - 1], 0.05)
    accel_lowpass_data.append(accel_lowpass)
    accel_angles = complementary_filter.compute_accel_angle(accel_lowpass)

    # Gyroscope angle and high pass filter calculation
    gyro_angles = complementary_filter.numeric_integrate_gyro(
        gyroscope_data[i], delta_t, gyro_angles_list[i - 1])
    gyro_angles_list.append(gyro_angles)

    gyro_highpass = complementary_filter.high_pass(
        gyro_angles, gyro_angles_list[i - 1], delta_t, gyro_highpass_data[i - 1], 0.1)
    gyro_highpass_data.append(gyro_highpass)

    # yPlot.append(gyro_highpass_data[i][0])
    xPlot.append(i)

    # Final orientation estimation calculation
    complementary_result = complementary_filter.complementary_filter(
        0.1, accel_angles, gyro_highpass)

    # yFPlot.append(accelerometer_data[i][1])
    # yPlot.append(accel_lowpass_data[i][1])


plt.plot(xPlot, yFPlot, label="accel_raw")
plt.plot(xPlot, yPlot, label="acce_lp")
plt.legend()
plt.show()
