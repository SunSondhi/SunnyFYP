import unittest
from unittest.mock import MagicMock
from IceServer import LaserDataI

class TestLaserDataI(unittest.TestCase):

    def setUp(self):
        self.laser_data = LaserDataI()

    def tearDown(self):
        pass

    def test_laser_data_callback(self):
        laser_scan_mock = MagicMock()
        laser_scan_mock.header.seq = 1
        laser_scan_mock.header.stamp.secs = 123456
        laser_scan_mock.header.stamp.nsecs = 789000000
        laser_scan_mock.header.frame_id = "laser_frame"
        laser_scan_mock.angle_min = -0.5
        laser_scan_mock.angle_max = 0.5
        laser_scan_mock.angle_increment = 0.1
        laser_scan_mock.time_increment = 0.01
        laser_scan_mock.scan_time = 0.1
        laser_scan_mock.range_min = 0.0
        laser_scan_mock.range_max = 10.0
        laser_scan_mock.ranges = [1.0, 2.0, 3.0]
        laser_scan_mock.intensities = [10.0, 20.0, 30.0]

        self.laser_data.laser_data_callback(laser_scan_mock)

        latest_data = self.laser_data.getLatestLaserData()
        self.assertEqual(latest_data.seq, 1)
        self.assertEqual(latest_data.sec, 123456)
        self.assertEqual(latest_data.nsec, 789000000)
        self.assertEqual(latest_data.frameId, "laser_frame")
        self.assertEqual(latest_data.angleMin, -0.5)
        self.assertEqual(latest_data.angleMax, 0.5)
        self.assertEqual(latest_data.angleIncrement, 0.1)
        self.assertEqual(latest_data.timeIncrement, 0.01)
        self.assertEqual(latest_data.scanTime, 0.1)
        self.assertEqual(latest_data.rangeMin, 0.0)
        self.assertEqual(latest_data.rangeMax, 10.0)
        self.assertEqual(latest_data.ranges, [1.0, 2.0, 3.0])
        self.assertEqual(latest_data.intensities, [10.0, 20.0, 30.0])

    def test_get_latest_laser_data(self):
        dummy_data = MagicMock()
        dummy_data.seq = 10
        dummy_data.sec = 123456
        dummy_data.nsec = 789000000
        dummy_data.frameId = "dummy_frame"
        dummy_data.angleMin = -1.0
        dummy_data.angleMax = 1.0
        dummy_data.angleIncrement = 0.2
        dummy_data.timeIncrement = 0.02
        dummy_data.scanTime = 0.2
        dummy_data.rangeMin = 0.1
        dummy_data.rangeMax = 20.0
        dummy_data.ranges = [0.1, 0.2, 0.3]
        dummy_data.intensities = [1.0, 2.0, 3.0]

        self.laser_data.latest_ice_data = dummy_data

        latest_data = self.laser_data.getLatestLaserData()

        self.assertEqual(latest_data.seq, 10)
        self.assertEqual(latest_data.sec, 123456)
        self.assertEqual(latest_data.nsec, 789000000)
        self.assertEqual(latest_data.frameId, "dummy_frame")
        self.assertEqual(latest_data.angleMin, -1.0)
        self.assertEqual(latest_data.angleMax, 1.0)
        self.assertEqual(latest_data.angleIncrement, 0.2)
        self.assertEqual(latest_data.timeIncrement, 0.02)
        self.assertEqual(latest_data.scanTime, 0.2)
        self.assertEqual(latest_data.rangeMin, 0.1)
        self.assertEqual(latest_data.rangeMax, 20.0)
        self.assertEqual(latest_data.ranges, [0.1, 0.2, 0.3])
        self.assertEqual(latest_data.intensities, [1.0, 2.0, 3.0])

if __name__ == '__main__':
    unittest.main()
