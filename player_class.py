import pygame

from GameObject_class import GameObject


class Player(GameObject):
    def __init__(self, group, animations, image_adr, size, cords,
                 speed_vector):
        super().__init__()
        self.size = size
        self.group = group
        self.animations = animations
        self.image_adr = image_adr
        self.cords = cords
        self.speed_vector = speed_vector

        self.bool_jump = False
        self.pomenal = False

        self.high_of_jump = 200

    def jump(self, tick):
        if not self.pomenal and self.rect.bottomleft[1] <= self.high_of_jump:
            self.pomenal = True
            self.speed_vector = -90
        elif self.pomenal and self.cords[1] >= self.rect.topleft:
            self.rect.move_ip(*self.cords)
            self.bool_jump = False
        elif not self.pomenal:
            self.speed_vector = 90

    def update(self, time, rotation=0):
        super().update(time, rotation)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.bool_jump = True
        if self.bool_jump:
            self.jump(time)





