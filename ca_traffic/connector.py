class Connector:
    def __init__(self, end_lane=None):
        self.end_lane = end_lane

    def next_cells(self, n):
        return self.end_lane.get_first_cells(n)

    def insert_cell(self, index, value):
        self.end_lane.insert_cell(index, value)
