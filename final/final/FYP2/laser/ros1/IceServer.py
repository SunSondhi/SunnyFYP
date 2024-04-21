#!/usr/bin/env python

import threading
import rospy
from sensor_msgs.msg import LaserScan
import Ice
import sys


# Working#

Ice.loadSlice("LaserModule.ice")
import LaserModule

class LaserDataI(LaserModule.LaserData):

    def __init__(self):
        self.latest_ice_data = LaserModule.LaserScan()
        self.lock = threading.Lock()  # Lock for thread safety
        rospy.Subscriber('/robot/front_laser/scan', LaserScan, self.laser_data_callback)

    def laser_data_callback(self, data):
        # Convert ROS laser data to Ice format
        self.latest_ice_data.seq = data.header.seq
        self.latest_ice_data.sec = data.header.stamp.secs
        self.latest_ice_data.nsec = data.header.stamp.nsecs
        self.latest_ice_data.frameId = data.header.frame_id
        self.latest_ice_data.angleMin = data.angle_min
        self.latest_ice_data.angleMax = data.angle_max
        self.latest_ice_data.angleIncrement = data.angle_increment
        self.latest_ice_data.timeIncrement = data.time_increment
        self.latest_ice_data.scanTime = data.scan_time
        self.latest_ice_data.rangeMin = data.range_min
        self.latest_ice_data.rangeMax = data.range_max
        self.latest_ice_data.ranges = data.ranges
        self.latest_ice_data.intensities = data.intensities

        # Print the received laser data
        rospy.loginfo("Server Started")
        rospy.loginfo("Received laser data from ROS")

    def publishLaserData(self, data, current=None):
        # Not implemented for now
        pass

    def getLatestLaserData(self, current=None):
        # Lock to ensure thread safety while accessing the shared data
        with self.lock:
            return self.latest_ice_data

class LaserDataServer(Ice.Application):

    def run(self, args):
        with self.communicator() as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("LaserDataAdapter", "default -p 10030")
            laser_data_impl = LaserDataI()
            adapter.add(laser_data_impl, self.communicator().stringToIdentity("LaserData"))
            adapter.activate()
            communicator.waitForShutdown()

class LaserDataClient:
    def __init__(self, communicator):
        self.proxy = LaserModule.LaserDataPrx.checkedCast(
            communicator.stringToProxy("LaserData:default -p 10000")
        )

    def getLatestLaserData(self):
        return self.proxy.getLatestLaserData()

    def sendDataToLowLevel(self, data):
        self.proxy.receiveDataFromHighLevel(data)


def main():
    try:
        # Initialize the ROS node
        rospy.init_node('laser_data_server')

        # Start the Ice server
        server_app = LaserDataServer()
        server_app.main(sys.argv)

        # Ice communicator
        with Ice.initialize(sys.argv) as communicator:
            laser_data_client = LaserDataClient(communicator)

            laser_data_client.sendDataToLowLevel("example data from high-level")

            latest_laser_data = laser_data_client.getLatestLaserData()
            #rospy.loginfo("Received latest laser data from low-level system: %s", latest_laser_data)

        rospy.spin()  # Start the ROS event loop
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")

if __name__ == '__main__':
    main()
