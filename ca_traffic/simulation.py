from ca_traffic.lane import Lane
from ca_traffic.lane_terminator import Terminator
from ca_traffic.traffic_generator import Generator

if __name__ == '__main__':
    l1 = Lane(lane_length=5)
    l2 = Lane(lane_length=20)
    l1.cells[0] = (0, False)
    Lane.link_lanes(l1, l2)
    terminator = Terminator()
    Lane.link_lanes(l2, terminator)
    generator = Generator()
    Lane.link_lanes(generator, l1)

    objects = [generator, l1, l2, terminator]
    lanes = [l1, l2]

    for i in range(100):
        for object in objects:
            object.simulation_step()

        for lane in lanes:
            lane.clear_flags()

        for lane in lanes:
            lane.print()

        print('')