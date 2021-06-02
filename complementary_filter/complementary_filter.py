
from process_imu import ParseIMU
import numpy as np
import math
from scipy.signal import butter, filtfilt
from scipy.spatial.transform import Rotation


'''
    Complementary Filter implementation to compensate for accelerometer noise
    and gyroscopic drift. The filter will estimate the optimal (correct) angle 
    of the robot.

    @authors Aditya Pratap, Andrea Covre
    @version 1.0
'''


class ComplementaryFilter:
    imu = ParseIMU()

    '''
        This method filters the raw accelerometer data by allowing data less than 
        a specified frequncy to pass through.

        Filter Design:
            LPFi = alpha * acceli + (1 - alpha) * LPFi-1.
            alpha = delta_t / (rc + delta_t)
            rc = 1 / (2 * pi * cutoff frequency)

        @param accel_values      The raw accelerometer data as collected from the robot. 
                                 Acceleration in the x,y, and z directions.
        @param delta_T           The time difference from the current time_step and the previous
                                 time step.
        @param accel_lp_previous The low-pass accel values calculated in the previous time step (LPF i-1)
        @param cutoff_frequency  The cutoff frequency of the low-pass filter. 
    '''

    def low_pass(self, accel_values, delta_t, accel_lp_previous, cutoff_frequency):
        r_c = 1 / (2 * math.pi * cutoff_frequency)
        filter_const = delta_t / (r_c + delta_t)

        accel_x = filter_const * \
            accel_values[0] + (1 - filter_const) * accel_lp_previous[0]
        accel_y = filter_const * \
            accel_values[1] + (1 - filter_const) * accel_lp_previous[1]
        accel_z = filter_const * \
            accel_values[2] + (1 - filter_const) * accel_lp_previous[2]

        return (accel_x, accel_y, accel_z)

    '''
        This method calculates the accelerometer angles for each axis.

        Angle Calculations:
            theta = arctan(accelX / sqrt(accelY^2 + accelZ^2))

            psi = arctan(accelY/ sqrt(accelX^2 + accelZ^2))

            phi = arctan(sqrt(accelX^2 + accelY^2) / accelZ)

        @param accel_values The low-pass filtered accelerometer readings

        @return Accelerometer angles in quaternion representation.
    '''

    def compute_accel_angle(self, accel_values):
        # Tokenize data
        accelx_lp = accel_values[0]
        accely_lp = accel_values[1]
        accelz_lp = accel_values[2]


        # Compute the accel angle
        x = math.sqrt((accely_lp * accely_lp) + (accelz_lp * accelz_lp))
        angle_x = math.atan(accelx_lp / x)

        y = math.sqrt((accelx_lp * accelx_lp) + (accelz_lp * accelz_lp))
        angle_y = math.atan(accely_lp / y)

        z = math.sqrt((accelx_lp * accelx_lp) + (accely_lp * accely_lp))
        angle_z = math.atan(z / accelz_lp)

        # Convert euler to quternion format.
        return self.euler_to_quaternion(angle_x, angle_y, angle_z)

    # Gyrosocpic Data

    '''
        This method performs discrete numeric integration over the gyroscopic data
        to estimate the gyroscope orientation (angles). 'Dead Reckoning'. 

        Equation:
            Angle_Gyro(i) = Angle_Gyro(i - 1) + Gyro_y * delta_t

        @param gyroscope_data       The raw gyroscope data as collected from the robot.
        @param delta_t              The time difference btween the current time step and the precious.
        @param estimated_quaternion The estimated gyrscope angles in quternion format from the previous time step.

        @return The estimated gyro angles in quaternion representation.

    '''

    def numeric_integrate_gyro(self, gyroscope_data, delta_t, estimated_quaternion):

        # Calculate the magnitude of the gyro measurement and multiply by the time differential.
        omega_x = gyroscope_data[0]
        omega_y = gyroscope_data[1]
        omega_z = gyroscope_data[2]

        omega_mag = math.sqrt(omega_x**2 + omega_y**2 + omega_z**2)
        theta = omega_mag * delta_t

        if(omega_mag != 0):
            normalize_vx = omega_x / omega_mag
            normalize_vy = omega_y / omega_mag
            normalize_vz = omega_z / omega_mag

            normalize_vector = (normalize_vx, normalize_vy, normalize_vz)

            # Q.update = (cos(theta/2),v_x * sin(theta/2), v_y * sin(theta/2), v_z * sin(theta/2));
            quaternion_update = (math.cos((theta)/2), normalize_vx * math.sin(
                theta/2), normalize_vy * math.sin(theta/2), normalize_vz * math.sin(theta/2))
            estimated_quaternion = self.quaternion_multiply(
                quaternion_update, estimated_quaternion)

        return estimated_quaternion

    '''
        This method filters the gyroscopic angles by only allowing the frequencies higher than the 
        specified frequency.

        Filter Design:
            HPFi = alpha * HPF (i - 1) + alpha *(Angle_Gyro(i) - Angle_Gyro(i - 1))
            alpha = (rc / rc + delta_t)
            rc = 1 / (2 * pi * cutoff_frequency)

            *alpha is the cutoff frequency

        @param quaternions          The current gyroscope angle estimates in quaternion format (i).
        @param quaternions_previous The gyroscope angle estimates in the previous time step (i-1).
        @param delta_t              The time difference between the current time step and the previous.
        @param gyro_hp_previous     The high-pass filtered gyroscopic angles from the previous time step.
        @param cutoff_frequency     The cutoff frequency for the filter.

        @return The high-pass filtered gyro angles in quaternion representation.
    '''

    def high_pass(self, quaternions, quaternions_previous, delta_t, gyro_hp_previous, cutoff_frequency):
        r_c = 1 / (2 * math.pi * cutoff_frequency)
        filter_const = r_c / (r_c + delta_t)
        gyro_angle_q1 = filter_const * \
            gyro_hp_previous[0] + filter_const * \
            (quaternions[0] - quaternions_previous[0])

        gyro_angle_q2 = filter_const * \
            gyro_hp_previous[1] + filter_const * \
            (quaternions[1] - quaternions_previous[1])

        gyro_angle_q3 = filter_const * \
            gyro_hp_previous[2] + filter_const * \
            (quaternions[2] - quaternions_previous[2])

        gyro_angle_q4 = filter_const * \
            gyro_hp_previous[3] + filter_const * \
            (quaternions[3] - quaternions_previous[3])

        return (gyro_angle_q1, gyro_angle_q2, gyro_angle_q3, gyro_angle_q4)

    '''
        This method combines the result from the compute_accel_angles and the 
        high_pass() methods to form the complementary filter.

        Filter Design:
            Angle = alpha * (accel_angles) + (1 - alpha) (Angle_gyro)
        
        @param filter_const The filter constant
        @param accel_angles The low-pass filtered accelerometer angles
        @param gyro_highpas The high-pass filtered gyroscopic angles

        @return The estimated orientation of the robot in quaternion representation.
    '''

    def complementary_filter(self, filter_const, accel_angles, gyro_highpass):
        comp_q1 = filter_const * \
            accel_angles[0] + (1 - filter_const) * gyro_highpass[0]
        comp_q2 = filter_const * \
            accel_angles[1] + (1 - filter_const) * gyro_highpass[1]
        comp_q3 = filter_const * \
            accel_angles[2] + (1 - filter_const) * gyro_highpass[2]
        comp_q4 = filter_const * \
            accel_angles[3] + (1 - filter_const) * gyro_highpass[3]
        return (comp_q1, comp_q2, comp_q3, comp_q4)

    '''
        Helper method to help multiply two quaternions
    '''

    def quaternion_multiply(self, quaternion1, quaternion0):
        w0, x0, y0, z0 = quaternion0
        w1, x1, y1, z1 = quaternion1
        return np.array([-x1 * x0 - y1 * y0 - z1 * z0 + w1 * w0,
                         x1 * w0 + y1 * z0 - z1 * y0 + w1 * x0,
                         -x1 * z0 + y1 * w0 + z1 * x0 + w1 * y0,
                         x1 * y0 - y1 * x0 + z1 * w0 + w1 * z0], dtype=np.float64)

    '''
        Helper method t help convert euler angles to quaternions
    '''

    def euler_to_quaternion(self, x, y, z):

        qx = np.sin(x/2) * np.cos(y/2) * np.cos(z/2) - \
            np.cos(x/2) * np.sin(y/2) * np.sin(z/2)
        qy = np.cos(x/2) * np.sin(y/2) * np.cos(z/2) + \
            np.sin(x/2) * np.cos(y/2) * np.sin(z/2)
        qz = np.cos(x/2) * np.cos(y/2) * np.sin(z/2) - \
            np.sin(x/2) * np.sin(y/2) * np.cos(z/2)
        qw = np.cos(x/2) * np.cos(y/2) * np.cos(z/2) + \
            np.sin(x/2) * np.sin(y/2) * np.sin(z/2)

        return (qx, qy, qz, qw)
