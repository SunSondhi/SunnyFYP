import Ice
import Message
import sys
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Header

# Implement the MovementSender interface
class MovementSenderI(Message.MessageSender):
    def __init__(self):
        rospy.init_node('ice_to_ros1_publisher', anonymous=True)
        self.publisher = rospy.Publisher('/robot/robotnik_base_control/cmd_vel', Twist, queue_size=10)

    def sendMessage(self, data, current=None):
        # Convert Ice TwistData to ROS 1 Twist message
        twist_msg = Twist()
        twist_msg.linear.x = data.linearx
        twist_msg.linear.y = data.lineary
        twist_msg.linear.z = data.linearz
        twist_msg.angular.x = data.angularx
        twist_msg.angular.y = data.angulary
        twist_msg.angular.z = data.angularz

        # Publish the converted message
        self.publisher.publish(twist_msg)

class Server(Ice.Application):
    def run(self, argv):
        with self.communicator() as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("MovementAdapter", "default -p 10000")
            sender = MovementSenderI()
            adapter.add(sender, communicator.stringToIdentity("sender"))
            adapter.activate()
            print("Server started...")
            communicator.waitForShutdown()
        return 0

if __name__ == "__main__":
    app = Server()
    sys.exit(app.main(sys.argv))
