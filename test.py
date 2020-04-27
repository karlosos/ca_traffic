import cv2
from Simulation import Simulation
from Vec2D import Vec2D
import numpy as np

if __name__ == "__main__":
    # mp = Simulation(100, 100, p=50)
    #
    # for cell in mp.cellmap[49, :]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(0, -1))
    #
    # for cell in mp.cellmap[:, 49]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(1, 0))
    #
    # for cell in mp.cellmap[51, :]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(0, 1))
    #
    # for cell in mp.cellmap[:, 51]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(-1, 0))
    #
    # mp.add_car(pos=Vec2D(49, 5))
    # mp.add_car(pos=Vec2D(49, 1), vel=2)
    # mp.add_car(pos=Vec2D(5, 51))

    mp = Simulation(50, 50, p=50)

    # for cell in mp.cellmap[25, :]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(0, 1))
    #
    # for cell in mp.cellmap[:, 25]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(1, 0))
    #
    # np.save("cross-section.npy", mp.cellmap)
    mp.cellmap = np.load("cross-section.npy", allow_pickle=True)
    mp.add_car(pos=Vec2D(25, 5))
    mp.add_car(pos=Vec2D(25, 1), vel=2)
    mp.add_car(pos=Vec2D(5, 25))

    mp.cellmap_outline_roads()
    mp.initialize_map()
    while True:
        mp.step()
        mp.print_map()
        k = cv2.waitKey(50)
        if k == 27:
            break
