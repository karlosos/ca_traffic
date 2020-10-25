import cv2
import numpy as np
from random import randrange, choice
import math
import seaborn as sns
import matplotlib.pyplot as plt
from copy import deepcopy

from src.car import Car
from src.cell import Cell
from src.vec_2d import Vec2D
from src.traffic_lights import TrafficLight, RED, GREEN, ORANGE


class Simulation:
    def __init__(
        self,
        sizeX,
        sizeY,
        p=50,
        starting_point=None,
        roadcolor=None,
        carcolor=None,
        sidecolor=None,
        nonecolor=None,
        slowcolor=None,
        prioritycolor=None
    ):
        if roadcolor is None:
            roadcolor = np.array([125, 125, 125], dtype=np.uint8)
        if carcolor is None:
            carcolor = np.array([0, 255, 0], dtype=np.uint8)
        if sidecolor is None:
            sidecolor = np.array([0, 0, 0], dtype=np.uint8)
        if nonecolor is None:
            nonecolor = np.array([255, 255, 255], dtype=np.uint8)
        if slowcolor is None:
            slowcolor = np.array([255, 0, 0], dtype=np.uint8)
        if prioritycolor is None:
            prioritycolor = np.array([150, 150, 90], dtype=np.uint8)
        self.cellmap = np.array(
            [list(Cell() for _ in range(sizeX)) for _ in range(sizeY)]
        )
        self.colormap = np.array(np.full([sizeY, sizeX, 3], 255), dtype=np.uint8)
        self.cars = []
        self.trafficLights = []
        self.probabilityOfTurn = p
        self.roadcolor = roadcolor
        self.carcolor = carcolor
        self.sidecolor = sidecolor
        self.nonecolor = nonecolor
        self.slowcolor = slowcolor
        self.prioritycolor = prioritycolor
        self.slow_cars = 0
        self.max_slow_cars = 0
        self.currentIteration = 0
        if starting_point is None:
            self.starting_point = []
        self.dt_string = ""
        self.car_distances = None

    def print_map(self, window):  # działa
        text = (
            "Global traffic jam: "
            + str(self.slow_cars)
            + ", "
            + "greatest global traffic jam: "
            + str(self.max_slow_cars)
        )
        windowWidth = cv2.getWindowImageRect(window)[2]
        windowHeight = cv2.getWindowImageRect(window)[3]
        image = cv2.resize(
            cv2.cvtColor(self.colormap, cv2.COLOR_BGR2RGB), (windowWidth, windowHeight)
        )
        cv2.putText(
            image,
            text,
            (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA,
        )
        cv2.imshow(window, image)

    def initialize_map(self):  # działa
        for row in range(self.cellmap.shape[0]):
            for col in range(self.cellmap.shape[1]):
                if self.cellmap[row, col].kind == "road":
                    if self.cellmap[row, col].car is not None:
                        self.colormap[row, col] = self.carcolor
                    elif self.cellmap[row, col].trafficLight is not None:
                        self.colormap[row, col] = self.cellmap[row, col].trafficLight.currentColor
                    else:
                        if self.cellmap[row, col].priority is False:
                            self.colormap[row, col] = self.roadcolor
                        else:
                            self.colormap[row, col] = self.prioritycolor
                elif (
                    self.cellmap[row, col].kind == "side"
                    and self.cellmap[row, col].trafficLight is None
                ):
                    self.colormap[row, col] = self.sidecolor
                elif self.cellmap[row, col].trafficLight is not None:
                    self.colormap[row, col] = np.array(
                        self.cellmap[row, col].trafficLight.currentColor, dtype=np.uint8
                    )

    def cellmap_outline_roads(self):  # działa
        for row in range(1, self.cellmap.shape[0] - 1):
            for col in range(1, self.cellmap.shape[1] - 1):
                if self.cellmap[row, col].kind == "road":
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if self.cellmap[row + i, col + j].kind is None:
                                self.cellmap[row + i, col + j].kind = "side"

    def add_car(self, pos=None, vel=1, idx=-1):
        if pos is None:
            pos = choice(self.starting_point)
        else:
            assert (
                0 <= pos.x < self.cellmap.shape[0]
                and 0 <= pos.y < self.cellmap.shape[1]
            ), "Invalid position"
            assert self.cellmap[pos.x, pos.y].kind == "road", "Position is not a road"
        assert 0 < vel < 5, "Invalid velocity"
        car = Car(position=pos, velocity=choice([1, 2, 3, 4]), idx=idx)
        self.cellmap[pos.x, pos.y].car = car
        self.cars.append(car)

    def step(self, cars_number):  # działa
        if self.car_distances is None:
            self.car_distances = [0] * cars_number
        self.currentIteration += 1
        toRemove = []
        self.slow_cars = 0
        [light.update(self.currentIteration) for light in self.trafficLights]
        for light in self.trafficLights:
            self.colormap[light.position.x, light.position.y] = np.array(
                light.currentColor, dtype=np.uint8
            )
        for car in self.cars:
            jumps = 0
            nextCellPos = car.position.add(car.oldDirection)
            potentialTrafficLightPosition = [
                    car.position.x + car.oldDirection.y,
                    car.position.y - car.oldDirection.x,
                ]
            if car.velocity == 0 and (
                (
                    self.cellmap[nextCellPos.x, nextCellPos.y].car is None
                    and car.flag is False
                )
                or (
                    car.flag is True
                    and self.cellmap[
                        potentialTrafficLightPosition[0],
                        potentialTrafficLightPosition[1],
                    ].trafficLight.currentColor
                    != RED
                )
            ):
                car.velocity = car.defaultvelocity
                car.flag = False
            for _ in range(car.velocity):
                nextCellPos = car.position.add(car.oldDirection)
                if abs(car.oldDirection.y) == 1:
                    potentialTrafficLightPosition = [
                        nextCellPos.x + car.oldDirection.y,
                        nextCellPos.y + car.oldDirection.x,
                    ]
                else:
                    potentialTrafficLightPosition = [
                        nextCellPos.x - car.oldDirection.y,
                        nextCellPos.y - car.oldDirection.x,
                    ]
                cell = self.cellmap[car.position.x, car.position.y]
                if (
                    self.cellmap[
                        potentialTrafficLightPosition[0],
                        potentialTrafficLightPosition[1],
                    ].trafficLight
                    is not None
                    and self.cellmap[
                        potentialTrafficLightPosition[0],
                        potentialTrafficLightPosition[1],
                    ].trafficLight.direction.equal(car.oldDirection)
                    and self.cellmap[
                        potentialTrafficLightPosition[0],
                        potentialTrafficLightPosition[1],
                    ].trafficLight.currentColor
                    == RED
                    and self.cellmap[nextCellPos.x, nextCellPos.y].car is None
                ):
                    cell.car = None
                    car.flag = True
                    car.velocity = 0
                    self.colormap[car.position.x, car.position.y] = self.roadcolor
                    car.position = nextCellPos
                    self.colormap[car.position.x, car.position.y] = self.slowcolor
                    self.cellmap[car.position.x, car.position.y].car = car
                    self.slow_cars += 1
                    if self.slow_cars > self.max_slow_cars:
                        self.max_slow_cars = self.slow_cars
                    break
                # początek reguł tutaj
                self.cellmap[car.position.x, car.position.y].visited += 1
                cell = self.cellmap[car.position.x, car.position.y]
                if (
                    all(dire.equal(Vec2D(0, 0)) for dire in cell.direction)
                    or cell.direction is None
                ):
                    self.colormap[car.position.x, car.position.y] = self.sidecolor
                    cell.car = None
                    toRemove.append(car)
                    break

                direction = car.oldDirection

                if len(cell.direction) == 1:
                    direction = cell.direction[0]

                elif len(cell.direction) == 2:
                    random = randrange(0, 100)
                    p = (
                        self.probabilityOfTurn
                        if cell.probability is None
                        else cell.probability
                    )
                    if random > p:
                        direction = cell.direction[0]
                    else:
                        direction = cell.direction[1]

                newpos = car.position.add(direction)

                if (
                    newpos.x < 0
                    or newpos.x >= self.cellmap.shape[0] - 1
                    or newpos.y < 0
                    or newpos.y >= self.cellmap.shape[1] - 1
                ):
                    cell.car = None
                    toRemove.append(car)
                    break

                try:
                    wrong = []
                    c = []
                    if len(self.cellmap[newpos.x, newpos.y].direction) == 1:
                        d = self.cellmap[newpos.x, newpos.y].direction[0]
                        if d.equal(Vec2D(-1, -1)) or d.equal(Vec2D(1, 1)):
                            c = [
                                Vec2D(newpos.x + 1, newpos.y - 1),
                                Vec2D(newpos.x - 1, newpos.y + 1),
                            ]
                            for v in c:
                                if (
                                    self.cellmap[v.x, v.y].kind != "road"
                                    or len(self.cellmap[v.x, v.y].direction) != 1
                                    or not self.cellmap[v.x, v.y].direction[0].equal(d)
                                ):
                                    wrong.append(v)
                        elif d.equal(Vec2D(0, -1)) or d.equal(Vec2D(0, 1)):
                            c = [
                                Vec2D(newpos.x + 1, newpos.y),
                                Vec2D(newpos.x - 1, newpos.y),
                            ]
                            for v in c:
                                if (
                                    self.cellmap[v.x, v.y].kind != "road"
                                    or len(self.cellmap[v.x, v.y].direction) != 1
                                    or not self.cellmap[v.x, v.y].direction[0].equal(d)
                                ):
                                    wrong.append(v)
                        elif d.equal(Vec2D(1, -1)) or d.equal(Vec2D(-1, 1)):
                            c = [
                                Vec2D(newpos.x - 1, newpos.y - 1),
                                Vec2D(newpos.x + 1, newpos.y + 1),
                            ]
                            for v in c:
                                if (
                                    self.cellmap[v.x, v.y].kind != "road"
                                    or len(self.cellmap[v.x, v.y].direction) != 1
                                    or not self.cellmap[v.x, v.y].direction[0].equal(d)
                                ):
                                    wrong.append(v)
                        elif d.equal(Vec2D(1, 0)) or d.equal(Vec2D(-1, 0)):
                            c = [
                                Vec2D(newpos.x, newpos.y - 1),
                                Vec2D(newpos.x, newpos.y + 1),
                            ]
                            for v in c:
                                if (
                                    self.cellmap[v.x, v.y].kind != "road"
                                    or len(self.cellmap[v.x, v.y].direction) != 1
                                    or not self.cellmap[v.x, v.y].direction[0].equal(d)
                                ):
                                    wrong.append(v)
                    for w in wrong:
                        c.remove(w)
                    if len(c) > 0:
                        r2 = randrange(0, 100)
                        if r2 < 10:
                            newpos = choice(c)
                except IndexError:
                    pass
                # here
                priorityflag = False
                if self.cellmap[car.position.x, car.position.y].priority is not True:
                    if self.cellmap[newpos.x, newpos.y].priority is True:
                        for dir in self.cellmap[newpos.x, newpos.y].direction:
                            currX = deepcopy(newpos.x) - dir.x
                            currY = deepcopy(newpos.y) - dir.y
                            for _ in range(4):
                                if self.cellmap[currX, currY].priority is False:
                                    break
                                elif self.cellmap[currX, currY].car is not None:
                                    priorityflag = True
                                    break
                                currX -= self.cellmap[currX, currY].direction[0].x
                                currY -= self.cellmap[currX, currY].direction[0].y
                if priorityflag is True:
                    self.colormap[car.position.x, car.position.y] = self.slowcolor
                    self.slow_cars += 1
                    cell.jammed += 1
                    if self.slow_cars > self.max_slow_cars:
                        self.max_slow_cars = self.slow_cars
                    break

                if self.cellmap[newpos.x, newpos.y].car is not None:
                    car.velocity = self.cellmap[newpos.x, newpos.y].car.velocity
                    self.colormap[car.position.x, car.position.y] = self.slowcolor
                    self.slow_cars += 1
                    cell.jammed += 1
                    if self.slow_cars > self.max_slow_cars:
                        self.max_slow_cars = self.slow_cars
                    break
                else:
                    car.velocity = car.defaultvelocity

                jumps += 1
                if self.cellmap[car.position.x, car.position.y].priority is False:
                    self.colormap[car.position.x, car.position.y] = self.roadcolor
                else:
                    self.colormap[car.position.x, car.position.y] = self.prioritycolor
                cell.car = None
                car.position = newpos

                self.colormap[car.position.x, car.position.y] = self.carcolor
                self.cellmap[car.position.x, car.position.y].car = car
                car.oldDirection = direction

            self.car_distances[car.idx] += jumps
            if self.currentIteration >= cars_number:
                file_handle_quiver = open(self.dt_string + "\\quiverdata.csv", "a")
                file_handle_quiver.write(
                    str(car.idx * 4 + self.car_distances[car.idx])
                    + ","
                    + str(self.currentIteration)
                    + ","
                    + str(car.oldDirection.x)
                    + ","
                    + str(car.oldDirection.y)
                    + "\n"
                )
                file_handle_quiver.close()
            if car.idx != -1:
                file_handle = open(
                    self.dt_string + "\\car" + str(car.idx) + ".csv", "a"
                )  # append only write mode
                file_handle.write(str(jumps) + ", ")
                file_handle.close()

        for cartoremove in toRemove:
            self.cars.remove(cartoremove)

    def find_starting_point(self):  # działa
        self.starting_point = []
        for x in range(self.cellmap.shape[0]):
            for y in range(self.cellmap.shape[1]):
                if self.cellmap[x, y].kind == "road":
                    if len(self.cellmap[x, y].direction) == 1:
                        newPos = Vec2D(x, y).add(
                            self.cellmap[x, y].direction[0].mul_int(-1)
                        )
                        if (
                            0 > newPos.x > self.cellmap.shape[0]
                            or 0 > newPos.y > self.cellmap.shape[1]
                        ):
                            continue
                        else:
                            if self.cellmap[newPos.x, newPos.y].kind != "road":
                                self.starting_point.append(Vec2D(x, y))
        to_remove = []
        for pos in self.starting_point:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    cell = self.cellmap[pos.x + i, pos.y + j]
                    if any(
                        Vec2D(pos.x + i + dire.x, pos.y + j + dire.y).equal(pos)
                        for dire in cell.direction
                    ):
                        to_remove.append(pos)
        for pos in to_remove:
            self.starting_point.remove(pos)

    def print_heatmap(self, axes):
        heatmap_accessed = np.zeros_like(self.cellmap, dtype=np.uint16)
        heatmap_jammed = np.zeros_like(self.cellmap, dtype=np.uint16)
        for x in range(heatmap_accessed.shape[0]):
            for y in range(heatmap_accessed.shape[1]):
                heatmap_accessed[x, y] = self.cellmap[x, y].visited
                heatmap_jammed[x, y] = self.cellmap[x, y].jammed
        # plt.figure()
        # plt.subplot(121)
        axes[0, 0] = axes[0, 0].imshow(
            X=np.array(self.colormap, dtype=np.uint8), aspect="auto"
        )
        # plt.subplot(122)
        sns.heatmap(heatmap_accessed, ax=axes[0, 1])
        sns.heatmap(heatmap_jammed, ax=axes[1, 1])
        # plt.show()
