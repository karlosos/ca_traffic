from ca_traffic.abstract_lane import AbstractLane
import random


class Generator(AbstractLane):
    def __init__(self, probability=0.3, max_velocity=5):
        super().__init__()
        self.start_connector = None
        self.end_connector = None
        self.probability = probability
        self.max_velocity = max_velocity

    def get_first_cells(self, n):
        return [None for i in range(n)]

    def insert_cell(self, index, value):
        pass

    def simulation_step(self):
        if random.random() < self.probability and self.end_connector is not None:
            v = random.randrange(0, self.max_velocity)
            self.end_connector.insert_cell(index=0, value=(v, True))
