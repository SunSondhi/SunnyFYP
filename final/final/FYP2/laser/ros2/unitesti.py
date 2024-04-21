import unittest
from unittest.mock import MagicMock
from sensor_msgs.msg import LaserScan
from IceClient import LaserDataClient
import LaserModule

class TestLaserDataClient(unittest.TestCase):

    def setUp(self):
        self.mock_ice_data = self.create_mock_ice_data()
        self.expected_ros2_message = self.create_expected_ros2_message()

    def test_conversion(self):
        client = LaserDataClient()

        mock_communicator = MagicMock()
        client.communicator = MagicMock(return_value=mock_communicator)

        mock_proxy = MagicMock()
        mock_communicator.stringToProxy = MagicMock(return_value=mock_proxy)

        mock_LaserDataPrx = MagicMock()
        LaserModule.LaserDataPrx.checkedCast = MagicMock(return_value=mock_LaserDataPrx)



        client.getLatestLaserData = MagicMock(return_value=self.mock_ice_data)

        node = MagicMock()
        publisher = MagicMock()
        node.create_publisher.return_value = publisher

        client.node = node

        client.run([])

        publisher.publish.assert_called_once_with(self.expected_ros2_message)

    def create_mock_ice_data(self):
        data = MagicMock()
        data.sec = 12
        data.nsec = 456
        data.frame_id = "laser_frame"
        data.angle_min = -0.5
        data.angle_max = 0.5
        data.angle_increment = 0.1
        data.time_increment = 0.01
        data.scan_time = 0.1
        data.range_min = 0.0
        data.range_max = 10.0
        data.ranges = [1.0, 2.0, 3.0]
        data.intensities = [10.0, 20.0, 30.0]
        return data

    def create_expected_ros2_message(self):
        scan_msg = LaserScan()
        scan_msg.header.stamp.sec = 12
        scan_msg.header.stamp.nanosec = 456
        scan_msg.header.frame_id = "laser_frame"
        scan_msg.angle_min = -0.5
        scan_msg.angle_max = 0.5
        scan_msg.angle_increment = 0.1
        scan_msg.time_increment = 0.01
        scan_msg.scan_time = 0.1
        scan_msg.range_min = 0.0
        scan_msg.range_max = 10.0
        scan_msg.ranges = [1.0, 2.0, 3.0]
        scan_msg.intensities = [10.0, 20.0, 30.0]
        return scan_msg

if __name__ == '__main__':
    unittest.main()
