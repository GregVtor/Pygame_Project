import pygame.sprite

from modul import *


def start_screen(clock, screen):
    running = True
    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [[]]})



    def stop():
        running = False


    while running:
        pass