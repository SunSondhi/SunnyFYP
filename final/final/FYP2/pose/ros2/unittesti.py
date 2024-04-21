import unittest
from unittest.mock import MagicMock
from sensor_msgs.msg import LaserScan
from IceClient import LaserDataClient

class TestLaserDataClient(unittest.TestCase):

    def test_conversion(self):
        
        proxy = MagicMock()
        proxy.getLatestLaserData.return_value = self.create_mock_ice_data()

        
        node = MagicMock()
        publisher = MagicMock()
        node.create_publisher.return_value = publisher

       
        client = LaserDataClient()
        client.communicator = MagicMock()
        client.communicator.stringToProxy.return_value = proxy

        
        client.run([])

        
        publisher.publish.assert_called_once_with(self.create_expected_ros2_message())

    def create_mock_ice_data(self):
        
        data = MagicMock()
        data.sec = 123
        data.nsec = 456
       
        return data

    def create_expected_ros2_message(self):
        
        scan_msg = LaserScan()
        scan_msg.header.stamp.sec = 123
        scan_msg.header.stamp.nanosec = 456
        
        return scan_msg

if __name__ == '__main__':
    unittest.main()
