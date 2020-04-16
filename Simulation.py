import cv2
from car import Car
import numpy as np
from resizer import fit
from random import randrange
from Cell import Cell


class Simulation:
    def __init__(self, sizeX, sizeY, p=15, roadcolor=None, carcolor=None, sidecolor=None, nonecolor=None, slowcolor=None):
        if roadcolor is None:
            roadcolor = [125, 125, 125]
        if carcolor is None:
            carcolor = [0, 255, 0]
        if sidecolor is None:
            sidecolor = [0, 0, 0]
        if nonecolor is None:
            nonecolor = [255, 255, 255]
        if slowcolor is None:
            slowcolor = [255, 0, 0]
        self.cellmap = np.array([list(Cell() for i in range(sizeX)) for j in range(sizeY)])
        self.colormap = np.array(np.full([sizeY, sizeX, 3], 255), dtype=np.uint8)
        self.cars = []
        self.probabilityOfTurn = p
        self.roadcolor = roadcolor
        self.carcolor = carcolor
        self.sidecolor = sidecolor
        self.nonecolor = nonecolor
        self.slowcolor = slowcolor

    def print_map(self):
        image = cv2.cvtColor(self.colormap, cv2.COLOR_BGR2RGB)
        f = fit(image, 1280, 960)
        cv2.imshow("Map", f)

    def initialize_map(self):
        for row in range(self.cellmap.shape[0]):
            for col in range(self.cellmap.shape[1]):
                if self.cellmap[row, col].kind == "road":
                    if self.cellmap[row, col].car is not None:
                        self.colormap[row, col] = self.carcolor
                    else:
                        self.colormap[row, col] = self.roadcolor
                elif self.cellmap[row, col].kind == "side":
                    self.colormap[row, col] = self.sidecolor

    def cellmap_outline_roads(self):
        for row in range(1, self.cellmap.shape[0] - 1):
            for col in range(1, self.cellmap.shape[1] - 1):
                if self.cellmap[row, col].kind == "road":
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if self.cellmap[row + i, col + j].kind is None:
                                self.cellmap[row + i, col + j].kind = "side"

    def add_car(self, pos, vel=1):
        assert 0 <= pos.x < self.cellmap.shape[0] and 0 <= pos.y < self.cellmap.shape[1], "Invalid position"
        assert self.cellmap[pos.x, pos.y].kind == "road", "Position is not a road"
        assert 0 < vel < 5, "Invalid velocity"
        car = Car(position=pos, velocity=vel)
        self.cellmap[pos.x, pos.y].car = car
        self.cars.append(car)

    def step(self):
        for car in self.cars:
            for i in range(car.velocity):
                cell = self.cellmap[car.position.x, car.position.y]
                self.colormap[car.position.x, car.position.y] = self.roadcolor
                cell.car = None
                direction = car.oldDirection

                if len(cell.direction) == 1:
                    direction = cell.direction[0]

                elif len(cell.direction) == 2:
                    random = randrange(0, 100)
                    if random > self.probabilityOfTurn:
                        direction = cell.direction[0] if cell.direction[0].equal(car.oldDirection) else cell.direction[1]
                    else:
                        direction = cell.direction[0] if not cell.direction[0].equal(car.oldDirection) else cell.direction[1]

                newpos = car.position.add(direction)

                if newpos.x < 0:
                    newpos.x = self.cellmap.shape[0] - 1 + car.position.x
                elif newpos.x >= self.cellmap.shape[0] - 1:
                    newpos.x -= self.cellmap.shape[0] - 1
                if newpos.y < 0:
                    newpos.y = self.cellmap.shape[1] - 1 + car.position.y
                elif newpos.y >= self.cellmap.shape[1] - 1:
                    newpos.y -= self.cellmap.shape[1] - 1

                if self.cellmap[newpos.x, newpos.y].car is not None:
                    car.velocity = self.cellmap[newpos.x, newpos.y].car.velocity
                    self.colormap[car.position.x, car.position.y] = self.slowcolor
                    break
                else:
                    car.velocity = car.defaultvelocity

                car.position = newpos

                self.colormap[car.position.x, car.position.y] = self.carcolor
                self.cellmap[car.position.x, car.position.y].car = car
                car.oldDirection = direction



