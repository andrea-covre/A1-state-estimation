import numpy as np
import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, lfilter
from parse_simu_data import ParseCSV

G = 9.81

filtering_mode = 0

def main():

    IMUFileName = 'inputData/imu-data_fw_10m.csv'

    IMU_data = ParseCSV(IMUFileName)

    timestamps = []
    acc_data = []
    gyro_data = []

    acc_data_x = [] 
    acc_data_y = [] 
    acc_data_z = [] 

    total_time = 0

    for time in range(IMU_data.get_data_size()):

        timestamps.append(IMU_data.get_time_stamp(time))

        acc_data_x.append(IMU_data.get_IMU_acceleration(time)[0])
        acc_data_y.append(IMU_data.get_IMU_acceleration(time)[1])       #=================================
        acc_data_z.append(IMU_data.get_IMU_acceleration(time)[2] - G)   # <- RAW subtraction of gravity
                                                                        #=================================

        gyro_data.append(IMU_data.get_IMU_angular_velocity(time))
    
    timeUnit = timestamps[len(timestamps) - 1] - timestamps[0]
    timeUnit = timeUnit / len(timestamps)

    acc_data.append(acc_data_x)
    acc_data.append(acc_data_y)
    acc_data.append(acc_data_z)

    #Filtering ----
    # Filter requirements.
    T = timeUnit     # Sample Period
    fs = T**(-1)     # sample rate, Hz
    cutoff = 0.005   # desired cutoff frequency of the filter, Hz ,         -> 0.1
    nyq = 0.4 * fs   # Nyquist Frequency                                    -> 0.6
    order = 3        # sin wave can be approx represented as quadratic      -> 2
    #n = int(T * fs) # total number of samples

    alpha = 0.125

    if (filtering_mode == 0):
        filtered_x = butter_lowpass_filter(acc_data[0], cutoff, fs, order, nyq)
        filtered_y = butter_lowpass_filter(acc_data[1], cutoff, fs, order, nyq)
        filtered_z = butter_lowpass_filter(acc_data[2], cutoff, fs, order, nyq)

    else:
        filtered_x = []
        filtered_y = []
        filtered_z = []

        filtered_x.append(acc_data[0][0])
        filtered_y.append(acc_data[1][0])
        filtered_z.append(acc_data[2][0])

        for i in range(1, IMU_data.get_data_size()):
            filtered_x.append(alpha * acc_data[0][i] + (1 - alpha) * acc_data[0][i-1])
            filtered_y.append(alpha * acc_data[1][i] + (1 - alpha) * acc_data[1][i-1])
            filtered_z.append(alpha * acc_data[2][i] + (1 - alpha) * acc_data[2][i-1])

    fig, axs = plt.subplots(2, 2)

    """
    #Plot filtered acc against averaged acc ---> mode needs to be set to 1
    test_filtered_x = butter_lowpass_filter(acc_data[0], cutoff, fs, order, nyq)
    test_filtered_y = butter_lowpass_filter(acc_data[1], cutoff, fs, order, nyq)
    test_filtered_z = butter_lowpass_filter(acc_data[2], cutoff, fs, order, nyq)

    plt.plot(timestamps, filtered_x, label="avg_acc_x")
    plt.plot(timestamps, test_filtered_x, label="filtered_acc_x")

    plt.plot(timestamps, filtered_y, label="avg_acc_y")
    plt.plot(timestamps, test_filtered_y, label="filtered_acc_y")

    plt.plot(timestamps, filtered_z, label="avg_acc_z")
    plt.plot(timestamps, test_filtered_z, label="filtered_acc_z")
    """

  
    #Plot raw acceleration
    axs[0,0].plot(timestamps, acc_data[0], label="raw_acc_x")
    axs[0,0].plot(timestamps, acc_data[1], label="raw_acc_y")
    axs[0,0].plot(timestamps, acc_data[2], label="raw_acc_z")
    axs[0,0].set_title("Raw Acceleration")


    
    #Plot filtered acceleration
    axs[0,1].plot(timestamps, filtered_x, label="filtered_acc_x")
    axs[0,1].plot(timestamps, filtered_y, label="filtered_acc_y")
    axs[0,1].plot(timestamps, filtered_z, label="filtered_acc_z")
    axs[0,1].set_title("Filtered Acceleration")
    


    #Velocity arrays
    xV = []
    yV = []
    zV = []

    #Setting starting point to 0
    xV.append(0)
    yV.append(0)
    zV.append(0)

    vel = []

    #Finding velocity
    for i in range(1, IMU_data.get_data_size()):
        dt = IMU_data.get_time_stamp(i) - IMU_data.get_time_stamp(i - 1)
        xV.append(xV[i-1] + filtered_x[i] * dt)
        yV.append(yV[i-1] + filtered_y[i] * dt) 
        zV.append(zV[i-1] + filtered_z[i] * dt) 
                                                     
    
    
    #Plot Velocity
    axs[1,0].plot(timestamps, xV, label="vel_x")
    axs[1,0].plot(timestamps, yV, label="vel_y")
    axs[1,0].plot(timestamps, zV, label="vel_z")
    axs[1,0].set_title("Velocity")
    
    

    xP = []
    yP = []
    zP = []

    xP.append(0)
    yP.append(0)
    zP.append(0)

    pos = []

    #Finding position
    for i in range(1, IMU_data.get_data_size()):
        dt = IMU_data.get_time_stamp(i) - IMU_data.get_time_stamp(i - 1)
        xP.append(xP[i-1] + xV[i] * dt)
        yP.append(yP[i-1] + yV[i] * dt)
        zP.append(zP[i-1] + zV[i] * dt)

    
    #Plot position
    axs[1,1].plot(timestamps, xP, label="x")
    axs[1,1].plot(timestamps, yP, label="y")
    axs[1,1].plot(timestamps, zP, label="z")
    axs[1,1].set_title("Position")
    

    """
    #Plot X-Y map
    plt.plot(yP, xP, label="trace")
    """


    plt.legend()
    plt.show()

def butter_lowpass_filter(data, cutoff, fs, order, nyq):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

"""
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
"""

if __name__ == "__main__":
    main()