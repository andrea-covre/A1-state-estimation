import numpy as np
import pandas as pd
import csv
import math

class ParseCSV:

    def __init__(self, fileName):
        self.data_frame = pd.read_csv(fileName)


    #Return the size of joints dataset

    def get_data_size(self):
        return self.data_frame.shape[0]


    #Return the time stamps

    def get_time_stamp(self, index):
        return self.data_frame['Time'][index]


    #Return foot contact
    def get_foot_contact(self, index):
        return self.data_frame['contacts'][index]

    #Return the parsed joints angle data

    def get_joints_angle(self, index):

        q = [
                [
                    self.data_frame['position_2'][index],
                    self.data_frame['position_1'][index],
                    self.data_frame['position_0'][index]
                ],
                [

                    self.data_frame['position_5'][index],
                    self.data_frame['position_4'][index],
                    self.data_frame['position_3'][index]
                ],
                [
                    self.data_frame['position_8'][index],
                    self.data_frame['position_7'][index],
                    self.data_frame['position_6'][index]
                ],
                [
                    self.data_frame['position_11'][index],
                    self.data_frame['position_10'][index],
                    self.data_frame['position_9'][index]
                ]
            ]

        q = [
                [q[0][2], q[0][1], q[0][0]],
                [q[1][2], q[1][1], q[1][0]],
                [q[2][2], q[2][1], q[2][0]],
                [q[3][2], q[3][1], q[3][0]]
            ]

        return q


    #Return IMU linear acceleration
    def get_IMU_acceleration(self, index):

        x = self.data_frame['linear_acceleration.x'][index]
        y = self.data_frame['linear_acceleration.y'][index]
        z = self.data_frame['linear_acceleration.z'][index]

        return (x, y, z)


    #Return IMU angular velocity
    def get_IMU_angular_velocity(self, index):

        x = self.data_frame['angular_velocity.x'][index]
        y = self.data_frame['angular_velocity.y'][index]
        z = self.data_frame['angular_velocity.z'][index]

        return (x, y, z)