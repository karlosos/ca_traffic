from ca_traffic.abstract_lane import AbstractLane
import random
from ca_traffic.gui.generator_renderer import GeneratorRenderer


class Generator(AbstractLane):
    def __init__(self, probability=0.3, max_velocity=5):
        super().__init__()
        self.start_connector = None
        self.end_connector = None
        self.probability = probability
        self.max_velocity = max_velocity
        self.is_on = False
        self.renderer = GeneratorRenderer(self)

    def get_first_cells(self, n):
        return [None for i in range(n)]

    def insert_cell(self, index, value):
        pass

    def simulation_step(self):
        self.is_on = False
        if random.random() < self.probability and self.end_connector is not None:
            if self.end_connector.get_cell(0) is None:
                v = random.randrange(0, self.max_velocity)
                self.end_connector.insert_cell(index=0, value=(v, True))
                self.is_on = True
