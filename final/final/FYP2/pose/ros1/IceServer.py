#!/usr/bin/env python3

"""
SUNNY SONDHI (210097072)

ASTON UNIVERSITY

2024

!!WORKING, pose server class working with ROS1, to be stored in the robot, 
this file will subscribe to the pose amcl_pose for the position of the robot on the map

!!!DO NOT MODIFY UNLESS YOU KNOW WHAT YOU DOING!!!

"""




import threading
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
import Ice
import sys

Ice.loadSlice("PoseModule.ice")  
import PoseModule

class PoseDataI(PoseModule.PoseData):

    def __init__(self):
        self.latest_ice_data = ""
        self.lock = threading.Lock() 
        rospy.Subscriber('/robot/amcl_pose', PoseWithCovarianceStamped, self.pose_data_callback)

    def pose_data_callback(self, msg):
        
        ice_data = f"{msg.pose.pose.position.x},{msg.pose.pose.position.y},{msg.pose.pose.position.z}," \
                   f"{msg.pose.pose.orientation.x},{msg.pose.pose.orientation.y}," \
                   f"{msg.pose.pose.orientation.z},{msg.pose.pose.orientation.w}," \
                   f"{','.join(map(str, msg.pose.covariance))}"

        with self.lock:
            self.latest_ice_data = ice_data

        #rospy.loginfo("Received pose data: %s", ice_data)

    def publishPoseData(self, data, current=None):
        # Not implemented for now
        pass

    def getLatestPoseData(self, current=None):
        with self.lock:
            return self.latest_ice_data

class PoseDataServer(Ice.Application):

    def run(self, args):
        with self.communicator() as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("PoseDataAdapter", "default -p 10010")
            pose_data_impl = PoseDataI()
            adapter.add(pose_data_impl, communicator.stringToIdentity("PoseData"))
            adapter.activate()
            communicator.waitForShutdown()

def main():
    try:
        
        rospy.init_node('pose_data_server')

        
        server_app = PoseDataServer()
        server_app.main(sys.argv)

        rospy.spin()  
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")

if __name__ == '__main__':
    main()
