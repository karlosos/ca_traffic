import cv2

from Lights import Lights
from car import Car
import numpy as np
from resizer import fit
from random import randrange
from Cell import Cell
from Vec2D import Vec2D


class Simulation:
    def __init__(self, sizeX, sizeY, p=15, starting_point=None, roadcolor=None, carcolor=None, sidecolor=None, nonecolor=None, slowcolor=None, lightcolor=None):
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
        if lightcolor is None:
            lightcolor = [255, 255, 0]
        self.lightmap = []
        self.cellmap = np.array([list(Cell() for _ in range(sizeX)) for _ in range(sizeY)])
        self.colormap = np.array(np.full([sizeY, sizeX, 3], 255), dtype=np.uint8)
        self.cars = []
        self.probabilityOfTurn = p
        self.lightcolor = lightcolor
        self.roadcolor = roadcolor
        self.carcolor = carcolor
        self.sidecolor = sidecolor
        self.nonecolor = nonecolor
        self.slowcolor = slowcolor
        self.starting_point = starting_point

    def print_map(self, window):  # działa
        image = cv2.cvtColor(self.colormap, cv2.COLOR_BGR2RGB)
        cv2.imshow(window, image)

    def initialize_map(self):  # działa
        tmpcounter = 14
        for row in range(self.cellmap.shape[0]):
            for col in range(self.cellmap.shape[1]):
                if self.cellmap[row, col].kind == "road":
                    if self.cellmap[row, col].car is not None:
                        self.colormap[row, col] = self.carcolor
                    else:
                        self.colormap[row, col] = self.roadcolor
                elif self.cellmap[row, col].kind == "side":
                    self.colormap[row, col] = self.sidecolor
                elif self.cellmap[row, col].kind == "light":
                    light = Lights(row=row, col=col, state=tmpcounter)
                    tmpcounter += 14
                    self.lightmap.append(light)
                    # self.colormap[row, col] = self.lightcolor

    def cellmap_outline_roads(self):  # działa
        for row in range(1, self.cellmap.shape[0] - 1):
            for col in range(1, self.cellmap.shape[1] - 1):
                if self.cellmap[row, col].kind == "road":
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if self.cellmap[row + i, col + j].kind is None:
                                self.cellmap[row + i, col + j].kind = "side"

    def add_car(self, pos=None, vel=1):
        if pos is None:
            pos = self.starting_point
        else:
            assert 0 <= pos.x < self.cellmap.shape[0] and 0 <= pos.y < self.cellmap.shape[1], "Invalid position"
            assert self.cellmap[pos.x, pos.y].kind == "road", "Position is not a road"
        assert 0 < vel < 5, "Invalid velocity"
        car = Car(position=pos, velocity=vel)
        self.cellmap[pos.x, pos.y].car = car
        self.cars.append(car)

    def step(self):  # działa
        toRemove = []
        for car in self.cars:
            for i in range(car.velocity):

                # początek reguł tutaj
                cell = self.cellmap[car.position.x, car.position.y]
                if all(dire.equal(Vec2D(0, 0)) for dire in cell.direction) or cell.direction is None:
                    self.colormap[car.position.x, car.position.y] = self.sidecolor
                    cell.car = None
                    toRemove.append(car)
                    break

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

                if newpos.x < 0 or newpos.x >= self.cellmap.shape[0] - 1 or newpos.y < 0 \
                        or newpos.y >= self.cellmap.shape[1] - 1:
                    cell.car = None
                    toRemove.append(car)
                    break

                if self.cellmap[newpos.x, newpos.y].car is not None:
                    car.velocity = self.cellmap[newpos.x, newpos.y].car.velocity
                    self.colormap[car.position.x, car.position.y] = self.slowcolor
                    break
                else:
                    car.velocity = car.defaultvelocity

                self.colormap[car.position.x, car.position.y] = self.roadcolor
                cell.car = None
                car.position = newpos

                self.colormap[car.position.x, car.position.y] = self.carcolor
                self.cellmap[car.position.x, car.position.y].car = car
                car.oldDirection = direction
        self.change_light()
        for cartoremove in toRemove:
            self.cars.remove(cartoremove)

    def change_light(self):
        for light in self.lightmap:
            light.state += 1;
            light.state %= 30;

            if 0 <= light.state < 14:
                light.color = [255, 0, 0]
            if 14 <= light.state <= 17:
                light.color = [255, 165, 0]
            if 17 < light.state <= 30:
                light.color = [0, 255, 0]

            self.colormap[light.row, light.col] = light.color


    def find_starting_point(self):  # działa
        for y in range(int(self.cellmap.shape[1]/2)):
            for x in range(self.cellmap.shape[0]):
                for direc in self.cellmap[x, y].direction:
                    if direc.equal(Vec2D(0, 1)) and self.cellmap[x, y].kind == "road":
                        self.starting_point = Vec2D(x, y)
                        return
                for direc in self.cellmap[x, -y].direction:
                    if direc.equal(Vec2D(0, -1)) and self.cellmap[x, -y].kind == "road":
                        self.starting_point = Vec2D(x, -y)
                        return




