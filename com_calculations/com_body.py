import numpy as np
import PyKDL as kdl
import sys
import rospy
import json
import os
import csv
from progress.bar import IncrementalBar as Bar
from parse_simu_data import ParseCSV

from sensor_msgs.msg import JointState
from urdf_parser_py.urdf import Robot

#joint_states_fw_10m.csv
#joint_states_bw_10m.csv
#joint_states_square_4m

#foot_contacts_fw_10m.csv
#foot_contacts_bw_10m.csv

jointsFileName = 'inputData/joint_states_bw_10m.csv'
footContactFileName = 'inputData/foot_contacts_bw_10m.csv'
outputFileName = 'data.json'




#Replace with your global path
upperCwd = os.path.dirname(os.getcwd())
kdlCwd = upperCwd + "/hrl_kdl/pykdl_utils/src/pykdl_utils/"
sys.path.append(kdlCwd)
from kdl_kinematics import KDLKinematics

class CenterMassBody():


    def calculateCenterOfMass(self, robot, q):

        state = {}

        base_link = robot.get_root()

        #print "// q =", q # q = [FL, FR, RL, RR]

        totalMass = 0
        xCom = 0
        yCom = 0
        zCom = 0

        #end_link = robot.link_map.keys()[int(end_link_index)]
        for end_link in robot.link_map.keys():

            #Selecting the proper subset of angles qT from q        
            if (end_link == "FL_thigh_shoulder"):
                qT = [q[0][0]]
            elif (end_link == "FL_hip"):
                qT = [q[0][0]]
            elif (end_link == "FL_thigh"):
                qT = [q[0][0], q[0][1]]
            elif (end_link == "FL_calf"):
                qT = [q[0][0], q[0][1], q[0][2]]
            elif (end_link == "FL_foot"):
                qT = [q[0][0], q[0][1], q[0][2]]

            elif (end_link == "FR_thigh_shoulder"):
                qT = [q[1][0]]
            elif (end_link == "FR_hip"):
                qT = [q[1][0]]
            elif (end_link == "FR_thigh"):
                qT = [q[1][0], q[1][1]]
            elif (end_link == "FR_calf"):
                qT = [q[1][0], q[1][1], q[1][2]]
            elif (end_link == "FR_foot"):
                qT = [q[1][0], q[1][1], q[1][2]]

            elif (end_link == "RL_thigh_shoulder"):
                qT = [q[2][0]]
            elif (end_link == "RL_hip"):
                qT = [q[2][0]]
            elif (end_link == "RL_thigh"):
                qT = [q[2][0], q[2][1]]
            elif (end_link == "RL_calf"):
                qT = [q[2][0], q[2][1], q[2][2]]
            elif (end_link == "RL_foot"):
                qT = [q[2][0], q[2][1], q[2][2]]
            
            elif (end_link == "RR_thigh_shoulder"):
                qT = [q[3][0]]
            elif (end_link == "RR_hip"):
                qT = [q[3][0]]
            elif (end_link == "RR_thigh"):
                qT = [q[3][0], q[3][1]]
            elif (end_link == "RR_calf"):
                qT = [q[3][0], q[3][1], q[3][2]]
            elif (end_link == "RR_foot"):
                qT = [q[3][0], q[3][1], q[3][2]]

            elif (end_link == "imu_link"):
                qT = []
            elif (end_link == "base"):
                qT = []
            elif (end_link == "trunk"):
                qT = []

            #Calculating xyz of the link
            kdl_kin = KDLKinematics(robot, base_link, end_link)
            pose = kdl_kin.forward(qT)

            #print "float[]", end_link, "= {", pose.item((0, 3)), ",", pose.item((1, 3)), ",", pose.item((2, 3)),"};" #left as example
            state[end_link] = [pose.item((0, 3)), pose.item((1, 3)), pose.item((2, 3))]

            #Calculating xyz of the link's COM
            link_com = self.getLinkInertialInfo(robot, end_link)[0]
            link_mass = self.getLinkInertialInfo(robot, end_link)[1]
            offset_m = np.mat([[link_com[0]], [link_com[1]], [link_com[2]], [1]])
            pose = pose * offset_m

            #Averaging the COMs
            xCom = xCom + pose.item((0,0)) * link_mass
            yCom = yCom + pose.item((1,0)) * link_mass
            zCom = zCom + pose.item((2,0)) * link_mass
            totalMass = totalMass + link_mass

            state[end_link+"_com"] = [pose.item((0, 0)), pose.item((1, 0)), pose.item((2, 0))]

        #Computing xyz of the total COM
        xCom = xCom / totalMass
        yCom = yCom / totalMass
        zCom = zCom / totalMass

        state["com"] = [xCom, yCom, zCom]

        return state


    def getLinkInertialInfo(self, robot, end_link):

        if (end_link == "RR_thigh"):
            link_com = (-0.003237, 0.022327, -0.027326)
            link_mass = 1.013

        elif (end_link == "FL_thigh"):
            link_com = (-0.003237, -0.022327, -0.027326)
            link_mass = 1.013

        elif (end_link == "FR_thigh"):
            link_com = (-0.003237, 0.022327, -0.027326)
            link_mass = 1.013

        elif (end_link == "RL_thigh"):
            link_com = (-0.003237, -0.022327, -0.027326)
            link_mass = 1.013

        elif (end_link == "RR_hip"):
            link_com = (-0.003311, 0.000635, 3.1e-05)
            link_mass = 0.696

        elif (end_link == "FR_hip"):
            link_com = (-0.003311, 0.000635, 3.1e-05)
            link_mass = 0.696

        elif (end_link == "FL_hip"):
            link_com = (-0.003311, 0.000635, 3.1e-05)
            link_mass = 0.696

        elif (end_link == "RL_hip"):
            link_com = (-0.003311, 0.000635, 3.1e-05)
            link_mass = 0.696

        elif (end_link == "FL_foot"):
            link_com = (0, 0, 0)
            link_mass = 0.06

        elif (end_link == "RL_foot"):
            link_com = (0, 0, 0)
            link_mass = 0.06

        elif (end_link == "FR_foot"):
            link_com = (0, 0, 0)
            link_mass = 0.06

        elif (end_link == "RR_foot"):
            link_com = (0, 0, 0)
            link_mass = 0.06

        elif (end_link == "FR_calf"):
            link_com = (0.006435, 0.0, -0.107388)
            link_mass = 0.166

        elif (end_link == "RL_calf"):
            link_com = (0.006435, 0.0, -0.107388)
            link_mass = 0.166

        elif (end_link == "FL_calf"):
            link_com = (0.006435, 0.0, -0.107388)
            link_mass = 0.166

        elif (end_link == "RR_calf"):
            link_com = (0.006435, 0.0, -0.107388)
            link_mass = 0.166

        elif (end_link == "FR_thigh_shoulder"):
            link_com = (0, 0, 0)
            link_mass = 0

        elif (end_link == "RR_thigh_shoulder"): 
            link_com = (0, 0, 0)
            link_mass = 0

        elif (end_link == "FL_thigh_shoulder"):
            link_com = (0, 0, 0)
            link_mass = 0 

        elif (end_link == "RL_thigh_shoulder"):
            link_com = (0, 0, 0)
            link_mass = 0

        elif (end_link == "imu_link"):
            link_com = (0, 0, 0)
            link_mass = 0.001

        elif (end_link == "base"):
            link_com = (0, 0, 0)
            link_mass = 0

        elif (end_link == "trunk"):
            link_com = (0.012731, 0.002186, 0.000515)
            link_mass = 4.713

        else:
            link_com = (0, 0, 0)
            link_mass = 0

        return (link_com, link_mass)

