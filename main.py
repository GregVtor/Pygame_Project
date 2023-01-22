import pygame
import os
from GameButton_class import GameButton


def font_adr(name):
    return os.path.join('data', 'fonts', name)


def start_screen(clock, screen):
    running = True

    def stop(*args, **kwargs):
        nonlocal running
        running = False

    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [['backgrounds', 'Background.png'],
                                          1, 1]}, (600, 900), (0, 0), stop)
    font = pygame.font.Font(font_adr('Pixel Times.ttf'), 30)
    text = font.render('Начать игру', False, 'red')
    while running:
        tick = clock.tick(60) / 1000
        screen.fill('red')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        group.update(tick)
        group.draw(screen)
        screen.blit(text, (230, 400))
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((600, 900))
Clock = pygame.time.Clock()
pygame.display.flip()
start_screen(Clock, screen)
