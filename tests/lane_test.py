import unittest
from ca_traffic.lane import Lane
import numpy as np


class LaneLinksTest(unittest.TestCase):
    def test_linking_roads(self):
        l1 = Lane(lane_length=5)
        l2 = Lane(lane_length=2)
        Lane.link_lanes(l1, l2)
        self.assertEqual(l1.end_connector, l2.start_connector)

    def test_next_cells_same_length(self):
        l1 = Lane(lane_length=5)
        l1.cells[0] = 5
        l1.cells[4] = 5
        next_cells = l1.get_first_cells(5)
        np.testing.assert_equal(next_cells, l1.cells)

    def test_next_cells_from_linked_road(self):
        l1 = Lane(lane_length=5)
        l1.cells[0] = 1
        l1.cells[1] = 2
        l1.cells[2] = 3
        l1.cells[3] = 4
        l1.cells[4] = 5
        l2 = Lane(lane_length=2)
        l2.cells[0] = 9
        l2.cells[1] = 9
        Lane.link_lanes(l1, l2)
        next_cells = l1.get_first_cells(7)
        next_cells = next_cells.tolist()
        expected_cells = [1, 2, 3, 4, 5, 9, 9]
        self.assertSequenceEqual(next_cells, expected_cells)

    def test_next_cells_when_no_linked_road_should_return_all_cells(self):
        l1 = Lane(lane_length=3)
        next_cells = l1.get_first_cells(5)
        np.testing.assert_equal(next_cells, l1.cells)

    def test_insert_cell_into_greater_index_than_length_should_insert_into_next_lane(self):
        l1 = Lane(lane_length=3)
        l2 = Lane(lane_length=3)
        Lane.link_lanes(l1, l2)
        l1.insert_cell(3, 9)
        self.assertEqual(l2.cells[0], 9)

        l1.insert_cell(4, 6)
        self.assertEqual(l2.cells[1], 6)

        l1.insert_cell(5, 3)
        self.assertEqual(l2.cells[2], 3)

    def test_insert_cell(self):
        l1 = Lane(lane_length=3)
        l1.insert_cell(1, 2)
        self.assertEqual(l1.cells[1], 2)

    def test_insert_cell_greater_index_than_length_no_end_connector(self):
        l1 = Lane(lane_length=3)
        l1.insert_cell(5, 2)
        self.assertEqual(l1.cells.tolist(), [-1, -1, -1])


class LaneLinksTest(unittest.TestCase):
    def test_simulation_loop(self):
        l1 = Lane(lane_length=3)
        Lane.link_lanes(l1, l1)
        l1.cells[1] = 0
        l1.simulation_step()
        self.assertEqual(l1.cells.tolist(), [-1, -1, 1])

    def test_simulation_two_lanes(self):
        l1 = Lane(lane_length=3)
        l2 = Lane(lane_length=2)
        Lane.link_lanes(l1, l2)
        Lane.link_lanes(l2, l1)
        l1.cells[2] = 0

        print(l1.cells)
        print(l2.cells)
        l1.simulation_step()
        l2.simulation_step()
        print(l1.cells)
        print(l2.cells)

if __name__ == '__main__':
    unittest.main()