def generateVisualizationData(robot, jointsFileNameData, footContactFileNameData):
    com = CenterMassBody()

    jointsData = ParseCSV(jointsFileNameData)
    fcData = ParseCSV(footContactFileNameData)

    print("Generating Visualization Data...  \n") 

    print("Loading " + jointsFileName)
    print("Loading " + footContactFileName + "\n")

    timeline = []
    dataPoints = int(jointsData.get_data_size() * 0.12)

    print dataPoints, "data points detected \n"

    bar = Bar('Computing Forward Kinematics', max=dataPoints, suffix='%(percent).1f%% - %(index)d/%(max)d - %(eta)ds')

    fcIndex = 0 #foot contact index

    for i in range(dataPoints):

        #Bringing foot contact index up to speed time-wise with joints data index 
        while (fcData.get_time_stamp(fcIndex) < jointsData.get_time_stamp(i) and fcIndex < fcData.get_data_size() - 1):
            fcIndex = fcIndex + 1

        timeline.append(com.calculateCenterOfMass(robot, jointsData.get_joints_angle(i)))

        fc = fcData.get_foot_contact(fcIndex)

        timeline[len(timeline) - 1]["FL_fc"] = fc[0]
        timeline[len(timeline) - 1]["FR_fc"] = fc[1]
        timeline[len(timeline) - 1]["RL_fc"] = fc[2]
        timeline[len(timeline) - 1]["RR_fc"] = fc[3]

        bar.next()
    bar.finish()
            

    with open(outputFileName, 'w') as outfile:
        json.dump(timeline, outfile)

    print("\n")
    print "JSON file generated successfully:"
    print " >", outputFileName, str(round(os.path.getsize(outputFileName)/1000000.0, 2)), "MB"
    print("\n")


