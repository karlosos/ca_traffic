from Vec2D import Vec2D


class Car:
    def __init__(self, velocity=1, position=Vec2D()):
        self.position = position
        self.velocity = velocity
        self.oldDirection = Vec2D()
        self.defaultvelocity = velocity
