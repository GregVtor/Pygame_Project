import os
from math import cos, sin, pi

import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, group, animations, size, cords, speed_vector):
        super().__init__(group)
        self.size = size
        self.image = self.image(animations)
        self.speed_x, self.speed_y = speed_vector[1] * cos(speed_vector[0] * pi / 180), \
                                     speed_vector[1] * sin(speed_vector[0] * pi / 180)
        self.rect = self.image.get_rect(topleft=cords)
        self.animations = animations

    def image(self, image_adr):
        adr = os.path.join('data', 'texture', *image_adr)
        img = pygame.image.load(adr)
        img = pygame.transform.scale(img, self.size)
        return img

    def update(self, time, rotation=0):
        self.rect.move_ip(self.speed_x * time, self.speed_y * time)

    def animate(self, key): ...


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    clock = pygame.time.Clock()
    running = True
    group = pygame.sprite.Group()
    sprite = GameObject(group, ['Player', 'deadpool.png'], [300, 350], [50, 200], [0, 0])
    while running:
        screen.fill((255, 255, 255))
        tick = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.draw(screen)
        group.update(tick)
        pygame.display.flip()
    pygame.quit()
