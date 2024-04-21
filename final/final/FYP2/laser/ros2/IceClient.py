import Ice
import rclpy
from sensor_msgs.msg import LaserScan
import LaserModule
import sys


#working#

class LaserDataClient(Ice.Application):
    def run(self, args):
        rclpy.init()

        node = rclpy.create_node('ice_to_ros_node')
        publisher = node.create_publisher(LaserScan, '/fromICE/Laser/data', 10)

        proxy = self.communicator().stringToProxy("LaserData:default -p 10030")
        laser_data_prx = LaserModule.LaserDataPrx.checkedCast(proxy)

        if not laser_data_prx:
            raise RuntimeError("Invalid proxy")

        while True:
            try:
                data = laser_data_prx.getLatestLaserData()
                if data:
                    try:
                        # Parse Ice data if it's a string
                        if isinstance(data, str):
                            data = [float(val) for val in data.split(",")]

                        # Convert Ice data to ROS2 message
                        
                        #scan_msg.header.stamp = node.get_clock().now().to_msg()
                        
                        scan_msg = LaserScan()
                        scan_msg.header.stamp.sec = data.sec
                        scan_msg.header.stamp.nanosec = data.nsec
                        scan_msg.header.frame_id = "robot_map"
                        scan_msg.angle_min = data.angleMin
                        scan_msg.angle_max = data.angleMax
                        scan_msg.angle_increment = data.angleIncrement
                        scan_msg.time_increment = data.timeIncrement
                        scan_msg.scan_time = data.scanTime
                        scan_msg.range_min = data.rangeMin
                        scan_msg.range_max = data.rangeMax
                        scan_msg.intensities = data.intensities
                        scan_msg.ranges = data.ranges

                        publisher.publish(scan_msg)
                        #node.get_logger().info("Ice data received and converted to ROS2 message successfully.")
                    except Exception as e:
                        node.get_logger().error("Error converting Ice data to ROS2 message: %s", e)
            except Ice.CommunicatorDestroyedException:
                break

        node.destroy_node()
        rclpy.shutdown()

        return 0

if __name__ == "__main__":
    client = LaserDataClient()
    sys.exit(client.main(sys.argv))
