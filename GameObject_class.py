import os
from math import cos, sin, pi

import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, group, animations, size, cords, speed_vector):
        super().__init__(group)
        self.frames = []
        self.not_stop = False
        self.frame_count = 1
        self.cords = cords
        self.size = size
        self.animations = animations
        self.animate('start', True)
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=cords)
        self.init_vector(speed_vector)

    def move_na(self, x, y):
        self.rect.move_ip(x, y)

    def image_con(self, image_adr):
        adr = os.path.join('data', 'texture', *image_adr)
        return pygame.image.load(adr)

    def init_vector(self, speed_vector):
        self.speed_x, self.speed_y = speed_vector[1] * cos(speed_vector[0] * pi / 180), \
                                     speed_vector[1] * sin(speed_vector[0] * pi / 180)

    def update(self, time):
        self.rect.move_ip(self.speed_x * time, self.speed_y * time)
        self.image = self.frames[self.frame_count - 1]
        if self.not_stop:
            self.frame_count = (self.frame_count + 1) % len(self.frames)
        elif self.frame_count == len(self.frames):
            self.frame_count = 1
            self.animate('start', True)
        else:
            self.frame_count += 1

    def animate(self, key, not_stop=False):
        if not_stop:
            self.not_stop = True
        else:
            self.not_stop = False
        self.frames = []
        image, row, col = self.animations[key]
        image = self.image_con(image)
        w, h = image.get_size()[0] // col, image.get_size()[1] // row
        for i in range(row):
            for j in range(col):
                sup = pygame.Surface((w, h))
                sup.blit(image, (0, 0), (w * j, h * i, w, h))
                self.frames.append(sup.convert())


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    clock = pygame.time.Clock()
    running = True
    group = pygame.sprite.Group()
    sprite = GameObject(group, {'start': [['pygame-8-1.png'], 2, 8]},
                        [50, 50], [50, 200], [0, 0])
    while running:
        screen.fill((255, 255, 255))
        tick = clock.tick(10) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.draw(screen)
        group.update(tick)
        pygame.display.flip()
    pygame.quit()
