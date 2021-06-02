import numpy as np
import pandas as pd
import csv
import math
import os
import sys

# import DataInfo
upperCwd = os.path.dirname(os.getcwd())
kdlCwd = upperCwd + "/ekf/"
print(kdlCwd)
sys.path.append(kdlCwd)

from datainfo import DataInfo

'''
    The purpose of this class is to parse the imu csv file to extract 
    needed imformation in desired format.

    @authors Aditya Pratap, Andrea Covre, Kinnera Banda
'''

class ParseCSV:

    def __init__(self):
        self.dataInfoObjs = []

        jointAnglesCols = ['position_0', 'position_1', 'position_2', 'position_3', 'position_4',
         'position_5', 'position_6', 'position_7', 'position_8' ,'position_9', 'position_10', 'position_11']

        self.imuData = pd.read_csv("csv/walk_fw_10m/mu-data.csv")
        self.jointsData = pd.read_csv("csv/walk_fw_10m/oint_states.csv", usecols = jointAnglesCols)
        self.footContactsData = pd.read_csv("csv/walk_fw_10m/oot_contacts.csv")

        for i in range(len(self.imuData)):
            dataInfo = DataInfo()
            self.dataInfoObjs.append(dataInfo)

        self.readTimeStamps(self.imuData)
        self.readLinearAcceleration(self.imuData)
        self.readAngularVelocity(self.imuData)
        self.readJointAngles(self.jointsData)
        self.readFootContacts(self.footContactsData)

    def readTimeStamps(self, imuData):
        timeStamps = imuData['Time']
        
        for i in range(len(timeStamps)):
            self.dataInfoObjs[i].timestamp = timeStamps[i]
        

    #Return IMU linear acceleration
    def readLinearAcceleration(self, imuData):

        x = np.array(self.imuData['linear_acceleration.x'])
        y = np.array(self.imuData['linear_acceleration.y'])
        z = np.array(self.imuData['linear_acceleration.z'])

        for i in range(len(x)):
            self.dataInfoObjs[i].lin_accel =  np.array([x[i], y[i], z[i]])
        

    #Return IMU angular velocity
    def readAngularVelocity(self, imuData):

        x = np.array(self.imuData['angular_velocity.x'])
        y = np.array(self.imuData['angular_velocity.y'])
        z = np.array(self.imuData['angular_velocity.z'])

        for i in range(len(x)):
            self.dataInfoObjs[i].ang_vel =  np.array([x[i], y[i], z[i]])
    
    def readJointAngles(self, jointsData):

        jointsList = jointsData.values.tolist()
        for i in range(len(jointsList) - 1):
            self.dataInfoObjs[i].joint_angles = jointsList[i]
            
    def readFootContacts(self, footData):
        contacts = footData['contacts']

        for i in range(len(contacts) - 1):
            self.dataInfoObjs[i].feet_contact = contacts[i]
    
    
    def getDataInfoObjects(self):
        return self.dataInfoObjs
       


parsecsv = ParseCSV()
dataInfoList = parsecsv.getDataInfoObjects()
print(dataInfoList[0].getTimestamp())
print(dataInfoList[0].getLinearAccel())
print(dataInfoList[0].getAngVel())
print(dataInfoList[0].getJointAngles())
print(dataInfoList[0].getFeetContactData())
