from ca_traffic.abstract_lane import AbstractLane


class Terminator(AbstractLane):
    def __init__(self):
        super().__init__()
        self.start_connector = None
        self.end_connector = None

    def get_first_cells(self, n):
        return [None for i in range(n)]

    def insert_cell(self, index, value):
        pass

    def simulation_step(self):
        pass