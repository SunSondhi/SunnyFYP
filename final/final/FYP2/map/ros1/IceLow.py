
"""
SUNNY SONDHI (210097072)

ASTON UNIVERSITY

2024

!!WOKRING, this is the server or more like the low entity sending data map

!!!DO NOT MODIFY UNLESS YOU KNOW WHAT YOU DOING!!!


"""

import Ice
import rospy
import threading
from nav_msgs.msg import OccupancyGrid
import sys

Ice.loadSlice("MapModule.ice")
import MapModule
Ice.MessageSizeMax=2000000


class MapDataI(MapModule.MapData):

    def __init__(self):
        self.latest_ice_data = None
        self.map_data_ready = threading.Event()
        rospy.Subscriber('/robot/map', OccupancyGrid, self.map_data_callback)



    def map_data_callback(self, msg):
        iced_data = MapModule.MapInfo()
        iced_data.header.seq = msg.header.seq
        iced_data.header.stamp.secs = msg.header.stamp.secs
        iced_data.header.stamp.nsecs = msg.header.stamp.nsecs
        iced_data.header.frameid = msg.header.frame_id
        iced_data.metadata.maploadtime.secs = msg.info.map_load_time.secs
        iced_data.metadata.maploadtime.nsecs = msg.info.map_load_time.nsecs
        iced_data.metadata.resolution = msg.info.resolution
        iced_data.metadata.width = msg.info.width
        iced_data.metadata.height = msg.info.height
        iced_data.metadata.origin.positionx = msg.info.origin.position.x
        iced_data.metadata.origin.positiony = msg.info.origin.position.y
        iced_data.metadata.origin.positionz = msg.info.origin.position.z
        iced_data.metadata.origin.orientationx = msg.info.origin.orientation.x
        iced_data.metadata.origin.orientationy = msg.info.origin.orientation.y
        iced_data.metadata.origin.orientationz = msg.info.origin.orientation.z
        iced_data.metadata.origin.orientationw = msg.info.origin.orientation.w
        grid_data = []
        for val in msg.data:
            grid_data.append(int(val))

        iced_data.griddata.data = grid_data  

        self.latest_ice_data = iced_data
        self.map_data_ready.set()


    def getLatestMapData(self, current=None):
        self.map_data_ready.wait()
        #print(self.latest_ice_data)
        return self.latest_ice_data

class MapDataServer(Ice.Application):
    def run(self, args):
        with self.communicator() as communicator:
            communicator = Ice.initialize(['--Ice.Config=ice.config'])
            adapter = communicator.createObjectAdapterWithEndpoints("MapDataAdapter", "default -p 10004")
            map_data_impl = MapDataI()
            adapter.add(map_data_impl, communicator.stringToIdentity("MapData"))
            adapter.activate()
            
            communicator.waitForShutdown()
            
        #rospy.spin()  

def main():
    try:
        rospy.init_node('map_data_server')
        server_app = MapDataServer()
        server_app.main(sys.argv)
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")

if __name__ == '__main__':
    main()
