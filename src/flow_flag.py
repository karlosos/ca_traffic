class flow_flag:
    def __init__(self, bbox):
        self.bbox = bbox
        self.entries = []
        self.exits = []
        self.total_entered = 0
        self.total_exit = 0

