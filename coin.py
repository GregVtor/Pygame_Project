from GameObject_class import GameObject


class Coin(GameObject):
    def __init__(self, group, animations, cords, player, func_add):
        super().__init__(group, animations, (35, 35), cords, (180, 200))
        self.player = player
        self.func_add = func_add

    def update(self, tick):
        super().update(tick)
        if self.rect.colliderect(self.player):
            self.func_add()
            self.kill()
        if self.rect.topright[0] <= 0:
            self.kill()
            
