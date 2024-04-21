#!/usr/bin/env python3

import Ice
import rclpy
from geometry_msgs.msg import Twist
import VelocityModule
import sys

Ice.loadSlice("VelocityModule.ice")

class VelDataClient(Ice.Application):
    def run(self, args):
        try:
            rclpy.init()

            node = rclpy.create_node('ice_to_ros_node')
            publisher = node.create_publisher(Twist, '/fromICE/velocity', 10)

            proxy = self.communicator().stringToProxy("VelData:default -p 10000")
            vel_data_prx = VelocityModule.VelDataPrx.checkedCast(proxy)

            if not vel_data_prx:
                raise RuntimeError("Invalid proxy")

            while True:
                try:
                    data = vel_data_prx.getLatestVelData()
                    if data:
                        try:
                            # Parse Ice data if it's a string
                            if isinstance(data, str):
                                linear_vel, angular_vel = map(float, data.split(","))

                                # Create Twist message
                                twist_msg = Twist()
                                twist_msg.linear.x = linear_vel
                                twist_msg.angular.z = angular_vel

                                publisher.publish(twist_msg)
                                #node.get_logger().info("Ice velocity data received and converted to ROS2 Twist message successfully.")
                        except Exception as e:
                            node.get_logger().error("Error converting Ice velocity data to ROS2 Twist message: %s", e)
                except Ice.CommunicatorDestroyedException:
                    break

            node.destroy_node()
            rclpy.shutdown()

            return 0

        except KeyboardInterrupt:
            if node:
                node.get_logger().info("KeyboardInterrupt detected. Shutting down...")
                node.destroy_node()
            rclpy.shutdown()
            return 0

if __name__ == "__main__":
    client = VelDataClient()
    sys.exit(client.main(sys.argv))
