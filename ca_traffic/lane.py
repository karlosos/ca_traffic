"""
Lane model based on NagelSch

Check https://www.wikiwand.com/en/Nagel%E2%80%93Schreckenberg_model for more insights

Every car is represented as tuple.
First element is velocity, second is flag if cell was simulated
"""
import random
from ca_traffic.abstract_lane import AbstractLane
from ca_traffic.gui.lane_render import LaneRender


class Lane(AbstractLane):
    def __init__(self, lane_length=80, max_velocity=5, randomization=True):
        super().__init__()
        self.max_velocity = max_velocity
        self.lane_length = lane_length
        self.cells = [None for _ in range(self.lane_length)]
        self.start_connector = None
        self.end_connector = None
        self.randomization = randomization

        self.renderer = LaneRender(self)

    def acceleration(self, cell):
        if cell is None:
            return None
        else:
            v = cell[0] + 1
            flag = cell[1]
            if flag is True:
                return cell
            if v > self.max_velocity:
                v = self.max_velocity
            return v, flag

    def slowing(self, cell, index):
        if cell is not None:
            v = cell[0]
            flag = cell[1]
            if flag is True:
                return cell
            collision, k = self.check_collision_next_cells(index, v)
            if collision:
                return v-1, flag
            else:
                return cell
        else:
            return None

    def random_slowing(self, cell):
        if cell is not None:
            if cell[0] > 0 and random.random() < 0.3:
                return cell[0]-1, cell[1]
            else:
                return cell
        else:
            return None

    def simulation_step(self):
        # acceleration
        self.cells = [self.acceleration(cell) for cell in self.cells]
        # slowing down
        self.cells = [self.slowing(cell, index) for index, cell in enumerate(self.cells)]
        # randomization
        if self.randomization:
            self.cells = [self.random_slowing(cell) for cell in self.cells]
        # car motion
        for i, cell in enumerate(self.cells):
            if cell is not None and cell[1] is False:
                v = cell[0]
                if v > 0:
                    j = (i + v)
                    if j < self.lane_length:
                        self.cells[j] = (cell[0], True)
                    else:
                        self.insert_cell(j, (cell[0], True))
                    self.cells[i] = None

    def clear_flags(self):
        self.cells = [(cell[0], False) if cell is not None else None for cell in self.cells]

    def get_first_cells(self, n):
        if n <= self.lane_length:
            return self.cells[0:n]
        else:
            if self.end_connector is not None:
                first_road = self.cells[0:n]
                remaining_length = n - self.lane_length
                second_road = self.end_connector.next_cells(remaining_length)
                return first_road + second_road
            else:
                return self.cells

    def check_collision_next_cells(self, start_index, length):
        i = start_index
        v = length
        for k in range(1, v + 1):
            if i + k < self.lane_length:
                if self.cells[i + k] is not None:
                    return True, k
            else:
                if self.end_connector.get_cell(i + k - self.lane_length) is not None:
                    return True, k
        return False, None

    def insert_cell(self, index, value):
        if index < self.lane_length:
            self.cells[index] = value
        else:
            if self.end_connector is not None:
                self.end_connector.insert_cell(index - self.lane_length, value)
