#!/usr/bin/env python3


"""
SUNNY SONDHI (210097072)

ASTON UNIVERSITY

2024

!!WORKING!! POSE TOPIC CLIENT; 

"""

import Ice
import rclpy
from geometry_msgs.msg import PoseWithCovarianceStamped
import sys

# Load Ice slice definition
Ice.loadSlice("PoseModule.ice")
import PoseModule

class PoseDataClient(Ice.Application):
    def run(self, args):
        rclpy.init()

        node = rclpy.create_node('ice_to_ros_node')
        publisher = node.create_publisher(PoseWithCovarianceStamped, '/fromICE/pose', 10)

        proxy = self.communicator().stringToProxy("PoseData:default -p 10010")
        pose_data_prx = PoseModule.PoseDataPrx.checkedCast(proxy)

        if not pose_data_prx:
            raise RuntimeError("Invalid proxy")

        while True:
            try:
                data = pose_data_prx.getLatestPoseData()
                if data:
                    try:
                        # Parse Ice data
                        pose_data = data.split(',')
                        pose_msg = PoseWithCovarianceStamped()
                        pose_msg.header.stamp = node.get_clock().now().to_msg()
                        pose_msg.header.frame_id = "robot_map"
                        pose_msg.pose.pose.position.x = float(pose_data[0])
                        pose_msg.pose.pose.position.y = float(pose_data[1])
                        pose_msg.pose.pose.position.z = float(pose_data[2])
                        pose_msg.pose.pose.orientation.x = float(pose_data[3])
                        pose_msg.pose.pose.orientation.y = float(pose_data[4])
                        pose_msg.pose.pose.orientation.z = float(pose_data[5])
                        pose_msg.pose.pose.orientation.w = float(pose_data[6])
                        pose_msg.pose.covariance = list(map(float, pose_data[7:]))

                        # Publish the pose message
                        publisher.publish(pose_msg)
                        #node.get_logger().info("Pose data received and converted to ROS2 message successfully.")
                    except Exception as e:
                        node.get_logger().error("Error converting pose data to ROS2 message: %s", e)
            except Ice.CommunicatorDestroyedException:
                break

        node.destroy_node()
        rclpy.shutdown()

        return 0

if __name__ == "__main__":
    client = PoseDataClient()
    sys.exit(client.main(sys.argv))
