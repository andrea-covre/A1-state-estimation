class DataInfo:

    '''
    when parsing data from file
    - each row is a data point
    - store information about timestamp for delta t
    '''

    def __init__(self):
        self.timestamp = 0 # seconds
        self.lin_accel = [] #3 x 1
        self.ang_vel = [] # 3 x 1
        self.joint_angles = [] # 4 x 3 
        self.feet_contact = [] # 4 x 1

    def getTimestamp(self):
        return self.timestamp

    def getLinearAccel(self):
        return self.lin_accel

    def getAngVel(self):
        return self.ang_vel

    def getJointAngles(self):
        return self.joint_angles
    
    def getFeetContactData(self):
        return self.feet_contact