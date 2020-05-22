class Cell:
    def __init__(self, car=None, kind=None, direction=None):
        if direction is None:
            direction = []

        self.car = car
        self.kind = kind
        self.direction = direction
        self.visited = 0
        self.probability = None
