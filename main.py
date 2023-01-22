import pygame.sprite

from modul import *


def start_screen(clock, screen):
    running = True

    def stop(*args, **kwargs):
        running = False

    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [['backgrounds', 'Backgrounds.png'],
                                          1, 1]}, (600, 900), stop)

    while running:
        tick = clock.tick(60) / 1000
        screen.fill('red')

        for event in pygame.event.get():
            if event.type == pygame.quit():
                exit(0)

        group.update(tick)
        group.draw(screen)
        pygame.display.flip()