def generateTrackingVectors(robot, jointsFileNameData, footContactFileNameData):
    com = CenterMassBody()

    jointsData = ParseCSV(jointsFileNameData)
    fcData = ParseCSV(footContactFileNameData)

    print("Generating Tracking Vectors...  \n") 

    print("Loading " + jointsFileName)
    print("Loading " + footContactFileName + "\n")

    timeline = []
    dataPoints = int(jointsData.get_data_size() * 0.12)

    print dataPoints, "data points detected \n"

    bar = Bar('Computing Leg Odometry Vectors', max=dataPoints, suffix='%(percent).1f%% - %(index)d/%(max)d - %(eta)ds')

    fcIndex = 0 #foot contact index

    for i in range(dataPoints):

        #Bringing foot contact index up to speed time-wise with joints data index 
        while (fcData.get_time_stamp(fcIndex) < jointsData.get_time_stamp(i) and fcIndex < fcData.get_data_size() - 1):
            fcIndex = fcIndex + 1

        timeline.append(com.calculateCenterOfMass(robot, jointsData.get_joints_angle(i)))

        fc = fcData.get_foot_contact(fcIndex)

        timeline[len(timeline) - 1]["FL_fc"] = fc[0]
        timeline[len(timeline) - 1]["FR_fc"] = fc[1]
        timeline[len(timeline) - 1]["RL_fc"] = fc[2]
        timeline[len(timeline) - 1]["RR_fc"] = fc[3]

        bar.next()
    bar.finish()
            

    with open(outputFileName, 'w') as outfile:
        json.dump(timeline, outfile)

    print("\n")
    print "JSON file generated successfully:"
    print " >", outputFileName, str(round(os.path.getsize(outputFileName)/1000000.0, 2)), "MB"
    print("\n")


def main():
    import sys
    def usage():
        print("Tests for kdl_parser:\n")
        print("kdl_parser <urdf file>")
        print("\tLoad the URDF from file.")
        print("kdl_parser")
        print("\tLoad the URDF from the parameter server.")
        sys.exit(1)
    # if len(sys.argv) > 2:
    #     usage()
    # if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    #     usage()
    # if (len(sys.argv) == 1):
    #     robot = Robot.from_parameter_server()
    # else:
    #     f = file(sys.argv[1], 'r')
    #     robot = Robot.from_xml_string(f.read())
    #     f.close()

    if len(sys.argv) > 4:
        usage()
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        usage()
    if (len(sys.argv) == 1):
        robot = Robot.from_parameter_server()
    else:
        f = file(sys.argv[1], 'r')
        robot = Robot.from_xml_string(f.read())
        f.close()
        end_link_index = sys.argv[2]
        angle = [int(sys.argv[3])]

    if True:
        base_link = robot.get_root()
        end_link = robot.link_map.keys()[int(end_link_index)]
        print "\n"
        print "\n"
        kdl_kin = KDLKinematics(robot, base_link, end_link)

        #--------------VVV-------------

        generateVisualizationData(robot, jointsFileName, footContactFileName)

        

        #--------------^^^-------------


if __name__ == "__main__":
    main()

# TODO: change name of com class as it acutally does both forward kinematics and COM calculations