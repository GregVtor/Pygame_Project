import pygame
import os
from math import cos, sin


class GameObject(pygame.sprite.Sprite):
    def __init__(self, group, image_adr, size, cords, speed_vector):
        super().__init__(group)
        self.size = size
        self.cords = cords
        self.image = self.image(image_adr)
        self.speed_x, self.speed_y = speed_vector[1] * cos(speed_vector[0]), speed_vector[1] * sin(speed_vector[0])
        self.rect = self.image.get_rect(topleft=cords)

    def image(self, image_adr):
        adr = os.path.join('data', 'texture', *image_adr)
        img = pygame.image.load(adr)
        img = pygame.transform.scale(img, self.size)
        return img

    def update(self, time, rotation=0):
        self.image = pygame.transform.rotate(self.image, rotation * time)
        self.rect = self.rect = self.image.get_rect(topleft=self.cords)
        self.rect.move(self.speed_x * time, self.speed_y * time)
        self.cords = [self.cords[0] + self.speed_x * time, self.cords[1] + self.speed_y * time]


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    clock = pygame.time.Clock()
    running = True
    group = pygame.sprite.Group()
    sprite = GameObject(group, ['Player', 'deadpool.png'], [300, 350], [50, 200], [-45, 100])
    while running:
        screen.fill((255, 255, 255))
        tick = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.draw(screen)
        group.update(tick)
        pygame.display.flip()
    pygame.quit()