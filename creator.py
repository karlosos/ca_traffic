import cv2
from Simulation import Simulation
from Vec2D import Vec2D
import numpy as np

if __name__ == "__main__":
    ###############################################################
    # Cross section X (2 lanes)
    ###############################################################
    mp = Simulation(100, 100, p=50)

    for cell in mp.cellmap[49, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in mp.cellmap[:, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in mp.cellmap[51, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in mp.cellmap[:, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    np.save("cross-section-X.npy", mp.cellmap)


    # mp.add_car(pos=Vec2D(49, 5))
    # mp.add_car(pos=Vec2D(49, 1), vel=2)
    # mp.add_car(pos=Vec2D(5, 51))

    # mp = Simulation(50, 50, p=50)

    # for cell in mp.cellmap[25, :]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(0, 1))
    #
    # for cell in mp.cellmap[:, 25]:
    #     cell.kind = "road"
    #     cell.direction.append(Vec2D(1, 0))
    #
    # mp.cellmap = np.load("cross-section.npy", allow_pickle=True)
    # mp.add_car(pos=Vec2D(25, 5))
    # mp.add_car(pos=Vec2D(25, 1), vel=2)
    # mp.add_car(pos=Vec2D(5, 25))
    #
    # mp.cellmap_outline_roads()
    # mp.initialize_map()
    # while True:
    #     mp.step()
    #     mp.print_map()
    #     k = cv2.waitKey(50)
    #     if k == 27:
    #         break


    ###############################################################
    # Cross section T up (2 lanes)
    ###############################################################
    T_up = Simulation(100, 100, p=50)

    for cell in T_up.cellmap[0, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in T_up.cellmap[1:, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in T_up.cellmap[2, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in T_up.cellmap[1:, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    np.save("cross-section-T-up.npy", T_up.cellmap)

    ###############################################################
    # Cross section T down (2 lanes)
    ###############################################################
    T_down = Simulation(100, 100, p=50)

    for cell in T_down.cellmap[97, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in T_down.cellmap[:99, 49]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in T_down.cellmap[99, :]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in T_down.cellmap[:99, 51]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    np.save("cross-section-T-down.npy", T_down.cellmap)

    ###############################################################
    # Cross section T left (2 lanes)
    ###############################################################
    T_left = Simulation(100, 100, p=50)

    for cell in T_left.cellmap[49, 1:]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in T_left.cellmap[:, 0]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in T_left.cellmap[51, 1:]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in T_left.cellmap[:, 2]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    np.save("cross-section-T-left.npy", T_left.cellmap)

    ###############################################################
    # Cross section T right (2 lanes)
    ###############################################################
    T_right = Simulation(100, 100, p=50)

    for cell in T_right.cellmap[49, :99]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, -1))

    for cell in T_right.cellmap[:, 97]:
        cell.kind = "road"
        cell.direction.append(Vec2D(1, 0))

    for cell in T_right.cellmap[51, :99]:
        cell.kind = "road"
        cell.direction.append(Vec2D(0, 1))

    for cell in T_right.cellmap[:, 99]:
        cell.kind = "road"
        cell.direction.append(Vec2D(-1, 0))

    np.save("cross-section-T-right.npy", T_right.cellmap)