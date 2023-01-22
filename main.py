import pygame
from GameButton_class import GameButton


def start_screen(clock, screen):
    running = True

    def stop(*args, **kwargs):
        nonlocal running
        running = False

    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [['backgrounds', 'Background.png'],
                                          1, 1]}, (600, 900), (0, 0), stop)

    while running:
        tick = clock.tick(60) / 1000
        screen.fill('red')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        group.update(tick)
        group.draw(screen)
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((600, 900))
Clock = pygame.time.Clock()
pygame.display.flip()
start_screen(Clock, screen)
