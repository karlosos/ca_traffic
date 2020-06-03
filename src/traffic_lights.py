import math
from src.vec_2d import Vec2D

RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)


class TrafficLigth:
    def __init__(self, N=7, offset=0, position=Vec2D()):
        self.N = N
        self.offset = offset
        self.currentColor = None
        self.position = position
        if self.offset % self.N < math.ceil(3 * self.N / 7):
            self.currentColor = GREEN
        elif self.offset % self.N < math.ceil(4 * self.N / 7):
            self.currentColor = ORANGE
        else:
            self.currentColor = RED

    def update(self, iteration):
        if (iteration + self.offset) % self.N < math.ceil(3 * self.N / 7):
            self.currentColor = GREEN
        elif (iteration + self.offset) % self.N < math.ceil(4 * self.N / 7):
            self.currentColor = ORANGE
        else:
            self.currentColor = RED
