class Vec2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, vec):
        x = self.x + vec.x
        y = self.y + vec.y
        return Vec2D(x, y)

    def mul(self, vec):
        x = self.x * vec.x
        y = self.y * vec.y
        return Vec2D(x, y)

    def mul_int(self, i):
        x = self.x * i
        y = self.y * i
        return Vec2D(x, y)

    def equal(self, vec):
        if self.x == vec.x and self.y == vec.y:
            return True
        else:
            return False

    def perpendicular_clockwise(self):
        return Vec2D(self.y, -self.x)

    def perpendicular_counterclockwise(self):
        return Vec2D(-self.y, self.x)
