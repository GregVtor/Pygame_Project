import pygame
from GameObject_class import GameObject


class GameButton(GameObject):
    def __init__(self, group, image_adr, size, cords, func, *args, **kwargs):
        super().__init__(group, image_adr, size, cords, [0, 0])
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def clicked(self):
        self.func(self.args, self.kwargs)
