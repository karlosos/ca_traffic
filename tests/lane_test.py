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
        l1.cells[0] = (5, False)
        l1.cells[4] = (5, False)
        next_cells = l1.get_first_cells(5)
        self.assertSequenceEqual(next_cells, l1.cells)

    def test_next_cells_from_linked_road(self):
        l1 = Lane(lane_length=5)
        l1.cells[0] = (1, False)
        l1.cells[1] = (2, False)
        l1.cells[2] = (3, False)
        l1.cells[3] = (4, False)
        l1.cells[4] = (5, False)
        l2 = Lane(lane_length=2)
        l2.cells[0] = (9, False)
        l2.cells[1] = (9, False)
        Lane.link_lanes(l1, l2)
        next_cells = l1.get_first_cells(7)
        next_cells = next_cells.tolist()
        expected_cells = [(1, False), (2, False), (3, False), (4, False), (5, False), (9, False), (9, False)]
        self.assertSequenceEqual(next_cells, expected_cells)

    def test_next_cells_when_no_linked_road_should_return_all_cells(self):
        l1 = Lane(lane_length=3)
        next_cells = l1.get_first_cells(5)
        self.assertSequenceEqual(next_cells, l1.cells)

    def test_insert_cell_into_greater_index_than_length_should_insert_into_next_lane(self):
        l1 = Lane(lane_length=3)
        l2 = Lane(lane_length=3)
        Lane.link_lanes(l1, l2)
        l1.insert_cell(3, (9, False))
        self.assertEqual(l2.cells[0], (9, False))

        l1.insert_cell(4, (6, False))
        self.assertEqual(l2.cells[1], (6, False))

        l1.insert_cell(5, (3, False))
        self.assertEqual(l2.cells[2], (3, False))

    def test_insert_cell(self):
        l1 = Lane(lane_length=3)
        l1.insert_cell(1, (2, False))
        self.assertEqual(l1.cells[1], (2, False))

    def test_insert_cell_greater_index_than_length_no_end_connector(self):
        l1 = Lane(lane_length=3)
        l1.insert_cell(5, (2, False))
        self.assertEqual(l1.cells, [None, None, None])


class LaneLinksTest(unittest.TestCase):
    def test_simulation_loop(self):
        l1 = Lane(lane_length=3, randomization=False)
        Lane.link_lanes(l1, l1)
        l1.cells[1] = (0, False)
        l1.simulation_step()
        self.assertEqual(l1.cells, [None, None, (1, True)])
        l1.clear_flags()
        l1.simulation_step()
        self.assertEqual(l1.cells, [None, (2, True), None])
        l1.simulation_step()

    def test_simulation_without_clearing_flags(self):
        l1 = Lane(lane_length=3, randomization=False)
        Lane.link_lanes(l1, l1)
        l1.cells[1] = (0, False)
        l1.simulation_step()
        self.assertEqual(l1.cells, [None, None, (1, True)])
        l1.simulation_step()
        l1.simulation_step()
        l1.simulation_step()
        self.assertEqual(l1.cells, [None, None, (1, True)])

    def test_simulation_loop_multiple_steps(self):
        l1 = Lane(lane_length=5, randomization=False)
        Lane.link_lanes(l1, l1)
        l1.cells[0] = (0, False)
        l1.simulation_step()
        l1.clear_flags()

        l1.simulation_step()
        l1.clear_flags()

        l1.simulation_step()
        l1.clear_flags()

        l1.simulation_step()
        l1.clear_flags()
        l1.simulation_step()

        l1.clear_flags()
        l1.simulation_step()

        l1.clear_flags()
        l1.simulation_step()

        l1.clear_flags()
        l1.simulation_step()

        l1.clear_flags()
        self.assertEqual(l1.cells, [None, (4, False), None, None, None])

    def test_simulation_two_lanes(self):
        l1 = Lane(lane_length=3, randomization=False)
        l2 = Lane(lane_length=2, randomization=False)
        Lane.link_lanes(l1, l2)
        Lane.link_lanes(l2, l1)
        l1.cells[2] = (0, False)

        l1.simulation_step()
        l2.simulation_step()
        self.assertEqual(l2.cells, [(1, True), None])

    def test_simulation_two_lanes_many_iterations(self):
        l1 = Lane(lane_length=1, randomization=True)
        l2 = Lane(lane_length=1, randomization=True)
        Lane.link_lanes(l1, l2)
        Lane.link_lanes(l2, l1)
        l1.cells[0] = (0, False)

        for i in range(100):
            l1.simulation_step()
            l2.simulation_step()
            l1.clear_flags()
            l2.clear_flags()

        found_not_none_cell = 0
        for cell in l1.cells:
            if cell is not None:
                found_not_none_cell += 1
        for cell in l2.cells:
            if cell is not None:
                found_not_none_cell += 1
        self.assertEqual(found_not_none_cell, 1)

if __name__ == '__main__':
    unittest.main()
