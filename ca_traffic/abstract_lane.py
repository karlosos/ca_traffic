from abc import ABC, abstractmethod
from ca_traffic.connector import Connector


class AbstractLane(ABC):
    def __init__(self):
        self.start_connector = None
        self.end_connector = None

    @abstractmethod
    def get_first_cells(self, n):
        pass

    @abstractmethod
    def insert_cell(self, index, value):
        pass

    @classmethod
    def link_lanes(cls, lane_a, lane_b):
        lane_a.end_connector = Connector()
        lane_a.end_connector.end_lane = lane_b
        lane_b.start_connector = lane_a.end_connector
