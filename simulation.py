from ca_traffic.lane import Lane
from ca_traffic.lane_terminator import Terminator
from ca_traffic.traffic_generator import Generator
from ca_traffic.gui.display import Display
import pygame

if __name__ == '__main__':
    display = Display()
    clock = pygame.time.Clock()

    # Definiowanie systemu dróg
    l1 = Lane(lane_length=5)
    l1.renderer.x = 10  # pozycja drogi na ekranie
    l1.renderer.y = 10

    l2 = Lane(lane_length=15, max_velocity=3)
    l2.renderer.x = 15
    l2.renderer.y = 10

    l3 = Lane(lane_length=15, max_velocity=2)
    l3.renderer.x = 30
    l3.renderer.y = 10
    l3.renderer.rotate = -90

    l4 = Lane(lane_length=50, max_velocity=5)
    l4.renderer.x = 30
    l4.renderer.y = 25

    l5 = Lane(lane_length=5, max_velocity=1)
    l5.renderer.x = 80
    l5.renderer.y = 25

    l6 = Lane(lane_length=20, max_velocity=5)
    l6.renderer.x = 85
    l6.renderer.y = 25


    # Połączenie dróg ze sobą
    Lane.link_lanes(l1, l2)
    Lane.link_lanes(l2, l3)
    Lane.link_lanes(l3, l4)
    Lane.link_lanes(l4, l5)
    Lane.link_lanes(l5, l6)

    # Stworzenie generatora i podłączenie go do pierwszej drogi
    generator = Generator(probability=1)
    generator.renderer.x = 9
    generator.renderer.y = 10
    Lane.link_lanes(generator, l1)

    # Stworzenie terminatora, który kończy drogę
    terminator = Terminator()
    Lane.link_lanes(l6, terminator)

    simulation_objects = [generator, l1, l2, l3, l4, l5, l6, terminator]
    renderers = [l1.renderer, l2.renderer, l3.renderer, l4.renderer, l5.renderer, l6.renderer, generator.renderer]

    running = True
    while running:
        dt = clock.tick(5)
        running = display.input_events()

        for simulation_object in simulation_objects:
            simulation_object.simulation_step()

        for simulation_object in simulation_objects:
            if isinstance(simulation_object, Lane):
                simulation_object.clear_flags()

        display.render(renderers)
