import pygame


class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode((1380, 600))
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption('Traffic Simulation')

    def input_events(self):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        return running

    def render(self, render_objects):
        background = pygame.Surface(self.screen.get_size())
        background.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))
        for render_object in render_objects:
            render_object.render(self.screen)
        pygame.display.flip()
