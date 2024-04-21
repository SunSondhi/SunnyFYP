#!/usr/bin/env python3

"""
SUNNY SONDHI (210097072)

ASTON UNIVERSITY

2024

!!WOKRING, this is the client or more like the high entity asking for the map data from the server- low level

!!!DO NOT MODIFY UNLESS YOU KNOW WHAT YOU DOING!!!


"""


import Ice
import rclpy
from nav_msgs.msg import OccupancyGrid
import sys
Ice.MessageSizeMax=2000000

Ice.loadSlice("MapModule.ice")
import MapModule

class MapDataClient(Ice.Application):
    def __init__(self):
        self.map_data = []
        self.map_data_received = False

    def run(self, args):
       
        self.communicator = Ice.initialize(['--Ice.Config=ice.config'])

        rclpy.init()
        node = rclpy.create_node('icetoros2map')
        publisher = node.create_publisher(OccupancyGrid, '/robot/map', 10)

        proxy = self.communicator.stringToProxy("MapData:default -p 10004")  ##local
        #proxy = self.communicator.stringToProxy("MapData:default -h 192.168.0.200 -p 10003")  ##robot

        map_data_prx = MapModule.MapDataPrx.checkedCast(proxy)

        if not map_data_prx:
            raise RuntimeError("Invalid proxy")

        try:
            while rclpy.ok():
                ice_data = map_data_prx.getLatestMapData()

                if ice_data:
                    ros2_data = OccupancyGrid()
                    ros2_data.header.stamp.sec = ice_data.timestamp.secs
                    ros2_data.header.stamp.nanosec = ice_data.timestamp.nsecs
                    ros2_data.header.frame_id = ice_data.header.frameid
                    ros2_data.info.map_load_time.sec = ice_data.metadata.maploadtime.secs
                    ros2_data.info.map_load_time.nanosec = ice_data.metadata.maploadtime.nsecs
                    ros2_data.info.resolution = ice_data.metadata.resolution
                    ros2_data.info.width = ice_data.metadata.width
                    ros2_data.info.height = ice_data.metadata.height
                    ros2_data.info.origin.position.x = ice_data.metadata.origin.positionx
                    ros2_data.info.origin.position.y = ice_data.metadata.origin.positiony
                    ros2_data.info.origin.position.z = ice_data.metadata.origin.positionz
                    ros2_data.info.origin.orientation.x = ice_data.metadata.origin.orientationx
                    ros2_data.info.origin.orientation.y = ice_data.metadata.origin.orientationy
                    ros2_data.info.origin.orientation.z = ice_data.metadata.origin.orientationz
                    ros2_data.info.origin.orientation.w = ice_data.metadata.origin.orientationw
                    #ros2_data.data = ice_data.data
                    #deserialise for each on of them: 
                    ros2_data.data = [int(value) for value in ice_data.griddata.data]
                    
                   
                    publisher.publish(ros2_data)
                    #node.get_logger().info("Received and published map message")

        except KeyboardInterrupt:
            node.get_logger().info("KeyboardInterrupt detected. Shutting down...")

        node.destroy_node()
        rclpy.shutdown()

        return 0

if __name__ == "__main__":
    client = MapDataClient()
    sys.exit(client.main(sys.argv))
