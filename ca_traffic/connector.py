class Connector:
    def __init__(self, end_lane=None):
        self.end_lane = end_lane

    def next_cells(self, n):
        return self.end_lane.get_first_cells(n)

    def get_cell(self, index):
        return self.end_lane.get_first_cells(index+1)[-1]

    def insert_cell(self, index, value):
        self.end_lane.insert_cell(index, value)
