import unittest
from unittest.mock import MagicMock, patch
from geometry_msgs.msg import PoseWithCovarianceStamped
from IceServer import PoseDataI  
class TestPoseDataI(unittest.TestCase):
    def setUp(self):
        self.pose_data_i = PoseDataI()

    @patch('rospy.Subscriber')
    def test_pose_data_callback(self, mock_subscriber):
        
        pose_msg = PoseWithCovarianceStamped()
        pose_msg.pose.pose.position.x = 1.0
        pose_msg.pose.pose.position.y = 2.0
        pose_msg.pose.pose.position.z = 3.0
        pose_msg.pose.pose.orientation.x = 0.1
        pose_msg.pose.pose.orientation.y = 0.2
        pose_msg.pose.pose.orientation.z = 0.3
        pose_msg.pose.pose.orientation.w = 0.4
        pose_msg.pose.covariance = "0.1, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.1, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.1, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.1, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.1, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.1"
        
        
        self.pose_data_i.pose_data_callback(pose_msg)

        
        expected_ice_data = "0.1, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.1, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.1, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.1, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.1, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.1"

        self.assertEqual(self.pose_data_i.latest_ice_data, expected_ice_data)

    def test_getLatestPoseData(self):
        
        dummy_data = "0.1, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.1, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.1, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.1, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.1, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.1"
        self.pose_data_i.latest_ice_data = dummy_data

       
        latest_data = self.pose_data_i.getLatestPoseData()

        
        self.assertEqual(latest_data, dummy_data)

if __name__ == '__main__':
    unittest.main()
