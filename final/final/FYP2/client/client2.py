import Ice
import Message
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


# Define a callback function to handle incoming messages from the /movement topic
def movement_callback(msg):
    # Convert ROS 2 Twist message to Ice TwistData message
    twist_data = Message.TwistData()
    twist_data.linearx = msg.linear.x
    twist_data.lineary = msg.linear.y
    twist_data.linearz = msg.linear.z
    twist_data.angularx = msg.angular.x
    twist_data.angulary = msg.angular.y
    twist_data.angularz = msg.angular.z

    if abs(twist_data.angularz) < 0.1:
        print(twist_data)


    # Send Ice message to the server
    with Ice.initialize(sys.argv) as communicator:
        #proxy = communicator.stringToProxy("sender:default -h 192.168.0.200 -p 10000") 
        proxy = communicator.stringToProxy("sender:default -p 10000")
        sender = Message.MessageSenderPrx.checkedCast(proxy)
        if not sender:
            raise RuntimeError("Invalid proxy")

        # Send the converted message
        sender.sendMessage(twist_data)

class MovementClient(Node):
    def __init__(self):
        super().__init__('movement_client')
        self.subscription = self.create_subscription(Twist, '/movement', movement_callback, 10)
        self.subscription  # prevent unused variable warning

def main(args=None):
    rclpy.init(args=args)
    movement_client = MovementClient()
    try:
        # Spin the ROS 2 node to receive messages
        movement_client.get_logger().info('Movement client node started...')
        rclpy.spin(movement_client)
    except KeyboardInterrupt:
        movement_client.get_logger().info('Movement client node stopped...')
    finally:
        movement_client.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
