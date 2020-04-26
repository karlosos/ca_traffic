"""
Lane model based on NagelSch

Check https://www.wikiwand.com/en/Nagel%E2%80%93Schreckenberg_model for more insights

Every car is represented as non-negative number. 0 - car is not moving, 1 - cars velocity is 1, and etc.
-1 is designated for empty space in lane
"""
import numpy as np
import random
from ca_traffic.abstract_lane import AbstractLane


class Lane(AbstractLane):
    def __init__(self, lane_length=80, max_velocity=5):
        super().__init__()
        self.max_velocity = max_velocity
        self.lane_length = lane_length
        self.cells = np.zeros(self.lane_length).astype(int)
        self.cells = self.cells - 1
        self.start_connector = None
        self.end_connector = None

    def simulation_step(self):
        # acceleration
        self.cells[self.cells >= 0] = self.cells[self.cells >= 0] + 1
        self.cells[self.cells > self.max_velocity] = self.max_velocity

        # slowing down
        for i in np.nonzero(self.cells >= 0)[0]:
            v = self.cells[i]
            collision, k = self.check_collision_next_cells(i, v)
            if collision:
                self.cells[i] = k - 1

        # randomization
        for i in np.nonzero(self.cells > 0)[0]:
            if random.random() < 0.3:
                self.cells[i] = self.cells[i] - 1

        # car motion
        for i in np.nonzero(self.cells > 0)[0]:
            v = self.cells[i]
            j = (i + v) % self.lane_length
            if j < self.lane_length:
                self.cells[j] = self.cells[i]
            else:
                self.insert_cell(j, self.cells[i])
            self.cells[i] = -1

    def get_first_cells(self, n):
        if n <= self.lane_length:
            return self.cells[0:n]
        else:
            if self.end_connector is not None:
                first_road = self.cells[0:n]
                remaining_length = n - self.lane_length
                second_road = self.end_connector.next_cells(remaining_length)
                return np.concatenate((first_road, second_road))
            else:
                return self.cells

    def check_collision_next_cells(self, start_index, length):
        i = start_index
        v = length
        for k in range(1, v + 1):
            if i + k < self.lane_length:
                if self.cells[(i + k) % self.lane_length] != -1:
                    return True, k
            else:
                if self.end_connector.next_cells(i + k - self.lane_length) != -1:
                    return True, k
        return False, None

    def insert_cell(self, index, value):
        if index < self.lane_length:
            self.cells[index] = value
        else:
            if self.end_connector is not None:
                self.end_connector.insert_cell(index - self.lane_length, value)
