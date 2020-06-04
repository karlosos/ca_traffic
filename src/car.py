from src.vec_2d import Vec2D


class Car:
    def __init__(self, velocity=1, position=Vec2D(), idx=-1):
        self.position = position
        self.velocity = velocity
        self.oldDirection = Vec2D()
        self.defaultvelocity = velocity
        self.idx = idx
        self.flag = False
