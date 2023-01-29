from GameObject_class import GameObject
import pygame


class Coin(GameObject):
    def __init__(self, group, animations, cords, vector, player, func_add):
        super().__init__(group, animations, (35, 35), cords, vector)
        self.player = player
        self.func_add = func_add

    def update(self, tick):
        super().update(tick)
        if pygame.sprite.collide_mask(self, self.player):
            self.func_add()
            self.kill()
        if self.rect.topright[0] <= 0:
            self.kill()
            
