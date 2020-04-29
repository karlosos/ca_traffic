import pygame
from ca_traffic.gui import constants


class LaneRender:
    def __init__(self, lane):
        self.x = 0
        self.y = 0
        self.lane = lane
        self.rotate = None

    def render(self, screen):
        cell_size = constants.cell_size
        cells = self.lane.cells
        lane_length = len(cells)
        surface_size = (cell_size*lane_length, cell_size)
        surface = pygame.Surface(surface_size)
        pygame.draw.rect(surface, (100, 100, 100), (0, 0, cell_size*lane_length, cell_size))
        for i in range(lane_length):
            if cells[i] is not None:
                cell_size = constants.cell_size
                x = cell_size * i
                pygame.draw.rect(surface, (250, 100, 100), (x, 0 * cell_size, cell_size, cell_size))

        if self.rotate is not None:
            surface = pygame.transform.rotate(surface, self.rotate)
        screen.blit(surface, (self.x*cell_size, self.y*cell_size))
