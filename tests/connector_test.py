import numpy as np
import unittest
from ca_traffic.connector import  Connector
from ca_traffic.abstract_lane import AbstractLane


class MockLane(AbstractLane):
    def __init__(self, lane_length=10):
        self.cells = np.zeros(lane_length).astype(int)
        self.cells = self.cells - 1

    def get_first_cells(self, n):
        return self.cells[0:n]

    def insert_cell(self, index, value):
        self.cells[index] = value


class ConnectorTestCase(unittest.TestCase):
    def test_get_next_cells(self):
        lane = MockLane()
        lane.cells[0] = 1
        lane.cells[1] = 2
        lane.cells[2] = 3
        c = Connector(end_lane=lane)
        next_cells = c.next_cells(n=3)
        np.testing.assert_equal(next_cells, lane.cells[0:3])

    def test_insert_cell(self):
        lane = MockLane()
        c = Connector(end_lane=lane)
        c.insert_cell(index=0, value=5)
        self.assertEqual(lane.cells[0], 5)


if __name__ == '__main__':
    unittest.main()
