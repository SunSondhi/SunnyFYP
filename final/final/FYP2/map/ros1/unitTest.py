import unittest
from unittest.mock import MagicMock, patch
from nav_msgs.msg import OccupancyGrid
from  IceLow import MapDataI, MapDataServer  

class TestMapDataI(unittest.TestCase):
    def setUp(self):
        self.map_data_i = MapDataI()

    @patch('rospy.Subscriber')
    def test_init(self, mock_subscriber):
        self.assertIsNotNone(self.map_data_i.latest_ice_data)
        self.assertIsNotNone(self.map_data_i.map_data_ready)
        mock_subscriber.assert_called_once_with('/robot/map', OccupancyGrid, self.map_data_i.map_data_callback)

    def test_map_data_callback(self):
        occupancy_grid_mock = MagicMock()
        self.map_data_i.map_data_callback(occupancy_grid_mock)
        self.assertEqual(self.map_data_i.latest_ice_data, occupancy_grid_mock)

    def test_getLatestMapData(self):
        dummy_data = MagicMock()
        self.map_data_i.latest_ice_data = dummy_data
        latest_data = self.map_data_i.getLatestMapData()
        self.assertEqual(latest_data, dummy_data)

class TestMapDataServer(unittest.TestCase):
    def setUp(self):
        self.map_data_server = MapDataServer()

    @patch('Ice.Application.communicator')
    def test_run(self, mock_communicator):
        mock_adapter = MagicMock()
        mock_ice_object = MagicMock()
        mock_communicator.return_value.createObjectAdapterWithEndpoints.return_value = mock_adapter
        mock_adapter.add.return_value = None

        self.map_data_server.run([])

        # Assertions
        mock_communicator.return_value.createObjectAdapterWithEndpoints.assert_called_once_with("MapDataAdapter", "default -p 10030")
        mock_adapter.add.assert_called_once_with(self.map_data_server.map_data_impl, self.map_data_server.communicator().stringToIdentity("MapData"))
        mock_adapter.activate.assert_called_once()
        self.map_data_server.communicator().waitForShutdown.assert_called_once()

if __name__ == '__main__':
    unittest.main()
