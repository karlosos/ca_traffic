import pygame
from ca_traffic.gui import constants


class GeneratorRenderer:
    def __init__(self, generator):
        self.x = 0
        self.y = 0
        self.generator = generator

    def render(self, screen):
        cell_size = constants.cell_size
        is_on = self.generator.is_on
        surface_size = (cell_size, cell_size)
        surface = pygame.Surface(surface_size)
        pygame.draw.rect(surface, (100, 100, 200), (0, 0, cell_size, cell_size))
        if is_on:
            pygame.draw.rect(surface, (255, 255, 255), (0, 0, cell_size, cell_size))
        screen.blit(surface, (self.x*cell_size, self.y*cell_size))
