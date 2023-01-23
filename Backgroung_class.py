from GameObject_class import GameObject


class Backgroung(GameObject):
    def __init__(self, group, animations, size, cords, speed_vector):
        super().__init__(group, animations, size, cords, speed_vector)
        self.screen_width = 600

    def update(self, time):
        super().update(time)
        if self.rect.topright[0] <= self.screen_width:
            self.rect.move(self.screen_width, 0)
