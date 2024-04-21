import threading
import rospy
from geometry_msgs.msg import Twist
import Ice
import sys

Ice.loadSlice("VelocityModule.ice")
import VelocityModule

class VelDataI(VelocityModule.VelData):

    def __init__(self):
        self.latest_ice_data = ""
        self.lock = threading.Lock() 
        rospy.Subscriber('/robot/robotnik_base_control/cmd_vel', Twist, self.vel_data_callback)

    def vel_data_callback(self, data):
        
        linear_vel = data.linear.x
        angular_vel = data.angular.z
        ice_data = f"{linear_vel},{angular_vel}"

        
        with self.lock:
            self.latest_ice_data = ice_data

        
        #rospy.loginfo("Received velocity data: %s", ice_data)

    def getLatestVelData(self, current=None):
        
        with self.lock:
            return self.latest_ice_data

class VelDataServer(Ice.Application):

    def run(self, args):
        with self.communicator() as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("VelDataAdapter", "default -p 10000")
            vel_data_impl = VelDataI()
            adapter.add(vel_data_impl, self.communicator().stringToIdentity("VelData"))
            adapter.activate()
            communicator.waitForShutdown()

def main():
    try:
        
        rospy.init_node('vel_data_server')

       
        server_app = VelDataServer()
        server_app.main(sys.argv)

        rospy.spin()  
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")

if __name__ == '__main__':
    main()
